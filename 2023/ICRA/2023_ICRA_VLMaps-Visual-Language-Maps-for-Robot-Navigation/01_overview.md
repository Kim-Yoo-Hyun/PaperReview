# VLMaps: Visual-Language Maps for Robot Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2210.05714.
> PDF retrieval source: https://arxiv.org/pdf/2210.05714. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: Vision-Language Navigation, semantic map, Robotics
- Official paper: https://arxiv.org/abs/2210.05714
- Full-text retrieval: https://arxiv.org/pdf/2210.05714
- Code/Project: https://vlmaps.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 A key aspect of VLMaps is that they are spatial, which enables them to: • Localize spatial goals beyond object-centric ones, e.g., "in between the TV and sofa" or "to the right ...를 문제로 두고, We propose VLMaps as one such representation, which can be constructed using off-the-shelf visual-language models (VLMs) and standard 3D reconstruction libraries.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Grounding language to the visual observations of a navigating agent can be performed using off-the-shelf visuallanguage models pretrained on Internet-scale data (e.g., image captions).
- **p. 1 / Abstract - extractive body cue:** While this is useful for matching images to natural language descriptions of object goals, it remains disjoint from the process of mapping the environment, so ...
- **p. 1 / Abstract - extractive body cue:** To address this problem, we propose VLMaps, a spatial map representation that directly fuses pretrained visual-language features with a 3D reconstruction of the physical world.
- **p. 1 / Abstract - extractive body cue:** VLMaps can be autonomously built from video feed on robots using standard exploration approaches and enables natural language indexing of the map without additional labeled ...
- **p. 1 / Abstract - extractive body cue:** Specifically, when combined with large language models (LLMs), VLMaps can be used to (i) translate natural language commands into a sequence of open-vocabulary navigation goals ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** A key aspect of VLMaps is that they are spatial, which enables them to: • Localize spatial goals beyond object-centric ones, e.g., "in between the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** VLMaps with different language models as well as a discussion on limitations, which point to areas for future work.

## Core Idea

