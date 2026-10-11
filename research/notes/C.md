# Batch C — Statistical zero-shot detectors: what word-choice predictability says about writing

Papers: 01 GLTR (ACL demo 2019), 02 Grover (NeurIPS 2019), 03 DetectGPT (ICML 2023), 04 DetectLLM (EMNLP Findings 2023), 06 Fast-DetectGPT (ICLR 2024), 09 Binoculars (ICML 2024), 11 Glimpse (ICLR 2025), 12 AdaDetectGPT (NeurIPS 2025), 13 DNA-DetectLLM (NeurIPS 2025).

All nine are detector papers. None was designed to give style advice, and most measure token probabilities under a scoring LM. The usable content splits into three parts: (a) one strong, well-replicated finding about word choice, (b) a few qualitative observations (mostly GLTR, Binoculars, plus example outputs quoted in appendices), and (c) evidence on which domains make human text look machine-like and which "fixes" fail. I have not invented surface patterns the papers do not report.

---

## A. Patterns (machine vs. human)

### 1. Machines choose the top-ranked word. Humans regularly pick words outside the top 100.
- **What the paper found:** GLTR (01, §4, Table 1, Fig. 4): human text "uses words outside of the top 100 predictions 2.41 times as frequently under GPT-2 (1.67 for BERT) as generated text, even compared to sampling with a lower temperature." In a logistic regression, a word outside the top 100 had an odds ratio of 5.32 for "human", and a top-1 word had an odds ratio of 0.09. Rank-bucket features scored AUC 0.87, against 0.63 for bag-of-words. In the Fig. 3 case study the GPT-2 sample has "not a single token… in purple and very few in red", while the NYT article and Nature/Science abstract show a "significantly higher fraction of red and purple (e.g. non-obvious) predictions." Later papers confirm the same signal: average log-rank is the strongest simple baseline (03 Table 1; 04 Table 1, where LogRank beats raw likelihood on every dataset), and log-rank combined with likelihood does better still (04 LRR).
- **Scope:** GPT-2 1.5B (temperature 0.7 and top-40) and the Heliograf templated-news system vs. NYT, Nature/Science abstracts, and a children's-book corpus. 50 docs per source. English, 2019. Replicated for GPT-2 through NeoX-20B, LLaMA-13B, ChatGPT and GPT-4 by 03, 04, 06 and 11.
- **Actionable rule:** At content-bearing positions (verbs, nouns, modifiers, examples), prefer the precise word the meaning calls for over the first word that comes to mind. When a phrase "writes itself", ask whether it is the exact word or only the default one. Function words, names and fixed terms are meant to be predictable, so leave them alone.
- **Caveats:** Humans do not choose rare words at random. The tail words in the human samples are correct in context (see Pattern 4 and §C on rare-word swaps that hurt readability). The effect is measured in aggregate over hundreds of tokens, not per sentence. The scoring model is a proxy (black-box results transfer but are weaker; 03 Fig. 6).
- **Strength:** Strong. Large effect, replicated across many models and datasets for six years.

### 2. Machine text sits at a local probability peak, so any rewording makes it less likely. Human text does not.
- **What the paper found:** DetectGPT (03, §4, Fig. 3): small meaning-preserving rewrites (T5 span-fills) lower the source model's log-probability much more for machine passages than for human ones. For human text the change "may have higher or lower log probability." In Fig. 9 a single threshold (~0.1) separates human and model text across XSum, SQuAD, WritingPrompts and PubMed. The authors' reading (§6) is that the model exposes "its bias toward the specific (and roughly arbitrary, by human standards) phrasing used… LLMs that do not perfectly imitate human writing essentially watermark themselves implicitly." DetectLLM-NPR (04 §3.2) finds the same with log-rank. Machine text is "more susceptible to perturbations."
- **Scope:** GPT-2, OPT-2.7B, Neo-2.7B, GPT-J, NeoX-20B, plus GPT-3 and Jurassic-2 (175B). 150–500 samples per cell. XSum, SQuAD, WritingPrompts, PubMedQA, WMT16 En/De.
- **Actionable rule:** The default phrasing of a model is a set of choices that are each the most probable and none of them motivated. When revising, don't keep a phrase only because it is fluent. Check that each loaded word is there for a reason: a fact, a nuance, the author's voice.
- **Caveats:** This is a property of the whole passage, not of individual words. Random token noise also lowers probability (03 Fig. 7: "random mask filling… performs poorly"). Detectors catch the gap at the data manifold, so noise is not the fix.
- **Strength:** Strong.

