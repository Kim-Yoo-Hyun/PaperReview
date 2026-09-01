# Evaluation - Sim-to-Real: Learning Agile Locomotion For Quadruped Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://roboticsproceedings.org/rss14/p10.html; PDF retrieval source: https://arxiv.org/pdf/1804.10332. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (VI. EVALUATION AND DISCUSSION), p. 6 (VI. EVALUATION AND DISCUSSION), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption)): After we improved the simulation (Section V-A), an agile galloping gait emerged automatically.

## Evaluation Body Digest

- **p. 6 / VI. EVALUATION AND DISCUSSION - extractive body cue:** This time, we observed stable, comparable movements in both simulation and on the real robot.
- **p. 6 / VI. EVALUATION AND DISCUSSION - extractive body cue:** After the policies were learned, we deployed them on the real robot.
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8: Performance of controllers when they are tested in different simulation environments. Error bars indicate one standard deviation. 0 2 4 6 small
- **p. 6 / VI. EVALUATION AND DISCUSSION - extractive body cue:** While it is unclear how to use reward shaping to learn such a gait, we can directly control the learned gait by providing an open ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Controller performance in simulation (blue) and on the robot (red). From left to right, the controllers are trained using baseline simulation, using baseline ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 9: Comparison of controllers trained with different obser- vation spaces and randomization. The blue and red bars are the performance in simulation and in ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Performance comparison of controllers that are trained with (red) and without (blue) randomization and tested with different body inertia. We also found that ...
- **p. 6 / VI. EVALUATION AND DISCUSSION - extractive body cue:** After we improved the simulation (Section V-A), an agile galloping gait emerged automatically.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** legged robot, terrain과 contact dynamics.
- **Input boundary:** proprioception, terrain/perception observation과 velocity command.
- **Output/decision under evaluation:** joint target, torque, footstep 또는 locomotion action.
- **Primary target:** velocity/progress, stability, energy와 terrain generalization.
- **Detected evaluation headings:** VI. EVALUATION AND DISCUSSION (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| VI. EVALUATION AND DISCUSSION | EMPIRICAL / REAL-ROBOT OR HARDWARE | After we improved the simulation (Section V-A), an agile galloping gait emerged automatically. | p. 6 (VI. EVALUATION AND DISCUSSION) |
| VI. EVALUATION AND DISCUSSION | EMPIRICAL / REAL-ROBOT OR HARDWARE | After training with the improved simulator and random perturbations, the Minitaur is able to trot stably in simulation. | p. 6 (VI. EVALUATION AND DISCUSSION) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 6: Controller performance in simulation (blue) and on the robot (red). From left to right, the controllers are trained using baseline simulation, using ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 9: Comparison of controllers trained with different obser- vation spaces and randomization. The blue and red bars are the performance in simulation and ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 7: Performance comparison of controllers that are trained with (red) and without (blue) randomization and tested with different body inertia. We also found ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / VI. EVALUATION AND DISCUSSION - extractive body cue:** This time, we observed stable, comparable movements in both simulation and on the real robot.
- **p. 6 / VI. EVALUATION AND DISCUSSION - extractive body cue:** After the policies were learned, we deployed them on the real robot.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: The simulated and the real Minitaurs learned to gallop using deep reinforcement learning. to locomotion tasks due to the difficulties of automatically resetting ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: The customized hardware architecture enables the Minitaur to perform deep neural network inference. Modulation (PWM) signal. The Minitaur is equipped with motor encoders ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3: Representation of the leg pose in motor space and leg space. Extension (e) sets the length of the leg by rotating both motors ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4: Comparison of the simulated motor trajectory (red) with the ground truth (blue). b) Latency: Latency is one of the main causes of in- ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: The learning curves of trotting and galloping. TABLE II: Parameters of learning algorithm for each task. Gait Observation Policy Net Value Net Learning ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Controller performance in simulation (blue) and on the robot (red). From left to right, the controllers are trained using baseline simulation, using baseline ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Performance comparison of controllers that are trained with (red) and without (blue) randomization and tested with different body inertia. We also found that ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 8: Performance of controllers when they are tested in different simulation environments. Error bars indicate one standard deviation. 0 2 4 6 small

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | This time, we observed stable, comparable movements in both simulation and on the real robot. | embodiment, simulator version and control stack | p. 6 (VI. EVALUATION AND DISCUSSION), p. 6 (VI. EVALUATION AND DISCUSSION) |
| Task/environment | After the policies were learned, we deployed them on the real robot. | reset, timeout, object/scene variation | p. 6 (VI. EVALUATION AND DISCUSSION) |
| Observation/sensor | proprioception, terrain/perception observation과 velocity command | calibration, preprocessing, privileged input | p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS) |
| Output/decision | joint target, torque, footstep 또는 locomotion action | action frame, controller and termination | p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS), p. 3 (IV. LEARNING LOCOMOTION CONTROLLERS) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 8: Performance of controllers when they are tested in different simulation environments. Error bars indicate one standard deviation. 0 2 4 6 small | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| While it is unclear how to use reward shaping to learn such a gait, we can directly control the learned gait by providing an ... | definition/direction/unit from same section | p. 6 (VI. EVALUATION AND DISCUSSION) |
| Fig. 6: Controller performance in simulation (blue) and on the robot (red). From left to right, the controllers are trained using baseline simulation, using ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Fig. 9: Comparison of controllers trained with different obser- vation spaces and randomization. The blue and red bars are the performance in simulation and ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Fig. 7: Performance comparison of controllers that are trained with (red) and without (blue) randomization and tested with different body inertia. We also found ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We compared the learned gaits with the handcrafted ones from Ghost Robotics [3]. | comparison identity and matched condition | p. 6 (VI. EVALUATION AND DISCUSSION) |
| Fig. 6: Controller performance in simulation (blue) and on the robot (red). From left to right, the controllers are trained using baseline simulation, using ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| The controllers worked directly in the real world without additional fine tuning on the physical system. | comparison identity and matched condition | p. 6 (VI. EVALUATION AND DISCUSSION) |
| Fig. 7: Performance comparison of controllers that are trained with (red) and without (blue) randomization and tested with different body inertia. We also found ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Fig. 9: Comparison of controllers trained with different obser- vation spaces and randomization. The blue and red bars are the performance in simulation and ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Fig. 4: Comparison of the simulated motor trajectory (red) with the ground truth (blue). b) Latency: Latency is one of the main causes of ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The controllers worked directly in the real world without additional fine tuning on the physical system. | component/input/data sensitivity | p. 6 (VI. EVALUATION AND DISCUSSION) |
| Fig. 7: Performance comparison of controllers that are trained with (red) and without (blue) randomization and tested with different body inertia. We also found ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Fig. 9: Comparison of controllers trained with different obser- vation spaces and randomization. The blue and red bars are the performance in simulation and ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Locomotion Tasks In the first experiment, we let the system learn from scratch: We set the open loop component ¯a(t) = 0 and gave ... | component/input/data sensitivity | p. 6 (VI. EVALUATION AND DISCUSSION) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The main contributions of this paper are: 1) We propose a complete learning system for agile locomotion. | After we improved the simulation (Section V-A), an agile galloping gait emerged automatically. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (VI. EVALUATION AND DISCUSSION), p. 6 (VI. EVALUATION AND DISCUSSION), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption) |
| Primary metric/result | After training with the improved simulator and random perturbations, the Minitaur is able to trot stably in simulation. | numeric claim only at cited anchor | p. 6 (VI. EVALUATION AND DISCUSSION) |

