# How commercial AI-text detectors work (as of 2026-10-12)

Scope: Pangram, GPTZero, Turnitin, Originality.ai, Copyleaks, ZeroGPT, plus independent evaluations. Ends with implications for an honest writing skill (the Shakespeare skill).

**Strength ratings**
- **A**: peer-reviewed independent study, or a primary technical report with a disclosed method and numbers
- **B**: independent but not peer-reviewed (working paper, preprint, or independent data analysis)
- **C**: vendor's own documentation or benchmark (self-reported, often comparing itself against competitors)
- **D**: press coverage, secondary summary, or anecdote

Every number below was read from the cited page during this session, through a fetch tool that summarizes pages. Items marked **[UNVERIFIED]** could not be checked against the primary text.

---

## 1. Headline: what the field looks like in 2026

1. **The leading detectors are now trained neural classifiers, not perplexity heuristics.**
   - Pangram, GPTZero (since about 2023–24), Turnitin and Originality all describe fine-tuned transformer classifiers.
   - "Perplexity/burstiness" survives only as a legacy explanation layer at GPTZero. Turnitin explicitly says it does *not* check burstiness or perplexity.
2. **Training data is built to remove shortcuts.**
   - Pangram's "synthetic mirrors" pair each human document with an AI text on the same topic, length and style. Hard-negative mining then retrains on the model's own false positives.
   - As a result the classifier learns "how was this written," not "what is this about."
   - It also means that topic, genre or vocabulary alone shouldn't be enough to look human or AI.
3. **Humanizers and bypassers are now training data.**
   - Pangram (DAMAGE, Jan 2025; Pangram 4, Jul 2026), GPTZero (2025–26) and Turnitin (Aug 2025) all train on humanizer output.
   - Copyleaks offers an "Extra Sensitive" mode aimed at humanized text.
   - Surface edits that humanizers make no longer fool the top detectors reliably: synonym swaps, removing em dashes and stock phrases, typo injection, homoglyphs.
4. **Mixed authorship is now a first-class output.**
   - Pangram 4 labels each segment Human, AI-Assisted or AI-Generated.
   - GPTZero labels documents Human, AI or Mixed, with sub-labels Pure AI, Polished or Paraphrased.
   - Turnitin and ZeroGPT highlight individual sentences.
   - Light grammar fixes are generally *not* flagged. Generative rewriting is.
5. **Detectors still miss text in two documented ways:**
   - **Style imitation from real author samples.** Misses rose to 10–18% in Epoch's July 2026 test, and to about 24–48% for scientific style.
   - **Base-model or iterative paraphrasing** (HIP, 2026). The authors argue detectors mainly track *instruction-tuning artifacts*, the "chat register."
6. **False positives at the top end are claimed to be very low.**
   - Pangram 4 claims about 0.004% FPR. GPTZero claims 0.08%. Turnitin claims under 1% at the document level for documents with at least 20% AI, and about 4% at the sentence level.
   - Independent tests partly support this: Jabarian & Imas 2025, Epoch 2026 (0/495 FPs for Pangram and GPTZero), and RAID 2024 (default-threshold FPR under 1.7% for closed detectors).
   - Errors concentrate in short texts, poetry, recipes, Wikipedia-like or templated text, and (historically) ZeroGPT and Originality.

---

## 2. Per-vendor findings

### 2.1 Pangram Labs

**Signal.** Pangram uses a trained transformer classifier.
- **v1 (2024):** a "slightly modified transformer-style architecture."
- **Pangram 4 (Jul 2026):** an open-weight sparse mixture-of-experts backbone with LoRA adapters and several heads:
  - 15-class segment head
  - 3-class tokenwise provenance head (human / AI-assisted / AI-generated)
  - binary mixed-authorship head
  - 4-class humanizer head
- The outputs are decoded with a linear-chain CRF over 512-token windows that overlap.
- It does not use hand-built features. The Pangram 4 report calls the model "partly a black box."

