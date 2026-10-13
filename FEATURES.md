# Little Sprout Learning: Features

> ✿ *Inspired and proudly made for **FANU** and **FIFE*** ✿

Little Sprout is a gentle learning garden for children aged **5–6**. It covers kindergarten **math, English, and science** in short 10–15 minute lessons that a child does with a grown-up nearby. Every lesson is read aloud by a warm, natural voice.

**Try it:** [fola-upskill.github.io/little-sprout](https://fola-upskill.github.io/little-sprout/)

---

## At a glance

| | |
|---|---|
| **Ages** | 5–6 (kindergarten) |
| **Subjects** | Math · English · Science |
| **Lessons** | 150 total (50 per subject, in 10 units of 5) |
| **Lesson length** | About 10–15 minutes |
| **Voice** | Recorded natural "Storyteller" voice, about an hour of narration |
| **Cost** | Free. No ads, no sign-up, no accounts |
| **Privacy** | Name, progress, and settings stay on the device |
| **Works on** | Phones, tablets, and computers in a modern browser |

---

## ✅ What it can do

### 🌱 Welcome every child personally
- **Gets to know the child.** The first screen asks the child's **name**, whether they are a **boy or a girl**, and their **favorite color**. The Storyteller voice asks each question out loud.
- **Says each choice back.** Picking a choice gets a cheerful reply, like *"Girl!"* or *"Blue!"*.
- **Greets the child.** It says *"Welcome, Fife! I'm so happy you're here. Let's learn and grow together!"*, and later visits say *"Welcome back!"*
- **Uses the child's name on screen.** For example *"Hi, Fanu!"*, *"Fanu's learning garden"*, and *"Fanu, you got 5 of 5 right…"*

### 🎨 Turn the site into the child's favorite color
- There are seven colors to choose from: red, orange, yellow, green, blue, purple, and pink.
- The **whole site changes color** to match: the banner, buttons, headings, progress bars, and lesson tiles. Each theme was checked to stay easy to read.

### 🗣️ Read everything aloud in a natural voice
- **Everything is narrated.** Every lesson sentence, question, answer choice, explanation, hint, cheer, and welcome is pre-recorded in the **Storyteller** voice. That's more than 1,800 lines, and the voice sounds the same on every device.
- **Follow-along highlighting.** Each sentence or answer choice lights up while it's being read.
- **Symbols said as words.** *"2 + 3 = ?"* becomes *"2 plus 3 equals what?"*, a blank becomes *"blank"*, and letters are said as *"small letter a"*.
- **Speed choice.** Grown-ups can pick **Natural** or **Slow and clear**.
- **Read on tap or automatically.** With **Read aloud** on, each step reads itself. With it off, a *"Read it to me"* button is always there.

### 📚 Teach a full kindergarten path
| Math | English | Science |
|---|---|---|
| Count to 5 · Count to 10 · Compare and order · Shapes around us · Patterns and positions · Addition to 5 · Subtraction to 5 · Numbers to 20 · Measure and sort · Put it all together | Letter beginnings · More letter partners · Short vowel sounds · Listen to words · Blend and read · Build and change words · Word families · Helpful little words · Read little stories · Speak and write | Observe and ask · Our five senses · Explore materials · Living things · Growing plants · Animal explorers · Weather watchers · Earth and sky · Care and motion · Investigate and celebrate |

Every lesson follows the same four steps:
1. **Learn:** a short, simple explanation.
2. **Practice + review:** 3 new questions plus 2 *"Remember this?"* questions from earlier lessons.
3. **Try at home:** a hands-on activity away from the screen, with a grown-up.
4. **Celebrate:** the results, with encouragement.

### 💛 Encourage, not pressure
- **Hints, not answers.** A wrong answer gets a gentle nudge (*"Good try! Let's look again."*) and a **little hint** from the lesson. It doesn't give the answer away.
- **Varied praise.** Right answers get different cheers (*"Wonderful thinking!"*, *"You got it!"*) along with a short explanation.
- **Unlimited retries.** A child can keep trying until they find the answer.
- **Mastery opens the next step.** Getting **4 of 5 right on the first try**, plus doing the home activity, unlocks the next lesson. Finished lessons always stay open for more practice.

### 👪 Support the grown-up
- **Grown-up corner.** It shows progress by subject, the next lesson in each, and **skills to revisit** (questions missed on the first try).
- **Preview any lesson.** A grown-up can look at any of the 150 lessons ahead of time without changing the child's progress.
- **Printable worksheets.** Every lesson has a worksheet with a name line, the lesson reminder, five questions, a drawing space, and a separate **answer key** page.
- **Backup and move progress.** Progress can be exported to a file and imported again, for example to move it to a new device.
- **Change learner details** (name, gender, color) at any time.

### 🔒 Respect privacy
- No accounts, no sign-in, no ads, and **no tracking or analytics**.
- The child's name, color, progress, and settings are saved **only in that browser on that device**. Nothing is sent to a server.

### ✔️ Built to be checked
- An automated check (`node verify.cjs`) tests all 150 lessons, every answer choice, scoring, unlocking, saved progress, the wording, the speech rules, and that **every spoken line has a recording**.
- Each update is checked automatically before it goes live on the website. If a check fails, the live site isn't changed.

---

## ❌ What it cannot do (yet)

### Voice and names
- **Say every child's name.** The Storyteller voice can only say words that were recorded ahead of time. **Fanu** and **Fife** have their own greetings. Any other child is welcomed as *"little sprout"* in the same voice, with their name shown on screen. *More names can be recorded on request.*
- **Listen to the child.** It doesn't use the microphone, so children answer by tapping, not by speaking.
- **Speak other languages.** The lessons and the voice are in English only.
- **Sound out letter sounds exactly.** For blending (*"m, a, t"*), the voice says letter **names**. A grown-up can model the letter **sounds**.
- **Play sound before the first tap.** Browsers block sound until the child taps or types, so the first spoken question plays on the first tap.

### Profiles and progress
- **Keep separate progress for each child.** Each device holds **one** learner's progress. Changing the name doesn't create a new progress record, so siblings who share a tablet share progress.
- **Sync between devices.** Progress made on a phone won't appear on a tablet. Use **Export / Import** in the Grown-up corner to move it.
- **Survive cleared browser data.** Clearing the browser's data, or using a private window, erases progress. Export a backup first.

### Learning and assessment
- **Grade or assess the child.** Scores are practice signals, not grades, test results, or a diagnosis. It isn't tied to a standardized curriculum.
- **Adapt the lesson order.** All children follow the same path. Review questions come from earlier lessons, but the order doesn't change with a child's answers.
- **Check handwriting or home activities.** The home activity is marked done by the grown-up, and drawings and writing happen on paper.
- **Replace a grown-up.** It's designed for a child **with** a grown-up nearby, who reads along, helps with activities, and celebrates.

### Technical
- **Work offline.** It needs an internet connection to load lessons and their audio. The Storyteller recordings are about 37 MB in total, downloaded one lesson at a time as needed.
- **Install as an app.** It runs in the browser; there's no app-store version.
- **Report usage.** It has no visitor statistics. Privacy-friendly, cookie-free analytics (such as GoatCounter) could be added.
- **Teacher or classroom view.** There's no dashboard for following several children or a whole class.

---

## Possible next steps

- Record greetings for more children's names
- Separate progress for each child on a shared device
- Offline mode, installable on the home screen
- Letter-sound recordings for phonics blending
- Privacy-friendly visit counts

---

*Source code, the curriculum generator, and the voice tools are in this repository. See the [README](README.md) for how to run the checks and re-record the Storyteller voice after editing lesson text.*
