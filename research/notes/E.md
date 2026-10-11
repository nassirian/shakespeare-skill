# Batch E: watermark papers (14, 15, 16) and detection surveys (30, 31)

Sources (full text in /mnt/user-data/uploads/shakespeare/tmp/pdfs/ai-detection-review/):
- **P14** Kirchenbauer et al. 2023, *A Watermark for LLMs* (ICML; OPT-1.3B/2.7B)
- **P15** Kuditipudi et al. 2023/24, *Robust Distortion-free Watermarks* (OPT-1.3B, LLaMA-7B, Alpaca-7B)
- **P16** Kirchenbauer et al. 2024, *On the Reliability of Watermarks* (ICLR; human paraphrase study)
- **P30** Ghosal et al. 2023, *Towards Possibilities & Impossibilities of AI-generated Text Detection: A Survey*
- **P31** Wu et al. 2025, *A Survey on LLM-Generated Text Detection* (Computational Linguistics 51(1))

Overall: the three watermark papers yield almost nothing for an editorial rulebook. P30 contains no linguistic-feature catalogue; it relays a few secondary findings (GLTR, HC3). P31 is the only one with a feature list (§2.1, §5.2.1, §5.3.1, §6.1), but those claims are **secondhand survey summaries** of other studies, mostly on GPT-3.5-era ChatGPT. Treat every P31 entry as a pointer to a primary source, not as evidence in itself.

---

## A. Patterns (AI-text tells a writer can act on)

### 1. Excess length / over-comprehensiveness
- **What the paper found:** "LLM-generated text tends to be about twice the length of human-written text" and LLMs "frequently produce extensive and comprehensive responses" (P31 §2.1, p.277–278, summarizing Guo et al. 2023 HC3 and others).
- **Scope:** ChatGPT (GPT-3.5) answers vs. human answers on Q&A (HC3: Reddit ELI5, finance, medicine, open_qa, wiki_csai), 2023.
- **Actionable rule:** Match length to the question. Cut sections that cover aspects nobody asked about, and don't add a recap of the answer at the end.
- **Caveats:** Partly an artifact of the prompt/task (human Q&A answers are short by genre). Length is easy to steer with a prompt.
- **Strength:** moderate (replicated across several 2023 corpora, but secondhand here and dated).

### 2. Narrower vocabulary that still reads as "polished"
- **What the paper found:** LLM text "exhibits a more limited vocabulary" (P31 §2.1). Hamed & Wu 2023: ChatGPT text "accounted for only 23% of all academic bigram content" in its domain, i.e. "substantial variations in terminology between human authors and LLM-generated content" (P31 §5.2.1, p.300). Countervailing: other studies found LLM-written papers "demonstrate a broader variety of expression" (P31 §6.1, citing Yan et al. 2023; Liao et al. 2023).
- **Scope:** ChatGPT; academic abstracts (bigram study, 100 papers); HC3.
- **Actionable rule:** Use the field's own working terms (the bigrams practitioners actually use, e.g. method names and units) rather than generic, broadly applicable phrasing. Vary content words because the content varies, not by swapping in synonyms.
- **Caveats:** The survey's own evidence conflicts (limited vocabulary vs. broader variety). Non-native human writers also show limited lexical variety and get falsely flagged (P30 §6.4; P31 §8.1). Don't treat lexical richness as a goal in itself.
- **Strength:** weak to moderate (the evidence conflicts).

### 3. Part-of-speech profile: more nouns, determiners, auxiliaries and coordinators; fewer adverbs and less punctuation
- **What the paper found:** "LLMs exhibit a higher frequency of noun, verb, determiner, adjective, auxiliary, coordinating conjunction, and particle word categories compared with humans, and less adverb and punctuation, incorporating more deterministic, conjunctive, and auxiliary structures in their syntax" (P31 §2.1, p.278).
- **Scope:** ChatGPT vs. human (2023 studies cited jointly: Guo et al.; Muñoz-Ortiz et al. "Contrasting linguistic patterns…"; Giorgi et al.; Seals & Shalin). English.
- **Actionable rule:** Watch for long chains joined with "and" and for "X and Y" coordination used as padding. Be wary of auxiliary-heavy hedged verb phrases ("can help to", "is able to", "may be"). Human prose uses more varied internal punctuation (dashes, parentheses, semicolons, colons) and more adverbs that carry stance ("frankly", "barely", "still").
- **Caveats:** This is a population average, not a sentence-level test. Note the tension with later popular "AI overuses em dashes" lore: this 2023 finding says *less* punctuation for AI. Model-specific and dated.
- **Strength:** moderate (multiple studies, but the survey reports no effect sizes).

