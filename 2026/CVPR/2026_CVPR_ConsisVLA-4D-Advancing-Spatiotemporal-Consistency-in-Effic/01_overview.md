# ConsisVLA-4D: Advancing Spatiotemporal Consistency in Efficient 3D-Perception and 4D-Reasoning for Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Li_ConsisVLA-4D_Advancing_Spatiotemporal_Consistency_in_Efficient_3D-Perception_and_4D-Reasoning_for_CVPR_2026_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_ConsisVLA-4D_Advancing_Spatiotemporal_Consistency_in_Efficient_3D-Perception_and_4D-Reasoning_for_CVPR_2026_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / CVPR
- Authors: Wei Li, Jizhihui Liu, Li Yixing, Junwen Tong, Rui Shao, Liqiang Nie
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, consistency, 4D reasoning
- Official paper: https://openaccess.thecvf.com/content/CVPR2026/html/Li_ConsisVLA-4D_Advancing_Spatiotemporal_Consistency_in_Efficient_3D-Perception_and_4D-Reasoning_for_CVPR_2026_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_ConsisVLA-4D_Advancing_Spatiotemporal_Consistency_in_Efficient_3D-Perception_and_4D-Reasoning_for_CVPR_2026_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_ConsisVLA-4D_Advancing_Spatiotemporal_Consistency_in_Efficient_3D-Perception_and_4D-Reasoning_for_CVPR_2026_paper.pdf) 기준이다.

## Why This Paper Is Here

ConsisVLA-4D는 지시에 등장하는 물체를 여러 시점에서 대응시키고 행동에 따른 장면 변화를 학습해 조작 행동을 예측한다. [PDF 1쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_ConsisVLA-4D_Advancing_Spatiotemporal_Consistency_in_Efficient_3D-Perception_and_4D-Reasoning_for_CVPR_2026_paper.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Current Vision-Language-Action (VLA) models primarily focus on mapping 2D observations to actions but exhibit notable limitations in spatiotemporal perception and reasoning: 1) spatial representations often ...
- **p. 1 / Abstract - extractive body cue:** To address these challenges, we propose ConsisVLA-4D, a unified and efficient framework that enhances spatiotemporal consistency in 3D-Perception and 4D-Reasoning.
- **p. 1 / Abstract - extractive body cue:** Specifically, we design: 1) CV-Aligner, which ensures CrossView object semantic consistency via filtering instructionrelevant regions and aligning object identities across multiple viewpoints; 2) CO-Fuser, which ...
- **p. 1 / Abstract - extractive body cue:** Building upon these, we introduce 3) CS-Thinker to achieve Cross-Scene spatiotemporal consistency as actions unfold.
- **p. 1 / Abstract - extractive body cue:** It learns implicit knowledge of local dynamics from object-semantic tokens of CV-Aligner and global depth from geometric tokens of CO-Fuser, thereby enhancing efficient visual reasoning ...
- **p. 2 / 1. Introduction - extractive body cue:** Due to the lack of a comprehensive understanding of current spatial states and insufficient knowledge of evolving scene dynamics, existing methods struggle to build consistent ...
- **p. 1 / 1. Introduction - extractive body cue:** Representative works such as RT2 [6], Octo [61], OpenVLA [28], and π-series [4, 15, 23, 50] highlight the potential of the VLA paradigm in bridging ...

## Core Idea

- **p. 2 / 3) Cross-Scene - extractive body cue:** Our contributions are summarized as follows: • We propose ConsisVLA-4D, an efficient and innovative framework that advances spatiotemporal consistency in 3D-Perception and 4D-Reasoning. • We ...
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose ConsisVLA-4D, a unified and efficient framework that enhances spatiotemporal consistency in 3D-perception and 4D-reasoning, as shown in Fig.
- **p. 1 / Abstract - extractive body cue:** Building upon these, we introduce 3) CS-Thinker to achieve Cross-Scene spatiotemporal consistency as actions unfold.
- **p. 4 / 4.2. Cross-View Object Semantic Consistency - extractive body cue:** (12) To inject 3D information into zobj i and establish associations between objects with the same identity across different viewpoints, we introduce Single-Fusion, which performs ...
- **p. 4 / 4.1. Proposed Framework - extractive body cue:** (5) On the other hand, we use the aggregated geometric relation zagg-3D L′ to infer the depth representations of future multiview perspectives as actions unfold: ...
- **p. 5 / 4.4. Cross-Scene Spatiotemporal Consistency - extractive body cue:** In the SC-Attn module, each dynamic token 0dyn-4D i is independently guided by its corresponding object representation zobj-3D i and the instruction embedding t: \ ...
- **p. 1 / Abstract - extractive body cue:** Current Vision-Language-Action (VLA) models primarily focus on mapping 2D observations to actions but exhibit notable limitations in spatiotemporal perception and reasoning: 1) spatial representations often ...
- **p. 5 / 4.4. Cross-Scene Spatiotemporal Consistency - extractive body cue:** Cross-Scene Thinker with Spatiotemporal Consistency Attention (SC-Attn) ensures: 1) Three sets of initialized dynamic tokens decode dynamic object representations for one view (CoTracker [26, 27] ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Current Vision-Language-Action (VLA) models primarily focus on mapping 2D observations to actions but exhibit notable limitations in spatiotemporal perception and reasoning: 1) spatial representations often rely on additional sensors, i ... | image/video, language instruction, proprioception과 history | p. 1 (Abstract), p. 1 (1. Introduction) |
| State/latent | Current, Vision-Language-Action, VLA, models, primarily, focus, mapping, observations, actions, exhibit, notable, limitations | language-grounded task state와 action-policy context | p. 1 (Abstract), p. 1 (1. Introduction), p. 4 (4.1. Proposed Framework) |
| Output/action | D): 1) CV-Aligner extracts instructionrelated and cross-correlated spatial objects; 2) CO-Fuser aggregates multi-view geometric relation; 3) CS-Thinker infers actions based on implicit knowledge of future dynamic objects and global depth. | continuous action, pose 또는 action chunk | p. 1 (1. Introduction), p. 4 (4.1. Proposed Framework), p. 3 (3. Preliminary & Problem Definition) |
| Objective/outcome | During this process, the initialized action tokens 0A are decoded in parallel to yield ˆA, optimized using the L1 loss Laction. | instruction following, task success, generalization과 latency | p. 6 (4.4. Cross-Scene Spatiotemporal Consistency), p. 2 (1. Introduction), p. 3 (3. Preliminary & Problem Definition) |