### 3. Machines pick the expected word given the context. Humans pick by meaning and intent.
- **What the paper found:** Fast-DetectGPT (06, §1, §2.3) states the hypothesis directly: "machines lean towards tokens with higher statistical probability… while humans individually exhibit no such bias because they craft sentences based on underlying meanings, intentions, and contexts rather than data statistics." LLMs "mirror human collective writing behaviors instead of human individual writing behavior." Fig. 1 shows a per-token z-score of the actual token against sampled alternatives. Machine text "typically hovers around 3, whereas human-generated texts exhibit curvatures close to 0." Results: 0.989 AUROC on five open models, 0.96 on ChatGPT and 0.91 on GPT-4 (black-box, Table 3). Recall is 87% on ChatGPT at 1% FPR. Glimpse (11, Table 1) reaches AUROC 0.94–0.98 on GPT-4, Claude-3 Sonnet/Opus and Gemini-1.5 using the same statistic. DNA-DetectLLM (13, §1, §3.4) frames human text as a "mutated strand" that departs from the greedy argmax sequence. AUROC is about 98% on GPT-4 Turbo, Gemini-2.0 Flash and Claude-3.7 Sonnet (Table 1).
- **Scope:** 2023–2025 frontier chat models, plus news, stories, PubMed, arXiv abstracts and multilingual sets (M4).
- **Actionable rule:** Let the specific claim choose the word. Write "the bridge was closed for 11 days", not "the bridge faced significant disruption." An individual writer's habits (preferred terms, idioms, the shape of their argument) count as human signal. Keep them when revising instead of normalizing toward the "collective" phrasing.
- **Caveats:** The z-score idea has a limit. An unusual word is human signal only if it is plausible. Text built from implausible words reads as noise.
- **Strength:** Strong (three independent groups, peer-reviewed, frontier models).

### 4. Human writers use unexpected words even where the context strongly predicts the next word.
- **What the paper found:** GLTR (01, §4, Fig. 5) plots context entropy against rank: "human authors use low-rank words, even when the entropy is low, a property that sampling methods for generated text avoid… human text uses high-rank words more frequently, regardless of the estimated entropy."
- **Scope:** NYT vs. GPT-2 (temperature 0.7).
- **Actionable rule:** Stock collocations are where defaults pile up ("plays a crucial role", "a wide range of", "in today's fast-paced world"). These are the places to substitute the concrete claim or simply cut.
- **Caveats:** One figure from a KDE plot. Moderate support, but consistent with Patterns 1–3.
- **Strength:** Moderate.

### 5. Machine text keeps the reader in predictable contexts. Human text keeps opening contexts where many continuations are possible.
- **What the paper found:** The "Entropy" baseline (high average predictive entropy taken as a machine signal) is consistently *inverted* on modern chat output. On ChatGPT, entropy AUROC is 0.33 on XSum, 0.19 on WritingPrompts and 0.28 on PubMed (06 Table 3). GPT-4 is 0.38. Glimpse with GPT-3.5 scoring gives 0.05 on ChatGPT WritingPrompts (11 Table 1). An AUROC far below 0.5 means human passages have *higher* average next-token uncertainty than ChatGPT passages. DetectLLM notes the entropy assumption "doesn't stand for high temperature" (04 §5.3). GLTR (01 §3) reports GPT-2 samples show "a high fraction of low-entropy predictions". Human samples have fewer "low-entropy contexts."
- **Scope:** ChatGPT and GPT-4 (2023), open models 1.5–20B. Story writing shows it most strongly.
- **Actionable rule:** Machine prose stays on rails: each sentence sets up the obvious next one (setup, elaboration, restatement, summary). Human prose brings in new information, turns, specifics or asides that a reader could not have predicted. So cut the sentences that only restate or set up the obvious, and make each sentence add something the previous one did not entail.
- **Caveats:** This is an inference from detector statistics. The papers do not describe it in stylistic terms. Direction depends on the model: for some open models and domains the entropy AUROC sits near 0.5–0.6 (03 Table 1). Paper 13 reports entropy AUROC of 0.75–0.91 on 2025 frontier-model stories (Table 1) without stating its sign convention, so it can't be compared directly. Treat this pattern as model- and decoding-specific.
- **Strength:** Moderate (strong numbers for ChatGPT, mixed elsewhere).