### 4. Syntactic simplicity, passive voice, low narrativity
- **What the paper found:** Differences "manifest in stylistic dimensions, such as syntactical simplicity, use of passive voice, and narrativity" (P31 §2.1, citing Seals & Shalin 2023). LLM text shows "enhanced organization, logical structure, formality, and objectivity" (ibid.).
- **Scope:** ChatGPT 2023, English.
- **Actionable rule:** Prefer active constructions with a named agent. Let explanatory text carry some narrative (who did what, in what order, what happened next) instead of an impersonal, evenly organized exposition.
- **Caveats:** The survey does not say which way passive voice goes. Formality and objectivity are normal in edited human academic writing (P31 §6.1 and P30 §6.2 warn against style-only judgments).
- **Strength:** weak to moderate (no direction or magnitude given for passive voice).

### 5. Low emotional intensity / positivity bias
- **What the paper found:** LLM text "often conveys less emotional intensity and exhibits clearer presentation than human writing. This phenomenon is possibly influenced by inherent positive bias in LLMs" (P31 §2.1, citing Giorgi et al. 2021; Markowitz et al. 2023; Mitrović et al. 2023). An emotion-aware detector (fine-tuned sentiment PLM) improved detection F1 by up to 9.03% (P31 §5.3.2, Cowap et al. 2023), so affect is a real discriminating signal.
- **Scope:** ChatGPT-era models; reviews, news, Q&A.
- **Actionable rule:** Let the stance match the material: say when something is bad, boring, or annoying. Don't default to an upbeat, even-keeled register, and don't soften a negative judgment with a balancing positive.
- **Caveats:** Professional human writing is often neutral, so neutrality alone is not a tell. RLHF changes the tone of newer models.
- **Strength:** moderate.

### 6. Generic rather than context-tailored content; missing specifics
- **What the paper found:** LLM-generated research summaries "frequently lack detail, particularly in describing the research motivation and methodology, which hampers the provision of fresh insights… these papers often use general terms instead of effectively tailored information relevant to the specific problem context" (P31 §6.1, citing Ma et al. 2023). In news, LLMs produce more "generic" text, and in stories more "irrelevant" text (P31 §6.1, citing Dugan et al. 2023, RoFT).
- **Scope:** ChatGPT academic abstracts; GPT-2/3-era news/story continuations (RoFT).
- **Actionable rule:** Every claim should carry the particular case: the actual method, number, motivation, or constraint. If a sentence could appear unchanged in a paper on a different topic, rewrite it or cut it. In fiction, every detail should matter to the plot or character. Don't add plausible-sounding tangents.
- **Caveats:** Weak human writers are also generic. This is primarily a quality issue, and fixing it helps regardless of provenance.
- **Strength:** moderate (human-evaluator studies, consistent with P28 in the existing guide).

### 7. Fewer hedges and concessive connectives than human scientists
- **What the paper found:** In human scientific writing, "authors are prone to composing lengthy paragraphs and using ambiguous language (Desaire et al. 2023), often incorporating terms like 'but,' 'however,' and 'although'" (P31 §6.1, p.311).
- **Scope:** Desaire et al. 2023: *Science* perspectives articles vs. ChatGPT, chemistry/science domain.
- **Actionable rule:** In argument, show the real tensions: qualifications, exceptions, "but" clauses that reverse or limit a claim. Paragraph length can follow the thought; some long, uneven paragraphs are normal.
- **Caveats:** Domain-specific (science). "However" as a mechanical transition is also an AI cliché in other work, so the point is genuine concession, not the word itself.
- **Strength:** moderate (a single primary study, but a well-known one).

