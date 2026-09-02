# Evaluation - Differentiable Robust Model Predictive Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p003.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p003.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (V. EXPERIMENTS), p. 11 (V. EXPERIMENTS), p. 11 (V. EXPERIMENTS), p. 20 (Figure/Table caption), p. 7 (Figure/Table caption), p. 9 (V. EXPERIMENTS)): On the other hand, the proposed DT-MPC bounds the true system within a safer tube around the nominal trajectory by tuning the ancillary MPC in real-time, drastically increasing the success ...

## Evaluation Body Digest

- **p. 9 / V. EXPERIMENTS - extractive body cue:** The generality of the proposed DT-MPC is established through benchmarks on five nonlinear robotics systems subject to highly non-convex constraints such as dense obstacle fields.
- **p. 11 / V. EXPERIMENTS - extractive body cue:** 8), a state-of-the-art, remotely accessible robotics hardware platform for multi-agent control [52].
- **p. 11 / V. EXPERIMENTS - extractive body cue:** Hardware Experiment - Robotarium Finally, we implement the proposed methodology on the Robotarium (Fig.
- **p. 10 / V. EXPERIMENTS - extractive body cue:** 5: Environment for the robot arm task. the linear and angular velocities are sampled from a larger range of [-0.1, 0.1] - this choice emulates ...
- **p. 10 / V. EXPERIMENTS - extractive body cue:** Dubins Vehicle Quadrotor Robot Arm Cheetah Quadruped Successes Violations Successes Violations Successes Violations Successes Violations Successes Violations NT-MPC 14% 0% 14% 20% 0% 56% 26% ...
- **p. 9 / V. EXPERIMENTS - extractive body cue:** Furthermore, we present a hardware experiment showing the ability of DT-MPC to adapt to an out-of-distribution test case.
- **p. 10 / V. EXPERIMENTS - extractive body cue:** On the other hand, the proposed DT-MPC bounds the true system within a safer tube around the nominal trajectory by tuning the ancillary MPC in ...
- **p. 11 / V. EXPERIMENTS - extractive body cue:** Overall, DT-MPC remains safe while increasing the task success rate by over 200% (20% success rate for NT-MPC vs.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** robot mechanism의 state와 task-space dynamics.
- **Input boundary:** joint/task state, reference와 sensor feedback.
- **Output/decision under evaluation:** torque, force, velocity 또는 position command.
- **Primary target:** tracking, stability, constraint satisfaction과 contact behavior.
- **Detected evaluation headings:** V. EXPERIMENTS (p. 9).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | On the other hand, the proposed DT-MPC bounds the true system within a safer tube around the nominal trajectory by tuning the ancillary MPC ... | p. 10 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Overall, DT-MPC remains safe while increasing the task success rate by over 200% (20% success rate for NT-MPC vs. | p. 11 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The JAX-based Python implementation of our method runs at over 50 Hz on the Robotarium - we expect further speedups can be achieved through ... | p. 11 (V. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 11: Robot arm numerical comparisons. As Diff-MPC [5] uses an LQ approximation to the control problem, their algorithm is able to achieve very ... | p. 20 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 3: Jacobian estimate errors on the quadrotor system as a function of DDP iterate error. differentiable compute graph and backpropagating to compute Jacobians ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 9 / V. EXPERIMENTS - extractive body cue:** The generality of the proposed DT-MPC is established through benchmarks on five nonlinear robotics systems subject to highly non-convex constraints such as dense obstacle fields.
- **p. 11 / V. EXPERIMENTS - extractive body cue:** 8), a state-of-the-art, remotely accessible robotics hardware platform for multi-agent control [52].
- **p. 11 / V. EXPERIMENTS - extractive body cue:** Hardware Experiment - Robotarium Finally, we implement the proposed methodology on the Robotarium (Fig.
- **p. 10 / V. EXPERIMENTS - extractive body cue:** 5: Environment for the robot arm task. the linear and angular velocities are sampled from a larger range of [-0.1, 0.1] - this choice emulates ...
- **p. 10 / V. EXPERIMENTS - extractive body cue:** Dubins Vehicle Quadrotor Robot Arm Cheetah Quadruped Successes Violations Successes Violations Successes Violations Successes Violations Successes Violations NT-MPC 14% 0% 14% 20% 0% 56% 26% ...
- **p. 9 / V. EXPERIMENTS - extractive body cue:** Furthermore, we present a hardware experiment showing the ability of DT-MPC to adapt to an out-of-distribution test case.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Proposed differentiable robust MPC architecture. Or- ange dashed arrows show how gradients are passed in our
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 2: Controlled quadrotor trajectories subject to large distur- bances. 50 trajectories are plotted for each algorithm. ‘Nom- inal' corresponds to the reference trajectory being ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 3: Jacobian estimate errors on the quadrotor system as a function of DDP iterate error. differentiable compute graph and backpropagating to compute Jacobians via ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 4: Controlled Dubins vehicle trajectories subject to large noise. NT-MPC trajectories diverge from the nominal trajec- tory and the uncertainty increases over time. Meanwhile, ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 4. DT-MPC bounds the true system within a safer tube around the nominal trajectory, and the trajectories remain on the same side of the ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 5: Environment for the robot arm task. the linear and angular velocities are sampled from a larger range of [-0.1, 0.1] - this choice ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 6: Comparison of tube-based MPC approaches on the DeepMind Control Suite cheetah robotics system [49]. such that the quadruped does not flip over ([-π/2, ...
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 7: Comparison of tube-based MPC approaches on the DeepMind Control Suite quadruped system [49]. method is verified for the robust control of multiple nonlinear ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The generality of the proposed DT-MPC is established through benchmarks on five nonlinear robotics systems subject to highly non-convex constraints such as dense obstacle ... | embodiment, simulator version and control stack | p. 9 (V. EXPERIMENTS), p. 11 (V. EXPERIMENTS) |
| Task/environment | 8), a state-of-the-art, remotely accessible robotics hardware platform for multi-agent control [52]. | reset, timeout, object/scene variation | p. 11 (V. EXPERIMENTS), p. 11 (V. EXPERIMENTS) |
| Observation/sensor | joint/task state, reference와 sensor feedback | calibration, preprocessing, privileged input | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Output/decision | torque, force, velocity 또는 position command | action frame, controller and termination | p. 3 (II. MATHEMATICAL BACKGROUND), p. 3 (II. MATHEMATICAL BACKGROUND) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| On the other hand, the proposed DT-MPC bounds the true system within a safer tube around the nominal trajectory by tuning the ancillary MPC ... | definition/direction/unit from same section | p. 10 (V. EXPERIMENTS) |
| Overall, DT-MPC remains safe while increasing the task success rate by over 200% (20% success rate for NT-MPC vs. | definition/direction/unit from same section | p. 11 (V. EXPERIMENTS) |
| NT-MPC is robust to disturbances due to both modeling error and process noise and can reach the target state successfully (Fig. | definition/direction/unit from same section | p. 11 (V. EXPERIMENTS) |
| Fig. 3: Jacobian estimate errors on the quadrotor system as a function of DDP iterate error. differentiable compute graph and backpropagating to compute Jacobians ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Fig. 11: Robot arm numerical comparisons. As Diff-MPC [5] uses an LQ approximation to the control problem, their algorithm is able to achieve very ... | definition/direction/unit from same section | p. 20 (Figure/Table caption) |
| Fig. 9: Dubins vehicle numerical comparisons. (a) Jacobian estimate error (repeated from Fig. 3 for reference). (b) Timing comparison. Note the log scale on ... | definition/direction/unit from same section | p. 19 (Figure/Table caption) |
| Meanwhile, DTMPC adapts to the environment, maintaining safety and robust task performance. | definition/direction/unit from same section | p. 9 (V. EXPERIMENTS) |
| The nominal MPC parameters are kept fixed, while the ancillary MPC is allowed to adapt through minimization of the loss defined in Eq. | definition/direction/unit from same section | p. 9 (V. EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 8), a state-of-the-art, remotely accessible robotics hardware platform for multi-agent control [52]. | comparison identity and matched condition | p. 11 (V. EXPERIMENTS) |
| As a baseline, the NT-MPC controller is tuned on a fixed task distribution where the other agents remain stationary throughout the experimental trial. | comparison identity and matched condition | p. 11 (V. EXPERIMENTS) |
| Fig. 11: Robot arm numerical comparisons. As Diff-MPC [5] uses an LQ approximation to the control problem, their algorithm is able to achieve very ... | comparison identity and matched condition | p. 20 (Figure/Table caption) |
| Fig. 2: Controlled quadrotor trajectories subject to large distur- bances. 50 trajectories are plotted for each algorithm. ‘Nom- inal' corresponds to the reference trajectory ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Fig. 3: Jacobian estimate errors on the quadrotor system as a function of DDP iterate error. differentiable compute graph and backpropagating to compute Jacobians ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| This puts the proposed framework to the test, especially in comparison to the non-adaptive, nonlinear tube-based MPC. | comparison identity and matched condition | p. 9 (V. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In the experiments that follow, the nominal MPC is tuned to perform the task successfully and then the algorithms are deployed on the true ... | component/input/data sensitivity | p. 9 (V. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The main contribution of this work is the development of a novel differentiable tube-based MPC (DT-MPC) framework for safe, robust control. | On the other hand, the proposed DT-MPC bounds the true system within a safer tube around the nominal trajectory by tuning the ancillary MPC ... | PDF body cue; verify exact table/figure and matched conditions | p. 10 (V. EXPERIMENTS), p. 11 (V. EXPERIMENTS), p. 11 (V. EXPERIMENTS), p. 20 (Figure/Table caption), p. 7 (Figure/Table caption), p. 9 (V. EXPERIMENTS) |
| Primary metric/result | Overall, DT-MPC remains safe while increasing the task success rate by over 200% (20% success rate for NT-MPC vs. | numeric claim only at cited anchor | p. 11 (V. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 10 / V. EXPERIMENTS - extractive body cue:** Dubins Vehicle Quadrotor Robot Arm Cheetah Quadruped Successes Violations Successes Violations Successes Violations Successes Violations Successes Violations NT-MPC 14% 0% 14% 20% 0% 56% 26% ...
- **p. 10 / V. EXPERIMENTS - extractive body cue:** The objective of the controller is to drive the cheetah to a target position of 5 m in 3 s, requiring an average velocity of ...
- **p. 10 / V. EXPERIMENTS - extractive body cue:** The system has 56 states and 12 controls, and the objective is to drive the quadruped towards a target position of 2.5 m in 2 ...
- **p. 11 / V. EXPERIMENTS - extractive body cue:** The JAX-based Python implementation of our method runs at over 50 Hz on the Robotarium - we expect further speedups can be achieved through a ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** 50 trajectories are plotted for each algorithm. ‘Nominal' corresponds to the reference trajectory being tracked by the two algorithms.
- **p. 2 / II. MATHEMATICAL BACKGROUND - extractive body cue:** The nominal MPC problem is, therefore, given as: Problem 1 (Nominal MPC). ¯τ = arg min τ ¯J(τ) := N-1 X k=0 ¯ℓ(xk, uk) + ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | For this task, the nominal controller (tuned for deterministic task completion) is too aggressive for the magnitude of disturbances received, leading to a large ... | p. 10 (V. EXPERIMENTS) |
| body limitation/failure cue | The results in Table I show that, while NT-MPC fails to reach the target in the majority of the cases and occasionally violates the ... | p. 10 (V. EXPERIMENTS) |
| body limitation/failure cue | While the deterministic nominal trajectory reaches the target state during every trial, the ancillary controller cannot keep up with the desired aggressive jumping maneuver ... | p. 11 (V. EXPERIMENTS) |
| body limitation/failure cue | Fig. 4: Controlled Dubins vehicle trajectories subject to large noise. NT-MPC trajectories diverge from the nominal trajec- tory and the uncertainty increases over time. ... | p. 9 (Figure/Table caption) |
| body limitation/failure cue | NT-MPC is robust to disturbances due to both modeling error and process noise and can reach the target state successfully (Fig. | p. 11 (V. EXPERIMENTS) |
| body limitation/failure cue | While both algorithms remain safe and avoid collisions (see Table I), only DT-MPC is able to complete the task the majority of the time. | p. 9 (V. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Algorithm 2: Differentiable Tube-based Model Predictive Control (DT-MPC) Input: Initial nominal parameters ¯θ and ancillary parameters θ, learning rate η, task horizon H 1 ... | p. 8 (IV. DIFFERENTIABLE TUBE-BASED MPC) |
| Furthermore, we present a hardware experiment showing the ability of DT-MPC to adapt to an out-of-distribution test case. | p. 9 (V. EXPERIMENTS) |
| A sample visualization of one trial per algorithm is provided in Fig. | p. 10 (V. EXPERIMENTS) |
| Dubins Vehicle Quadrotor Robot Arm Cheetah Quadruped Successes Violations Successes Violations Successes Violations Successes Violations Successes Violations NT-MPC 14% 0% 14% 20% 0% 56% ... | p. 10 (V. EXPERIMENTS) |
| 8), a state-of-the-art, remotely accessible robotics hardware platform for multi-agent control [52]. | p. 11 (V. EXPERIMENTS) |
| Hardware Experiment - Robotarium Finally, we implement the proposed methodology on the Robotarium (Fig. | p. 11 (V. EXPERIMENTS) |
| The proposed algorithm is benchmarked on multiple nonlinear robotic systems, including two systems in the MuJoCo simulator environment and one hardware experiment on the ... | p. 1 (Abstract) |
| A hardware experiment on the Robotarium [52] demonstrates the ability of the proposed DT-MPC to adapt to an out-of-distribution test case. | p. 2 (I. INTRODUCTION) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / V. EXPERIMENTS - extractive body cue:** For this task, the nominal controller (tuned for deterministic task completion) is too aggressive for the magnitude of disturbances received, leading to a large number ...
- **p. 10 / V. EXPERIMENTS - extractive body cue:** The results in Table I show that, while NT-MPC fails to reach the target in the majority of the cases and occasionally violates the safety ...
- **p. 11 / V. EXPERIMENTS - extractive body cue:** While the deterministic nominal trajectory reaches the target state during every trial, the ancillary controller cannot keep up with the desired aggressive jumping maneuver due ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 4: Controlled Dubins vehicle trajectories subject to large noise. NT-MPC trajectories diverge from the nominal trajec- tory and the uncertainty increases over time. Meanwhile, ...
- **p. 11 / V. EXPERIMENTS - extractive body cue:** NT-MPC is robust to disturbances due to both modeling error and process noise and can reach the target state successfully (Fig.
- **p. 9 / V. EXPERIMENTS - extractive body cue:** While both algorithms remain safe and avoid collisions (see Table I), only DT-MPC is able to complete the task the majority of the time.

- **Evidence anchors reviewed:** datasets p. 9 (V. EXPERIMENTS), p. 11 (V. EXPERIMENTS), p. 11 (V. EXPERIMENTS), p. 10 (V. EXPERIMENTS), p. 10 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS), metrics p. 10 (V. EXPERIMENTS), p. 11 (V. EXPERIMENTS), p. 11 (V. EXPERIMENTS), p. 7 (Figure/Table caption), p. 20 (Figure/Table caption), p. 19 (Figure/Table caption), baselines p. 11 (V. EXPERIMENTS), p. 11 (V. EXPERIMENTS), p. 20 (Figure/Table caption), p. 1 (Figure/Table caption), p. 7 (Figure/Table caption), p. 9 (V. EXPERIMENTS), results p. 10 (V. EXPERIMENTS), p. 11 (V. EXPERIMENTS), p. 11 (V. EXPERIMENTS), p. 20 (Figure/Table caption), p. 7 (Figure/Table caption), p. 9 (V. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
