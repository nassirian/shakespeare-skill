# Batch D — Robustness, rewriting, paraphrasing, practical detector testing

Papers: 05 RADAR (Hu et al., NeurIPS 2023), 08 DNA-GPT (Yang et al., ICLR 2024 preprint), 10 Raidar (Mao et al., ICLR 2024), 23 Sadasivan et al. "Can AI-generated text be reliably detected?" (v4, 2025), 24 Chakraborty et al. "On the possibilities…" (2023), 25 Krishna et al. DIPPER / retrieval (NeurIPS 2023), 26 Weber-Wulff et al. "Testing of detection tools" (2023), 27 Tufts et al. "Practical examination of detectors" (2025).

Overall character of this batch: these are mostly detector/attack papers, so they report few lexical tells directly. The usable material is (a) the qualitative rewrite and regeneration examples in 08, 10, 05 and 23, which show what an LLM does to text, and (b) the robustness results, which show what surface edits leave in place. The two most useful papers for the skill are 10 (Raidar) and 08 (DNA-GPT).

---

## A. Pattern entries

### A1. Predictable continuation: the model writes what any model would write next
- **What the paper found (08, §3, Fig. 1, App. D Tables 14–16):** Given the first half of a text, GPT-3.5/GPT-4 regenerate the second half with heavy n-gram overlap with an AI-written original. The overlap is much lower for a human-written original. Black-box AUROC is 96–99.6 on Reddit-ELI5 and scientific abstracts (Table 1). The authors state a "Likelihood-Gap Hypothesis": machine continuations have systematically higher log-likelihood than human ones given the same prefix (§3, Fig. 2). Evidence examples where regenerations reproduce the original nearly verbatim:
  - AI abstract ending: "Our findings highlight the importance of considering human dimensions in wildlife translocation planning and implementation to improve conservation outcomes." The regeneration ends identically, except for "enhance" in place of "improve" (Table 14, BScore 0.396 vs 0.004 for the human version).
  - AI medical answer: "Ultimately, the decision to use volumetric analysis should be made on a case-by-case basis, in consultation with a healthcare provider." This was regenerated almost word for word in 2 of 2 shown samples (Table 15).
  - AI answer: "Attempting to use the device without proper training and certification can lead to serious injury or even death. Therefore, it is essential to…" appears in both regenerations (Table 16).
- **Scope:** text-davinci-003, GPT-3.5-turbo, GPT-4-0314, LLaMA-13B, GPT-NeoX-20B. English: Reddit ELI5 (2022–23), Nature abstracts (Apr 2023), PubMedQA, XSum. German: WMT16. Temperature 0.7. Human comparison is the original human continuation.
- **Actionable rule:** At paragraph ends and conclusions, test each sentence by asking whether a generic writer on this topic would produce it. If so, replace it with the specific point this text alone can make: a number, a named exception, a concrete limit. Cut "Ultimately, X should be decided case by case", "Our findings highlight the importance of…", and "Therefore, it is essential to…" closers.
- **Caveats:** The method needs the generating model and the prompt (performance drops without the "golden prompt"). Memorized human text (WikiText) is also regenerated verbatim, which produced false positives in App. B.2 (13/100 WikiText prefixes produced 3-sentence verbatim copies). Human formulaic genres will share some of this.
- **Strength:** moderate–strong (several models and datasets, ~150–300 samples each, explicit qualitative evidence).

### A2. Formulaic safety, recommendation and summary closers
- **What the paper found (08, Tables 15–16):** GPT continuations default to generic advisory endings even where the human text ends on data. Examples: "It is important to note that this type of training may not fully prepare individuals for real-life emergency situations… It is still highly recommended to receive formal CPR and first aid training from certified instructors"; "It is important to seek proper training and education before attempting to use any medical device"; "Additionally, healthcare professionals should also be aware of the potential complications". The human original instead ends: "Operating errors (n = 91) were frequently not recognized and corrected (n = 77). Improvements in labeling and the quality of instructional photographs may reduce individual error…"
- **Scope:** GPT-3.5-turbo on PubMedQA, 2023.
- **Actionable rule:** Delete reflexive caveats ("It is important to note…", "consult a professional", "should also be aware of") unless the reader needs them. End on the finding, the number or the concrete implication.
- **Caveats:** This is qualitative, from a handful of examples. Medical writing legitimately carries caveats.
- **Strength:** weak–moderate (illustrative examples, not counted).

