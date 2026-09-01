# Dynamic Open-Vocabulary 3D Scene Graphs for Long-term Language-Guided Mobile Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2410.11989.
> PDF retrieval source: https://arxiv.org/pdf/2410.11989. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / RA-L
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: Robotics, 3D Vision, Graph Reasoning, semantic
- Official paper: https://arxiv.org/abs/2410.11989
- Full-text retrieval: https://arxiv.org/pdf/2410.11989
- Code/Project: https://github.com/BJHYZJ/DovSG
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 This limitation restricts their applicability in real-world scenarios where adaptability is crucial.를 문제로 두고, Our contributions are as follows: • We propose a novel robotic framework that integrates dynamic open-vocabulary 3D scene graphs with languageguided task planning, enabling accurate long-term task execution in dynamic and interactive ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Enabling mobile robots to perform long-term tasks in dynamic real-world environments is a formidable challenge, especially when the environment changes frequently due to humanrobot interactions ...
- **p. 1 / Abstract - extractive body cue:** Traditional methods typically assume static scenes, which limits their applicability in the continuously changing real world.
- **p. 1 / Abstract - extractive body cue:** To overcome these limitations, we present DovSG, a novel mobile manipulation framework that leverages dynamic open-vocabulary 3D scene graphs and a language-guided task planning module ...
- **p. 1 / Abstract - extractive body cue:** DovSG takes RGB-D sequences as input and utilizes vision-language models (VLMs) for object detection to obtain high-level object semantic features.
- **p. 1 / Abstract - extractive body cue:** Based on the segmented Manuscript received: October 16, 2024; Revised January 2, 2025; Accepted February 4, 2025.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This limitation restricts their applicability in real-world scenarios where adaptability is crucial.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To address the challenge of scene perception, our perception module integrates advanced tools such as RecognizeAnything [6], Grounding DINO [7], Segment Anything-2 [8], and CLIP ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our contributions are as follows: • We propose a novel robotic framework that integrates dynamic open-vocabulary 3D scene graphs with languageguided task planning, enabling accurate ...
- **p. 4 / III. METHOD - extractive body cue:** We propose an efficient method that leverages new RGB-D observations to update the volumetric representation accordingly.
- **p. 2 / III. METHOD - extractive body cue:** DovSG enables mobile robots to perform long-term tasks in indoor environments by constructing dynamic 3D scene graphs and using large language models for task planning.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we enhance robotic capabilities by introducing a novel and practical robotic framework, the DovSG system.
- **p. 4 / III. METHOD - extractive body cue:** To address this issue, we have designed a simple memory update module that can quickly perform local updates to the memory based on new RGB-D ...
- **p. 4 / III. METHOD - extractive body cue:** Then, we apply an advanced Open-Vocal segmentation model to segment regions in the RGB images, extract semantic feature vectors for each region, and project them ...
- **p. 5 / III. METHOD - extractive body cue:** 2) Mobile control: Once the target location is determined, we use the A* [34] algorithm to generate a collision-free navigation path from the start point ...
- **p. 5 / III. METHOD - extractive body cue:** Each subtask output by GPT consists of an "action_name" and multiple "object_name", which are directly extracted from the description and maintain the same level of ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | YAN et al.: DYNAMIC OPEN-VOCABULARY 3D SCENE GRAPHS FOR LONG-TERM LANGUAGE-GUIDED MOBILE MANIPULATION 5 and color information, we process each new observation Ik as follows: (1) We transform the all voxel point ... | egocentric RGB-D, language/task goal, base-arm proprioception | p. 5 (III. METHOD), p. 4 (III. METHOD) |
| State/latent | YAN, DYNAMIC, OPEN-VOCABULARY, SCENE, GRAPHS, LONG-TERM, LANGUAGE-GUIDED, MOBILE, MANIPULATION, color, information, process | map/object/contact state와 base-arm coordination decision | p. 5 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD) |
| Output/action | After the robot collects new RGB-D observations Ik for k ∈{t + 1, ..., t + n}, where each observation Ik = ⟨Irgb k , Idepth k , Ic2b k ⟩includes the ... | base motion plus arm/gripper action | p. 4 (III. METHOD), p. 5 (III. METHOD), p. 3 (III. METHOD) |
| Objective/outcome | 1) Open-vocabuary 2D Segmentation: To maximize object recognition in the scene, we first apply the image tagging model Recognize-Anything [6] to each frame It, generating a set of object classes {ct,i}, i ... | long-horizon task success, reachability, collision과 recovery | p. 3 (III. METHOD), p. 4 (III. METHOD), p. 6 (III. METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** Our contributions are as follows: • We propose a novel robotic framework that integrates dynamic open-vocabulary 3D scene graphs with languageguided task planning, enabling accurate ...
- **p. 4 / III. METHOD - extractive body cue:** We propose an efficient method that leverages new RGB-D observations to update the volumetric representation accordingly.
- **p. 2 / III. METHOD - extractive body cue:** DovSG enables mobile robots to perform long-term tasks in indoor environments by constructing dynamic 3D scene graphs and using large language models for task planning.
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this work, we enhance robotic capabilities by introducing a novel and practical robotic framework, the DovSG system.
- **p. 4 / III. METHOD - extractive body cue:** To address this issue, we have designed a simple memory update module that can quickly perform local updates to the memory based on new RGB-D ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** This makes it highly likely for the robot to navigate near the target, resulting in a significantly higher success rate compared to "Appearance" and "Positional ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Additionally, in "Appearance" and "Positional Shift" scenarios, DovSG achieves a scene change recognition success rate approximately 28% higher than the GPT-4o.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** In this section, We evaluate DovSG's performance in dynamic, real-world environments to answer two key questions: (1) How well does our system adapt to changes ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Embodiment/environment | 2) Environment and Task Setups: To verify our method's ability to enable robots to perform long-term tasks in dynamic environments, we designed an experiment in 4 real-world rooms. | hardware/simulator version and reset protocol | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Dataset/benchmark | (3) In dynamic environments, DovSG significantly outperforms Ok-Robot (which assumes a static scene) in long-term tasks, thanks to its ability to adapt to scene changes. | role, split, size and leakage | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |
| Metric | (3) Task Success Rate: This metric represents the overall task completion success rate. | definition, denominator, direction and uncertainty | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (Figure/Table caption) |
| Baseline/ablation | In contrast, DovSG, supported by precise relocalization, can accurately identify the voxel index where changes have occurred in the scene, significantly outperforming the baseline. | fair input/data/compute/action matching | p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / IV. EXPERIMENTS - extractive body cue:** In the "Positional Shift" scenario, the residual effect of CLIP features can occasionally mislead the robot into navigating toward the object's historical location, ultimately causing ...
- **p. 5 / III. METHOD - extractive body cue:** 2) Mobile control: Once the target location is determined, we use the A* [34] algorithm to generate a collision-free navigation path from the start point ...
- **p. 6 / III. METHOD - extractive body cue:** A buffer of 0.1 is added to account for potential collisions.
- **p. 6 / III. METHOD - extractive body cue:** In the first row, we cropped the point cloud input into anyGrasp within a certain range around the target object, allowing anyGrasp to focus more ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Although Ok-Robot can occasionally succeed in locating the correct object under minor changes (e.g., "Minor Adjustment"), it struggles with larger modifications such as "Appearance" or ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 This limitation restricts their applicability in real-world scenarios where adaptability is crucial.를 문제로 두고, Our contributions are as follows: • We propose a novel robotic framework that integrates dynamic open-vocabulary 3D scene graphs with languageguided task planning, enabling accurate long-term task execution in dynamic and interactive ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
