# Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhu_Move_to_Understand_a_3D_Scene_Bridging_Visual_Grounding_and_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhu_Move_to_Understand_a_3D_Scene_Bridging_Visual_Grounding_and_ICCV_2025_paper.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: Navigation, grounding, exploration
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Zhu_Move_to_Understand_a_3D_Scene_Bridging_Visual_Grounding_and_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhu_Move_to_Understand_a_3D_Scene_Bridging_Visual_Grounding_and_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Our approach bridges online exploration with dynamically spatial memory updates for lifelong grounding. ries presents significant challenges, and methods for effectively leveraging such data remain an open problem.를 문제로 두고, Our main contributions can be summarized as follows: • We present MTU3D, bridging visual grounding and exploration for efficient and versatile embodied navigation. • We propose a unified objective that jointly optimizes ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Embodied scene understanding requires not only comprehending visual-spatial information that has been observed but also determining where to explore next in the 3D physical world.
- **p. 1 / Abstract - extractive body cue:** Existing 3D Vision-Language (3D-VL) models primarily focus on grounding objects in static observations from 3D reconstruction, such as meshes and point clouds, but lack the ...
- **p. 1 / Abstract - extractive body cue:** To address this limitation, we introduce Move to Understand (MTU3D), a unified framework that integrates active perception with 3D vision-language learning, enabling embodied agents to ...
- **p. 1 / Abstract - extractive body cue:** This is achieved by three key innovations: 1) Online query-based representation learning, enabling direct spatial memory construction from RGB-D frames, eliminating the need for explicit ...
- **p. 1 / Abstract - extractive body cue:** 2) A unified objective for grounding and exploring, which represents unexplored locations as frontier queries and jointly optimizes object grounding and frontier selection.
- **p. 2 / 1. Introduction - extractive body cue:** Our approach bridges online exploration with dynamically spatial memory updates for lifelong grounding. ries presents significant challenges, and methods for effectively leveraging such data remain ...
- **p. 2 / 1. Introduction - extractive body cue:** In contrast, reinforcement learning (RL)-based embodied agents can explore environments but often struggle with sample inefficiency [71], poor generalization due to limited training data [20, ...

## Core Idea

- **p. 3 / Method - extractive body cue:** Our main contributions can be summarized as follows: • We present MTU3D, bridging visual grounding and exploration for efficient and versatile embodied navigation. • We ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we propose Move to Understand (MTU3D), a unified framework that bridges visual grounding and exploration for versatile embodied navigation as shown ...
- **p. 2 / 1. Introduction - extractive body cue:** Our approach introduces three key innovations:
- **p. 3 / Method - extractive body cue:** When combined with a large vision-language model, serving as its trajectory generator, our approach improves the embodied question answering for LM-SR by 2.4% and LLM-SPL ...
- **p. 5 / 3.4. Vision-Language-Exploration Training - extractive body cue:** The unified decision scores SU t are optimized with binary cross-entropy loss, teaching the model to assign higher scores to appropriate query locations based on ...
- **p. 5 / 3.4. Vision-Language-Exploration Training - extractive body cue:** We utilize RGBD trajectories from ScanNet and HM3D to train query representation with instance segmentation loss.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | (a) 3D-VL Model (b) End-to-End RL (c) MTU3D (Ours) Full RGB-D Video Time World Visual Grounding Model Explicit Mesh Open loop Single RGB-D image World State Action Model Closed loop Implicit state ... | camera/depth stream, pose, map와 language goal | p. 2 (1. Introduction), p. 3 (Method) |
| State/latent | D-VL, Model, End-to-End, MTU3D, Ours, Full, RGB-D, Video, Time, World, Visual, Grounding | robot pose, free-space/semantic map와 local goal | p. 2 (1. Introduction), p. 3 (Method), p. 5 (3.4. Vision-Language-Exploration Training) |
| Output/action | Specifically, MTU3D improves the state-of-the-art results by 13.7%, 23.0%, and 9.1% in SR, and 2.4%, 13.0%, and 6.3% in SPL on HM3D-OVON [79], GOAT-Bench [37], and SG3D [87], respectively. | collision-free trajectory 또는 velocity command | p. 3 (Method), p. 5 (3.4. Vision-Language-Exploration Training), p. 3 (Method) |
| Objective/outcome | The unified decision scores SU t are optimized with binary cross-entropy loss, teaching the model to assign higher scores to appropriate query locations based on the current state and goal. | goal reach, safety, localization error와 replanning latency | p. 5 (3.4. Vision-Language-Exploration Training), p. 3 (Method), p. 5 (3.4. Vision-Language-Exploration Training) |

## Main Claims and Actual Contribution

- **p. 3 / Method - extractive body cue:** Our main contributions can be summarized as follows: • We present MTU3D, bridging visual grounding and exploration for efficient and versatile embodied navigation. • We ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we propose Move to Understand (MTU3D), a unified framework that bridges visual grounding and exploration for versatile embodied navigation as shown ...
- **p. 2 / 1. Introduction - extractive body cue:** Our approach introduces three key innovations:
- **p. 3 / Method - extractive body cue:** When combined with a large vision-language model, serving as its trajectory generator, our approach improves the embodied question answering for LM-SR by 2.4% and LLM-SPL ...
- **p. 6 / 4.2. Quantitative Results - extractive body cue:** While MTU3D significantly outperforms Embodied Video Agent [21] and SenseAct-NN Monolithic [37, 87], overall success rates remain lower than in GOAT-Bench and HM3D-OVON, highlighting SG3D's ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 4. Sequential task navigation results on SG3D-Nav [87]. Multi-modal Lifelong Navigation. The results in Tab. 5 highlight the significant performance improvement of our MTU3D ...
- **p. 7 / 4.3. Discussions - extractive body cue:** 4a show that VisionLanguage Exploration (VLE) Pre-training significantly improves navigation performance, as indicated by the SR across all datasets.
- **p. 7 / 4.3. Discussions - extractive body cue:** 4b show that memory significantly improves SR across all goal types.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (4.2. Quantitative Results), p. 6 (Figure/Table caption) |
| Embodiment/environment | Unlike other benchmarks, SG3D emphasizes task consistency across multiple steps, making it more complex. | hardware/simulator version and reset protocol | p. 6 (4.2. Quantitative Results), p. 6 (4.2. Quantitative Results) |
| Dataset/benchmark | Model speed and parameter metrics, results are average from 5 runs across multiple frames and episodes on 3090 Ti. | role, split, size and leakage | p. 6 (4.2. Quantitative Results), p. 6 (4.2. Quantitative Results), p. 7 (4.3. Discussions), p. 7 (4.3. Discussions) |
| Metric | While MTU3D significantly outperforms Embodied Video Agent [21] and SenseAct-NN Monolithic [37, 87], overall success rates remain lower than in GOAT-Bench and HM3D-OVON, highlighting SG3D's inherent difficulty in requiring both navigati ... | definition, denominator, direction and uncertainty | p. 6 (4.2. Quantitative Results), p. 6 (4.1. Experimental setting), p. 7 (4.2. Quantitative Results) |
| Baseline/ablation | 3 demonstrate that our proposed MTU3D significantly outperforms all baselines in terms of SR across both Val Seen and Val Unseen settings. | fair input/data/compute/action matching | p. 6 (4.2. Quantitative Results), p. 7 (4.2. Quantitative Results), p. 6 (4.2. Quantitative Results) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4.3. Discussions - extractive body cue:** Does Vision-Langauge-Exploration Pe-training benefit navigation?
- **p. 7 / 4.3. Discussions - extractive body cue:** 4a show that VisionLanguage Exploration (VLE) Pre-training significantly improves navigation performance, as indicated by the SR across all datasets.
- **p. 7 / 4.3. Discussions - extractive body cue:** Specifically, SR increases from 27.8% to 33.3% in OVON, 22.2% to 36.1% in GOAT, and 22.9% to 27.9% in SG3D, demonstrating a consistent benefit of ...

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Our approach bridges online exploration with dynamically spatial memory updates for lifelong grounding. ries presents significant challenges, and methods for effectively leveraging such data remain an open problem.를 문제로 두고, Our main contributions can be summarized as follows: • We present MTU3D, bridging visual grounding and exploration for efficient and versatile embodied navigation. • We propose a unified objective that jointly optimizes ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (Method), p. 3 (Method), p. 5 (3.4. Vision-Language-Exploration Training), p. 5 (3.4. Vision-Language-Exploration Training) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
