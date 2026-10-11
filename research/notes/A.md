# Batch A: extraction (papers 28, 07, 22, 29)

Papers:
- **[28]** Russell, Karpinska, Iyyer. "People who frequently use ChatGPT for writing tasks are accurate and robust detectors of AI-generated text." arXiv 2501.15654v2 (May 2025), ACL 2025 long paper.
- **[07]** Verma, Fleisig, Tomlin, Klein. "Ghostbuster: Detecting Text Ghostwritten by Large Language Models." UC Berkeley (NAACL 2024).
- **[22]** Liang, Yuksekgonul, Mao, Wu, Zou. "GPT detectors are biased against non-native English writers." Patterns 4(7), 2023 (arXiv 2304.02819v3).
- **[29]** Van Vlasselaer, Van Droogenbroeck, Spruyt. "Who wrote this? Evaluating the reliability of AI detection tools in higher education." Int. J. Educational Integrity 22:16 (2026).

---

## 0. Scope of paper [28], which applies to every [28] entry below

- **Generators:** GPT-4o (2024-08-06, temp 0), Claude-3.5-Sonnet, GPT-4o + sentence-level paraphrase (PostMark method), o1-Pro (ChatGPT Pro UI), o1-Pro "humanized" (generated in one step with the expert guidebook plus example articles in the prompt).
- **Human corpus:** 150 American-English non-fiction articles under 1K words from AP, Discover, National Geographic, NYT, Reader's Digest, Scientific American, Smithsonian, WSJ (2022–2024). AI articles are minimal pairs: same title, subtitle, section, publication and approximate length. Prompt: "Include quotations from relevant experts and make sure the article is concise and easily understandable to a lay audience" (Table 8).
- **Annotators:** 5 "expert" Upwork annotators, all frequent LLM users (editors, copywriters, proofreaders, a language teacher), with no training or feedback. They produced 1,790 annotations on 300 articles. Each annotation has a label, a 1–5 confidence score, highlighted spans and a paragraph-length explanation.
- **Results:** expert majority vote got 299/300 right (TPR 99.3%, FPR 0%). Nonexperts were at chance (TPR 56.7%, FPR 51.7%) despite confidence of 4.03/5.
- **How explanations were coded:** GPT-4o-2024-11-20 coded 1,500 explanations into a 15-category taxonomy (Table 17). The frequencies count mentions, not verified features.
- **Strength:** peer reviewed (ACL), minimal-pair design, and rich qualitative data. However, there are only 5 expert raters, one genre (news and feature non-fiction), one dialect, and 2024-era models. Category frequencies are rater attention, not measured corpus statistics. The only actual corpus counts are the names (Emily/Sarah) and the article lengths.

### Clue taxonomy frequencies (Table 3 / Table 17; % of all expert explanations mentioning the category)
| Category | Freq |
|---|---|
| Vocabulary | 53.1% |
| Sentence structure | 35.9% |
| Grammar & punctuation | 24.8% |
| Originality | 23.7% |
| Quotes | 22.3% |
| Clarity | 19.5% |
| Formatting | 15.0% |
| Conclusions | 13.1% |
| Formality | 12.3% |
| Names & titles | 11.7% |
| Tone | 9.3% |
| Introductions | 7.3% |
| Factuality | 7.2% |
| Topics | 3.1% |
| Other | 2.6% |

**Shifts across conditions (Fig. 3, §3, §D.3).** Among correct explanations, vocabulary was cited in 57.1% for o1-Pro but only 42.3% for humanized o1-Pro. Paraphrased GPT-4o drew vocabulary mentions in 88% of explanations, against 69.8% for unparaphrased GPT-4o. Quotes were cited in 33.8% of explanations of paraphrased articles. When experts were wrong (Fig. 9), formality misled them on o1-Pro, and fixating on sentence structure produced false positives.

---

## 1. AI tells (pattern entries)

