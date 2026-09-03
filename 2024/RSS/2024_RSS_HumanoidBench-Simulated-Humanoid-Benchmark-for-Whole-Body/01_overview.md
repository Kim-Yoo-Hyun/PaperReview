# HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss20/p061.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss20/p061.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / RSS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: CORE
- Tags: Robotics, humanoid, Benchmark, whole-body control, loco-manipulation
- Official paper: https://www.roboticsproceedings.org/rss20/p061.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss20/p061.pdf
- Code/Project: https://humanoid-bench.github.io/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 benchmark 문제를 이해하기 위해 읽는다. 본문은 However, all these works focus fon demonstrating their approaches on specific humanoid tasks and lack a diversity of tasks.를 문제로 두고, To accelerate the progress of research for humanoid robots, We present the first-of-its-kind humanoid robot benchmark, HumanoidBench, with a diverse set of locomotion and manipulation tasks.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Humanoid robots hold great promise in assisting ‘humans in diverse environments and tasks, due to their flexibility and adaptability leveraging human-like morphology.
- **p. 1 / Abstract - extractive body cue:** However, research in humanoid robots is often bottlenecked by the costly and fragile hardware setups.
- **p. 1 / Abstract - extractive body cue:** To aecelerate algorithmic research in humanoid robots, we present a high-dimensional, simulated robot learning henchmark, HumanoidBench, featuring a humanoid robot equipped with dexterous hands and ...
- **p. 1 / Abstract - extractive body cue:** With HumanoidBench, we provide the robotics community with a platform to identify the challenges arising when solving diverse tasks with humanoid robots, facilitating prompt verification ...
- **p. 1 / Abstract - extractive body cue:** The open-source code is available at ‘hupst//humanold-bench.github.io.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, all these works focus fon demonstrating their approaches on specific humanoid tasks and lack a diversity of tasks.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, most of these benchmarks use a singlearm manipulation setup with either a parallel gripper or a dexterous hand [9, 49], limiting the types of ...

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** To accelerate the progress of research for humanoid robots, We present the first-of-its-kind humanoid robot benchmark, HumanoidBench, with a diverse set of locomotion and manipulation ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present extensive benchmarking results of the state-of-the-art reinforcement leaning (RL) algorithms, which do not require extensive domain knowledge, and a hierarchical ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** 4, 42, 29, 17, 30, 48] In the context of humanoids, we propose an HRL paradigm
- **p. 3 / I. INTRODUCTION - extractive body cue:** While this is not currently a realistic model, we anticipate the trend in the industry towards developing slimmer, human-like hhands (e-g., Tesla Optimus, Figure 01) ...
- **p. 4 / I. INTRODUCTION - extractive body cue:** Torque-based control is also supported but we found that position control is generally more stable and allows for lower control frequency than torque control.
- **p. 1 / Abstract - extractive body cue:** To aecelerate algorithmic research in humanoid robots, we present a high-dimensional, simulated robot learning henchmark, HumanoidBench, featuring a humanoid robot equipped with dexterous hands and ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** The benchmarking results on this task suite show how the state-ofthe-art RL algorithms struggle with controlling the complex humanoid robot dynamics and solving the most ...
- **p. 3 / I. INTRODUCTION - extractive body cue:** We use two dexterous Shadow Hands*, which also have model files freely available®, and have shown impressive manipulation capabilities both in simulation [67] and in ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | + Proprioceptive robot state (i, joint angles and velocities) and task-relevant environment observations (ie, object, poses and velocities) | standardized observation, action, task state와 evaluation split | p. 3 (I. INTRODUCTION), p. 3 (I. INTRODUCTION) |
| State/latent | Proprioceptive, robot, state, joint, angles, velocities, task-relevant, environment, observations, object, poses, Although | benchmark state/goal와 method decision | p. 3 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Output/action | Although other sensory inputs are available from the environment, to investigate challenges in whole-body control of humanoid robots, we first focus on the state-based environment setup, where proprioceptive robot states and object ... | policy/controller trajectory 또는 measured result | p. 3 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 1 (Abstract) |
| Objective/outcome | mns represent the standard deviation, Returns are computed by summing the rewards at all timesteps of an episode. | success metric, robustness, generalization과 reproducibility | p. 6 (IV. HuMANOIDBENcH), p. 1 (Abstract), p. 1 (I. INTRODUCTION) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** To accelerate the progress of research for humanoid robots, We present the first-of-its-kind humanoid robot benchmark, HumanoidBench, with a diverse set of locomotion and manipulation ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present extensive benchmarking results of the state-of-the-art reinforcement leaning (RL) algorithms, which do not require extensive domain knowledge, and a hierarchical ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** 4, 42, 29, 17, 30, 48] In the context of humanoids, we propose an HRL paradigm
- **p. 3 / I. INTRODUCTION - extractive body cue:** While this is not currently a realistic model, we anticipate the trend in the industry towards developing slimmer, human-like hhands (e-g., Tesla Optimus, Figure 01) ...
- **p. 4 / I. INTRODUCTION - extractive body cue:** Torque-based control is also supported but we found that position control is generally more stable and allows for lower control frequency than torque control.
- **p. 9 / B. Results - extractive body cue:** In Figure 9, our hierarchical architecture significantly outperforms the flat, end-to-end baselines on the push task, achieving very high success rates ‘with DreamerV3.
- **p. 9 / B. Results - extractive body cue:** On the other hand, we note a less pronounced performance improvement in the more challenging package task.
- **p. 8 / B. Results - extractive body cue:** The results in Figure 7 show that the presence of hands, with their additional joints and actuators, leads to a large decrease in performance ‘compared ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 9 (B. Results), p. 9 (B. Results) |
| Embodiment/environment | To identify the challenges in learning with humanoid robots, we benchmark reinforcement learning (RL) algorithms on HumanoidBench, which promises for robots to learn from | hardware/simulator version and reset protocol | p. 7 (V. BENCHMARKING RESULTS), p. 8 (B. Results) |
| Dataset/benchmark | Remarkably, this class of algorithms requires limited domain expertise and does not necessarily rely fon expert demonstrations, which are not only expensive but also challenging to collect for humanoid robots." | role, split, size and leakage | p. 7 (V. BENCHMARKING RESULTS), p. 8 (B. Results), p. 7 (V. BENCHMARKING RESULTS), p. 9 (B. Results) |
| Metric | We only run PPO on a subset of tasks (walk, kitchen, door, package), given its inferior performance without massive parallelization, Each of the environments is evaluated with a combination of dense rewards ... | definition, denominator, direction and uncertainty | p. 8 (B. Results), p. 9 (B. Results), p. 7 (Figure/Table caption) |
| Baseline/ablation | In Figure 9, our hierarchical architecture significantly outperforms the flat, end-to-end baselines on the push task, achieving very high success rates ‘with DreamerV3. | fair input/data/compute/action matching | p. 9 (B. Results), p. 8 (B. Results), p. 8 (B. Results) |

