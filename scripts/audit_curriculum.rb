#!/usr/bin/env ruby

require 'yaml'
require 'json'
require 'pathname'

ROOT = Pathname(__dir__).join('..').expand_path
CONTENTS = ROOT.join('contents')
MANIFEST_PATH = ROOT.join('scripts', 'vi_curriculum_manifest.json')
VISIBLE_CHAPTERS = %w[01 02 03 04 05 06 07 08].freeze
LANGS = %w[en vi].freeze
MANIFEST = JSON.parse(MANIFEST_PATH.read)
EXPECTED_CHAPTER_SEQUENCES = MANIFEST.fetch('chapter_sequences')
EXPECTED_VI_REQUIRED_LESSONS = MANIFEST.fetch('required_lessons')

Issue = Struct.new(:type, :message)

def load_front_matter(path)
  text = path.read
  return {} unless text.start_with?("---\n")

  YAML.safe_load(text.split("---\n", 3)[1]) || {}
end

issues = []
visible_posts = []

LANGS.each do |lang|
  VISIBLE_CHAPTERS.each do |chapter|
    index_path = CONTENTS.join(lang, "chapter#{chapter}", "index.html")
    unless index_path.exist?
      issues << Issue.new(:missing_index, "Missing chapter index: #{index_path.relative_path_from(ROOT)}")
      next
    end

    expected_sequence = EXPECTED_CHAPTER_SEQUENCES.fetch(lang).fetch(chapter)
    actual_sequence = load_front_matter(index_path)['sequence']
    next if actual_sequence == expected_sequence

    issues << Issue.new(
      :chapter_sequence,
      "Unexpected chapter sequence for #{lang}/chapter#{chapter}: expected #{expected_sequence}, got #{actual_sequence.inspect}"
    )
  end
end

Dir.glob(CONTENTS.join('*', 'chapter*', '_posts', '*.md').to_s).sort.each do |file|
  path = Pathname(file)
  data = load_front_matter(path)
  next if data.empty? || data['hidden']

  path_chapter = path.each_filename.find { |segment| segment.start_with?('chapter') }

  visible_posts << {
    path: path,
    basename: path.basename.to_s,
    lang: data['lang'],
    chapter: data['chapter'].to_s,
    path_chapter: path_chapter.to_s.sub('chapter', ''),
    order: data['order'],
    lesson_type: data['lesson_type'],
    title: data['title'].to_s
  }
end

core_groups = visible_posts
              .select { |post| post[:lesson_type] == 'required' && VISIBLE_CHAPTERS.include?(post[:chapter]) }
              .group_by { |post| [post[:lang], post[:chapter]] }

core_groups.each do |(lang, chapter), posts|
  orders = posts.map { |post| post[:order] }.compact.sort
  duplicates = orders.group_by(&:itself).select { |_, group| group.size > 1 }.keys
  duplicates.each do |order|
    issues << Issue.new(:duplicate_order, "Duplicate required order #{order} for #{lang}/chapter#{chapter}")
  end

  next if orders.empty?

  missing = (orders.min..orders.max).to_a - orders
  next if missing.empty?

  issues << Issue.new(:order_gap, "Required order gap in #{lang}/chapter#{chapter}: missing #{missing.join(', ')}")
end

chapter00_visible = visible_posts.select { |post| post[:chapter] == '00' }
chapter00_visible.each do |post|
  issues << Issue.new(:age_scope, "Visible chapter00 post should be archived: #{post[:path].relative_path_from(ROOT)}")
end

advanced_keywords = /continuity|uniform continuity|lipschitz/i
visible_posts.each do |post|
  next unless advanced_keywords.match?(post[:title])

  issues << Issue.new(:age_scope, "Advanced learner-facing content detected: #{post[:path].relative_path_from(ROOT)}")
end

visible_posts
  .select { |post| post[:lang] == 'vi' && post[:lesson_type] == 'required' && VISIBLE_CHAPTERS.include?(post[:chapter]) }
  .each do |post|
    expected_chapter = EXPECTED_VI_REQUIRED_LESSONS[post[:basename]]

    if expected_chapter.nil?
      issues << Issue.new(
        :unexpected_required_lesson,
        "Visible required Vietnamese lesson is missing from the canonical manifest: #{post[:path].relative_path_from(ROOT)}"
      )
      next
    end

    if post[:chapter] != expected_chapter
      issues << Issue.new(
        :curriculum_scope,
        "Visible required Vietnamese lesson is under chapter#{post[:chapter]} but canonical chapter is #{expected_chapter}: #{post[:path].relative_path_from(ROOT)}"
      )
    end

    next if post[:path_chapter] == post[:chapter]

    issues << Issue.new(
      :path_metadata_mismatch,
      "Visible required Vietnamese lesson path and front matter chapter disagree: #{post[:path].relative_path_from(ROOT)}"
    )
  end

visible_required_basenames = visible_posts
                             .select { |post| post[:lang] == 'vi' && post[:lesson_type] == 'required' && VISIBLE_CHAPTERS.include?(post[:chapter]) }
                             .map { |post| post[:basename] }

(EXPECTED_VI_REQUIRED_LESSONS.keys - visible_required_basenames).sort.each do |basename|
  issues << Issue.new(
    :missing_required_lesson,
    "Canonical Vietnamese required lesson is missing or hidden: #{basename}"
  )
end

vi_required = visible_posts
              .select { |post| post[:lang] == 'vi' && post[:lesson_type] == 'required' && VISIBLE_CHAPTERS.include?(post[:chapter]) }
              .group_by { |post| [post[:chapter], post[:order]] }

en_required = visible_posts
              .select { |post| post[:lang] == 'en' && post[:lesson_type] == 'required' && VISIBLE_CHAPTERS.include?(post[:chapter]) }
              .group_by { |post| [post[:chapter], post[:order]] }

missing_en = vi_required.keys.reject { |key| en_required.key?(key) }.sort

puts "Curriculum audit report"
puts "======================="
puts

if issues.empty?
  puts "Structural checks: OK"
else
  puts "Structural checks: FAILED"
  issues.each do |issue|
    puts "- #{issue.message}"
  end
end

puts
puts "Parity report (VI required lessons missing EN counterpart): #{missing_en.size}"
missing_en.each do |chapter, order|
  source_post = vi_required[[chapter, order]].first
  puts "- chapter#{chapter} order #{order}: #{source_post[:title]}"
end

exit(issues.empty? ? 0 : 1)