### 1.1 "AI vocabulary": a specific overused lexicon
- **What the paper found:** [28]. This is the most cited clue (53.1%). Experts know the *exact* overused items (e.g., "testament", "crucial", "vibrant", "significantly", "delve", "tapestry"). Nonexperts instead flag *any* fancy or low-frequency word (§2.1). The full list the experts compiled (Table 12) is reproduced verbatim below.
  - **Nouns:** aspect, challenges, climate, community, component, development, dreams, environment, exploration, grand scheme, health, hidden, importance, landscape, life, manifold, multifaceted, nuance, possibilities, professional, quest, realm, revolution, roadmap, role, significance, tapestry, testament, toolkit, whimsy
  - **Verbs:** capturing, change, consider, delve/dive into, elevate, embrace, empower, enact, enhance, engage, ensure, evoking, evolving, explore, fostering, guiding, harness, highlights, improve, integrate, intricate, jeopardizing, journey, navigating, navigate, notes, offering, partaking, resonate, revolutionize, shape, seamlessly, support, tailor, transcend, underscores, understanding
  - **Adjectives:** authentic, complex, comprehensive, crafted, creative, critical, crucial, curated, deeper, diverse, elegant, essential, groundbreaking, key, meaningful, paramount, pivotal, powerful, profound, quirky, robust, seamless, significant, straightforward, structured, sustainable, transformative, valuable, vast, vibrant, vivid, whimsical
  - **Adverbs:** additionally, aptly, creatively, moreover, successfully
  - **Phrases:** as we [verb] the topic, cautionary tale, connect with, has shaped the, in a world of/where, in conclusion, in summary, it's crucial to, it's important to note, it's not about ___ it's about ___, manage topic issues/problems, not only ___ but also, packs a punch/brings a punch, paving the way, personal growth, quality of life, remember that, simple yet ___, step-by-step, such as, the effects of, the rise of, their understanding of, they identified patterns, to form the, to mitigate the risk, weaving, when it comes to topic
  - Expert quote (§6, Annotator 5, on a GPT-4o conclusion): the "testament" serving "as a beacon of hope and inspiration" and "demonstrating" to us humans "that anything is possible", plus the urge to "showcase" advocacy, social change, inclusivity…
  - Table 11 also refers to guide sections named "Overused AI Metaphors" and "AI Grammar Patterns" (Table 13), but their contents are truncated in the paper.
- **Scope:** GPT-4o, Claude-3.5, o1-Pro, 2024; US news and feature articles.
- **Actionable rule:** Treat the Table 12 list as a high-scrutiny list, not a ban list. For each hit, ask whether a plainer or more exact word exists ("shows" for "underscores", "use" for "harness", "important" or nothing for "crucial/pivotal/paramount"). Cut stock phrases outright: "it's important to note", "when it comes to", "in a world where", "paving the way", "testament to", "beacon of hope". Clusters matter more than single words.
- **Caveats:** This is the main false-positive source among experts. 31% of their *false-positive* explanations cited vocabulary, typically human text containing "delve" or "crucial" (§3). Many listed words ("such as", "community", "health", "life", "role", "support", "change") are ordinary words that humans use constantly. The list is an annotator impression, not a frequency study. Vocabulary is also model-specific: Annotator 2 leaned on GPT vocabulary and fell to 80% TPR / 30% FPR on Claude because they "were not familiar with the distribution of words that are overused by Claude" (§2.2). Vocabulary was a weaker clue for o1-Pro and humanized o1-Pro (57.1% to 42.3%), so avoiding these words alone did not make text pass.
- **Strength:** Moderate. The finding is consistent across raters and conditions, but no counts were made.

### 1.2 Over-descriptive speech verbs: "notes", "explains" instead of "says"
- **What the paper found:** [28] §2.4: "experts frequently point to how humans repeatedly write the word *says*, while AI tries to use more descriptive synonyms like *notes* and *explains*." "notes" also appears in Table 12.
- **Scope:** Mainly o1-Pro, in news articles.
- **Actionable rule:** In attribution, default to "said/says" and repeat it freely. Don't rotate through notes/explains/emphasizes/highlights/observes for variety.
- **Caveats:** This is a journalism convention, so it is genre specific. It is one example of a broader AI habit of elegant variation (synonym cycling).
- **Strength:** Moderate (qualitative, multiple experts).

### 1.3 Formulaic sentence templates: "not only… but also", "it's not just X, it's Y"
- **What the paper found:** [28] Table 17, Sentence structure (35.9%): "high frequency of 'not only . . . but also . . .'". Expert on o1-Pro: "the comparison of 'it's not just this, it's this'". Both also appear in Table 12 phrases ("it's not about ___ it's about ___").
- **Scope:** All models, including o1-Pro.
- **Actionable rule:** Remove "not only X but also Y", "It's not just X; it's Y" and "It's not about X, it's about Y" frames. State the claim directly ("X also does Y"). If a contrast is real, name the actual thing being corrected.
- **Caveats:** Humans use these constructions too. The tell is repetition within one piece.
- **Strength:** Moderate.

### 1.4 Lists of exactly three
- **What the paper found:** [28] Table 17: "consistently listing three items". Expert on o1-Pro: "listings of specifically three ideas". Annotators 2 and 3 emphasize "the tendency of LLMs to always list examples in groupings of three" (§3, §D.3).
- **Scope:** All tested models.
- **Actionable rule:** Let list length follow the content: two items, four, or one strong example. Never pad to three. Avoid triadic adjective strings.
- **Caveats:** Triads are a classic human rhetorical device too. Flag them only when they recur.
- **Strength:** Moderate.

### 1.5 Uniformly complex sentences and low length variance
- **What the paper found:** [28] Table 11: "AI-generated sentences often follow the complex sentence structure, with multiple dependent and independent clauses, while human writing contains more of a mixture of simple, complex, and compound sentences." Table 17: "human-written sentences vary more in terms of length." Example AI sentence (Table 11): "When it comes to celebrating Halloween, this holiday is a testament to the importance of empathy and community." Expert on human text: "Short choppy sentences and paragraphs."
- **Scope:** All models.
- **Actionable rule:** Mix sentence types and lengths. Include some genuinely short, plain sentences and some fragments where they suit the register. Don't open sentences with a framing subordinate clause by default.
- **Caveats:** Fig. 9: "fixating on sentence structure can lead experts to false positives." Edited professional prose can be very regular.
- **Strength:** Moderate.