### 6. Truncated sampling never reaches the tail, while real documents always include some tail words.
- **What the paper found:** Grover (02, §6): "The probability of observing a human-written article where all tokens are drawn from the top-p% of the distribution is p^n… goes to zero as n increases. However, for Nucleus Sampled text… all tokens come from the top-p." Lower p, k or temperature makes detection easier (03 Table 3; 04 Table 4; 06 Table 9). With T=0.6, Fast-DetectGPT reaches 0.9996 AUROC. GLTR's GPT-2 sample contains no purple (rank >1000) tokens (01 §3).
- **Scope:** Grover-Mega 1.5B news, 2019, and later open models.
- **Actionable rule:** A long passage in which every word is the expected one is itself a signature. Over a full document some genuinely unexpected but correct word choices are normal and necessary: proper nouns, numbers, domain terms, the author's idiom. Do not sand them down in revision.
- **Caveats:** This describes decoding, not writing. It is listed only because it explains why the "polish everything to the smoothest word" style of revision pushes text toward the machine end.
- **Strength:** Strong (mathematical plus empirical).

### 7. Machines repeat an entity's name instead of using pronouns or varied references (GPT-2 era).
- **What the paper found:** GLTR (01 §5, qualitative findings from a 35-student study): "While humans would vary expressions in real texts, models rarely generate synonyms or referring expressions for entities, which does not follow the theory of centering… the model keeps generating the name Pérez and never refers to him as he."
- **Scope:** GPT-2 1.5B, 2019. Anecdotal (one example).
- **Actionable rule:** Use natural reference chains: name, then pronoun, then a short descriptor, as a careful writer would. Do not tip into forced "elegant variation" either.
- **Caveats:** Dated, and possibly reversed in modern chat models (other batches may report synonym cycling). Treat as weak.
- **Strength:** Weak.

### 8. Templated systems produce high parallelism in sentence structure.
- **What the paper found:** GLTR (01 §5): "samples from Heliograf exhibit high parallelism in sentence structure." Humans in the study trusted Heliograf text *more* than GPT-2 text (68.6% vs 51.4% judged real, p<0.01).
- **Scope:** Washington Post Heliograf (rule-based sports and election reports), 2019.
- **Actionable rule:** Vary sentence frames across consecutive sentences. Avoid stacks of "X did A. Y did B. Z did C." built on one template, unless the parallelism is a deliberate device.
- **Caveats:** This finding is about a template engine, not an LLM. Readers found the parallel prose *more* credible, so parallelism is not penalized by human readers.
- **Strength:** Weak (qualitative).

### 9. Generic content and stock phrasing in modern LLM output (qualitative examples)
- **What the paper found:** The detector papers print raw model outputs as examples. They are useful as illustrations, not as frequency data:
  - GPT-4, capybara prompt (09 Table 1): "astounded the scientific community with his groundbreaking research", "unparalleled ability to interpret cosmic data", "uncovered new insights into the mysteries of black holes", "it seemed as if the stars themselves whispered their secrets directly to him", "became a beacon of inspiration to aspiring scientists but also proved that intellect and innovation can be found in the most unexpected of creatures."
  - LLaMA-2-13B-chat, default style (09 Table 2): "A well-trained dog is not only a delight to be around, but it also provides a sense of pride and accomplishment… Whether you're doing it for fun, agility competitions, or simply to keep your furry companion physically engaged, teaching your dog how to jump can be a bonding and rewarding experience."
  - GPT-4 (13 Table 3): "This paper delves into the field of pure exploration and regret minimization… an important area in machine learning". The story continuation reads "their eyes widened at the sight of the vibrantly colored parrots squawking from the treetops".
  - DetectGPT (03 §5.1 fn. 4): machine creative writing "tends to be noticeably generic, and therefore relatively easy to detect." Stories (WritingPrompts) are the easiest domain for every detector in 03, 04 and 06.