**Training data and synthetic mirrors.**
- **v1 data:** about 28M human documents from 2021 or earlier, covering reviews, books, papers, Q&A, Wikipedia, news, creative writing, 165K ESL texts, email and student writing.
- **Mirror prompts:** for each human document, an LLM writes an AI counterpart matched on topic, length and style. Boilerplate such as "Sure, here is…" is filtered out.
- **Hard-negative mining:** each round mines up to 10K false positives per domain, mirrors them, and retrains. Domain-weighted FPR fell from 2.29% to 0.02%.
- **Pangram 4 additions:**
  - an LLM extracts a topic and writes a fresh article on it
  - outputs that copy the original verbatim are discarded
  - AI-assisted text is produced with the EditLens method (AI edits applied to human documents)
  - humanizer data covers typo injection, casing changes, synonym substitution and homoglyphs

**Humanized and paraphrased text.**
- **DAMAGE (arXiv 2501.03437, Jan 2025):**
  - Audited 19 tools: DIPPER, Grammarly, QuillBot, Undetectable AI, StealthGPT, WriteHuman, and others.
  - Tools were grouped into three quality tiers. Humanized text beat the original in a GPT-4o pairwise judge only 26%, 14.7% and 2.7% of the time, by tier.
  - The lowest tier fabricated citations and inserted junk such as "??????".
  - Every humanizer degraded quality.
  - The detector learned humanization as an invariance: humanized *human* text keeps the label "human."
  - **TPR at 5% FPR on humanized academic text:** DAMAGE 98.26%, GPTZero 60.04%, Binoculars 28.23%.
  - An adversarially fine-tuned GPT-4o humanizer, trained against DAMAGE, was still caught 93.2% of the time, and its fluency fell to mid-tier.
- **Pangram 4 report:**
  - Humanized text is flagged AI 97.67% of the time, and AI or Mixed 98.83%.
  - Across 13 anonymized commercial humanizers, AI-or-Mixed recall is 92.78–99.70%.
  - The humanizer head is 96.8% accurate on paired data.

**Mixed text.**
- **EditLens (arXiv 2510.03154):** a regression on the *extent* of AI editing.
  - "Fix any mistakes" edits produce the smallest scores. "Summarize" or "make more detailed" produce the largest.
  - On BEEMO (AI text later edited by humans), scores fell after human editing in 88.9% of documents.
- **Pangram 4 on mixed text:**
  - Document label: Human if at least 90% of characters are human, AI if at least 80% are AI, Mixed otherwise.
  - AI-polish FPR is 0.01%.
  - Recall on heavily AI-edited essays is 55.01%, up from 5.54% in 3.3.2.
  - For interleaved human and AI blocks, tokenwise accuracy is 75% when blocks are one sentence and 98% when they are 20 sentences.

**Minimum length.**
- Inputs must be at least 50 words. Segments are at least about two sentences long.
- On UChicago's under-50-word split, Pangram 4's TPR at 1% FPR is 99.70%.
- **Out of scope:**
  - single-correct-answer replies
  - math and code
  - summaries that add no new words
  - memorized or copied text
  - terse factual bullets
  - templated writing and manuals

**Error rates claimed by Pangram (strength C).**
- **Pangram 4 FPR:** 0.0041% on 1M English FineWeb documents. By domain, the highest are poetry (0.078%), recipes (0.049%) and academic writing (0.019%).
- **Pangram 4 FNR:** 0.34% across 26 generators.
- **Stated limitation:** "People who deliberately write like LLMs, or who have absorbed LLM style" are not accounted for.

**Sources**
| Source | Strength |
|---|---|
| Emi & Spero, *Technical Report on the Pangram AI-Generated Text Classifier*, arXiv:2402.14873v3 (Jul 2024). https://arxiv.org/abs/2402.14873 | **C+** (primary tech report, method disclosed, self-evaluated) |
| Masrour, Emi, Spero, *DAMAGE: Detecting Adversarially Modified AI Generated Text*, arXiv:2501.03437 (Jan 2025); GenAIDetect workshop 2025. https://arxiv.org/html/2501.03437v1 | **C+/B−** (workshop paper, vendor authors) |
| Thai, Emi, Masrour, Iyyer, *EditLens: Quantifying the Extent of AI Editing in Text*, arXiv:2510.03154 (Oct 2025). https://arxiv.org/html/2510.03154v1 | **C+** |
| Glickenhaus et al., *Pangram 4 Technical Report* (Jul 2026). https://pangram-public.s3.us-east-1.amazonaws.com/pdf/pangram_4_technical_report.pdf | **C+** |
| Pangram model card. https://www.pangram.com/it/research/model-card | **C** |
| Pangram "How it works" page. https://www.pangram.com/research/how-it-works | **C** |
| Pangram research index. https://www.pangram.com/research | **C** |

