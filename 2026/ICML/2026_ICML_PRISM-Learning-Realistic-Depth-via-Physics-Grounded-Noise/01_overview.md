# PRISM: Learning Realistic Depth via Physics-Grounded Noise Disentanglement with Semantic-Geometric Collaboration

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://icml.cc/virtual/2026/poster/65722.
> PDF retrieval source: https://openreview.net/pdf/9655ce373e592ae3473dc14dddd5cc2be47a3b47.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: Xiujian Liang, Jiacheng Liu, Mingyang Sun, Qichen He, Anda Cheng, Cewu Lu, Jianhua Sun
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: semantic, alignment, depth, 3D Vision, sim-to-real
- Official paper: https://icml.cc/virtual/2026/poster/65722
- Published PDF: https://raw.githubusercontent.com/mlresearch/v306/main/assets/liang26n/liang26n.pdf
- Full-text retrieval at original review: https://openreview.net/pdf/9655ce373e592ae3473dc14dddd5cc2be47a3b47.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (35 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/liang26n/liang26n.pdf)

## Why This Paper Is Here

PRISM은 합성 깊이 영상에 실제 센서에서 관찰되는 결측과 측정 오차를 더해 시뮬레이션에서 학습한 조작 정책의 실물 전이를 평가한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/liang26n/liang26n.pdf#page=1) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/liang26n/liang26n.pdf#page=4)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Real-world physical sensing exhibits complex, heterogeneous noise patterns that deviate significantly from idealized simulation, posing a fundamental bottleneck for sim-to-real transfer.
- **p. 1 / Abstract - extractive body cue:** Existing sensor modelings typically treat depth noise as a monolithic black-box process, overlooking the distinct physical mechanisms that govern different error modalities.
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce a physics-grounded paradigm that disentangles monolithic noise into two complementary modalities: sensing invalidation and measurement inaccuracy, enabling a tailored treatment ...
- **p. 1 / Abstract - extractive body cue:** Building on this insight, we propose PRISM, a tripartite framework that distills 3D Visual Foundation Model features as rich spatialsemantic priors for physics-based reasoning.
- **p. 1 / Abstract - extractive body cue:** To address the inherent sparsity and class imbalance of invalidation regions, we develop Hierarchical Positive-Prioritized Supervision, integrating multi-scale positive-weighted objectives with a positive-preserving dynamic hard ...
- **p. 1 / 1. Introduction - extractive body cue:** However, the deployment of simulation-trained policies remains fundamentally bottlenecked by the sim-to-real gap(Jia et al., 2025).
- **p. 1 / 1. Introduction - extractive body cue:** (a) The Reality Gap: Unlike pristine simulation, real-world physical sensing exhibits a bimodal noise distribution: black voids and gray residuals.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To operationalize this insight, we propose PRISM (PhysicsReasoned Implicit Sensor Modeling), a semantic-geometric collaborative framework designed to ′refract′ monolithic sensor noise into physically motivated modalities.
- **p. 2 / 1. Introduction - extractive body cue:** 2) Semantic-Geometric Collaboration: We propose PRISM, a unified framework that distills the rich physical common sense of 3D Visual Foundation Model to drive noise synthesis.
- **p. 3 / 3.1. Semantic-Physics Reasoner - extractive body cue:** The architecture consists of three sequential modules.
- **p. 3 / 3. Methodology - extractive body cue:** We present PRISM, a tripartite framework that synthesizes realistic depth by disentangling sensor noise into physically grounded modalities.
- **p. 5 / 3.4. Hierarchical Positive-Prioritized Supervision - extractive body cue:** To address the extreme class imbalance and ensure precise boundary detection, we propose a supervision strategy comprised of three coupled mechanisms.
- **p. 3 / 2.3. Visual Foundation Models as Semantic Priors - extractive body cue:** State-of-theart architectures like Metric3Dv2 (Hu et al., 2024) and MoGe (Wang et al., 2025b) employ ViT-based encoders to distill invariant geometric representations.
- **p. 5 / 3) Sequential Optimization Objectives. Since PRISM is - extractive body cue:** Stage I: Noise Disentanglement Learning.In addition to the pixel-wise classification, we introduce a Dice Loss to enforce shape compactness and prevent trivial solutions.
- **p. 4 / 2) Mask-Aware Denoising Objective. The frozen U-Net ϵθ - extractive body cue:** During inference, the predicted latent is decoded by the VAE Decoder D to obtain the residual ˆR = ψ-1(D(ˆz0)), which is added to Dsim to ...

