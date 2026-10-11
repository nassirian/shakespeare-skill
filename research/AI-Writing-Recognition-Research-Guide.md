# What makes AI-generated writing recognizable?

> This guide was written with AI assistance (ChatGPT) in September 2026 as background for the Shakespeare skill. Page references point to the PDFs in `manifest.json`. Check figures against the papers before citing them.

A synthesis of the 31 papers listed in this folder's README. Links to local PDFs work only after you run `download_papers.py` and move the files into this folder. Prepared September 20, 2026.

## What the research supports

AI-generated writing can leave detectable patterns in its word choices, probability distributions, response to rewriting, and sometimes deliberately embedded watermarks. Human readers also notice recurring rhetorical habits and weaknesses in article construction. **None of the ordinary stylistic clues establishes authorship by itself.**

Here, “AI” means the language models and generation settings studied in these papers. The observations do not apply uniformly to every model, language, genre, prompt, or edited document. A tendency measured across a collection is not a rule for an individual sentence.

**Review scope:** I examined all 31 downloaded papers, focusing on the methods, empirical findings, limitations, and relevant appendices that answer this question. This is a section-focused research synthesis, not a reproduction of the experiments or a line-by-line audit of every mathematical proof. Paper numbers match the downloaded filenames. Page references below use PDF page positions. Examples explicitly marked “illustrative” were written for this guide, not taken from experiments.

## 1. What human readers notice