### 8. Uniform, stylistically consistent text (cohesion that is too tight)
- **What the paper found:** "language models tend to produce stylistically consistent texts" (P31 §5.3.1, citing Schuster et al. 2020). TOCSIN (Ma & Wang 2024): "LLM-generated text tends to exhibit higher cohesiveness, while human-written text is more flexible and less cohesive". Deleting 1.5% of tokens changes LLM text's semantics more (P31 §5.2.2, p.303). Uniform Information Density features beat baselines by more than 20% (P31 §5.2.2). Intrinsic dimension of LLM text is about 1.5 units lower than human text (about 9 for human text in alphabetic languages, about 7 for Chinese) (P31 §5.2.2, Tulchinskii et al. 2023).
- **Scope:** Multiple generators (GPT-2 through GPT-3.5/4/Claude 3 for some methods); multi-domain.
- **Actionable rule:** Let information density vary. Mix a short blunt sentence with a dense one, allow an aside, and don't make each sentence a smooth handoff to the next. Avoid connective tissue whose only job is the transition ("Building on this,", "This highlights…").
- **Caveats:** These are model-internal statistics. A writer can't target "intrinsic dimension" directly, and these results translate only loosely into editorial advice. The ID detector degrades on high-temperature generators.
- **Strength:** moderate for the existence of the signal; weak for any specific writing rule derived from it.

### 9. Fewer grammatical errors
- **What the paper found:** GECScore (Wu et al. 2024a): "human-written texts often contain more grammatical errors than texts generated by LLMs" (AUROC about 98.6%) (P31 §5.2.3). LLM papers "exhibit fewer grammatical and other types of errors" (P31 §6.1). But "relying solely on grammatical errors as a detection strategy is unreliable" (P31 §6.1, Dugan et al. 2023).
- **Actionable rule:** None. **Do not inject errors** (the brief forbids it, and it would degrade quality). The legitimate takeaway: natural, informal constructions that prescriptive grammar flags (fragments, starting with "And"/"But", contractions, a dangling "which" referring to a whole clause) are fine where the register allows them. Don't over-normalize them away.
- **Strength:** strong as a detector feature; as a writing rule, only the narrow permissive reading is defensible.

### 10. Refusal/disclaimer boilerplate and fabricated-sounding citations
- **What the paper found:** P31 Table 1 (p.278): Refusal example "I'm sorry, but I am an AI language model and do not have access to current dates or events. Is there anything else I can help you with…". The fabrication example invents a plausibly titled paper ("Natural Language Processing: A Comprehensive Overview and Recent Advances" (2023)). In normal operation the human and LLM definitions of NLP are near-identical ("an interdisciplinary subfield of linguistics, computer science, and artificial intelligence" vs. "a field of computer science, artificial intelligence, and linguistics that focuses on").
- **Actionable rule:** Strip assistant meta-talk (AI disclaimers, "Is there anything else…", offers of further help). Never cite a source that has not been verified. Note the title pattern: "X: A Comprehensive Overview and Recent Advances" is the stock LLM-coined title shape.
- **Caveats:** The Table 1 point is that *normal* outputs are indistinguishable. Only refusals and fabrication stand out.
- **Strength:** strong for the boilerplate, weak/anecdotal for the title shape.

### 11. Repeated high-order n-grams / stock phrasing across documents
- **What the paper found:** Gallé et al. 2021: "certain n-grams appear with unusual frequency within LLM-generated text" (repeated high-order n-grams) (P31 §5.2.1). DNA-GPT: each model has a "tendency of generating comparable n-grams". Regenerating from a truncated prefix reproduces the original's n-grams (P30 §4.2.1; P31 §5.2.3). P30 §6.7: for a fixed prompt ("Compose an essay on computers"), LLM essays cluster tightly enough that an instructor could characterize the distribution in advance.
- **Scope:** GPT-2 through GPT-4, LLaMA, NeoX.
- **Actionable rule:** Avoid the default phrasing a model would produce for this prompt. If the first wording that comes to mind is the one any writer would reach for on this topic, find the specific one. Don't open with the prompt's own words restated. Repeated multi-word phrases within one document (the same 4–6-word frame reused) should be varied or cut.
- **Caveats:** Human formulaic genres (legal, boilerplate) also repeat n-grams. P14 §4.1 notes that repeated n-grams in human text can even trigger watermark false positives.
- **Strength:** moderate to strong (several independent detection methods depend on this).

