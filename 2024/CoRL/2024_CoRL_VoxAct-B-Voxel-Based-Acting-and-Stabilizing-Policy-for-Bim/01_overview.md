# VoxAct-B: Voxel-Based Acting and Stabilizing Policy for Bimanual Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v270/liu25i.html.
> PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v270/main/assets/liu25i/liu25i.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CoRL
- Authors: I-Chun Arthur Liu, Sicheng He, Daniel Seita, Gaurav S. Sukhatme
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLM, 3D manipulation, bimanual, Robotics
- Official paper: https://proceedings.mlr.press/v270/liu25i.html
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v270/main/assets/liu25i/liu25i.pdf
- Code/Project: https://voxact-b.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VoxAct-B는 언어 지시와 복셀 관측으로 양팔 조작에서 움직이는 팔과 물체를 안정시키는 팔의 행동을 예측한다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Bimanual manipulation is critical to many robotics applications.
- **p. 1 / Abstract - extractive body cue:** In contrast to single-arm manipulation, bimanual manipulation tasks are challenging due to higher-dimensional action spaces.
- **p. 1 / Abstract - extractive body cue:** Prior works leverage large amounts of data and primitive actions to address this problem, but may suffer from sample inefficiency and limited generalization across various ...
- **p. 1 / Abstract - extractive body cue:** To this end, we propose VoxAct-B, a language-conditioned, voxel-based method that leverages Vision Language Models (VLMs) to prioritize key regions within the scene and reconstruct ...
- **p. 1 / Abstract - extractive body cue:** We provide this voxel grid to our bimanual manipulation policy to learn acting and stabilizing actions.
- **p. 1 / 1 Introduction - extractive body cue:** However, they are generally sample inefficient, and using primitives can hinder generalization to different tasks as they are not easily adaptable to other types of ...
- **p. 1 / 1 Introduction - extractive body cue:** They typically require two-hand coordination and high-precision, fine-grained manipulation, which are challenging for current robotic manipulation systems.

## Core Idea

- **p. 1 / 1 Introduction - extractive body cue:** To this end, we propose VoxAct-B, a novel voxel-based, language-conditioned method for bimanual manipulation.
- **p. 4 / 4 Method - extractive body cue:** This allows our method to learn to map the appropriate acting or stabilizing actions to a given arm during training.
- **p. 1 / 1 Introduction - extractive body cue:** To address this, we propose utilizing VLMs to focus on the most pertinent regions within the scene by cropping out less relevant regions.
- **p. 2 / 1 Introduction - extractive body cue:** We introduce a bimanual version of Open Drawer, Open Jar, Put Item in Drawer, and Hand Over Item tasks.
- **p. 5 / 4 Method - extractive body cue:** The overall training loss for VoxAct-B is: Ltotal = Lacting + Lstabilizing (1) and where for both values of arm ∈{acting, stabilizing}, we have Larm ...
- **p. 5 / 4 Method - extractive body cue:** Then, we use Segment Anything [65], a foundational image segmentation model, to obtain the segmentation mask of the object and use the mask's centroid along ...
- **p. 14 / A.1 Additional Implementation Details - extractive body cue:** We use 2048 latents of dimension 512 in the Perceiver Transformer [70] and optimize the entire network using the LAMB [71] optimizer.
- **p. 17 / C Additional Implementation Details for the Baselines - extractive body cue:** Hyperparameter ACT Value Diffusion Policy Value learning rate 3e-5 1e-4 weight decay (for transformer only) - 1e-3 # encoder layers 4 - # decoder layers ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | At each time step, the input to each arm is a voxel observation v, proprioception data of both robot arms ρ, a language goal l ∈{ℓas, ℓsa}, and an arm ID ξ ... | image/video, language instruction, proprioception과 history | p. 4 (4 Method), p. 1 (1 Introduction) |
| State/latent | time, step, input, voxel, observation, proprioception, data, robot, arms, language, goal, task | language-grounded task state와 action-policy context | p. 4 (4 Method), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Output/action | Voxel representations, when coupled with discretized action spaces, can increase sample efficiency and generalization by introducing spatial equivariance into a learned system, where transformations of the input lead to corresponding tr ... | continuous action, pose 또는 action chunk | p. 1 (1 Introduction), p. 2 (1 Introduction), p. 4 (4 Method) |
| Objective/outcome | The overall training loss for VoxAct-B is: Ltotal = Lacting + Lstabilizing (1) and where for both values of arm ∈{acting, stabilizing}, we have Larm = -EY arm trans[log Varm trans]-EY arm ... | instruction following, task success, generalization과 latency | p. 5 (4 Method), p. 5 (4 Method), p. 16 (C Additional Implementation Details for the Baselines) |

## Main Claims and Actual Contribution

- 두 팔의 역할을 구분해 행동을 학습한다.
- 서랍과 병 열기 등 양팔 과제로 정책을 평가한다.

