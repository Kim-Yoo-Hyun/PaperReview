# 4D-VLA: Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://neurips.cc/virtual/2025/poster/115166.
> PDF retrieval source: https://arxiv.org/pdf/2506.22242. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: Jiahui Zhang, Yurui Chen, Yueming Xu, Ze Huang, Yanpeng Zhou, Yu-Jie Yuan, Xinyue Cai, Guowei Huang, Xingyue Quan, Hang Xu, Li Zhang
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model
- Official paper: https://neurips.cc/virtual/2025/poster/115166
- Published PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/30b9c38b9ebeee281cd2bc41d39bf0e7-Paper-Conference.pdf
- Full-text retrieval at original review: https://arxiv.org/pdf/2506.22242
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

## Why This Paper Is Here

4D-VLA는 서로 다른 카메라와 로봇에서 모은 시연을 학습할 때 좌표계와 현재 상태의 모호성을 줄이도록 공간·시간 관측을 함께 사용한다. [PDF 1쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/30b9c38b9ebeee281cd2bc41d39bf0e7-Paper-Conference.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Leveraging diverse robotic data for pretraining remains a critical challenge.
- **p. 1 / Abstract - extractive body cue:** Existing methods typically model the dataset's action distribution using simple observations as inputs.
- **p. 1 / Abstract - extractive body cue:** However, these inputs are often incomplete, resulting in a dispersed conditional action distribution-an issue we refer to as coordinate system chaos and state chaos.
- **p. 1 / Abstract - extractive body cue:** This inconsistency significantly hampers pretraining efficiency.
- **p. 1 / Abstract - extractive body cue:** To address this, we propose 4D-VLA, a novel approach that effectively integrates 4D information into the input to mitigate these sources of chaos.
- **p. 2 / 1 Introduction - extractive body cue:** However, this approach lacks scalability and increases the complexity of training.
- **p. 2 / 1 Introduction - extractive body cue:** However, efficiently extracting useful information from these datasets remains a challenge for improving generalization across diverse scenarios.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are: (i) We propose 4D-VLA, an efficient VLA model that integrates a spatial module with vision features to generate 3D-aware spatial vision tokens, ...
- **p. 2 / 1 Introduction - extractive body cue:** Our approach enables robust pretraining, improving generalization to novel scenarios while outperforming baselines.
- **p. 5 / 3 Method - extractive body cue:** 3.5 MV-Bench We propose the MV-Bench to provide a comprehensive evaluation of model capabilities in learning control policies across diverse viewpoints and generalizing to novel ...
- **p. 3 / 3 Method - extractive body cue:** Vision-language model backbone We leverage a pretrained large vision-language model (VLM) as the backbone, specifically InternVL-4B [12], which consists of a text tokenizer T , ...
- **p. 4 / 3 Method - extractive body cue:** In our method, the input image I ∈R3×h×w is first encoded by E into a feature map with a downsampling rate of c, yielding fv ...
- **p. 5 / 3 Method - extractive body cue:** 3.4 Loss functions Algorithm 1: memory bank sampling Input: t, {It-j / j = 0, 1, . . . , n -1}, sample size k, ...
- **p. 3 / 3 Method - extractive body cue:** Specifically, VLA with a low-level control policy refers to a class of models that use the current observations as input to predict an action for ...
- **p. 8 / Method - extractive body cue:** In long-horizon tasks (Task 2 and 4), the model often succeeds in the first step but fails the second without access to history, due to ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Specifically, VLA with a low-level control policy refers to a class of models that use the current observations as input to predict an action for the robot in its present state, enabling ... | image/video, language instruction, proprioception과 history | p. 3 (3 Method), p. 5 (3 Method) |
| State/latent | Specifically, VLA, low-level, control, policy, refers, class, models, current, observations, input, predict | language-grounded task state와 action-policy context | p. 3 (3 Method), p. 5 (3 Method), p. 3 (3 Method) |
| Output/action | 3.4 Loss functions Algorithm 1: memory bank sampling Input: t, {It-j / j = 0, 1, . . . , n -1}, sample size k, feature extractor ϕ Output: A set of ... | continuous action, pose 또는 action chunk | p. 5 (3 Method), p. 3 (3 Method), p. 4 (3 Method) |
| Objective/outcome | 3.4 Loss functions Algorithm 1: memory bank sampling Input: t, {It-j / j = 0, 1, . . . , n -1}, sample size k, feature extractor ϕ Output: A set of ... | instruction following, task success, generalization과 latency | p. 5 (3 Method), p. 5 (3 Method), p. 3 (3 Method) |

## Main Claims and Actual Contribution

- 순차 RGB-D 관측으로 장면과 로봇 좌표를 정렬하고, 기억에서 서로 다른 정보를 담은 과거 프레임을 골라 행동 예측에 사용한다. [PDF 3쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/30b9c38b9ebeee281cd2bc41d39bf0e7-Paper-Conference.pdf#page=3) · [PDF 4쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/30b9c38b9ebeee281cd2bc41d39bf0e7-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/30b9c38b9ebeee281cd2bc41d39bf0e7-Paper-Conference.pdf#page=5)
- 새 카메라 시점에 대한 일반화를 시험하는 MV-Bench를 구성하고, 실물 조작에서도 시점 변화와 과거 프레임 사용의 효과를 비교했다. [PDF 6쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/30b9c38b9ebeee281cd2bc41d39bf0e7-Paper-Conference.pdf#page=6) · [PDF 7쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/30b9c38b9ebeee281cd2bc41d39bf0e7-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/30b9c38b9ebeee281cd2bc41d39bf0e7-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/30b9c38b9ebeee281cd2bc41d39bf0e7-Paper-Conference.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4 Experiments), p. 7 (4 Experiments) |
| Embodiment/environment | 4.1 Datasets and simulation environments DROID [2] A diverse real-world robot manipulation dataset with 76,000 demonstration trajectories, or 350 hours of interaction data, spanning a total of 564 scenes and 86 tasks, ... | hardware/simulator version and reset protocol | p. 6 (4 Experiments), p. 6 (4 Experiments) |
| Dataset/benchmark | 4.5 Real-world evaluation To evaluate models in real-world scenarios, we conducted physical experiments using a Franka robotic arm. | role, split, size and leakage | p. 6 (4 Experiments), p. 6 (4 Experiments), p. 7 (4 Experiments), p. 5 (4 Experiments) |
| Metric | Figure 4: Our real-world experiment settings. These settings aim to evaluate the model's spatial generalization, robustness to distractors, precision in placement, and ability to follow instructions. Each row presents a 3-frame executio ... | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 6 (4 Experiments), p. 7 (4 Experiments) |
| Baseline/ablation | Our model significantly outperforms other competitors, with an average success rate 12.1 higher than OpenVLA. †Denotes no available standard deviation data. | fair input/data/compute/action matching | p. 6 (4 Experiments), p. 7 (4 Experiments), p. 1 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 6 Conclusion - extractive body cue:** A limitation of our approach is its reliance on RGB-D input, which introduces hardware restriction.
- **p. 6 / 4 Experiments - extractive body cue:** To avoid occlusion from the black box, test views in blocked areas are excluded.
- **p. 7 / 4 Experiments - extractive body cue:** It highlights the robustness of our model in handling diverse viewpoints.
- **p. 7 / 4 Experiments - extractive body cue:** Task2: Robustness to distractors Task3: Precise placement Task4: Instruction following Figure 4: Our real-world experiment settings.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Our multi-view real-world experiment settings. These settings aim to evaluate the model's out-of-distribution and novel-view generalization ability.
- **p. 9 / Figure/Table caption - extractive body cue:** Table 4: Real-world multi-view evaluation. We test our model's spatial generalization across varying viewpoints and object layouts. 4D-VLA shows strong in-view and cross-view performance, highlighting ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 2 (1 Introduction), p. 3 (1 Introduction), p. 5 (3 Method), p. 3 (3 Method)이다.