**[UNVERIFIED]** The Pangram 4 report is mirrored on hyper.ai as paper "2607.27183", which looks like an arXiv ID. The arXiv page itself could not be fetched (permission timeout), so the ID is unconfirmed.

### 2.2 GPTZero

**Signal.**
- **2023 (vendor blog):** a seven-part stack:
  - perplexity, using an internal language model
  - burstiness
  - GPTZeroX sentence classifier
  - an education fine-tune for student and ESL writing
  - internet text search
  - "Shield," against homoglyph and spacing attacks
  - an end-to-end deep-learning classifier
- **2026 (arXiv 2602.13042):**
  - A hierarchical multi-task deep classifier.
  - Level 0 is ternary: Human, AI, Mixed. Level 1 splits AI into Pure AI, Polished (human text improved by an LLM) and AI-Paraphrased.
  - It is trained with a document-level loss plus a sentence-level loss.
  - Long texts are split into overlapping windows and aggregated.
  - A conservative remapping shifts low-confidence AI or Mixed predictions toward Human.
  - "Deep Scan" explains a result by occluding one sentence at a time.
  - Perplexity appears in the paper only as a fluency metric for adversarial examples, not as a detection feature (per the alphaXiv summary).

**Humanized and paraphrased text.**
- The training data includes:
  - DIPPER-paraphrased text
  - multi-round translation and rephrasing
  - white-box gradient token-substitution attacks
  - fine-tuning on outputs of commercial "bypasser" services
- **Claimed bypasser recall:** 93.5%. GPTZero's own benchmark (Feb 2026, updated Jul 2026) reports bypasser recall of 91.8% for GPTZero 4.3b, 68.1% for Pangram 3.2 and 57.3% for Originality lite.
- **Independent results tell a different story:**
  - DAMAGE (Pangram-authored): GPTZero caught only 34.5% of humanized text at its default threshold.
  - Jabarian & Imas: GPTZero's FNR after StealthGPT was about 50% or higher.
  - Both of these predate GPTZero's 2025–26 retraining.

**Mixed text and minimum length.**
- Mixed is a document class. Sentences are highlighted individually.
- The benchmark minimum is 250 characters, about 50 words.

**Claimed error rates (self-reported benchmark, 4 domains).**
| Detector | FPR | Recall |
|---|---|---|
| GPTZero | 0.08% | 99.6% |
| Pangram 3.2 | 0.10% | 95.7% |
| Originality | 1.88% | 93.1% |
- **Caveat:** GPTZero maps all of its AI-containing classes to "AI" when scoring itself, but maps competitors' outputs differently.

**Sources**
| Source | Strength |
|---|---|
| Adam et al., *GPTZero: Robust Detection of LLM-Generated Texts*, arXiv:2602.13042 (Feb 2026). Abstract: https://arxiv.org/abs/2602.13042v1. Overview: https://www.alphaxiv.org/abs/2602.13042 | **C+** |
| GPTZero benchmark page. https://gptzero.me/news/gptzero-ai-detection-benchmarking-the-industry-standard-in-accuracy-transparency-and-fairness/ | **C** |
| GPTZero humanizer blog (Jan 2026). https://gptzero.me/news/detecting-ai-humanized-text-how-gptzero-stays-ahead/ | **C** |
| "Inside GPTZero AI Detection" (Jun 2023). https://gptzero.substack.com/p/inside-gptzero-ai-detection | **C** |

**[UNVERIFIED]** The full GPTZero arXiv HTML failed to load. Architecture details come from the alphaXiv overview, not the paper body.

### 2.3 Turnitin AI writing indicator

**Signal.**
- "A modern deep learning approach based on the transformer architecture."
- Sentences are grouped into overlapping segments. Each segment gets a score from 0 to 1, sentences inherit it, and the scores are pooled into a document percentage.
- Turnitin says the model is not rule-based and does not check burstiness or perplexity.
- The guide says a multi-model ensemble was consolidated into a single model in July 2026.

