# Evaluation - Rapid Locomotion via Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss18/p022.html; PDF retrieval source: https://arxiv.org/pdf/2205.02824. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (IV. RESULTS), p. 6 (IV. RESULTS), p. 7 (IV. RESULTS), p. 7 (IV. RESULTS), p. 5 (Figure/Table caption)): The performance of the system is improved substantially by implementing the Box Curriculum.

## Evaluation Body Digest

- **p. 6 / IV. RESULTS - extractive PDF cue:** The maximum attainable speed is intimately tied to the robot's hardware properties, such as its weight, motor strength, and leg length.
- **p. 7 / IV. RESULTS - extractive PDF cue:** Response to Terrain Changes and Hardware Failures We tested our system in a diverse set of challenging real-world scenarios: (1) ascending a steep incline made ...
- **p. 2 / II. EXPERIMENTAL SETUP - extractive PDF cue:** The robot stands 30 cm tall and weighs 9 kg.
- **p. 2 / II. EXPERIMENTAL SETUP - extractive PDF cue:** Hardware: We use the MIT Mini Cheetah [20] as our experimental platform.
- **p. 6 / IV. RESULTS - extractive PDF cue:** On the other hand, some aspects of the real-world dynamics are probably not captured under any configuration of the simulator.
- **p. 7 / IV. RESULTS - extractive PDF cue:** The privileged teacher πT trained with access to environment parameters attains a strictly larger command area than the policy πDR trained with only the robot ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 3: (a) Forward and angular velocity tracking performance. The Grid Adaptive curriculum tracks a larger range of velocities than the Box Adaptive curriculum for ...
- **p. 5 / IV. RESULTS - extractive PDF cue:** Curriculum Learning Enables High-Speed Locomotion Figure 3(a) visualizes the tracking error (see Section III-E) of the policies learned from the three command sampling strategies as ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** legged robot, terrain과 contact dynamics.
- **Input boundary:** proprioception, terrain/perception observation과 velocity command.
- **Output/decision under evaluation:** joint target, torque, footstep 또는 locomotion action.
- **Primary target:** velocity/progress, stability, energy와 terrain generalization.
- **Detected evaluation headings:** II. EXPERIMENTAL SETUP (p. 2); IV. RESULTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| IV. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The performance of the system is improved substantially by implementing the Box Curriculum. | p. 6 (IV. RESULTS) |
| IV. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Using the Grid Curriculum, the performance of the policy further improves, as evidenced by the larger command area. | p. 6 (IV. RESULTS) |
| IV. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | In contrast, a single policy achieved all indoor and outdoor running and spinning results in our work. | p. 7 (IV. RESULTS) |
| IV. RESULTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | While these results highlight the robustness of policies, we want to emphasize that we are not claiming that such (or even more) robustness cannot ... | p. 7 (IV. RESULTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 3: (a) Forward and angular velocity tracking performance. The Grid Adaptive curriculum tracks a larger range of velocities than the Box Adaptive curriculum ... | p. 5 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / IV. RESULTS - extractive PDF cue:** The maximum attainable speed is intimately tied to the robot's hardware properties, such as its weight, motor strength, and leg length.
- **p. 7 / IV. RESULTS - extractive PDF cue:** Response to Terrain Changes and Hardware Failures We tested our system in a diverse set of challenging real-world scenarios: (1) ascending a steep incline made ...
- **p. 2 / II. EXPERIMENTAL SETUP - extractive PDF cue:** The robot stands 30 cm tall and weighs 9 kg.
- **p. 2 / II. EXPERIMENTAL SETUP - extractive PDF cue:** Hardware: We use the MIT Mini Cheetah [20] as our experimental platform.
- **p. 6 / IV. RESULTS - extractive PDF cue:** On the other hand, some aspects of the real-world dynamics are probably not captured under any configuration of the simulator.
- **p. 7 / IV. RESULTS - extractive PDF cue:** The privileged teacher πT trained with access to environment parameters attains a strictly larger command area than the policy πDR trained with only the robot ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: An end-to-end learned controller enables the MIT Mini Cheetah to execute: (a) fast sprinting at 3.9 m/s (top); (b) a rough terrain 10-meter ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 2: Our controller is a learned mapping from sensory inputs to desired joint positions. We parameterize it as 5-layer neural network πθ with parameters ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 3: (a) Forward and angular velocity tracking performance. The Grid Adaptive curriculum tracks a larger range of velocities than the Box Adaptive curriculum for ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 4: Online system identification reduces tracking error, particularly at high speeds. The command area increases as the error threshold is relaxed for teacher, student, ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 5: (a) Increasing the magnitude of terrain roughness during training shrinks the range of commands the robot can successfully track - the command area ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The maximum attainable speed is intimately tied to the robot's hardware properties, such as its weight, motor strength, and leg length. | embodiment, simulator version and control stack | p. 6 (IV. RESULTS), p. 7 (IV. RESULTS) |
| Task/environment | Response to Terrain Changes and Hardware Failures We tested our system in a diverse set of challenging real-world scenarios: (1) ascending a steep incline ... | reset, timeout, object/scene variation | p. 7 (IV. RESULTS), p. 2 (II. EXPERIMENTAL SETUP) |
| Observation/sensor | proprioception, terrain/perception observation과 velocity command | calibration, preprocessing, privileged input | p. 2 (III. METHOD), p. 2 (III. METHOD) |
| Output/decision | joint target, torque, footstep 또는 locomotion action | action frame, controller and termination | p. 3 (III. METHOD), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 3: (a) Forward and angular velocity tracking performance. The Grid Adaptive curriculum tracks a larger range of velocities than the Box Adaptive curriculum ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| Curriculum Learning Enables High-Speed Locomotion Figure 3(a) visualizes the tracking error (see Section III-E) of the policies learned from the three command sampling strategies ... | definition/direction/unit from same section | p. 5 (IV. RESULTS) |
| We are the first to demonstrate that reinforcement learning (RL) achieves agile locomotion with Froude number ≥1 (along with concurrent work Ji et al.). ... | definition/direction/unit from same section | p. 6 (IV. RESULTS) |
| Fig. 5: (a) Increasing the magnitude of terrain roughness during training shrinks the range of commands the robot can successfully track - the command ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Hence, the reward almost always remains small, providing minimal learning signal. | definition/direction/unit from same section | p. 6 (IV. RESULTS) |
| 4: Online system identification reduces tracking error, particularly at high speeds. | definition/direction/unit from same section | p. 7 (IV. RESULTS) |
| Fig. 1: An end-to-end learned controller enables the MIT Mini Cheetah to execute: (a) fast sprinting at 3.9 m/s (top); (b) a rough terrain ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Unlike our learned controller, the baseline did not recover from (1) slipping down the gravelly incline and (4) tripping over the barrier. | comparison identity and matched condition | p. 7 (IV. RESULTS) |
| ANYmal Y 0.5 1.5 50 TABLE III: Measure of Agility: Comparison between the Froude numbers of various prior works. | comparison identity and matched condition | p. 6 (IV. RESULTS) |
| While prior work demonstrated that sim-to-real gap can be mitigated at low velocities [23, 24], our results show that these findings also hold true ... | comparison identity and matched condition | p. 6 (IV. RESULTS) |
| The strategy of training on rough terrains has been applied successfully in prior works [23, 24, 37] to enable robust locomotion on diverse terrains. | comparison identity and matched condition | p. 7 (IV. RESULTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We observe that the policy trained without any curriculum fails to learn. | component/input/data sensitivity | p. 6 (IV. RESULTS) |
| The results reveal that online system identification leads to better tracking of the velocity command of 6.0 m/s in simulation (speed of 5.46 m/s ... | component/input/data sensitivity | p. 6 (IV. RESULTS) |
| Ablation Studies 1) Impact of Online System Identification: System identification can become both more critical and more challenging as locomotion speed increases; this has ... | component/input/data sensitivity | p. 7 (IV. RESULTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| RL algorithms * Equal contribution. | The performance of the system is improved substantially by implementing the Box Curriculum. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (IV. RESULTS), p. 6 (IV. RESULTS), p. 7 (IV. RESULTS), p. 7 (IV. RESULTS), p. 5 (Figure/Table caption) |
| Primary metric/result | Using the Grid Curriculum, the performance of the policy further improves, as evidenced by the larger command area. | numeric claim only at cited anchor | p. 6 (IV. RESULTS) |

- Numeric sentences retained from the body:
- **p. 2 / II. EXPERIMENTAL SETUP - extractive PDF cue:** Our neural network controller runs at 50 Hz on an onboard NVIDIA Jetson TX2 NX computer.
- **p. 2 / II. EXPERIMENTAL SETUP - extractive PDF cue:** This is roughly equivalent to 92 real-time days, which we can simulate in under three hours of wall-clock time using a single NVIDIA RTX 3090 ...
- **p. 6 / IV. RESULTS - extractive PDF cue:** This is higher than the previous record of 3.7 m/s reported for a vcmd x vx (Sim) vx (Real) With System ID (πθST ) 6.0 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Our system also does not use vision, so in general, it cannot perform tasks that require planning ahead of time, like efficiently ascending stairs ... | p. 8 (VI. DISCUSSION) |
| body limitation/failure cue | We cannot use motion capture to record the robot's state outdoors as we do in the lab. | p. 8 (VI. DISCUSSION) |
| body limitation/failure cue | Response to Terrain Changes and Hardware Failures We tested our system in a diverse set of challenging real-world scenarios: (1) ascending a steep incline ... | p. 7 (IV. RESULTS) |
| body limitation/failure cue | While these results highlight the robustness of policies, we want to emphasize that we are not claiming that such (or even more) robustness cannot ... | p. 7 (IV. RESULTS) |
| body limitation/failure cue | Fig. 3: (a) Forward and angular velocity tracking performance. The Grid Adaptive curriculum tracks a larger range of velocities than the Box Adaptive curriculum ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | We observe that the policy trained without any curriculum fails to learn. | p. 6 (IV. RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Hardware: We use the MIT Mini Cheetah [20] as our experimental platform. | p. 2 (II. EXPERIMENTAL SETUP) |
| Our neural network controller runs at 50 Hz on an onboard NVIDIA Jetson TX2 NX computer. | p. 2 (II. EXPERIMENTAL SETUP) |
| For instance, from the same starting state, it makes sense to run on ice in a manner different from running on grass. | p. 3 (III. METHOD) |
| The main idea is that accurately matching the teacher's actions forces the student to implicitly infer domain parameters (dt) from a state history of ... | p. 3 (III. METHOD) |
| Indoor Running To evaluate how fast our robot can run in the real world, we ramped the velocity command to 6.0 m/s. | p. 6 (IV. RESULTS) |
| The maximum attainable speed is intimately tied to the robot's hardware properties, such as its weight, motor strength, and leg length. | p. 6 (IV. RESULTS) |
| Response to Terrain Changes and Hardware Failures We tested our system in a diverse set of challenging real-world scenarios: (1) ascending a steep incline ... | p. 7 (IV. RESULTS) |
| We evaluate this hypothesis in the teacher-student setting by quantifying (1) the benefit of access to privileged information when learning to run at high ... | p. 7 (IV. RESULTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / VI. DISCUSSION - extractive PDF cue:** Our system also does not use vision, so in general, it cannot perform tasks that require planning ahead of time, like efficiently ascending stairs or ...
- **p. 8 / VI. DISCUSSION - extractive PDF cue:** We cannot use motion capture to record the robot's state outdoors as we do in the lab.
- **p. 7 / IV. RESULTS - extractive PDF cue:** Response to Terrain Changes and Hardware Failures We tested our system in a diverse set of challenging real-world scenarios: (1) ascending a steep incline made ...
- **p. 7 / IV. RESULTS - extractive PDF cue:** While these results highlight the robustness of policies, we want to emphasize that we are not claiming that such (or even more) robustness cannot be ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 3: (a) Forward and angular velocity tracking performance. The Grid Adaptive curriculum tracks a larger range of velocities than the Box Adaptive curriculum for ...
- **p. 6 / IV. RESULTS - extractive PDF cue:** We observe that the policy trained without any curriculum fails to learn.

- **PDF anchors reviewed:** datasets p. 6 (IV. RESULTS), p. 7 (IV. RESULTS), p. 2 (II. EXPERIMENTAL SETUP), p. 2 (II. EXPERIMENTAL SETUP), p. 6 (IV. RESULTS), p. 7 (IV. RESULTS), metrics p. 5 (Figure/Table caption), p. 5 (IV. RESULTS), p. 6 (IV. RESULTS), p. 7 (Figure/Table caption), p. 6 (IV. RESULTS), p. 7 (IV. RESULTS), baselines p. 7 (IV. RESULTS), p. 6 (IV. RESULTS), p. 6 (IV. RESULTS), p. 7 (IV. RESULTS), results p. 6 (IV. RESULTS), p. 6 (IV. RESULTS), p. 7 (IV. RESULTS), p. 7 (IV. RESULTS), p. 5 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