The most direct evidence comes from the expert-reader study [P28](#p28). Its participants described these clues while judging articles. These are **reported cues used by readers**, not separately validated diagnostic tests. The study included incorrect judgments as well as correct ones. MAGE [P18](#p18) provides an important counterweight: several stylistic differences become less distinctive when the dataset includes more domains and generators.

| # | Tendency observed in studied AI outputs | What a reader notices | Evidence and limits |
|---|---|---|---|
| H1 | Reuses a familiar vocabulary | Clusters of stock adjectives, verbs, and transitions recur across unrelated subjects. | P28 §§2–3 and Tables 11–12. Individual words also produced false positives. |
| H2 | Recycles rhetorical patterns | Repeated contrast formulas, parallel clauses, or lists of three make the prose feel templated. | P28 Table 3. These are also ordinary human rhetorical devices. |
| H3 | Uses a narrow range of sentence shapes | Similar rhythms and clause structures persist across paragraphs. | P28 Tables 3 and 17. Genre and editorial style can explain this. |
| H4 | Wraps up too neatly | Conclusions restate the article and add an uplifting general lesson. | P28 §§2–3 and Table 11. This is common in human school essays too. |
| H5 | Falls back on generic openings | A stock scene-setting introduction substitutes for a distinctive angle. | P28 Table 11. Context matters more than the opening phrase. |
| H6 | Overexplains without adding much | More sentences repeat the message instead of supplying evidence or useful detail. | P28 clarity category; P07 discusses related qualitative findings. |
| H7 | Produces interchangeable voices | Different quoted people sound like the narrator and express suspiciously convenient points. | P28 quotes category. Quote verification is separate from judging style. |
| H8 | Repeats presentation templates | Uniform headings or bold-label-and-explanation bullets appear regardless of the material. | P28 formatting category. House styles and templates produce the same appearance. |
| H9 | Applies an oddly consistent emotional tone | Serious or mundane material receives similar optimistic, inspirational treatment. | P28 tone category. Neutrality or positivity alone is not diagnostic. |
| H10 | Uses strained synonyms or imagery | Grammatically fluent wording carries an unnatural meaning or forced metaphor. | P28 vocabulary and originality categories. Humans also write awkwardly. |
| H11 | Offers safe, unsurprising treatment | The text lacks the distinctive detail, humor, or unexpected observation readers expect. | P28 originality category. This is subjective and task-dependent. |
| H12 | Reuses stereotyped names or naming conventions | Names or honorifics recur conspicuously across generated articles. | P28 §§2.5 and 3. A dataset-level observation, not a test based on someone's name. |
| H13 | Maintains unusually uniform polish | Consistent grammar and formality can contribute to an overall impression. | P28; P22 documents the danger of judging authorship through linguistic style. Edited human prose can be flawless. |

These are overlapping clues. Counting five correlated stylistic habits does not create five independent pieces of evidence.

### An illustrative example

> In an ever-changing world, community gardens play a crucial role in bringing people together. They are not merely places to grow food; they are spaces for connection, resilience, and transformation. Ultimately, they remind us of the power of collective action.

This invented example combines a generic opening, familiar abstract vocabulary, a contrast formula, a three-item list, and a moralizing conclusion. It supplies no location, event, observation, or source to make the claim concrete. It illustrates what can create an AI-like impression; **the wording cannot tell us who wrote it**.

For comparison, an equally invented passage could say:

> The garden's water bill doubled in July. At Tuesday's meeting, residents voted to leave two beds empty rather than raise the membership fee.

The second passage is specific and consequential. An AI can write it too. Specificity improves the writing; it does not authenticate the writer.

### How capable are human readers?

P28 studied 300 English nonfiction articles and five experienced LLM users whose majority vote missed one article. This does not mean any reader is 99.7% accurate: inexperienced readers performed poorly, individual experts differed markedly, and the study had a narrow language/genre scope. One expert detected none of the humanized AI articles in one experiment. The study's clue frequencies measure how often annotators mentioned a category, not that category's predictive accuracy. See P28 §§2–3 and Limitations.

Earlier work reached different results under different conditions. GLTR improved human detection with probability visualizations [P01](#p01); the Grover study found generated propaganda persuasive to its readers [P02](#p02). There is no single context-free “human detection accuracy.”

## 2. What automated systems measure

Many systems do not look for a suspicious word or sentence. They examine a numerical pattern across tokens—pieces of words or words—as evaluated by a language model. Other systems learn classification features from examples. A trained classifier is not necessarily able to explain its decision in human terms.

| # | Detectable behavior or signal | How the system recognizes it | Papers | Main qualification |
|---|---|---|---|---|
| M1 | Preference for model-predictable wording | Computes token likelihood, rank, or passage perplexity: how surprising the words are to a particular model. | P01, P04, P06 | Predictability is model-relative. Formulaic human text can also be predictable. |
| M2 | Word choices differ from the model's expected alternatives | Compares observed token scores with a conditional sampling baseline and normalizes the difference. | P06 | Fast-DetectGPT measures more than raw perplexity; scoring-model and domain choices matter. |
| M3 | Small changes lower the model's score disproportionately | Generates nearby versions of the passage and measures the likelihood difference. | P03 | DetectGPT depends on scoring access and meaningful perturbations. |
| M4 | Token ranks respond differently to perturbations | Uses a likelihood-to-log-rank ratio or normalized changes in rank after rewriting small parts. | P04 | DetectLLM's two variants have different costs and access assumptions. |
| M5 | Two models exhibit a characteristic prediction relationship | Normalizes observed log-perplexity with cross-model predictive cross-entropy. | P09 | Binoculars controls for some topic effects; it does not identify a unique originating model. |
| M6 | A model regenerates a similar continuation | Removes the ending, generates alternative endings, and measures phrase overlap or probability differences. | P08 | Similarity depends on task, model, and regeneration settings; it is not an exact provenance record. |
| M7 | Rewriting leaves comparatively little changed | Measures edit distance and consistency after asking an LLM to rewrite the input. | P10 | Raidar uses rewriting behavior; simply asking a chatbot who wrote the text is a different task. |
| M8 | Text lies closer to a model-preferred token sequence | Measures a cumulative score while replacing tokens with model-preferred alternatives. | P13 | “Repair” means movement toward the model's preference, not correction of factual or grammatical mistakes. |
| M9 | A combination of probability features separates examples | Learns a classifier from features produced by multiple models, or learns an adaptive scoring function. | P07, P12 | Ghostbuster and AdaDetectGPT still depend on training/calibration choices. |
| M10 | Learned features persist across some paraphrases | Trains a classifier against a paraphraser so it encounters harder generated examples. | P05 | RADAR improves robustness in its experiments; it does not guarantee resistance to all rewrites. |
| M11 | Word-sequence and linguistic distributions differ | Examines repeated phrases, n-grams, entity patterns, or other corpus-level features. | P18, P31 | Some features are dataset shortcuts that weaken across domains and models. |
| M12 | An intentionally embedded statistical signature is present | Tests whether token choices follow a watermark rule, or align with a keyed random sequence. | P14–P16 | Requires a compatible watermarking scheme. Absence of a mark is not evidence of human authorship. |
| M13 | Text matches a recorded model output | Searches a database of actual generated responses for exact or approximate matches. | P25 | Requires access to the relevant output archive and suitable match thresholds. An ordinary web match is not enough. |

**Glimpse [P11](#p11) is an access technique:** it estimates missing parts of probability distributions from limited API observations so existing statistical methods can operate. It is not an additional visible writing habit. The paper also notes that it cannot use every proprietary model.

### Why some of these signals exist

An autoregressive language model assigns probabilities to possible next tokens. Generation settings select from that distribution. Those choices can leave a statistical pattern even when the passage sounds natural. Restricting sampling can remove unlikely words, while unrestricted generation can introduce other distributional artifacts. GLTR and Grover study this relationship [P01–P02]. It is inaccurate to say that an LLM always chooses the single most likely word.

The later methods measure more specific relationships: sensitivity to changes (DetectGPT), conditional token preferences (Fast-DetectGPT), agreement between models (Binoculars), or reproducibility of continuation (DNA-GPT). These are related but not interchangeable tests. A high vocabulary variety does not automatically eliminate them, and a human-sounding tone does not determine their output.

### Why watermarks are different

A watermark is an intentionally inserted signal, not an accidental consequence of sounding “robotic.” The Maryland method biases generation toward token sets chosen by a reproducible rule [P14]. Stanford's method ties sampling to a watermark key while preserving the marginal output distribution under its assumptions [P15]. Detection therefore does not require an obvious visual marker.

Watermark robustness depends on the scheme, amount of text, and transformations. P16 finds surviving signals after substantial rewriting when enough text remains; P23 and P25 demonstrate significant degradation under their attack conditions. These results should not be flattened into “watermarks are unremovable” or “watermarks never work.” A detection p-value is not the probability that a person used AI, and provenance claims still depend on the scheme's security assumptions.

## 3. Common claims that these papers do not justify

| Claim | What the evidence permits us to say |
|---|---|
| “It uses an em dash, so it is AI.” | No universal punctuation rule is established. The human-reader study even includes cues about avoided dashes in its tested outputs. Model and style conventions change. P28. |
| “This word proves ChatGPT wrote it.” | Vocabulary is contextual evidence at most. Experts also falsely flagged human passages containing familiar model-associated words. P28. |
| “Perfect grammar, formality, or neutral tone means AI.” | These occur in edited, academic, and professional human writing. Stylistic shortcuts can fail or introduce bias. P18, P22, P28. |
| “Low perplexity proves AI.” | It is a relative model score, with overlap between human and generated text. Normalized and multi-feature methods exist precisely because simple thresholds are inadequate. P07, P09, P22. |
| “High burstiness proves human.” | Sentence variation or variable token surprise is not a universal provenance signal. The term is also used inconsistently. These papers do not establish a transferable cutoff. P18, P20, P29, P31. |
| “A 90% AI score means 90% of the words were generated.” | A classifier confidence, a document probability, and a fraction of flagged text are different quantities. Interpret the tool's stated metric; do not substitute one for another. P27, P29, P31. |
| “The model can recognize its own writing if we ask it.” | Prompted judgment is not a record of authorship. In P28, prompting models with the experts' guide did not match the experts and struggled with humanized articles. |
| “A made-up fact proves machine authorship.” | It establishes a factual problem, not its cause. Human falsehood and AI generation are different classifications. P01 explicitly separates generation detection from misinformation detection. |
| “A benchmark score applies to every new model.” | Unseen generators, domains, languages, and sampling settings can change performance sharply. P17–P21, P27. |
| “Detection is either always possible or always impossible.” | Feasibility depends on distributional separation, access, sample size, and task assumptions. P23 and P24 study different sides of that question. |

## 4. What makes recognition less reliable?

1. **Short passages:** fewer opportunities to observe a stable pattern. The effect depends on the method; it is not a universal minimum-word rule. P03, P07, P19.
2. **A different genre:** a news detector may mistake normal scientific style for a machine signature. P18–P21.
3. **A different language:** English performance does not establish performance in another language. P17 and P19.
4. **An unfamiliar generator or generation setting:** sampling and repetition penalties change detectable distributions. P20, P27.
5. **Human and AI contributions mixed together:** a binary label cannot fully describe translation, polishing, inserted paragraphs, or extensive revision. P21, P27, P29, P31.
6. **Non-native or constrained writing:** simple word choices can look statistically predictable. The Stanford bias study documents this risk for the tools it tested, not for every future detector. P22.
7. **Paraphrasing and editing:** these can weaken some signals while leaving others. Outcomes vary by method and transformation. P05, P16, P23, P25–P29.
8. **Unrepresentative evaluation:** high average accuracy can hide poor detection when the false-positive rate is kept low. P20, P27.

The 2026 evaluation [P29](#p29) also shows why an old failure should not be treated as a permanent result: three tools recorded no false positives on its 40 human documents. That small test does not prove a zero false-positive rate in general. Its larger application to 1,163 theses lacked known authorship, so the proportion flagged was not a confirmed rate of AI use.

## 5. A defensible way to use the list

This is a practical synthesis of the papers, not a validated new detector.

- **Describe the observation:** identify an actual repeated construction, unverified quote, or measured statistical signal.
- **Consider the human explanation:** genre conventions, editing, non-native language use, templates, and the assignment itself can produce similar patterns.
- **Separate style from provenance:** a bland or inflated sentence may need editing regardless of who wrote it.
- **Match evaluation to the task:** use results from the relevant language, genre, model family, text length, and level of editing.
- **Treat unknown as a real outcome:** unsupported certainty is not improved by adding more weak style checks.
- **Where authorship matters, seek independent context:** drafts, verifiable sources, or an available generation record can add information that the prose alone lacks. A missing draft is not proof of AI use.

The recurring distinction is between **“this resembles examples of generated text”** and **“we have evidence of how this document was produced.”** Most style checks and statistical classifiers answer the first question. Watermarks and recorded outputs can add evidence toward the second, within their technical assumptions.

## 6. Contribution of each of the 31 papers

The notes below state what each paper contributes to this guide and a boundary on the inference. Original papers are linked locally; source URLs remain available in README.md and manifest.json.

<a id="p01"></a>

**P01. [GLTR: Statistical Detection and Visualization of Generated Text](01_2019_GLTR-Statistical-Detection-and-Visualization-of-Generated-Text.pdf)**

Relevant reading: pp. 2–5, method, case studies, human study. Probability, rank, and entropy visualizations expose sampling artifacts and can assist readers. The approach targets statistical generation patterns, not truthfulness.

<a id="p02"></a>

**P02. [Defending Against Neural Fake News — Grover](02_2019_Defending-Against-Neural-Fake-News-Grover.pdf)**

Relevant reading: §§3.2, 4, 6. Sampling restrictions and exposure bias can leave detectable artifacts. Persuasive machine text need not look obviously defective; results concern the Grover/news setting.

<a id="p03"></a>

**P03. [DetectGPT](03_2023_DetectGPT.pdf)**

Relevant reading: §4 and pp. 7–9. DetectGPT measures how log likelihood changes under meaningful perturbations. Scoring access and the quality of perturbations limit applicability.

<a id="p04"></a>

**P04. [DetectLLM](04_2023_DetectLLM.pdf)**

Relevant reading: §§3, 6 and Limitations. DetectLLM combines token likelihood with rank, or measures rank changes under perturbation. Evidence is largely English-centric and assumes access to suitable model statistics.

<a id="p05"></a>

**P05. [RADAR: Robust AI-Text Detection via Adversarial Learning](05_2023_RADAR-Robust-AI-Text-Detection-via-Adversarial-Learning.pdf)**

Relevant reading: §§3–4 and §6. RADAR learns against a paraphraser. Greater robustness on tested rewrites does not make its decisions infallible, and clean-text performance can trade off against robustness.

<a id="p06"></a>

**P06. [Fast-DetectGPT](06_2024_Fast-DetectGPT.pdf)**

Relevant reading: §2.3, §3 and Limitations. Fast-DetectGPT compares conditional token preferences efficiently. Its signal is not just sentence length or vocabulary sophistication; surrogate-model coverage matters.

<a id="p07"></a>

**P07. [Ghostbuster: Detecting Text Ghostwritten by Large Language Models](07_2024_Ghostbuster-Detecting-Text-Ghostwritten-by-Large-Language-Models.pdf)**

Relevant reading: §4, generalization experiments, §9. Ghostbuster combines features from weaker language models. Short text, unfamiliar styles, non-native writing, and human–AI editing remain important limitations.

<a id="p08"></a>

**P08. [DNA-GPT](08_2024_DNA-GPT.pdf)**

Relevant reading: §3, §4 and revision experiments. DNA-GPT compares regenerated continuations through n-gram overlap or probability divergence. Reproducibility provides a statistical clue, not an actual generation log.

<a id="p09"></a>

**P09. [Spotting LLMs With Binoculars](09_2024_Spotting-LLMs-With-Binoculars.pdf)**

Relevant reading: §3, §5 and pp. 8–9. Binoculars normalizes with a second model to address topic-dependent perplexity. Its original evaluation does not guarantee robustness against motivated evasion.

<a id="p10"></a>

**P10. [Raidar: geneRative AI Detection viA Rewriting](10_2024_Raidar-geneRative-AI-Detection-viA-Rewriting.pdf)**

Relevant reading: §3 and §4. Raidar measures consistency and changes under rewriting. The best prompt varies by data source; behavior depends on rewriting and generating models.

<a id="p11"></a>

**P11. [Glimpse](11_2025_Glimpse.pdf)**

Relevant reading: §2 and discussion/limitations. Glimpse estimates missing probability distributions from partial API outputs. It extends access to existing detector signals rather than revealing a new human-visible tell.

<a id="p12"></a>

**P12. [AdaDetectGPT](12_2025_AdaDetectGPT.pdf)**

Relevant reading: §§2–3 and Appendix G. AdaDetectGPT learns an adaptive statistic. Theoretical guarantees primarily concern the white-box setting; generation-distribution mismatch complicates their use.

<a id="p13"></a>

**P13. [DNA-DetectLLM](13_2025_DNA-DetectLLM.pdf)**

Relevant reading: §§3.2–3.6. DNA-DetectLLM scores movement toward model-preferred tokens. Its repair process is a statistical construction, not a measure of correctness or writing quality.

<a id="p14"></a>

**P14. [A Watermark for Large Language Models](14_2023_A-Watermark-for-Large-Language-Models.pdf)**

Relevant reading: §§1.2–3. Token-set watermarking creates a deliberate signature. Low-entropy continuations leave little freedom to embed a mark without changing quality.

<a id="p15"></a>

**P15. [Robust Distortion-free Watermarks for Language Models](15_2024_Robust-Distortion-free-Watermarks-for-Language-Models.pdf)**

Relevant reading: methodology and detection test. A secret sequence can guide sampling while preserving the marginal distribution under the scheme assumptions. Detection tests key alignment rather than suspicious prose style.

<a id="p16"></a>

**P16. [On the Reliability of Watermarks for Large Language Models](16_2024_On-the-Reliability-of-Watermarks-for-Large-Language-Models.pdf)**

Relevant reading: rewriting, human paraphrasing and copy-paste experiments. Some watermark signal survives changes and mixing when enough tokens remain. Required text length and transformation strength are central to interpreting results.

<a id="p17"></a>

**P17. [MULTITuDE](17_2023_MULTITuDE.pdf)**

Relevant reading: §§4–6. MULTITuDE tests multilingual and cross-generator generalization. Success in one language does not establish success in another.

<a id="p18"></a>

**P18. [MAGE: Machine-generated Text Detection in the Wild](18_2024_MAGE-Machine-generated-Text-Detection-in-the-Wild.pdf)**

Relevant reading: §7 and Limitations. MAGE shows how linguistic differences can shrink across diverse domains and generators. A shortcut in a narrow dataset is not a universal signature.

<a id="p19"></a>

**P19. [M4: Multi-Generator Multi-Domain and Multi-Lingual Black-Box Machine-Generated Text Detection](19_2024_M4-Multi-Generator-Multi-Domain-and-Multi-Lingual-Black-Box-Machine-Generated-Text-Detection.pdf)**

Relevant reading: §§5.4–5.6 and conclusion. M4 tests transfer across languages, domains, generators, and text lengths. Strong matched-condition performance can coexist with poor transfer.

<a id="p20"></a>

**P20. [RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors](20_2024_RAID-A-Shared-Benchmark-for-Robust-Evaluation-of-Machine-Generated-Text-Detectors.pdf)**

Relevant reading: benchmark design, robustness experiments and §7. RAID demonstrates sensitivity to decoding settings, repetition penalties, unseen generators, and attacks. Reported accuracy needs demanding shared evaluation.

<a id="p21"></a>

**P21. [DetectRL](21_2024_DetectRL.pdf)**

Relevant reading: §§2–3 and conclusion. DetectRL tests revisions, noise, mixing, and varied text lengths. Realistic writing conditions change which detectors work well.

<a id="p22"></a>

**P22. [GPT detectors are biased against non-native English writers](22_2023_GPT-detectors-are-biased-against-non-native-English-writers.pdf)**

Relevant reading: results and discussion. The tested detectors frequently flagged human non-native English writing. Predictability and restricted expression can create unfair false positives.

<a id="p23"></a>

**P23. [Can AI-Generated Text be Reliably Detected](23_2023_Can-AI-Generated-Text-be-Reliably-Detected.pdf)**

Relevant reading: theory and recursive-paraphrasing experiments. Closer human and model distributions limit discrimination; recursive paraphrasing stresses several detectors. This is not a claim that all detection always fails.

<a id="p24"></a>

**P24. [On the Possibilities of AI-Generated Text Detection](24_2024_On-the-Possibilities-of-AI-Generated-Text-Detection.pdf)**

Relevant reading: §3, sample complexity and dependence analysis. Distinguishable distributions may be detected with enough observations under stated assumptions. A theoretical multi-sample possibility does not authenticate one short passage.

<a id="p25"></a>

**P25. [Paraphrasing evades detectors of AI-generated text but retrieval is an effective defense](25_2023_Paraphrasing-evades-detectors-of-AI-generated-text-but-retrieval-is-an-effective-defense.pdf)**

Relevant reading: paraphrasing experiments and §5. DIPPER weakens several detectors; retrieval can recover matches to archived model responses. The needed archive is an essential requirement.

<a id="p26"></a>

**P26. [Testing of Detection Tools for AI-Generated Text](26_2023_Testing-of-Detection-Tools-for-AI-Generated-Text.pdf)**

Relevant reading: methods, results and discussion. Commercial and research-tool performance varies across human, generated, translated, and edited text. Scores and evaluation conventions are not interchangeable.

<a id="p27"></a>

**P27. [A Practical Examination of AI-Generated Text Detectors for Large Language Models](27_2024_A-Practical-Examination-of-AI-Generated-Text-Detectors-for-Large-Language-Models.pdf)**

Relevant reading: evaluation methodology, experiments and conclusion. Low-false-positive operating points reveal weaknesses hidden by average metrics. Human-source rewriting and translation complicate binary authorship labels.

<a id="p28"></a>

**P28. [People who frequently use ChatGPT for writing tasks are accurate and robust detectors of AI-generated text](28_2025_People-who-frequently-use-ChatGPT-for-writing-tasks-are-accurate-and-robust-detectors-of-AI-generated-text.pdf)**

Relevant reading: §§2–4, Limitations, Tables 3, 11–12 and 17. Experienced readers use clusters of lexical, structural, and semantic clues. Individual cues were not isolated causal tests; results concern a small expert group and selected English articles.

<a id="p29"></a>

**P29. [Who wrote this Evaluating the reliability of AI detection tools in higher education](29_2026_Who-wrote-this-Evaluating-the-reliability-of-AI-detection-tools-in-higher-education.pdf)**

Relevant reading: methods, discussion and limitations, pp. 8–17. A 160-document evaluation finds different performance across complete, hybrid, and humanized text. The separate 1,163-thesis application has no ground-truth validation.

<a id="p30"></a>

**P30. [Towards Possibilities and Impossibilities of AI-generated Text Detection: A Survey](30_2023_Towards-Possibilities-and-Impossibilities-of-AI-generated-Text-Detection-A-Survey.pdf)**

Relevant reading: detection taxonomy and §6. The survey separates prepared/provenance methods from post-hoc detectors and relates feasibility to practical conditions. It supplies a framework, not an additional independent experiment.

<a id="p31"></a>

**P31. [A Survey on LLM-Generated Text Detection: Necessity Methods and Future Directions](31_2025_A-Survey-on-LLM-Generated-Text-Detection-Necessity-Methods-and-Future-Directions.pdf)**

Relevant reading: §§5–9. The survey connects linguistic statistics, model scores, learned methods, and human-assisted detection. It emphasizes generalization, mixed writing, and evaluation limitations.

## Reading the evidence correctly

This bibliography contains overlapping research lines and two surveys. Thirty-one papers do not constitute 31 independent confirmations of each cue. Several use related models or datasets. Observed effects can conflict because the access assumptions, sampling settings, attacks, language, and amount of text differ.

No detector was run on a user document for this review. No claim here establishes whether a particular piece of writing is AI-generated.
