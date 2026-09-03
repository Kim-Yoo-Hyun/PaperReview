# RVT: Robotic View Transformer for 3D Object Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2306.14896.
> PDF retrieval source: https://arxiv.org/pdf/2306.14896. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2023 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: CORE
- Tags: Robotics, 3D manipulation, Transformer
- Official paper: https://arxiv.org/abs/2306.14896
- Full-text retrieval: https://arxiv.org/pdf/2306.14896
- Code/Project: https://robotic-view-transformer.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 vla 문제를 이해하기 위해 읽는다. 본문은 C2FARM [5] represents the scene with multi-resolution voxels and achieves strong performance on difficult RLBench tasks.를 문제로 두고, To summarize, our contributions are threefold: first, we propose RVT, a multi-view transformer for 3D object manipulation that is accurate and scalable; second, we investigate various design choices for the multi-view transformer ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** For 3D object manipulation, methods that build an explicit 3D representation perform better than those relying only on camera images.
- **p. 1 / Abstract - extractive body cue:** But using explicit 3D representations like voxels comes at large computing cost, adversely affecting scalability.
- **p. 1 / Abstract - extractive body cue:** In this work, we propose RVT, a multi-view transformer for 3D manipulation that is both scalable and accurate.
- **p. 1 / Abstract - extractive body cue:** Some key features of RVT are an attention mechanism to aggregate information across views and re-rendering of the camera input from virtual views around the ...
- **p. 1 / Abstract - extractive body cue:** In simulations, we find that a single RVT model works well across 18 RLBench tasks with 249 task variations, achieving 26% higher relative success than ...
- **p. 1 / 1 Introduction - extractive body cue:** C2FARM [5] represents the scene with multi-resolution voxels and achieves strong performance on difficult RLBench tasks.
- **p. 2 / 1 Introduction - extractive body cue:** Hence, a key question is - can we build a manipulation network that not only performs well but also inherits the scalability of view-based methods?

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** To summarize, our contributions are threefold: first, we propose RVT, a multi-view transformer for 3D object manipulation that is accurate and scalable; second, we investigate ...
- **p. 2 / 1 Introduction - extractive body cue:** To this end, we propose RVT (Robotic View Transformer) that significantly outperforms the SOTA voxel-based method both in terms of success rate and training time, ...
- **p. 3 / 3 Method - extractive body cue:** The input consists of (1) a language description of the task, (2) the current visual state (from RGB-D camera(s)), and (3) the current gripper state ...
- **p. 1 / 1 Introduction - extractive body cue:** This hinders fast development and prototyping.
- **p. 5 / 3 Method - extractive body cue:** The training time and inference speed of PerAct and RVT are measured on the same GPU model. we use global features (G).
- **p. 4 / 3 Method - extractive body cue:** The model outputs an 8-dimensional action, including the 6-DoF target end effector pose (3-DoF for translation and 3-DoF for rotation), 1-DoF gripper state (open or ...
- **p. 4 / 3 Method - extractive body cue:** Our proposed method (RVT) is a transformer model [27] that processes images re-rendered around the robot workspace, produces an output for each view, and then ...
- **p. 5 / 3 Method - extractive body cue:** We use binary classification loss for the gripper state and collision indicator.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The model outputs an 8-dimensional action, including the 6-DoF target end effector pose (3-DoF for translation and 3-DoF for rotation), 1-DoF gripper state (open or close), and a binary indicator for whether ... | image/video, language instruction, proprioception과 history | p. 4 (3 Method), p. 4 (3 Method) |
| State/latent | model, outputs, dimensional, action, including, DoF, target, effector, pose, translation, rotation, gripper | language-grounded task state와 action-policy context | p. 4 (3 Method), p. 4 (3 Method), p. 3 (3 Method) |
| Output/action | Each demonstration Di = ({oi 1...mi}, {ai 1...mi}, li) is a successful roll-out of length mi, where li is the language description of the task, {oi 1, oi 2, ..., oi mi} ... | continuous action, pose 또는 action chunk | p. 4 (3 Method), p. 3 (3 Method), p. 3 (3 Method) |
| Objective/outcome | For heatmaps, we use the cross-entropy loss for each image. | instruction following, task success, generalization과 latency | p. 5 (3 Method), p. 5 (3 Method) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** To summarize, our contributions are threefold: first, we propose RVT, a multi-view transformer for 3D object manipulation that is accurate and scalable; second, we investigate ...
- **p. 2 / 1 Introduction - extractive body cue:** To this end, we propose RVT (Robotic View Transformer) that significantly outperforms the SOTA voxel-based method both in terms of success rate and training time, ...
- **p. 3 / 3 Method - extractive body cue:** The input consists of (1) a language description of the task, (2) the current visual state (from RGB-D camera(s)), and (3) the current gripper state ...
- **p. 1 / 1 Introduction - extractive body cue:** This hinders fast development and prototyping.
- **p. 6 / 4 Experiments - extractive body cue:** Overall, RVT outperforms all baselines with the best rank and success rate when averaged across all tasks.
- **p. 8 / 4 Experiments - extractive body cue:** Our model overall achieves an 82.5% success rate on non-marker tasks.
- **p. 8 / 4 Experiments - extractive body cue:** Overall, RVT achieves high success rates for the stack block task (100%) and the press sanitizer task (80%).
- **p. 6 / 4 Experiments - extractive body cue:** It outperforms prior state-of-the-art methods, C2F-ARM, by 42 percentage points (213% relative improvement); and PerAct by 13 percentage points (26% relative improvement).

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4 Experiments), p. 8 (4 Experiments) |
| Embodiment/environment | Just like the baselines, we use the RLBench training dataset with 100 expert demonstrations per task (1800 demonstrations over all tasks). | hardware/simulator version and reset protocol | p. 5 (4 Experiments), p. 8 (4 Experiments) |
| Dataset/benchmark | Given a sampled task and scene configuration, we ask the human demonstrator to specify a sequence of gripper target poses by kinesthetically moving the robot arm around. | role, split, size and leakage | p. 5 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 5 (4 Experiments) |
| Metric | Due to the randomness of the sampling-based motion planner, we run each model five times on the same 25 variations for each task and report the average success rate and standard deviation ... | definition, denominator, direction and uncertainty | p. 6 (4 Experiments), p. 5 (Figure/Table caption), p. 8 (4 Experiments) |
| Baseline/ablation | Overall, RVT outperforms all baselines with the best rank and success rate when averaged across all tasks. | fair input/data/compute/action matching | p. 6 (4 Experiments), p. 6 (4 Experiments), p. 8 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4 Experiments - extractive body cue:** 5 Conclusions and Limitations We proposed RVT, a multi-view transformer model for 3D object manipulation.
- **p. 8 / 4 Experiments - extractive body cue:** Although we found RVT to achieve state-of-the-art results, we identify some limitations that present exciting directions for future research.
- **p. 15 / 6 Appendix - extractive body cue:** 6.2 RVT Overview Insert peg in the blue spoke Virtual Image 1 Virtual Image 2 Virtual Image 5 Patchify Projection Attention X 4 Attention X ...
- **p. 6 / 4 Experiments - extractive body cue:** Hence, the reported performance does not reflect a single multi-task model.
- **p. 5 / 4 Experiments - extractive body cue:** The visual observations are captured from four noiseless RGB-D cameras positioned at the front, left shoulder, right shoulder, and wrist with a resolution of 128×128.