### 1.6 Grammatical perfection and narrow punctuation
- **What the paper found:** [28] Table 17, Grammar & punctuation (24.8%): "AI-generated text is usually grammatically perfect (also avoiding dashes and ellipses), while human-written text often contains minor errors." Expert on human text: "There's a lot of variety in the article's grammar use, with dashes, brackets, quotes intermixed with sentences, and short spurts of comma sections throughout." On paraphrased AI text: "there's nothing off about the grammar or syntax in this piece…" Table 11: "Human writing generally less strictly adheres to English grammar rules and punctuation." §2.1: nonexperts wrongly believe humans write more grammatically. Experts know "humans actually make more grammatical errors."
- **Scope:** 2024 models. Note the dash observation: experts said AI *avoided* dashes, yet the o1-Pro article that fooled the majority (Table 14) uses many em dashes. Dash behavior is model and era specific.
- **Actionable rule:** Do **not** add errors (out of scope and dishonest). Do use the full punctuation range where it serves meaning: parentheses, the occasional dash, a quote run into a sentence, short comma runs, a sentence starting with "And" or "But". Allow idiomatic, non-textbook constructions the writer's voice would use. Preserve the author's own idiosyncrasies when editing rather than "correcting" them into a standard.
- **Caveats:** This contradicts the popular "em dashes = AI" heuristic. The rule is variety, not any single mark.
- **Strength:** Moderate.

### 1.7 Low originality: safe, obvious, no surprise or humor
- **What the paper found:** [28] Table 17, Originality (23.7%): "AI-generated writing is generally straightforward, 'safe,' and lacking in surprises or humor, leaving annotators bored or disengaged." Human example: "great analogies and creative phrasing… 'amateur sleuths', 'catnip for a certain type of Reddit user.'" AI example (o1-Pro): "What happens when AI tries to be creative? Penguins 'stand on their own flippers'." Table 11: "sticking to an 'obvious' way to answer a prompt… Humans incorporate twists, unexpected insights." The paper calls this a "gulf in creativity" (§3).
- **Scope:** All models, including the humanized ones.
- **Actionable rule:** Take a specific angle, not the default survey of the topic. Include at least one non-obvious observation, analogy or comparison drawn from the actual subject. Humor is allowed. Avoid forced whimsy, which experts also flagged (failed "creative" idioms; "quirky" and "whimsical" are on the vocab list).
- **Caveats:** This is hard to operationalize, and humanizing did not fix it.
- **Strength:** Moderate to strong as a signal, since humans have an advantage here that detectors lack.

### 1.8 Odd or misapplied metaphorical verbs (humanized output)
- **What the paper found:** [28] Table 17, Vocabulary, AI (o1-humanized): "Odd word choices: wheat that 'stores' a lineage; genes that are 'honed.'" Contrast with human food writing that uses "adventurous adjectives like 'chunky', 'musky' or 'thin'" and "verbs like 'blitzing' or 'bolstering'."
- **Scope:** o1-Pro humanized. This tell appears *after* AI vocabulary is suppressed.
- **Actionable rule:** When replacing stock words, choose concrete, sensory, literal-accurate words, not near-miss metaphors. Check that each figurative verb fits its subject physically.
- **Caveats:** One example; the observation is qualitative.
- **Strength:** Weak to moderate.

### 1.9 Fabricated or homogeneous quotes
- **What the paper found:** [28] Table 17, Quotes (22.3%): "AI-generated quotes sound overly formal, lack the varied nuances of real conversation, and often mirror the article's main text too closely in style." GPT-4o: "every expert speaks the same way and it's too homogenous with the text." Human: "The quotes being short snippets also makes me think they're real, as the writer had to find a way to fit them into the text, rather than them just perfectly stating either side's views." After paraphrasing, quotes were flagged in 33.8% of explanations: "always in the same format and style (e.g., only placed at the end of each paragraph)." Fig. 1 (humanized o1-Pro): quotes with unneeded stage-direction narration ("He shrugged as if that were the most ordinary idea, then laughed."). Annotator 5 specialized in judging whether quotes sound natural.
- **Scope:** News articles; GPT-4o, paraphrased, and humanized o1-Pro.
- **Actionable rule:** Never invent quotes. When using real ones, use partial quotes and fragments woven into sentences, vary their placement, and let speakers sound unlike the narrator: speech is looser and less on-message. Drop narrated gestures around quotes unless they carry information. Don't let every quote neatly state one side's thesis.
- **Caveats:** Relevant mainly to journalism and essays with sources.
- **Strength:** Moderate.

