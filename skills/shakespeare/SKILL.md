---
name: shakespeare
description: "Write or revise prose so it reads like a skilled person wrote it: specific, in the author's voice, without the recurring habits of LLM text. Use for drafting and editing, and when text 'sounds like AI/ChatGPT', 'reads robotic', needs humanizing, or should be rewritten in someone's voice. Preserves facts and meaning. Not for authorship detection."
---

# Shakespeare

Write the way a capable person writes when they have something particular to tell a particular reader. The name is a label. Use modern language unless the user asks for another period.

People who read a lot of LLM output can spot it almost every time, and single words are rarely what gives it away. They notice clusters: stock vocabulary, the same sentence templates, lists of three, uniform paragraphs, quotes that all sound alike, a tidy uplifting ending, and content that any model would produce on the topic. Most of these come from how the piece was planned, so they survive paraphrasing, synonym swaps and "make it sound human" passes. This skill works in that order: plan like a person, draft from real material, then run one targeted pattern pass. The evidence is summarized in [research basis](references/research-basis.md).

## 1. Plan before you write

**Name the genre and use its conventions.** Chat-tuned models drift into one dense, noun-heavy expository register whatever the task. Decide what the genre actually sounds like. A text message is short and loose. A forum post can ramble and be blunt. News attributes with "said" and uses the passive where the actor doesn't matter. An academic abstract can be nominal and formal. Fiction runs on scene, action and dialogue. Spoken or casual registers allow contractions, fragments and plain run-ons.

**Find the angle.** Ask what this piece says that the generic piece on the topic would not. If the first structure that comes to mind is a survey (background, three considerations, summary), choose something narrower: one claim, one case, one problem, one recommendation.

**Inventory the real specifics.** List the names, numbers, dates, examples, quotes and first-hand details you actually have from the user or the sources. Write from them. If the piece needs specifics you don't have, ask, or leave clearly marked placeholders in a draft. Never invent people, quotes, statistics, studies, anecdotes or experiences to make writing vivid. The same goes for small things: outcomes ("the kitchen is calmer"), mechanisms, settings, policies, offers, motives. Models reach for these to fill space. A fabricated detail is worse than a vague one.

**Decide what to leave out.** Background the reader didn't ask for, definitions they know, a "why this matters" paragraph, a list of considerations, the history of the topic. Readers judge filler and off-topic content as the main sign of low-quality AI text.

**Don't pad, but deliver the piece.** LLM documents run about a fifth longer than comparable human ones, and expanding notes into fluent filler is how the machine signal gets into text. If the user asked only for a cleanup, keep the density of their notes. If they asked for a blog post or an essay, deliver one, within about 15% of any requested length. A stub that only lists the facts fails the assignment, and readers notice that compression too.

**Grow the piece by development, not invention.**
- Connect the facts with the reasoning between them. A long menu means more ingredients sitting unused, and fewer cooks means each one covers more dishes. That reasoning is implied by the facts, not added to them.
- Say what each fact means for this reader, and answer the questions they would ask.
- Use well-established general knowledge where the genre allows it. Give typical ranges with "about" or "usually" rather than false precision.
- In first-person writing, the narrator can reflect on the stated facts in ways the notes support. Don't hand them feelings they didn't express (regret, gratitude, a lesson learned).

**When the missing material is something only the user has** (memories, what a place looked like, why they did something), ask before writing if the user is there. If they aren't, write the full draft and put short bracketed prompts where those details belong ("[what the back room was like that winter]"), then list the questions after the draft. Never fill those gaps yourself.

**Use everything the brief supplies.** Every name, place, number and role given should appear unless there's a reason to drop it. If the prompt says she's a nurse, the reader should know it. Arithmetic or conversions you add must be correct ("30% of produce orders" is not "30 cents of every dollar of vegetables").

## 2. Draft

### Content

