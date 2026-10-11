# Batch B — Benchmark papers (MAGE, M4, MULTITuDE, RAID, DetectRL)

Papers: 17 = MULTITuDE (Macko et al., EMNLP 2023); 18 = MAGE (Li et al., ACL 2024); 19 = M4 (Wang et al., EACL 2024); 20 = RAID (Dugan et al., ACL 2024); 21 = DetectRL (Wu et al., NeurIPS 2024 D&B).

Overall character of this batch: these are detection *benchmarks*, not stylistic studies. Their linguistic analyses are thin, and two of them (MAGE, DetectRL) mainly show that surface features (POS, NER, sentiment, lexical diversity) *converge* between humans and LLMs once you pool domains and models. What does survive pooling is low perplexity / high predictability, repetitiveness (Self-BLEU), narrower vocabulary, and a polished-but-generic register. The qualitative example tables in M4 (App. H) and RAID (App. H) are the richest source of writer-actionable tells; I flag those entries as illustrative (single examples, my reading, no statistics in the paper).

---

## A. Patterns (AI tells a writer can act on)

### 1. Low perplexity: predictable word choice
- **What the paper found:** MAGE §7.2, Fig. 7–8: machine text has markedly lower mean perplexity than human text, and that holds "regardless of the text domain or the language model". The authors call it the one feature that stays general once everything else converges. RAID Table 3: mean PPL by LLaMA-7B is 9.09 for humans versus 3.33–7.74 for most models (MPT is the exception at 14.0). By GPT-2-XL it is 21.2 for humans versus 8.1–13.4 for the GPT family. App. G.1/Fig. 10: "human-written text is still significantly less likely than machine-generated text."
- **Scope:** MAGE has 27 LLMs (GPT-3.5, LLaMA, OPT, FLAN-T5, etc.), 10 English domains and 2023 models. RAID has 11 models including GPT-4, ChatGPT, LLaMA-2-70B-chat, Mistral, MPT and Cohere, across 8 domains.
- **Actionable rule:** Where the meaning allows, choose the specific, correct word over the statistically safest one. Name the actual thing ("the Metternich Stela", "11 days", "a 12.1-inch display") instead of a generic category ("a powerful framework", "various methods").
- **Caveats:** This is a cost trap as well as a target. MAGE Fig. 7–8 shows that *human* texts with low perplexity are exactly the ones detectors misflag, concentrated in ROC stories, XSum news and TLDR (§6.3). Formulaic genres are naturally low-perplexity. Don't add oddness for its own sake. Specificity is the legitimate route.
- **Strength:** strong (two large benchmarks, many models).

### 2. Repetitiveness within and across outputs (Self-BLEU)
- **What the paper found:** RAID Table 3 / §4.1 reports Self-BLEU of 7.64 for humans against 9.4–23.9 for models (ChatGPT 10.3, GPT-4 9.42, LLaMA-chat 10.6, Mistral 19.1, GPT-2 23.9). The only model below the human figure is MPT-chat at 5.39. "Models are more repetitive than humans." App. G.1/Fig. 11: "human-written text is by far the least repetitive"; continuation (base) models are more repetitive than chat models. Generating with a repetition penalty (θ=1.2) cuts accuracy by up to 32 points across all detectors (§6 Finding 3, Fig. 5). Sampling with a penalty makes text that "often sounds more human-like" (citing Keskar 2019).
- **Scope:** RAID, English, 2023 models.
- **Actionable rule:** Don't reuse the same words, phrases or sentence frames inside one piece. In particular, don't restate the title or prompt wording in the body, and don't repeat the key noun phrase in every sentence (see the M4 WikiHow example below, where "Wii points" and "Virtual Console" are restated over and over). Vary how sentences open and how they are built.
- **Caveats:** This is a decoding effect. A writer controls the equivalent at the level of words and frames, not at the sampling level. Prompt engineering in RAID had to tell chat models "Do not repeat the title" (App. E.3, Table 12), so echoing the title is a known LLM habit.
- **Strength:** strong (RAID, 6M generations).