## Explicit Limitations and Failure Boundary

- **p. 9 / B. Results - extractive body cue:** In this subsection, we remark on notable challenges and com- ‘mon failures for some representative tasks in our benchmark, which denote the challenge in learning ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 10: Failure Scenarios. This figure presents a selection of common failures that occur while training our benchmark tasks.
- **p. 9 / B. Results - extractive body cue:** For low-level reaching policy training, we employ a simplified Hi model that only considers collisions between feet and ground in the MuJoCo MIX environments, as ...
- **p. 7 / V. BENCHMARKING RESULTS - extractive body cue:** Remarkably, this class of algorithms requires limited domain expertise and does not necessarily rely fon expert demonstrations, which are not only expensive but also challenging ...
- **p. 8 / B. Results - extractive body cue:** training with a lange action space (ie., additional 42 dimensions with two dexterous Shadow Hands) on walk that does not necessarily require to control dexterous ...
- **p. 8 / B. Results - extractive body cue:** Although the hands of the ‘humanoid robot are barely used for most locomotion tasks, the RL algorithms fail to ignore this information, which makes policy ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 benchmark 문제를 이해하기 위해 읽는다. 본문은 However, all these works focus fon demonstrating their approaches on specific humanoid tasks and lack a diversity of tasks.를 문제로 두고, To accelerate the progress of research for humanoid robots, We present the first-of-its-kind humanoid robot benchmark, HumanoidBench, with a diverse set of locomotion and manipulation tasks.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 4 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (1 pages; pdftotext fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, research in humanoid robots is often bottlenecked by the To accelerate the progress of research for humanoid robots, costly and fragile hardware setups. (p. 1, Abstract).
- **Actual contribution:** [3] Firas Al-Hafez, Guoping Zhao, Jan Peters, and Davide We presented HumanoidBench, a high-dimensional hu- Tateo. (p. 1, V. B ENCHMARKING R ESULTS).
- **Evaluation boundary:** The results in combination of dense rewards and sparse subtask completion Figure 7 show that the presence of hands, with their additional rewards, and for each of these we provide ... (p. 1, V. B ENCHMARKING R ESULTS).
- **Explicit failure boundary:** Mobility Fellowship 211086, ONR MURI N00014-22-1-2773, Common Failure on door. (p. 1, V. B ENCHMARKING R ESULTS).
