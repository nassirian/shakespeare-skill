# Pattern catalog

This file collects the patterns that separate LLM prose from human prose. Each entry gives what to look for, what to do, and where the evidence comes from. Source codes refer to [research-basis.md](research-basis.md): P01–P31 are the original detection papers, and N01–N13 are the newer style studies.

Three rules apply to the whole catalog:

1. **Look for frequency and clusters.** Almost every item here also occurs in good human writing. One "crucial" proves nothing; "crucial", "pivotal" and "underscores" in one paragraph are a pattern.
2. **Fix the cause.** If a sentence exists only to restate, cut the sentence. Changing one word in it is not enough.
3. **Never trade accuracy for texture.** Specifics must be true. Quotes must be real. Qualifications stay.

---

## A. Planning and content

| Pattern | What to do | Evidence |
|---|---|---|
| **Generic angle.** The default survey of a topic: background, several considerations, summary. AI stories also cluster in a narrow region of possible plots and premises. | Pick one claim, case or problem. Ask what only this piece could say. | P28 (originality, 24% of expert explanations), N04 (AI stories cluster; human stories are rarer), N05 |
| **Low information density.** Filler, background nobody asked for, generic content. | Every paragraph must serve the actual question. Cut background and "why this matters" passages. | N05 (relevance and density were the strongest predictors of a "slop" judgment), P28 (clarity) |
| **Padding.** Machine documents run about 20% longer at the same sentence length. | Stop when the content is done. | P18 (MAGE), P31 |
| **Expanding notes into prose.** This is the use that creates the strongest signal; proofreading alone barely registers. | Keep the density of the user's notes. Don't inflate bullet points into fluent paragraphs unless asked. | N10 (Liang et al.) |
| **Vague, unverifiable claims.** Category nouns instead of names ("a major tech company"), broad claims instead of numbers. | Use the name, the number, the date, but only when it is true and supplied. Otherwise ask, mark a placeholder, or keep the claim general. | P28, P19, P20 (models invent specifics), N01 (lack of specificity) |
| **Invented specifics.** Fabricated statistics, places, people, albums, quotes. | Never. Specificity that isn't true is the worst possible fix. | P19, P20, P23, P25 |
| **Uniformly positive tone.** Optimism, uplift, softened bad news, reviews that default to praise. | Keep the author's verdict and complaints. State harms concretely. Don't pivot to hope. | P28 (tone, topics), P18 (positive bias in reviews), N13 (rewrites shift toward positive moral tone) |
| **Reflective commentary.** "This reminds us…", "underscores how much we have yet to learn…". | Cut it. | P28 |
| **Avoiding dark or awkward material.** | Don't euphemize what the subject includes. Don't add darkness for effect either. | P28 |

## B. Sentence construction