**Humanizers.**
- **Timeline:**
  - AI paraphrasing detection: July 2024
  - "AI bypasser detection": August 2025
  - Turnitin Clarity, a controlled writing environment: May 2025
- **What it says about humanizers:**
  - Turnitin "researched and identified the signals and patterns of leading humanizers and have trained our model to identify them."
  - Humanizers leave a "statistical trace."
  - Results are reported as "AI-generated" or "AI-generated and modified (paraphraser/bypasser)."
  - It does not name the tools it detects.
  - Bypasser detection is **English only**.
- No accuracy or recall numbers for bypasser detection have been published.

**Grammar tools.**
- "Not tuned to target Grammarly-generated spelling, grammar, and punctuation modifications."
- Grammarly's generative features (drafting, paraphrasing, summarizing) "will likely be flagged."

**Mixed text and length.**
- Input must be **at least 300 words of long-form prose** and at most 30,000 words.
- Scores between 1% and 19% are shown only as "*%", with no highlights, to limit false positives.
- **Document-level FPR:** under 1% for documents with more than 20% AI writing. Before each release Turnitin validates on 700K+ papers written before ChatGPT.
- **Sentence-level FPR:** about 4%. 54% of falsely flagged sentences sit right next to genuinely AI-written text, so errors cluster at human/AI transitions.
- **Admitted imprecision:** a document scored at 50% AI "could contain as much as 65%."
- **Languages:** English, Spanish, Japanese, Arabic, Dutch, German, Turkish.

**Independent evaluation.**
- Walters (2023): Turnitin and Copyleaks were among only three of 16 detectors with high accuracy on GPT-3.5, GPT-4 and student essays.
- Weber-Wulff et al. (2023): tested 14 tools including Turnitin, found them "neither accurate nor reliable," biased toward labeling text human, and much worse after obfuscation.
- Perkins et al. (2024): six detectors, *names not confirmed in the summary fetched*. Mean accuracy was 39.5% and fell to 17.4% after adversarial edits (n=805).
- No peer-reviewed independent test of the 2025 bypasser feature was found.

**Sources**
| Source | Strength |
|---|---|
| Turnitin Guides, "Turnitin's AI writing detection capabilities." https://guides.turnitin.com/hc/en-us/articles/28477544839821 | **C** |
| Chechitelli, "Understanding the false positive rate for sentences…" (Jun 2023). https://www.turnitin.co.uk/blog/understanding-the-false-positive-rate-for-sentences-of-our-ai-writing-detection-capability | **C** |
| Plagiarism Today, 27 Aug 2025. https://www.plagiarismtoday.com/2025/08/27/turnitin-launches-anti-ai-humanizer-feature/ | **D** |
| IT Brief, 28 Aug 2025. https://itbrief.co.uk/story/turnitin-updates-tool-to-detect-ai-bypassers-humanised-text | **D** |
| Walters, *Open Information Science* 7(1) (2023). https://doaj.org/article/341948f5dc8b4aaf9d5a34cd2289d8fa | **A−** (126 essays, small) |
| Weber-Wulff et al., *Int. J. Educational Integrity* 19:26 (2023), doi:10.1007/s40979-023-00146-z. https://www.muni.cz/en/research/publications/2355979 | **A** (dated: pre-GPT-4-era tools) |
| Perkins et al., *Int. J. Educ. Tech. Higher Ed.* 21:53 (2024), arXiv:2403.19148. https://arxiv.org/abs/2403.19148v1 | **A−** |

**[UNVERIFIED]**
- Turnitin's ELL "no statistically significant bias" study was seen only as a search-result title: https://www.turnitin.ca/blog/new-research-turnitin-s-ai-detector-shows-no-statistically-significant-bias-against-english-language-learners. It was not read.
- The July 2026 consolidation into a single model is stated only on the guide page.

### 2.4 Originality.ai

**Signal.**
- Originality describes an ELECTRA-style pretrained transformer (generator plus discriminator; it is "based on a modified version of BERT" but "did not use BERT to train") on 160GB of pretraining text.
- The model is then fine-tuned as a binary classifier on millions of human and AI samples, generated with mixed sampling methods.
- Sentences are highlighted individually.
- It claims "acceptable reliability" at 50 tokens or more.
- The current model lineup is "Turbo," "Lite" and the retired "Standard."

