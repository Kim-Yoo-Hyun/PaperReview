# Evaluation - TACTO: A Fast, Flexible, and Open-source Simulator for High-Resolution Vision-based Tactile Sensors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/LRA.2022.3146945; PDF retrieval source: https://doi.org/10.1109/LRA.2022.3146945. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (IV. SIMULATED EXPERIMENTS), p. 5 (IV. SIMULATED EXPERIMENTS), p. 7 (V. SIM2REAL EXPERIMENTS), p. 7 (IV. SIMULATED EXPERIMENTS), p. 6 (IV. SIMULATED EXPERIMENTS), p. 4 (Figure/Table caption)): Results show that learning grasp stability from touch needs significantly less amount of data to achieve relative high accuracy compared to vision, and that increasing the amount of data helps ...

## Evaluation Body Digest

- **p. 6 / IV. SIMULATED EXPERIMENTS - extractive body cue:** The vertical dashed line shows the largest dataset collected on real robot [6].
- **p. 5 / IV. SIMULATED EXPERIMENTS - extractive body cue:** We choose these two tasks based on previous works with real robots[6], [27] for better comparison between simulated and real environments.
- **p. 5 / IV. SIMULATED EXPERIMENTS - extractive body cue:** The experiments in simulation achieve similar results to the ones with real robots, which demonstrates the effectiveness and potentials of the simulated environment.
- **p. 6 / IV. SIMULATED EXPERIMENTS - extractive body cue:** In our experiment, we used a single box object for demonstration purposes, but it would be straightforward to extend to various object datasets, such as ...
- **p. 7 / IV. SIMULATED EXPERIMENTS - extractive body cue:** Learning In-hand Marble Manipulation In this task, we learn in simulation to roll a marble to target locations in the sensor coordinate, following the previous ...
- **p. 7 / IV. SIMULATED EXPERIMENTS - extractive body cue:** Our main purpose here is to validate the simulation system, and provide benchmark experiments, however, the controller can be replaced by model predictive control and/or ...
- **p. 7 / IV. SIMULATED EXPERIMENTS - extractive body cue:** The cost is defined as cumulative error distance in tactile space P t ∥¯xt∥, and we set eight different target locations and take the average ...
- **p. 7 / V. SIM2REAL EXPERIMENTS - extractive body cue:** We repeat the experiments 5 times, and report the mean error ± standard deviation.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** physics simulation의 robot/environment model.
- **Input boundary:** simulated state, geometry, contact와 control input.
- **Output/decision under evaluation:** simulation step, trajectory 또는 environment query.
- **Primary target:** physical plausibility, speed, reproducibility와 task utility.
- **Detected evaluation headings:** IV. SIMULATED EXPERIMENTS (p. 5); V. SIM2REAL EXPERIMENTS (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| IV. SIMULATED EXPERIMENTS | BENCHMARK / DATASET | Results show that learning grasp stability from touch needs significantly less amount of data to achieve relative high accuracy compared to vision, and that ... | p. 6 (IV. SIMULATED EXPERIMENTS) |
| IV. SIMULATED EXPERIMENTS | BENCHMARK / DATASET | The experiments in simulation achieve similar results to the ones with real robots, which demonstrates the effectiveness and potentials of the simulated environment. | p. 5 (IV. SIMULATED EXPERIMENTS) |
| V. SIM2REAL EXPERIMENTS | BENCHMARK / DATASET | Without any real data, Sim2Real with augmentation can achieve comparable results with Real2Real (64). | p. 7 (V. SIM2REAL EXPERIMENTS) |
| IV. SIMULATED EXPERIMENTS | BENCHMARK / DATASET | Since there are rich contacts with friction happening during the rolling, we aim to investigate how stable the TACTO and PyBullet are, and explore ... | p. 7 (IV. SIMULATED EXPERIMENTS) |
| IV. SIMULATED EXPERIMENTS | BENCHMARK / DATASET | To evaluate the performance of different dataset sizes, we used K-fold cross-validation and computed the median and 68% percentile of the classification accuracy. | p. 6 (IV. SIMULATED EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 6 / IV. SIMULATED EXPERIMENTS - extractive body cue:** The vertical dashed line shows the largest dataset collected on real robot [6].
- **p. 5 / IV. SIMULATED EXPERIMENTS - extractive body cue:** We choose these two tasks based on previous works with real robots[6], [27] for better comparison between simulated and real environments.
- **p. 5 / IV. SIMULATED EXPERIMENTS - extractive body cue:** The experiments in simulation achieve similar results to the ones with real robots, which demonstrates the effectiveness and potentials of the simulated environment.
- **p. 6 / IV. SIMULATED EXPERIMENTS - extractive body cue:** In our experiment, we used a single box object for demonstration purposes, but it would be straightforward to extend to various object datasets, such as ...
- **p. 7 / IV. SIMULATED EXPERIMENTS - extractive body cue:** Learning In-hand Marble Manipulation In this task, we learn in simulation to roll a marble to target locations in the sensor coordinate, following the previous ...
- **p. 7 / IV. SIMULATED EXPERIMENTS - extractive body cue:** Our main purpose here is to validate the simulation system, and provide benchmark experiments, however, the controller can be replaced by model predictive control and/or ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: We open-source TACTO - a simulator of vision-based tactile sensors. TACTO produces high-resolution and high-fidelity reading from tactile sensors at high-frequency (>100 Hz). ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: Software Architecture. TACTO bridges between physics simulator and back-end rendering engine, and can be configured to model different sensor designs through configuration files. ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 3: Workflow showing the functionality of TACTO at three major phases. (1) Initialize: create the sensor structure in the renderer; (2) Create scene: parse ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 4: Example images of simulated DIGIT imprints. TACTO is able to generate color and depth images at the same time with details of the ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 5: Example images of a simulated OmniTact [3] touching a sphere. We show only 3 of the 5 cameras mounted on the sensor. It ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 6: If readings from a real-world sensor are available, TACTO allows to fine-tune the simulator using the real-world data. This is achieved by calculating ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 7: Comparison of simulation and real signals with contacts across the sensor. TACTO captures the non-uniform light distribution similar to the real signals. The ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 8: TACTO supports rendering shadows to obtain more realistic simula- tions. The real-world measurement is collected from a DIGIT sensor touching a ball of ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The vertical dashed line shows the largest dataset collected on real robot [6]. | embodiment, simulator version and control stack | p. 6 (IV. SIMULATED EXPERIMENTS), p. 5 (IV. SIMULATED EXPERIMENTS) |
| Task/environment | We choose these two tasks based on previous works with real robots[6], [27] for better comparison between simulated and real environments. | reset, timeout, object/scene variation | p. 5 (IV. SIMULATED EXPERIMENTS), p. 5 (IV. SIMULATED EXPERIMENTS) |
| Observation/sensor | simulated state, geometry, contact와 control input | calibration, preprocessing, privileged input | p. 3 (1. Phong's model for RGB rendering from Depth (simple), p. 3 (1. Phong's model for RGB rendering from Depth (simple) |
| Output/decision | simulation step, trajectory 또는 environment query | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The cost is defined as cumulative error distance in tactile space P t ∥¯xt∥, and we set eight different target locations and take the ... | definition/direction/unit from same section | p. 7 (IV. SIMULATED EXPERIMENTS) |
| We repeat the experiments 5 times, and report the mean error ± standard deviation. | definition/direction/unit from same section | p. 7 (V. SIM2REAL EXPERIMENTS) |
| To evaluate the performance of different dataset sizes, we used K-fold cross-validation and computed the median and 68% percentile of the classification accuracy. | definition/direction/unit from same section | p. 6 (IV. SIMULATED EXPERIMENTS) |
| Results show that learning grasp stability from touch needs significantly less amount of data to achieve relative high accuracy compared to vision, and that ... | definition/direction/unit from same section | p. 6 (IV. SIMULATED EXPERIMENTS) |
| The goal is to predict whether a grasped object will be successfully lifted, based on the touch | definition/direction/unit from same section | p. 5 (IV. SIMULATED EXPERIMENTS) |
| We now demonstrate TACTO on a perception task to learn grasp stability from touch, and on a control task to manipulate a marble between ... | definition/direction/unit from same section | p. 5 (IV. SIMULATED EXPERIMENTS) |
| Fig. 1: We open-source TACTO - a simulator of vision-based tactile sensors. TACTO produces high-resolution and high-fidelity reading from tactile sensors at high-frequency (>100 ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Fig. 4: Example images of simulated DIGIT imprints. TACTO is able to generate color and depth images at the same time with details of ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Results show that learning grasp stability from touch needs significantly less amount of data to achieve relative high accuracy compared to vision, and that ... | comparison identity and matched condition | p. 6 (IV. SIMULATED EXPERIMENTS) |
| When mixed with real data, Sim2Real consistently outperforms Real2Real with the same amount of real data. | comparison identity and matched condition | p. 7 (V. SIM2REAL EXPERIMENTS) |
| WANG et al.: A SIMULATOR FOR HIGH-RESOLUTION VISION-BASED TACTILE SENSORS 7 achieved comparable results to the combined model, we think the difference can increase ... | comparison identity and matched condition | p. 7 (IV. SIMULATED EXPERIMENTS) |
| We choose these two tasks based on previous works with real robots[6], [27] for better comparison between simulated and real environments. | comparison identity and matched condition | p. 5 (IV. SIMULATED EXPERIMENTS) |
| Fig. 3: Workflow showing the functionality of TACTO at three major phases. (1) Initialize: create the sensor structure in the renderer; (2) Create scene: ... | comparison identity and matched condition | p. 2 (Figure/Table caption) |
| Fig. 7: Comparison of simulation and real signals with contacts across the sensor. TACTO captures the non-uniform light distribution similar to the real signals. ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| From the results in Table II, we can observe the sim2real gap (Sim2Real without augmentation). | component/input/data sensitivity | p. 7 (V. SIM2REAL EXPERIMENTS) |
| Without any real data, Sim2Real with augmentation can achieve comparable results with Real2Real (64). | component/input/data sensitivity | p. 7 (V. SIM2REAL EXPERIMENTS) |
| Fig. 6: If readings from a real-world sensor are available, TACTO allows to fine-tune the simulator using the real-world data. This is achieved by ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Fig. 7: Comparison of simulation and real signals with contacts across the sensor. TACTO captures the non-uniform light distribution similar to the real signals. ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| This allows to perform orders of magnitude more experiments at a fraction of the effort, and in many cases of the time. | Results show that learning grasp stability from touch needs significantly less amount of data to achieve relative high accuracy compared to vision, and that ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (IV. SIMULATED EXPERIMENTS), p. 5 (IV. SIMULATED EXPERIMENTS), p. 7 (V. SIM2REAL EXPERIMENTS), p. 7 (IV. SIMULATED EXPERIMENTS), p. 6 (IV. SIMULATED EXPERIMENTS), p. 4 (Figure/Table caption) |
| Primary metric/result | The experiments in simulation achieve similar results to the ones with real robots, which demonstrates the effectiveness and potentials of the simulated environment. | numeric claim only at cited anchor | p. 5 (IV. SIMULATED EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 6 / IV. SIMULATED EXPERIMENTS - extractive body cue:** We trained 10 epochs for each dataset size using Adam optimizer [32] with a learning rate of 5e-4 and batch size of 32.
- **p. 7 / IV. SIMULATED EXPERIMENTS - extractive body cue:** It includes 6 minutes for optimizing the acquisition function, and 2 minutes for simulation, where there are 50 iterations, and each iteration includes 50 steps ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In the failure grasp, the object is only grasped by the corner and begins to slip after being lifted. | p. 6 (IV. SIMULATED EXPERIMENTS) |
| body limitation/failure cue | (Left) Examples of a successful grasp and a failure grasp. | p. 6 (IV. SIMULATED EXPERIMENTS) |
| body limitation/failure cue | Fig. 8: TACTO supports rendering shadows to obtain more realistic simula- tions. The real-world measurement is collected from a DIGIT sensor touching a ball ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | It makes the model more robust to a variety of illumination conditions (Sim2Real with augmentation vs. | p. 7 (V. SIM2REAL EXPERIMENTS) |
| body limitation/failure cue | The cost is defined as cumulative error distance in tactile space P t ∥¯xt∥, and we set eight different target locations and take the ... | p. 7 (IV. SIMULATED EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We trained 10 epochs for each dataset size using Adam optimizer [32] with a learning rate of 5e-4 and batch size of 32. | p. 6 (IV. SIMULATED EXPERIMENTS) |
| To evaluate the performance of different dataset sizes, we used K-fold cross-validation and computed the median and 68% percentile of the classification accuracy. | p. 6 (IV. SIMULATED EXPERIMENTS) |
| During the experiments, we validate that both PyBullet and TACTO run as expected without abnormal situations. | p. 7 (IV. SIMULATED EXPERIMENTS) |
| It includes 6 minutes for optimizing the acquisition function, and 2 minutes for simulation, where there are 50 iterations, and each iteration includes 50 ... | p. 7 (IV. SIMULATED EXPERIMENTS) |
| Although it can be extended to support more ray-tracing functionalities, this may require non-trivial engineering time to re-implement methods with GPU acceleration which are ... | p. 3 (1. Phong's model for RGB rendering from Depth (simple) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / IV. SIMULATED EXPERIMENTS - extractive body cue:** In the failure grasp, the object is only grasped by the corner and begins to slip after being lifted.
- **p. 6 / IV. SIMULATED EXPERIMENTS - extractive body cue:** (Left) Examples of a successful grasp and a failure grasp.
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 8: TACTO supports rendering shadows to obtain more realistic simula- tions. The real-world measurement is collected from a DIGIT sensor touching a ball of ...
- **p. 7 / V. SIM2REAL EXPERIMENTS - extractive body cue:** It makes the model more robust to a variety of illumination conditions (Sim2Real with augmentation vs.
- **p. 7 / IV. SIMULATED EXPERIMENTS - extractive body cue:** The cost is defined as cumulative error distance in tactile space P t ∥¯xt∥, and we set eight different target locations and take the average ...

- **Evidence anchors reviewed:** datasets p. 6 (IV. SIMULATED EXPERIMENTS), p. 5 (IV. SIMULATED EXPERIMENTS), p. 5 (IV. SIMULATED EXPERIMENTS), p. 6 (IV. SIMULATED EXPERIMENTS), p. 7 (IV. SIMULATED EXPERIMENTS), p. 7 (IV. SIMULATED EXPERIMENTS), metrics p. 7 (IV. SIMULATED EXPERIMENTS), p. 7 (V. SIM2REAL EXPERIMENTS), p. 6 (IV. SIMULATED EXPERIMENTS), p. 6 (IV. SIMULATED EXPERIMENTS), p. 5 (IV. SIMULATED EXPERIMENTS), p. 5 (IV. SIMULATED EXPERIMENTS), baselines p. 6 (IV. SIMULATED EXPERIMENTS), p. 7 (V. SIM2REAL EXPERIMENTS), p. 7 (IV. SIMULATED EXPERIMENTS), p. 5 (IV. SIMULATED EXPERIMENTS), p. 2 (Figure/Table caption), p. 4 (Figure/Table caption), results p. 6 (IV. SIMULATED EXPERIMENTS), p. 5 (IV. SIMULATED EXPERIMENTS), p. 7 (V. SIM2REAL EXPERIMENTS), p. 7 (IV. SIMULATED EXPERIMENTS), p. 6 (IV. SIMULATED EXPERIMENTS), p. 4 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
