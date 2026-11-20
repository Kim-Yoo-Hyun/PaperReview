# Learning Transferable Visual Models From Natural Language Supervision

> Evidence maturity: `FULL_TEXT_CHECKED`.
> 2026-11-19 표본 감사에서 요약과 관련 본문 표현을 원문에 대조해 교정했다. [원문](https://proceedings.mlr.press/v139/radford21a.html)
> Analysis basis: full-text PDF body checked on 2026-09-03 (48 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2103.00020.
> PDF retrieval source: https://arxiv.org/pdf/2103.00020. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / ICML
- Authors: Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, Ilya Sutskever
- Primary track: VLA and generalist robot policies
- Tier: CORE
- Tags: CLIP, Vision-Language Model, alignment
- Official paper: https://arxiv.org/abs/2103.00020
- Full-text retrieval: https://arxiv.org/pdf/2103.00020
- Code/Project: https://github.com/openai/CLIP
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (48 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

CLIP은 이미지에 대응하는 자연어 설명을 고르는 과제로 시각 표현을 학습해, 클래스 이름만으로 여러 이미지 분류 과제에 전이한다. [원문](https://proceedings.mlr.press/v139/radford21a.html)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** State-of-the-art computer vision systems are trained to predict a fixed set of predetermined object categories.
- **p. 1 / Abstract - extractive body cue:** This restricted form of supervision limits their generality and usability since additional labeled data is needed to specify any other visual concept.
- **p. 1 / Abstract - extractive body cue:** Learning directly from raw text about images is a promising alternative which leverages a much broader source of supervision.
- **p. 1 / Abstract - extractive body cue:** We demonstrate that the simple pre-training task of predicting which caption goes with which image is an efficient and scalable way to learn SOTA image ...
- **p. 1 / Abstract - extractive body cue:** After pre-training, natural language is used to reference learned visual concepts (or describe new ones) enabling zero-shot transfer of the model to downstream tasks.
- **p. 2 / 1. Introduction and Motivating Work - extractive body cue:** Both approaches also use static softmax classifiers to perform prediction and lack a mechanism for dynamic outputs.
- **p. 2 / 1. Introduction and Motivating Work - extractive body cue:** In this work, we close this gap and study the behaviors of image classifiers trained with natural language supervision at large scale.

## Core Idea

CLIP은 웹에서 수집한 이미지·텍스트 4억 쌍으로 두 인코더를 대조학습한다. 추론 시 이미지와 클래스 설명의 임베딩 유사도를 비교해 별도 분류기 학습 없이 클래스를 예측한다. [원문](https://proceedings.mlr.press/v139/radford21a.html)

## Observation, State, and Output Interface

영상과 클래스별 텍스트 프롬프트를 각각 인코딩한다. 두 임베딩 사이의 유사도에서 클래스별 점수와 예측값을 얻는다. [원문](https://proceedings.mlr.press/v139/radford21a.html)

## Main Claims and Actual Contribution

텍스트로 클래스 이름을 표현하면 같은 시각 인코더를 여러 이미지 분류 과제에 전이할 수 있었다. 분류 성능은 태스크와 프롬프트에 따라 달랐다. [원문](https://proceedings.mlr.press/v139/radford21a.html)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 8 (3.1.4. PROMPT ENGINEERING AND ENSEMBLING), p. 6 (3.1.3. INITIAL COMPARISON TO VISUAL N-GRAMS) |
| Embodiment/environment | The 20 datasets with at least 16 examples per class were used in this analysis. we see that zero-shot CLIP is quite weak on several specialized, complex, or abstract tasks such as ... | hardware/simulator version and reset protocol | p. 9 (3.1.5. ANALYSIS OF ZERO-SHOT CLIP PERFORMANCE), p. 6 (3.1.1. MOTIVATION) |
| Dataset/benchmark | This evaluation suite, detailed in Appendix A includes datasets representing the aforementioned tasks, German Traffic Signs Recognition Benchmark (Stallkamp et al., 2011), as well as several other datasets adapted from VTAB (Zhai ... | role, split, size and leakage | p. 9 (3.1.5. ANALYSIS OF ZERO-SHOT CLIP PERFORMANCE), p. 6 (3.1.1. MOTIVATION), p. 11 (3.2. Representation Learning), p. 16 (3.3. Robustness to Natural Distribution Shift) |
| Metric | On aYahoo, CLIP achieves a 95% reduction in the number of errors, and on SUN, CLIP more than doubles the accuracy of Visual N-Grams. | definition, denominator, direction and uncertainty | p. 7 (3.1.3. INITIAL COMPARISON TO VISUAL N-GRAMS), p. 13 (3.3. Robustness to Natural Distribution Shift), p. 14 (Figure/Table caption) |
| Baseline/ablation | Compared to the baseline of using contextless class names, prompt engineering and ensembling boost zero-shot classification performance by almost 5 points on average across 36 datasets. | fair input/data/compute/action matching | p. 7 (3.1.4. PROMPT ENGINEERING AND ENSEMBLING), p. 8 (3.1.5. ANALYSIS OF ZERO-SHOT CLIP PERFORMANCE), p. 8 (3.1.4. PROMPT ENGINEERING AND ENSEMBLING) |

## Explicit Limitations and Failure Boundary

- **p. 25 / 7.3. Future Work - extractive body cue:** This process of characterization can help researchers increase the likelihood models are used beneficially by: • Identifying potentially beneficial downstream uses of models early in ...
- **p. 11 / 3.2. Representation Learning - extractive body cue:** Fine-tuning, because it adapts representations to each dataset during the fine-tuning phase, can compensate for and potentially mask failures to learn general and robust representations ...
- **p. 18 / 6. Limitations - extractive body cue:** There are still many limitations to CLIP.
- **p. 20 / 6. Limitations - extractive body cue:** Our methodology has several significant limitations.
- **p. 20 / 6. Limitations - extractive body cue:** In our work, we fall back to fitting linear classifiers on top of CLIP's features.
- **p. 11 / 3.2. Representation Learning - extractive body cue:** Linear classifiers, because of their limited flexibility, instead highlight these failures and provide clear feedback during development.
- **p. 13 / 3.3. Robustness to Natural Distribution Shift - extractive body cue:** To what degree are these failures attributable to deep learning, ImageNet, or some combination of the two?

## Why Read It

언어로 시각 개념을 지정하는 표현이 VLA의 지각 단계에 어떻게 쓰일 수 있는지 읽는 원전이다. 이 논문이 평가한 출력은 이미지 분류 점수다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (48 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Both approaches also use static softmax classifiers to perform prediction and lack a mechanism for dynamic outputs. (p. 2, 1. Introduction and Motivating Work).
- **Actual contribution:** CLIP은 웹에서 수집한 이미지·텍스트 4억 쌍으로 두 인코더를 대조학습한다. 추론 시 이미지와 클래스 설명의 임베딩 유사도를 비교해 별도 분류기 학습 없이 클래스를 예측한다. [원문](https://proceedings.mlr.press/v139/radford21a.html)
- **Evaluation boundary:** The best CLIP model improves accuracy on ImageNet from a proof of concept 11.5% to 76.2% and matches the performance of the original ResNet-50 despite using none of the 1.28 ... (p. 6, 3.1.3. INITIAL COMPARISON TO VISUAL N-GRAMS).
- **Explicit failure boundary:** Linear classifiers, because of their limited flexibility, instead highlight these failures and provide clear feedback during development. (p. 11, 3.2. Representation Learning).
