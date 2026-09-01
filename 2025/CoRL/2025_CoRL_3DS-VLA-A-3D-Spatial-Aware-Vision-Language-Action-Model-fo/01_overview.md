# 3DS-VLA: A 3D Spatial-Aware Vision Language Action Model for Robust Multi-Task Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v305/li25g.html.
> PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v305/main/assets/li25g/li25g.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2025 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, 3D Vision, Robotics
- Official paper: https://proceedings.mlr.press/v305/li25g.html
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v305/main/assets/li25g/li25g.pdf
- Code/Project: https://vis-www.cs.umass.edu/3ds-vla/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 All these limitations lead us to consider: "How can we build a robust VLA model that incorporates comprehensive 3D spatial awareness?" To address the above challenges, as shown in Fig.를 문제로 두고, Our contributions are as follows: 1) We propose 3DS-VLA, equipping pretrained 2D VLMs with comprehensive 3D awareness for robust end-effector pose prediction.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recently, 2D vision-language-action (VLA) models have made significant strides in multi-task manipulation.
- **p. 1 / Abstract - extractive body cue:** However, these models struggle to reason about 3D spatial relationships from 2D image inputs.
- **p. 1 / Abstract - extractive body cue:** Although an increasing number of 3D imitation learning approaches explicitly integrate 3D information, they face challenges such as the lack of generalized 3D pretrained models ...
- **p. 1 / Abstract - extractive body cue:** Meanwhile, existing policies typically focus on the perception-to-action learning paradigm, lacking an explicit understanding of the spatial and temporal relationships between the robot and its ...
- **p. 1 / Abstract - extractive body cue:** To address this, we propose 3DS-VLA, which enhances pretrained 2D vision-language models (VLMs) with comprehensive 3D awareness, enabling the prediction of robust end-effector poses.
- **p. 2 / 1 Introduction - extractive body cue:** All these limitations lead us to consider: "How can we build a robust VLA model that incorporates comprehensive 3D spatial awareness?" To address the above ...
- **p. 1 / 1 Introduction - extractive body cue:** However, since robots operate in a complex 3D world, they face challenges in perceiving 3D geometry and reasoning about spatial context solely from 2D image ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are as follows: 1) We propose 3DS-VLA, equipping pretrained 2D VLMs with comprehensive 3D awareness for robust end-effector pose prediction.
- **p. 4 / 3 Method - extractive body cue:** Therefore, we propose a 2D-to-3D positional alignment mechanism that allows the original 2D PEs, which are interpretable to pretrained models, to encode semantically aligned 2D ...
- **p. 2 / 1 Introduction - extractive body cue:** 1 (left), we propose 3DS-VLA, which equips pretrained 2D vision-language models (2D VLMs) with 3D spatial awareness for robust action generation.
- **p. 3 / 3 Method - extractive body cue:** 3.1 Task Formulation and Model Architecture Given a dataset D = {τ1, . . . , τN} of N expert demonstrations, each demonstration τ is ...
- **p. 4 / 3 Method - extractive body cue:** The model π consists of a 2D visual encoder, LLM (LLaMA) [63], a cross-modality projection module [62], and LoRA adapters [64].
- **p. 3 / 3 Method - extractive body cue:** The objective of policy model π is to learn action generation in SE(3) space: π : (ot, l, kt, rt) →ˆat+1.
- **p. 4 / 3 Method - extractive body cue:** 3.2), 2D images and 3D point clouds are first tokenized and encoded using pretrained 2D positional embeddings (PEa), then fused and processed by the shared ...
- **p. 5 / 3 Method - extractive body cue:** To model spatial constraints, we use task-specific 3D keypoints corresponding to scene entities.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | It takes visual inputs ot = {it, pt}, where it is the image and pt is the point cloud, while language l, keypoints kt, and robot state rt are provided as structured ... | image/video, language instruction, proprioception과 history | p. 3 (3 Method), p. 3 (3 Method) |
| State/latent | takes, visual, inputs, where, image, point, cloud, while, language, keypoints, robot, state | language-grounded task state와 action-policy context | p. 3 (3 Method), p. 3 (3 Method), p. 5 (3 Method) |
| Output/action | 3.1 Task Formulation and Model Architecture Given a dataset D = {τ1, . . . , τN} of N expert demonstrations, each demonstration τ is paired with a task description l and ... | continuous action, pose 또는 action chunk | p. 3 (3 Method), p. 5 (3 Method), p. 2 (1 Introduction) |
| Objective/outcome | The model supports the output of 7 or 14-DoF end-effector pose for single or dual arms and generates the predicted action ˆat+1 autoregressively, supervised by the ground-truth action at+1 under cross-entropy loss. | instruction following, task success, generalization과 latency | p. 3 (3 Method), p. 3 (3 Method), p. 4 (3 Method) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are as follows: 1) We propose 3DS-VLA, equipping pretrained 2D VLMs with comprehensive 3D awareness for robust end-effector pose prediction.
- **p. 4 / 3 Method - extractive body cue:** Therefore, we propose a 2D-to-3D positional alignment mechanism that allows the original 2D PEs, which are interpretable to pretrained models, to encode semantically aligned 2D ...
- **p. 2 / 1 Introduction - extractive body cue:** 1 (left), we propose 3DS-VLA, which equips pretrained 2D vision-language models (2D VLMs) with 3D spatial awareness for robust action generation.
- **p. 3 / 3 Method - extractive body cue:** 3.1 Task Formulation and Model Architecture Given a dataset D = {τ1, . . . , τN} of N expert demonstrations, each demonstration τ is ...
- **p. 4 / 3 Method - extractive body cue:** The model π consists of a 2D visual encoder, LLM (LLaMA) [63], a cross-modality projection module [62], and LoRA adapters [64].
- **p. 7 / 4 Experiment - extractive body cue:** Both Ours and Ours-s achieve the same average success rate of 0.66 on single-arm tasks, demonstrating that our model can effectively handle different embodiments within ...
- **p. 8 / 4 Experiment - extractive body cue:** Remarkably, the model achieves similar accuracy as it does in clean background settings.
- **p. 6 / 4 Experiment - extractive body cue:** 1, in the single-arm setting, our method surpasses all baselines by at least 4% average success rate.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4 Experiment), p. 8 (4 Experiment) |
| Embodiment/environment | Since we establish associations between the robot and its environment through structured text input, our model learns to focus on task-relevant objects while disregarding irrelevant background disturbances. | hardware/simulator version and reset protocol | p. 8 (4 Experiment), p. 6 (4 Experiment) |
| Dataset/benchmark | Our method is evaluated across 10 tasks on the Franka Research 3 (FR3) robot with a 3Dprinted UMI gripper [75]. | role, split, size and leakage | p. 8 (4 Experiment), p. 6 (4 Experiment), p. 7 (4 Experiment), p. 7 (4 Experiment) |
| Metric | 1, in the single-arm setting, our method surpasses all baselines by at least 4% average success rate. | definition, denominator, direction and uncertainty | p. 6 (4 Experiment), p. 7 (4 Experiment), p. 7 (4 Experiment) |
| Baseline/ablation | 2, in the dual-arm setting, our method outperforms all baselines by a significant margin. | fair input/data/compute/action matching | p. 6 (4 Experiment), p. 8 (4 Experiment), p. 5 (4 Experiment) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4 Experiment - extractive body cue:** This makes the pipeline prone to failure if the underlying models are inaccurate-for example, if GroundingDINO [71] misses critical keypoints on the cup handle that ...
- **p. 6 / 4 Experiment - extractive body cue:** Compared with 2D VLA methods, we observe frequent failures during the critical final stage of 3D contact.
- **p. 8 / 4 Experiment - extractive body cue:** Please refer to Appendix for more details: Section 7.2 for visualization of tasks in RLBench and real world and Section 7.3 for discussion of failure ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 6: Visualization of real-world tasks. The tasks are shown in key-frame flow. The primary failure mode is the imprecise prediction of end-effector poses. This ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 5: Visualization of simulation tasks. We conduct on both single-arm and dual-arm simula- tion tasks. 4. Bottle at rack: The robot needs to grasp ...
- **p. 7 / 4 Experiment - extractive body cue:** The robustness of 3DS-VLA when handling noise.
- **p. 6 / 4 Experiment - extractive body cue:** This demonstrates our model's robustness and potential for generalization across different control modalities, enabling strong spatial reasoning for dual-arm 6

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 All these limitations lead us to consider: "How can we build a robust VLA model that incorporates comprehensive 3D spatial awareness?" To address the above challenges, as shown in Fig.를 문제로 두고, Our contributions are as follows: 1) We propose 3DS-VLA, equipping pretrained 2D VLMs with comprehensive 3D awareness for robust end-effector pose prediction.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (3 Method), p. 4 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
