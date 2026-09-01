# Evaluation - Learning Agile and Dynamic Motor Skills for Legged Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1901.08652; PDF retrieval source: https://arxiv.org/pdf/1901.08652. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (Front matter), p. 9 (Front matter), p. 9 (Front matter), p. 6 (Front matter), p. 11 (Front matter), p. 10 (Front matter)): We then further improved the success rate to 100 % by relaxing the joint velocity constraints.

## Evaluation Body Digest

- **p. 7 / Front matter - extractive PDF cue:** Many hardware changes were introduced as well: different robot configurations, which roughly contribute 2.0 kg to the total weight, and a new drive which has ...
- **p. 6 / Front matter - extractive PDF cue:** The recovery task was successful on the very first attempt on the hardware.
- **p. 6 / Front matter - extractive PDF cue:** DISCUSSION The learning-based control approach presented in this paper achieved a new level of locomotion skill based purely on training in simulation and without tedious ...
- **p. 8 / Front matter - extractive PDF cue:** The rigid-body simulator outputs the next state of the robot given the joint torques and the current state.
- **p. 9 / Front matter - extractive PDF cue:** Observation and action The observations in our method should be observable (i.e., can be inferred from measurements) on the real robot and relevant for the ...
- **p. 11 / Front matter - extractive PDF cue:** Each trajectory lasts 6 seconds unless the robot reaches a terminal state earlier.
- **p. 11 / Front matter - extractive PDF cue:** This way, the robot first learns how to achieve the objective and then how to respect various constraints.
- **p. 7 / Front matter - extractive PDF cue:** A learned recovery controller deployed on the real robot.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** legged robot, terrain과 contact dynamics.
- **Input boundary:** proprioception, terrain/perception observation과 velocity command.
- **Output/decision under evaluation:** joint target, torque, footstep 또는 locomotion action.
- **Primary target:** velocity/progress, stability, energy와 terrain generalization.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Front matter | EMPIRICAL / REAL-ROBOT OR HARDWARE | We then further improved the success rate to 100 % by relaxing the joint velocity constraints. | p. 6 (Front matter) |
| Front matter | EMPIRICAL / REAL-ROBOT OR HARDWARE | [57] found that such a controller can outperform a torque controller in both training speed and final control performance. | p. 9 (Front matter) |
| Front matter | EMPIRICAL / REAL-ROBOT OR HARDWARE | A learning session terminates if the average performance of the policy does not improve by more than a task-specific threshold within 300 TRPO iterations. | p. 9 (Front matter) |
| Front matter | EMPIRICAL / REAL-ROBOT OR HARDWARE | The system achieved more precise and energy-efficient motions than the prior state of the art. | p. 6 (Front matter) |
| Front matter | EMPIRICAL / REAL-ROBOT OR HARDWARE | This way, the robot first learns how to achieve the objective and then how to respect various constraints. | p. 11 (Front matter) |

## Dataset / Benchmark Role

