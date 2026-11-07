Markov Lyric Chain

> A rule-based, bigram Markov chain language model built from scratch in Python to generate synthetic song lyrics.
> Was built for Khan Academy's Unit 6 capstone project.

---

Overview

This project is a lightweight, custom Natural Language Processing (NLP) text generator. Referenced from Khan Academy's starter code, 
this program was engineered from the ground up. As the project grew, a few additional functions were added:

* Ingests raw song lyrics and maps word-to-word transitions into a dictionary.
* Uses Python's walrus operator (`:=`) as a temporary buffer to handle commas without breaking key lookups.
* Preserves proper nouns (like "Jesus" and "Bimmer") while standardizing dictionary keys.
* Cleans and formats the generated output into capitalized sentences ending with a period.

The model was trained on a curated group of lyrics from artists I enjoy listening to: Daniel Caesar, Olivia Dean, Drake.

---

Sample Generated Output

Here are a few actual snippets produced by the model during testing:

> _"Used to call me on my love."_

> _"I will rise Always, on it, as stars in the sky Always, will rise Always, nowhere Always, count on it, nowhere Always, you can count on Always, stars in the sky."_

---

Dev note: I'm definitely going to come back and further improve this project. Also I am flabbergasted to have realized I am a developer now. I can write such a thing as "Dev note". Oh my god.

(Requires Python 3.8+ for walrus operator support :D).
