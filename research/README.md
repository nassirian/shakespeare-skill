# Research

Shakespeare's rules draw on the 31 AI-text-detection papers listed below and on 17 newer style studies listed in [research-basis.md](../skills/shakespeare/references/research-basis.md). The PDFs are not included in this repository because most are not licensed for redistribution. Use the source links, or run `python3 research/download_papers.py` to fetch them and check them against the SHA-256 hashes in `manifest.json`.

The list was compiled in September 2026. Repository copies may be preprints or revised manuscripts rather than publisher typeset versions. Years follow the reading list and are not necessarily the revision year of the downloaded copy.

| # | Paper | Source |
|---|---|---|
| 1 | GLTR: Statistical Detection and Visualization of Generated Text (2019) | [Source](https://aclanthology.org/P19-3019.pdf) |
| 2 | Defending Against Neural Fake News — Grover (2019) | [Source](https://arxiv.org/pdf/1905.12616) |
| 3 | DetectGPT (2023) | [Source](https://arxiv.org/pdf/2301.11305) |
| 4 | DetectLLM (2023) | [Source](https://aclanthology.org/2023.findings-emnlp.827.pdf) |
| 5 | RADAR: Robust AI-Text Detection via Adversarial Learning (2023) | [Source](https://arxiv.org/pdf/2307.03838) |
| 6 | Fast-DetectGPT (2024) | [Source](https://arxiv.org/pdf/2310.05130) |
| 7 | Ghostbuster: Detecting Text Ghostwritten by Large Language Models (2024) | [Source](https://nlp.cs.berkeley.edu/pubs/Verma-Fleisig-Tomlin-Klein_2024_Ghostbuster_paper.pdf) |
| 8 | DNA-GPT (2024) | [Source](https://arxiv.org/pdf/2305.17359) |
| 9 | Spotting LLMs With Binoculars (2024) | [Source](https://arxiv.org/pdf/2401.12070) |
| 10 | Raidar: geneRative AI Detection viA Rewriting (2024) | [Source](https://www.cs.columbia.edu/~junfeng/papers/raidar-iclr24.pdf) |
| 11 | Glimpse (2025) | [Source](https://arxiv.org/pdf/2412.11506) |
| 12 | AdaDetectGPT (2025) | [Source](https://proceedings.neurips.cc/paper_files/paper/2025/file/808bc5e3d076c1125a87f81b42d5e52d-Paper-Conference.pdf) |
| 13 | DNA-DetectLLM (2025) | [Source](https://papers.neurips.cc/paper_files/paper/2025/file/0287c393907259ae6a269fca5e3509cd-Paper-Conference.pdf) |
| 14 | A Watermark for Large Language Models (2023) | [Source](https://arxiv.org/pdf/2301.10226) |
| 15 | Robust Distortion-free Watermarks for Language Models (2024) | [Source](https://arxiv.org/pdf/2307.15593) |
| 16 | On the Reliability of Watermarks for Large Language Models (2024) | [Source](https://arxiv.org/pdf/2306.04634) |
| 17 | MULTITuDE (2023) | [Source](https://aclanthology.org/2023.emnlp-main.616.pdf) |
| 18 | MAGE: Machine-generated Text Detection in the Wild (2024) | [Source](https://aclanthology.org/2024.acl-long.3.pdf) |
| 19 | M4: Multi-Generator Multi-Domain and Multi-Lingual Black-Box Machine-Generated Text Detection (2024) | [Source](https://aclanthology.org/2024.eacl-long.83.pdf) |
| 20 | RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors (2024) | [Source](https://arxiv.org/pdf/2405.07940) |
| 21 | DetectRL (2024) | [Source](https://papers.neurips.cc/paper_files/paper/2024/file/b61bdf7e9f64c04ec75a26e781e2ad51-Paper-Datasets_and_Benchmarks_Track.pdf) |
| 22 | GPT detectors are biased against non-native English writers (2023) | [Source](https://arxiv.org/pdf/2304.02819) |
| 23 | Can AI-Generated Text be Reliably Detected (2023) | [Source](https://arxiv.org/pdf/2303.11156) |
| 24 | On the Possibilities of AI-Generated Text Detection (2024) | [Source](https://arxiv.org/pdf/2304.04736) |
| 25 | Paraphrasing evades detectors of AI-generated text but retrieval is an effective defense (2023) | [Source](https://arxiv.org/pdf/2303.13408) |
| 26 | Testing of Detection Tools for AI-Generated Text (2023) | [Source](https://arxiv.org/pdf/2306.15666) |
| 27 | A Practical Examination of AI-Generated Text Detectors for Large Language Models (2024) | [Source](https://arxiv.org/pdf/2412.05139) |
| 28 | People who frequently use ChatGPT for writing tasks are accurate and robust detectors of AI-generated text (2025) | [Source](https://arxiv.org/pdf/2501.15654) |
| 29 | Who wrote this Evaluating the reliability of AI detection tools in higher education (2026) | [Source](https://link.springer.com/content/pdf/10.1007/s40979-026-00226-w.pdf) |
| 30 | Towards Possibilities and Impossibilities of AI-generated Text Detection: A Survey (2023) | [Source](https://arxiv.org/pdf/2310.15264) |
| 31 | A Survey on LLM-Generated Text Detection: Necessity Methods and Future Directions (2025) | [Source](https://aclanthology.org/2025.cl-1.8.pdf) |

## Detector studies

The 18 sources on current commercial detectors (D01–D18) are listed with links in [research-basis.md](../skills/shakespeare/references/research-basis.md#detector-studies-d01d18). They are links only.

## Other files here

- `AI-Writing-Recognition-Research-Guide.md`: a synthesis of the 31 papers, written with AI assistance (ChatGPT) in September 2026 and reviewed for this project. Check figures against the papers before citing them.
- `notes/`: the pattern-extraction notes behind Shakespeare v2, written by AI agents in October 2026 while reading the papers. See `notes/README.md`.
- `manifest.json`: titles, source URLs, page counts and SHA-256 hashes for the PDFs.
