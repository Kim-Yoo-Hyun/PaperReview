# Evaluation - ANYmal Parkour: Learning Agile Navigation for Quadrupedal Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2306.14874; PDF retrieval source: https://arxiv.org/pdf/2306.14874. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 4 (Figure/Table caption)): Fig. 4: Training scenarios of the locomotion skills with the resulting behaviors. (A) Jumping. (B) Climbing down. (C) Climbing up. (D) Crouching. (E) Walking. (F) Success rate of each skill ...

## Evaluation Body Digest

- **p. 5 / II. RESULTS - extractive body cue:** The three learning-based modules operate together without expert demonstration, offline computation, or a priori knowledge of the environment and enable the robot to reliably reach ...
- **p. 5 / II. RESULTS - extractive body cue:** In trajectory B, the policy saturates the motor during the climb to propel the robot onto the 0.9 m high platform (Fig.
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 4: Training scenarios of the locomotion skills with the resulting behaviors. (A) Jumping. (B) Climbing down. (C) Climbing up. (D) Crouching. (E) Walking. (F) ...
- **p. 5 / II. RESULTS - extractive body cue:** The locomotion and navigation modules operate synchronously in a single node on the onboard computer.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Description of our approach. We decompose the problem into three components: The perception module receives the point cloud measurements to estimate the scene's ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 6: Terrain reconstructions for different scenarios (real-world data). The first column shows the point cloud measurements, the second the baseline elevation map [37] viewed ...
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 7: Types of environments used for training. The dimensions of the individual obstacles and the arrangements are randomized. for a broader view of the ...
- **p. 12 / A. Current Limitations - extractive body cue:** Finally, since the navigation module must make a series of correct decisions to reach the goal with many possibilities leading to failure, the algorithm requires ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** legged robot, terrain과 contact dynamics.
- **Input boundary:** proprioception, terrain/perception observation과 velocity command.
- **Output/decision under evaluation:** joint target, torque, footstep 또는 locomotion action.
- **Primary target:** velocity/progress, stability, energy와 terrain generalization.
- **Detected evaluation headings:** II. RESULTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Fig. 4: Training scenarios of the locomotion skills with the resulting behaviors. (A) Jumping. (B) Climbing down. (C) Climbing up. (D) Crouching. (E) Walking. ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Fig. 2: Description of our approach. We decompose the problem into three components: The perception module receives the point cloud measurements to estimate the ... | p. 4 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / II. RESULTS - extractive body cue:** The three learning-based modules operate together without expert demonstration, offline computation, or a priori knowledge of the environment and enable the robot to reliably reach ...
- **p. 5 / II. RESULTS - extractive body cue:** In trajectory B, the policy saturates the motor during the climb to propel the robot onto the 0.9 m high platform (Fig.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: Deployment of the pipeline on the quadrupedal robot ANYmal D. The robot performs highly dynamic maneuvers and makes contacts with its limbs where ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: Description of our approach. We decompose the problem into three components: The perception module receives the point cloud measurements to estimate the scene's ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3: Deployment of the pipeline on the robot ANYmal D. (A) Trajectory on the real robot. (B) Trajectory in simulation. (A1)- (A3) and (B1)-(B3) ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 4: Training scenarios of the locomotion skills with the resulting behaviors. (A) Jumping. (B) Climbing down. (C) Climbing up. (D) Crouching. (E) Walking. (F) ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 5: Adaptive path selection. The robot starts on the ground and is given a target on top of the box in the back, and ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 6: Terrain reconstructions for different scenarios (real-world data). The first column shows the point cloud measurements, the second the baseline elevation map [37] viewed ...
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 7: Types of environments used for training. The dimensions of the individual obstacles and the arrangements are randomized. for a broader view of the ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The three learning-based modules operate together without expert demonstration, offline computation, or a priori knowledge of the environment and enable the robot to reliably ... | embodiment, simulator version and control stack | p. 5 (II. RESULTS), p. 5 (II. RESULTS) |
| Task/environment | In trajectory B, the policy saturates the motor during the climb to propel the robot onto the 0.9 m high platform (Fig. | reset, timeout, object/scene variation | p. 5 (II. RESULTS) |
| Observation/sensor | proprioception, terrain/perception observation과 velocity command | calibration, preprocessing, privileged input | p. 14 (IV. MATERIALS AND METHODS), p. 5 (3) We develop a neural terrain reconstruction method that) |
| Output/decision | joint target, torque, footstep 또는 locomotion action | action frame, controller and termination | p. 12 (IV. MATERIALS AND METHODS), p. 12 (IV. MATERIALS AND METHODS) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 4: Training scenarios of the locomotion skills with the resulting behaviors. (A) Jumping. (B) Climbing down. (C) Climbing up. (D) Crouching. (E) Walking. ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| The locomotion and navigation modules operate synchronously in a single node on the onboard computer. | definition/direction/unit from same section | p. 5 (II. RESULTS) |
| In trajectory B, the policy saturates the motor during the climb to propel the robot onto the 0.9 m high platform (Fig. | definition/direction/unit from same section | p. 5 (II. RESULTS) |
| Fig. 2: Description of our approach. We decompose the problem into three components: The perception module receives the point cloud measurements to estimate the ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Fig. 6: Terrain reconstructions for different scenarios (real-world data). The first column shows the point cloud measurements, the second the baseline elevation map [37] ... | definition/direction/unit from same section | p. 11 (Figure/Table caption) |
| Fig. 7: Types of environments used for training. The dimensions of the individual obstacles and the arrangements are randomized. for a broader view of ... | definition/direction/unit from same section | p. 13 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The skill learns to turn on the spot in tight spaces and is more capable in such scenarios compared to other skills. | comparison identity and matched condition | p. 5 (II. RESULTS) |
| Fig. 6: Terrain reconstructions for different scenarios (real-world data). The first column shows the point cloud measurements, the second the baseline elevation map [37] ... | comparison identity and matched condition | p. 11 (Figure/Table caption) |
| The three learning-based modules operate together without expert demonstration, offline computation, or a priori knowledge of the environment and enable the robot to reliably ... | comparison identity and matched condition | p. 5 (II. RESULTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The three learning-based modules operate together without expert demonstration, offline computation, or a priori knowledge of the environment and enable the robot to reliably ... | component/input/data sensitivity | p. 5 (II. RESULTS) |
| Fig. 2: Description of our approach. We decompose the problem into three components: The perception module receives the point cloud measurements to estimate the ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Despite the promising results and the close similarity to our method, this work requires human-designed path and skill selection and is limited to a ... | Fig. 4: Training scenarios of the locomotion skills with the resulting behaviors. (A) Jumping. (B) Climbing down. (C) Climbing up. (D) Crouching. (E) Walking. ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 4 (Figure/Table caption) |
| Primary metric/result | Fig. 2: Description of our approach. We decompose the problem into three components: The perception module receives the point cloud measurements to estimate the ... | numeric claim only at cited anchor | p. 4 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 14 / IV. MATERIALS AND METHODS - extractive body cue:** scale well with the reinforcement learning set-up with 4000 robots.
- **p. 14 / IV. MATERIALS AND METHODS - extractive body cue:** We train these networks in an unsupervised fashion from simulated data on a total of 2000 trajectories with 100 timesteps each.
- **p. 14 / IV. MATERIALS AND METHODS - extractive body cue:** 2) Locomotion Module: The locomotion module is an interface that exposes the low-level skills to the rest of the pipeline and operates at 50 Hz.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Finally, since the navigation module must make a series of correct decisions to reach the goal with many possibilities leading to failure, the algorithm ... | p. 12 (A. Current Limitations) |
| body limitation/failure cue | We develop a specific curriculum to overcome this limitation. | p. 12 (A. Current Limitations) |
| body limitation/failure cue | 3 (A2)), which is necessary for the leg to reach the other side of the gap and catch the fall of the robot during ... | p. 5 (II. RESULTS) |
| body limitation/failure cue | At this location, it has to perform precise foothold placement to pass the last step and prepare for the jump, despite the out-of-distribution scenario ... | p. 5 (II. RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Surprisingly, the dense formulation can handle such a large batch size with sufficient speeds but this comes at the cost of high memory requirements ... | p. 14 (IV. MATERIALS AND METHODS) |
| However, the plan is computed offline, the switch to the jumping controller is hard-coded, and the system can only overcome obstacles of 0.1 m ... | p. 4 (3) We develop a neural terrain reconstruction method that) |
| We also modify the network architecture to allow for efficient inference with large batch sizes during RL training. | p. 3 (3) We develop a neural terrain reconstruction method that) |
| In parallel, bipedal robots have also demonstrated their agile capabilities by walking blindly on rough terrain [20] and jumping on obstacles [21]. b) Navigation ... | p. 3 (3) We develop a neural terrain reconstruction method that) |
| The whole system is implemented in several ROS nodes across different onboard computers. | p. 5 (II. RESULTS) |
| The locomotion and navigation modules operate synchronously in a single node on the onboard computer. | p. 5 (II. RESULTS) |
| To overcome these challenges, we opt for a data-driven method with an encoder-decoder architecture inspired by [3]. | p. 12 (IV. MATERIALS AND METHODS) |
| Supplementary sections S1 and S2 define the observations, actions, and rewards of the locomotion and navigation policies and provide further implementation details. | p. 12 (IV. MATERIALS AND METHODS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 12 / A. Current Limitations - extractive body cue:** Finally, since the navigation module must make a series of correct decisions to reach the goal with many possibilities leading to failure, the algorithm requires ...
- **p. 12 / A. Current Limitations - extractive body cue:** We develop a specific curriculum to overcome this limitation.
- **p. 5 / II. RESULTS - extractive body cue:** 3 (A2)), which is necessary for the leg to reach the other side of the gap and catch the fall of the robot during the ...
- **p. 5 / II. RESULTS - extractive body cue:** At this location, it has to perform precise foothold placement to pass the last step and prepare for the jump, despite the out-of-distribution scenario for ...

- **PDF anchors reviewed:** datasets p. 5 (II. RESULTS), p. 5 (II. RESULTS), metrics p. 8 (Figure/Table caption), p. 5 (II. RESULTS), p. 5 (II. RESULTS), p. 4 (Figure/Table caption), p. 11 (Figure/Table caption), p. 13 (Figure/Table caption), baselines p. 5 (II. RESULTS), p. 11 (Figure/Table caption), p. 5 (II. RESULTS), results p. 8 (Figure/Table caption), p. 4 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