### A3. LLM "polish" inflates diction and adds stock evaluative phrasing
- **What the paper found (10, Fig. 1, Fig. 3; examples shown with GPT-3.5-turbo rewrites of human text):**
  - Abstract: "has been used frequently" became "has frequently been employed"; "Fairness and privacy are two big concerns" became "raising significant concerns regarding fairness and privacy"; "show good results" became "demonstrate promising privacy preservation"; "require high computation resources" became "demand substantial computational resources"; "we design a fast, fair, flexible and private data generation method" became "To address these limitations, we present a novel approach to data generation that prioritizes speed, fairness, flexibility, and privacy"; "We show the effectiveness" became "we showcase the effectiveness"; and the rewrite added "Importantly, we demonstrate that models… excel in real-world application scenarios".
  - Student essay: "gained popularity" became "gained significant popularity"; "using organically certified methods" became "adhering to organic certification standards"; "some of the challenges faced by" became "the challenges encountered by"; "how conventional producers can change" became "Moreover, I will explore how conventional producers can modify"; "the advantages and disadvantages" became "evaluate the advantages and disadvantages".
  - Non-native academic sentence: "Last but not the least, since the issues centralised in this paper requests…" became "Lastly, it is important to highlight that this paper identifies the need… The aim is to develop a more comprehensive and innovative framework…"
- **Scope:** GPT-3.5-turbo, prompts "Help me polish this", "Rewrite this for me", "Refine this for me please". Domains: news, creative writing, student essays (BAWE), code, Yelp, ICLR abstracts.
- **Actionable rule:** When revising, keep the plain verb (use, show, need, change, find). Do not upgrade to employ, demonstrate, demand, modify, showcase or encounter. Do not insert intensifiers ("significant", "substantial", "novel", "importantly", "crucial") or "To address these limitations," transitions that the original did not need.
- **Caveats:** These are examples from figures, not frequency counts. Formal registers use some of these words legitimately.
- **Strength:** moderate. The direction is backed by the statistically significant edit-distance gap (Table 14, p = 2e-13), but the word lists are illustrative.

### A4. Fragment, rhythm and voice flattening in narrative and informal text
- **What the paper found (10, Fig. 3 creative-writing row):** The human original "The two started yelling back and forth. At me. At each other. I zoned out, closed my eyes. I blocked them out and drew my gun." was rewritten by GPT-3.5 as "The two engaged in a heated exchange, their voices reverberating in my ears. They directed their anger towards me, throwing accusatory words in my direction. Simultaneously, they turned their anger on each other, unleashing a barrage of insults. Overwhelmed by the commotion, I instinctively tuned out their voices, shutting my eyes and concentrating on blocking out the chaotic scene unfolding before me. In an effort to regain control of the situation, I reached for my gun." The rewrite does four things:
  - It removes fragments.
  - It adds participial clauses ("…, unleashing a barrage of insults", "…, shutting my eyes and concentrating on…").
  - It adds stock collocations ("heated exchange", "barrage of insults", "chaotic scene unfolding before me").
  - It adds explained motive ("In an effort to regain control of the situation").
  
  In dialogue tags, "insisted" became "insisted, intrigued" and "said Paul Raisler" became "emphasized Paul Raisler".
- **Scope:** GPT-3.5-turbo; WritingPrompts (text-davinci-003 data from Ghostbuster); Reuters news.
- **Actionable rule:**
  - Keep deliberate fragments and short repeated beats.
  - Do not convert action into participial chains.
  - Do not explain a character's motive when the action already shows it.
  - Keep "said" and do not upgrade it to emphasized, insisted or noted.
  - Cut stock collocations such as "heated exchange", "barrage of", "unfolding before me" and "in an effort to".
- **Caveats:** This rests on a single vivid example, though it matches the paper-wide finding that human text is edited more.
- **Strength:** weak–moderate.

