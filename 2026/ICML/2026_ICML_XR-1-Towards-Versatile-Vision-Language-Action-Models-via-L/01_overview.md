# XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (45 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=JO0IsGJg16.
> PDF retrieval source: https://openreview.net/pdf/181715f87df4dd5677ebf2619dcb456e071c95dd.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Imitation Learning
- Official paper: https://openreview.net/forum?id=JO0IsGJg16
- Full-text retrieval: https://openreview.net/pdf/181715f87df4dd5677ebf2619dcb456e071c95dd.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (45 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Despite VLM advancements, two challenges persist: (i) Precision Gap: Mapping high-dimensional observations to precise low-level actions is difficult due to multimodal uncertainty; even centimeter-level errors lead to failure in dexterou ...를 문제로 두고, Our main contributions are summarized as follows: • We propose X Robotic Model 1 (XR-1), a scalable three-stage framework for VLA learning that effectively leverages heterogeneous data sources, including Internet-scale human videos ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are summarized as follows: • We propose X Robotic Model 1 (XR-1), a scalable three-stage framework for VLA learning that effectively leverages ...
- **p. 2 / 1. Introduction - extractive body cue:** Addressing the limitations of unimodal representations and inspired by human supramodal cognition, we propose X Robotic Model 1 (XR-1) to achieve cross-data exploitation and cross-embodiment ...
- **p. 4 / 3.1. Overview - extractive body cue:** We introduce XR-1, a scalable framework for cross-robot VLA learning (Figure 2), structured in three stages.
- **p. 5 / 3.1. Overview - extractive body cue:** To unify both modalities, we introduce a VQ-VAE codebook e ∈Rd×f with d discrete entries of dimension f.
- **p. 5 / 3.1. Overview - extractive body cue:** To mitigate this gap, we introduce an alignment loss that constrains visual codes to remain consistent with their motion counterparts: Lalign = DKL(q(ze mo) ∥q(ze ...
- **p. 8 / 4.4. Generalization Analysis - extractive body cue:** As shown in Figure 7, XR-1 achieves significantly higher success rates than ACT and DP, despite the setting favoring 8
- **p. 8 / 4.4. Generalization Analysis - extractive body cue:** As shown in Figure 6, the pre-trained XR-1-oob model, despite no adaptation, achieves performance comparable to GR00T-N1.5 and π0, while outperforming RDT and UniVLA.
- **p. 7 / 4.1. Experiment Setup - extractive body cue:** Success rate results across 20 tasks on Tien Kung 2.0.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 Despite VLM advancements, two challenges persist: (i) Precision Gap: Mapping high-dimensional observations to precise low-level actions is difficult due to multimodal uncertainty; even centimeter-level errors lead to failure in dexterou ...를 문제로 두고, Our main contributions are summarized as follows: • We propose X Robotic Model 1 (XR-1), a scalable three-stage framework for VLA learning that effectively leverages heterogeneous data sources, including Internet-scale human videos ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. Overview), p. 4 (3.1. Overview), p. 5 (3.1. Overview), p. 5 (3.1. Overview) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
