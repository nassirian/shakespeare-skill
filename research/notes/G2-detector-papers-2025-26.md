# AI-text detection research, 2025–2026: additions to the existing reading list

Compiled 2026-10-12. This list leaves out everything already on the skill's reading list (GLTR … Miklian & Katsos).
Every URL below was fetched with WebFetch and resolved, except where a note says otherwise. Figures come from the abstract or HTML full text as fetched. Where only an abstract was available, the entry says so.
Strength ratings: **strong** means peer-reviewed at a top venue with large or controlled data. **moderate** means peer-reviewed at a workshop or minor venue, a vendor-authored paper, or a solid preprint. **weak** means a small preprint, a self-report, or a paper with no published numbers.

Topic key: (1) humanizers and paraphrase attacks, (2) mixed or AI-polished text, (3) which features detectors use and what survives editing, (4) how much human editing it takes, and co-writing, (5) independent benchmarks of commercial detectors, (6) newest models.

---

## 1. Jabarian & Imas (2025). *Artificial Writing and Automated Detection.* NBER Working Paper 34223 (also BFI WP 2025-116). DOI 10.3386/w34223
- URL: https://www.nber.org/papers/w34223 (PDF: https://www.nber.org/system/files/working_papers/w34223/w34223.pdf)
- Venue/status: NBER working paper, Sept 2025. Not peer-reviewed. The authors are independent academics (Chicago Booth). Topics 5, 6, 1.
- Design: 1,992 human passages across 6 genres (novels 1,000, news 300, blogs 200, Amazon reviews 200, résumés 192, restaurant reviews 100). Each passage was matched with AI versions from GPT-4.1, Claude Opus 4, Claude Sonnet 4 and Gemini 2.0 Flash. Detectors: Pangram, OriginalityAI, GPTZero and open-source RoBERTa. The study also tests stubs under 50 words and StealthGPT humanizer output.
- Findings (Youden thresholds): average FPR was about 0.002 for Pangram, 0.009 for GPTZero, 0.008 for Originality and 0.58 for RoBERTa. Commercial FPR peaked in **short review genres**: GPTZero 2.4% on Amazon reviews, Originality 2.2% and Pangram 0.75% on restaurant reviews. On stubs, FPR rose to about 2.5–3.3% and Claude Opus 4 news stubs were missed often (FNR up to 0.22 for Pangram and 0.44 for GPTZero). On humanized (StealthGPT) text, FNR was 0–0.05 for Pangram, 0.02–0.21 for Originality and 0.26–0.77 for GPTZero. Pangram was the only detector that met a strict FPR ≤ 0.005 policy cap.
- Takeaway for the skill: the best commercial detectors rarely flag long human prose. The real risk zone is **short, formulaic genres** such as reviews and blurbs. A commercial humanizer did not reliably defeat the strongest detector. For honest writing, the lesson is that surface rewording does little. What matters is real specificity and voice, especially in short pieces where generic phrasing is all a reader sees.
- Strength: **strong** (large and well-designed, though still a working paper). Caution: GPTZero's marketing cites a Jan 2026 "Chicago Booth benchmark" update with GPTZero at 99.5% and Pangram at 99.1% accuracy. I did not find or verify an updated paper.

## 2. Saha & Feizi (2025). *Almost AI, Almost Human: The Challenge of Detecting AI-Polished Writing.* Findings of ACL 2025, pp. 25414–25431. DOI 10.18653/v1/2025.findings-acl.1303
- URL: https://aclanthology.org/2025.findings-acl.1303/ (arXiv 2502.15666)
- Venue/status: ACL Findings 2025, peer-reviewed. Topics 2, 4.
- Design: the APT-Eval dataset has about 11.7K samples built from 300 human texts in 6 domains (blogs, email, news, game reviews, abstracts, speech). Each text was polished at 4 degree levels (extremely minor to major) and 7 percentage levels (1–75% of words), by GPT-4o, Llama-3.1-70B, Llama-3-8B and Llama-2-7B. The authors ran about 11 detectors on the results.
- Findings: **light polishing gets flagged.** GLTR's FPR on unpolished text was 6.83%, but it flagged 40.87% of GPT-4o "extremely-minor" polishes and 26.85% of texts where only 1% of words changed. Detectors barely track how much was edited: RoBERTa-large flagged 47.7% of minor polishes and 52.0% of major ones, and FastDetectGPT flagged 10.1% at 1% edits and 9.6% at 75%. Older and smaller polishers were flagged more (Llama-2 about 45% vs. GPT-4o and Llama-3 about 27–32%). Speech-style text was misclassified most (36–56%) and abstracts least (17–31%).
- Takeaway for the skill: running a human draft through an LLM "polish" pass can leave a detectable signature that is out of proportion to how much changed. An honest skill should **edit with targeted, visible changes** and keep the author's own sentences, rather than regenerating whole passages.
- Strength: **strong**.