### A5. Normalizing informal reviews into a concessive "Despite X and Y, Z" template
- **What the paper found (10, Fig. 1; Fig. 3 Yelp row):** The human review "Ok yeah, the service can be a little high falutin', and the wait is painful but this is THE BEST BURGER EVER. That's all you need to know. The BEST." was rewritten as "Despite the slightly pretentious service and long wait, this restaurant undeniably serves the best burger you will ever taste." The GPT-written review was nearly invariant: "Despite pretentious service and long wait, this place serves the best burger you'll ever taste." The human review "Really nice place to get a pedicure! People are very friendly and it is a relaxing environment. Definitely recommend…" became "Highly recommend this place for a clean and relaxing pedicure experience. Friendly staff and great ambiance."
- **Scope:** GPT-3.5-turbo, Yelp (2000 human reviews; GPT reviews generated to similar length).
- **Actionable rule:**
  - Keep interjections, caps for emphasis, colloquial words and the writer's own order of thoughts.
  - Avoid collapsing mixed opinions into one "Despite A and B, [verdict]" sentence.
  - Avoid "undeniably", "experience" as a filler noun, and "great ambiance"-style stock pairs.
- **Caveats:** This applies to informal genres only. The concessive frame is normal English.
- **Strength:** weak–moderate (examples).

### A6. Nominalization of stance
- **What the paper found (10, Fig. 3 news row):** "we seriously doubt that the regulations will work, meet consumer demands or be accepted by the private sector unless the administration radically changes its approach immediately" became "the alliance strongly questions the efficacy, consumer satisfaction, and industry acceptance of the regulations". Clause-level claims were turned into a noun list.
- **Scope:** GPT-3.5-turbo, Reuters.
- **Actionable rule:** Keep claims as clauses with verbs ("will work", "be accepted"). Do not compress them into abstract noun triplets ("efficacy, satisfaction, and acceptance").
- **Caveats:** This comes from one example. It is consistent with the broader literature on noun-heavy LLM style, but it is not measured here.
- **Strength:** weak.

### A7. Model self-consistency: an LLM barely edits its own kind of text
- **What the paper found (10, §3, Fig. 2, Tables 1, 4, 9, 14):** When asked to rewrite, LLMs change human text much more than AI text. The invariance, equivariance and output-uncertainty gaps are all significant (p = 2.19e-13, 9.21e-7, 5.47e-16). F1 rises by up to 29 points over Ghostbuster/DetectGPT (e.g., code 95.4, Yelp 87.8, arXiv 81.9). The effect transfers across generators (Ada, davinci-002, GPT-3.5, GPT-4-turbo, LLaMA 2), and Claude-written essays score F1 57.8. Non-native ASAP essays and ICLR abstracts are both edited heavily, so the signal is not just "low quality" (Table 10). In a human preference test, machine text was preferred 53.3% of the time for Yelp but only 26.7% for arXiv abstracts (Table 8).
- **Scope:** GPT-3.5-turbo rewriter; texts from 2015–2023 human corpora; paragraph-level (median 21–102 words).
- **Actionable rule:** "Polish this" passes push text toward the model's preferred form, and those edits are exactly what makes text look machine-written. When revising a human draft, make the minimum necessary edits and preserve the author's idiosyncratic but correct choices. When drafting, do not run the model's own output through further "refine" passes and expect it to become less machine-like.
- **Caveats:** This is a detector property. It does not say which specific features LLMs prefer. Adaptive prompts ("Help me rephrase it in human style") defeated a single-prompt detector (code F1 95→34, Yelp 88→61; Table 3). Multi-prompt training restored detection (87–93), so "human style" rewriting changes surface but not deeply.
- **Strength:** strong (ICLR, 6 domains, significance tests, multiple models).

### A8. "Sound more human" prompting produces inflated, adjective-stacked prose
- **What the paper found:**
  - (05, App. D, Table A5) GPT-3.5-turbo was given "Enhance the word choices in the sentence to sound more like that of a human." Its output scored 0.9999 AI probability: "Greetings I would like to express my utmost gratitude for the extraordinary experience… revitalized my fascination for this captivating planet… capturing breathtaking photographs and filming videos that showcased the red planet's impressive terrain fascinating geology and intriguing scientific discoveries. This experience has forever changed my perception of humanity and inspired my passion for space exploration hoping to further contribute to our understanding of the universe and our place within it."
  - (27, §5.2) Appending "Try to sound as human as possible" to prompts for GPT-4o, Llama-3-8B, Mistral-v0.3 and Phi-3 had little effect. Where scores did change, detectability generally went up.