## Observation, State, and Output Interface

| 항목 | 원문에서 확인한 범위 |
|---|---|
| 입력 | 깊이 합성에는 시뮬레이션 RGB·깊이, 실물 평가에는 센서 RGB·깊이 |
| 표현 | 센서 결측 및 측정 오차가 반영된 학습 깊이와 조작 정책 |
| 출력 | 합성 깊이 및 학습한 정책의 행동열 |
| 평가 | 깊이 데이터의 충실도와 실물 조작 성공 |

[원문 4쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/liang26n/liang26n.pdf#page=4) · [원문 5쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/liang26n/liang26n.pdf#page=5) · [원문 6쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/liang26n/liang26n.pdf#page=6) · [원문 8쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/liang26n/liang26n.pdf#page=8)

## Main Claims and Actual Contribution

- 깊이 결측과 유효 픽셀의 오차를 구분하고 시각 기초 모델의 의미·기하 특징과 희소한 결측 영역에 가중한 감독을 이용한다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/liang26n/liang26n.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/liang26n/liang26n.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/liang26n/liang26n.pdf#page=5)
- 합성 깊이의 품질과 실물 조작 성공률을 따로 측정하고 여섯 과제에서 DP3·PPT·RISE를 같은 깊이 합성 조건으로 비교했다. [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/liang26n/liang26n.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/liang26n/liang26n.pdf#page=8)

## Evaluation Scope

Franka Research 3와 Realman RM75에서 여섯 조작 과제를 평가했다. 표 3은 RISE의 과제별 20회 시행 성공 횟수를 세 시드로 집계하고, 표 4는 여섯 과제에서 DP3 91.1%, PPT 92.8%, RISE 92.5%의 평균 성공률을 각각 보고한다. [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/liang26n/liang26n.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/liang26n/liang26n.pdf#page=8)

## Explicit Limitations and Failure Boundary

- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Quantitative comparison of depth synthesis fidelity on ByteCameraDepth (In-Domain of Realsense D435). We evaluate three aspects: Overall Metrics (global reconstruction quality), Sensing Invalidation ...
- **p. 9 / 7. Limitations - extractive body cue:** While PRISM demonstrates strong capabilities in simulateddepth enhancement, it possesses certain limitations.
- **p. 9 / 7. Limitations - extractive body cue:** Second, the current per-frame generation pipeline does not explicitly enforce temporal consistency for highly dynamic scenes, leaving flickering noise across frames as a key open ...
- **p. 6 / 5.1. Experimental Settings - extractive body cue:** We utilize the provided models to construct aligned sim-real pairs and define the ground-truth invalidation mask by identifying native sensor failures (zeros or NaNs) in ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative evaluation of physics-grounded depth synthesis. (a) Disentangled Generation: PRISM decomposes noise into Sensing Invalidation (binary masks) and Measurement Inaccuracy (continuous residuals) to ...
- **p. 8 / 5.3. Downstream Application Evaluation - extractive body cue:** Articulated tasks on a Realman RM75 arm test robustness against translucent refraction, transparent obstacles, and severe occlusions during long-horizon behaviors like interacting with a drawer ...
- **p. 8 / 5.3. Downstream Application Evaluation - extractive body cue:** By physically grounding noise synthesis, PRISM forces the policy to learn compliant behaviors robust to sensor dropouts (e.g., inferring geometry from boundaries), achieving an average ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Semantic-Physics Reasoner), p. 3 (2.3. Visual Foundation Models as Semantic Priors)이다.

## 검색 태그 근거

합성 RGB와 깊이에서 실제 센서와 유사한 결측과 수치 잔차를 생성한다. 보정한 깊이로 모방 정책을 훈련하고, 실제 깊이 카메라를 장착한 로봇팔의 조작에서 전이를 평가한다. [원문 4쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/liang26n/liang26n.pdf#page=4) · [원문 5쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/liang26n/liang26n.pdf#page=5) · [원문 6쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/liang26n/liang26n.pdf#page=6) · [원문 8쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/liang26n/liang26n.pdf#page=8)
