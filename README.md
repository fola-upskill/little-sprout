# Little Sprout Learning

**Live site:** https://fola-upskill.github.io/little-sprout/ · **[What it can and cannot do →](FEATURES.md)**

A guided kindergarten web app for ages 5–6. Includes 50 progressive modules per subject: Math, English, and Science.

## Use it

On first visit the app asks for the child's first name, whether they are a boy or a girl, and their favorite color (the whole site then takes on that color), then greets them by name out loud ("Welcome, Fanu!"). Return visits say "Welcome back". The name is used on screen and in the Grown-up corner, stays in this browser only, and can be changed in the Grown-up corner. Fanu and Fife have recorded Storyteller greetings by name; other children are welcomed as "little sprout" in the same voice, with their name shown on screen.


Open `dist/index.html` in a modern browser, or use the private hosted site. Begin with module 1 in each subject. A parent or caregiver should read along and supervise home activities.

Each module has teaching, three focus questions, two reinforcement questions, and a home activity. Four of five correct on first choices plus the home activity unlocks the next module. Wrong choices can be retried with feedback. Parent previews never change progress.

Progress is saved in this browser, not synced across devices. Export and import backups in the Grown-up corner. Read aloud is optional. By default it uses the Storyteller voice: natural, pre-recorded narration of every lesson sentence, question, answer choice, explanation, hint, and cheer, stored in `dist/voice/` (one MP3 per module plus `common.mp3`, with timings in `voice/index.js`). Each sentence or answer choice is highlighted as it is heard. Every screen uses the Storyteller voice, including the entry and welcome screens; a grown-up can choose a slower speed in the Grown-up corner. If a recording cannot load, the app falls back to the best device voice automatically, preferring natural voices and skipping novelty ones. Wrong answers get a gentle nudge and a hint from the lesson rather than the answer. External Google Fonts are decorative and the app falls back to system fonts when offline.

Print any module using its Print worksheet button. The child worksheet and answer key are separated by a page break. Browser print settings and longer questions may affect pagination; keep the answer key separate.

## Source and checks

Regenerating the Storyteller voice (after changing any lesson text): `node tools/voice-manifest.cjs dist manifest.json`, then `python3 tools/record_voice.py` and `python3 tools/assemble_voice.py dist/voice`. These use the open Kokoro TTS model (`pip install kokoro-onnx soundfile`, model files `kokoro-v1.0.onnx` and `voices-v1.0.bin` from the kokoro-onnx GitHub releases) and ffmpeg. `node verify.cjs` fails if any spoken line is missing a recording.


`make_curriculum.py` generates `dist/curriculum.js` using Python's standard library. `dist/app.js` handles the learning flow. `dist/style.css` contains responsive and print styles. `node verify.cjs` checks all modules, wording and read-aloud speech rules, answer choices, review ordering, scoring, unlocking, preview isolation, persistence, and worksheet content using a DOM stub; it does not verify browser rendering.

The content is guided practice, not a standardized curriculum or a diagnostic assessment. The parent view explains the intended use and scoring.