## Main Claims and Actual Contribution

- 시점 사이에서 물체의 정체성을 정렬하고 물체 간 공간 관계와 시간에 따른 국소 동역학을 정책 표현에 결합한다. [PDF 3쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_ConsisVLA-4D_Advancing_Spatiotemporal_Consistency_in_Efficient_3D-Perception_and_4D-Reasoning_for_CVPR_2026_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_ConsisVLA-4D_Advancing_Spatiotemporal_Consistency_in_Efficient_3D-Perception_and_4D-Reasoning_for_CVPR_2026_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_ConsisVLA-4D_Advancing_Spatiotemporal_Consistency_in_Efficient_3D-Perception_and_4D-Reasoning_for_CVPR_2026_paper.pdf#page=5)
- LIBERO와 RoboTwin 2.0에서 과제 성공률을 비교하고 시공간 정보를 처리하는 구성 요소의 역할을 평가했다. [PDF 6쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_ConsisVLA-4D_Advancing_Spatiotemporal_Consistency_in_Efficient_3D-Perception_and_4D-Reasoning_for_CVPR_2026_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_ConsisVLA-4D_Advancing_Spatiotemporal_Consistency_in_Efficient_3D-Perception_and_4D-Reasoning_for_CVPR_2026_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_ConsisVLA-4D_Advancing_Spatiotemporal_Consistency_in_Efficient_3D-Perception_and_4D-Reasoning_for_CVPR_2026_paper.pdf#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (5.2. Overall Performance & Efficiency), p. 7 (5.2. Overall Performance & Efficiency) |
| Embodiment/environment | We conduct evaluations across multiple simulation benchmarks, including: 1) the four task suites of LIBERO [44]-Spatial, Object, Goal, and Long; 2) three pick-and-place tasks emphasizing spatial scene perception in ManiSkill2 [19]; and ... | hardware/simulator version and reset protocol | p. 6 (5.1. Experimental Setup), p. 7 (5.1. Experimental Setup) |
| Dataset/benchmark | 5, for both simulation and real-world results: 1) Removing ES-Sel. and S-Fus. from CV-Aligner prevents the filtering of redundant visual inputs and fails to align object identities across different viewpoints, leading to ... | role, split, size and leakage | p. 6 (5.1. Experimental Setup), p. 7 (5.1. Experimental Setup), p. 7 (5.3. Ablation Studies), p. 6 (5.1. Experimental Setup) |
| Metric | Decimal values indicate averages over 15 trials, and the average success rate reflects complete task completion. | definition, denominator, direction and uncertainty | p. 7 (5.1. Experimental Setup), p. 7 (5.2. Overall Performance & Efficiency), p. 8 (5.3. Ablation Studies) |
| Baseline/ablation | 3, despite adding approximately 2B parameters (mainly from VGGT), ConsisVLA-4D achieves 2.31× and 1.25× speedups in inference latency and 1.36× and 1.43× speedups in training cost compared to the base 7B baseline ... | fair input/data/compute/action matching | p. 7 (5.2. Overall Performance & Efficiency), p. 6 (5.1. Experimental Setup), p. 6 (5.1. Experimental Setup) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 5.3. Ablation Studies - extractive body cue:** 5, for both simulation and real-world results: 1) Removing ES-Sel. and S-Fus. from CV-Aligner prevents the filtering of redundant visual inputs and fails to align ...
- **p. 8 / 6. Conclusion - extractive body cue:** Through the integration of CVAligner, CO-Fuser, and CS-Thinker, it achieves cross-view, cross-object, and cross-scene consistency, enabling robust and efficient understanding of dynamic environments.
- **p. 7 / 5.2. Overall Performance & Efficiency - extractive body cue:** Notably, its realworld results are nearly consistent with those on RoboTwin 2.0 (ALOHA manipulator), demonstrating robust sim-toreal transfer capability.
- **p. 8 / 5.3. Ablation Studies - extractive body cue:** Moreover, all modules are adaptively designed, and swapping them with counterparts in SigLIP and DINOv2 degrades performance.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (3. Preliminary & Problem Definition), p. 2 (3) Cross-Scene)이다.
