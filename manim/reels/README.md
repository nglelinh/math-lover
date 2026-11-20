# Short Manim reels (1080x1920, dark background, no music)

Source for the `### Video ngắn` / `### Short video` clips in the lessons.
Each scene file renders both languages: `REEL_LANG=vi|en manim -qh <file>.py <Scene>`
(9x16 frame, 1 unit = 120 px, background #10121a). Captions live in the `TX` dict of each scene.
Compress with: ffmpeg -i in.mp4 -c:v libx264 -crf 26 -preset slow -pix_fmt yuv420p -movflags +faststart -an out.mp4
Output goes to public/videos/reels/<slug>_<lang>.mp4.

| scene file | class | slug |
|---|---|---|
| evenodd.py | EvenOdd | even-pairs |
| squares.py | Squares | square-dots |
| sieve.py | Sieve | prime-sieve |
| gcf.py | Gcf | gift-packs-gcf |
| lcm.py | Lcm | common-multiple-meet |
| pizza.py | Pizza | pizza-fractions |
| balance.py | Balance | balance-scale |
| binary.py | Binary | binary-bulbs |