### 1.10 Clarity failures: over-explaining, irrelevant detail, telling not showing
- **What the paper found:** [28] Table 17, Clarity (19.5%): "AI-generated text often lacks concise flow by over-explaining or including irrelevant details, effectively 'telling' rather than 'showing'." Claude: "The sentences are condensed to provide the best possible precision with its word choice, but the article lacks flow and clarity." Table 11: "AI prioritizes efficiency, sometimes sacrificing clarity or depth." Fig. 1 expert: the narration "could have been shortened to get more facts in about what people in Alaska face and why."
- **Scope:** All models.
- **Actionable rule:** Spend words on facts and causes, not on narration or restated context. Use plain words "sparingly" for flow (human example: "meander"). Replace abstract claims of significance with the concrete detail that shows it.
- **Caveats:** This category contains opposite complaints (too dense vs. over-explained). The common factor is information-poor prose.
- **Strength:** Moderate.

### 1.11 Overly consistent formatting
- **What the paper found:** [28] Table 17, Formatting (15.0%): "overly consistent (e.g., fully capitalized headings, bolded lists, paragraphs of similar length)." Table 11: AI lists use "a bold header per bullet point, followed by a colon and then description"; "AI-generated text will always italicize the title" of a book; "headers written by AI are quite repetitive." o1-Pro: "a structured article format of commonly used headers." Human: "topic headers focusing on lowercase lettering, longer explanations, and the bullet points not going into a title: one to two sentence explanation format." The evader prompt notes "There are 1/3 odds an article has headers" (Table 13).
- **Scope:** All models.
- **Actionable rule:** Don't add headers to short pieces by default. When used, write specific sentence-case headers, not generic ones ("Why the Search Matters", "Beyond X"). Avoid the **Bold label:** description bullet format. Let paragraph lengths vary.
- **Caveats:** Italicizing titles is correct style in many guides, so don't drop correct conventions. Consistency isn't wrong per se; *uniformity* is the tell.
- **Strength:** Moderate.

### 1.12 Neat, summarizing, optimistic conclusions
- **What the paper found:** [28] Table 17, Conclusions (13.1%): "repetitive and overly optimistic summaries, while human-written conclusions end more abruptly and less tidily." Table 11: "AI-generated text always ends with a neat conclusion, instead of just ending the article naturally… often overly long and summarize everything." Abstract: "optimistically vague conclusions". §D.3: "cheerful summary conclusions" survived paraphrasing. Table 13 evader: "Avoid generic, vague, and forward-looking conclusions, and do not summarize… Concluding sentences don't have to wrap everything up nicely." Example ending from the article that fooled the experts (Table 14): "Until then, the search continues, driven by powerful new telescopes and the human desire to uncover the unseen." Claude: "summarizing, flowery tone".
- **Scope:** All models.
- **Actionable rule:** End on the last substantive point, a concrete fact, or a quote. Delete recap paragraphs and "the future holds" or "the journey continues" closers. No uplifting moral.
- **Caveats:** Some genres (reports, abstracts) legitimately summarize.
- **Strength:** Moderate to strong (repeatedly cited, survives paraphrase).

### 1.13 Generic paragraph openers
- **What the paper found:** [28] Table 13: "Avoid using generic statements to start paragraphs, such as 'For now' or 'In the end'." See also the Table 12 phrases "when it comes to", "in a world where" and "the rise of".
- **Actionable rule:** Begin paragraphs with the subject or the new information, not a temporal or framing filler.
- **Strength:** Weak to moderate (guide-derived).

### 1.14 Formulaic scene-setting introductions
- **What the paper found:** [28] Table 17, Introductions (7.3%): AI intros "are usually generic or focus on scenic details without providing key background, while human introductions have more compelling hooks." Table 11: "a strong scene-opener with a description of a specific time or place, such as 'On a drab November morning…' or 'On December 8, 1660, a London audience gathered…'." Claude: the intro "essentially tells you what the entire article is about." Human: "starts with the subject of the article watching a movie rather than instantly explaining the entire point." Table 13 evader: "Avoid formulaic introductions that elaborate on scene-setting or time, immediately quote experts, or bring in too much historical context. Avoid formatting the first setting by mentioning the setting, then a comma, then some detail… Avoid mentioning atmospheric details or time… in the first sentence." The fooling article opens "For decades, astronomers have speculated…".
- **Actionable rule:** Don't open with "On a [weather/time] morning in [place]," and don't open with a thesis preview of the whole piece. Start with a specific, relevant action, fact or person that leads into the point.
- **Caveats:** Human feature writers do use scene openers; the tell is the formula plus generic atmosphere.
- **Strength:** Moderate.

