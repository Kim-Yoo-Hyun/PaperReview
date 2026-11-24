# 3DS-VLA: A 3D Spatial-Aware Vision Language Action Model for Robust Multi-Task Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v305/li25g.html.
> PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v305/main/assets/li25g/li25g.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CoRL
- Authors: Xiaoqi Li, Liang Heng, Jiaming Liu, Yan Shen, Chenyang Gu, Zhuoyang Liu, Hao Chen, Nuowei Han, Renrui Zhang, Hao Tang, Shanghang Zhang, Hao Dong
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, 3D Vision, Robotics
- Official paper: https://proceedings.mlr.press/v305/li25g.html
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v305/main/assets/li25g/li25g.pdf
- Code/Project: https://vis-www.cs.umass.edu/3ds-vla/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

3DS-VLA는 2차원 시각·언어 모델에 공간 정보를 더해 다중 조작 작업의 말단장치 자세를 예측한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v305/main/assets/li25g/li25g.pdf#page=1)

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

- 영상 위치와 3차원 좌표를 정렬해 같은 시각 인코더가 두 관측을 함께 표현하게 한다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v305/main/assets/li25g/li25g.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v305/main/assets/li25g/li25g.pdf#page=4)
- 행동에 관련된 물체와 로봇 동작 사이의 순차적 공간 제약을 학습시키고 시뮬레이션과 실제 조작에서 평가했다. [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v305/main/assets/li25g/li25g.pdf#page=5) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v305/main/assets/li25g/li25g.pdf#page=8)

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

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 1 (1 Introduction), p. 3 (3 Method), p. 4 (3 Method)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, since robots operate in a complex 3D world, they face challenges in perceiving 3D geometry and reasoning about spatial context solely from 2D image observations [12, 13, 14]. (p. 1, 1 Introduction).
- **Actual contribution:** Our contributions are as follows: 1) We propose 3DS-VLA, equipping pretrained 2D VLMs with comprehensive 3D awareness for robust end-effector pose prediction. (p. 2, 1 Introduction).
- **Evaluation boundary:** Additionally, we perform an extra experiment where we first fine-tune the pretrained VLM on the OXE dataset [74], which only takes 2D images as input, and then continue finetuning on ... (p. 7, 4 Experiment).
- **Explicit failure boundary:** This makes the pipeline prone to failure if the underlying models are inaccurate-for example, if GroundingDINO [71] misses critical keypoints on the cup handle that needs to be grasped, or ... (p. 8, 4 Experiment).

## 공개 자료 대조

- **코드** · 저자 배포판에 포함된 3DS-VLA 추론 코드. [배포 파일](https://raw.githubusercontent.com/clorislili/3ds-vla/3e51fedffa25f3039e2c58d85628b39c91be9a59/3ds-vla/test_model_2.py) · [저자 배포 안내](https://raw.githubusercontent.com/clorislili/3ds-vla/3e51fedffa25f3039e2c58d85628b39c91be9a59/readme.md)
- **데이터** · 저자 배포의 RLBench 과제 자료 ZIP. 실물 전체 학습 자료의 공개 범위는 미확인이다. [배포 파일](https://huggingface.co/datasets/Clorisss/RLBench/blob/763cbdc3f14faf559d29ccf59d95aeb494aef945/RLBench.zip) · [저자 배포 안내](https://raw.githubusercontent.com/clorislili/3ds-vla/3e51fedffa25f3039e2c58d85628b39c91be9a59/readme.md)
- **가중치** · 3DS-VLA가 배포한 과제 모델의 checkpoint-478000.pth. [배포 파일](https://huggingface.co/Clorisss/3ds-vla/blob/6d952d6f4ad082ad0da314a49234a87ac2138b50/checkpoint-478000.pth) · [저자 배포 안내](https://raw.githubusercontent.com/clorislili/3ds-vla/3e51fedffa25f3039e2c58d85628b39c91be9a59/readme.md)
