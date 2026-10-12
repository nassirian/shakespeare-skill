# Research basis and limits

Shakespeare's rules come from 66 sources: the 31 AI-text-detection papers in the original collection, 17 newer studies (2024–2026) of how LLM prose differs from human prose and how expert writers edit it, and 18 sources (2024–2026) on how current commercial detectors work and what changes their results. The skill hasn't been tested as an intervention in any of these studies. Its rules are editorial inferences from what they report, and following them does not guarantee that text will be indistinguishable from human writing.

## What the evidence supports, in brief

1. **Experienced readers catch AI text through clusters of habits.** Five people who use LLMs heavily caught 299 of 300 articles by majority vote, including paraphrased and "humanized" ones. Their explanations cited vocabulary (53%), sentence templates and lists of three (36%), uniform grammar and punctuation (25%), lack of originality (24%), homogeneous quotes (22%), over-explanation (20%), formatting (15%), tidy conclusions (13%), formality (12%) and stock names (12%). (P28)
2. **The habits come from planning more than wording.** Paraphrase, word-list avoidance, multi-pass humanizing and translation left the signal mostly intact for expert readers and for model-identification classifiers. (P28, N08, N04, P25)
3. **Models choose the most expected word, and people choose by meaning.** Human text uses words outside a model's top 100 predictions 2.4 times as often, and this holds across six years of models. The right response is the exact word, not a rare one. (P01, P03, P06, P09, P11, P13)
4. **Instruction tuning creates a single dense register.** Chat models overuse participle clauses (2–5×) and nominalizations (about 2×), underuse agentless passives, and write every genre in the same style. (N02)
5. **Polishing creates the fingerprint.** Asked to polish human text, models rewrite it heavily toward their own style. LLM rewrites also flatten individual voice. (P10, N13)
6. **Self-assessment is unreliable.** Models judge writing quality and "slop" near chance. (N01, N05, N14, N15)
7. **Plain writing is not AI writing.** Detectors flagged non-native writers' plain prose, and formulaic human genres look machine-like. (P22, P18, P09)
8. **Detectors measure provenance more than style.** Current commercial detectors are trained classifiers, trained against topic-matched AI texts and humanizer output. Substantive human content and human editing lower their scores; style tweaks, humanizer tools and paraphrase mostly don't. (D03, D04, D05, D07, D11, D14)

## Sources

Strength ratings reflect design, sample size and peer review, not importance to the skill.

### Original detection collection (P01–P31)