## 3. Thai, Emi, Masrour & Iyyer (2026). *EditLens: Quantifying the Extent of AI Editing in Text.* ICLR 2026 (poster). arXiv 2510.03154
- URL: https://iclr.cc/virtual/2026/poster/10008153 (arXiv: https://arxiv.org/abs/2510.03154)
- Venue/status: ICLR 2026, peer-reviewed. Three of the four authors are from Pangram Labs. Topics 2, 4.
- Design: Mistral-Small-24B with a regression head, trained to predict the *magnitude* of AI editing. Supervision comes from cosine-embedding distance or soft-n-gram distance between the original and edited text. Training data: 60k examples, edits by GPT-4.1, Claude 4 Sonnet and Gemini 2.5 Flash from 303 editing prompts. Held out: Llama-3.3-70B and the Enron domain.
- Findings: human vs. any-AI F1 was 95.6, against 83.7 for Pangram, 81.4 for Binoculars and 80.5 for FastDetectGPT. On the ternary human / AI-edited / AI task, macro-F1 was 90.4 vs. 72.7 for GPTZero and 69.5 for Pangram. On APT-Eval, the score correlated with polish magnitude at r = 0.606. **Human editing of AI text (BEEMO) lowered scores by 0.33 ± 0.30, and scores fell in 88.9% of documents.** Successive AI edits kept raising the score. On Grammarly, "Fix any mistakes" produced the smallest edit signal, while "Summarize" and "Make it more detailed" produced the largest. A typo-fix floor was used so trivial corrections do not count as AI editing.
- Takeaway for the skill: detection is moving from yes/no to "**how much** AI rewriting happened". Copy-editing (grammar fixes) leaves almost no trace. Expansion, summarization and wholesale rewriting leave a large one. The skill should prefer minimal, local edits, which are also better editing practice.
- Strength: **strong**.

## 4. Artemova, Lucas, Venkatraman, Lee, Tilga, Uchendu & Mikhailov (2025). *Beemo: Benchmark of Expert-edited Machine-generated Outputs.* NAACL 2025 (Long), pp. 6992–7018
- URL: https://aclanthology.org/2025.naacl-long.357/ (arXiv 2411.04032)
- Venue/status: NAACL 2025, peer-reviewed. Topics 2, 4, 3.
- Design: 19.6k texts from 2,187 prompts. For each prompt the dataset holds a human answer, an answer from one of 10 LLMs, a version **edited by professional experts**, and versions edited by GPT-4o or Llama-3.1-70B. The authors ran 33 detector configurations.
- Findings: experts changed about 70% of the text, fixing facts, hallucinations, repetitive vocabulary, unnatural flow and formatting. Expert editing reduced separability by up to about 22 AUROC points (Binoculars: 83.9 for human vs. machine, 61.2 for human vs. expert-edited). **LLM-edited text stayed much more detectable** (78–80 AUROC). RADAR was near chance on expert edits. Zero-shot detectors generalized better than fine-tuned ones.
- Takeaway for the skill: substantive human editing moves text toward human-like, while asking an LLM to "make it more human" mostly does not. What expert editors fixed (repetitive word choice, unnatural flow, format clutter, factual vagueness) is a useful checklist for the skill.
- Strength: **strong**.

## 5. Baumler, Bao, Nghiem, Yang, Carpuat & Daumé III (2026). *Can You Make It Sound Like You? Post-Editing LLM-Generated Text for Personal Style.* ACL 2026 (Long), pp. 43867–43895
- URL: https://aclanthology.org/2026.acl-long.2030/ (arXiv 2604.24444)
- Venue/status: ACL 2026, peer-reviewed, pre-registered. Topics 4, 3.
- Design: 81 Prolific participants wrote personal texts (vows, apologies) in two ways: alone, and by post-editing an LLM draft (o4-mini). Style was measured with LUAR author embeddings, plus Pangram scores.
- Findings: post-editing raised similarity to the writer's own style (g = 0.55) and lowered Pangram AI scores (g = −0.45). However, **post-edited text stayed much closer to LLM style than to the person's own writing (g = −1.43)**. It was also more homogeneous across writers (g = 1.42 vs. unassisted). Participants felt the edited texts were as much "theirs" as their own writing (p = .906), and that perception correlated only weakly with measured style (r = 0.244). Edits were shallow: writers removed about 23% of em dashes and added contractions about 5× more often, but **rarely removed LLM-typical vocabulary**.
- Takeaway for the skill: this is the key result. Light post-editing (punctuation, contractions) gives people a false sense of ownership while the LLM's structure and diction remain. A voice-preserving skill has to work at the level of **content selection, structure and word choice**, and should lean on the author's own samples, not punctuation swaps.
- Strength: **strong**.