- **Scope:** 05: GPT-3.5-turbo paraphrasing outputs of 8 open models (Xsum, SQuAD, WritingPrompts, TOEFL). 27: 2024 models, 7 tasks, 4 languages, 7 detectors.
- **Actionable rule:**
  - Never "humanize" by adding feeling words and superlatives.
  - Cut stacked evaluative adjectives ("extraordinary", "captivating", "breathtaking", "impressive", "fascinating", "intriguing").
  - Cut gratitude or formal openers ("I would like to express my utmost gratitude").
  - Cut cosmic or transformational closers ("forever changed my perception", "our place within it").
- **Caveats:** Evidence conflicts. A web test cited in 26 (Demers 2023) found that a "beat detection" prompt made 12 of 16 tools call ChatGPT text human, and 10's adaptive prompts evaded a single-prompt detector. These are detector outcomes, not reader judgments.
- **Strength:** moderate (two independent sources, one vivid example).

### A9. Paraphrasers drift facts and add generic dramatic framing
- **What the paper found:**
  - (23, App. B.3, Tables 11–14) Recursive paraphrasing (DIPPER, LLaMA-2-7B-Chat) changed facts: "appendix… cut down" became "a large primary cancer and five smaller growths were removed"; "the 35-year-old" became "The 38-year-old"; "Ireland… Bulgaria and Greece… Aberystwyth… fourth" became "Northern Ireland… Spain and Scotland… Cardiff… fifth" by pp4–pp5. It also appended an irrelevant line: "Would you like to book an appointment with the British Transport Police?"
  - The LLaMA-2 rounds added stock framing: "On the eve of the crucial final match", "could potentially qualify", "Despite their strong campaign so far, the Northern Irish will face a tough challenge against Wales, who have also had a impressive run of form".
  - Content preservation fell with rounds. For DIPPER, 70.2% of pp1 and 61.4% of pp5 were rated 4–5, and 17.5% of pp5 were only "topically related" (Table 7). Perplexity rose from 5.2 to 8.7 (DIPPER) and 10.5 (LLaMA) (Table 3).
  - (25, App. C.2, Table 8) Human raters judged 81.1% of DIPPER paraphrases nearly or approximately equivalent, falling to 70% at L60. Failures: invented proper nouns ("Homing Attack, Slide Attack… Speed Shoes" became "Speed Boost, Super Speed, invincibility meter"); "the stairway of the Great Pyramid… was relocated" became "The Great Pyramid… was moved"; and omitted content.
- **Scope:** OPT-1.3B/13B, GPT-2, GPT-3.5 outputs; XSum, PubMedQA, Kafkai, Wikipedia, ELI5.
- **Actionable rule:**
  - Treat every rewrite pass as a fact risk.
  - After revising, diff names, numbers, places, ages and quantities against the source.
  - Never paraphrase recursively.
  - Do not add stakes framing ("crucial", "on the eve of", "will face a tough challenge") or hedges ("could potentially") that the source lacks.
  - Keep coined or proper names verbatim.
- **Caveats:** The paraphrasers here are older and smaller models. Frontier models drift less, but the risk is the same in kind.
- **Strength:** moderate–strong (human evaluation plus documented examples).

### A10. Rewriting human-authored content is far less detectable than open generation
- **What the paper found (27, §5.3, §6):** "Rewrite the following text to improve clarity and professionalism" applied to human answers cut TPR@1%FPR for the previously strong detectors. Translation outputs were also harder to detect. The authors conclude that "the model is not generating any new ideas, just improving the readability". RADAR's hardest case (05, Table A5, p = 0.0031) was an AI continuation "nearly identical to the original Human-text, except for… a suffix composed of several words".
- **Scope:** GPT-4o, Llama-3-8B, Mistral-7B-v0.3, Phi-3-mini; 2024.
- **Actionable rule:** Human-originated content and structure are what make text read as human. The skill should preserve the author's ideas, ordering and specifics, and limit itself to local fixes rather than regenerating paragraphs.
- **Caveats:** These are detector results, not reader studies. A10 sits in tension with A7: rewriting still leaves model-preferred edits, and Raidar catches them.
- **Strength:** moderate.