### 1.15 Excessive formality: no contractions, filler or slang
- **What the paper found:** [28] Table 17, Formality (12.3%): AI "rarely contains filler words, contractions, slang, or abbreviations, favoring fully spelled-out terms and a polished tone." Human: "filler words like 'just', 'very' and 'really'. Colloquial language like 'sucked'." Claude: "'maintains that extending habeas corpus rights to animals'… so strictly formal, so tight and dense with wordage." Table 11: "AI-generated text uses a very formal writing style unless explicitly told not to."
- **Scope:** Unhumanized GPT-4o and Claude.
- **Actionable rule:** Match the register of the venue. In non-academic prose, use contractions and ordinary intensifiers where a person would, and prefer the common term or abbreviation over the fully spelled-out formal phrase.
- **Caveats (important):** This is the **weakest and most gameable** clue. o1-Pro uses contractions and colloquialisms freely, and that fooled Annotator 3. 66.7% of their o1-Pro explanations (83.3% for humanized o1-Pro) cited formality, and their TPR fell to 16.7% and then 0% (§2.4, Fig. 12). So informality is *not* evidence of humanness, and adding "just/actually/really" doesn't make text human. Nonexperts also over-attribute neutral tone to AI. Strong formality signals AI; casualness proves nothing.
- **Strength:** Moderate as an AI signal; strong evidence that the reverse inference fails.

### 1.16 Stock names and uniform honorifics
- **What the paper found:** [28] Table 17, Names & titles (11.7%): "LLMs frequently generate the same names regardless of the prompt (e.g., 'Emily Carter,' 'Sarah Thompson')… if an article contains multiple people, they tend to refer to all of them with the same title (e.g., 'Dr.') without offering unique details. Unique or context-specific names (including real brands or products) are associated with human writing." **Corpus count:** 63.3% of GPT-4o and 70% of Claude-3.5 articles include Emily or Sarah (§3). o1-Pro uses names of real people instead. Humanized articles "use titles for these people (e.g., Dr., Prof.) much more frequently than in human-written articles" (§2.5). Human: "none of them are referred to as Dr. X (bonus points for none of them being named Emily)." GPT-4o: "Dr. Sarah Thompson and Dr. Emily Carter (who by now has more than a lifetime's worth of qualifications)." In Table 14, every expert is "Dr." on first mention.
- **Actionable rule:** Never invent people. For real people, use the venue's convention (often full name plus role on first mention, surname after; "Dr." only where the style calls for it). Give each person an individuating detail instead of stacked credentials.
- **Caveats:** Partly model and era specific (o1 switched to real names).
- **Strength:** Strong for the names (counted); moderate for titles.

### 1.17 Uniformly positive or neutral tone, reflective uplift
- **What the paper found:** [28] Table 17, Tone (9.3%): "consistently neutral or positive, lacking depth or emotional variety." Table 11: "flowery and formal, and its sentences are frequently structured as a reflective, onlooking statement, regardless of topic. AI tends to be inherently positive, attempting to emotionally uplift the reader, especially towards the conclusion." o1-humanized: "the same language it uses to describe everything—inspirational, stunning, essential, and resonating—using formal words, an inherent positivity bias, and a reflective, romantic tone that doesn't give details on why this topic matters…". Human: "display some bias… its political slant which although subtle seems to be there." Fig. 1: "it got sentimental and corny at times."
- **Actionable rule:** Let the piece have a stance, including skepticism, irritation or bias where honest. Cut reflective "this reminds us…" or "underscores how much we have yet to learn" sentences (Table 14 example: "underscores how much we have yet to learn about our own cosmic backyard"). Don't lift the mood at the end.
- **Caveats:** Nonexperts wrongly flag *any* neutral tone as AI (§2.1). Neutral news style is human too; the tell is the uplift and the reflective framing.
- **Strength:** Moderate.

### 1.18 Avoidance of dark or mature topics and swearing
- **What the paper found:** [28] Table 17, Topics (3.1%): "LLMs generally avoid darker or more mature topics (e.g., violence, graphic descriptions)." Human: "burned to ashes and scattered at sea to prevent the crowd from venerating them as relics". GPT-4o: "spends very little time talking about the horrors of the disease, and instead focuses on future research, hopeful quotes, and potential cures… 'embarking on a new chapter'." Table 11: "AI will avoid controversial topics at all costs… avoid any type of swear word, including mild ones like 'darn'." The evader is told to "Add references to darker topics when appropriate."
- **Actionable rule:** Don't euphemize or skip the grim, costly or controversial parts when they are part of the subject. State harms concretely. Don't pivot to hope.
- **Caveats:** Low-frequency clue; don't inject darkness or profanity gratuitously.
- **Strength:** Weak to moderate.

### 1.19 Vagueness instead of verifiable specifics, plus confident errors
- **What the paper found:** [28] Table 17, Factuality (7.2%): AI "contains factual inconsistencies or hallucinations more often." GPT-4o-para: "Incorrect information delivered with customary AI confidence: the 'quad axel' is not another name for the backflip." Human: "very factual, with details about the dates, materials used, and sales portions." Table 11: "Human writing in the domain of non-fiction is factually accurate and contains many specific factual claims… people, places, brands… can be verified." Table 13: "Always opt for specifics over broad details… mention correct statistics instead of broad claims and mention company names instead of saying the type of company." Limitations: factual accuracy was "not a significant cue".
- **Actionable rule:** Replace category nouns with the named entity, and broad claims with the number, date or source, but only with verified facts. Hedge or omit what you can't verify.
- **Caveats:** Specificity is useless if invented, and inventing detail is the worst possible fix.
- **Strength:** Moderate.