## 6. Cheng, Sadasivan, Saberi, Saha & Feizi (2025). *Adversarial Paraphrasing: A Universal Attack for Humanizing AI-Generated Text.* NeurIPS 2025 (poster). arXiv 2506.07001
- URL: https://neurips.cc/virtual/2025/poster/116833 (arXiv: https://arxiv.org/abs/2506.07001)
- Venue/status: NeurIPS 2025, peer-reviewed. Topic 1.
- Findings: simple LLM paraphrasing *raised* detection on some detectors (+8.6% T@1%F on RADAR, +15.0% on Fast-DetectGPT). Paraphrasing guided by a detector at each token cut T@1%F by an average of 87.9% across 8 detectors, including watermarks: KGW fell from 1.00 to 0.13. Quality fell slightly (GPT-4o rating 4.48 vs. 4.75 for plain paraphrase), and the attack transfers across detectors.
- Takeaway for the skill: "humanizing" by naive paraphrase is not only dishonest, it often does not work. Detector-guided evasion is an adversarial optimization problem, not a writing-quality problem. This supports keeping the skill **detector-agnostic** and quality-focused.
- Strength: **strong**.

## 7. Masrour, Emi & Spero (2025). *DAMAGE: Detecting Adversarially Modified AI Generated Text.* Proc. 1st GenAI Content Detection Workshop (GenAIDetect @ COLING 2025), pp. 120–133
- URL: https://aclanthology.org/2025.genaidetect-1.9/ (arXiv 2501.03437)
- Venue/status: workshop, peer-reviewed. Vendor-authored (Pangram). Topic 1.
- Findings: audit of **19 commercial humanizers and paraphrasers** in 3 fluency tiers. On a GPT-4o fluency win rate (how often the humanized text was judged more coherent than the original), tier L1 tools averaged 26%, L2 14.7% and L3 2.7%. Most humanizers degrade the prose. TPR on humanized text at 5% FPR: GPTZero 60%, Binoculars 28%, DAMAGE 98%. A GPT-4o humanizer fine-tuned specifically against DAMAGE was still detected 93% of the time. DIPPER paraphrasing removed SynthID watermarks (TPR fell from 87.6% to 5.4%).
- Takeaway for the skill: commercial humanizers mostly make text **worse** (less coherent) and are detectable by detectors trained on their output. The honest route of actually better writing is also the more durable one.
- Strength: **moderate** (workshop venue, vendor conflict of interest).

## 8. Karr, Khvatskii, Hua & Chawla (2026). *Why AI Detection Fails for Academic Integrity.* ACM AI Leadership Summit (AILS '26). arXiv 2608.11256
- URL: https://arxiv.org/abs/2608.11256
- Venue/status: AILS '26 (ACM), minor venue. Independent authors (Notre Dame). Topics 2, 5, 1, 3.
- Design: 642 published abstracts in chemistry, CS, political science and theology, from 2013–15 and 2023–25. The authors ran AI rewrites and Undetectable AI humanization, then scored everything with Pangram and GPTZero at a 0.5 threshold.
- Findings: abstracts that were only *lightly refined* by AI were flagged 38–80% of the time. Of pre-LLM originals (2013–15), 0% were flagged. Of 2023–25 originals, Pangram flagged 14.9% and GPTZero 8.9% (unconfirmed, possibly undisclosed AI use). **Non-STEM text was flagged far more often** (Pangram: theology 26.6% vs. chemistry 2.1%, p < .001). Density of long words and Academic Word List vocabulary correlated with AI scores (ρ ≈ 0.30–0.35). After humanization, fewer than 4% of AI rewrites were still flagged, and the two detectors stopped agreeing.
- Takeaway for the skill: dense, abstract academic vocabulary correlates with "AI" scores even in human text. Plain, concrete wording is both better prose and less likely to be misread. Note the conflict with study 1 on humanizer robustness: results depend on the specific tool, the genre and the detector version.
- Strength: **moderate**.