- **p. 7 / Front matter - extractive PDF cue:** Many hardware changes were introduced as well: different robot configurations, which roughly contribute 2.0 kg to the total weight, and a new drive which has ...
- **p. 6 / Front matter - extractive PDF cue:** The recovery task was successful on the very first attempt on the hardware.
- **p. 6 / Front matter - extractive PDF cue:** DISCUSSION The learning-based control approach presented in this paper achieved a new level of locomotion skill based purely on training in simulation and without tedious ...
- **p. 8 / Front matter - extractive PDF cue:** The rigid-body simulator outputs the next state of the robot given the joint torques and the current state.
- **p. 9 / Front matter - extractive PDF cue:** Observation and action The observations in our method should be observable (i.e., can be inferred from measurements) on the real robot and relevant for the ...
- **p. 11 / Front matter - extractive PDF cue:** Each trajectory lasts 6 seconds unless the robot reaches a terminal state earlier.
- **p. 11 / Front matter - extractive PDF cue:** This way, the robot first learns how to achieve the objective and then how to respect various constraints.
- **p. 7 / Front matter - extractive PDF cue:** A learned recovery controller deployed on the real robot.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive PDF cue:** Fig. 1. Creating a control policy. In the first step, we identify the physical parameters of the robot and estimate uncertainties in the identification. In ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 2. Quantitative evaluation of the learned locomotion controller. (A) The discovered gait pattern for 1.0 m/s forward velocity command. The abbreviations stand for Left ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 3. Evaluation of the trained policy for high-speed loco- motion. (A) Forward velocity of ANYmal. (B) Joint velocities. (C) Joint torques. (D) Gait pattern. ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 4. A learned recovery controller deployed on the real robot. The learned policy successfully recovers from a random initial configuration in less than 3 ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Fig. 5. Training control policies in simulation. The policy net- work maps the current observation and the joint state history to the joint position targets. ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Fig. 6. Validation of the learned actuator model. The measured torque and the predicted torque from the trained actuator model are shown. The "ideal model" ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Many hardware changes were introduced as well: different robot configurations, which roughly contribute 2.0 kg to the total weight, and a new drive which ... | embodiment, simulator version and control stack | p. 7 (Front matter), p. 6 (Front matter) |
| Task/environment | The recovery task was successful on the very first attempt on the hardware. | reset, timeout, object/scene variation | p. 6 (Front matter), p. 6 (Front matter) |
| Observation/sensor | proprioception, terrain/perception observation과 velocity command | calibration, preprocessing, privileged input | p. 9 (Front matter), p. 9 (Front matter) |
| Output/decision | joint target, torque, footstep 또는 locomotion action | action frame, controller and termination | p. 3 (Front matter), p. 8 (Front matter) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We then further improved the success rate to 100 % by relaxing the joint velocity constraints. | definition/direction/unit from same section | p. 6 (Front matter) |
| Fig. 2. Quantitative evaluation of the learned locomotion controller. (A) The discovered gait pattern for 1.0 m/s forward velocity command. The abbreviations stand for ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| The policy is trained to foresee that position errors will occur and even uses them to generate acceleration and interaction forces. | definition/direction/unit from same section | p. 10 (Front matter) |
| Position controllers are sometimes limited in performance when the position reference is time-indexed, which means that there is a higherlevel controller that assumes that ... | definition/direction/unit from same section | p. 10 (Front matter) |
| Learning actuators independently might not result in a sufficient accuracy for these systems. | definition/direction/unit from same section | p. 7 (Front matter) |
| With good understanding on the actuator dynamics, appropriate history configuration can be estimated a priori and tuned further with respect to the validation error. | definition/direction/unit from same section | p. 7 (Front matter) |
| This process is error-prone and time-consuming. | definition/direction/unit from same section | p. 8 (Front matter) |
| We expect up to about 20 % error in the estimation due to unmodeled cabling and electronics. | definition/direction/unit from same section | p. 8 (Front matter) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| It outperformed the previous speed record by 25 % and learned to consistently restore the robot to an operational configuration by dynamically rolling over ... | comparison identity and matched condition | p. 6 (Front matter) |
| [57] found that such a controller can outperform a torque controller in both training speed and final control performance. | comparison identity and matched condition | p. 9 (Front matter) |
| Fig. 2. Quantitative evaluation of the learned locomotion controller. (A) The discovered gait pattern for 1.0 m/s forward velocity command. The abbreviations stand for ... | comparison identity and matched condition | p. 5 (Figure/Table caption) |
| DISCUSSION The learning-based control approach presented in this paper achieved a new level of locomotion skill based purely on training in simulation and without ... | comparison identity and matched condition | p. 6 (Front matter) |
| All control policies have been tested for more than three months on the real robot without any modification. | comparison identity and matched condition | p. 7 (Front matter) |
| The "ideal model" curve is computed assuming an ideal actuator (i.e., zero communication delay and zero mechanical response time) and is shown for comparison. | comparison identity and matched condition | p. 10 (Front matter) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| DISCUSSION The learning-based control approach presented in this paper achieved a new level of locomotion skill based purely on training in simulation and without ... | component/input/data sensitivity | p. 6 (Front matter) |
| All control policies have been tested for more than three months on the real robot without any modification. | component/input/data sensitivity | p. 7 (Front matter) |
| However, since this height estimator cannot be used when the robot is not on its feet, we removed the height observation when training for ... | component/input/data sensitivity | p. 9 (Front matter) |
| Samples that result in unrealistic internal collisions are removed. | component/input/data sensitivity | p. 11 (Front matter) |
| Developing the recovery policy took about a week largely due to the fact that some safety concerns (i.e., high impacts, fast swing legs, collisions ... | component/input/data sensitivity | p. 7 (Front matter) |
| In what follows we describe each component in detail. | component/input/data sensitivity | p. 8 (Front matter) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Furthermore, the system still consists of two independent modules that do not adapt to each other's performance characteristics. | We then further improved the success rate to 100 % by relaxing the joint velocity constraints. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (Front matter), p. 9 (Front matter), p. 9 (Front matter), p. 6 (Front matter), p. 11 (Front matter), p. 10 (Front matter) |
| Primary metric/result | [57] found that such a controller can outperform a torque controller in both training speed and final control performance. | numeric claim only at cited anchor | p. 9 (Front matter) |

- Numeric sentences retained from the body:
- **p. 8 / Front matter - extractive PDF cue:** Note that too sparse input configuration might not effectively capture the dynamics at high frequency (> 100 Hz).
- **p. 9 / Front matter - extractive PDF cue:** To obtain a rich set of data, we varied the amplitude (5∼10 cm) and the frequency (1∼25 Hz) of the foot trajectories and disturbed the ...
- **p. 9 / Front matter - extractive PDF cue:** Data was collected at 400 Hz, therefore the resulting dataset contains more than a million samples.
- **p. 9 / Front matter - extractive PDF cue:** The joint state history is sampled at t = tk -0.01 s and t = tk -0.02 s.
- **p. 11 / Front matter - extractive PDF cue:** For training the command-conditioned controller and the high-speed controller, we used γ = 0.9988 which corresponds to a half-life of 5.77 s.
- **p. 11 / Front matter - extractive PDF cue:** We also successfully trained almost equally performant policies with lower half-life (∼2 s) but they manifest a less natural standing posture.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | However, since this height estimator cannot be used when the robot is not on its feet, we removed the height observation when training for ... | p. 9 (Front matter) |
| body limitation/failure cue | For training recovery from a fall, the collision bodies of the ANYmal model are randomized in size and position. | p. 11 (Front matter) |
| body limitation/failure cue | However, as in many other RL literature, our control policy is state-indexed and does not suffer from the limitations of common PD controllers. | p. 10 (Front matter) |
| body limitation/failure cue | Fast and flexible recovery after a fall, as seen in animals, requires dynamic motion with multiple unspecified contact points. | p. 6 (Front matter) |
| body limitation/failure cue | Developing the recovery policy took about a week largely due to the fact that some safety concerns (i.e., high impacts, fast swing legs, collisions ... | p. 7 (Front matter) |
| body limitation/failure cue | For training for recovery from a fall, TRPO took 79 days of simulated time, which corresponds to eleven hours of computation in real time. | p. 11 (Front matter) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Thanks to efficient software implementations, we did not need any special computing hardware, such as multi-CPU or multi-GPU servers, for training. | p. 3 (Front matter) |
| All training sessions presented in this paper were done on a personal computer with one CPU and one GPU, and none lasted more than ... | p. 3 (Front matter) |
| The analytical model uses the actual controller code running on the actuator in conjunction with identified dynamics parameters from experiments and ComputerAided Design (CAD) ... | p. 4 (Front matter) |
| Designing control algorithms for these hardware platforms remains exceptionally challenging. | p. 1 (Front matter) |
| Given the foothold positions, the next module computes a parameterized trajectory for the foot to follow. | p. 1 (Front matter) |
| The planning module uses rigid-body dynamics and numerical optimization to compute an optimal path that the robot should follow to reach the desired goal. | p. 2 (Front matter) |
| The idea of RL is to collect data by trial and error and automatically tune the controller to optimize the given cost (or reward) ... | p. 2 (Front matter) |
| The ideal actuator model assumes that all controllers and hardware inside the actuator have infinite bandwidth and zero latency. | p. 4 (Front matter) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / Front matter - extractive PDF cue:** However, since this height estimator cannot be used when the robot is not on its feet, we removed the height observation when training for recovery ...
- **p. 11 / Front matter - extractive PDF cue:** For training recovery from a fall, the collision bodies of the ANYmal model are randomized in size and position.
- **p. 10 / Front matter - extractive PDF cue:** However, as in many other RL literature, our control policy is state-indexed and does not suffer from the limitations of common PD controllers.
- **p. 6 / Front matter - extractive PDF cue:** Fast and flexible recovery after a fall, as seen in animals, requires dynamic motion with multiple unspecified contact points.
- **p. 7 / Front matter - extractive PDF cue:** Developing the recovery policy took about a week largely due to the fact that some safety concerns (i.e., high impacts, fast swing legs, collisions with ...
- **p. 11 / Front matter - extractive PDF cue:** For training for recovery from a fall, TRPO took 79 days of simulated time, which corresponds to eleven hours of computation in real time.

- **PDF anchors reviewed:** datasets p. 7 (Front matter), p. 6 (Front matter), p. 6 (Front matter), p. 8 (Front matter), p. 9 (Front matter), p. 11 (Front matter), metrics p. 6 (Front matter), p. 5 (Figure/Table caption), p. 10 (Front matter), p. 10 (Front matter), p. 7 (Front matter), p. 7 (Front matter), baselines p. 6 (Front matter), p. 9 (Front matter), p. 5 (Figure/Table caption), p. 6 (Front matter), p. 7 (Front matter), p. 10 (Front matter), results p. 6 (Front matter), p. 9 (Front matter), p. 9 (Front matter), p. 6 (Front matter), p. 11 (Front matter), p. 10 (Front matter).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