### 1.20 Residual signature after humanization: what the fooling article looks like
- **What the paper found:** [28] Table 14 shows the only article the majority missed (o1-Pro, no humanization). The three vocab and structure-focused annotators "did not find enough clues in those categories." The article still contains: "a leap forward", "game-changer", "This isn't just another telescope—it's a new way of doing astronomy" (template 1.3), headers "Why the Search Matters / Enter the… / Technological Edge / Ruling In or Ruling Out / Beyond Planet X", "underscores how much we have yet to learn", and the "Until then, the search continues…" closer. Every expert is introduced as "Dr.". It also uses many em dashes, contractions and real names.
- **Actionable rule:** Surface fixes (real names, contractions, dashes) can hide text from some readers, but structural tells (template contrasts, generic headers, uplifting closers) remain. Edit structure, not just words.
- **Strength:** Single example; illustrative.

---

## 2. Human-text features reported (what humans do that LLMs don't)

From [28] unless noted:
- **Plain repeated "says"** for attribution (§2.4).
- **Adventurous, concrete, sensory diction**: "chunky", "musky", "thin"; verbs "blitzing", "bolstering" (Table 17).
- **Short choppy sentences and paragraphs**; sentence-length variety; a mix of simple, compound and complex sentences (Tables 11, 17).
- **Punctuation variety**: dashes, brackets, quotes intermixed with sentences, "short spurts of comma sections" (Table 17).
- **Minor errors and non-standard conventions** (not always italicizing titles, not "proper" conventions) (Table 11, §D.3). Note this as a description, not something to imitate.
- **Analogies and creative phrasing** tied to the subject: "amateur sleuths", "catnip for a certain type of Reddit user" (Table 17).
- **Humor**, including humorous introductions and conclusions (Table 17).
- **Short, fragmentary quotes fitted into the prose**, with speakers who sound different from the narrator (Table 17).
- **Sparing use of a vivid word** ("meander… used sparingly") (Table 17).
- **Irregular formatting**: lowercase headers, bullets that are not "Title: explanation" (Table 17). Only about 1/3 of articles have headers (Table 13).
- **Abrupt, untidy endings** (Table 17).
- **Filler and colloquialisms**: "just", "very", "really", "sucked" (Table 17). This is not diagnostic on its own (see 1.15).
- **Unique, context-specific names**, real brands and products; people not uniformly titled "Dr." (Table 17).
- **Detectable bias or slant** while trying to appear impartial (Table 17).
- **Hooks that start with the subject doing something**, not with a thesis summary (Table 17).
- **Dense, verifiable specifics**: dates, materials, sales figures (Table 17).
- **Willingness to describe horror and violence concretely** (Table 17).
- **An overall human "ring"** that experts couldn't articulate (Table 17, Other).
- [07] Fig. 2 (human story excerpt): first-person anxiety, run-on emotional rhythm ("there's no answer, there's never an answer because…"), colloquial idiom ("between the ears", "line drawn in the sand"). The ChatGPT counterpart opens with "It was a sunny December morning when…", "Word had spread like wildfire", "Yet, there was an unsettling twist –", and "As the clock struck midnight on Christmas Eve". The figure itself illustrates the stock scene opener and cliché density (1.14), though the paper does not analyze it.
- [07] App. G: human text is **less predictable** (higher per-token entropy under GPT-3), and the gap **widens toward the end of documents**. ChatGPT text grows more predictable as it goes on.
- [22]: native writers show more lexical richness, lexical diversity, syntactic complexity and grammatical complexity (citing L2-acquisition literature), which yields higher perplexity.

---

## 3. Things that do NOT work or that backfire

