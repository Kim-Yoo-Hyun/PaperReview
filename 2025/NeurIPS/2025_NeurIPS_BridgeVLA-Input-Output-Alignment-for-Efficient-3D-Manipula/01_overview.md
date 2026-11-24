# BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (32 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://neurips.cc/virtual/2025/poster/116823.
> PDF retrieval source: https://arxiv.org/pdf/2506.07961.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: Peiyan Li, Yixiang Chen, Hongtao Wu, Xiao Ma, Xiangnan Wu, Yan Huang, Liang Wang, Tao Kong, Tieniu Tan
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics, 3D Vision
- Official paper: https://neurips.cc/virtual/2025/poster/116823
- Full-text retrieval: https://arxiv.org/pdf/2506.07961.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (32 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

BridgeVLA는 3차원 점군을 여러 시점의 영상으로 투영하고, 각 영상에서 행동 위치의 히트맵을 예측해 로봇팔 동작을 결정한다. [PDF 1쪽](https://arxiv.org/pdf/2506.07961v2#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recently, leveraging pre-trained vision-language models (VLMs) for building vision-language-action (VLA) models has emerged as a promising approach to effective robot manipulation learning.
- **p. 1 / Abstract - extractive body cue:** However, only few methods incorporate 3D signals into VLMs for action prediction, and they do not fully leverage the spatial structure inherent in 3D data, ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce a new paradigm for constructing 3D VLAs.
- **p. 1 / Abstract - extractive body cue:** Specifically, we first pre-train the VLM backbone to take 2D images as input and produce 2D heatmaps as output.
- **p. 1 / Abstract - extractive body cue:** Using this pre-trained VLM as the backbone, we then fine-tune the entire VLA model while maintaining alignment between inputs and outputs by: (1) projecting raw ...
- **p. 2 / 1 Introduction - extractive body cue:** This strategy fails to take advantage of the 3D structural priors as previous efficient 3D policies [10-14] that align the observation input and action output ...
- **p. 2 / 1 Introduction - extractive body cue:** To tackle the challenges mentioned above, as inllustrated in Fig.

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** In summary, the contributions of this paper are threefold: • We introduce BridgeVLA, a novel 3D VLA model that efficiently and effectively learns 3D robot ...
- **p. 2 / 1 Introduction - extractive body cue:** 1, we present BridgeVLA, a novel 3D VLA model that achieves remarkable sample efficiency and strong generalization capabilities.
- **p. 2 / 1 Introduction - extractive body cue:** 2D Finetune 2D Pretrain Real World Simulation BridgeVLA 2D Heatmap Image Instructions 3D Projection 3D actions [ Our framework VLM BridgeVLA ... ... "Find all ...
- **p. 9 / Method - extractive body cue:** We also compare with four methods introduced in Sec.
- **p. 10 / Method - extractive body cue:** Although our method outperforms baseline methods in the Category setting, its absolute success rate is not high.
- **p. 10 / Method - extractive body cue:** To demonstrate BridgeVLA's advantages over existing manipulation policy, we compare it with four types of representative methods: 1) SpatialVLA [16]: A state-of-the-art 3D VLA model ...
- **p. 10 / Method - extractive body cue:** 3) ACT [24]: A state-of-the-art 2D non-VLA model using a Conditional Variational Autoencoder (CVAE) to model action distributions.
- **p. 11 / Method - extractive body cue:** For ablation, we replaced the convex upsampling module (309M parameters) with a similarly sized Transformer decoder (303M) to directly predict target positions, supervised by MSE ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Keys to our method are that (1) it converts 3D inputs to 2D images to align with the 2D image inputs of the pre-trained VLM; (2) it aligns the input observation and ... | image/video, language instruction, proprioception과 history | p. 12 (Method), p. 2 (1 Introduction) |
| State/latent | Keys, converts, inputs, images, align, image, pre-trained, VLM, aligns, input, observation, output | language-grounded task state와 action-policy context | p. 12 (Method), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Output/action | The 2D heatmaps, generated from the tokens corresponding to the projection images, share the same resolution as these images, aligning the input observations and output actions within a unified spatial structure. | continuous action, pose 또는 action chunk | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 10 (Method) |
| Objective/outcome | For ablation, we replaced the convex upsampling module (309M parameters) with a similarly sized Transformer decoder (303M) to directly predict target positions, supervised by MSE loss. | instruction following, task success, generalization과 latency | p. 11 (Method), p. 11 (Method), p. 12 (Method) |

## Main Claims and Actual Contribution

- 일반 영상에서 2차원 위치 히트맵을 예측하도록 VLM을 사전학습한 뒤, 로봇 자료에서도 같은 공간적 입력·출력 형식을 유지했다. [PDF 3쪽](https://arxiv.org/pdf/2506.07961v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2506.07961v2#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2506.07961v2#page=5)
- RLBench에서 조작 과제 성공률을 비교하고 COLOSSEUM에서 카메라·배경 등 조건 변화에 대한 강건성을 평가했다. [PDF 6쪽](https://arxiv.org/pdf/2506.07961v2#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2506.07961v2#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2506.07961v2#page=8)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 8 (4 Experiments), p. 7 (4 Experiments) |
| Embodiment/environment | Both visual encoders show strong adaptability on various robotics tasks in both simulation and the real world. | hardware/simulator version and reset protocol | p. 8 (4 Experiments), p. 7 (4 Experiments) |
| Dataset/benchmark | The model is trained on the data from the original RLBench benchmark but evaluated in environments spanning 12 axes of perturbations. | role, split, size and leakage | p. 8 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments) |
| Metric | Models are evaluated via binary success rates over 25 trials per task, with a maximum of 25 action steps per trial. | definition, denominator, direction and uncertainty | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments) |
| Baseline/ablation | Compared to the state-of-the-art baseline, BridgeVLA improves the average success rate by 7.3%. perturbation, 3) compute the average success rate of all evaluated tasks for every perturbation. | fair input/data/compute/action matching | p. 8 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 10 / Method - extractive body cue:** A common failure mode is that the robot often ignores the target object and moves directly to the 10
- **p. 10 / Method - extractive body cue:** As we can see, most methods completely fails when given only 10 trajectories per task except two 3D related methods: RVT-2 and BridgeVLA.
- **p. 6 / 4 Experiments - extractive body cue:** Q3: How robust is BridgeVLA in handling visual disturbances (e.g., distractors, background, and lighting)?
- **p. 12 / Method - extractive body cue:** 5 Conclusions & Future Work This paper has introduced BridgeVLA, a novel and efficient 3D vision-language-action (VLA) model built on top of a pre-trained vision-language ...
- **p. 8 / 4 Experiments - extractive body cue:** These results address Q3, showcasing that BridgeVLA possesses strong robustness against visual perturbation.
- **p. 9 / Method - extractive body cue:** Distractor, Lighting, Background, and Height aim to evaluate the robustness 9

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 1 (1 Introduction), p. 10 (Method), p. 11 (Method)이다.
