# Evaluation - Information Theoretic MPC for Model-Based Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ieeexplore.ieee.org/document/7989202/; PDF retrieval source: https://ieeexplore.ieee.org/document/7989202/. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (V. SIMULATED RESULTS), p. 6 (V. SIMULATED RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS), p. 6 (V. SIMULATED RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS), p. 1 (Figure/Table caption)): After one iteration, the algorithm achieves the same level of performance regardless of which network is being used.

## Evaluation Body Digest

- **p. 5 / V. SIMULATED RESULTS - extractive body cue:** The bootstrapping dataset for the cart-pole comes from 5 minutes of multiple MPPI demonstrations using known dynamics but a different cost function for the swing-up ...
- **p. 6 / VI. EXPERIMENTAL RESULTS - extractive body cue:** Bootstrapping Dataset To train an initial model, we collected a system identification dataset of approximately 30 minutes of humancontrolled driving at speeds varying between 4 ...
- **p. 7 / VI. EXPERIMENTAL RESULTS - extractive body cue:** One explanation for this is that the initial dataset was deliberately collected for system identification, and it consists of a variety of maneuvers meant to ...
- **p. 5 / V. SIMULATED RESULTS - extractive body cue:** In these simulated scenarios, a convenient benchmark is the MPPI algorithm with access to the ground-truth model used for the simulation.
- **p. 7 / VI. EXPERIMENTAL RESULTS - extractive body cue:** 5 11.11 10.84 7.49 22.62 training set and re-training the neural network model did not noticeably improve the performance of the algorithm.
- **p. 6 / VI. EXPERIMENTAL RESULTS - extractive body cue:** In our prior work, MPPI was successfully applied to this task using a physics-inspired model.
- **p. 6 / V. SIMULATED RESULTS - extractive body cue:** Multi-Step Error We train the neural network dynamics on one-step prediction error, which does not necessarily result in accurate multistep prediction.
- **p. 6 / V. SIMULATED RESULTS - extractive body cue:** None of the networks for the quadrotor dynamics perform significantly better or worse in multi-step error, which is reflected in the near identical performance of ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** robot mechanism의 state와 task-space dynamics.
- **Input boundary:** joint/task state, reference와 sensor feedback.
- **Output/decision under evaluation:** torque, force, velocity 또는 position command.
- **Primary target:** tracking, stability, constraint satisfaction과 contact behavior.
- **Detected evaluation headings:** V. SIMULATED RESULTS (p. 5); VI. EXPERIMENTAL RESULTS (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| V. SIMULATED RESULTS | EMPIRICAL / SIMULATION | After one iteration, the algorithm achieves the same level of performance regardless of which network is being used. | p. 5 (V. SIMULATED RESULTS) |
| V. SIMULATED RESULTS | EMPIRICAL / SIMULATION | The final performance margins for both the cart-pole and quadrotor are within 10% of what can be achieved with perfect model knowledge, which indicates ... | p. 6 (V. SIMULATED RESULTS) |
| VI. EXPERIMENTAL RESULTS | EMPIRICAL / SIMULATION | 5 11.11 10.84 7.49 22.62 training set and re-training the neural network model did not noticeably improve the performance of the algorithm. | p. 7 (VI. EXPERIMENTAL RESULTS) |
| V. SIMULATED RESULTS | EMPIRICAL / SIMULATION | None of the networks for the quadrotor dynamics perform significantly better or worse in multi-step error, which is reflected in the near identical performance ... | p. 6 (V. SIMULATED RESULTS) |
| VI. EXPERIMENTAL RESULTS | EMPIRICAL / SIMULATION | Results With training settings of 9 m/s and 0.275 radians, the controller successfully maneuvered the vehicle around the track using only the initial system ... | p. 7 (VI. EXPERIMENTAL RESULTS) |

## Dataset / Benchmark Role

- **p. 5 / V. SIMULATED RESULTS - extractive body cue:** The bootstrapping dataset for the cart-pole comes from 5 minutes of multiple MPPI demonstrations using known dynamics but a different cost function for the swing-up ...
- **p. 6 / VI. EXPERIMENTAL RESULTS - extractive body cue:** Bootstrapping Dataset To train an initial model, we collected a system identification dataset of approximately 30 minutes of humancontrolled driving at speeds varying between 4 ...
- **p. 7 / VI. EXPERIMENTAL RESULTS - extractive body cue:** One explanation for this is that the initial dataset was deliberately collected for system identification, and it consists of a variety of maneuvers meant to ...
- **p. 5 / V. SIMULATED RESULTS - extractive body cue:** In these simulated scenarios, a convenient benchmark is the MPPI algorithm with access to the ground-truth model used for the simulation.
- **p. 7 / VI. EXPERIMENTAL RESULTS - extractive body cue:** 5 11.11 10.84 7.49 22.62 training set and re-training the neural network model did not noticeably improve the performance of the algorithm.
- **p. 6 / VI. EXPERIMENTAL RESULTS - extractive body cue:** In our prior work, MPPI was successfully applied to this task using a physics-inspired model.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Aggressive driving with MPPI and neural network dynamics. be equipped with fast decision making processes. Model predictive control (MPC) or receding horizon control ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 2. Normalized state costs of executed cart-pole trajectories. The cost is normalized so that the ground-truth MPPI controller has a cost of 1. Average ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3. Left: Normalized state costs of executed quadrotor trajectories. The costs are normalized so that the controller with the ground-truth model has a cost ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4. Multi-step prediction error for cart position and pendulum angle.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5. Experimental setup at the Georgia Tech Autonomous Racing Facility. at any point during the time window. During training, we set the slip angle ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6. Top: Multi-step prediction error on AutoRally dynamics, the vertical bar denotes the prediction horizon. Bottom: Actual trajectory vs. predicted trajectory sequence. The prediction ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7. Trajectory traces and speeds during training runs (top) and aggressive testing runs (bottom). Counter-clockwise travel direction. angle and the desired speed. We started ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The bootstrapping dataset for the cart-pole comes from 5 minutes of multiple MPPI demonstrations using known dynamics but a different cost function for the ... | embodiment, simulator version and control stack | p. 5 (V. SIMULATED RESULTS), p. 6 (VI. EXPERIMENTAL RESULTS) |
| Task/environment | Bootstrapping Dataset To train an initial model, we collected a system identification dataset of approximately 30 minutes of humancontrolled driving at speeds varying between ... | reset, timeout, object/scene variation | p. 6 (VI. EXPERIMENTAL RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS) |
| Observation/sensor | joint/task state, reference와 sensor feedback | calibration, preprocessing, privileged input | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| Output/decision | torque, force, velocity 또는 position command | action frame, controller and termination | p. 2 (II. MODEL PREDICTIVE CONTROL), p. 2 (II. MODEL PREDICTIVE CONTROL) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Multi-Step Error We train the neural network dynamics on one-step prediction error, which does not necessarily result in accurate multistep prediction. | definition/direction/unit from same section | p. 6 (V. SIMULATED RESULTS) |
| None of the networks for the quadrotor dynamics perform significantly better or worse in multi-step error, which is reflected in the near identical performance ... | definition/direction/unit from same section | p. 6 (V. SIMULATED RESULTS) |
| Specifically, we increased the threshold for penalized slip 0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0 Time (s) 0.0 0.5 1.0 1.5 2.0 ... | definition/direction/unit from same section | p. 7 (VI. EXPERIMENTAL RESULTS) |
| Fig. 6. Top: Multi-step prediction error on AutoRally dynamics, the vertical bar denotes the prediction horizon. Bottom: Actual trajectory vs. predicted trajectory sequence. The ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| An example trajectory successfully navigating the field is also shown in Fig. | definition/direction/unit from same section | p. 5 (V. SIMULATED RESULTS) |
| This provides a metric for how much performance is lost by using an approximate model to the system. | definition/direction/unit from same section | p. 5 (V. SIMULATED RESULTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In our prior work, MPPI was successfully applied to this task using a physics-inspired model. | comparison identity and matched condition | p. 6 (VI. EXPERIMENTAL RESULTS) |
| Running the algorithm without a bootstrapped neural network results in repeated failures. | comparison identity and matched condition | p. 5 (V. SIMULATED RESULTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Running the algorithm without a bootstrapped neural network results in repeated failures. | component/input/data sensitivity | p. 5 (V. SIMULATED RESULTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| This is a significant step forward because it enables a purely data-driven approach to model learning within the MPPI framework. | After one iteration, the algorithm achieves the same level of performance regardless of which network is being used. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (V. SIMULATED RESULTS), p. 6 (V. SIMULATED RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS), p. 6 (V. SIMULATED RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS), p. 1 (Figure/Table caption) |
| Primary metric/result | The final performance margins for both the cart-pole and quadrotor are within 10% of what can be achieved with perfect model knowledge, which indicates ... | numeric claim only at cited anchor | p. 6 (V. SIMULATED RESULTS) |

- Numeric sentences retained from the body:
- **p. 6 / V. SIMULATED RESULTS - extractive body cue:** The final positional and orientation errors after the 2.5 second prediction horizon are approximately 1.5 meters and 0.4 radians, respectively.
- **p. 6 / VI. EXPERIMENTAL RESULTS - extractive body cue:** This facility consists of an elliptical dirt track approximately 3 meters wide and 30 meters across at its furthest point.
- **p. 6 / VI. EXPERIMENTAL RESULTS - extractive body cue:** The cost-map grid has a 10 centimeter resolution and is stored in CUDA texture memory for efficient look-ups inside the optimization kernel.
- **p. 6 / VI. EXPERIMENTAL RESULTS - extractive body cue:** The MPPI controller uses a time horizon of 2.5 seconds, a control frequency of 40 Hz, and performs 1200 samples every time-step.
- **p. 7 / VI. EXPERIMENTAL RESULTS - extractive body cue:** During training, we set the slip angle threshold to 15.76 degrees (0.275 radians), and for the final testing runs we raised it to 21.5 degrees ...
- **p. 7 / VI. EXPERIMENTAL RESULTS - extractive body cue:** We performed 5 iterations, each consisting of 3 trials, for a total of 45 laps around the track.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Running the algorithm without a bootstrapped neural network results in repeated failures. | p. 5 (V. SIMULATED RESULTS) |
| body limitation/failure cue | The slip angle is defined as -arctan( vy /vx/), where vx and vy are the longitudinal and lateral velocities, respectively. | p. 6 (VI. EXPERIMENTAL RESULTS) |
| body limitation/failure cue | M(x, y) is the cost-map value at the position (x, y), and Sc is an indicator variable which activates if the magnitude of the ... | p. 6 (VI. EXPERIMENTAL RESULTS) |
| body limitation/failure cue | During training, we set the slip angle threshold to 15.76 degrees (0.275 radians), and for the final testing runs we raised it to 21.5 ... | p. 7 (VI. EXPERIMENTAL RESULTS) |
| body limitation/failure cue | Slip 10 m/s 10.34 9.93 8.05 38.68 11 m/s 9.97 9.43 8.71 34.65 12 m/s 9.88 9.47 8.63 43.72 13 m/s 9.74 9.36 8.44 ... | p. 7 (VI. EXPERIMENTAL RESULTS) |
| body limitation/failure cue | The temperature was set as λ = 1 and the system noise to (2.5, .25, .25, .25), where the 2.5 value corresponds to the ... | p. 5 (V. SIMULATED RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| On-board computation is performed using an Nvidia GTX 750 Ti GPU, which has 640 CUDA cores. | p. 6 (VI. EXPERIMENTAL RESULTS) |
| This corresponds to slightly over 8 minutes of total run-time. | p. 7 (VI. EXPERIMENTAL RESULTS) |
| Each training/test iteration consisted of three separate trial runs. | p. 7 (VI. EXPERIMENTAL RESULTS) |
| Average costs are computed from ten trials. | p. 5 (V. SIMULATED RESULTS) |
| 2, where each iteration consists of one 10 second trial. | p. 5 (V. SIMULATED RESULTS) |
| There are five trials per iteration. | p. 6 (V. SIMULATED RESULTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / V. SIMULATED RESULTS - extractive body cue:** Running the algorithm without a bootstrapped neural network results in repeated failures.
- **p. 6 / VI. EXPERIMENTAL RESULTS - extractive body cue:** The slip angle is defined as -arctan( vy /vx/), where vx and vy are the longitudinal and lateral velocities, respectively.
- **p. 6 / VI. EXPERIMENTAL RESULTS - extractive body cue:** M(x, y) is the cost-map value at the position (x, y), and Sc is an indicator variable which activates if the magnitude of the slip ...
- **p. 7 / VI. EXPERIMENTAL RESULTS - extractive body cue:** During training, we set the slip angle threshold to 15.76 degrees (0.275 radians), and for the final testing runs we raised it to 21.5 degrees ...
- **p. 7 / VI. EXPERIMENTAL RESULTS - extractive body cue:** Slip 10 m/s 10.34 9.93 8.05 38.68 11 m/s 9.97 9.43 8.71 34.65 12 m/s 9.88 9.47 8.63 43.72 13 m/s 9.74 9.36 8.44 48.70 ...
- **p. 5 / V. SIMULATED RESULTS - extractive body cue:** The temperature was set as λ = 1 and the system noise to (2.5, .25, .25, .25), where the 2.5 value corresponds to the thrust ...

- **PDF anchors reviewed:** datasets p. 5 (V. SIMULATED RESULTS), p. 6 (VI. EXPERIMENTAL RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS), p. 5 (V. SIMULATED RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS), p. 6 (VI. EXPERIMENTAL RESULTS), metrics p. 6 (V. SIMULATED RESULTS), p. 6 (V. SIMULATED RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS), p. 7 (Figure/Table caption), p. 5 (V. SIMULATED RESULTS), p. 5 (V. SIMULATED RESULTS), baselines p. 6 (VI. EXPERIMENTAL RESULTS), p. 5 (V. SIMULATED RESULTS), results p. 5 (V. SIMULATED RESULTS), p. 6 (V. SIMULATED RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS), p. 6 (V. SIMULATED RESULTS), p. 7 (VI. EXPERIMENTAL RESULTS), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
