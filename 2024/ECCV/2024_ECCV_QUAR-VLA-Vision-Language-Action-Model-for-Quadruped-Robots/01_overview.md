# QUAR-VLA: Vision-Language-Action Model for Quadruped Robots

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/808_ECCV_2024_paper.php.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00808.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, Vision-Language Model, Robotics
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/808_ECCV_2024_paper.php
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00808.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 locomotion 문제를 이해하기 위해 읽는다. 본문은 However, such a task specification often relies on a single (coarse-grained) goal image instruction, making it difficult to apply in many real-world combination tasks, i.e. requiring combining multiple sub-instructions.를 문제로 두고, Our extensive evaluation shows that our approach leads to performant robotic policies and enables QUART to obtain a range of generalization capabilities.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** Quadruped robots, characterized by their excellent traversability on complex terrains and agile movements, have garnered significant attention in the field of robotics [14].
- **p. 1 / 1 Introduction - extractive body cue:** Researchers have extensively employed these robots to explore tasks encompassing autonomous navigation and manipulation [16,17,36]. ⋆Corresponding author
- **p. 2 / 1 Introduction - extractive body cue:** Ding et al. "Trot in place, with the front right leg move twice as fast as other legs" (a) QUAR-VA (b) QUAR-LA (c) QUAR-VLA Language ...
- **p. 2 / 1 Introduction - extractive body cue:** 1: Comparison of QUAR-VA, QUAR-LA, and QUAR-VLA.
- **p. 2 / 1 Introduction - extractive body cue:** QUAR-VA solely utilizes coarse-grained vision information, lacking explicit instructions for handling diverse tasks.
- **p. 2 / 1 Introduction - extractive body cue:** However, such a task specification often relies on a single (coarse-grained) goal image instruction, making it difficult to apply in many real-world combination tasks, i.e. ...
- **p. 2 / 1 Introduction - extractive body cue:** This task primarily encompasses two challenges.

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** Our extensive evaluation shows that our approach leads to performant robotic policies and enables QUART to obtain a range of generalization capabilities.
- **p. 2 / 1 Introduction - extractive body cue:** To enable quadruped robots to autonomously navigate and manipulate various tasks, in this paper, we propose a new paradigm: Vision-Language-Action tasks for QUAdruped Robots (QUAR-VLA), ...
- **p. 4 / 1 Introduction - extractive body cue:** 2) We present a large-scale multi-task dataset, QUARD, and a Vision-Language-Action model, QUART to solve the QUAR-VLA tasks.
- **p. 5 / 3 Method - extractive body cue:** Initially, we present the definition of our proposed QUAR-VLA in Section 3.1.
- **p. 5 / 3 Method - extractive body cue:** The policy is a mapping from images and instructions to actions, and can be written as µ : S × W →A, where the action ...
- **p. 8 / 3 Method - extractive body cue:** Notably, QUART model takes a single image s and a natural language instruction w as input, which are first converted into corresponding tokens t through ...
- **p. 9 / 3 Method - extractive body cue:** We use a standard categorical cross-entropy objective and causal masking that was utilized in prior Transformer-based controllers [18,29].
- **p. 9 / 3 Method - extractive body cue:** To directly convert models' output to valid robot actions for downstream control, we need detokenize the discrete action token ad into continuous representation ac (except ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The policy QUART could be shown as follow: \begin {a li g ned} &\operat orname {QUART}(a_d/s, w) = p(a_d/t) \tau (t/s, w)\\ \end {aligned} (2) where w, s are the input images ... | proprioception, terrain/perception observation과 velocity command | p. 8 (3 Method), p. 9 (3 Method) |
| State/latent | policy, QUART, could, follow, begin, operat, orname, a_d/s, a_d/t, aligned, where, input | body/contact state, foothold 또는 behavior mode | p. 8 (3 Method), p. 9 (3 Method), p. 9 (3 Method) |
| Output/action | Observation I Instruction W VLA De-Tokenize Deploy ··· Action ad Velocity Gait B-Pose Terminate vx vy wz θ1 θ2 θ3 f hz sy hz f Φ t Feature Extraction & Fusion Concat ... | joint target, torque, footstep 또는 locomotion action | p. 9 (3 Method), p. 9 (3 Method), p. 2 (1 Introduction) |
| Objective/outcome | We use a standard categorical cross-entropy objective and causal masking that was utilized in prior Transformer-based controllers [18,29]. | velocity/progress, stability, energy와 terrain generalization | p. 9 (3 Method), p. 5 (3 Method), p. 7 (3 Method) |