1. **Paraphrasing.** [28] Exp. 3: sentence-level GPT-4o paraphrase left expert TPR and FPR unchanged (majority 100%). AI vocabulary mentions *rose* to 88% (from 69.8%). Quote-placement uniformity became more visible (33.8%), and cheerful summary conclusions remained. It did hurt open-source detectors (Binoculars 60%, Fast-DetectGPT 56.7%). [07] §7.2: swapping adjacent sentences or paragraphs had negligible effect on Ghostbuster, and sentence or paragraph paraphrase (Pegasus) degraded it only modestly, though repeated paraphrase calls hurt more. Takeaway: rewording sentence by sentence does not remove discourse-level tells.
2. **"Generate, then make it sound more human."** [28] §B.2: o1-Pro asked to humanize its own draft gave "an effect similar to paraphrasing."
3. **Iterative multi-pass LLM humanization.** [28] §B.2: step-by-step passes (creativity, then tone, then grammar, then vocab swap) were abandoned because "the numerous calls to LLMs was adding more characteristics of AI." Each LLM rewrite pass can add tells.
4. **Best method found, still caught.** [28]: a two-step pass (list AI tells against the guide, then edit) was best among post-hoc methods. The final method generated the article in one step with guide plus human examples, because "many of the largest identifiable traits of AI were due to the base generation." Experts still caught 100% of these by majority vote, though confidence dropped and 15.1% of annotations had confidence 1. Lesson: you can't fully retrofit; plan the piece (angle, specifics, structure) humanly from the start.
5. **Avoiding the AI word list alone.** [28]: humanized o1-Pro had fewer vocabulary clues (42.3%) but was still detected through structure, titles, tone, originality and odd replacement words (1.8). Swapping words creates new tells.
6. **Adding informality.** [28]: contractions, slang, "just/actually" fooled one expert but not the panel. Informality is not humanness (1.15).
7. **Character and word-level noise.** [07] §7.2: random character flips, spaces, capitalization, adjacent-word swaps and WordNet synonym replacement degrade a detector smoothly. "Numerous edits are typically required." It is also out of scope (fake typos).
8. **Synonym swapping / "Enhance word choices" / "Elevate… literary language".** [22]: these prompts raise perplexity and fooled 2023 perplexity detectors. "Elevate the provided text by employing literary language" cut detection of ChatGPT-3.5 college essays from 100% to 13%, and "advanced technical language" cut abstract detection from 68% to 28%. But this *adds* exactly the flowery "elevated" register (elevate, vibrant, tapestry) that [28]'s human experts flag. So it is an anti-pattern for us: it beats a 2023 statistic and fails human readers. [28] shows modern classifiers (Pangram) and experts are robust to such tactics.
9. **Commercial humanizers.** [07] App. C: Undetectable.ai reduced Ghostbuster recall from 99% to 62%, so it still fooled the detector less than half the time. [29]: a GPT-4o humanize prompt ("natural, fluid, and nuanced… vary the sentence structure… include modest hedging or reflection, e.g., 'This suggests that…', 'One might argue…'") barely moved Pangram (92.5% accuracy on both hybrid and humanized). It moved Turnitin only modestly (60% to 50%). Note that the prompt itself injects stock hedges, which is just another formula.
10. **Prompting for a style ("high-school student", "very short sentences", "beginner writer", "NYT style").** [07] §6.3, Table 8: Ghostbuster kept 99.5 F1 across these prompt variants. Persona or style prompts don't change the underlying distribution much.
11. **Judging by low-level "fanciness" or neutrality.** Nonexperts in [28] flagged fancy words, neutral tone and grammatical correctness as human or AI incorrectly, scoring at chance with high confidence. A writer optimizing against those folk heuristics optimizes for the wrong things.
12. **Detector fairness (false positives for constrained human prose).** [22]: seven 2023 detectors flagged 61.22% of 91 TOEFL essays (Chinese L1 writers) as AI; 18 essays were flagged by all seven and 89 by at least one. US 8th-grade essays were near-perfect. Flagged essays had significantly lower perplexity. Simplifying native essays' word choice ("as if written by a non-native speaker") raised false positives from 5.19% to 56.65%. Non-native ICLR 2023 abstracts had lower perplexity (p = 0.035). Implication: *plain, simple, repetitive diction is not the AI signature humans use*. Plainness is human too. Don't "fix" plain writing by elevating it. [07] found that its own model's errors on non-native text were largely a length effect (TOEFL-91 median 104 words: 74.7% accuracy; TOEFL11 median 315 words: 99.9%). [29] (2025 tools) found **zero false positives** on 40 non-native master's theses for Turnitin, Copyleaks and Pangram, with only a small error for GPTZero (+1.95). The [22] bias is dated to 2023 perplexity tools.

---

## 4. Statistical and detector findings, and what translates to writing

- **[07] Ghostbuster.** A structured search over token-probability features from unigram, trigram, ada and davinci models feeds a logistic regression. Training data: ChatGPT (gpt-3.5-turbo) vs. Reuters 50-50 news, r/WritingPrompts stories and IvyPanda essays (~500-word median). Results: 99.0 F1 in-domain, 97.0 out-of-domain, 92.2 on Claude.
  - *Translates:* (a) LLM text is more predictable token by token, especially late in a document (App. G, Fig. 6). Endings are where AI prose goes most on autopilot, consistent with [28]'s summary-conclusion tell. Give endings the most editorial attention. (b) Handcrafted features included the average length of the longest words, a weak hint that word-length extremes differ. The paper gives no direction, so no rule. (c) Detection is unreliable under 100 tokens and plateaus around 500, so the signal is distributional and accumulates over length.
  - Related-work notes in [07] §2 (secondary, citing others): AI text "adhered to Heaps' type-token law less" (Meister & Cotterell 2021), meaning vocabulary growth is less human-like. ChatGPT answers are "more formal, more strictly focused, and used more conjunctions" (Guo et al. 2023). That is weak to moderate support for allowing tangents and asides and for trimming connective glue ("Additionally", "Moreover"; compare the [28] adverb list).
  - Human baseline: 6 students with LLM experience reached 59% accuracy (34–80%); 17 web participants reached 58.1%. These are 2023 general users, not experts, consistent with [28]'s nonexperts.