**Humanizers.**
- The how-it-works page makes no specific claim about humanizers.

**Independent evaluation.**
- **RAID** (Dugan et al., ACL 2024; 6M+ texts, 11 attacks), accuracy at 5% FPR:
  - Base: 85.0%. Paraphrase attack: 96.7%. Synonym attack: 96.5%.
  - Homoglyph attack: **9.3%** (−75.7 points). Article deletion: 71.4%.
- **RAID per-domain FPR** at a single threshold reached 13% on Wikipedia.
- **Jabarian & Imas (2025):** second tier, less robust to StealthGPT than Pangram.
- **Epoch (Jul 2026):** **19/495 (about 4%) false positives on pre-ChatGPT human text**, against 0 for Pangram and GPTZero. Misses under style imitation were 18%.
- **GPTZero benchmark (competitor-run):** 1.88% FPR overall, 5.30% on academic text, 14.81% multilingual.

**Sources**
| Source | Strength |
|---|---|
| Originality, "How does AI content detection work." https://originality.ai/blog/how-does-ai-content-detection-work | **C** |
| Originality's RAID write-up. https://originality.ai/blog/robust-ai-detection-study-raid | **C** (vendor reading of RAID) |
| Dugan et al., *RAID*, ACL 2024, doi:10.18653/v1/2024.acl-long.674. https://preview.aclanthology.org/setup/2024.acl-long.674 and PDF https://par.nsf.gov/servlets/purl/10563509 | **A** |

### 2.5 Copyleaks

**Signal.**
- The method is essentially undisclosed. Copyleaks names a "V11 model" and gives no architecture.
- "AI Logic" (API `explain`) returns `aiCount` and `humanCount` statistics comparing the text's statistical properties against known AI and human patterns, plus the spans that look AI-like.
- This suggests a phrase- or pattern-frequency explanation layer on top of a classifier. **[Inference, not stated]**
- AI Logic covers 6 languages. Detection covers 30.

**Humanizers.**
- Three sensitivity settings, with self-reported rates:
| Setting | Intended for | FP | FN |
|---|---|---|---|
| Extra Safe | | 0.16% | 0.88% |
| Balanced (default) | | 0.30% | 0.64% |
| Extra Sensitive | "humanizer" or spun text | 0.66% | 0.49% |
- No separate humanizer results are published.

**Self-reported evaluation (Sep 2026).**
- 500K texts: TPR 0.989, TNR 0.999.
- A separate QA team: 0.9970 accuracy on human texts (923 of 326,120 misclassified) and 0.9936 on AI texts.
- Minimum input is 350 characters.

**Independent evaluation.**
- Walters 2023: among the top three of 16 detectors.
- Alshammari & Rao (2025, arXiv 2507.17944, small n=49+49): 98.8% on DeepSeek text, 0 false positives, but 71% after humanized paraphrasing.

**Sources**
| Source | Strength |
|---|---|
| Copyleaks testing methodology (published 2026-09-28). https://copyleaks.com/ai-detector/testing-methodology | **C** |
| AI Logic docs. https://docs.copyleaks.com/concepts/features/ai-logic | **C** |
| Alshammari & Rao. https://arxiv.org/pdf/2507.17944 | **B−** (tiny sample) |
| Walters 2023 (above) | **A−** |

### 2.6 ZeroGPT

**Signal.**
- Marketing only. "DeepAnalyse™ technology," a "multi-stage methodology," trained on internet text, educational datasets and "proprietary synthetic AI datasets."
- Claims "98.4%" accuracy and "<1%" FPR, with no published method or evaluation.
- Highlights sentences and gives a percentage. Maximum input is 15,000 characters.
- No stated minimum length and no claim about humanizers.

**Independent evaluation (the weakest of the six).**
- **RAID (ACL 2024):**
  - ZeroGPT could not reach the 5% FPR target; it is asterisked in the paper.
  - Accuracy ranged from 0.3% to 95.4% depending on generator and sampling.
  - Default-threshold FPR was 0.90–1.71%.
  - Per-domain FPR at one threshold reached **52% on recipes and 48% on Wikipedia**.
