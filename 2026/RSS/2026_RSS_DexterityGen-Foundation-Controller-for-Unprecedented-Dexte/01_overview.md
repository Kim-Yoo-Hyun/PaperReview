# DexterityGen: Foundation Controller for Unprecedented Dexterity

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://roboticsconference.org/2026/program/papers/103/.
> PDF retrieval source: https://roboticsconference.org/2026/program/papers/103/. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, dexterous manipulation, Reinforcement Learning, foundation controller, teleoperation, sim-to-real, tool use
- Official paper: https://roboticsconference.org/2026/program/papers/103/
- Full-text retrieval: https://roboticsconference.org/2026/program/papers/103/
- Code/Project: https://roboticsconference.org/2026/program/papers/103/
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 This limitation makes it difficult to prompt existing models to generate more detailed, finger-level interaction behaviors, such as using a syringe or screwdriver.를 문제로 두고, "Motivated by these observations, in this paper, we propose를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Teaching robots dexterous manipulation skill, such as tool use, presents a significant challenge.
- **p. 1 / Abstract - extractive body cue:** Current approaches ‘can be broadly categorized into two strategies: human teleoperation (for imitatic }-to-real_ reinforcement Tearing The fat approseh produce safe and dexterous motions on ...
- **p. 1 / Abstract - extractive body cue:** The second RL-based approach struggles with the domain gap and involves highly task-specifie reward enineering on complex tasks.
- **p. 1 / Abstract - extractive body cue:** Our key insight is that RIL is effective at learning low-level motion primitives, while humans excel providing coarse motion commands for complex, long-horizon tasks.
- **p. 1 / Abstract - extractive body cue:** Therefore, the optimal solution might be a combination of both approaches.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** This limitation makes it difficult to prompt existing models to generate more detailed, finger-level interaction behaviors, such as using a syringe or screwdriver.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** the significant domain gap between simulation and the real world, as well as the need for highly task-specific reward specifications when training an RL agent ...

## Core Idea