| Pattern | What to do | Evidence |
|---|---|---|
| **Present-participle clauses.** "…, highlighting the need for…", "…, leaving a lasting impression". GPT-4o uses them at 5.3× the human rate; instruction-tuned models generally 2–5×. | Cut the tail, or make it its own finite clause with a subject. | N02 (Reinhart et al., PNAS), P10 (LLM rewrites add -ing chains), N01 (poor sentence structure) |
| **Nominalizations and noun stacks.** About 2× the human rate. "The implementation of X led to a reduction in Y." | Use a verb with an actor: "When they adopted X, Y fell." Academic genres can stay more nominal. | N02, P10 ("questions the efficacy, consumer satisfaction, and industry acceptance") |
| **Phrasal coordination.** Noun or adjective pairs by default ("innovation and growth"); 1.9× in GPT-4o. | Keep one, or keep the pair only when both carry information. | N02, N01 ("a mix of X and Y") |
| **Negative parallelism.** "Not X, but Y", "It's not just X, it's Y", "This isn't about X. It's about Y.", "not X — Y", "no longer X. It's Y." Up to 6.3× the human rate in some models. | State Y directly. Keep a contrast only when someone really holds X, and at most once per piece. | N06 (Antislop, four regex families), P28 (sentence structure), P09 examples |
| **"Not only … but also".** | Rewrite as a plain statement: "X also does Y." | P28, P09 |
| **Lists of three.** Triadic examples and adjective strings ("well-motivated, well-executed, and well-evaluated"). | Use as many items as the content has. | P28 (experts singled out "groupings of three"), P19 |
| **Hedged and inceptive verbs.** "Seemed to amplify", "began to drift". | Use the verb unless doubt or the start of the action matters. | N01 (writers' notes) |
| **Formulaic openers.** "As the sun set, …", "When it comes to…", "In a world where…", "Whether you're A, B, or simply C". | Start with the subject or the new information. | P28, P09, N01 |
| **Uniform sentence complexity and length.** Every sentence multi-clause, little variance. | Mix simple and complex sentences because the content differs. Short sentences and fragments are fine where a person would use them. | P28, P07 |
| **Repeated syntactic templates.** The same part-of-speech skeleton recurs ("Fiercely, the beast breathed. Slowly, the caterpillar inched."). Templates survive synonym swaps and alignment training. | Change the structure of the sentence, not just its words. Check consecutive sentences for identical shape. | N03 (Shaib et al., EMNLP 2024), P01 |
| **Concessive verdict template.** "Despite A and B, Z", collapsing a mixed opinion into one balanced sentence. | Keep the author's order of thoughts and the strength of each. | P10 |
| **Under-used agentless passive.** Models use it at about half the human rate. | Don't purge passives. News and academic writing use them naturally. | N02 |
| **"That"-clause subjects and extraposed framings.** "It is clear that…", "That X is true shows…". | State the claim. | N02 |

## C. Vocabulary

None of these words is wrong. They are the words that rise sharply in model output relative to human writing, so a cluster of them is a strong signal. Replace a word only when a plainer or more exact one exists. Don't swap in a synonym that does the same job.

**Style verbs** (largest excess in scientific abstracts; delves 28×, underscores 13.8×, showcasing 10.7×): delve, underscore, showcase, highlight (for "show"), foster, leverage, harness, bolster, pave (the way), unveil, unlock, illuminate, elucidate, encompass, navigate, embark, elevate, empower, embrace, enhance, streamline, revolutionize, resonate, transcend, grapple, garner, surpass, tailor, ensure, exhibit, utilize. *Sources: N07, N09, P28 Table 12, N02.*

**Evaluative adjectives:** crucial, pivotal, vital, paramount, essential, key, comprehensive, robust, seamless, meticulous (34.7× in peer reviews), commendable, noteworthy, notable, invaluable, groundbreaking, transformative, unparalleled, innovative, novel, profound, multifaceted, nuanced, intricate, vibrant, vivid, dynamic, burgeoning, pressing, imperative, holistic, compelling, remarkable. *Sources: N07, N09, N10, P28.*

**Abstract nouns:** tapestry (155× in GPT-4o fiction continuations), testament, realm, landscape, journey, beacon, interplay, intricacies, endeavor(s), avenue(s), insights, nuance, camaraderie (162×), solace, synergy, paradigm, cornerstone, framework (as filler), ecosystem, roadmap, toolkit. *Sources: N02, N07, P28.*

**Literary words common in model fiction:** palpable, unspoken, amidst, fleeting, unravel, ignite, cacophony, unease, pang, waft, whisper(ed), murmured, flicker(ed/ing), glint, gaze, shimmered, hummed, faintly, unreadable. *Sources: N02, N06 (most shared across 67 models: flicker 98.5% of models, leaned 82%, muttered 82%, gaze 81%).*

**Connectives and adverbs:** additionally, moreover, furthermore, notably, consequently, ultimately, importantly, essentially, seamlessly, particularly, arguably, undeniably. Sentence-initial ones are the strongest signal. *Sources: N09, P28, P07.*

**Stock phrases:** it's important to note; it's worth noting; when it comes to; in today's (fast-paced / digital) world; in a world where; plays a crucial role; a wide range of; at the end of the day; paving the way; a testament to; stands as a; serves as a; the power of; the future of X; a deeper understanding; a rich tapestry; navigate the complexities; delve into; shed light on; strike a balance; a double-edged sword; cautionary tale; game-changer; a leap forward; at its core; in conclusion; in summary; to address these limitations; our findings highlight the importance of. *Sources: P28, P08, P10, P19, N09.*

**Abstract blends (fiction and essays):** a sense of [noun]; a mix of [emotion] and [emotion]; the weight of [noun]; a state of [adj] [noun]; the subtle shift in; "unspoken" (in about 15% of model paragraphs in one corpus). *Source: N01.*

**Speech verbs:** notes, explains, emphasizes, highlights, observes, remarks, insists. Default to "said"/"says" and repeat it. *Sources: P28 §2.4, P10.*

**Verb upgrades during "polish":** use→employ/utilize, show→demonstrate/showcase, need→require, change→modify, faced→encountered, big→significant, new→novel, based on→rooted in. *Sources: P10, P21.*

**Model-specific vocabulary.** GPT, Claude, Gemini and Llama each have their own overused words. A list built from one family under-covers the others (P28: one expert's accuracy fell on Claude because they knew GPT's words). Rely on the rules more than on any list. *Sources: P28, N08, P17.*

## D. Format and surface

| Pattern | What to do | Evidence |
|---|---|---|
| **Markdown habits.** Headers on short pieces, bold lead-ins on bullets, uniform lists. Formatting alone identifies the model 73% of the time. | Prose by default. Headers only for navigation in long documents, in sentence case and specific. No "**Label:** explanation" bullets. | N08, P28 (formatting, 15%) |
| **Uniform paragraphs.** Similar lengths, each with a topic sentence and a wrap-up sentence. | Let length follow content. A one-sentence paragraph is fine. | P28 |
| **Em dashes.** Prevalence in medRxiv Discussion sections rose from 4.2% before ChatGPT to 20.3% in 2025. Banning them in the prompt is unreliable, so check after drafting. | Keep a few. Use a comma, colon, parentheses or a full stop for most. | N11 (preprint), N12 (weak) |
| **Narrow punctuation otherwise.** Experts describe human text as using dashes, brackets, quotes run into sentences and "short spurts of comma sections". | Use punctuation that serves the meaning, including parentheses and colons. | P28 |
| **Assistant framing.** "Certainly!", "Here is…", "Below is…", "Overall,…", "I hope this helps", "Let me know if…". | Delete at both ends. | N08 |
| **Signposting.** "Let's dive in", "In this article, we will explore", "Here's the thing", "The short answer:". | Delete. Start with the content. | P28, N08 |
| **Echoing the title or prompt** in the first sentence or repeatedly. | Don't restate the prompt. | P20 (RAID had to instruct models not to repeat the title) |
| **Repetition across outputs and within a piece** (Self-BLEU 9–24 for models against 7.6 for humans). | Vary openers, transitions and paragraph-ending moves across a long piece. | P20, P24 |

## E. Openings and endings

| Pattern | What to do | Evidence |
|---|---|---|
| **Scene-setting opener.** "On a crisp November morning in [place], …", or atmospheric detail before the subject. | Open on a person doing something, or on the fact. | P28 (introductions), P07 (examples) |
| **Hook question.** "Have you ever wondered…?" | Delete. | P19 |
| **Thesis preview.** An introduction that summarizes the whole piece. | Start with the first real point. | P28 |
| **Neat conclusion.** A recap, an uplifting send-off, "the journey continues", "the future holds", "Ultimately, …". This tell survived paraphrasing. | End on the last substantive point, a fact, a quote or the next step. Abrupt is fine. | P28 (conclusions), P07 (AI text gets more predictable toward the end), P08 (models regenerate their own closers almost word for word) |
| **Reflexive caveats and advice.** "It is important to consult a professional", "should be decided on a case-by-case basis". | Keep only if the reader needs it. | P08 |
| **Sign-offs in informal text.** "Thanks in advance!", "Good luck!", "Hope this helps!" stacked with a greeting and enthusiasm. | Use one only if the genre and the author would. | P20, P19 |

## F. People and quotes

| Pattern | What to do | Evidence |
|---|---|---|
| **Default names.** 63% of GPT-4o and 70% of Claude-3.5 news articles included an Emily or a Sarah. Fiction defaults include Elara and Kael. | Use real names in nonfiction. In fiction, choose names that fit the setting. | P28, N06 |
| **Title stacking.** Everyone is "Dr." | Follow the venue's style. Give each person an individual detail instead of credentials. | P28 |
| **Uniform quotes.** Every speaker sounds like the narrator, quotes always end paragraphs, each neatly states one side. | Use real quotes only. Partial quotes worked into sentences; vary placement; let speech sound like speech. | P28 (quotes, 22%), N05 |
| **"Name, a [role] at [institution], said" every time.** | Vary attribution structure; repeat "said". | N05 (templatedness) |
| **Narrated gestures around quotes.** "He shrugged, then laughed." | Cut unless it carries information. | P28 |

## G. Register

| Pattern | What to do | Evidence |
|---|---|---|
| **One register for every genre.** Instruction-tuned models write fiction, news, speech and scripts in the same dense expository style. Bigger models don't fix this; base models are closer to human. | Decide the genre's conventions before drafting. | N02 |
| **Over-formality in informal genres.** No contractions, no filler words, everything spelled out. In informal domains models are more grammatical than humans. | Match the register: contractions, common abbreviations and looser syntax where a person would use them. | P28, P18 |
| **But informality proves nothing.** o1-Pro's contractions fooled one expert completely, and the panel still caught it. | Don't add "honestly" or "just" as decoration. | P28 |
| **Formal genres converge.** Human academic and news writing is close to model defaults. | Put the effort into content and specifics, not surface style. | P21, P13, P03 |

## H. Revision-specific patterns

| Pattern | What to do | Evidence |
|---|---|---|
| **Polish inflation.** Asked to polish human text, models rewrite heavily and add the patterns above. They barely change AI text. | Minimal edits. Leave good sentences alone. | P10 (Raidar, p≈1e-13) |
| **Voice flattening.** Rewrites cut the variance of writing complexity across authors by 21–50% and erase markers of age, gender and emotion; output drifts toward a positive, measured voice. | Preserve sentence-length range, unusual words, pronoun habits, negative emotion words, fragments, caps, interjections, dialect. | N13 (Nature Human Behaviour 2026) |
| **Fragment removal.** "At me. At each other." becomes "They directed their anger towards me…". | Keep deliberate fragments and repetitions. | P10 |
| **Motive explanation.** Rewrites add "In an effort to regain control of the situation, …". | Don't explain what the action shows. | P10 |
| **Fact drift.** Repeated paraphrasing changed ages, places and diagnoses, invented names and added stray sentences. | After any rewrite, compare every name, number, date, place and quote to the source. Never paraphrase repeatedly. | P23, P25 |
| **Structural tells survive word edits.** Paraphrase and translation leave the model identifiable about 91% of the time; narrative features stay detectable after style edits. | Revise the plan (angle, inclusion, order, ending) first. | N08, N04, P28 |

## I. Things that don't work

- **Synonym swaps and "elevated" language.** They lower some 2023 statistical detectors while adding the flowery register human readers flag. One synonym attack turned "Paul Walker" into "Scott Davis". (P22, P20, P11, P26)
- **"Sound human" / persona prompts.** These produced stacked superlatives ("utmost gratitude… captivating… breathtaking") that detectors still flagged at 0.9999, or casual clichés ("Hey there, fellow dog lovers!"). (P05, P09, P27, P21)
- **Multi-pass LLM humanizing.** Each call added more AI characteristics. (P28)
- **Typos, homoglyphs, zero-width characters, character noise.** Inconsistent, sometimes raises detection, damages text, and is dishonest. (P20, P21, P07, P13)
- **Back-translation.** It produces garbage. (P21)
- **Huge banlists.** Banning thousands of patterns degrades writing quality, and a replacement cliché is still a cliché. (N06, N01)
- **Self-judgment.** LLM judges score writing quality and "slop" near chance; one model failed to recognize its own output. Use the concrete checklist. (N05, N01, P28)

## J. Overcorrection (found in testing this skill)

A blind review of drafts written with an earlier version of this skill found that removing the usual tells produced new ones. These are observations from that test, not from the literature.

| Pattern | Example | What to do |
|---|---|---|
| Announced counts | "had three problems on her desk… A shorter menu helped with all three"; "harder in two ways" (followed by a third) | List the items without announcing the number. |
| Bookend closer | Opening "Fieldnote now works offline." / closing "Offline mode is in the app now." | Delete the last line if it only echoes. |
| Practical wrap-up as formula | "If your usual order is still on the menu, it should reach the table faster now." | End on the last fact unless the line carries new information. |
| Staccato | Four or more short declaratives in a row to sound blunt | Combine where the thoughts connect. |
| Cold minimalism | One-word "Thank you." beat; "get in touch" with no contact; under-length with nothing developed | Develop the given facts; keep a specific warm line and a real call to action. |
| Compression | 125 words for a 250-word post; a 300-word essay delivered as 70 words of facts | Develop the facts (reasoning, meaning for the reader); use bracketed prompts for memories only the author has. |
| Warm-filler swap | "a testament to" → "remarkable"; "We hear you"; "we'd love to have you" | Make warmth specific to the facts. |
| Writerly dialogue | aphorisms, set-up/punchline exchanges, the insight spoken aloud | Make speech less tidy; let some lines miss. |
| Symmetrical emotion line | "He was grateful, and a little angry about being grateful." | Show the second feeling in an action, or cut. |
| Default scene | Two models wrote nearly the same hospital story: vending crackers, "he's comfortable", a monitor chirping down the hall, a father memory | Pick the less obvious event or detail. |
| POV drift | A post written as "we" that refers to the owner in the third person | Pick one voice and keep it. |
| Simplified into wrong | "Inside the outdoor unit, a refrigerant circulates in a loop" | Simplify without changing the facts. |

## K. False-positive warnings

- Plain, simple, repetitive diction is human too. Non-native writers were flagged by 2023 detectors at rates up to 61%. Don't "fix" plainness by inflating it. (P22)
- Formulaic genres (recipes, news briefs, abstracts, famous texts) look machine-like whoever wrote them. (P09, P18, P20)
- Experts' false positives most often cited vocabulary: humans also write "delve" and "crucial". (P28)