- **[22]** Perplexity-based detectors equate low lexical and syntactic variety with AI. *Translates:* only weakly. Varied, precise word choice is human-like, but [22]'s "elevate" result shows that inflating diction is the wrong way to get variety. Prefer the exact word over the safe default, not the fancier one.
- **[29]** (2025; GPT-4o Deep Research full papers, GPT-4o hybrid literature reviews, one humanize prompt; 40 human theses per category, Belgian social sciences, non-native English). Pangram reached 65% strict and 97.5% inclusive accuracy on full AI papers, and 92.5% on both hybrid and humanized papers. Turnitin, GPTZero and Copyleaks *missed every* full Deep Research paper (Turnitin 100% false negatives). On 1,163 real 2024–25 theses, Pangram flagged 45.5%, with a mean flagged AI share of 34% and only 1.9% above 80% AI.
  - *Translates:* almost nothing at the sentence-craft level; the paper is a tool evaluation. Usable points: (a) a stylistic AI signature "persists even after humanisation" (§Results, speculative attribution to Pangram's mirror-prompt training on "how sentences are built, which linking words are used, and how varied the writing is"). (b) Descriptions of what tools key on: Copyleaks looks at "unusually consistent generation of word and sentence lengths", AI-typical expressions, part-of-speech structure, syllable dispersion and "unique usage patterns of hyphens". Turnitin looks at "perplexity, burstiness, repetition and generic writing". These are vendor claims, not findings. (c) The paper defines burstiness as variation in length, tone and transitions. (d) Real-world AI use is mostly partial (hybrid), so the skill's main use case is editing mixed drafts.
  - Strength: moderate (preregistered, peer reviewed), but N = 40 per cell, one model, one humanize prompt.

---

## 5. Meta-findings useful to the skill's design

- **Expertise comes from exposure.** [28]: people who frequently edit LLM output detect it at about 93% TPR individually; non-users score at chance. A reader familiar with LLM text is the audience to write for. Vocabulary is necessary but not sufficient; structure, originality, quotes, conclusions and names carry the remaining signal.
- **Model-specific vocabularies.** [28] §2.2: Claude has a different overused-word distribution from GPT. A GPT-derived list under-covers Claude tells, so the skill needs Claude-specific vigilance as well.
- **LLM-as-judge with a guide is weak.** [28] §4: GPT-4o plus guide plus CoT reached 78% TPR but only 3.3% on humanized text, and o1 with the guide did worse (36.7%). Claude-3.5 "failed to detect content generated by itself" (§E.3). Self-review by the generating model is unreliable, so the skill should use explicit checklists and concrete rewrites, not "does this sound AI?" self-assessment.
- **Ensemble of clue types.** [28]: each expert specialized (names, grammar and triads, flow and specificity, quotes), and the ensemble was near perfect. A good revision pass must cover all categories, not just vocabulary.

---

## 6. Five-line summary
1. [28] is the core source: expert LLM users caught 299/300 articles from GPT-4o, Claude-3.5 and o1-Pro, even paraphrased or humanized. Their clues, ranked: AI vocabulary (53%), sentence templates and triads (36%), too-perfect grammar with narrow punctuation (25%), low originality (24%), homogeneous quotes (22%), over-explaining (20%), uniform formatting (15%), tidy optimistic conclusions (13%), formality (12%), stock names and "Dr." titles (12%; Emily/Sarah in 63–70% of GPT-4o and Claude articles).
2. Paraphrasing, multi-pass LLM "humanizing", word-list avoidance, synonym swaps and added informality all fail with expert readers, and some add new tells: odd metaphoric verbs, "Dr." inflation, and the flowery "elevated" diction that [22]'s detector-beating prompts produce. Structural and discourse tells survive surface edits.
3. The human features to emulate: plain repeated "says", concrete and sensory diction, varied sentence length and punctuation, fragmentary real quotes, verifiable named specifics, a real stance or slant, willingness to state grim facts, and abrupt untidy endings with no recap or uplift.
4. Know the false-positive traps. Humans also use "delve" and "crucial" (31% of expert false positives cited vocabulary), neutral tone and plain diction are human too ([22]: non-native and simplified prose flagged by 2023 detectors), and informality proves nothing (o1-Pro's contractions fooled one expert down to 0% TPR). Rules should target clusters and formulas, not single words.
5. [07] and [29] give little sentence-level guidance. LLM text is most predictable toward the end of a document, so endings need the most editing; style and persona prompts and commercial humanizers leave a persistent signature; and 2025 tools barely false-flag human theses. Fixes must change planning and structure, not just wording.