## Main Claims and Actual Contribution

- **p. 3 / 1 Introduction - extractive body cue:** Our extensive evaluation shows that our approach leads to performant robotic policies and enables QUART to obtain a range of generalization capabilities.
- **p. 2 / 1 Introduction - extractive body cue:** To enable quadruped robots to autonomously navigate and manipulate various tasks, in this paper, we propose a new paradigm: Vision-Language-Action tasks for QUAdruped Robots (QUAR-VLA), ...
- **p. 4 / 1 Introduction - extractive body cue:** 2) We present a large-scale multi-task dataset, QUARD, and a Vision-Language-Action model, QUART to solve the QUAR-VLA tasks.
- **p. 5 / 3 Method - extractive body cue:** Initially, we present the definition of our proposed QUAR-VLA in Section 3.1.
- **p. 5 / 3 Method - extractive body cue:** The policy is a mapping from images and instructions to actions, and can be written as µ : S × W →A, where the action ...
- **p. 11 / 4 Experiments - extractive body cue:** QUART has achieved success rates far exceeding those of the baselines in tasks of all difficulty levels, especially in the most challenging crawl and unload ...
- **p. 12 / 1. Comparison within VLM baselines. The experiment results reveal - extractive body cue:** Consequently, while the performance gains may be marginal in simple tasks, there is a noticeable enhancement in tasks that involve complex mechanical movements. significantly improved ...
- **p. 10 / 4 Experiments - extractive body cue:** We follow the standard robot evaluation metrics [7, 9], success rate (SR), to evaluate the overall performance.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 11 (4 Experiments), p. 12 (1. Comparison within VLM baselines. The experiment results reveal) |
| Embodiment/environment | To tackle these two questions, we present the QUART models tailored for quadruped robots and the QUARD dataset, which includes diverse tasks such as navigation and manipulation. | hardware/simulator version and reset protocol | p. 14 (1. Comparison within VLM baselines. The experiment results reveal), p. 14 (1. Comparison within VLM baselines. The experiment results reveal) |
| Dataset/benchmark | Both models are trained with the next token prediction objective, which corresponds to the behavior cloning loss in robot learning. | role, split, size and leakage | p. 14 (1. Comparison within VLM baselines. The experiment results reveal), p. 14 (1. Comparison within VLM baselines. The experiment results reveal), p. 10 (4 Experiments), p. 10 (4 Experiments) |
| Metric | We follow the standard robot evaluation metrics [7, 9], success rate (SR), to evaluate the overall performance. | definition, denominator, direction and uncertainty | p. 10 (4 Experiments), p. 11 (4 Experiments), p. 13 (1. Comparison within VLM baselines. The experiment results reveal) |
| Baseline/ablation | Ding et al. action architecture for multi-task quadruped task compared to previous VLM baselines? | fair input/data/compute/action matching | p. 10 (4 Experiments), p. 10 (4 Experiments), p. 11 (1. Comparison within VLM baselines. The experiment results reveal) |

## Explicit Limitations and Failure Boundary

- **p. 12 / 1. Comparison within VLM baselines. The experiment results reveal - extractive body cue:** This failure manifests in behaviors such as repetitive motion, misdirection, wrong terminate commands.
- **p. 12 / 1. Comparison within VLM baselines. The experiment results reveal - extractive body cue:** When confronted with unseen instructions, the alighment between the existing language and the integration of vision and action cues within the baselines is compromised, resulting ...
- **p. 11 / 1. Comparison within VLM baselines. The experiment results reveal - extractive body cue:** This observation suggests that while visual language models (VLMs) can grasp abstract principles of the world, directly applying VLMs does not readily translate to the ...
- **p. 14 / 1. Comparison within VLM baselines. The experiment results reveal - extractive body cue:** 5 Conclusion & Future Work This paper emphasizes the significance of deploying Vision-Language-Action models on quadruped robots.
- **p. 14 / 1. Comparison within VLM baselines. The experiment results reveal - extractive body cue:** Future works will explore hardware acceleration techniques and model compression techniques to enable faster and more efficient execution of the models.

## Why Read It

VLA and generalist robot policies의 locomotion 문제를 이해하기 위해 읽는다. 본문은 However, such a task specification often relies on a single (coarse-grained) goal image instruction, making it difficult to apply in many real-world combination tasks, i.e. requiring combining multiple sub-instructions.를 문제로 두고, Our extensive evaluation shows that our approach leads to performant robotic policies and enables QUART to obtain a range of generalization capabilities.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 8 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