### 12. Predictable, top-ranked word choices (GLTR)
- **What the paper found:** "unlike language models, human writers tend to use low-probability and low-ranking words much more frequently" (P30 §4.2.1, GLTR). ChatGPT texts show lower perplexity, while student responses show "more evenly distributed scores" (P31 §5.2.2, HowkGPT). With GLTR visualizations, human detection rose from 54% to 72% (P31 §5.2.2).
- **Actionable rule:** Where several words are correct, prefer the precise, less expected one over the safe default ("gutted" vs. "significantly reduced", "the bill doubled" vs. "costs increased substantially"). Don't choose rare words for their own sake; precision is the criterion.
- **Caveats:** Perplexity alone is insufficient, because prompts can push LLM perplexity up (Hans et al. 2024, Binoculars; P31 §5.2.2). Non-native writers have low perplexity (P30 §6.4). P31 itself garbles the entropy direction ("High entropy … likely to have been generated by an LLM", §5.2.2), which contradicts GLTR's logic (low entropy = model-confident). Treat that P31 sentence as an error.
- **Strength:** strong as a statistical signal; moderate as a writing rule.

### 13. LLM-preferred text survives LLM rewriting nearly unchanged
- **What the paper found:** "texts rewritten and edited by an LLM tend to undergo fewer modifications than human-written texts, as LLMs favor their own generative logic" (P31 §5.2.3, Raidar/Mao et al. 2024; Zhu et al. 2023).
- **Actionable rule (process):** If a model "polishing" pass barely changes a passage, that passage is already in the model's preferred form. That makes it the place to look for default phrasing to replace with specific content. For the skill: don't expect a model's self-revision to remove its own patterns. Revise against an explicit checklist, not "make it better".
- **Strength:** moderate (an indirect inference).

---

## B. Human-text features (what human writing does that LLM writing lacks)

| Feature | Source | Note |
|---|---|---|
| Uses lower-probability, lower-rank words more often | P30 §4.2.1 (GLTR) | Precision and surprise, not obscurity |
| More adverbs and more punctuation | P31 §2.1 | Stance adverbs, varied internal punctuation |
| More emotional intensity; not uniformly positive | P31 §2.1, §5.3.2 | |
| Concessive connectives ("but", "however", "although") and hedged/ambiguous language in science writing; long paragraphs | P31 §6.1 (Desaire 2023) | |
| Less tight cohesion; more "flexible" text | P31 §5.2.2 (TOCSIN) | Allows digressions and asides |
| Higher intrinsic dimensionality (about 1.5 units higher) | P31 §5.2.2 | Hard to target directly |
| Tailored, problem-specific detail (motivation, method) | P31 §6.1 | |
| Reflects "personal knowledge, cultural milieu, and emotional disposition" | P31 §2.1 definition | Definitional, not empirical |
| Domain-specific terminology (field bigrams) | P31 §5.2.1 | |
| Occasional grammatical irregularity | P31 §5.2.3 | Never fake it (see A9) |
| Spoken vs. written stylistic differences matter | P31 §4 (HANSEN) | Register-sensitivity |

---

## C. Things that do NOT work or backfire