- **p. 2 / III. METHOD - extractive body cue:** We propose VLMaps as one such representation, which can be constructed using off-the-shelf visual-language models (VLMs) and standard 3D reconstruction libraries.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Extensive experiments show that using VLMaps enables more effective long-horizon multi-object goal navigation than baseline alternatives, e.g., CoW [12] and LM-Nav [13], and, in particular, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** A key aspect of VLMaps is that they are spatial, which enables them to: • Localize spatial goals beyond object-centric ones, e.g., "in between the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** 2: VLMaps enables a robot to perform complex zero-shot spatial goal navigation tasks given natural language commands, without additional data collection or model finetuning.
- **p. 3 / III. METHOD - extractive body cue:** Generating Open-Vocabulary Obstacle Maps Building a VLMap enables us to generate obstacle maps that inherit the open-vocabulary nature of the VLMs used (LSeg and CLIP).
- **p. 4 / III. METHOD - extractive body cue:** Zero-Shot Spatial Goal Navigation from Language In this section, we describe our approach to long-horizon (spatial) goal navigation, given a set of landmark descriptions specified ...
- **p. 4 / III. METHOD - extractive body cue:** The robot code can express functions or logic structures (if-then-else statements or for/while loops) and parameterize API calls (e.g., robot.move_to(target_name) or robot.turn(degrees).
- **p. 2 / III. METHOD - extractive body cue:** The LSeg visual encoder maps an image such that the embedding of each pixel lies in the CLIP feature space.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Zero-Shot Spatial Goal Navigation from Language In this section, we describe our approach to long-horizon (spatial) goal navigation, given a set of landmark descriptions specified by natural language instructions such as move ... | camera/depth stream, pose, map와 language goal | p. 4 (III. METHOD), p. 3 (III. METHOD) |
| State/latent | Zero-Shot, Spatial, Goal, Navigation, Language, section, describe, long-horizon, given, landmark, descriptions, specified | robot pose, free-space/semantic map와 local goal | p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Output/action | Open-Vocabulary Label Set ( entries) VLMap Creation LSeg Visual Encoder (Frozen) Input Depth Camera Pose Global Point Cloud Input Image Each Point Top-down Projection VLMap Per-Pixel Embedding Pixel-Text Similarity Argmax Segmentation M ... | collision-free trajectory 또는 velocity command | p. 3 (III. METHOD), p. 4 (III. METHOD), p. 1 (I. INTRODUCTION) |
| Objective/outcome | goal reach, safety, localization error와 replanning latency | goal reach, safety, localization error와 replanning latency | 본문 anchor 없음 |

## Main Claims and Actual Contribution

- **p. 2 / III. METHOD - extractive body cue:** We propose VLMaps as one such representation, which can be constructed using off-the-shelf visual-language models (VLMs) and standard 3D reconstruction libraries.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Extensive experiments show that using VLMaps enables more effective long-horizon multi-object goal navigation than baseline alternatives, e.g., CoW [12] and LM-Nav [13], and, in particular, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** A key aspect of VLMaps is that they are spatial, which enables them to: • Localize spatial goals beyond object-centric ones, e.g., "in between the ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** 2: VLMaps enables a robot to perform complex zero-shot spatial goal navigation tasks given natural language commands, without additional data collection or model finetuning.
- **p. 3 / III. METHOD - extractive body cue:** Generating Open-Vocabulary Obstacle Maps Building a VLMap enables us to generate obstacle maps that inherit the open-vocabulary nature of the VLMs used (LSeg and CLIP).
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Subgoals in a Row 1 2 3 4 LM-Nav [13] 5 5 0 0 CoW [12] 33 5 0 0 CLIP Map 19 0 0 ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** This improves object navigation efficiency (Success [%] weighted by Path Length, SPL).
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Overall, these results demonstrate the ability of VLMaps to index landmarks with natural language in the real world and, more importantly, its applicability to achieve ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Embodiment/environment | We use the Habitat simulator [45] with the Matterport3D dataset [46] for the evaluation of multi-object and spatial goal navigation tasks. | hardware/simulator version and reset protocol | p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Dataset/benchmark | Our benchmark consists of 21 trajectories in seven scenes, with manually specified corresponding language instructions for evaluation. | role, split, size and leakage | p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Metric | In contrast, while achieving similar success rate compared to the drone with a ground map, the drone with a drone map manages to navigate with higher path efficiency, reflected by the increased ... | definition, denominator, direction and uncertainty | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Baseline/ablation | Our method outperforms other baselines in this task. | fair input/data/compute/action matching | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We observe that failure cases are caused by: 1) inaccurate depth, which introduces noise during the map creation and decreases the landmark indexing accuracy and ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: VLMaps enables a robot to perform complex zero-shot spatial goal navigation tasks given natural language commands, without additional data collection or model finetuning. ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** This is because when the drone does not have access to a customized obstacle map, it fails to benefit from flying over ground objects to ...

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 A key aspect of VLMaps is that they are spatial, which enables them to: • Localize spatial goals beyond object-centric ones, e.g., "in between the TV and sofa" or "to the right ...를 문제로 두고, We propose VLMaps as one such representation, which can be constructed using off-the-shelf visual-language models (VLMs) and standard 3D reconstruction libraries.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 4 (III. METHOD), p. 2 (III. METHOD), p. 4 (III. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (11 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** A key aspect of VLMaps is that they are spatial, which enables them to: • Localize spatial goals beyond object-centric ones, e.g., "in between the TV and sofa" or "to ... (p. 1, I. INTRODUCTION).
- **Actual contribution:** Extensive experiments show that using VLMaps enables more effective long-horizon multi-object goal navigation than baseline alternatives, e.g., CoW [12] and LM-Nav [13], and, in particular, excels at enabling spatial open-vocabulary ... (p. 1, I. INTRODUCTION).
- **Evaluation boundary:** Subgoals in a Row 1 2 3 4 LM-Nav [13] 5 5 0 0 CoW [12] 33 5 0 0 CLIP Map 19 0 0 0 VLMaps (ours) 62 33 ... (p. 5, IV. EXPERIMENTS).
- **Explicit failure boundary:** We observe that failure cases are caused by: 1) inaccurate depth, which introduces noise during the map creation and decreases the landmark indexing accuracy and 2) action noise, which can ... (p. 6, IV. EXPERIMENTS).
