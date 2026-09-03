# BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (32 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=ffBF6hYuQv.
> PDF retrieval source: https://arxiv.org/pdf/2506.07961.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics, 3D Vision
- Official paper: https://openreview.net/forum?id=ffBF6hYuQv
- Full-text retrieval: https://arxiv.org/pdf/2506.07961.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (32 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 This strategy fails to take advantage of the 3D structural priors as previous efficient 3D policies [10-14] that align the observation input and action output into a unified space, therefore leading to ...를 문제로 두고, In summary, the contributions of this paper are threefold: • We introduce BridgeVLA, a novel 3D VLA model that efficiently and effectively learns 3D robot manipulation with a vision-language model via input-output ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

- **p. 3 / 1 Introduction - extractive body cue:** In summary, the contributions of this paper are threefold: • We introduce BridgeVLA, a novel 3D VLA model that efficiently and effectively learns 3D robot ...
- **p. 2 / 1 Introduction - extractive body cue:** 1, we present BridgeVLA, a novel 3D VLA model that achieves remarkable sample efficiency and strong generalization capabilities.
- **p. 2 / 1 Introduction - extractive body cue:** 2D Finetune 2D Pretrain Real World Simulation BridgeVLA 2D Heatmap Image Instructions 3D Projection 3D actions [ Our framework VLM BridgeVLA ... ... "Find all ...
- **p. 9 / Method - extractive body cue:** We also compare with four methods introduced in Sec.
- **p. 10 / Method - extractive body cue:** Although our method outperforms baseline methods in the Category setting, its absolute success rate is not high.
- **p. 8 / 4 Experiments - extractive body cue:** BridgeVLA outperforms all the comparing baseline methods in terms of average success rate, significantly outperforming the best baseline method by 7.3%.
- **p. 7 / 4 Experiments - extractive body cue:** BridgeVLA outperforms all the comparing baseline methods, achieving an average success rate of 88.2% and an average rank of 1.9 across all the 18 tasks, ...
- **p. 8 / 4 Experiments - extractive body cue:** Compared to the state-of-the-art baseline, BridgeVLA improves the average success rate by 7.3%. perturbation, 3) compute the average success rate of all evaluated tasks for ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

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

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 This strategy fails to take advantage of the 3D structural priors as previous efficient 3D policies [10-14] that align the observation input and action output into a unified space, therefore leading to ...를 문제로 두고, In summary, the contributions of this paper are threefold: • We introduce BridgeVLA, a novel 3D VLA model that efficiently and effectively learns 3D robot manipulation with a vision-language model via input-output ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 10 (Method), p. 10 (Method), p. 11 (Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