- Start with the point, the news, the request or the scene. No warm-up.
- Every sentence should add something the previous one didn't already imply. Delete sentences that restate, set up the obvious, or explain the significance of what was just shown.
- Choose the word the meaning calls for, not the first fluent one. Human writing is less predictable because people pick words for what they mean, not because they reach for rare words. "The bridge was closed for 11 days" beats "the bridge faced significant disruption."
- Keep the author's real stance: doubts, complaints, irritation, a verdict. Don't soften negative facts or pivot to hope. Reviews need not be positive. Grim subjects can stay grim.
- An odd topic doesn't make prose sound human. Write the non-obvious sentence about an ordinary topic.

### Sentences

- **Trailing participle clauses.** Chat models use "-ing" clauses two to five times as often as people: "…, highlighting the need for reform", "…, leaving a lasting impact". Cut the tail or make it its own sentence with a subject and verb.
- **Noun stacks.** Turn nominalizations back into verbs with an actor. "The implementation of the policy led to a reduction in costs" becomes "When the city adopted the policy, costs fell." Academic prose can stay more nominal.
- **Negative parallelism.** "Not X, but Y", "It's not just X, it's Y", "This isn't about X. It's about Y." State Y. Keep the contrast only when someone actually holds view X, and use it once at most.
- **Pairs and triplets.** Don't group things in threes or pairs by reflex ("innovation and growth", "fast, fair and flexible"). Use the number of items the content has, and don't announce the count ("three problems", "in two ways", "helped with all three"). Just give the items.
- **Hedged verbs.** "Seemed to hover" becomes "hovered", "began to drift" becomes "drifted", unless the doubt or the beginning is the point.
- **Formulaic openers.** Avoid "As [time clause], …", "When it comes to", "In a world where", "In today's …", and "Whether you're A, B or C".
- **Rhythm.** Let length follow the thought: some short sentences, some long, a fragment where a person would use one. Don't alternate lengths by quota. Check that consecutive sentences aren't built on the same frame.
- **Passive voice.** Keep it where the actor is unknown or unimportant. Chat models underuse agentless passives, so an "always active" rule moves text away from human writing.

### Words

- Prefer the plain verb: use, show, find, need, help, change, said. Repeat "said" freely; don't rotate through noted, explained, emphasized, highlighted.
- Look hard at the words LLMs overuse. Sharpest offenders: delve, underscore, showcase, highlight (meaning "show"), foster, leverage, harness, navigate, embark, elevate, tapestry, testament, realm, landscape, journey, intricate, pivotal, crucial, vital, vibrant, seamless, robust, comprehensive, meticulous, multifaceted, nuanced, profound, transformative, palpable, unspoken, camaraderie, additionally, moreover, furthermore, notably, ultimately. The [pattern catalog](references/pattern-catalog.md) has the full lists. These are prompts to check, not banned words. Clusters matter, and swapping each one for its nearest synonym fixes nothing.
- Cut empty intensifiers and evaluations ("significant", "novel", "remarkable", "invaluable") unless a number or a fact backs them.
- Don't cycle synonyms to avoid repeating a noun. Name, pronoun, short description is the natural chain.
- Use one figure of speech at most, and only when it carries something plain words can't. It must fit literally: wheat doesn't "store" a lineage.
- Avoid the abstract-blend constructions "a sense of …", "a mix of X and Y", "the weight of …", "a testament to …".

### Shape and format

- Use prose unless the content is a set, a sequence or a comparison. Don't put headers on short pieces. Never write bullets that start with a **bold label:** followed by an explanation. Model formatting habits are distinctive enough to identify the model on their own.
- Let paragraph length follow the content. Uniform paragraphs are a tell.
- Use the full range of punctuation where it serves the meaning: parentheses, a colon, a quote run into a sentence, a sentence starting with "And" or "But". Ration em dashes. Their use in published writing has climbed since chat models arrived, and many readers now treat them as a marker. Most can be a comma, colon, parentheses or a full stop.
- No assistant framing: no "Certainly", "Here is …", "Great question", "I hope this helps", "Let me know if …". Don't signpost ("Let's dive in", "In this article we will explore").

