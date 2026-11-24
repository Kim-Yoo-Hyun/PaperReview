# VLR-Driver: Large Vision-Language-Reasoning Models for Embodied Autonomous Driving

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=0.9); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Kong_VLR-Driver_Large_Vision-Language-Reasoning_Models_for_Embodied_Autonomous_Driving_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Kong_VLR-Driver_Large_Vision-Language-Reasoning_Models_for_Embodied_Autonomous_Driving_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: Fanjie Kong, Yitong Li, Weihuang Chen, Chen Min, Yizhe Li, Zhiqiang Gao, Haoyang Li, Zhongyu Guo, Hongbin Sun
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Vision-Language Model
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Kong_VLR-Driver_Large_Vision-Language-Reasoning_Models_for_Embodied_Autonomous_Driving_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Kong_VLR-Driver_Large_Vision-Language-Reasoning_Models_for_Embodied_Autonomous_Driving_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=0.9)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 원문 해당 쪽과 대조했다. [본문](https://openaccess.thecvf.com/content/ICCV2025/papers/Kong_VLR-Driver_Large_Vision-Language-Reasoning_Models_for_Embodied_Autonomous_Driving_ICCV_2025_paper.pdf)

> DOC-QA2 targeted source review: 2026-10-23; PDF pp. 4, 6. 손상 구간·직접 연결된 표 분류만 원문 이미지와 대조했다. 전체 주장 정독·실험 검증·reading status 승격을 뜻하지 않는다. [URL·PDF hash·수정 기록](../../../work/sources/pdf_note_review_followup_2026-10-23.json).

## Why This Paper Is Here

VLR-Driver는 도로 장면의 시공간 단서를 단계별로 해석한 뒤 그 판단을 주행 계획에 반영하는 시각·언어 모델이다. [PDF 1쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Kong_VLR-Driver_Large_Vision-Language-Reasoning_Models_for_Embodied_Autonomous_Driving_ICCV_2025_paper.pdf#page=1) · [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Kong_VLR-Driver_Large_Vision-Language-Reasoning_Models_for_Embodied_Autonomous_Driving_ICCV_2025_paper.pdf#page=3)

## Problem and Motivation

- **p. 1 / Body text (section not recovered) - extractive body cue:** This ICCV paper is the Open Access version, provided by the Computer Vision Foundation.
- **p. 1 / Body text (section not recovered) - extractive body cue:** Except for this watermark, it is identical to the accepted version; the final published version of the proceedings is available on IEEE Xplore.
- **p. 2 / Body text (section not recovered) - extractive body cue:** However, the decision-making process of VLMs often functions as a "black box", making it challenging to trace and interpret their underlying logic.
- **p. 2 / Body text (section not recovered) - extractive body cue:** This makes it difficult for AD systems to be fully trusted by drivers when encountering complex and emergency situations, such as illegal roadside parking, navigating ...
- **p. 2 / Body text (section not recovered) - extractive body cue:** Moreover, most VLMs are trained on internet data, lacking spatial understanding and specialized training in the field of AD, making it difficult for them to ...
- **p. 2 / Body text (section not recovered) - extractive body cue:** However, existing CoT-based methods typically rely on openended language generation for reasoning, which lacks structural constraints.
- **p. 4 / 3.2.1. Perception Level CoT - extractive body cue:** A critical aspect of safe driving is identifying potential risk points within the current lane.

## Core Idea

- **p. 4 / 3.2.1. Perception Level CoT - extractive body cue:** Our method enables VLR model to describe the current driving scenario, construct real-time spatial layout and dynamic changes of the environment, and achieve long-term planning ...
- **p. 2 / Body text (section not recovered) - extractive body cue:** We introduce VLR-Driver, a visual-language-reasoning model developed for embodied AD.
- **p. 4 / 3. Method - extractive body cue:** We present the motivation and design details of our VLRDriver framework.
- **p. 5 / 3.2.1. Perception Level CoT - extractive body cue:** To address this limitation, we introduce consecutive frames I = {If, Ifr, Ifl, Ib, Ibl, Ibr}Tnow t=Tnow-T into the model, allowing it to track temporal ...
- **p. 5 / 3.2.1. Perception Level CoT - extractive body cue:** In this scenario, where some vehicles are illegally parked ahead and blocking the lane, our method can conduct hierarchical patiotemporal reasoning analysis and make a ...
- **p. 6 / 3.3. Training Paradigm - extractive body cue:** Specifically, we first generate multiple candidate decision answers for the current driving scenario using prompts within the VLR model; Then, following our ST-CoT strategy, the ...
- **p. 6 / 3.3. Training Paradigm - extractive body cue:** We use LoRA for all linear modules, which not only saves computation but also ensures the performance of the model.
- **p. 4 / 3. Method - extractive body cue:** Initially, we introduce the design concept of the VLR model, which builds upon enhancements to the VLA model (Sec.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 과거 N_f frames × N_v views의 image와 ego 위치·속도·target point | Driving visual history 및 ego-state input | PDF p. 4 §3.1; p. 6 Eq. (2)는 LoRA 연산으로 sensor 정의가 아님 |
| State/latent | forward, pass, computed, where, output, input, Subsequently, compressed, cropped, image, data, information | geometry, map, object/relationship state | p. 6 (3.3. Training Paradigm), p. 4 (3.1. Overview), p. 4 (3.1. Overview) |
| Output/action | Subsequently, the compressed and cropped image data and the information from the ego's sensors are input into the model. | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.1. Overview), p. 4 (3.1. Overview), p. 2 (Body text (section not recovered)) |
| Objective/outcome | The core principle of GRPO [34] is to optimize strategies by assigning relative rewards to multiple outputs generated from the same prompt, thereby eliminating the need for additional value function models. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (3.3. Training Paradigm), p. 6 (3.3. Training Paradigm), p. 4 (3.2. Spatiotemporal CoT Reasoning) |

## Main Claims and Actual Contribution

- 장면 묘사와 시간에 따른 위험 판단을 주행 의사결정에 연결하는 추론 절차를 설계하고, 이를 학습할 다중 모달 추론·결정 자료를 구축했다. [PDF 3쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Kong_VLR-Driver_Large_Vision-Language-Reasoning_Models_for_Embodied_Autonomous_Driving_ICCV_2025_paper.pdf#page=3) · [PDF 4쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Kong_VLR-Driver_Large_Vision-Language-Reasoning_Models_for_Embodied_Autonomous_Driving_ICCV_2025_paper.pdf#page=4) · [PDF 5쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Kong_VLR-Driver_Large_Vision-Language-Reasoning_Models_for_Embodied_Autonomous_Driving_ICCV_2025_paper.pdf#page=5) · [PDF 6쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Kong_VLR-Driver_Large_Vision-Language-Reasoning_Models_for_Embodied_Autonomous_Driving_ICCV_2025_paper.pdf#page=6)
- CARLA의 Bench2Drive 폐루프에서 주행 점수, 경로 완주, 위반, 성공률을 측정하고 추론 구성에 따른 변화를 비교했다. [PDF 6쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Kong_VLR-Driver_Large_Vision-Language-Reasoning_Models_for_Embodied_Autonomous_Driving_ICCV_2025_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Kong_VLR-Driver_Large_Vision-Language-Reasoning_Models_for_Embodied_Autonomous_Driving_ICCV_2025_paper.pdf#page=7) · [PDF 8쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Kong_VLR-Driver_Large_Vision-Language-Reasoning_Models_for_Embodied_Autonomous_Driving_ICCV_2025_paper.pdf#page=8)

## Evaluation Scope

CARLA 기반 Bench2Drive 표 1에서 VLR-Driver의 주행 점수는 75.01, 경로 완주 지표는 86.09, 성공률은 50.00%다. 각 수치는 카메라와 텍스트를 쓰는 동일 행의 서로 다른 열이다. [PDF 6쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Kong_VLR-Driver_Large_Vision-Language-Reasoning_Models_for_Embodied_Autonomous_Driving_ICCV_2025_paper.pdf#page=6) · [PDF 7쪽](https://openaccess.thecvf.com/content/ICCV2025/papers/Kong_VLR-Driver_Large_Vision-Language-Reasoning_Models_for_Embodied_Autonomous_Driving_ICCV_2025_paper.pdf#page=7)

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.1. Data Collection - extractive body cue:** CP, CV, CL, RL, SS, OR, AB, YEV correspond to the Collision with a Pedestrian, Collision with another Vehicle, Collision with Layout, Red Light infractions, ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of VLR-Driver framework. We introduce VLR-Driver Dataset, an advanced visual-language-reasoning dataset designed for AD, featuring detailed annotations of scene descriptions, analytical reasoning, ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (Body text (section not recovered)), p. 4 (3.2.1. Perception Level CoT), p. 4 (3.1. Overview), p. 6 (3.3. Training Paradigm)이다.