## Why Read It

Robotics-enabling 3D perception의 vla 문제를 이해하기 위해 읽는다. 본문은 C2FARM [5] represents the scene with multi-resolution voxels and achieves strong performance on difficult RLBench tasks.를 문제로 두고, To summarize, our contributions are threefold: first, we propose RVT, a multi-view transformer for 3D object manipulation that is accurate and scalable; second, we investigate various design choices for the multi-view transformer ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (3 Method), p. 4 (3 Method), p. 4 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (16 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** C2FARM [5] represents the scene with multi-resolution voxels and achieves strong performance on difficult RLBench tasks. (p. 1, 1 Introduction).
- **Actual contribution:** To summarize, our contributions are threefold: first, we propose RVT, a multi-view transformer for 3D object manipulation that is accurate and scalable; second, we investigate various design choices for the ... (p. 2, 1 Introduction).
- **Evaluation boundary:** Table 2: Left: Ablations on RLBench. A larger res., adding view correspondence, adding depth channel, separating initial attention layers, orthographic projection, using rotation aug., and re- rendered views around cube ... (p. 7, Figure/Table caption).
- **Explicit failure boundary:** 5 Conclusions and Limitations We proposed RVT, a multi-view transformer model for 3D object manipulation. (p. 8, 4 Experiments).
