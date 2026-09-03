# RoboPack: Learning Tactile-Informed Dynamics Models for Dense Packing

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss20/p130.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss20/p130.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: CORE
- Tags: Robotics, contact-rich manipulation, tactile sensing, dynamics model
- Official paper: https://www.roboticsproceedings.org/rss20/p130.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss20/p130.pdf
- Code/Project: https://www.roboticsproceedings.org/rss20/p130.html
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 At the same time, tasks such as dense packing present significant challenges due to severe occlusions among objects, creating partially observable scenarios where vision alone is insufficient to determine the properties of ...를 문제로 두고, To tackle these challenges, in this work, we propose to 1) learn dynamics directly from real physical interaction data using powerful deep function approximators, 2) equip our robotic system with a compliant ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Tactile feedback is critical for understanding the dynamics of both rigid and deformable objects in many manipulation tasks, such as non-prehensile manipulation and dense packing.
- **p. 1 / Abstract - extractive body cue:** We introduce an approach that combines visual and tactile sensing for robotic manipulation by learning a neural, tactile-informed dynamics model.
- **p. 1 / Abstract - extractive body cue:** Our proposed framework, RoboPack, employs a recurrent graph neural network to estimate object states, including particles and object-level latent physics information, from historical visuo-tactile observations ...
- **p. 1 / Abstract - extractive body cue:** Our tactile-informed dynamics model, learned from real-world data, can solve downstream robotics tasks with model-predictive control.
- **p. 1 / Abstract - extractive body cue:** We demonstrate our approach on a real robot equipped with a compliant SoftBubble tactile sensor on non-prehensile manipulation and dense packing tasks, where the robot ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** At the same time, tasks such as dense packing present significant challenges due to severe occlusions among objects, creating partially observable scenarios where vision alone ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** These tasks involve multi-object interactions with complex dynamics that cannot be determined from vision alone.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** To tackle these challenges, in this work, we propose to 1) learn dynamics directly from real physical interaction data using powerful deep function approximators, 2) ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We find that our method can successfully leverage histories of visuo-tactile information to improve prediction, with models trained on just 30 minutes of real-world interaction ...
- **p. 4 / III. METHOD - extractive body cue:** For multi-object packing settings with significant occlusion, we introduce an objective that constrains tracked points to be near the corresponding object masks, providing more consistent ...
- **p. 5 / III. METHOD - extractive body cue:** In the following paragraphs, we describe how our method performs state estimation using history information and future prediction.
- **p. 5 / III. METHOD - extractive body cue:** For a training trajectory of length H, the state estimator estimates the first T states, and the dynamics predictor predicts all remaining states.
- **p. 4 / III. METHOD - extractive body cue:** State Estimation and Latent Physics Vector Inference In real-world robotic manipulation, visual observations are not always available due to occlusion, but knowledge about object dynamics ...
- **p. 4 / III. METHOD - extractive body cue:** F x, F y are the mean of local force vectors across spatial dimensions, and /Q/ is defined as /Q/ = r max i,j /qx ...
- **p. 5 / III. METHOD - extractive body cue:** Concretely, we use Model Predictive Path Integral (MPPI) to perform this optimization [58].

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | To formulate this problem, we define the observation space as O, the state space as S, and the action space as A. | tactile image/force, vision과 proprioceptive history | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| State/latent | formulate, problem, define, observation, space, state, action, Secondly, estimator, infers, object, states | contact geometry, force state 또는 latent dynamics | p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Output/action | Secondly, the state estimator g infers object states s from any prior interactions, which includes a single visual frame ovis 0 , the subsequent tactile observations otact 0:t , and the corresponding ... | grasp/contact action, force command 또는 object motion | p. 3 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD) |
| Objective/outcome | The objective is to find a sequence of actions a0, ..., aH-1 to minimize a cost function J between the final states and a given target state sg: (a0, ..., aH-1) = ... | slip/contact success, force/pose error와 robustness | p. 4 (III. METHOD), p. 5 (III. METHOD), p. 5 (III. METHOD) |

## Main Claims and Actual Contribution