1. **Surface edits (whitespace, misspellings, homoglyphs, zero-width characters, emoji-insertion tricks).** P14 §5: these can be neutralized by normalization, and "changing the spelling of many words is likely to severely degrade the quality of text". P31 §8.2 reports that homoglyphs and misspellings cut one detector's recall from 97.44% to 0.26% and 22.68%. That is a trick, and it degrades the text. Out of scope for an editorial skill and harmful to readers.
2. **Light paraphrase / synonym swapping of a model draft.** P16 §4 and human study (§5, Fig. 4): 14 expert graduate-student paraphrasers, with P-SP similarity >0.86 to the source, still left the watermark detectable after about 800 tokens, because "paraphrases are statistically likely to leak n-grams or even longer fragments of the original text". Machine paraphrase (Dipper/GPT) dropped AUC by only 0.05–0.15 at 200 tokens, and AUC recovered to >0.9 by 600 tokens. Kulkarni et al. (P31 §8.2): synonym substitution "had no effect on Grover's detection". **Implication for the skill:** sentence-by-sentence rewording of an AI draft keeps its structure, sequencing and n-grams. Real revision means reworking the plan and the content (what is said, in what order, with which specifics), not the wording of each sentence.
3. **Copy-paste mixing.** Inserting AI spans into human text leaves locally detectable windows (P16 §4.2, P30 §5.3). Uniform human framing does not hide uniform AI paragraphs.
4. **Recursive paraphrasing** eventually removes signals but "invariably introduces alterations in the original text's meaning" (P30 §6.5). That violates the skill's fact-preservation requirement.
5. **Asking a model whether text is AI.** GPT-4 labeled about 95% of human texts as LLM-generated, and ChatGPT labeled about 50% of LLM texts as human (P31 §5.3.3, Bhattacharjee & Liu 2023). GPT-4-Turbo scored below 50% accuracy (ArguGPT). A model self-check is not a valid acceptance test for the skill.
6. **Judging by style alone flags non-native and constrained writers** (P30 §6.2/6.4; P31 §8.1; P14 §7). Liang et al.: TOEFL essays were misclassified at high rates. Also, "effective prompt strategies can mitigate this bias" but also let generated text bypass detection (P31 §8.1). Don't push writers to inflate vocabulary to look "human".
7. **Grammar as a criterion** is unreliable on its own (P31 §6.1, Dugan et al.).
8. **Complex prompts already defeat detectors** (P31 §8.2, Guo 2023; Lu et al. 2023 SCO: AUC −0.54). This is evidence that prompt-level style instruction can move output away from default patterns. It supports the skill's premise but is not itself a writing rule.

---

## D. Statistical / watermark / theory papers: what translates to writing

- **P14 (Maryland watermark):** Little. One transferable idea: **low-entropy text is indistinguishable by construction.** Human and machine produce the same completion for formulaic sequences ("The quick brown fox…", code loops; §1.2), and undetectable outputs "typically involve data memorization" (§3). For writing: formulaic and boilerplate passages are not where AI-ness lives. It lives in the open choices (framing, examples, word choice where many options exist). Focus revision effort there. Also (§7): post-hoc detectors rely on the model being "biased away from human text… such as low variation in perplexity across sentences", which loosely supports varying sentence-level predictability.
- **P15 (distortion-free watermarks):** Almost nothing. Two side notes: (a) instruction-tuned responses (Alpaca-7B) have much lower per-token entropy (0.28) than base-model text (LLaMA 0.59, OPT 0.67; App. §D). Assistant-style answers are more predictable than open text, consistent with A12. (b) Alpaca separates list items "by the same recurring token", and with hashing (k=1) lists "degenerate into repetition" (Fig. 14). That is a sampler artifact, not a style rule. Nothing else usable.
- **P16 (reliability of watermarks):** See C2. The writing-relevant result: **human rewriting that preserves sentence-level meaning and length still leaks the source's n-grams.** Rewrite from intent rather than from the AI sentence. Otherwise nothing.
- **P30 theory (§3, §6.3):** When human and machine distributions overlap, detection is impossible; with enough samples or length it is almost always possible. Takeaway: patterns show up in aggregate over long texts. The skill should check for **document-level repetition of habits** (the same move recurring every paragraph) rather than only polishing single sentences.

---

## E. Cross-check against the existing synthesis (AI-Writing-Recognition-Research-Guide.md)

