# ORION: A Holistic End-to-End Autonomous Driving Framework by Vision-Language Instructed Action Generation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Fu_ORION_A_Holistic_End-to-End_Autonomous_Driving_Framework_by_Vision-Language_Instructed_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Fu_ORION_A_Holistic_End-to-End_Autonomous_Driving_Framework_by_Vision-Language_Instructed_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Vision-Language Model
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Fu_ORION_A_Holistic_End-to-End_Autonomous_Driving_Framework_by_Vision-Language_Instructed_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Fu_ORION_A_Holistic_End-to-End_Autonomous_Driving_Framework_by_Vision-Language_Instructed_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: system
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Besides, limited by the intrinsic autoregressive mechanism of VLMs, the trajectories these method output lack diversity [54], which is inconsistent with the natural uncertainty of human planning [9].를 문제로 두고, To tackle this problem, we propose a hOlistic E2E autonomous dRiving framework by vIsion-language instructed actiON generation, termed ORION.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** End-to-end (E2E) autonomous driving methods still struggle to make correct decisions in interactive closed-loop evaluation due to limited causal reasoning capability.
- **p. 1 / Abstract - extractive body cue:** Current methods attempt to leverage the powerful understanding and reasoning abilities of Vision-Language Models (VLMs) to resolve this dilemma.
- **p. 1 / Abstract - extractive body cue:** However, the problem is still open that few VLMs for E2E methods perform well in the closed-loop evaluation due to the gap between the semantic ...
- **p. 1 / Abstract - extractive body cue:** To tackle this issue, we propose ORION, a hOlistic E2E autonomous dRiving framework by vIsion-language instructed actiON generation.
- **p. 1 / Abstract - extractive body cue:** ORION uniquely combines a QT-Former to aggregate long-term history context, a Large Language Model (LLM) for driving scenario reasoning, and a generative planner for precision ...
- **p. 2 / 1. Introduction - extractive body cue:** Besides, limited by the intrinsic autoregressive mechanism of VLMs, the trajectories these method output lack diversity [54], which is inconsistent with the natural uncertainty of ...
- **p. 1 / 1. Introduction - extractive body cue:** Nevertheless, these methods lack the common sense to complete complex causal reasoning.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To tackle this problem, we propose a hOlistic E2E autonomous dRiving framework by vIsion-language instructed actiON generation, termed ORION.
- **p. 2 / 1. Introduction - extractive body cue:** Instead, motivated by OmniDrive [61], which extracts features through Q-Former-styled architecture, we introduce QT-Former, a query-based temporal module.
- **p. 3 / 3.1. QT-Former - extractive body cue:** To compress and extract multi-view image features Fm derived from the vision encoder while achieving long-term information modeling, we introduce QT-Former, a querybased temporal module, ...
- **p. 4 / 3.3. Generative Planner - extractive body cue:** Inspired by the generative domain, we introduce a generative planner to bridge the gap between the reasoning and action space.
- **p. 4 / 3.2. Large Language Model - extractive body cue:** The LLM is pivotal to our framework because the highquality reasoning of the current driving scenario is necessary to instruct the generator to generate a ...
- **p. 4 / 3.3. Generative Planner - extractive body cue:** As there are essential differences in the distribution between the reasoning space of VLM and the action space of trajectory, we use the VAE [29] ...
- **p. 4 / 3.1. QT-Former - extractive body cue:** Then they interact with image features Fm with 3D positional encoding [38] Pm in the cross-attention (CA) module.
- **p. 5 / 3.3. Generative Planner - extractive body cue:** (5) We then use the GRU decoder in GenAD [72] to decode the trajectory from the latent space z.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 2, the user instruction Xq, including scene description, history information review, scene analysis, and action reasoning, is first encoded into language tokens xq ∈RL×C by the text tokenizer, where L is the ... | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3.2. Large Language Model), p. 5 (3.3. Generative Planner) |
| State/latent | user, instruction, including, scene, description, history, information, review, analysis, action, reasoning, first | geometry, map, object/relationship state | p. 4 (3.2. Large Language Model), p. 5 (3.3. Generative Planner), p. 2 (1. Introduction) |
| Output/action | The former only uses a single token encoded in the reasoning space from the perspective of the ego vehicle as input, aiming to bridge the gap between reasoning space and action space. | point map, pose, scene graph, affordance 또는 query result | p. 5 (3.3. Generative Planner), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective/outcome | The total loss of QTFormer is: Lqt = Ldet + Ltra + Lm. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.4. Training Objectives), p. 5 (3.4. Training Objectives), p. 4 (3.3. Generative Planner) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To tackle this problem, we propose a hOlistic E2E autonomous dRiving framework by vIsion-language instructed actiON generation, termed ORION.
- **p. 2 / 1. Introduction - extractive body cue:** Instead, motivated by OmniDrive [61], which extracts features through Q-Former-styled architecture, we introduce QT-Former, a query-based temporal module.
- **p. 3 / 3.1. QT-Former - extractive body cue:** To compress and extract multi-view image features Fm derived from the vision encoder while achieving long-term information modeling, we introduce QT-Former, a querybased temporal module, ...
- **p. 4 / 3.3. Generative Planner - extractive body cue:** Inspired by the generative domain, we introduce a generative planner to bridge the gap between the reasoning and action space.
- **p. 4 / 3.2. Large Language Model - extractive body cue:** The LLM is pivotal to our framework because the highquality reasoning of the current driving scenario is necessary to instruct the generator to generate a ...
- **p. 7 / 4.5. Ablation Study - extractive body cue:** By leveraging explicit traffic state supervision (ID-2), ORION achieves 74.65 DS and 49.31% SR, which already outperforms DriveAdapter [22] and DriveTRansformer [25] by a large ...
- **p. 6 / 25.00 71.11 78.33 30.00 69.15 54.72(+16.12) - extractive body cue:** ORION achieves +16.12% and +12.64% performance improvements compared with DriveTransformer [25] and DriveAdapter [22] in the average ability, respectively.
- **p. 6 / 25.00 71.11 78.33 30.00 69.15 54.72(+16.12) - extractive body cue:** achieves improvements of +13.52 DS and +21.54% SR over DriveAdapter [22], even if DriveAdapter distills the expert feature from Think2Drive [30] and accepts two modalities ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (4.5. Ablation Study), p. 6 (25.00 71.11 78.33 30.00 69.15 54.72(+16.12)) |
| Embodiment/environment | Additionally, we compare our method with other baselines on nuScenes [7] open-loop evaluation (details in Appendix). | hardware/simulator version and reset protocol | p. 5 (4.1. Dataset and Evaluation Metrics), p. 5 (4.1. Dataset and Evaluation Metrics) |
| Dataset/benchmark | The slight degradation on DS may be caused by the trade-off between DS and SR in the CARLA benchmark protocol [74]. | role, split, size and leakage | p. 5 (4.1. Dataset and Evaluation Metrics), p. 5 (4.1. Dataset and Evaluation Metrics), p. 8 (4.5. Ablation Study), p. 8 (4.5. Ablation Study) |
| Metric | Bench2drive includes five metrics for closed-loop evaluation: Driving Score (DS), Success Rate (SR), Efficiency, Comfortness, and Multi-Ability. | definition, denominator, direction and uncertainty | p. 5 (4.1. Dataset and Evaluation Metrics), p. 6 (4.3. Main Results), p. 7 (4.5. Ablation Study) |
| Baseline/ablation | By leveraging explicit traffic state supervision (ID-2), ORION achieves 74.65 DS and 49.31% SR, which already outperforms DriveAdapter [22] and DriveTRansformer [25] by a large margin and makes an improvement of +18.32 ... | fair input/data/compute/action matching | p. 7 (4.5. Ablation Study), p. 5 (4.1. Dataset and Evaluation Metrics), p. 5 (4.1. Dataset and Evaluation Metrics) |

