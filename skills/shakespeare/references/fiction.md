# Fiction and narrative

Story-level habits survive sentence-level editing. In one study, narrative features alone identified AI stories at 93% macro-F1, and expert-style phrase edits barely moved that number (N04). Fixing them means changing what happens and how the story is told, not only its wording. Source codes refer to [research-basis.md](research-basis.md).

## Theme and meaning

- **The narrator states the lesson.** AI stories include narratorial commentary on the theme in 77% of cases against 52% for human stories. Dialogue also turns into philosophical debate more often (59% against 34%). Let the reader infer the meaning, and keep dialogue about what characters want from each other. (N04)
- **No subtext.** On the test "does the story work on more than one level?", New Yorker stories passed 89% of the time and the best model 11%. Experts described AI characters as over-explaining situations and emotions, and AI dialogue as "clumsy exposition directed at the reader". Leave at least one important thing unsaid. (N14, N01)
- **Explaining what was just shown.** "Unnecessary exposition" made up 18% of professional writers' edits to model paragraphs. If an action shows that a character is afraid, cut the sentence that says so. (N01)

## Emotion and the senses

- **Every emotion as a body sensation.** AI stories render emotion through bodily sensation in 81% of cases against 38% for human ones. Human writers name an emotion plainly more often (29% against 8%). Over-applied "show, don't tell" is itself a tell. Mix plain naming, behavior, dialogue and the occasional physical detail. (N04)
- **Smell and sensory density.** AI stories lean on smell (82% against 57%) and pack in more sensory detail. Don't open scenes with scent by default. (N04)
- **Setting as mirror.** Weather and landscape that echo the character's mood are more common in AI stories. Let setting be setting. (N04)
- **Stock beats.** Flicker, glint, gaze, nodded, leaned, murmured, grinned, hesitated, blinked: these appear in the top overused lists of most of 67 models tested. So do "voice barely above a whisper", "the air thick with the scent of", "took a deep breath", "a smile playing on her lips", "eyes never leaving", "casting long shadows", "heart pounding in her chest", "couldn't shake the feeling", "something else entirely", "a profound sense of", "hung in the air", "eyes darting", "a knot in her stomach". Replace with an action specific to this character, or with nothing. (N06, N01)

## Plot and structure

- **Single track, strictly causal.** AI stories have no subplot 79% of the time (humans 57%), follow tighter cause-and-effect chains and stay chronological. Human stories use parallel subplots, flashbacks, out-of-order telling and late revelations that reframe earlier scenes. In longer pieces, consider one of these. (N04)
- **Resolution by acceptance.** AI stories resolve through the protagonist's inner understanding (47% against 27%) and their own choice (69% against 46%). Let outside events decide things sometimes, and allow ambiguous endings. (N04)
- **Endings that don't stop.** Epilogues, flash-forwards, extended denouements, a closing realization. Experts said "the falling action falls… and falls." Stop soon after the climax, on an action or image. (N14, N04)
- **Rushing through time.** Models summarize the middle to reach the end and accelerate after the first scene. Dramatize the key moments as scenes. (N14)
- **Escalation.** Claude-written stories in particular show flat event escalation. Raise the stakes. (N04)

## Characters

- **Morally clean protagonists.** Human stories have ambivalent or mixed protagonists 59% of the time against 38%. Give the main character choices that cost someone something. (N04)
- **Flat secondary characters.** Experts found other characters were not "full human beings" and sometimes vanished without effect. Give each one a want that conflicts with the protagonist's. (N14)
- **Introduction by description.** AI stories introduce characters with an external description more often (52% against 30%). The most distinctive human habit was introducing a character in dialogue. (N04)
- **Default names.** Elara, Kael, Sarah, Emily, Marcus. Pick names for the setting. (N06, P28)

## References and voice

- **Vague allusion.** AI stories gesture at "an old song" or "the poets"; humans name the work explicitly about twice as often (47% against 24%). (N04)
- **No reader address.** Human stories break the fourth wall and address the reader far more often. Use it if the voice supports it. (N04)
- **More dialogue.** Human stories carry a higher proportion of dialogue to narration. (N04)

## Dialogue and scene defaults

- **Tidy dialogue.** Aphorisms ("I don't remember what the fight was about, only that I was right"), set-up-and-punchline exchanges, a character who speaks the story's insight ("Now I'd give anything for him to turn it up"). People interrupt, dodge, answer the wrong question and leave things unsaid.
- **Wisdom in narration.** "Most of the time the right thing was to stand there and be a person." This is the lesson stated by the narrator instead of a character.
- **Default scenes.** Given the same prompt, two different models produced nearly the same story: crackers from the machine, the patient described as "comfortable", a monitor chirping down the hall, a childhood memory of the father, the nurse walking him back. If a detail is the first one anyone would think of for this setting, find the second or third.
- **Circular endings.** Ending on the object from the opening (the crackers again) is a neat device that has become a default.

## What to put in their place

Avoiding defaults leaves a gap. In testing, these filled it well:

- **Give each character an errand of their own** that has nothing to do with the theme: the nurse has nineteen minutes of break left and wanted to sit down; the quarters in her pocket are for her building's laundry room. People in a crisis are surrounded by other people's ordinary days.
- **Use objects with a history.** A sign taped to the machine in March that nobody acted on. A visitor sticker with the name misspelled. These are particular to this place and nobody would guess them.
- **Let the important thing be said sideways.** A man asking about changing a flight is asking how long his father has. The other character answers the question he asked.
- **End on a small, unexplained action** that the reader has to interpret: she leaves the twenty where it is. Don't add the sentence that explains it.

These are examples of a method, not a new template. If every story has a misspelled name tag, that's a tell too.

## Model fingerprints worth knowing (2026 models)

- **Claude:** flat escalation, quiet endings, epilogues and flash-forwards, a uniform voice, reverence for literary tradition.
- **GPT:** gossip and rumor as plot devices, a distant retrospective narrator ("years later"), ambiguous reconciliations.
- **Gemini:** the tidiest endings, extended denouements, relentlessly bleak settings, external character description.
- **DeepSeek:** a visible narrator, emotion through behavior, atmosphere over plot.

Correct for the defaults of whichever model is drafting. (N04)