- **Scope:** GPT-4 (2023–24), LLaMA-2-13B-chat.
- **Actionable rule:** Cut the following: "not only X but also Y" constructions; "Whether you're A, B, or simply C" openers; abstract inflation ("groundbreaking", "unparalleled", "beacon of inspiration", "new insights into the mysteries of"); "delves into"; closing moral summaries ("proved that… can be found in the most unexpected of…"); stock sensory clichés ("eyes widened"). Replace each with a specific detail or delete it.
- **Caveats:** These are illustrative excerpts and the papers do not count them. Other batches should supply frequency evidence.
- **Strength:** Weak as statistics. They are consistent illustrations of Patterns 1–3.

### 10. Topic novelty is not human signal. Detection depends on word choice relative to the context ("the capybara problem").
- **What the paper found:** Binoculars (09 §3.2–3.3): an odd prompt ("a capybara that is an astrophysicist") makes the output high-perplexity (Falcon log-PPL 2.20, "well above the mean for both human and machine data"). Raw perplexity then calls it human, and so do DetectGPT and GPTZero (49.7%). Binoculars normalizes by what an LLM would itself predict in that same context (cross-perplexity) and flags the text confidently (0.73 against a 0.901 threshold). "We expect the next-token choices of humans to be even higher perplexity than those of a machine." Perplexity alone is a poor detector at low FPR (09 Table 4, e.g. LLaMA X-PPL TPR 0.00 on News).
- **Scope:** Falcon-7B/-Instruct observer pair. ChatGPT, GPT-3/4 (Open-Orca), LLaMA-2, Falcon outputs. News, creative writing, student essays, M4.
- **Actionable rule:** An unusual subject, a quirky premise or exotic vocabulary in the *topic* does not make prose read as human. What matters is whether, *given* the subject, each sentence says what any fluent writer would say about it. Write the non-obvious sentence about the topic, not the obvious sentence about an unusual topic.
- **Caveats:** None significant. This is the central design insight of a well-validated paper.
- **Strength:** Strong.

---

## B. Domains where humans look machine-like (false-positive zones)

| Domain / text type | Evidence | Implication for the skill |
|---|---|---|
| **Memorized and famous texts** | Binoculars (09 §5.3, Table 5): US Constitution scores 0.76, "I have a dream" 0.81 and a Cosmos snippet 0.85, all classed machine (threshold 0.901). Lesser-known texts pass: an unreleased Dylan song scores 1.01, while "Blowin' in the Wind" has log-PPL 1.11 vs 3.30 for the unreleased song (A.4). "Memorized text is both text written by human writers, and text that is likely to be generated by an LLM." | Stock quotations, famous lines and much-repeated boilerplate are maximally predictable. Prose that leans on well-worn phrases ("ask not what…", textbook definitions) inherits that predictability. Paraphrase clichés or replace them. Quote only when quoting is the point. |
| **Templated or formulaic news** | Grover (02 §7): "Domains with templated news articles exist in our dataset… and are easy for Grover to spoof convincingly" (e.g. americanbankingnews.com). GLTR: humans rated Heliograf template output real 68.6% of the time (01 §5). | Formulaic genres (earnings blurbs, sports recaps, press releases) are inherently low-surprise whoever writes them. Expect less room to differ and focus on specifics (numbers, names, quotes). |
| **Academic and technical writing** | DNA-DetectLLM (13 Table 1): Likelihood AUROC for GPT-4 Turbo on arXiv abstracts is only 57.9, and Entropy 45.6 (near chance), i.e. human abstracts are about as predictable as GPT-4's. PubMedQA is the hardest domain in 03 (DetectGPT 0.84 vs 0.99 on XSum with GPT-2; Fig. 4) and 06 (ChatGPT PubMed 0.90 vs 0.99 for news/stories). GPTZero is weakest on technical writing (06 §3.3). | Conventional academic register is close to the model's default. In technical text the human signal comes from exact terms, specific results and the author's own framing, not from vocabulary flourishes. Don't "humanize" technical prose with casual diction. |
| **News (vs. stories)** | News (XSum) is consistently harder to separate than stories with likelihood-type statistics (03 Table 1; 12 Table 1: Likelihood 0.62 on XSum vs 0.70 on Writing). On GPT-4o, black-box Likelihood on XSum is 0.52, chance level (12 Table 2). | Journalistic convention compresses human variation. |
| **Short passages** | All detectors lose power on short inputs (06 Fig. 4; 09 Fig. 2; 13 Fig. 5). | Short texts give less statistical evidence either way. Individual phrase choices weigh more. |
| **Non-native / ESL writing** | Liang et al. (cited in 09 §2): commercial detectors flagged 48–76% of TOEFL essays as AI. Binoculars itself scored original and grammar-corrected ESL essays identically, 99.67% classed human (09 §5.2, Fig. 7). | Grammar correction alone did not make ESL writing machine-like under a perplexity-ratio detector. The well-known ESL bias is a property of particular (trained/commercial) detectors. |

