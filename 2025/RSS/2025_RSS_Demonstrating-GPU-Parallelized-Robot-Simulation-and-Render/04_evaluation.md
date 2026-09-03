# Evaluation - Demonstrating GPU Parallelized Robot Simulation and Rendering for Generalizable Embodied AI with ManiSkill3

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (30 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p021.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p021.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 18 (Figure/Table caption), p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), p. 22 (Figure/Table caption), p. 4 (Figure/Table caption)): Fig. 25: Evaluated success rates of generalist robotics models like Octo and RT-IX on 4 different tasks. The correlation and MMRV metrics are close to that of the original paper. ...

## Evaluation Body Digest

- **p. 3 / 5) Scalable Dataset Generation Pipeline from Few - extractive body cue:** DROID [28] addresses some of OpenX's problems by using a consistant data collection platform, However, both Open-X and DROID require immense amounts ‘of human labor ...
- **p. 2 / 5) Scalable Dataset Generation Pipeline from Few - extractive body cue:** OpenX [14] is one of the largest real-world roboties datasets but
- **p. 2 / 5) Scalable Dataset Generation Pipeline from Few - extractive body cue:** Robotics Datasets: Amongst existing datasets there are typically two kinds, real-world and simulated datasets.
- **p. 3 / 5) Scalable Dataset Generation Pipeline from Few - extractive body cue:** Concretely we categorize the 12 distinct categories as follows: Table top manipulation, mobile manipulation, room-scale scenes for manipulation, quadruped/humanoid locomotion, humanoid/bi-manual ‘manipulation, multi-agent robotics, draw ...
- **p. 7 / IV. BASELINES AND RESULTS - extractive body cue:** ManiSkill3 provides several popular robot learning. baselines as well as simple reproducible setups for end-to-end trainable vision-based sim2real policies.
- **p. 18 / Figure/Table caption - extractive body cue:** Fig. 25: Evaluated success rates of generalist robotics models like Octo and RT-IX on 4 different tasks. The correlation and MMRV metrics are close to ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 13: Koch pick-cube sim and real success rates on the grasp cube subtask as well as the full success consisting of grasping, lifting, and ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 11: Wall-clock training time of PPO on GPU/CPU sim- ulation showing the average success rate over time across 5 seeds. Shaded areas correspond to ...

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** defined robot simulator/hardware task suite.
- **Input boundary:** standardized observation, action, task state와 evaluation split.
- **Output/decision under evaluation:** policy/controller trajectory 또는 measured result.
- **Primary target:** success metric, robustness, generalization과 reproducibility.
- **Detected evaluation headings:** 5) Scalable Dataset Generation Pipeline from Few (p. 2); IV. BASELINES AND RESULTS (p. 7); B. Simulation Only Benchmark Results (p. 24); C. Simulation+Rendering Benchmark Results (p. 24).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | BENCHMARK / DATASET | Fig. 25: Evaluated success rates of generalist robotics models like Octo and RT-IX on 4 different tasks. The correlation and MMRV metrics are close ... | p. 18 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Fig. 11: Wall-clock training time of PPO on GPU/CPU sim- ulation showing the average success rate over time across 5 seeds. Shaded areas correspond ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Fig. 13: Koch pick-cube sim and real success rates on the grasp cube subtask as well as the full success consisting of grasping, lifting, ... | p. 9 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Fig. 27: Success rate curves of PerAct over 80k training steps ‘on PushCube-v1 and StackCube-v1 | p. 22 (Figure/Table caption) |
| Figure/Table caption | BENCHMARK / DATASET | Fig. 2: GPU Simulation+Rendering of RGB speeds of the Cartpole environment with different camera setups ManiSkill3 and Isaac Lab. Annotated numbers indicate GPU memory ... | p. 4 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 3 / 5) Scalable Dataset Generation Pipeline from Few - extractive body cue:** DROID [28] addresses some of OpenX's problems by using a consistant data collection platform, However, both Open-X and DROID require immense amounts ‘of human labor ...
- **p. 2 / 5) Scalable Dataset Generation Pipeline from Few - extractive body cue:** OpenX [14] is one of the largest real-world roboties datasets but
- **p. 2 / 5) Scalable Dataset Generation Pipeline from Few - extractive body cue:** Robotics Datasets: Amongst existing datasets there are typically two kinds, real-world and simulated datasets.
- **p. 3 / 5) Scalable Dataset Generation Pipeline from Few - extractive body cue:** Concretely we categorize the 12 distinct categories as follows: Table top manipulation, mobile manipulation, room-scale scenes for manipulation, quadruped/humanoid locomotion, humanoid/bi-manual ‘manipulation, multi-agent robotics, draw ...
- **p. 7 / IV. BASELINES AND RESULTS - extractive body cue:** ManiSkill3 provides several popular robot learning. baselines as well as simple reproducible setups for end-to-end trainable vision-based sim2real policies.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: Multiple distinct task categories are displayed, ranging from room-scale tasks to humanoid interactions and drawing tasks, Majority of tasks shown are GPU-parallelized, simulating ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: GPU Simulation+Rendering of RGB speeds of the Cartpole environment with different camera setups ManiSkill3 and Isaac Lab. Annotated numbers indicate GPU memory usage, ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: GPU Simulation+Rendering speeds of various tasks with a single 128x128 resolution camera with a simulation frequency of 120 and control frequency of 60, ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5: Parallel rendering outputs of 1024 parallel environ- ments for the StackCube and PushT tasks with a subset of 4 them visualized here. Original ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 6: Example tasks in ManiSkill3 showing heterogeneous GPU simulation with different DoF articulations and/or dif- ferent numbers of objects being simulated in each parallel ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 7: Visualization of VR teleoperation system. Left: A teleoperator using hand poses captured by the Meta Quest 3 headset to control robot motion in ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 8: Three different kinds of digital twins in ManiSkill3. Top row shows the real-world setup and bottom row shows the digital twin, Left: Domain ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 9: Code comparison for computing a grasp position on a cabinet handle and the joint angle of the cabinet drawer in 3

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | DROID [28] addresses some of OpenX's problems by using a consistant data collection platform, However, both Open-X and DROID require immense amounts ‘of human ... | embodiment, simulator version and control stack | p. 3 (5) Scalable Dataset Generation Pipeline from Few), p. 2 (5) Scalable Dataset Generation Pipeline from Few) |
| Task/environment | OpenX [14] is one of the largest real-world roboties datasets but | reset, timeout, object/scene variation | p. 2 (5) Scalable Dataset Generation Pipeline from Few), p. 2 (5) Scalable Dataset Generation Pipeline from Few) |
| Observation/sensor | standardized observation, action, task state와 evaluation split | calibration, preprocessing, privileged input | p. 8 (A. Reinforcement Learning), p. 8 (A. Reinforcement Learning) |
| Output/decision | policy/controller trajectory 또는 measured result | action frame, controller and termination | p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 25: Evaluated success rates of generalist robotics models like Octo and RT-IX on 4 different tasks. The correlation and MMRV metrics are close ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| Fig. 13: Koch pick-cube sim and real success rates on the grasp cube subtask as well as the full success consisting of grasping, lifting, ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Fig. 11: Wall-clock training time of PPO on GPU/CPU sim- ulation showing the average success rate over time across 5 seeds. Shaded areas correspond ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Fig. 27: Success rate curves of PerAct over 80k training steps ‘on PushCube-v1 and StackCube-v1 | definition/direction/unit from same section | p. 22 (Figure/Table caption) |
| For easier tasks, motion planning and rewards for RL are used to generate demonstrations. | definition/direction/unit from same section | p. 3 (5) Scalable Dataset Generation Pipeline from Few) |
| Demonstrations: For tasks in ManiSkill3 where reward design is difficult, we provide a pipeline that leverages demonstration | definition/direction/unit from same section | p. 2 (5) Scalable Dataset Generation Pipeline from Few) |
| For more complex tasks without easily defined motion planning scripts or reward functions, ManiSkill3 relies on ‘online learning from demonstrations algorithms like RLPD [2] ... | definition/direction/unit from same section | p. 3 (5) Scalable Dataset Generation Pipeline from Few) |
| Fig. 2: GPU Simulation+Rendering of RGB speeds of the Cartpole environment with different camera setups ManiSkill3 and Isaac Lab. Annotated numbers indicate GPU memory ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| ManiSkill3 provides several popular robot learning. baselines as well as simple reproducible setups for end-to-end trainable vision-based sim2real policies. | comparison identity and matched condition | p. 7 (IV. BASELINES AND RESULTS) |
| For more complex tasks without easily defined motion planning scripts or reward functions, ManiSkill3 relies on ‘online learning from demonstrations algorithms like RLPD [2] ... | comparison identity and matched condition | p. 3 (5) Scalable Dataset Generation Pipeline from Few) |
| Note that the environments and baselines leveraging the fast parallel rendering in ManiSkill3 is concurrent work to Isaac Lab. | comparison identity and matched condition | p. 2 (5) Scalable Dataset Generation Pipeline from Few) |
| Fig. 1: Multiple distinct task categories are displayed, ranging from room-scale tasks to humanoid interactions and drawing tasks, Majority of tasks shown are GPU-parallelized, ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| ManiSkill3 is the most feature-rich GPU simulation frame- ‘work compared to popular alternatives as shown in Table I. | comparison identity and matched condition | p. 3 (5) Scalable Dataset Generation Pipeline from Few) |
| Fig. 10: Code comparison for manipulating batched poses | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| For more complex tasks without easily defined motion planning scripts or reward functions, ManiSkill3 relies on ‘online learning from demonstrations algorithms like RLPD [2] ... | component/input/data sensitivity | p. 3 (5) Scalable Dataset Generation Pipeline from Few) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We propose ManiSkill3 to address past imitations and open source the framework under the Apache-2.0 license, building upon past work in ManiSkill 1 and ... | Fig. 25: Evaluated success rates of generalist robotics models like Octo and RT-IX on 4 different tasks. The correlation and MMRV metrics are close ... | PDF body cue; verify exact table/figure and matched conditions | p. 18 (Figure/Table caption), p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), p. 22 (Figure/Table caption), p. 4 (Figure/Table caption) |
| Primary metric/result | Fig. 11: Wall-clock training time of PPO on GPU/CPU sim- ulation showing the average success rate over time across 5 seeds. Shaded areas correspond ... | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 1 / Abstract - extractive body cue:** GPU Simulation with rendering on ManiSkiI3 uses 2-3x less GPU memory usage than other platforms and achieves up to 30,000+ FPS in benchmarked environments due ...
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Importantly ManiSkill3 maintains extremely low GPU memory usage, typically 2-3x lower than that of other simulators which enables on device visual RL and larger neural ...
- **p. 4 / B. GPU Parallelized Simulation and Rendering - extractive body cue:** ManiSkill3 digital twins can evaluate models like Octo at 60x to 100s the speed of the real world without human supervision, approximately 10x faster than ...
- **p. 5 / C. Heterogeneous GPU Simulation - extractive body cue:** At the same time, the system streams 4K stereo video via Air Light VR (ALVR) to the VR device at 60 Hz, ensuring a smooth ...
- **p. 5 / C. Heterogeneous GPU Simulation - extractive body cue:** Middle: A 360degree scene displayed in the VR device, providing immersive sensory feedback.
- **p. 6 / C. Heterogeneous GPU Simulation - extractive body cue:** Finally, for the real2sim digital twins we evaluate Octo and RT-1X on the ManiSkill3 GPU parallelized version of 4 tasks in SIMPLER [31].

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This enables flexibility in trajectory replay as data collected on one machine with more GPU memory can be replayed on other machines with less ... | p. 6 (C. Heterogeneous GPU Simulation) |
| body limitation/failure cue | Fig. 18: Comparison of the visual and collision mesh of one of the robot quadruped models, AnyMAL-C. | p. 16 (Figure/Table caption) |
| body limitation/failure cue | Brax/Mujoco uses the MJX backend and currently does not have parallel rendering. | p. 2 (5) Scalable Dataset Generation Pipeline from Few) |
| body limitation/failure cue | We also support evaluating (but not training) several vision-language action (VLA) models, namely Octo [40], RT-X [14], and RDT-IB [32 We leave to future ... | p. 7 (A. Reinforcement Learning) |
| body limitation/failure cue | During simulation training and real-world evaluation, observations are restricted to RGB inputs and robot joint positions; ‘no demonstrations or privileged state information such as ... | p. 8 (A. Reinforcement Learning) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 11: Wall-clock training time of PPO on GPU/CPU simulation showing the average success rate over time across 5 seeds. | p. 8 (A. Reinforcement Learning) |
| Importantly we support collecting data in CPU/GPU simulation and replaying them in CPU/GPU simulation with different numbers of parallel environments via explicit control over ... | p. 6 (C. Heterogeneous GPU Simulation) |
| We run experiments using PPO [44] on the ManiSkill3 GPU simulation and the ManiSkill2 CPU simulation, ManiSkill2 was previously the fastest robotics simulation+rendering, framework ... | p. 8 (A. Reinforcement Learning) |
| RL replay buffers or larger neural network models such as large vision language action models. ‘Training and inference can be kept extremely optimized on ... | p. 3 (B. GPU Parallelized Simulation and Rendering) |
| 4: GPU Simulation+Rendering speeds of various tasks with a single 128x128 resolution camera with a simulation frequency of 120 and control frequency of 60, ... | p. 4 (B. GPU Parallelized Simulation and Rendering) |
| We further adapt the trajectory replay tool from ManiSkill2 to work with both CPU and GPU simulated demonstration data, The replay tool enables users ... | p. 6 (C. Heterogeneous GPU Simulation) |
| GPU parallelized simulation makes data incredibly cheap to generate. | p. 1 (1. INTRODUCTION) |
| Simulation has enabled unprecedented compute ‘approaches to robot learning. | p. 1 (Abstract) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / C. Heterogeneous GPU Simulation - extractive body cue:** This enables flexibility in trajectory replay as data collected on one machine with more GPU memory can be replayed on other machines with less GPU ...
- **p. 16 / Figure/Table caption - extractive body cue:** Fig. 18: Comparison of the visual and collision mesh of one of the robot quadruped models, AnyMAL-C.
- **p. 2 / 5) Scalable Dataset Generation Pipeline from Few - extractive body cue:** Brax/Mujoco uses the MJX backend and currently does not have parallel rendering.
- **p. 7 / A. Reinforcement Learning - extractive body cue:** We also support evaluating (but not training) several vision-language action (VLA) models, namely Octo [40], RT-X [14], and RDT-IB [32 We leave to future work ...
- **p. 8 / A. Reinforcement Learning - extractive body cue:** During simulation training and real-world evaluation, observations are restricted to RGB inputs and robot joint positions; ‘no demonstrations or privileged state information such as cube ...

- **Evidence anchors reviewed:** datasets p. 3 (5) Scalable Dataset Generation Pipeline from Few), p. 2 (5) Scalable Dataset Generation Pipeline from Few), p. 2 (5) Scalable Dataset Generation Pipeline from Few), p. 3 (5) Scalable Dataset Generation Pipeline from Few), p. 7 (IV. BASELINES AND RESULTS), metrics p. 18 (Figure/Table caption), p. 9 (Figure/Table caption), p. 8 (Figure/Table caption), p. 22 (Figure/Table caption), p. 3 (5) Scalable Dataset Generation Pipeline from Few), p. 2 (5) Scalable Dataset Generation Pipeline from Few), baselines p. 7 (IV. BASELINES AND RESULTS), p. 3 (5) Scalable Dataset Generation Pipeline from Few), p. 2 (5) Scalable Dataset Generation Pipeline from Few), p. 2 (Figure/Table caption), p. 3 (5) Scalable Dataset Generation Pipeline from Few), p. 7 (Figure/Table caption), results p. 18 (Figure/Table caption), p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), p. 22 (Figure/Table caption), p. 4 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (30 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** ManiSkill3 provides several popular robot learning. baselines as well as simple reproducible setups for end-to-end trainable vision-based sim2real policies. (p. 7, IV. BASELINES AND RESULTS).
- **Metric evidence:** Fig. 13: Koch pick-cube sim and real success rates on the grasp cube subtask as well as the full success consisting of grasping, lifting, and return the cube to a ... (p. 9, Figure/Table caption).
- **Baseline/ablation evidence:** ManiSkill3 provides several popular robot learning. baselines as well as simple reproducible setups for end-to-end trainable vision-based sim2real policies. (p. 7, IV. BASELINES AND RESULTS).
- **Failure/negative evidence:** Implementation Details: We further make several modifications to ReplicaCAD to make it completely interactive as some of the collision meshes for articulations were modelled incorrectly and thus did not support ... (p. 16, C. Room Scale Environments).