### Openings and endings

- Open on the subject doing something, or on the fact. Avoid weather-and-time scene setting ("On a crisp autumn morning…"), a hook question, a thesis preview of the whole piece, and "In today's fast-paced world".
- End when the content ends: the last real point, a fact, the next step, a quote, an image. No recap, no moral, no "the journey continues", no "Ultimately, …", no "the future of X is bright". LLM text is most predictable near the end, so give the ending the hardest look.
- Watch for replacement closers too: a last line that echoes the opening ("X now works offline." … "Offline mode is in the app now."), a soft practical wrap-up that adds nothing, a slogan, or a story that ends by returning to the object it opened with. If the last sentence could be deleted without loss, delete it. An ending the author supplied in their notes ("I never asked") is theirs. Keep it.
- Delete reflexive closing caveats ("It's important to note…", "consult a professional") unless the reader actually needs them.

### People and quotes

- Use real names and the venue's naming convention. Don't stack titles ("Dr." on everyone), and never invent people. Fictional names should suit the setting; avoid model defaults like Emily Carter, Sarah Thompson, Elara and Kael.
- Use quotes only from the source. Partial quotes fitted into a sentence read naturally. Speakers should sound unlike the narrator and unlike each other. Don't surround quotes with narrated gestures.

### Fiction

See [fiction](references/fiction.md) for detail. In short:
- Let the theme stay implicit. Cut the narrator stating the lesson and dialogue that explains the situation to the reader.
- Not every emotion has to be a body sensation (tight chest, knot in the stomach). Sometimes name the feeling plainly or show it in behavior. Go easy on smell-led openings and on weather that mirrors mood.
- Resolution doesn't have to come through the hero's inner acceptance. Leave ambiguity, let outside events decide things, stop soon after the climax, skip the epilogue.
- Give characters mixed motives. Introduce them through what they say or do, not a description paragraph.
- Cut stock beats: flicker, glint, gaze, nodded, murmured, "voice barely above a whisper", "the air thick with", "a smile playing on her lips", "let out a breath she didn't know she was holding".
- Name real works instead of gesturing at "the old stories".

## 3. Revising someone else's text

- **Edit as little as you can.** When an LLM is asked to polish human writing, it changes it heavily toward the model's preferred form, and that is where the fingerprint comes from. Leave good sentences alone. Returning a passage unchanged is a valid edit.
- **Keep the author's voice markers:** their range of sentence length, unusual words, pronoun habits, emotion words (negative ones included), fragments, caps for emphasis, interjections, dialect and humor. LLM rewrites flatten these and push every author toward the same upbeat, measured voice. Don't raise the positivity.
- **Don't upgrade words.** use→employ, show→demonstrate or showcase, need→require, change→modify, said→emphasized, "big concern"→"significant concern" are all moves toward machine text. Don't add "novel", "crucial", "importantly", or connective frames like "To address these limitations,".
- **Fix errors without re-voicing.** Correct grammar and clarity problems the author would want fixed. Keep non-standard but deliberate choices.
- **When the source is all boilerplate** (nothing but filler around a few facts), cut to the facts and the author's real purpose, then keep one specific warm line if the genre expects warmth: thanks to the people actually named, the real ask with a real contact. Don't strip it to a bare list.
- **For AI-drafted text, fix structure before words:** the angle, what's included, the order, the opening and the ending. Then sentence templates, then vocabulary. Swapping words inside a template leaves the template.
- **One pass, then check the facts.** Compare every name, number, date, place, quote and qualification against the source. Repeated rewriting drifts facts and adds generic stakes ("crucial", "could potentially").

## 4. Pattern pass

Read the draft once against this list. Look for repetition and clusters, not single occurrences.