### 3. Narrower vocabulary per document
- **What the paper found:** M4 §3.2.1 and App. Table 9: human text "had a richer vocabulary than each of the six generators". English unique unigrams per domain: Wikipedia 144,523 human against 34k–65k per model. Table 10, per-document unique unigrams across all domains: human 228, ChatGPT 170, davinci-003 160, Dolly 154, BLOOMz 136, Cohere 115. Bigrams: human 457 against 207–315. Only the union of *all* generators matched human vocabulary. MULTITuDE App. Table 8: unique-word ratio is 0.69 for humans against 0.59–0.68 for models (GPT-4 0.64, ChatGPT 0.65, Vicuna 0.62).
- **Scope:** M4 is English (5 domains) with ChatGPT, davinci-003, Cohere, Dolly-v2 and BLOOMz. MULTITuDE covers news in 11 languages.
- **Actionable rule:** Use the domain's real, concrete vocabulary: proper names, technical terms, numbers, dates. Don't let one stock verb or adjective carry a whole piece.
- **Caveats:** The per-document counts are confounded by length (generators were controlled to at least 1,000 characters, but lengths still differ). The MULTITuDE difference is small, and DetectRL App. D.6/Fig. 7 found "almost no significant variation" in lexical diversity, which clusters around 0.7 for GPT-3.5, Claude-instant, PaLM-2 and Llama-2. So per-document TTR is a weak tell in the 2023–24 chat models. The M4 effect is clearest for per-domain type counts.
- **Strength:** moderate (M4 clear; DetectRL/MULTITuDE show small or no effect).

### 4. Fixed, task-default rhetorical scaffolding (open with a summary, close with a wrap-up)
- **What the paper found (illustrative, M4 App. H, Tables 18–19; RAID App. H, Table 17):**
  - ChatGPT peer reviews (M4 p. 29–30) open by restating the paper's title and problem and close with "Overall, the paper provides a valuable contribution to the field…" / "Overall, the paper is a strong contribution to the field…". They hedge with "further research is needed to fully explore its potential and limitations", praise in triplets ("well-motivated, well-executed, and well-evaluated"), and use template weaknesses ("it would have been beneficial if the authors had provided more in-depth analysis", "would have benefited from a more detailed discussion of the limitations and potential future directions"). The human review is terse and fragmentary ("- Weaknesses: amount of novel content. Clarity in some sections."), has typos, and makes concrete demands (asks the authors to compare with Yamada et al. 2016 and to test on parsing, coreference and SRL).
  - ChatGPT WikiHow (M4 p. 28) opens with "Have you ever experienced a damaged laptop display hinge? If so, you know how frustrating it can be…", then "Fortunately, there's a workaround…", and ends with "With these simple steps, you can…" plus "Good luck!". The davinci WikiHow ends "Now, you know how to… Have fun!"
  - ChatGPT abstract (M4 p. 25): "Our methodology involves a careful combination of intuition, formalism, and numerical simulations." "The ideas proposed in this work are relevant to the understanding of… as well as to quantum computing and information."
  - Chat-model Reddit posts (RAID Table 17): ChatGPT, GPT-4, Mistral-chat, MPT-chat and LLaMA-chat all follow the same frame. They greet ("Hello everyone", "Hey fellow Redditors", "Hello fellow VW fans!"), add an enthusiasm filler ("absolutely loving it! The production, the melodies, and the lyrics are just top-notch"), make a polite ask ("I would greatly appreciate it", "point me in the right direction") and close with "Thanks in advance!". Five chat models produced nearly the same post.