[저자 원문](https://proceedings.mlr.press/v270/liu25i.html)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 16 (C Additional Implementation Details for the Baselines), p. 6 (5 Experiments) |
| Embodiment/environment | For simulation experiments, we build on top of RLBench [14], a popular robot manipulation benchmark widely used in prior work, including VoxPoser and PerAct. | hardware/simulator version and reset protocol | p. 6 (5 Experiments), p. 6 (5 Experiments) |
| Dataset/benchmark | We generate 25 episodes of validation and test data using different random seeds. | role, split, size and leakage | p. 6 (5 Experiments), p. 6 (5 Experiments), p. 7 (5 Experiments), p. 14 (A.1 Additional Implementation Details) |
| Metric | Then, we use the bestperforming acting and stabilizing checkpoints to obtain the test success rate. | definition, denominator, direction and uncertainty | p. 14 (A.1 Additional Implementation Details), p. 16 (C Additional Implementation Details for the Baselines), p. 7 (6 Results) |
| Baseline/ablation | When we train all methods using more demonstrations (100), VoxAct-B still outperforms all baselines. | fair input/data/compute/action matching | p. 7 (6 Results), p. 6 (5 Experiments), p. 17 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6 Results - extractive body cue:** 6.3 Limitations and Failure Cases VoxAct-B implicitly assumes the object of interest does not encompass most of the workspace.
- **p. 8 / 6 Results - extractive body cue:** VoxAct-B succeeds in 6 out of 10 trials; the failures include robot joints hitting their limits, imprecision in grasping the handle, and collisions with the ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of VoxAct-B. Given RGB-D images and a language goal, we input an RGB image from the front camera and a text query ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Top: VLMs usage as part of VoxAct-B, visualizing the Open Jar task in simulation, showing the role of OWL-ViT and Segment Anything. The ...
- **p. 6 / 5 Experiments - extractive body cue:** Note that the real-world jar and drawer cannot be opened without the use of a second arm.
- **p. 6 / 5 Experiments - extractive body cue:** We also test the following ablations of VoxAct-B: • VoxAct-B w/o VLMs: does not use the VLMs to detect the object of interest and crop ...
- **p. 7 / 6 Results - extractive body cue:** VoxPoser does not have training, so its 10 and 100 results are identical.

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 Introduction), p. 5 (4 Method), p. 14 (A.1 Additional Implementation Details), p. 17 (C Additional Implementation Details for the Baselines)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, they are generally sample inefficient, and using primitives can hinder generalization to different tasks as they are not easily adaptable to other types of tasks. (p. 1, 1 Introduction).
- **Actual contribution:** To this end, we propose VoxAct-B, a novel voxel-based, language-conditioned method for bimanual manipulation. (p. 1, 1 Introduction).
- **Evaluation boundary:** Figure 4: Example successful rollouts (one per row) of VoxAct-B on a real-world bimanual setup with UR5s. Ablation experiments. Table 2 reports results on Open Drawer in simulation, based on ... (p. 8, Figure/Table caption).
- **Explicit failure boundary:** 6.3 Limitations and Failure Cases VoxAct-B implicitly assumes the object of interest does not encompass most of the workspace. (p. 8, 6 Results).

## 공개 자료 대조

- **코드** · 저자 양팔 행동·안정화 정책의 학습 진입점. [배포 파일](https://raw.githubusercontent.com/VoxAct-B/voxactb/1cc074b1730f52a7fd35d069d8c9099d18718bca/peract/train.py) · [저자 배포 안내](https://raw.githubusercontent.com/VoxAct-B/voxactb/1cc074b1730f52a7fd35d069d8c9099d18718bca/README.md)
- **데이터** · 저자의 양팔 Open Drawer 훈련 시연 ZIP. 같은 배포처의 pretrained_weights.zip은 CLIP·SAM 인코더 가중치다. [배포 파일](https://huggingface.co/datasets/arthur801031/voxact-b/blob/1c97d3e318a3d54bf2864a0bb346a1bae4b34c79/data/train/open_drawer_100_demos_corl_v1.zip) · [저자 배포 안내](https://raw.githubusercontent.com/VoxAct-B/voxactb/1cc074b1730f52a7fd35d069d8c9099d18718bca/README.md)
- **가중치** · Hand Over Item의 행동 담당 팔에 학습한 복셀 정책 가중치. 역할과 과제별 정책 파일을 따로 배포한다. [배포 파일](https://huggingface.co/datasets/arthur801031/voxact-b/blob/1c97d3e318a3d54bf2864a0bb346a1bae4b34c79/weights/hand_over_item_10_demos_ours_vlm_v1_11_acting/PERACT_BC/seed11/weights/700000/QAttentionAgent_layer0.pt) · [저자 배포 안내](https://raw.githubusercontent.com/VoxAct-B/voxactb/1cc074b1730f52a7fd35d069d8c9099d18718bca/README.md)