1. Template sentences: not X but Y, not only… but also, whether you're…, when it comes to.
2. Trailing -ing clauses and noun stacks.
3. Overused vocabulary, abstract blends ("a sense of"), empty intensifiers.
4. Reflexive pairs and triplets.
5. Hedged verbs: seemed to, began to.
6. Assistant framing, signposting, sentence-initial "Additionally / Moreover / Ultimately".
7. Formatting: headers, bold labels, uniform bullets and paragraphs, em-dash density.
8. Repetition across the piece: the same paragraph opener, sentence frame or key phrase; echoing the title.
9. Opening and ending: scene-setting, hook question, recap, moral, uplift.
10. Tone: uniformly upbeat, reflective "this reminds us…" sentences, softened bad news.
11. Redundancy: sentences that restate or explain what was just shown.
12. Clichés and purple prose, including fiction beats.
13. Facts: read each sentence and ask where it came from. Anything not in the source or in well-established general knowledge goes, including small outcomes, settings and offers. Nothing changed, qualifications kept, point of view consistent.
14. Overcorrection: see the next section.

If you can run code, `python3 scripts/pattern_check.py <file>` counts many of these and points to the lines. Treat it as a pointer, not a score. Don't rely on asking yourself "does this sound human?". Models judging writing quality or "slop" perform near chance, so use the concrete list.

## 5. Overcorrection

Removing the usual tells tends to produce new ones. Test drafts made with this skill showed these:

- **Staccato.** Four or five short declaratives in a row, used to sound blunt. Short sentences are for emphasis, not a default rhythm.
- **Cold minimalism.** Cutting until the piece is curt: a one-word "Thank you." beat, no call to action, no sense of who the reader is. Warmth is fine when it comes from something specific: thank the volunteers for the 180 deliveries, not for "showing up".
- **Compression.** Every sentence a bare fact with nothing connecting them, half the requested length. It reads like notes with verbs added. Blind reviewers judged this a failed assignment, even when it had no other tells.
- **Warm-filler swaps.** Replacing "a testament to" with "remarkable", or adding "We hear you" and "we'd love to have you". Same move, different words.
- **Writerly dialogue.** Lines that are too neat: aphorisms ("only that I was right"), set-up-and-punchline exchanges, a character delivering the insight. Real speech is less tidy.
- **Symmetrical emotion lines.** "He was grateful, and a little angry about being grateful."
- **Default scenes.** Two models given the same story prompt produced nearly the same story (vending-machine crackers, "he's comfortable", a monitor chirping down the hall, a childhood memory of the father). If your scene could be anyone's, choose a less obvious detail, event or turn.

## 6. What not to do

- Don't plant typos, slang, odd punctuation, look-alike characters or deliberate grammar errors.
- Don't swap synonyms or "elevate" the language. Thesaurus-style variation reads worse and keeps the underlying structure.
- Don't add casualness as a token. Contractions, "honestly" and "just" don't make text human. Use them when the register calls for them.
- Don't rely on persona instructions ("write like a human", "be casual"). They swap formal clichés for casual ones.
- Don't run repeated "humanize" passes. Each LLM pass adds new tells and drifts facts.
- Don't replace each flagged word with its nearest neighbor. A replacement cliché is still a cliché.
- Don't make clean, plain writing eccentric. Plain, simple prose is human too, and detectors have wrongly flagged non-native writers for exactly that.

## Deliver

Return the finished text without a preface, an edit log or commentary about this skill. Explain changes only when asked. If an essential fact is missing or contradictory, say so briefly instead of smoothing over it.

These are editorial methods drawn from research on how AI text differs from human text. They are not a way to prove or conceal authorship, and no particular detector result is promised. Don't add this caveat to ordinary outputs.

## References

- [pattern-catalog.md](references/pattern-catalog.md): full pattern list with word lists, evidence and caveats. Read it when doing a thorough edit or when a pattern needs checking.
- [fiction.md](references/fiction.md): narrative-level patterns for stories and creative nonfiction.
- [editing-examples.md](references/editing-examples.md): before-and-after examples. Read them when a choice is unclear.
- [research-basis.md](references/research-basis.md): the studies behind each rule and their limits. Read it when the user asks why.
- `scripts/pattern_check.py`: an optional standard-library checker that counts surface patterns.
