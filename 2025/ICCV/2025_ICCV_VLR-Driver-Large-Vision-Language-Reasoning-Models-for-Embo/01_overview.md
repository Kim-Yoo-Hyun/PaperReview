# VLR-Driver: Large Vision-Language-Reasoning Models for Embodied Autonomous Driving

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=0.9); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Kong_VLR-Driver_Large_Vision-Language-Reasoning_Models_for_Embodied_Autonomous_Driving_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Kong_VLR-Driver_Large_Vision-Language-Reasoning_Models_for_Embodied_Autonomous_Driving_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Vision-Language Model
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Kong_VLR-Driver_Large_Vision-Language-Reasoning_Models_for_Embodied_Autonomous_Driving_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Kong_VLR-Driver_Large_Vision-Language-Reasoning_Models_for_Embodied_Autonomous_Driving_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=0.9)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, existing CoT-based methods typically rely on openended language generation for reasoning, which lacks structural constraints.를 문제로 두고, Our method enables VLR model to describe the current driving scenario, construct real-time spatial layout and dynamic changes of the environment, and achieve long-term planning for driving decisions.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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
| Observation/input | The forward pass is computed as: y = W ′x =  W0 + α r B · A  x, (2) where y is the output and x is input. | RGB-D, image set, point cloud, depth와 camera pose | p. 6 (3.3. Training Paradigm), p. 4 (3.1. Overview) |
| State/latent | forward, pass, computed, where, output, input, Subsequently, compressed, cropped, image, data, information | geometry, map, object/relationship state | p. 6 (3.3. Training Paradigm), p. 4 (3.1. Overview), p. 4 (3.1. Overview) |
| Output/action | Subsequently, the compressed and cropped image data and the information from the ego's sensors are input into the model. | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.1. Overview), p. 4 (3.1. Overview), p. 2 (Body text (section not recovered)) |
| Objective/outcome | The core principle of GRPO [34] is to optimize strategies by assigning relative rewards to multiple outputs generated from the same prompt, thereby eliminating the need for additional value function models. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (3.3. Training Paradigm), p. 6 (3.3. Training Paradigm), p. 4 (3.2. Spatiotemporal CoT Reasoning) |

## Main Claims and Actual Contribution

- **p. 4 / 3.2.1. Perception Level CoT - extractive body cue:** Our method enables VLR model to describe the current driving scenario, construct real-time spatial layout and dynamic changes of the environment, and achieve long-term planning ...
- **p. 2 / Body text (section not recovered) - extractive body cue:** We introduce VLR-Driver, a visual-language-reasoning model developed for embodied AD.
- **p. 4 / 3. Method - extractive body cue:** We present the motivation and design details of our VLRDriver framework.
- **p. 5 / 3.2.1. Perception Level CoT - extractive body cue:** To address this limitation, we introduce consecutive frames I = {If, Ifr, Ifl, Ib, Ibl, Ibr}Tnow t=Tnow-T into the model, allowing it to track temporal ...
- **p. 5 / 3.2.1. Perception Level CoT - extractive body cue:** In this scenario, where some vehicles are illegally parked ahead and blocking the lane, our method can conduct hierarchical patiotemporal reasoning analysis and make a ...
- **p. 7 / 5.2. Metrics - extractive body cue:** We employ four core metrics to evaluate AD performance: driving score (DS), route completion (RC), infraction score (IS), and success rate (SR).
- **p. 8 / 5.3. Comparisons with Existing Methods - extractive body cue:** Our method achieved the best results in all abilities, thanks to the deep reflection and reasoning ability of our VLR model, which has stronger traffic ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. The comparison of core metrics and subdivision infraction scores with state-of-the-art E2E/VLM models on the Bench2Drive benchmark. C, L and T indicate camera, ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 7 (5.2. Metrics), p. 8 (5.3. Comparisons with Existing Methods) |
| Embodiment/environment | The dataset includes 20,000 sets of multi-frame, multi-angle image data collected from various road conditions such as urban, rural, and highways in the CARLA simulator, covering over 30 specific complex traffic scenarios ... | hardware/simulator version and reset protocol | p. 6 (4. VLR-Driver Dataset), p. 6 (4.1. Data Collection) |
| Dataset/benchmark | We conducted comprehensive experiments with the SOTA methods including E2E and VLM in the CARLA simulator across 44 routes from the Bench2Drive benchmark. | role, split, size and leakage | p. 6 (4. VLR-Driver Dataset), p. 6 (4.1. Data Collection), p. 8 (5.3. Comparisons with Existing Methods), p. 7 (5.1. Experimental Setup) |
| Metric | We employ four core metrics to evaluate AD performance: driving score (DS), route completion (RC), infraction score (IS), and success rate (SR). | definition, denominator, direction and uncertainty | p. 7 (5.2. Metrics), p. 7 (Figure/Table caption), p. 8 (5.2. Metrics) |
| Baseline/ablation | It can be seen that our method outperforms other methods in key metrics such as DS, RC, and SR, achieving first place and effectively improving DS by 17.5%, mean advanced driving ability ... | fair input/data/compute/action matching | p. 8 (5.3. Comparisons with Existing Methods), p. 7 (4.1. Data Collection), p. 7 (4.1. Data Collection) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.1. Data Collection - extractive body cue:** CP, CV, CL, RL, SS, OR, AB, YEV correspond to the Collision with a Pedestrian, Collision with another Vehicle, Collision with Layout, Red Light infractions, ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of VLR-Driver framework. We introduce VLR-Driver Dataset, an advanced visual-language-reasoning dataset designed for AD, featuring detailed annotations of scene descriptions, analytical reasoning, ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, existing CoT-based methods typically rely on openended language generation for reasoning, which lacks structural constraints.를 문제로 두고, Our method enables VLR model to describe the current driving scenario, construct real-time spatial layout and dynamic changes of the environment, and achieve long-term planning for driving decisions.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (Body text (section not recovered)), p. 2 (Body text (section not recovered)), p. 4 (3.2.1. Perception Level CoT), p. 4 (3.1. Overview), p. 6 (3.3. Training Paradigm), p. 6 (3.3. Training Paradigm) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