- **Scope:** ChatGPT/GPT-4/davinci and open chat models, 2023. These are single examples, not measured frequencies.
- **Actionable rule:** Cut the hook question, the "Fortunately," pivot, the "Overall, …" summary close and the sign-off ("Good luck!", "Have fun!", "Thanks in advance!" unless the genre really uses it). Replace stock praise and stock weakness sentences with the specific point. Avoid adjective triplets ("well-motivated, well-executed, and well-evaluated"; "intuition, formalism, and numerical simulations").
- **Caveats:** Real Reddit posts do sometimes say "thanks". The tell is the whole template appearing together. These are qualitative examples, so treat them as consistent with patterns other papers quantify, not as standalone evidence.
- **Strength:** weak as evidence (illustrative examples), but consistent across models and two papers.

### 5. Generic "powerful framework" academic boilerplate
- **What the paper found (illustrative, DetectRL App. F.3, Tables 14–15):** The PaLM-2 direct-prompt abstract reads: "The resolvent algebra is a new mathematical structure that provides a powerful framework for studying quantum systems." The few-shot version says "provides a unified framework…", and the LLM-polished version says "a novel mathematical structure offering a robust framework… rooted in the concept of…". The human original states a concrete defect: the Weyl algebra "neither admits the formulation of physically interesting dynamic laws nor does it incorporate pertinent physical observables such as (bounded functions of) the Hamiltonian." The M4 ChatGPT abstract similarly says "present a theoretical framework for the investigation of other polymer properties that are still poorly understood" and actually misreads "polymer quantum mechanics" as being about polymers (M4 p. 25).
- **Scope:** PaLM-2 and ChatGPT, arXiv abstracts.
- **Actionable rule:** In technical prose, lead with the specific problem or result, not with what kind of thing the work "provides". Delete "powerful/robust/unified/novel framework", "rooted in the concept of" and "relevant to the understanding of" unless you follow them immediately with the concrete content. Note that polishing *adds* these words ("new" became "novel", "powerful" became "robust", "based on the idea" became "rooted in the concept").
- **Caveats:** Single examples. Humans write "framework" too.
- **Strength:** weak (illustrative).

### 6. Smoother, more positive and over-explained content (filler elaboration)
- **What the paper found:** MAGE App. H/Fig. 14: across domains, sentiment converges overall, but "LLMs generally generate more positive texts, especially when creating reviews or comments (Yelp)". In M4's davinci WikiHow (p. 27), each human step gets padded with a justification sentence ("Going online with your Wii allows you to access all the Virtual Console titles…", "This code is what you use to transfer the money…"). The ChatGPT WikiHow restates every step in a "To begin…", "Next,…", "Once the glue has dried,…", "To finalize the repair," frame. The human WikiHow is clipped, digressive and practical ("Don't confuse the setting time of the epoxy (which can be as quick as 5 minutes) with the time until it reaches maximum strength"; "I used an 'improved blood knot' for this").
- **Scope:** MAGE (27 LLMs); the M4 examples are davinci-003 and ChatGPT.
- **Actionable rule:** In reviews and opinion pieces, don't default to positive. Keep the writer's actual verdict, including complaints. In instructions, cut sentences that only explain why an obvious step matters. Keep the non-obvious, experience-based caveat (the "setting time vs. full strength" kind of detail).
- **Caveats:** MAGE says the sentiment difference largely vanishes in aggregate. The positivity skew is strongest in reviews.
- **Strength:** moderate (positivity); weak (padding, illustrative).

### 7. Over-correct grammar in informal genres
- **What the paper found:** MAGE App. H/Fig. 15 used grammar-error-correction edits per text. In informal domains (CMV, Yelp, ELI5, WritingPrompts), "machine-generated texts are equally or even more grammatical". In formal domains (XSum, SQuAD, SciXGen), *human* text was more grammatical. MAGE Table 12: average sentence length is the same (18.90 human vs 18.80 machine), but machine documents are longer (280 vs 232 words; 15.3 vs 13.5 sentences).
- **Scope:** MAGE, 27 LLMs, 10 domains.
- **Actionable rule:** In informal registers (forum posts, reviews, casual Q&A), allow natural conversational syntax: fragments, run-ons where a person would use them, contractions, asides. Don't do this by planting errors. Don't pad length. Say it and stop.
- **Caveats:** In formal registers, grammar should stay correct, since humans there were *more* grammatical. Never insert fake typos (see section C).
- **Strength:** moderate.