- **Temple University CAT addendum (about 2023):** none of the four alternative detectors tested, including ZeroGPT, identified all human or all AI samples correctly. One identified *no* human sample as fully human. *Per-tool attribution was not confirmed.*

**Sources**
| Source | Strength |
|---|---|
| ZeroGPT homepage. https://www.zerogpt.com/ | **D** (marketing) |
| RAID (above) | **A** |
| Temple CAT addendum. https://teaching.temple.edu/sites/teaching/files/images/Addendum%20to%20Evaluating%20the%20Effectiveness%20of%20Turnitin%E2%80%99s%20AI%20Writing%20Indicator%20Model%5B80%5D.pdf | **B−** |

---

## 3. Cross-vendor independent evaluations (2024–2026)

| Study | What it found | Strength |
|---|---|---|
| **Jabarian & Imas, "Artificial Writing and Automated Detection," NBER WP 34223 / BFI WP 2025-116 (Sep 2025).** https://www.nber.org/papers/w34223 and https://bfi.uchicago.edu/insights/artificial-writing-and-automated-detection/ | <ul><li>1,992 human passages across 6 genres (news, blogs, reviews, novels, restaurant reviews, résumés), with AI versions from 4 LLMs.</li><li>Pangram: about 0 FPR and FNR on medium and long text. It was the only detector to meet a 0.5% FPR cap. It held on texts of 50 words or fewer and against StealthGPT.</li><li>GPTZero lost about half its recall after humanization.</li><li>OriginalityAI and GPTZero were second tier.</li><li>The open RoBERTa detector had 30–78% FPR.</li></ul> | **B+** (independent economists; working paper; tested a May 2025 Pangram) |
| **Epoch AI data insight, J. Lee (15 Jul 2026).** https://epoch.ai/data-insights/ai-detectors-false-negatives | <ul><li>495 pre-2022 human passages of about 500 words.</li><li>FPs: Pangram 0, GPTZero 0, Originality 19.</li><li>With a plain prompt (Claude Opus 4.8, GPT-5.5, Gemini 3.1 Pro), misses were 0–1%.</li><li>With 5-shot imitation of a real author's style, misses were Pangram 10%, GPTZero 11%, Originality 18%.</li><li>Scientific style: about 24–29%, peaking at 48% for Pangram on Gemini output.</li><li>If "Mixed" counts as a detection, misses drop to about 6% (Pangram) and 9% (GPTZero).</li></ul> | **B** (independent; small cells of 33) |
| **Russell, Karpinska, Iyyer, ACL 2025 (long), doi:10.18653/v1/2025.acl-long.267.** https://arxiv.org/abs/2501.15654 | <ul><li>Five frequent LLM users, by majority vote, misclassified 1 of 300 articles, including paraphrased and humanized ones.</li><li>This beat most detectors.</li><li>The clues they used: "AI vocabulary," plus formality, originality and clarity.</li></ul> | **A** (Iyyer/Russell later co-author with Pangram; per-detector table not verified) |
| **Dugan et al., RAID, ACL 2024** (see above) | <ul><li>Detectors are "easily fooled" by attacks, by changes in sampling, and by unseen generators.</li><li>A repetition penalty cuts accuracy by up to 32 points.</li><li>Closed detectors are reasonably calibrated at default thresholds, with FPR at or below 1.7%.</li></ul> | **A** |
| **Xu, Zhong, Raghunathan, Fang, Kolter, "Base Models Look Human To AI Detectors" / HIP, arXiv:2605.19516 (2026).** https://arxiv.org/pdf/2605.19516 and coverage at https://aiweekly.co/alerts/gptzero-and-pangram-read-base-model-output-as-human-paper-finds | <ul><li>Output from *base* (non-instruction-tuned) models is judged overwhelmingly human by GPTZero and Pangram.</li><li>A paraphraser built from a base model and applied iteratively evades both detectors.</li><li>The authors conclude detectors track instruction-tuning artifacts.</li></ul> | **B** — **[UNVERIFIED numbers]**: only secondary summaries were read |
| **Al Ali, Helcl, Libovický, "Different Time, Different Language: Revisiting the Bias Against Non-Native Speakers in GPT Detectors," EACL 2026 SRW, arXiv:2602.05769.** https://aclanthology.org/2026.eacl-srw.20 | <ul><li>For Czech, non-native texts do *not* have lower perplexity.</li><li>No systematic bias against non-native writers was found.</li></ul> | **B+** (detectors not named in the summary) |
| **Liang et al., "GPT detectors are biased against non-native English writers," *Patterns* 2023, arXiv:2304.02819** | <ul><li>Older perplexity-era detectors flagged many TOEFL essays.</li><li>Pangram reports 0% FPR on that set, and GPTZero's updated model 7.7%.</li></ul> | **A** (original paper); Pangram/GPTZero numbers **C** |
| **"Eye You," LessWrong, 30 Mar 2026.** https://www.lesswrong.com/posts/hrpQxfYvF6CBGWfJX/pangram-ai-detection-software-can-be-evaded | <ul><li>Against Pangram ≤3.2: swapping em dashes for commas moved the score from 94% to 83% AI, and removing flagged phrases moved it back to 100% AI.</li><li>Iterative "more Plato-like" rewrites by GPT-5.4 reached 100% human.</li><li>Scores were unstable under 250 words.</li></ul> | **D** (anecdote, n of about 3) |