- **p. 2 / 1. INTRODUCTION - extractive body cue:** "Motivated by these observations, in this paper, we propose
- **p. 4 / III. THE DEXGEN CONTROLLER - extractive body cue:** We propose to pretrain a generative behavior model po(o/0) ‘on the simulation dataset to model prior action distribution so that it can generate stable and ...
- **p. 6 / C. DexGen Model Architecture - extractive body cue:** The above function encourages the generated future fingertip position to closely match the commanded fingertip position Since the action of the robot hand has a ...
- **p. 3 / 1. INTRODUCTION - extractive body cue:** Our approach effectively decouples high-level semantic motion generation from finegrained low-level control, serving as a foundational low-level dexterity controller.
- **p. 3 / 1. INTRODUCTION - extractive body cue:** novel training framework called DexterityGen (DexGen) to address the challenges of teaching dexterous in-hand manipulation skills.
- **p. 6 / C. DexGen Model Architecture - extractive body cue:** The inverse dynamics model is a simple residual multilayer perceptron that outputs a normal distribution to model the actions conditioned on the current robot state ...
- **p. 5 / C. DexGen Model Architecture - extractive body cue:** The first module is a diffusion model that characterizes the distribution of robot finger keypoint motions given current observations.
- **p. 6 / C. DexGen Model Architecture - extractive body cue:** The generated finger keypoint ‘movement is then converted to action by the inverse dynamics model.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The inverse dynamics model is a simple residual multilayer perceptron that outputs a normal distribution to model the actions conditioned on the current robot state and motion ‘command. | RGB-D/point cloud, object state와 contact/task observation | p. 6 (C. DexGen Model Architecture), p. 6 (C. DexGen Model Architecture) |
| State/latent | inverse, dynamics, model, simple, residual, multilayer, perceptron, outputs, normal, distribution, actions, conditioned | object geometry, affordance, contact mode 또는 end-effector state | p. 6 (C. DexGen Model Architecture), p. 6 (C. DexGen Model Architecture), p. 2 (1. INTRODUCTION) |
| Output/action | The above function encourages the generated future fingertip position to closely match the commanded fingertip position Since the action of the robot hand has a high degree of freedom (16 for the ... | grasp, pose, force 또는 end-effector trajectory | p. 6 (C. DexGen Model Architecture), p. 2 (1. INTRODUCTION), p. 3 (1. INTRODUCTION) |
| Objective/outcome | During inference, we can sample actions from this distribution and further aligned with extemal motion ‘commands using gradient guidance. | task completion, contact success, pose/force error와 generalization | p. 4 (III. THE DEXGEN CONTROLLER), p. 6 (C. DexGen Model Architecture), p. 6 (C. DexGen Model Architecture) |

## Main Claims and Actual Contribution

- **p. 2 / 1. INTRODUCTION - extractive body cue:** "Motivated by these observations, in this paper, we propose
- **p. 4 / III. THE DEXGEN CONTROLLER - extractive body cue:** We propose to pretrain a generative behavior model po(o/0) ‘on the simulation dataset to model prior action distribution so that it can generate stable and ...
- **p. 6 / C. DexGen Model Architecture - extractive body cue:** The above function encourages the generated future fingertip position to closely match the commanded fingertip position Since the action of the robot hand has a ...
- **p. 3 / 1. INTRODUCTION - extractive body cue:** Our approach effectively decouples high-level semantic motion generation from finegrained low-level control, serving as a foundational low-level dexterity controller.
- **p. 3 / 1. INTRODUCTION - extractive body cue:** novel training framework called DexterityGen (DexGen) to address the challenges of teaching dexterous in-hand manipulation skills.
- **p. 8 / B. Simulated Experiments - extractive body cue:** 4) Evaluation Protocol: We evaluate the performance of 1 teleoperation system by measuring the success rate a human user can achieve when using it to ...
- **p. 8 / B. Simulated Experiments - extractive body cue:** This explains why the user can achieve a much higher success rate in these dexterous tasks.
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** figure, DexGen can successfully improve the performance of these polici

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 8 (B. Simulated Experiments), p. 8 (B. Simulated Experiments) |
| Embodiment/environment | ‘We have demonstrated that our system can provide effective assistance through simulated validation. ‘Then, we further design several tasks for benchmarking in the real world. | hardware/simulator version and reset protocol | p. 7 (B. Simulated Experiments), p. 5 (B. Large-Scale Behavior Dataset Generation) |
| Dataset/benchmark | We collect a total of 1 x 10? transitions as our simulation dataset, equivalent to 31.7 years of real world experience. | role, split, size and leakage | p. 7 (B. Simulated Experiments), p. 5 (B. Large-Scale Behavior Dataset Generation), p. 5 (B. Large-Scale Behavior Dataset Generation), p. 8 (B. Simulated Experiments) |
| Metric | In the experiments, we first validate the effectiveness of DexGen through simulated experiments, demonstrating its ability to enhance the robustness and success rate of extremely suboptimal policies. | definition, denominator, direction and uncertainty | p. 6 (IV. EXPERIMENTS), p. 8 (B. Simulated Experiments), p. 8 (B. Simulated Experiments) |
| Baseline/ablation | Compared to the baseline, our system can successfully help the user to solve many tasks in various challenging setups. | fair input/data/compute/action matching | p. 8 (B. Simulated Experiments), p. 7 (IV. EXPERIMENTS), p. 7 (IV. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 7 / B. Simulated Experiments - extractive body cue:** We find that without our assistance, the noisy ‘expert has much more frequent failures.
- **p. 7 / B. Simulated Experiments - extractive body cue:** We record the average number of critical failures (drop the object) and the number of goal achievements within a certain time of different policies
- **p. 8 / B. Simulated Experiments - extractive body cue:** We report success rate (SR) and time-to-fall (ITF) / Holding Time metric which is normalized by the test episode length.
- **p. 8 / B. Simulated Experiments - extractive body cue:** The raw teleoperation baseline fails completely on those tasks, while our method can help the teleoperation policy to achieve both stability and success in diverse ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We introduce DexterityGen (DexGen) as a foundation controller that achieves unprecedented dexterous manipulation behavior with teleoperation. DexGen is a generative model that can ...
- **p. 5 / B. Large-Scale Behavior Dataset Generation - extractive body cue:** To enhance the robustness of our policy, we randomly adjust the wrist to different poses throughout the process, in addition to employing. commonly used domain ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** In the experiments, we first validate the effectiveness of DexGen through simulated experiments, demonstrating its ability to enhance the robustness and success rate of extremely ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 manipulation 문제를 이해하기 위해 읽는다. 본문은 This limitation makes it difficult to prompt existing models to generate more detailed, finger-level interaction behaviors, such as using a syringe or screwdriver.를 문제로 두고, "Motivated by these observations, in this paper, we propose를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 3 (1. INTRODUCTION), p. 5 (A. Preliminaries), p. 6 (C. DexGen Model Architecture) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (14 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** This limitation makes it difficult to prompt existing models to generate more detailed, finger-level interaction behaviors, such as using a syringe or screwdriver. (p. 2, 1. INTRODUCTION).
- **Actual contribution:** "Motivated by these observations, in this paper, we propose (p. 2, 1. INTRODUCTION).
- **Evaluation boundary:** figure, DexGen can successfully improve the performance of these polici (p. 7, IV. EXPERIMENTS).
- **Explicit failure boundary:** We find that without our assistance, the noisy ‘expert has much more frequent failures. (p. 7, B. Simulated Experiments).
