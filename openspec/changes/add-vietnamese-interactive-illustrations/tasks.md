## 1. Discovery and mapping
- [x] 1.1 Inventory all Vietnamese lesson posts in `contents/vi/chapter*/_posts/*.md` and classify each lesson by interactive illustration type.
- [x] 1.2 Define a lightweight mapping table (lesson -> interactive template/container IDs) that covers existing and future Vietnamese lessons.

## 2. Vietnamese interactive delivery
- [x] 2.1 Add Vietnamese-only interactive script loading in `_layouts/post.html` so interactive modules activate only for `page.lang == 'vi'`.
- [x] 2.2 Implement or extend Vietnamese interactive modules in `public/js/` to support the mapped lesson types with Vietnamese UI copy.

## 3. Content rollout
- [x] 3.1 Backfill all existing published Vietnamese lessons with at least one interactive illustration container and short learner guidance text.
- [x] 3.2 Update contributor guidance (`ILLUSTRATIONS_GUIDE.md`) with a required workflow for new Vietnamese lessons.

## 4. Validation
- [x] 4.1 Add an automated coverage check (script or build-time check) that fails when any published Vietnamese lesson is missing an interactive illustration container.
- [x] 4.2 Run `bundle exec jekyll build` and the new coverage check; document any exclusions (for hidden or intentionally non-lesson pages).