## 9. Rivera Soto, Chen & Andrews (2025). *Language Models Optimized to Fool Detectors Still Have a Distinct Style (And How to Change It).* arXiv 2505.14608 (v2, Sept 2025)
- URL: https://arxiv.org/abs/2505.14608
- Venue/status: preprint, no venue listed (JHU and LLNL). Topic 3.
- Findings: DPO-tuning Mistral-7B against FastDetectGPT dropped FastDetectGPT AUROC from 0.72 to 0.18 and Binoculars from 0.70 to 0.17. **A few-shot stylometric detector (StyleDetect) barely moved (0.96 to 0.95).** A paraphraser optimized to match a specific human's style evades all the detectors tested, but with more documents per author the text becomes distinguishable again. The authors argue detection should move to **multi-document** analysis.
- Takeaway for the skill: style, meaning consistent authorial choices across many documents, is the signal that survives token-level evasion. Over a body of work, an LLM's default voice shows. The skill should anchor on a specific author's voice rather than "generic human".
- Strength: **moderate** (strong lab, but a preprint).

## 10. Wang, Dou, Xiong & Lian (2026). *Reasoning-Aware AIGC Detection via Alignment and Reinforcement (REVEAL).* Findings of ACL 2026
- URL: https://aclanthology.org/2026.findings-acl.1043.pdf
- Venue/status: ACL Findings 2026, peer-reviewed. Topics 6, 2.
- Findings: AIGC-text-bank has about 67k human, 699k AI and 732k **AI-polished** texts from 12 generators across 10 domains. REVEAL (Qwen3-8B, SFT on o3 reasoning traces, then RL) averages 91.2% accuracy and 90.3 macro-F1. As zero-shot judges, prompted reasoning LLMs are decent (o3 87.3%, GPT-5 86.1%), while plain LLMs are at chance (GPT-4o 48.8%). On the **3-way task (human / AI-native / AI-polished), everything is weak**: REVEAL 70.7%, GPT-5 48.3%, o3 47.5%. RoBERTa-SFT fell from 89% to 73% out of domain.
- Takeaway for the skill: frontier reasoning models can act as fairly competent AI-text judges, but telling *polished human* text from AI-native text is still largely unsolved. That supports the skill's stance that the right goal is quality, not a "pass".
- Strength: **moderate–strong**.

## 11. Glickenhaus, Thai, Russell, Masrour, Han, Spero & Emi (2026). *Pangram 4 Technical Report.* arXiv 2607.27183
- URL: https://arxiv.org/abs/2607.27183 (verified via https://papers.cool/arxiv/2607.27183 and arXiv HTML)
- Venue/status: vendor technical report, not peer-reviewed. Topics 6, 2, 1.
- Findings (self-reported): AUROC 0.9916, FPR 0.0041% (about 1 in 24k), FNR 0.34%. The model has a token-level 3-class head (human / AI-assisted / AI-generated), a 15-bucket "AI fraction" head per 512-token segment, and a separate humanizer head. Text under 50 words is not analyzed. The authors note that letting the humanizer head train the backbone concentrated false positives on **academic writing and ESL essays**. The report says the model targets the newest frontier models, but the HTML excerpt cut off before the evaluation section, so I could not verify per-model, domain or boundary numbers.
- Takeaway for the skill: commercial detectors now report **span-level and "AI-assisted" labels**, not just a document verdict, so mixed drafts are segmented. Academic and ESL prose remain the known false-positive risk.
- Strength: **moderate** (vendor self-report; evaluation section not verified).

## 12. Su, Wang, Wan, Zhang & Luo (2025). *HACo-Det: A Study Towards Fine-Grained Machine-Generated Text Detection under Human-AI Coauthoring.* ACL 2025 (Long), pp. 22015–22036
- URL: https://aclanthology.org/2025.acl-long.1069/ (arXiv 2506.02959)
- Venue/status: ACL 2025, peer-reviewed. Topic 2.
- Findings: an automatic pipeline makes word-level-labelled co-authored text through multi-turn partial LLM paraphrasing of human text. Seven document-level detectors were adapted to word and sentence level. **Metric-based (zero-shot) detectors average only 0.462 F1** at fine granularity. Fine-tuned models do better, but the authors call the problem "far from solved". (The abstract and HTML did not give per-detector numbers.)
- Takeaway for the skill: per-word attribution in co-written text is still unreliable, so any "this sentence is AI" highlighting from tools should be treated as weak evidence.
- Strength: **moderate**.