### A11. Machine translation leaves machine traces in human writing
- **What the paper found (26, §5.1.1, Table 9):** Across 14 tools, accuracy on human texts written in other languages and machine-translated by DeepL or Google Translate (02-MT) was about 20 points lower than on native English human texts (96% vs ~77–79%). The false-accusation ratio rose from 2.4% to 11.1%.
- **Scope:** 9 authors, 7 source languages, 14 detectors (incl. Turnitin), ChatGPT Feb-2023.
- **Actionable rule:** If a draft was machine-translated, it needs a human-voice pass for idiom, word order and register, with the same discipline as AI text, while keeping meaning.
- **Caveats:** This is small-n (9 documents per class). The paper doesn't say which features carry the signal.
- **Strength:** moderate (peer-reviewed, small sample).

### A12. Length and repetition accumulate the signal
- **What the paper found:**
  - (24, §4, Fig. 2–4) Best-detector AUROC rises from 58% to 97% as the feature n-gram grows from 1 to 6. Pairing two samples raises real-detector AUROC from 73% to 97%. Zero-shot AUROC improves from ~50% to ~90% with sequence length.
  - (10, Fig. 5, 7–9) Longer inputs are generally easier to detect.
  - (25, Fig. 6b) Retrieval needs at least 50 tokens.
  - (23, Fig. 4b) Watermark detection on 50–100 token texts is near random after paraphrasing.
- **Scope:** XSum, SQuAD, IMDb, FakeNews; GPT-2 through Llama-2-70B.
- **Actionable rule:** Single sentences rarely give text away. Repeated habits across a long piece do. In long documents, vary recurring constructions (openers, transitions, paragraph-ending moves) so that no device recurs on schedule.
- **Caveats:** This is a theoretical and statistical result. It does not name which features accumulate.
- **Strength:** strong for the statistical claim; the translation to writing is an inference.

---

## B. Human-text features these papers report

1. **Divergent continuations.** Given the same opening, human writers go somewhere a model would not predict. Their continuations share few long n-grams with model regenerations (08, Fig. 2, Tables 14–16).
2. **Specific data in conclusions.** Example: "Operating errors (n = 91) were frequently not recognized and corrected (n = 77)" and "For jugulotympanic tumours, the preferred method is manual area tracing. However, volumetric changes… may be of less clinical importance than changes in relation to surrounding anatomical structures." These come where GPT wrote "the choice of measurement method should be tailored to the specific type and location…" (08, Table 15).
3. **Fragments and rhythmic repetition.** Example: "At me. At each other." (10, Fig. 3).
4. **Informal emphasis devices.** Caps ("THE BEST BURGER EVER"), dialect ("high falutin'"), interjections ("Ok yeah"), and closing punches ("That's all you need to know. The BEST.") (10, Fig. 1).
5. **Plain dialogue tags and plain verbs.** Examples: "said", "used", "show", "need" (10, Fig. 3).
6. **Idiosyncratic but meaningful constructions.** Run-on academic sentences and terse code names (`x`, `ret += [x]`). An LLM rewrites these heavily, which is itself the human signal (10, Fig. 3; Table 10).
7. **Text that differs from what a model would produce.** Human text is "unfavoured" by the LLM in rewriting; it is not lower quality. Humans preferred the human text in 73.3% of arXiv pairs (10, Table 8).

## C. Things that do NOT work or backfire