- Numeric sentences retained from the body:
- **p. 6 / VI. EVALUATION AND DISCUSSION - extractive body cue:** At each iteration of policy update, we collected the simulated experience by running 25 roll-outs (up to 1000 steps each) in parallel.
- **p. 6 / VI. EVALUATION AND DISCUSSION - extractive body cue:** One diagonal pair of legs shares the same curves and the other diagonal pair's are 180 degree out of phase.
- **p. 4 / IV. LEARNING LOCOMOTION CONTROLLERS - extractive body cue:** An episode terminates after 1000 steps or when the simulated Minitaur loses balance: its base tilts more than 0.5 radians.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | However, when the policies were deployed on the robot, we had mixed results due to the reality gap: Some policies can transfer while others ... | p. 6 (VI. EVALUATION AND DISCUSSION) |
| body limitation/failure cue | Note that while this open loop controller expresses the user's preference of the locomotion style, by itself, it cannot produce any forward movement in ... | p. 6 (VI. EVALUATION AND DISCUSSION) |
| body limitation/failure cue | Fig. 1: The simulated and the real Minitaurs learned to gallop using deep reinforcement learning. to locomotion tasks due to the difficulties of automatically ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | This points us to two interesting avenues for future work. | p. 8 (VII. CONCLUSION) |
| body limitation/failure cue | With an accurate physical model and robust controllers, we have successfully deployed the controllers learned in simulation on the real robots. | p. 8 (VII. CONCLUSION) |
| body limitation/failure cue | Fig. 7: Performance comparison of controllers that are trained with (red) and without (blue) randomization and tested with different body inertia. We also found ... | p. 7 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We repeated the training with different hyperparameters and random seeds, and found that the majority of the solutions converged to galloping. | p. 6 (VI. EVALUATION AND DISCUSSION) |
| Their sizes were determined using hyperparameter search. | p. 6 (VI. EVALUATION AND DISCUSSION) |
| An episode terminates after 1000 steps or when the simulated Minitaur loses balance: its base tilts more than 0.5 radians. | p. 4 (IV. LEARNING LOCOMOTION CONTROLLERS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / VI. EVALUATION AND DISCUSSION - extractive body cue:** However, when the policies were deployed on the robot, we had mixed results due to the reality gap: Some policies can transfer while others cannot.
- **p. 6 / VI. EVALUATION AND DISCUSSION - extractive body cue:** Note that while this open loop controller expresses the user's preference of the locomotion style, by itself, it cannot produce any forward movement in the ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: The simulated and the real Minitaurs learned to gallop using deep reinforcement learning. to locomotion tasks due to the difficulties of automatically resetting ...
- **p. 8 / VII. CONCLUSION - extractive body cue:** This points us to two interesting avenues for future work.
- **p. 8 / VII. CONCLUSION - extractive body cue:** With an accurate physical model and robust controllers, we have successfully deployed the controllers learned in simulation on the real robots.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7: Performance comparison of controllers that are trained with (red) and without (blue) randomization and tested with different body inertia. We also found that ...

- **PDF anchors reviewed:** datasets p. 6 (VI. EVALUATION AND DISCUSSION), p. 6 (VI. EVALUATION AND DISCUSSION), metrics p. 8 (Figure/Table caption), p. 6 (VI. EVALUATION AND DISCUSSION), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), baselines p. 6 (VI. EVALUATION AND DISCUSSION), p. 7 (Figure/Table caption), p. 6 (VI. EVALUATION AND DISCUSSION), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 5 (Figure/Table caption), results p. 6 (VI. EVALUATION AND DISCUSSION), p. 6 (VI. EVALUATION AND DISCUSSION), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