## 13. Maier, Zaiss & Bayer (2026). *Beating the Style Detector: Three Hours of Agentic Research on the AI-Text Arms Race.* arXiv 2605.02620
- URL: https://arxiv.org/abs/2605.02620 (verified via https://papers.cool/arxiv/2605.02620)
- Venue/status: preprint, agent-conducted re-analysis. Topics 6, 4, 3.
- Findings: it re-ran the Baumler et al. (ACL 2026) data with **GPT-5.5 and Claude Opus 4.7** as style imitators, given held-out author samples. The models closed about 71–75% of the style gap to the author's ceiling, vs. about 24% for the human post-edit, and beat the human post-edit on about 80% of tasks. A stylometric SVM on LUAR embeddings still detected the mimics (AUC 0.93–1.00). GPT-5.5 detection was mostly a **length confound**, while Opus detection reflected a real stylistic signature. With 20 feedback iterations against a frozen detector, an agent flipped 2 of 5 test mimics.
- Takeaway for the skill: with real author samples, frontier models imitate voice much better than people do by hand-editing. Even so, length and stylistic habits remain detectable. Matching the target length and register of the author's real writing matters.
- Strength: **weak–moderate** (fast, agentic, small adversarial n; useful as the only evidence found on GPT-5.5 / Opus 4.7).

## 14. Pudasaini, Miralles-Pechuán, Lillis & Llorens Salvador (2026). *Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy.* arXiv 2603.23146
- URL: https://arxiv.org/abs/2603.23146 (verified via arXiv HTML and papers.cool)
- Venue/status: preprint. Topic 3.
- Findings: an interpretable detector with 30 linguistic features reaches F1 0.9734 in-domain (PAN-CLEF 2025, COLING 2025 shared tasks), but degrades substantially across domains and generators. SHAP shows **the most important features differ by dataset**: the best in-domain discriminators are the ones most sensitive to domain shift, formatting and length.
- Takeaway for the skill: many "AI tells" that detectors learn depend on the dataset (formatting, length, genre conventions) rather than being universal. Generic checklists of tells are fragile. Specificity and voice are the robust aims.
- Strength: **weak–moderate** (preprint; cross-domain numbers not extracted).

---

## Considered but not included (weaker or unverified)
- Dik, Erdem & Dik (2025), *Assessing GPTZero's Accuracy…*, arXiv 2506.23517: 78 essays, 16% FPR on human essays. Too small and no venue. https://arxiv.org/abs/2506.23517
- DAMASHA (Sai Teja et al., arXiv 2512.04838; an ACL preview lists Findings of EACL 2026) and Sai Teja et al., sentence-level segmentation (arXiv 2509.17830): mixed-text span detection. The abstracts give no numbers, or the evaluation is narrow.
- Lu et al. (2026), *Detecting LLM-Generated Tokens in Human–LLM Coauthored Text*, arXiv 2607.21458: token-level smoothing with an adaptive bandwidth. No numbers on the abstract page.
- Fu, Guo & Li (2025), *DetectAnyLLM / MIRAGE* (17 LLMs), arXiv 2509.14268: claims more than 70% improvement. Numbers not verified.
- Kuznetsov et al. (2025), *Feature-Level Insights into Artificial Text Detection with Sparse Autoencoders*, arXiv 2503.03601: LLM style is most distinct in information-dense domains. No numbers on the abstract page.
- A PMC article, "Does a Human-drafted Letter Edited by ChatGPT Escape Detection…" (PMC12889295), could not be fetched because of a captcha, so it is unverified.

## Cross-cutting takeaways for an honest-prose skill
1. Detectors now measure **how much** AI rewriting happened and **where**, not just yes/no (EditLens, Pangram 4, REVEAL). Light copy-editing leaves little trace, while regenerating, expanding or summarizing leaves a lot.
2. Shallow human edits (em dashes, contractions) change perception more than substance (Baumler). Real change comes from content, structure and word choice, which is also what expert editors did in Beemo.
3. Commercial humanizers mostly degrade coherence (DAMAGE), and naive paraphrase can *increase* detection (Adversarial Paraphrasing). Results also vary by tool and detector (Jabarian & Imas vs. Karr).
4. False-positive hot spots for human text are **short, formulaic genres**, **dense academic or non-STEM abstract vocabulary**, and **ESL and academic prose** (Jabarian & Imas, Karr, Pangram 4, APT-Eval domain effects).
5. Stylometric, multi-document signals are the ones that survive token-level evasion (Rivera Soto, Maier). Anchoring on the specific author's own samples is the principled route to "sounds like a person".