---

## C. Things that do NOT work or backfire

1. **"Write in the voice of X" or "don't sound robotic" prompts barely change the statistical signature.** Binoculars (09 §5.4, Fig. 8, Table 6) tried system prompts for Carl Sagan, "Non-Robotic" ("doesn't sound pretentious or overly formal. Don't use robotic-sounding words like 'logical' and 'execute.' Write in the casual style of a normal person.") and Pirate. The largest effect was a 1% rise in false-negative rate. The "non-robotic" output simply moved to a different stock register: "Hey there, fellow dog lovers! Are you looking for a fun and challenging way… Look no further than an adjustable jump! Not only is it a great way to… but it's also a great way to bond with your pup." **Lesson:** a register instruction swaps one set of defaults for another (casual clichés replace formal ones). The rule has to work at the level of each choice ("say the specific thing"), not of tone.
2. **Thesaurus-style lexical diversification hurts readability.** Glimpse (11 App. E.2): DIPPER at high lexical diversity "replaces common words with rare expressions, thus reducing the readability of the content… increased diversity also lowers the readability due to excessive use of unusual words and sequences." It did lower some detectors (Fast-Detect GPT-3.5 TPR 0.7% on XSum). **Lesson:** rare-for-rare's-sake substitution is the wrong reading of Pattern 1. Human low-rank words are correct and meaningful.
3. **Sentence-level paraphrasing breaks coherence, and modern detectors survive it anyway.** Fast-DetectGPT (06 App. F.2): T5 paraphrasing "a noticeable reduction in cross-sentential coherence". A "decoherence attack" (swapping two adjacent words in sentences over 20 words) caused a similar detection drop, so the drop came from damaged text. DNA-DetectLLM / Binoculars / Fast-DetectGPT keep about 93–98% AUROC under DIPPER paraphrase of GPT-4 Turbo, Gemini-2.0 and Claude-3.7 output (13 Tables 6–8). DetectGPT holds 0.8+ AUROC with about 24% of the text replaced (03 Fig. 5). **Lesson:** paraphrasing an LLM draft does not remove its signature. Rewriting has to change *what* is said (specifics, structure, claims), not only the surface.
4. **Random noise, typos and token edits are worthless and get detected.** Random token sequences score strongly "human" (Binoculars mean 1.35 vs a human mean of about 1.0, 09 A.7), which shows the detector rewards unpredictability with no regard for quality. 1% random insert/delete/substitute edits cut naive likelihood detectors to chance, but modern ones still score 86–98% (13 Tables 6–8). This matches the brief's ban on fake typos. Noise lowers quality and does not reliably change the outcome.
5. **Lower-temperature, "safer" generation makes text more machine-like.** 04 §5.3 and 06 Table 9 show AUROC rising as p, k or T fall (Fast-DetectGPT 0.9996 at T=0.6). Revision toward the most conventional phrasing pushes text the same way.
6. **Polish is not a reliable cue to human readers.** Grover (02 §4, Fig. 4): when Grover rewrote propaganda, readers rated it *more* trustworthy (2.42 vs 2.19 out of 3, p=0.01). Without tools, people spot GPT-2 text at only 54% (01 §5). Fluency persuades readers. It does not make text sound human, which is a separate goal.

---

## D. Human-text features reported (what human writing does that LLM writing lacks)

- More words outside the model's top 100 (2.41× under GPT-2), and more "red and purple" words, in NYT and scientific abstracts (01).
- Unexpected words even where the context is low-entropy (01 Fig. 5).
- Phrasing that is *not* a local maximum: alternative wordings are as likely as the original or more (03, 04).
- Word choice driven by "underlying meanings, intentions, and contexts rather than data statistics", reflecting *individual* rather than collective writing behavior (06 §1, §2.3).
- Movement into higher-uncertainty contexts: next-token entropy is higher on average than ChatGPT output (06 Table 3; 11 Table 1).
- Varied referring expressions (pronouns, descriptors) for recurring entities (01 §5, GPT-2 era).
- Over any long document, at least some tokens fall outside the top-p nucleus (02 §6).