---

## 4. Implications for an honest, human-sounding writing skill

The goal is good prose, not evasion, so detectors are useful here only as evidence about which properties of a text separate LLM output from human writing. Expert humans notice the same properties (Russell et al. 2025).

### 4.1 Properties that plausibly matter (and are legitimate to pursue)

1. **Human-supplied first-hand content.**
   - Mirror training holds topic constant, so a classifier can't be fooled by *what* a text is about. It keys on *how* the text was produced.
   - What actually changes provenance, as both EditLens and Pangram 4 model it, is how much of the final text originated with a human. That covers specific facts, experiences, judgments and phrasing the author supplied.
   - EditLens: human edits to AI text lowered the AI score in 88.9% of documents.
   - Pangram 4 separates "surface-style provenance" from "underlying-idea provenance."
   - **Skill implication:** elicit and preserve the author's own material and words, and keep generated connective tissue to a minimum. This is also simply better writing.
2. **The degree of AI intervention is now measured as a spectrum.**
   - Light grammar fixes are not flagged: Turnitin is "not tuned to" Grammarly-style fixes, and Pangram's AI-polish FPR is 0.01%.
   - Summarizing, expanding or rewriting registers as AI-assisted or AI-generated: EditLens, GPTZero's "Polished" class, Turnitin's generative-feature note.
   - **Skill implication:** a revise-in-place mode (minimal edits that keep the author's sentences) is both more honest and less likely to be labeled AI than regenerating. A skill that rewrites everything *should* be labeled AI-assisted, and the skill should not promise otherwise.
3. **Author edits after generation.**
   - Supported by EditLens (BEEMO) and by Pangram 4's block-size result: one-sentence human blocks interleaved with AI are hard to attribute (75% tokenwise accuracy).
   - **Skill implication:** encourage a real author pass. Don't simulate one.
4. **Length.**
   - Detectors are least reliable on short text both ways. Minimums: Turnitin 300 words, Pangram 50, GPTZero about 50, Copyleaks 350 characters.
   - An anecdote reports Pangram instability under 250 words.
   - Very short outputs will get noisy verdicts whatever the quality. Don't read meaning into them.
5. **Genre.**
   - FPR is highest for poetry, recipes, Wikipedia-like, templated and factual text: Pangram's domain table, and RAID's 52% FPR for ZeroGPT on recipes.
   - Detectors declare factual Q&A, manuals, bullet lists and code out of scope.
   - Scientific and formal registers are where style imitation slips through most (Epoch: 24–48%), because human formal prose is already close to LLM prose.
   - **Skill implication:** in formal genres, specificity and real data matter more than stylistic tinkering.
6. **The "chat register" is the core signal.**
   - The HIP paper (base models look human) and the Pangram 4 caveat about humans who absorbed LLM style both point to post-training habits: assistant tone, balanced hedging, formulaic structure, stock vocabulary.
   - Expert readers also cite "AI vocabulary," formality, low originality and over-clarity.
   - **Skill implication:** removing these habits is a legitimate quality goal. A detector score can serve at most as a weak diagnostic of "assistant voice," never as a target. Optimizing against a detector is the evasion arms race DAMAGE shows degrades fluency.
7. **Voice from real samples.**
   - 5-shot imitation of a *real author's own passages* measurably shifted detectors (Epoch 2026).
   - For an honest skill this means writing in the user's own voice from their own samples, which is the skill's stated purpose anyway. Do not present it as a bypass. Even so, about 80–90% of such text was still caught, and "Mixed" verdicts are common.

### 4.2 Tricks known not to work (or that work only against weak or old detectors)

| Trick | Evidence it fails | Notes |
|---|---|---|
| Synonym swapping / word-level paraphrase | RAID: Originality improved on synonym attacks, to 96.5%. DAMAGE: 98% recall on humanized text. Pangram 4: 92.8–99.7% recall across 13 humanizers. | It also degrades meaning. Low-tier humanizers fabricate citations. |
| Commercial humanizers (Undetectable, StealthGPT, WriteHuman, etc.) | DAMAGE; Pangram 4; Turnitin bypasser (Aug 2025); GPTZero bypasser training | Humanized text beat the original on quality only 3–26% of the time. Detectors increasingly flag "humanized" as its own class (Pangram humanizer head, Turnitin "AI-modified"). |
| Removing em dashes / banned-word lists | LessWrong anecdote: 94% → 83% → 100% AI after phrase removal. Pangram's design treats stock phrases only as supporting evidence. | It is cosmetic. It may improve style but does not change provenance. |
| Typos, casing changes, homoglyphs, zero-width spaces | These are now in Pangram 4 training data and in GPTZero's "Shield." Homoglyphs did break Originality in RAID 2024 (9.3%). | Deceptive, and it damages the text. Never use. |
| Single-pass DIPPER / QuillBot paraphrase | DAMAGE (DIPPER in training); GPTZero trains on DIPPER | It did defeat 2023-era detectors and watermarks: SynthID dropped from 66.5% to 1.5% after DIPPER. |
| Grammarly "fix mistakes" to launder AI text | Polish of *AI* text stays AI | Polish of *human* text stays human, which is correct. |
| Raising sampling temperature / repetition penalty | RAID showed large drops for detectors in 2024 | **[UNVERIFIED]** whether 2026 detectors remain sensitive to this. Not a writing-quality lever anyway. |
| Iterative LLM rewriting or base-model paraphrasing (HIP) | **Does** evade current detectors (HIP 2026; LessWrong) | Deliberate evasion. Out of scope for an honest skill. It is listed only because it reveals that the signal is the instruction-tuned register. |

### 4.3 Practical recommendations for the skill

- Do not claim or measure "undetectability." Say so in the skill description. AI-assisted text being labeled AI-assisted is a correct outcome.
- Define quality targets from what expert readers notice: specificity, original claims, a natural register, no assistant framing, no formulaic structure. Do not define them from what detectors score.
- Prefer minimal-edit revision of the author's own drafts over regeneration. Ask the author for concrete first-hand details rather than inventing them.
- Never use character-level tricks, deliberate typos, homoglyphs, invented anecdotes or fake citations. All of them are dishonest, degrade the text, and are now detected anyway.
- If detectors appear in evals at all, use several, read "Mixed" separately, use texts of at least 300 words, and treat the results as a diagnostic of chat register, never as a pass/fail goal.

---

## 5. Verification gaps

- arXiv 2402.14873 was read from the PDF. The abs and html pages timed out on permission.
- The GPTZero arXiv paper body was not read; only the abstract and the alphaXiv overview were.
- The Pangram 4 report's arXiv ID (possibly 2607.27183) is unconfirmed.
- HIP (2605.19516) numbers were not read. Only secondary summaries were.
- The Russell et al. per-detector table was not read. The claim that Pangram did best there is **not** asserted.
- Perkins et al. per-tool numbers and the list of tools were not read.
- No independent evaluation of Turnitin's August 2025 bypasser detection, ZeroGPT post-2024, or Copyleaks V11 was found.
- Turnitin's ELL bias study was not read.
- Model names in the Epoch and vendor 2026 pages (Claude Opus 4.8, GPT-5.5, Gemini 3.1 Pro, etc.) are reported as written there and were not cross-checked.
- All page content came through a summarizing fetch tool. Exact figures should be spot-checked against the PDFs before anything is published.
