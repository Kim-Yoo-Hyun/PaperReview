# ORION: A Holistic End-to-End Autonomous Driving Framework by Vision-Language Instructed Action Generation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Fu_ORION_A_Holistic_End-to-End_Autonomous_Driving_Framework_by_Vision-Language_Instructed_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Fu_ORION_A_Holistic_End-to-End_Autonomous_Driving_Framework_by_Vision-Language_Instructed_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: Haoyu Fu, Diankun Zhang, Zongchuang Zhao, Jianfeng Cui, Dingkang Liang, Chong Zhang, Dingyuan Zhang, Hongwei Xie, Bing Wang, Xiang Bai
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Vision-Language Model
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Fu_ORION_A_Holistic_End-to-End_Autonomous_Driving_Framework_by_Vision-Language_Instructed_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Fu_ORION_A_Holistic_End-to-End_Autonomous_Driving_Framework_by_Vision-Language_Instructed_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: system
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/ICCV2025/papers/Fu_ORION_A_Holistic_End-to-End_Autonomous_Driving_Framework_by_Vision-Language_Instructed_ICCV_2025_paper.pdf)

## Why This Paper Is Here

ORION은 주행 장면에 관한 시각·언어 추론과 생성형 궤적 계획기를 결합해 같은 모델에서 질문에 답하고 차량의 미래 궤적을 예측한다. [PDF 1쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Fu_ORION_A_Holistic_End-to-End_Autonomous_Driving_Framework_by_Vision-Language_Instructed_ICCV_2025_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Fu_ORION_A_Holistic_End-to-End_Autonomous_Driving_Framework_by_Vision-Language_Instructed_ICCV_2025_paper.pdf#page=3)

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

- 시간에 걸친 시각 특징을 요약하고 언어 모델의 추론 표현을 생성형 계획기에 전달해 질의응답과 계획을 함께 최적화한다. [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Fu_ORION_A_Holistic_End-to-End_Autonomous_Driving_Framework_by_Vision-Language_Instructed_ICCV_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Fu_ORION_A_Holistic_End-to-End_Autonomous_Driving_Framework_by_Vision-Language_Instructed_ICCV_2025_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Fu_ORION_A_Holistic_End-to-End_Autonomous_Driving_Framework_by_Vision-Language_Instructed_ICCV_2025_paper.pdf#page=5)
- Bench2Drive에서 폐루프 주행 점수와 경로 완주 성공률을 별도 지표로 비교하고, 시간 특징과 계획기 구성의 기여를 분석했다. [PDF 6쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Fu_ORION_A_Holistic_End-to-End_Autonomous_Driving_Framework_by_Vision-Language_Instructed_ICCV_2025_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Fu_ORION_A_Holistic_End-to-End_Autonomous_Driving_Framework_by_Vision-Language_Instructed_ICCV_2025_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Fu_ORION_A_Holistic_End-to-End_Autonomous_Driving_Framework_by_Vision-Language_Instructed_ICCV_2025_paper.pdf#page=8)

## Evaluation Scope

Bench2Drive 폐루프에서 ORION이 기록한 77.74는 주행 점수이고 54.62%는 성공률이다. 표의 두 열은 같은 시뮬레이션에서 서로 다른 결과를 측정한다. [PDF 6쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Fu_ORION_A_Holistic_End-to-End_Autonomous_Driving_Framework_by_Vision-Language_Instructed_ICCV_2025_paper.pdf#page=6)

## Explicit Limitations and Failure Boundary

- **p. 5 / 4.1. Dataset and Evaluation Metrics - extractive body cue:** For open-loop evaluation, we use the L2 distance error and the collision rate.
- **p. 6 / 25.00 71.11 78.33 30.00 69.15 54.72(+16.12) - extractive body cue:** On the other hand, our model falls behind DriveAdapter in Merging and Give Way, which shows that ORION is not good at making lane-changing decisions.
- **p. 6 / 4.5. Ablation Study - extractive body cue:** The plain text paradigm performs the worst (42.23 DS, 13.14% SR, and 15.39% mean ability), indicating the limitations of plain text output in closed-loop driving ...
- **p. 8 / 4.5. Ablation Study - extractive body cue:** The model cannot obtain both reasoning and planning capabilities with single-task training.
- **p. 8 / 4.5. Ablation Study - extractive body cue:** Then, we combine the motion prediction module in the QT-Former's perception head, which gains a slight improvement of +0.4% SR and further reduces the collision ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (3.1. QT-Former), p. 4 (3.3. Generative Planner), p. 4 (3.1. QT-Former)이다.