**Confirmed by my reading:**
- M11 ("word-sequence and linguistic distributions differ… some features are dataset shortcuts") matches P31 §5.2.1 ("effectiveness heavily depends on access to extensive corpus statistics and diverse types of LLMs") and §8.1.
- M12/"Why watermarks are different": accurate. P14 notes low-entropy limits (§1.2), and P16's 800-token human-paraphrase figure supports the guide's "surviving signals after substantial rewriting when enough text remains".
- The P30 entry ("a framework, not an additional independent experiment") is accurate.
- §3 claims "Perfect grammar… means AI" not justified: P31 §6.1 (Dugan) supports this. "The model can recognize its own writing": P31 §5.3.3 strongly supports it (GPT-4 flagged about 95% of human text).
- §4 items 6 (non-native) and 7 (paraphrase) are confirmed.

**Contradictions / corrections:**
- The guide's P15 note is fine, but it omits the Alpaca finding: instruction-tuned responses carry far less watermark potential (0.28 vs. 0.59/0.67). This matters to the guide's claims about watermark reliability on chat-assistant output.
- The guide implies P31 offers a coherent linguistic picture. In fact P31 contradicts itself (limited vocabulary §2.1 vs. "broader variety of expression" §6.1) and misstates the entropy direction (§5.2.2). The guide should flag that P31's feature claims are secondhand and internally inconsistent.
- The guide's em-dash row says "no universal punctuation rule". P31 §2.1 goes further: 2023 evidence says LLMs use **less** punctuation than humans. That is the opposite of current em-dash folklore, a useful corrective the guide doesn't state.
- P30 §5.1.3 states that human paraphrasers are "more capable of fooling a detector" than machine paraphrasers. P16's actual data (human writers were still detected after about 800 tokens; machine paraphrase AUC recovered by 600 tokens) shows humans need *longer* texts to be caught, not that they escape. The guide does not mention this nuance either way.

**Missed by the guide (and relevant to Shakespeare):**
- P31 §2.1's concrete POS profile (more nouns/determiners/auxiliaries/coordinators, fewer adverbs/punctuation), the 2× length finding, lower emotional intensity/positive bias, and syntactic simplicity/passive/narrativity. The guide has no row for length, POS, or affect intensity (H9 covers tone only qualitatively).
- P31 §6.1: human scientific prose uses concessive "but/however/although" and longer, more ambiguous paragraphs (Desaire 2023). LLM summaries omit motivation and methodology.
- Cohesion/UID/intrinsic-dimension signals (TOCSIN, UID, PHD). The guide lists model-probability methods but not the "too cohesive / too uniform information density" family.
- Rewrite-stability (Raidar) appears only as a detector (M7). The guide misses its practical implication: model self-polishing won't remove model patterns.
- P16: light human paraphrase leaks n-grams. This is the strongest evidence in this batch that **sentence-level rewording is not real revision**.
- P30 §6.7: outputs for the same prompt cluster tightly. This supports the rule "don't take the default angle a prompt invites".

---

## 5-line summary
1. The watermark papers (P14–16) give almost no style rules. Their one transferable lesson is that rewording an AI draft sentence by sentence leaks its n-grams and structure (P16: expert human paraphrases were still detected after about 800 tokens), so real revision has to rework content and plan, not wording.
2. P31 is the only source in this batch with a linguistic profile: about 2× length, narrower vocabulary, more nouns/determiners/auxiliaries/coordinators, fewer adverbs and *less* punctuation, simpler syntax, low emotional intensity and positivity, generic rather than problem-specific content. All of it is secondhand, GPT-3.5-era evidence.
3. Human-text markers worth encoding: precise, lower-probability word choices (GLTR); stance adverbs and varied punctuation; genuine concession ("but/although") and uneven paragraphs; uneven information density and looser cohesion; field-specific terminology and concrete motivation/method detail.
4. What doesn't work: synonym swaps, misspellings/homoglyphs, injected errors, recursive paraphrase (it destroys meaning), inflating vocabulary (non-native writers get flagged anyway), and asking a model to judge AI-ness (GPT-4 called about 95% of human texts AI).
5. Corrections to the existing guide: P31 contradicts itself on vocabulary breadth and gets the entropy direction backwards. 2023 data says LLMs under-punctuate, contrary to em-dash lore. The guide misses the length, POS, affect, cohesion and rewrite-stability findings.