- **p. 2 / I. INTRODUCTION - extractive body cue:** To tackle these challenges, in this work, we propose to 1) learn dynamics directly from real physical interaction data using powerful deep function approximators, 2) ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** We find that our method can successfully leverage histories of visuo-tactile information to improve prediction, with models trained on just 30 minutes of real-world interaction ...
- **p. 4 / III. METHOD - extractive body cue:** For multi-object packing settings with significant occlusion, we introduce an objective that constrains tracked points to be near the corresponding object masks, providing more consistent ...
- **p. 5 / III. METHOD - extractive body cue:** In the following paragraphs, we describe how our method performs state estimation using history information and future prediction.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Does integrating tactile sensing information from prior interactions improve future prediction accuracy? ii.
- **p. 9 / V. EXPERIMENTS - extractive body cue:** A trial is labeled as a success if it achieves an error lower than 0.02 for point-wise MSE within 10 pushes. histories than a certain ...
- **p. 9 / V. EXPERIMENTS - extractive body cue:** While the physics-based simulator achieves the strongest performance of the baselines, it is not able to achieve as precise control as our method, taking more ...
- **p. 10 / V. EXPERIMENTS - extractive body cue:** Method Seen Objects Unseen Objects RoboPack 12/15 10/15 RoboPack (no tactile) 6/15 5/15 TABLE III: Success rates on the dense packing task.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS) |
| Embodiment/environment | Benchmarking Real-World Planning Performance Next, we evaluate the performance of our approach in solving real-world robotic planning tasks. | hardware/simulator version and reset protocol | p. 9 (V. EXPERIMENTS), p. 6 (IV. EXPERIMENTAL SETUP) |
| Dataset/benchmark | The robot has access to tactile feedback at all steps but only visual observations in between pushes, which corresponds to the real-world feedback loop frequency. | role, split, size and leakage | p. 9 (V. EXPERIMENTS), p. 6 (IV. EXPERIMENTAL SETUP), p. 6 (IV. EXPERIMENTAL SETUP), p. 7 (V. EXPERIMENTS) |
| Metric | We report the minimum error to goal across 10 plan executions per trial, trial success rates, and number of execution steps to solve the task. | definition, denominator, direction and uncertainty | p. 9 (V. EXPERIMENTS), p. 10 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS) |
| Baseline/ablation | Fig. 6: Qualitative results on dynamics prediction. Pre- dictions made by our model compared to baseline methods in the Non-prehensile Box Pushing task. Red dots indicate the rod and blue dots represent ... | fair input/data/compute/action matching | p. 8 (Figure/Table caption), p. 8 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 6 / IV. EXPERIMENTAL SETUP - extractive body cue:** The test objects are more complex than the training set visually, geometrically, and physically, to showcase the generalizability of our model. yet the same visual ...
- **p. 7 / IV. EXPERIMENTAL SETUP - extractive body cue:** Each episode includes various attempts at packing an object into the box and includes pushing and deforming objects, as well as in-hand slipping of the ...
- **p. 8 / V. EXPERIMENTS - extractive body cue:** Metrics such as EMD and CD that emphasize global shape and distribution but are insensitive to subtle positional changes cannot differentiate the two methods in ...
- **p. 6 / IV. EXPERIMENTAL SETUP - extractive body cue:** Due to heavy occlusions during task execution, the robot does not have access to meaningful visual feedback during robot execution other than the initial frame, ...
- **p. 7 / IV. EXPERIMENTAL SETUP - extractive body cue:** Mathematically, the loss function is J (ˆot, og, at) = X x∈ˆot min y∈og //x -y//2 - X y∈og min x∈ˆot //x -y//2 + r ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Tactile sensing for dense packing. Tactile feedback is critical in tasks with heavy occlusion and rich contact, such as dense packing. (a) Humans ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 tactile 문제를 이해하기 위해 읽는다. 본문은 At the same time, tasks such as dense packing present significant challenges due to severe occlusions among objects, creating partially observable scenarios where vision alone is insufficient to determine the properties of ...를 문제로 두고, To tackle these challenges, in this work, we propose to 1) learn dynamics directly from real physical interaction data using powerful deep function approximators, 2) equip our robotic system with a compliant ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 5 (III. METHOD), p. 4 (III. METHOD) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** At the same time, tasks such as dense packing present significant challenges due to severe occlusions among objects, creating partially observable scenarios where vision alone is insufficient to determine the ... (p. 1, I. INTRODUCTION).
- **Actual contribution:** We find that our method can successfully leverage histories of visuo-tactile information to improve prediction, with models trained on just 30 minutes of real-world interaction data per task on average. (p. 2, I. INTRODUCTION).
- **Evaluation boundary:** 2.65 ± 0.18 4.11 ± 0.17 4.57 ± 0.16 Dense RoboPack 0.070 ± 0.005 1.12 ± 0.036 2.01 ± 0.050 Packing RoboPack (no tactile) 0.088 ± 0.006 1.18 ± 0.043 ... (p. 8, V. EXPERIMENTS).
- **Explicit failure boundary:** Due to heavy occlusions during task execution, the robot does not have access to meaningful visual feedback during robot execution other than the initial frame, but again tactile signals are ... (p. 6, IV. EXPERIMENTAL SETUP).
