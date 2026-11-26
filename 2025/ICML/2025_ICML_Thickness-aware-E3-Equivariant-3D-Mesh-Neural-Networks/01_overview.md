# Thickness-aware E(3)-Equivariant 3D Mesh Neural Networks

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v267/kim25r.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/167333. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICML
- Authors: Sungwon Kim, Namkyeong Lee, Yunyoung Doh, Seungmin Shin, Guimok Cho, Seung-Won Jeon, Sangkook Kim, Chanyoung Park
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: equivariant, 3D Vision, 3D geometry
- Official paper: https://proceedings.mlr.press/v267/kim25r.html
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v267/main/assets/kim25r/kim25r.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/kim25r/kim25r.pdf)

## Why This Paper Is Here

T-EMNN은 표면 메시와 국소 두께가 주어졌을 때 사출 성형 부품의 변형을 예측한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/kim25r/kim25r.pdf#page=1) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/kim25r/kim25r.pdf#page=4)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Mesh-based 3D static analysis methods have recently emerged as efficient alternatives to traditional computational numerical solvers, significantly reducing computational costs and runtime for various physics-based ...
- **p. 1 / Abstract - extractive body cue:** However, these methods primarily focus on surface topology and geometry, often overlooking the inherent thickness of real-world 3D objects, which exhibits high correlations and similar ...
- **p. 1 / Abstract - extractive body cue:** This limitation arises from the disconnected nature of these surfaces and the absence of internal edge connections within the mesh.
- **p. 1 / Abstract - extractive body cue:** In this work, we propose a novel framework, the Thickness-aware E(3)-Equivariant 3D Mesh Neural Network (T-EMNN), that effectively integrates the thickness of 3D objects while ...
- **p. 1 / Abstract - extractive body cue:** Additionally, we introduce data-driven coordinates that encode spatial information while preserving E(3)-equivariance or invariance properties, ensuring consistent and robust analysis.
- **p. 2 / 1. Introduction - extractive body cue:** However, meshbased objects, which represent the geometry and topology of surfaces, face challenges in accurately modeling these interactions due to the lack of connections between ...
- **p. 1 / 1. Introduction - extractive body cue:** However, existing mesh-based methods focus solely on modeling the surfaces of 3D objects, overlooking their thickness.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** The key contributions of this study are as follows: • Thickness-Aware Framework: We propose a Thicknessaware E(3)-Equivariant 3D Mesh Neural Networks (TEMNN) that accurately models ...
- **p. 1 / 1. Introduction - extractive body cue:** To quantitatively illustrate the significance of these interactions, we present an analysis in Fig.
- **p. 3 / 4. Methodology - extractive body cue:** T-EMNN consists of an encoder (Sec.
- **p. 3 / 4. Methodology - extractive body cue:** Our method, T-EMNN, extends the encode-process-decode framework of MGN (Pfaff et al., 2020), introducing key innovations for handling 3D shapes with thickness while incorporating spatial ...
- **p. 5 / 4.2.3. THICKNESS PROCESSOR - extractive body cue:** In addition, to account for thickness-related interactions, we introduce a thickness edge ei,thick connecting vi to T (vi), with its feature fi,thick ∈R2 defined as: ...
- **p. 4 / 4.2.1. ENCODER - extractive body cue:** The outputs of the geometric encoders, z(0) i ∈Rd and e(0) ij ∈ Rd, are later used as the input embeddings for the first layer ...
- **p. 6 / 4.2.3. THICKNESS PROCESSOR - extractive body cue:** The embedding for this thickness edge ei,thick ∈Rd is initialized in the first layer using a dedicated encoder, ϕthick, which maps the thickness edge feature ...
- **p. 5 / 4.2.3. THICKNESS PROCESSOR - extractive body cue:** By training on real-world data, the model dynamically adapts to identify the optimal threshold τ that captures interactions between opposing surfaces without relying on manual ...

## Observation, State, and Output Interface

| 항목 | 원문에서 확인한 범위 |
|---|---|
| 입력 | 성형 부품의 표면 메시와 국소 두께 |
| 표현 | 메시 이웃과 두께 방향을 포함한 그래프 |
| 출력 | 각 절점의 3차원 변위 |
| 평가 | 사출 성형 부품의 변형 예측 오차 |

[원문 3쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/kim25r/kim25r.pdf#page=3) · [원문 7쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/kim25r/kim25r.pdf#page=7)

## Main Claims and Actual Contribution

- 두께를 반영한 메시 표현과 형상에 정렬한 좌표계를 구성해 회전·평행이동에 일관된 변형을 예측한다. [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/kim25r/kim25r.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/kim25r/kim25r.pdf#page=5) · [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/kim25r/kim25r.pdf#page=6)
- 사출 부품의 변형 자료에서 오차를 평가하고 두께 정보와 좌표 정렬을 제거한 결과를 비교했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/kim25r/kim25r.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/kim25r/kim25r.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/kim25r/kim25r.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 7 (5.4.1. MAIN RESULTS), p. 7 (5.4.1. MAIN RESULTS) |
| Embodiment/environment | We evaluate T-EMNN using a dataset from real-world injection molding applications. | hardware/simulator version and reset protocol | p. 6 (5.1. Dataset Description), p. 6 (5.1. Dataset Description) |
| Dataset/benchmark | We assess the model performance using three metrics: 1) RMSE, which evaluates the effectiveness of handling outliers, 2) MAE, which measures the consistency and accuracy of the model's predictions, and 3) R2, ... | role, split, size and leakage | p. 6 (5.1. Dataset Description), p. 6 (5.1. Dataset Description), p. 7 (5.3. Evaluation Settings), p. 8 (5.4.3. EVALUATION UNDER DYNAMIC SETTING) |
| Metric | This underscores the critical role of E(3)-equivariance in ensuring the robustness of the coordinate system. | definition, denominator, direction and uncertainty | p. 7 (5.4.1. MAIN RESULTS), p. 7 (5.4.1. MAIN RESULTS), p. 8 (5.4.1. MAIN RESULTS) |
| Baseline/ablation | 8, all baseline models exhibit improved performance when incorporating thickness edges compared to their counterparts without them. | fair input/data/compute/action matching | p. 8 (5.4.2. IMPACT OF THICKNESS-AWARE FRAMEWORK), p. 8 (5.4.1. MAIN RESULTS), p. 6 (5.2. Baselines) |

## Explicit Limitations and Failure Boundary

- **p. 14 / Figure/Table caption - extractive body cue:** Figure 14. Comparisons between volume mesh and surface mesh. The methods used for comparison are based on the MGN framework with coordinate embeddings from our ...
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 13. R2 scores for all test data. In the shape IDs, ‘s' indicates seen shapes included in the training data, while ‘us' refers to ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 4. Comparison of training speed (iteration/sec) and GPU memory usage (MB) across different models. Our model is based on MGN, with an additional thickness ...
- **p. 6 / 5.3. Evaluation Settings - extractive body cue:** Note that the out-of-distribution scenario is designed to assess how well the methods adapt to objects 6
- **p. 7 / 5.4.1. MAIN RESULTS - extractive body cue:** This underscores the critical role of E(3)-equivariance in ensuring the robustness of the coordinate system.
- **p. 7 / 5.3. Evaluation Settings - extractive body cue:** Model Performance in In-Distribution and Out-of-Distribution Settings, averaged over 3 seeds with standard deviation (in parentheses).
- **p. 8 / 5.4.2. IMPACT OF THICKNESS-AWARE FRAMEWORK - extractive body cue:** Moreover, when the threshold is set to zero-removing thickness edges-performance degrades significantly.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.3. Thickness in the Mesh), p. 4 (4.2.1. ENCODER)이다.

## 검색 태그 근거

표면 메시에서 공간 연결과 국소 두께를 함께 표현하는 E(3) 등변 네트워크로 사출 성형 부품의 변위를 추정한다. 평가에서는 변형 예측 오차를 비교했다. [원문 3쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/kim25r/kim25r.pdf#page=3) · [원문 7쪽](https://raw.githubusercontent.com/mlresearch/v267/7914d3407046b308db90001490534e422dab7d87/assets/kim25r/kim25r.pdf#page=7)
