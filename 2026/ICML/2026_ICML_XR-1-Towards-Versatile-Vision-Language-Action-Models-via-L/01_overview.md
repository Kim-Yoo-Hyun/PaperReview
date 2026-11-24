# XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (45 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://icml.cc/virtual/2026/oral/71118.
> PDF retrieval source: https://openreview.net/pdf/181715f87df4dd5677ebf2619dcb456e071c95dd.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: Shichao Fan, Kun Wu, Zhengping Che, Xinhua Wang, Di Wu, Fei Liao, Ning Liu, Yixue Zhang, Zhen Zhao, Zhiyuan Xu, Meng Li, Qingjie Liu, Shanghang Zhang, Min Wan, Jian Tang
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Imitation Learning
- Official paper: https://icml.cc/virtual/2026/oral/71118
- Published PDF: https://raw.githubusercontent.com/mlresearch/v306/main/assets/fan26f/fan26f.pdf
- Full-text retrieval at original review: https://openreview.net/pdf/181715f87df4dd5677ebf2619dcb456e071c95dd.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (45 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

XR-1은 영상에 나타나는 변화와 로봇의 운동을 공유하는 이산 표현으로 바꾸어 여러 로봇과 인간 시연에서 정책을 학습한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/fan26f/fan26f.pdf#page=1) · [PDF 2쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/fan26f/fan26f.pdf#page=2)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent progress in large-scale robotic datasets and vision-language models (VLMs) has advanced research on vision-language-action (VLA) models.
- **p. 1 / Abstract - extractive body cue:** However, existing VLA models still face two fundamental challenges: (i) producing precise low-level actions from high-dimensional ob
- **p. 1 / Abstract - extractive body cue:** 1Beijing Innovation Center of Humanoid Robotics, Beijing, China 2State Key Laboratory of Multimedia Information Processing, School of Computer Science.
- **p. 1 / Abstract - extractive body cue:** Existing methods often encode latent variables from either visual dynamics or robotic actions to guide policy learning, but they fail to fully exploit the complementary ...
- **p. 1 / Abstract - extractive body cue:** In this work, we present X Robotic Model 1 (XR-1), a novel framework for versatile and scalable VLA learning across diverse robots, tasks, and environments.
- **p. 2 / 1. Introduction - extractive body cue:** Despite VLM advancements, two challenges persist: (i) Precision Gap: Mapping high-dimensional observations to precise low-level actions is difficult due to multimodal uncertainty; even centimeter-level errors ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, prior research (Cui et al., 2023; Shafiullah et al., 2022; Lee et al., 2024; Xie et al., 2025; Zheng et al., ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as follows: • We propose X Robotic Model 1 (XR-1), a scalable three-stage framework for VLA learning that effectively leverages ...
- **p. 2 / 1. Introduction - extractive body cue:** Addressing the limitations of unimodal representations and inspired by human supramodal cognition, we propose X Robotic Model 1 (XR-1) to achieve cross-data exploitation and cross-embodiment ...
- **p. 4 / 3.1. Overview - extractive body cue:** We introduce XR-1, a scalable framework for cross-robot VLA learning (Figure 2), structured in three stages.
- **p. 5 / 3.1. Overview - extractive body cue:** To unify both modalities, we introduce a VQ-VAE codebook e ∈Rd×f with d discrete entries of dimension f.
- **p. 5 / 3.1. Overview - extractive body cue:** To mitigate this gap, we introduce an alignment loss that constrains visual codes to remain consistent with their motion counterparts: Lalign = DKL(q(ze mo) ∥q(ze ...
- **p. 4 / 3.1. Overview - extractive body cue:** The motion decoder Dmo(·) then takes the latent motion embedding zmo and optional conditions cd as input, such as the language instruction l, proprioceptive states ...
- **p. 4 / 3.1. Overview - extractive body cue:** At each inference step t, the policy π receives a language instruction l and multimodal observations o = ⟨c, m⟩, where c ∈RK×3×H×W denotes K ...
- **p. 5 / 3.1. Overview - extractive body cue:** In our implementation, we use the proprioceptive states m as the condition input.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | At each inference step t, the policy π receives a language instruction l and multimodal observations o = ⟨c, m⟩, where c ∈RK×3×H×W denotes K RGB images from external or robot-mounted cameras, ... | image/video, language instruction, proprioception과 history | p. 4 (3.1. Overview), p. 4 (3.1. Overview) |
| State/latent | inference, step, policy, receives, language, instruction, multimodal, observations, where, denotes, RGB, images | language-grounded task state와 action-policy context | p. 4 (3.1. Overview), p. 4 (3.1. Overview), p. 5 (3.1. Overview) |
| Output/action | The motion decoder Dmo(·) then takes the latent motion embedding zmo and optional conditions cd as input, such as the language instruction l, proprioceptive states m, and the observations o. | continuous action, pose 또는 action chunk | p. 4 (3.1. Overview), p. 5 (3.1. Overview), p. 5 (3.1. Overview) |
| Objective/outcome | Training follows standard VQ-VAE objectives (Van Den Oord et al., 2017), combining reconstruction losses with codebook and commitment regularization terms: Lvis = ∥ˆct+h -ct+h∥1 + β∥sg(zvis) -ze vis∥2 2 + β∥zvis -sg(ze ... | instruction following, task success, generalization과 latency | p. 5 (3.1. Overview), p. 5 (3.1. Overview), p. 4 (3.1. Overview) |

## Main Claims and Actual Contribution

- 두 입력을 처리하는 벡터 양자화 인코더로 공통 코드를 만들고, 코드를 예측하는 사전학습 뒤 이를 저수준 행동 학습의 중간 표현으로 사용했다. [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/fan26f/fan26f.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/fan26f/fan26f.pdf#page=5)
- 서로 다른 로봇과 작업에서 조작 성공률 및 새로운 조건에 대한 일반화를 평가하고 시각·운동 정보의 결합이 주는 효과를 분석했다. [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/fan26f/fan26f.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/fan26f/fan26f.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/fan26f/fan26f.pdf#page=8) · [PDF 9쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/fan26f/fan26f.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4.4. Generalization Analysis), p. 8 (4.4. Generalization Analysis) |
| Embodiment/environment | Unlike the UR-5e, this robot is unseen during pretraining (e.g., Stages 1 and 2 for XR1), making the evaluation a stringent embodiment-transfer benchmark. | hardware/simulator version and reset protocol | p. 7 (4.2. Results on Real-World Robotic Tasks), p. 6 (4. Experiments) |
| Dataset/benchmark | This trend unequivocally demonstrates the foundational importance of leveraging large and diverse datasets to learn generalizable robotic policies. | role, split, size and leakage | p. 7 (4.2. Results on Real-World Robotic Tasks), p. 6 (4. Experiments), p. 8 (4.3. Ablation Study), p. 8 (4.4. Generalization Analysis) |
| Metric | For evaluation, we conduct 20 rollouts per task and report success rates based on human evaluation. | definition, denominator, direction and uncertainty | p. 6 (4.1. Experiment Setup), p. 7 (4.1. Experiment Setup), p. 8 (4.3. Ablation Study) |
| Baseline/ablation | Figure 9. Out-of-box evaluation results of 7 tasks on Dual-Arm UR-5e. Out-of-Box Evaluation. In addition to the evaluation on the Dual-Arm Franka, we also conduct an out-of-box evaluation of XR-1 on the ... | fair input/data/compute/action matching | p. 24 (Figure/Table caption), p. 7 (4.2. Results on Real-World Robotic Tasks), p. 7 (4.2. Results on Real-World Robotic Tasks) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 5. Conclusion - extractive body cue:** We presented X Robotic Model 1 (XR-1), a unified framework for versatile and scalable vision-language-action learning that addresses the key limitations of existing approaches: precise ...
- **p. 9 / 4.5. Additional Analyses - extractive body cue:** Failure analyses for baselines and XR-1 are provided in Appendix I and Appendix J, respectively, showing that XR-1 reduces baseline failures such as optimization collapse, ...
- **p. 30 / Figure/Table caption - extractive body cue:** Figure 15. Visualizing UVMC across different embodiments (Dual-Arm Franka and Dual-Arm UR) using t-SNE. an intermediate feature supervision signal, UVMC guides the model to generate ...
- **p. 31 / Figure/Table caption - extractive body cue:** Figure 16. Failure cases of baseline methods. Miss Miss Drop XR-1 Precision Deficiency: TK2-CollectScrews
- **p. 31 / Figure/Table caption - extractive body cue:** Figure 17. Failure Cases of XR-1. • Deformable Object Handling: DFR-HangTowelRack. The robot performs a bimanual manipulation task involving deformable object handling: the right arm ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. We introduce X Robotic Model 1 (XR-1), a versatile and scalable vision-language-action framework. XR-1 supports robust multi-task learning across diverse robot embodiments and ...
- **p. 5 / 3.5. Data Collection and Implementation Details - extractive body cue:** We also provide a lightweight variant, XR-1-Light, built upon SwitchVLA (Li et al., 2025a), which uses Florence-2 (Xiao et al., 2024) to reduce computational cost ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 4 (3.1. Overview), p. 5 (3.1. Overview)이다.