| Code | Paper | Main contribution to the skill | Strength |
|---|---|---|---|
| P01 | Gehrmann et al., [GLTR](https://aclanthology.org/P19-3019/) (ACL 2019 demo) | Humans use low-rank (unexpected but correct) words far more often | Strong |
| P02 | Zellers et al., [Grover](https://arxiv.org/abs/1905.12616) (NeurIPS 2019) | Truncated sampling never reaches the tail; templated news looks machine-like | Strong (dated) |
| P03 | Mitchell et al., [DetectGPT](https://arxiv.org/abs/2301.11305) (ICML 2023) | Model phrasing sits at a probability peak; machine creative writing is generic | Strong |
| P04 | Su et al., [DetectLLM](https://aclanthology.org/2023.findings-emnlp.827/) (EMNLP Findings 2023) | Log-rank signal; confirms P01 | Strong |
| P05 | Hu et al., [RADAR](https://arxiv.org/abs/2307.03838) (NeurIPS 2023) | "Sound more human" prompting produced superlative-stacked prose still flagged | Moderate |
| P06 | Bao et al., [Fast-DetectGPT](https://arxiv.org/abs/2310.05130) (ICLR 2024) | Machines pick by statistics, humans by intent; persona prompts don't help | Strong |
| P07 | Verma et al., [Ghostbuster](https://nlp.cs.berkeley.edu/pubs/Verma-Fleisig-Tomlin-Klein_2024_Ghostbuster_paper.pdf) (NAACL 2024) | AI text grows more predictable toward the end; style prompts barely change signal | Strong |
| P08 | Yang et al., [DNA-GPT](https://arxiv.org/abs/2305.17359) (ICLR 2024) | Models regenerate their own closers almost verbatim ("Our findings highlight the importance of…") | Moderate–strong |
| P09 | Hans et al., [Binoculars](https://arxiv.org/abs/2401.12070) (ICML 2024) | Odd topics don't read human; "non-robotic" prompts swap in casual clichés; memorized text looks machine-like | Strong |
| P10 | Mao et al., [Raidar](https://www.cs.columbia.edu/~junfeng/papers/raidar-iclr24.pdf) (ICLR 2024) | LLM polish rewrites human text heavily and adds employ/showcase/participial chains; barely changes AI text | Strong |
| P11 | Bao et al., [Glimpse](https://arxiv.org/abs/2412.11506) (ICLR 2025) | Rare-word substitution hurts readability | Strong |
| P12 | Zhou et al., [AdaDetectGPT](https://proceedings.neurips.cc/paper_files/paper/2025/file/808bc5e3d076c1125a87f81b42d5e52d-Paper-Conference.pdf) (NeurIPS 2025) | Statistical only; nothing direct for writing | — |
| P13 | Zhu et al., [DNA-DetectLLM](https://papers.neurips.cc/paper_files/paper/2025/file/0287c393907259ae6a269fca5e3509cd-Paper-Conference.pdf) (NeurIPS 2025) | Human text departs from the greedy path; academic human text is close to model defaults | Strong |
| P14 | Kirchenbauer et al., [A Watermark for LLMs](https://arxiv.org/abs/2301.10226) (ICML 2023) | Watermarks are a separate, embedded signal; nothing for style | — |
| P15 | Kuditipudi et al., [Distortion-free watermarks](https://arxiv.org/abs/2307.15593) | Same | — |
| P16 | Kirchenbauer et al., [Reliability of watermarks](https://arxiv.org/abs/2306.04634) (ICLR 2024) | Sentence-by-sentence human paraphrase leaks structure | Moderate |
| P17 | Macko et al., [MULTITuDE](https://aclanthology.org/2023.emnlp-main.616/) (EMNLP 2023) | Model families cluster; English rules may not transfer to other languages | Moderate |
| P18 | Li et al., [MAGE](https://aclanthology.org/2024.acl-long.3/) (ACL 2024) | Machine documents ~20% longer; over-grammatical in informal genres; positive bias in reviews; many surface differences vanish across domains | Strong |
| P19 | Wang et al., [M4](https://aclanthology.org/2024.eacl-long.83/) (EACL 2024) | Narrower vocabulary; hook-question and "Overall" scaffolding in examples | Moderate |
| P20 | Dugan et al., [RAID](https://arxiv.org/abs/2405.07940) (ACL 2024) | Models more repetitive (Self-BLEU); evasion tricks inconsistent and damaging | Strong |
| P21 | Wu et al., [DetectRL](https://papers.neurips.cc/paper_files/paper/2024/file/b61bdf7e9f64c04ec75a26e781e2ad51-Paper-Datasets_and_Benchmarks_Track.pdf) (NeurIPS 2024 D&B) | "Write in human style" prompts move detectors 1–2%; polish adds "robust framework" boilerplate | Moderate |
| P22 | Liang et al., [GPT detectors are biased against non-native writers](https://arxiv.org/abs/2304.02819) (Patterns 2023) | Plain diction flagged; "elevate" prompts fool 2023 detectors while adding flowery tells | Strong (dated tools) |
| P23 | Sadasivan et al., [Can AI-generated text be reliably detected?](https://arxiv.org/abs/2303.11156) | Recursive paraphrase drifts facts | Moderate |
| P24 | Chakraborty et al., [On the possibilities of AI-generated text detection](https://arxiv.org/abs/2304.04736) | Signal accumulates with length and repetition | Strong (theory) |
| P25 | Krishna et al., [Paraphrasing evades detectors](https://arxiv.org/abs/2303.13408) (NeurIPS 2023) | Paraphrase keeps content; drift in names and facts | Strong |
| P26 | Weber-Wulff et al., [Testing of detection tools](https://arxiv.org/abs/2306.15666) (IJEI 2023) | Machine translation leaves traces; patchwriting changes surface only | Moderate |
| P27 | Tufts et al., [A practical examination of AI-generated text detectors](https://arxiv.org/abs/2412.05139) | "Sound human" prompts don't help; rewrites of human content are hardest to flag | Moderate |
| P28 | Russell, Karpinska, Iyyer, [People who frequently use ChatGPT… are accurate and robust detectors](https://arxiv.org/abs/2501.15654) (ACL 2025) | The core source: clue taxonomy, word lists, humanization results | Strong (5 raters, one genre) |
| P29 | Van Vlasselaer et al., [Who wrote this?](https://link.springer.com/article/10.1007/s40979-026-00226-w) (IJEI 2026) | Humanize prompts barely move strong detectors; most real use is hybrid | Moderate |
| P30 | Ghosal et al., [Towards possibilities and impossibilities of AI-generated text detection](https://arxiv.org/abs/2310.15264) | Background | — |
| P31 | Wu et al., [A survey on LLM-generated text detection](https://aclanthology.org/2025.cl-1.8/) (Computational Linguistics 2025) | Secondary summary: longer, noun-heavy, positive, generic | Weak (secondhand) |

### Newer style studies (N01–N17)

| Code | Paper | Main contribution to the skill | Strength |
|---|---|---|---|
| N01 | Chakrabarty, Laban, Wu, [Can AI writing be salvaged?](https://arxiv.org/abs/2409.14509) (2024–25; venue unconfirmed) | 18 professional writers, 8,035 edits on 1,057 model paragraphs: awkward word choice 28%, poor sentence structure 20%, unnecessary exposition 18%, cliché 17%, plus purple prose, lack of specificity, tense inconsistency | Strong |
| N02 | Reinhart et al., [Do LLMs write like humans?](https://arxiv.org/abs/2410.16107) (PNAS 2025) | Participle clauses 2–5×, nominalizations ~2×, agentless passive ~0.5×; vocabulary ratios (tapestry 155×, camaraderie 162×); one register for all genres | Strong |
| N03 | Shaib et al., [Detection and measurement of syntactic templates](https://arxiv.org/abs/2407.00211) (EMNLP 2024) | Repeated part-of-speech templates survive synonym swaps and alignment | Strong |
| N04 | Russell et al., [StoryScope](https://arxiv.org/abs/2604.03136) (COLM 2026) | 61,608 stories: explicit themes, embodied emotion, tidy single-track plots, morally clean heroes; narrative signal survives style edits | Strong |
| N05 | Shaib et al., [Measuring AI "slop" in text](https://arxiv.org/abs/2509.19163) (preprint) | Copy-editors' slop judgments driven by relevance, density and tone; LLM judges near zero agreement | Moderate |
| N06 | Paech et al., [Antislop](https://arxiv.org/abs/2510.15061) (ICLR 2026) | Slop words and phrases across 67 models, some over 1,000× human frequency; "not X but Y" up to 6.3× | Strong |
| N07 | Kobak et al., [Delving into LLM-assisted writing in biomedical publications through excess vocabulary](https://arxiv.org/abs/2406.07016) (Science Advances 2025) | Excess style verbs and adjectives in 15M PubMed abstracts (delves 28×) | Strong |
| N08 | Sun et al., [Idiosyncrasies in large language models](https://arxiv.org/abs/2502.12150) (ICML 2025) | Model identifiable from formatting alone (73%) and after paraphrase (~91%); assistant framing words | Strong |
| N09 | Liang et al., [Mapping the increasing use of LLMs in scientific papers](https://arxiv.org/abs/2404.01268) (COLM 2024) | realm, intricate, showcasing, pivotal | Strong |
| N10 | Liang et al., [Monitoring AI-modified content at scale](https://arxiv.org/abs/2403.07183) (ICML 2024) | Peer-review vocabulary (meticulous 34.7×); expanding notes into prose creates the signal | Strong |
| N11 | Czuma, [Em-ergence of the em-dash](https://arxiv.org/abs/2606.29540) (preprint 2026) | Em-dash prevalence in medRxiv Discussions 4.2% → 20.3% | Moderate (single author, preregistered) |
| N12 | Freeburg, [The last fingerprint](https://arxiv.org/abs/2603.27006) (preprint 2026) | Em dashes persist when markdown is suppressed | Weak |
| N13 | Sourati, Karimi-Malekabadi, Dehghani et al., [The shrinking landscape of linguistic diversity](https://arxiv.org/abs/2502.11266) (Nature Human Behaviour 2026) | Rewrites cut stylistic variance 21–50% and erase identity markers | Strong |
| N14 | Chakrabarty et al., [Art or artifice?](https://arxiv.org/abs/2309.14556) (CHI 2024) | Expert creativity tests: subtext, endings, pacing, character | Moderate (2023 models) |
| N15 | Chakrabarty, Laban, Wu, [AI-Slop to AI-Polish?](https://arxiv.org/abs/2504.07532) (preprint) | Detect-then-edit helps; LLMs near chance at judging quality; content quality limits style | Moderate |
| N16 | Chakrabarty, Ginsburg, Dhillon, [Readers prefer outputs of AI trained on copyrighted books](https://arxiv.org/abs/2510.13939) (preprint) | Experts' dislike of prompted AI text tracks cliché density | Moderate |
| N17 | Miklian & Katsos, ["That's AI slop, you bot!"](https://arxiv.org/abs/2606.12073) (preprint 2026) | Online AI accusations don't track real AI features | Moderate |


### Detector studies (D01–D18)

| Code | Source | Main contribution to the skill | Strength |
|---|---|---|---|
| D01 | Jabarian & Imas, [Artificial Writing and Automated Detection](https://www.nber.org/papers/w34223) (NBER WP 34223, 2025) | Independent test of Pangram, GPTZero, Originality across 6 genres and 4 LLMs: commercial false positives under 1% on long text, highest in short reviews and sub-50-word stubs; humanizer resistance varies widely by detector | Strong (working paper) |
| D02 | Saha & Feizi, [Almost AI, Almost Human](https://aclanthology.org/2025.findings-acl.1303/) (ACL Findings 2025) | Light AI polish of human text gets flagged out of proportion to the change; one detector flagged 41% of "extremely minor" polishes | Strong |
| D03 | Thai, Emi, Masrour & Iyyer, [EditLens](https://arxiv.org/abs/2510.03154) (ICLR 2026) | Detection of *how much* AI editing occurred; grammar fixes leave little trace, summarizing and expanding a lot; human editing lowered scores in 89% of documents | Strong (Pangram-affiliated authors) |
| D04 | Artemova et al., [Beemo](https://aclanthology.org/2025.naacl-long.357/) (NAACL 2025) | Expert editing of AI text cut detector separability by up to 22 AUROC points; LLM edits didn't | Strong |
| D05 | Baumler et al., [Can You Make It Sound Like You?](https://aclanthology.org/2026.acl-long.2030/) (ACL 2026) | People post-editing AI drafts mostly removed dashes and added contractions; the result stayed closer to LLM style than to their own (g = −1.43) | Strong |
| D06 | Cheng et al., [Adversarial Paraphrasing](https://arxiv.org/abs/2506.07001) (NeurIPS 2025) | Plain LLM paraphrasing raised detection on some detectors; only detector-guided optimization evaded them | Strong |
| D07 | Masrour, Emi & Spero, [DAMAGE](https://aclanthology.org/2025.genaidetect-1.9/) (GenAIDetect @ COLING 2025) | Audit of 19 humanizers: all degraded coherence; detectors trained on them catch most output | Moderate (workshop, vendor authors) |
| D08 | Karr et al., [Why AI Detection Fails for Academic Integrity](https://arxiv.org/abs/2608.11256) (AILS 2026) | Dense academic vocabulary correlates with AI scores in human text; theology abstracts flagged far more than chemistry | Moderate |
| D09 | Rivera Soto, Chen & Andrews, [Language Models Optimized to Fool Detectors Still Have a Distinct Style](https://arxiv.org/abs/2505.14608) (preprint 2025) | Stylometric signals survive token-level evasion, especially across several documents | Moderate |
| D10 | Wang et al., [REVEAL](https://aclanthology.org/2026.findings-acl.1043.pdf) (ACL Findings 2026) | Telling AI-polished human text from AI-native text is still largely unsolved (≤71% on a 3-way task) | Moderate–strong |
| D11 | Glickenhaus et al., [Pangram 4 Technical Report](https://pangram-public.s3.us-east-1.amazonaws.com/pdf/pangram_4_technical_report.pdf) (2026) | Segment-level human / AI-assisted / AI labels, humanizer head, 50-word minimum; false positives concentrated in poetry, recipes, academic and ESL text | Moderate (vendor self-report) |
| D12 | Su et al., [HACo-Det](https://aclanthology.org/2025.acl-long.1069/) (ACL 2025) | Word- and sentence-level attribution in co-written text is unreliable | Moderate |
| D13 | Pudasaini et al., [Why AI-Generated Text Detection Fails](https://arxiv.org/abs/2603.23146) (preprint 2026) | The features detectors learn depend on dataset, formatting and length; generic tell lists are fragile | Weak–moderate |
| D14 | Emi & Spero, [Technical Report on the Pangram AI-Generated Text Classifier](https://arxiv.org/abs/2402.14873) (2024) | Synthetic "mirror" training texts and hard-negative mining: the classifier learns how text was produced, not its topic | Moderate (vendor) |
| D15 | Adam et al., [GPTZero: Robust Detection of LLM-Generated Texts](https://arxiv.org/abs/2602.13042) (2026) | Deep classifier with Human / AI / Mixed and Polished / Paraphrased labels; trained on bypasser output | Moderate (vendor; read via abstract and overview) |
| D16 | Lee, [AI detectors' false negatives](https://epoch.ai/data-insights/ai-detectors-false-negatives) (Epoch AI, 2026) | No false positives for Pangram or GPTZero on 495 pre-2022 passages, 19 for Originality; style imitation from real author samples raised misses to 10–18% | Moderate (small cells) |
| D17 | Xu et al., [Base Models Look Human to AI Detectors](https://arxiv.org/abs/2605.19516) (preprint 2026) | Detectors mainly key on the instruction-tuned "chat register" | Weak (numbers not verified) |
| D18 | Turnitin, [AI writing detection capabilities](https://guides.turnitin.com/hc/en-us/articles/28477544839821) (vendor documentation, 2025–26) | Transformer classifier, 300-word minimum, not tuned to grammar fixes, bypasser detection since Aug 2025, ~4% sentence-level false positives clustered near AI text | Moderate (vendor) |

## Limits

- Most findings come from English and from 2023–2026 models. Vocabulary lists date quickly, and each model family has its own.
- Expert-reader results come from small panels and specific genres (news, literary fiction, abstracts).
- Several newer sources are preprints. Where a rule rests on one, the catalog says so.
- The detector findings describe 2024–2026 tools that are retrained often. Several sources are vendor reports with obvious interests; treat their numbers as claims.
- The skill does not inspect or remove watermarks, query generation archives or run classifiers. Good writing and verified provenance are separate questions.
- Venues for N01 and the preprints are as listed on arXiv in October 2026. Check them before citing formally.