1. **Asking the model to "sound human" or "enhance word choices to sound human".** This yields inflated, superlative-stacked prose and is still detected at 0.9999 (05, Table A5). In 27 (§5.2) it has no effect or makes text easier to detect. A conflicting web test is cited in 26 (Demers), and 10's adaptive prompts beat only single-prompt detectors.
2. **Self-polishing with the same model.** LLMs leave their own text nearly unchanged (10). "Polish/refine/rewrite" on human text injects model-preferred edits (A3–A6). 25 (§1) notes that paraphrases by the base LLM remain watermark-detectable.
3. **Synonym swaps and reordering ("patchwriting").** These cut detector accuracy from 74% to 42% (26), and Quillbot cut it to 26%. They do not change what is said. Retrieval still finds 97–98% of DIPPER paraphrases (25, Table 2), and RADAR recovers 0.86 AUROC on paraphrased text (05, Table 2). Surface substitution leaves the content and structure signal. It also amounts to evasion, which is not the skill's goal.
4. **Recursive or multi-pass paraphrasing.** It raises perplexity and causes semantic drift. Wrong names, numbers and places appear by pass 3–5, plus hallucinated sentences (23, App. B.3; 25, App. C.2).
5. **Machine translation as a "humanizer".** Translated human text is flagged more (26).
6. **Simplifying vocabulary.** Low-perplexity, plain non-native writing is misclassified as AI. Prompting it toward "native" phrasing reduced misclassification (24, App. A Remark 2, citing Liang et al. 2023). Plainness alone is not a human signal, and neither is fanciness. Specificity and unpredictability of content matter more.
7. **Character-level tricks (typos, homoglyphs, invisible characters).** These are mentioned only as prior attacks in 27 (§2, citing Wang et al. 2024) and were not tested there. They are also out of scope for the skill.
8. **Assuming a "better" model writes less detectably.** Chatbot Arena quality did not correlate with lower detectability (27, Table 5).

## D. Statistical/theory papers: what translates

- **05 RADAR:** This is a detector-training method. The only writing-relevant material is the A8 example and the finding that instruction-tuned models share a transferable signature (Fig. 3: detectors trained on instruction-tuned models transfer better). That implies chat-tuned style is a common house style, not model-specific.
- **08 DNA-GPT:** Machines maximize likelihood conditional on the prefix and humans do not (Likelihood-Gap Hypothesis). For writing: at each point, prefer the specific, less-expected but correct continuation over the default next move. This applies to endings especially.
- **23 Sadasivan:** AUROC ≤ ½ + TV − TV²/2, and TV between model and human text shrinks with model size (Fig. 9–10). There is no direct writing rule. Its practical writing content is the paraphrase-drift evidence (A9). It also shows a human passage can be spoofed or flagged (§3): prepending one "AI-looking" human passage to other human text raised detector false positives, so false flags on human writing are real.
- **24 Chakraborty:** Detection improves exponentially with sample count (Chernoff information). The writing translation is A12: recurring habits across a document matter more than any single sentence. Nothing lexical.
- **25 DIPPER:** Paraphrase changes unigrams and order but preserves semantics (P-SP; human paraphrase pairs average 0.76). Retrieval on content defeats it. The writing translation is that the "what" and its arrangement survive rewording. A human feel has to come from the author's actual content and choices, not from rewording.

---

## Summary (5 lines)
1. LLMs regenerate their own text almost verbatim, and especially the formulaic endings: "Our findings highlight the importance of…", "Ultimately… case-by-case basis", "It is important to note…/consult a professional". Human continuations diverge into specifics such as numbers and named exceptions. Rule: replace predictable closers with the concrete point (08).
2. "Polish/refine" passes are where the machine fingerprint comes from (10). Human text is edited heavily, toward employ/demonstrate/substantial/novel/showcase, "To address these limitations", participial chains, stock collocations, "said" changed to "emphasized", and fragments and caps removed. The skill should make minimal edits and keep the author's plain verbs, fragments and voice.
3. "Sound more human" prompts backfire, producing stacked superlatives, gratitude openers and cosmic closers that are still detected (05, 27). Synonym swaps and reordering leave content and structure intact and only evade weak detectors (25, 26). Neither is a valid strategy.
4. Every rewrite pass risks factual drift. Recursive paraphrases changed places, ages, diagnoses and invented names, and added "crucial"/"could potentially"/"tough challenge" framing (23, 25). Diff facts after every revision and never paraphrase recursively.
5. Text built on human content (light rewrites, translation of a human source) is hardest to flag (27, 05), and signals accumulate with length (24, 10). The skill should preserve the author's ideas and specifics and vary recurring devices across long pieces rather than regenerate prose.