### 8. Formal registers are where LLM and human text are hardest to separate; informal is where LLM tells show
- **What the paper found:** DetectRL §3.2: zero-shot detectors do better on informal data (Yelp, WritingPrompts) and worse on formal data (arXiv, XSum). Detectors trained on informal data generalise about 10 AUROC points better (§3.3). M4 §5.1 reports WikiHow as the hardest domain and PeerRead the easiest. Humans did worse on arXiv (0.72) than Reddit (0.77), probably because readers "depended less on content signals and more on stylistic cues" for arXiv (M4 §3.2.2).
- **Actionable rule:** Spend the most editing effort on informal and personal genres (social posts, reviews, stories, peer reviews). That is where a generic, polished, upbeat LLM voice clashes most with human norms. In formal genres, focus on content specificity rather than surface style.
- **Strength:** moderate.

### 9. Prompted voice ≠ human voice; specified prompts help
- **What the paper found:** MAGE §6.3/Fig. 2: texts from "specified prompts" (the source named, e.g., "Write an article for BBC News…") were harder to detect (MachineRec 66.9%) than continuation (83.3%) or bare topical prompts (79.9%), "because they follow a detailed prompt condition, making them more similar to human-written texts". By contrast, M4 example p. 24: asking ChatGPT for "an amateurish mediocre voice" produced a cartoonish "Well, let me tell you, it was quite a tragic event…" opener, a factually inverted story (it says Henry killed Montgomery, when Montgomery's lance killed Henry), and an "Overall, it was a tragic event that had a lasting impact…" close. DetectRL F.1: few-shot and "write in human style" (ICO) prompts reduced detector AUROC by only about 1–2%.
- **Actionable rule:** Ground the writing in the concrete target context (venue, audience, real exemplar) rather than adjectives about voice ("casual", "human", "mediocre"). Voice instructions on their own produce caricature, not human texture.
- **Strength:** moderate.

### 10. Factual confabulation dressed as fluent specifics
- **What the paper found (illustrative):** M4 Cohere Wikipedia "Shed (deity)" (p. 26) turns an Egyptian god into a Norse giantess married to Odin, with repetitive "Shed is the goddess of… She is also…" sentences. BLOOMz "Edgehill, Virginia" (p. 31) invents a population of 4,941, says the town lies on Interstate 81 and the James River, and calls it Lee's headquarters. RAID Reddit examples invent band names and albums ("Volcano Witch", "The Velvet Underground"). The human Reddit post names the real album ("Modern vampires of the city") and reasons tentatively.
- **Actionable rule:** Specificity has to be *true*. When adding concrete detail (a rule from patterns 1 and 3), add only facts the author supplied or can verify. Never invent names, numbers or sources to sound specific.
- **Strength:** weak as statistics, but critical as a guardrail for the skill.

---

## B. Human-text features reported

- **Higher perplexity / less predictable wording** (MAGE §7.2; RAID Table 3, Fig. 10).
- **Least repetitive** by Self-BLEU (RAID Fig. 11).
- **Richer vocabulary** per domain and per document (M4 Tables 9–10; MULTITuDE Table 8, UW 0.69).
- **Slightly shorter documents with the same sentence length** (MAGE Table 12). Humans stop sooner.
- **Less grammatically "clean" in informal domains; *more* grammatical in formal ones** (MAGE Fig. 15).
- **Less uniformly positive in reviews** (MAGE Fig. 14).
- **Human texts "inherently contain more adversarial features"**: perturbing human text actually made it *easier* to recognise as human (+10.22 AUROC; DetectRL §3.5). Human text tolerates mixing. Inserting a quarter of LLM sentences into human text barely moved detectors (−3.71), while the reverse moved them a lot (−18.17). The authors attribute this to the "inherent complexity" of human text.
- **Qualitative (M4/RAID examples):** source citations ("Sourced, in part, 'The Death of Henry II of France' Journal of Neurosurgery 12/1992"), exact names and numbers, admitted uncertainty ("his history gets a bit complicated", "I looked it up, and I thought originally… maybe it was…"), first-person method notes ("I used an 'improved blood knot'"), terse fragmentary structure in reviews, concrete requests rather than template critique.

---

## C. Things that do NOT work, backfire, or are cheating

**Detector-evasion tricks (excluded from the skill as cheating, not writing):** RAID §3.6 / App. E.4 lists homoglyphs (Cyrillic look-alikes), zero-width spaces, extra whitespace, random upper/lower swaps, digit shuffling ("2011" became "0346"), article deletion, injected common misspellings, and BERT synonym swaps. DetectRL D.4.3 adds DeepWordBug, TextFooler and TextBugger perturbations, which produce character and word typos ("reolvent", "inversG", "He is based on").
- They are *inconsistent*. Homoglyphs drop Originality from 85.0 to 9.3 but leave GPTZero almost unchanged (66.5 to 66.2). Zero-width spaces push some detectors to 99.9% and others to 0% (RAID Table 16). Synonym swaps and DIPPER paraphrase *raised* RoBERTa-GPT2 accuracy by 16–23 points (RAID Table 6), because the edits made the text look more like the detector's training distribution.
- They degrade the text. RAID's synonym-swap example turns "Paul Walker" into "Scott Davis", "Bringing back" into "Taking down", and "was a great idea" into "was a good thing". Number swaps corrupt facts. TextFooler produces "investigation quantum systems" and "He is based on". The synonym attack only "works" by making prose worse and sometimes false.
- Against supervised detectors they barely matter. DetectRL Table 4: RoBERTa stays above 96% AUROC under perturbation. Applied to *human* text, perturbations made it look *more* human to zero-shot detectors (§3.5), which is evidence that this does not move text toward human style.
- **Verdict:** never apply these to the skill's output. They are not editorial rules.

**Paraphrasing:**
- MAGE §6.3 / Table 5: paraphrasing with gpt-3.5 sentence by sentence moved *human* text's perplexity toward the machine peak (Fig. 9). LLM paraphrase makes human text look machine-like. The skill should not run an "LLM rephrase everything" pass on human drafts.
- DetectRL F.1: DIPPER paraphrase barely moved detectors. "Polish using LLMs" cut about 10% AUROC (and, in the examples, *introduced* "novel", "robust framework" and "rooted in the concept"). Google back-translation cut more than 40% AUROC but produced garbage ("Wel-did numbers", "the countdowner counts", "Hamilton, Hamilton (Limited)"). Rewording for its own sake does not create a human voice.
- RAID Table 6: DIPPER paraphrase sometimes *helped* detectors.

**Prompting for "human style":** DetectRL F.1: few-shot and ICO "write in human style" prompts reduced AUROC by only about 1–2%. "Efforts to guide models to mimic human writing through such instructions may not effectively evade detection." The M4 "amateurish mediocre voice" example produced caricature (see pattern 9).

**Mixing models:** DetectRL F.1: sentence-mixing outputs of several LLMs did not confuse detectors.

**Relying on surface statistics:** MAGE §7.1 / Fig. 5, 13: POS, named-entity, constituent and word-frequency distributions converge across domains and models. Shortcuts like ORDINAL or DATE entity rates (Fig. 6) appear only within one domain and one model. Tuning POS ratios or entity counts is not a general strategy.

**False-positive warnings (do not over-correct toward "weird"):**
- MAGE §6.3: the best detector misclassified 61.95% of human text from unseen domains; low-perplexity human genres (short stories, BBC summaries, TLDR) were flagged most.
- RAID Table 8: per-domain false positive rates reach 20.4% (RADAR on Reviews), 33.4% (GLTR on Recipes) and 48–52% (ZeroGPT on Wiki and Recipes).
- RAID ethics section and MAGE §2 (citing Liang et al. 2023): detectors are biased against non-native English writers. MULTITuDE ethics section: dialects, slang and code-switching are at risk.
- Implication: plain, formulaic, correct prose is not proof of AI. The skill should fix *patterns* (template scaffolding, generic claims, repetition), not make clean writing eccentric.

---

## D. Statistical / multilingual takeaways that translate (briefly)

- **Decoding (RAID §3.5, Finding 3):** greedy decoding is the most detectable; sampling plus repetition penalty is the least. Writing translation: the default, most-probable continuation *and* reusing earlier tokens are the two machine signatures. Prefer the precise word, and don't recycle phrases. (Already covered by patterns 1 and 2.)
- **Model families differ (MULTITuDE §5.4 Table 6; M4 §5.2; DetectRL §3.2):** OpenAI-derived models (davinci, ChatGPT, GPT-4, Alpaca, Vicuna) form one stylistic cluster and Meta/OPT models another. ChatGPT and Cohere share patterns. Claude-instant is statistically distinct (detectors fail on it). BLOOMz is unlike all the others. Translation: an "AI tells" list derived from OpenAI outputs will not cover every model. Prefer model-agnostic rules (specificity, non-repetition, no template scaffolding).
- **Multilingual (MULTITuDE, M4 §5.4):** detection transfers along language family and script. English is an outlier. These papers report **no language-specific stylistic tells** usable for writing guidance. Nothing actionable beyond the fact that English-derived rules may not transfer to other languages.
- **Length (M4 §5.6; DetectRL §3.4):** longer texts are more detectable (accuracy fell 4.5 points going from 1,000 to 125 characters). Machine signals accumulate. Translation: the patterns above compound over length, so long-form pieces need the most consistent editing. Don't pad (MAGE: machine docs about 20% longer).
- **Model updates (M4 §5.5):** a detector trained on March-2023 ChatGPT still caught September-2023 ChatGPT (99.4% accuracy). Style fingerprints persist across versions of the same model.
- **Human judges (MAGE Table 1; M4 Table 2):** expert linguistics annotators in MAGE scored 54.5% average recall, roughly chance. M4 annotators averaged 0.77 on Reddit and 0.72 on arXiv. Annotators who knew "ChatGPT generation patterns" did best (up to 0.94), so the stylistic tells are learnable and real to informed readers even when untrained readers miss them.

---

## 5-line summary
1. Across MAGE/M4/RAID, the signals that survive pooling of domains and models are predictability (lower perplexity), repetitiveness (Self-BLEU about 9–24 for models vs 7.6 for humans) and narrower vocabulary (per-doc unique words 228 human vs 115–170). Surface POS, NER, sentiment and lexical-diversity differences mostly vanish (MAGE §7.1, DetectRL D.6).
2. Writer-actionable rules: pick the specific, *true* word or name over the safe default. Don't recycle phrases or echo the title. Cut template scaffolding (hook question, "Fortunately," "Overall, …" wrap-up, "Thanks in advance!/Good luck!") and "powerful/robust/unified framework" boilerplate. Don't default to positive, and don't pad. Machine docs run about 20% longer at the same sentence length.
3. In informal genres LLMs are *over*-grammatical and uniformly upbeat, while humans are terse, digressive, concrete and hedged. Formal genres converge, so effort there should go into content specificity rather than surface style.
4. Homoglyphs, zero-width spaces, misspellings, digit swaps, article deletion and BERT synonym swaps are cheating with inconsistent effect (some *raise* detection), and they corrupt meaning ("Paul Walker" became "Scott Davis"). LLM polishing *adds* AI boilerplate, back-translation produces garbage, and "write like a human" prompts barely help (DetectRL F.1). Exclude all of them.
5. False positives are severe: up to 62% of out-of-domain human text was flagged (MAGE), with 20–52% FPR in some domains (RAID), concentrated on low-perplexity formulaic genres and non-native writers. The skill should fix patterns, not make clean prose eccentric. Specificity must never become invented detail, since fabricated specifics were common in the M4 and RAID examples.