## Explicit Limitations and Failure Boundary

- **p. 5 / 4.1. Dataset and Evaluation Metrics - extractive body cue:** For open-loop evaluation, we use the L2 distance error and the collision rate.
- **p. 6 / 25.00 71.11 78.33 30.00 69.15 54.72(+16.12) - extractive body cue:** On the other hand, our model falls behind DriveAdapter in Merging and Give Way, which shows that ORION is not good at making lane-changing decisions.
- **p. 6 / 4.5. Ablation Study - extractive body cue:** The plain text paradigm performs the worst (42.23 DS, 13.14% SR, and 15.39% mean ability), indicating the limitations of plain text output in closed-loop driving ...
- **p. 8 / 4.5. Ablation Study - extractive body cue:** The model cannot obtain both reasoning and planning capabilities with single-task training.
- **p. 8 / 4.5. Ablation Study - extractive body cue:** Then, we combine the motion prediction module in the QT-Former's perception head, which gains a slight improvement of +0.4% SR and further reduces the collision ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Besides, limited by the intrinsic autoregressive mechanism of VLMs, the trajectories these method output lack diversity [54], which is inconsistent with the natural uncertainty of human planning [9].를 문제로 두고, To tackle this problem, we propose a hOlistic E2E autonomous dRiving framework by vIsion-language instructed actiON generation, termed ORION.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. QT-Former), p. 4 (3.3. Generative Planner), p. 4 (3.1. QT-Former) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