---

## E. Per-paper: what translates to writing behaviour

- **01 GLTR:** The most directly useful paper in the batch. Rank statistics, the low-entropy/high-rank plot, and qualitative notes on missing referring expressions and template parallelism. Patterns 1, 4, 7, 8.
- **02 Grover:** Little stylistic content. Useful points: the truncation tail argument (Pattern 6), templated news being easy to spoof (§B), and machine rewrites raising perceived trustworthiness (§C6). Appendix examples are long article samples with no analysis.
- **03 DetectGPT:** The local-maximum / "implicit watermark" interpretation (Pattern 2), stories being the easiest domain ("noticeably generic"), PubMed the hardest, and robustness to partial revision (§C3).
- **04 DetectLLM:** Confirms that log-rank beats log-probability and that machine text is more sensitive to small rewrites. Temperature results (§C5). Nothing beyond that translates to writing.
- **06 Fast-DetectGPT:** The cleanest statement of the "machine picks the top token given context; humans pick by intent" hypothesis (Pattern 3). Entropy inversion on ChatGPT/GPT-4 (Pattern 5). The paraphrase/decoherence analysis (§C3).
- **09 Binoculars:** The capybara problem (Pattern 10), memorized-text false positives (§B), the failure of style-shifting prompts and the "non-robotic" example (§C1), the ESL result (§B), and random tokens (§C4). Also: GPT-4 (March 2024) had a 58% false-negative rate vs 3% for Gemini-1.0-Pro (A.10, Table 8). The newest models were already harder to catch.
- **11 Glimpse:** Shows the same statistic works with GPT-3.5/4 as scorer on Claude-3, GPT-4 and Gemini-1.5 output (AUROC 0.92–0.98), so the top-token preference persists in 2024 frontier models. DIPPER rare-word readability finding (§C2). Otherwise methodological.
- **12 AdaDetectGPT:** Mostly theory (a learned witness function over token log-probs, MCLT-based FNR control). One relevant fact: on GPT-4o output, raw Likelihood is near chance on XSum (0.52), yet curvature-style statistics reach about 0.90 (Table 2). Modern output is not uniformly "low perplexity". The signal is the choice *relative to the alternatives available* at each position. Nothing else translates.
- **13 DNA-DetectLLM:** Frames human text as departures from the greedy sequence. Repairing low-probability tokens shifts the score most (§3.6), so a relatively small number of genuinely unexpected human choices carry much of the signal. Includes arXiv false-positive data (§B), attack robustness on Claude-3.7 / GPT-4 Turbo / Gemini-2.0 (§C3–4), and GPT-4 sample outputs (Pattern 9).

---

## 5-line summary
1. Every detector here relies on one robust, replicated finding: LLMs pick the most probable word for the context, and humans regularly pick lower-ranked but correct words (2.41× more words outside the top 100, GLTR). This holds through GPT-4, Claude-3/3.7 and Gemini (AUROC 0.92–0.98).
2. LLM phrasing sits at a local probability peak, so any rewording lowers its probability. Human phrasing does not, and human text keeps moving into less predictable contexts (entropy-detector AUROC as low as 0.05 on ChatGPT stories). The editorial rule: let the meaning, a specific fact or the author's habit choose each word, and make each sentence add something the last did not entail.
3. Topic novelty does not count as human signal (Binoculars "capybara problem"). Famous or memorized texts (US Constitution, "I have a dream"), templated news, and academic/PubMed prose make human writing look machine-like, so clichés and boilerplate carry machine-like predictability whoever writes them.
4. What fails: tone or persona prompts ("non-robotic", pirate, Carl Sagan) changed detection by ≤1% and just swapped in casual clichés. Thesaurus-style rare-word swaps hurt readability. Paraphrasing leaves the signature (modern detectors keep 93–98% AUROC). Random edits and typos add noise and do not change the outcome.
5. Usable qualitative tells from printed outputs: "not only X but also Y", "Whether you're A, B or simply C", "delves into", "groundbreaking / unparalleled / beacon of inspiration", closing moral summaries, stock clichés ("eyes widened"). GPT-2-era studies also note names repeated instead of pronouns and template-like sentence parallelism, which are weak and dated.
