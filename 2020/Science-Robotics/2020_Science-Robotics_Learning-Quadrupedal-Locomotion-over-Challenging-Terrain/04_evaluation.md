# Evaluation - Learning Quadrupedal Locomotion over Challenging Terrain

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2010.11251; PDF retrieval source: https://arxiv.org/pdf/2010.11251. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 4 (2. RESULTS), p. 4 (2. RESULTS), p. 5 (2. RESULTS), p. 5 (2. RESULTS), p. 3 (2. RESULTS), p. 6 (2. RESULTS)): (E) Success rates for different step heights.

## Evaluation Body Digest

- **p. 5 / 2. RESULTS - extractive body cue:** The objective of the competition is to develop robotic systems that rapidly map, navigate, and search complex underground environments, including tunnels, urban underground, and cave ...
- **p. 3 / 2. RESULTS - extractive body cue:** The robots have different kinematics, inertia, and actuators.
- **p. 3 / 2. RESULTS - extractive body cue:** We have deployed the trained locomotion controller on two generations of ANYmal robots: ANYmal-B (Fig.
- **p. 4 / 2. RESULTS - extractive body cue:** 0 ◦refers to the front of the robot.
- **p. 4 / 2. RESULTS - extractive body cue:** The robot steps onto loose boards (highlighted in red and blue) that dislodge under the robot's feet.
- **p. 5 / 2. RESULTS - extractive body cue:** The robot moves omnidirectionally over the area.
- **p. 6 / 2. RESULTS - extractive body cue:** The heading error is the angle between the command velocity and the base velocity of the robot.
- **p. 6 / 2. RESULTS - extractive body cue:** This payload is 22.7 % of the total weight of the robot, and was never simulated during training.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** legged robot, terrain과 contact dynamics.
- **Input boundary:** proprioception, terrain/perception observation과 velocity command.
- **Output/decision under evaluation:** joint target, torque, footstep 또는 locomotion action.
- **Primary target:** velocity/progress, stability, energy와 terrain generalization.
- **Detected evaluation headings:** 2. RESULTS (p. 3).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 2. RESULTS | EMPIRICAL / SIMULATION | (E) Success rates for different step heights. | p. 4 (2. RESULTS) |
| 2. RESULTS | EMPIRICAL / SIMULATION | The success rate is evaluated over 10 trials for each condition. | p. 4 (2. RESULTS) |
| 2. RESULTS | EMPIRICAL / SIMULATION | The success rates are given in Fig. | p. 5 (2. RESULTS) |
| 2. RESULTS | EMPIRICAL / SIMULATION | We conducted 10 trials for each step height and computed the success rate. | p. 5 (2. RESULTS) |
| 2. RESULTS | EMPIRICAL / SIMULATION | Movie 1 summarizes the results of the presented work. | p. 3 (2. RESULTS) |

## Dataset / Benchmark Role

- **p. 5 / 2. RESULTS - extractive body cue:** The objective of the competition is to develop robotic systems that rapidly map, navigate, and search complex underground environments, including tunnels, urban underground, and cave ...
- **p. 3 / 2. RESULTS - extractive body cue:** The robots have different kinematics, inertia, and actuators.
- **p. 3 / 2. RESULTS - extractive body cue:** We have deployed the trained locomotion controller on two generations of ANYmal robots: ANYmal-B (Fig.
- **p. 4 / 2. RESULTS - extractive body cue:** 0 ◦refers to the front of the robot.
- **p. 4 / 2. RESULTS - extractive body cue:** The robot steps onto loose boards (highlighted in red and blue) that dislodge under the robot's feet.
- **p. 5 / 2. RESULTS - extractive body cue:** The robot moves omnidirectionally over the area.
- **p. 6 / 2. RESULTS - extractive body cue:** The heading error is the angle between the command velocity and the base velocity of the robot.
- **p. 6 / 2. RESULTS - extractive body cue:** This payload is 22.7 % of the total weight of the robot, and was never simulated during training.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1. Deployment of the presented locomotion controller in a variety of challenging environments.
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. A number of specific deployments. (A-F) Zero-shot gener- alization to slippery and deforming terrain. (G) Steep descent during the DARPA Subterranean Challenge. The ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. Evaluation in an indoor environment. (A) Locomotion over unstable debris. The robot steps onto loose boards (highlighted in red and blue) that dislodge ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. Comparison of locomotion performance in natural envi- ronments. The mechanical COT is computed using positive mechan- ical power exerted by the actuators. mountain ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4. Overview of the presented approach. (A) Two-stage training process. First, a teacher policy is trained using reinforcement learning in simulation. It has access ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 5. Ablation studies. We trained each model 5 times using different random seeds. Error bars denote 95 % confidence intervals. (A) Test setups. The ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 6. Analysis of the emergent foot-trapping reflex. FT denotes the first contact of the LF foot with the step (foot-trapping event). (A) The LF ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The objective of the competition is to develop robotic systems that rapidly map, navigate, and search complex underground environments, including tunnels, urban underground, and ... | embodiment, simulator version and control stack | p. 5 (2. RESULTS), p. 3 (2. RESULTS) |
| Task/environment | The robots have different kinematics, inertia, and actuators. | reset, timeout, object/scene variation | p. 3 (2. RESULTS), p. 3 (2. RESULTS) |
| Observation/sensor | proprioception, terrain/perception observation과 velocity command | calibration, preprocessing, privileged input | p. 6 (4. MATERIALS AND METHODS), p. 6 (4. MATERIALS AND METHODS) |
| Output/decision | joint target, torque, footstep 또는 locomotion action | action frame, controller and termination | p. 7 (4. MATERIALS AND METHODS), p. 3 (1. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Research Article ETH Zurich and Intel 4 B A command C command 10 kg payload D Baseline 0.2 m/s Ours w/ payload Baseline 0.6 ... | definition/direction/unit from same section | p. 4 (2. RESULTS) |
| Fig. 3. Evaluation in an indoor environment. (A) Locomotion over unstable debris. The robot steps onto loose boards (highlighted in red and blue) that ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Fig. 5. Ablation studies. We trained each model 5 times using different random seeds. Error bars denote 95 % confidence intervals. (A) Test setups. ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| The success rates are given in Fig. | definition/direction/unit from same section | p. 5 (2. RESULTS) |
| We conducted 10 trials for each step height and computed the success rate. | definition/direction/unit from same section | p. 5 (2. RESULTS) |
| 3G shows the heading error of the controllers in each commanded direction. | definition/direction/unit from same section | p. 6 (2. RESULTS) |
| The heading error is the angle between the command velocity and the base velocity of the robot. | definition/direction/unit from same section | p. 6 (2. RESULTS) |
| Fig. 6. Analysis of the emergent foot-trapping reflex. FT denotes the first contact of the LF foot with the step (foot-trapping event). (A) The ... | definition/direction/unit from same section | p. 11 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We have compared the presented controller to a state-of-the-art baseline [1, 26] in the forest environment. | comparison identity and matched condition | p. 5 (2. RESULTS) |
| The presented controller outperforms the baseline in both stepping up and down. | comparison identity and matched condition | p. 5 (2. RESULTS) |
| Our controller and a baseline [1, 26] are commanded to walk over a step with and without the 10 kg payload. | comparison identity and matched condition | p. 4 (2. RESULTS) |
| The heading error of the presented controller is consistently smaller than the baseline, both with and without the payload. | comparison identity and matched condition | p. 6 (2. RESULTS) |
| Research Article ETH Zurich and Intel 4 B A command C command 10 kg payload D Baseline 0.2 m/s Ours w/ payload Baseline 0.6 ... | comparison identity and matched condition | p. 4 (2. RESULTS) |
| The baseline quickly loses balance, aggressively swings the legs, and falls. | comparison identity and matched condition | p. 6 (2. RESULTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig. 5. Ablation studies. We trained each model 5 times using different random seeds. Error bars denote 95 % confidence intervals. (A) Test setups. ... | component/input/data sensitivity | p. 10 (Figure/Table caption) |
| Our controller and a baseline [1, 26] are commanded to walk over a step with and without the 10 kg payload. | component/input/data sensitivity | p. 4 (2. RESULTS) |
| The baseline showed high sensitivity to foot-trapping, which often led to a fall, as shown in Movie S3. | component/input/data sensitivity | p. 5 (2. RESULTS) |
| Accordingly, the locomotion controller needs to perform without failure over extended mission durations. | component/input/data sensitivity | p. 5 (2. RESULTS) |
| In contrast, the average heading error of the presented controller stays within 10 ◦with or without the payload. | component/input/data sensitivity | p. 6 (2. RESULTS) |
| The heading error of the presented controller is consistently smaller than the baseline, both with and without the payload. | component/input/data sensitivity | p. 6 (2. RESULTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Here we present a radically robust controller for blind quadrupedal locomotion on challenging terrain. | (E) Success rates for different step heights. | PDF body cue; verify exact table/figure and matched conditions | p. 4 (2. RESULTS), p. 4 (2. RESULTS), p. 5 (2. RESULTS), p. 5 (2. RESULTS), p. 3 (2. RESULTS), p. 6 (2. RESULTS) |
| Primary metric/result | The success rate is evaluated over 10 trials for each condition. | numeric claim only at cited anchor | p. 4 (2. RESULTS) |

- Numeric sentences retained from the body:
- **p. 4 / 2. RESULTS - extractive body cue:** Research Article ETH Zurich and Intel 4 B A command C command 10 kg payload D Baseline 0.2 m/s Ours w/ payload Baseline 0.6 m/s ...
- **p. 4 / 2. RESULTS - extractive body cue:** The success rate is evaluated over 10 trials for each condition.
- **p. 5 / 2. RESULTS - extractive body cue:** In each trial, the robot is driven straight to a step for 10 s.
- **p. 5 / 2. RESULTS - extractive body cue:** We conducted 10 trials for each step height and computed the success rate.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We see a number of limitations and opportunities for future work. | p. 6 (3. DISCUSSION) |
| body limitation/failure cue | Support surfaces are unstable and the robot's feet frequently slip. | p. 5 (2. RESULTS) |
| body limitation/failure cue | The baseline's catastrophic failures are not factored into these measurements: when the baseline fails, it is reset by a human operator in a more ... | p. 5 (2. RESULTS) |
| body limitation/failure cue | This is a significant advantage in that the controller makes few assumptions on the sensor suite and is not susceptible to failure when exteroception ... | p. 6 (3. DISCUSSION) |
| body limitation/failure cue | Fig. 2. A number of specific deployments. (A-F) Zero-shot gener- alization to slippery and deforming terrain. (G) Steep descent during the DARPA Subterranean Challenge. ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | (A) Locomotion over unstable debris. | p. 4 (2. RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We conducted 10 trials for each step height and computed the success rate. | p. 5 (2. RESULTS) |
| (D) Controlled experiments with steps and payload. | p. 4 (2. RESULTS) |
| The success rate is evaluated over 10 trials for each condition. | p. 4 (2. RESULTS) |
| In each trial, the robot is driven straight to a step for 10 s. | p. 5 (2. RESULTS) |
| The vectors ¯lt and ¯at computed by the teacher policy are used to supervise the student. | p. 6 (4. MATERIALS AND METHODS) |
| The baseline is incapable of traversing any steps under any command speed with the payload. | p. 6 (2. RESULTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 3. DISCUSSION - extractive body cue:** We see a number of limitations and opportunities for future work.
- **p. 5 / 2. RESULTS - extractive body cue:** Support surfaces are unstable and the robot's feet frequently slip.
- **p. 5 / 2. RESULTS - extractive body cue:** The baseline's catastrophic failures are not factored into these measurements: when the baseline fails, it is reset by a human operator in a more stable ...
- **p. 6 / 3. DISCUSSION - extractive body cue:** This is a significant advantage in that the controller makes few assumptions on the sensor suite and is not susceptible to failure when exteroception breaks ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. A number of specific deployments. (A-F) Zero-shot gener- alization to slippery and deforming terrain. (G) Steep descent during the DARPA Subterranean Challenge. The ...
- **p. 4 / 2. RESULTS - extractive body cue:** (A) Locomotion over unstable debris.

- **PDF anchors reviewed:** datasets p. 5 (2. RESULTS), p. 3 (2. RESULTS), p. 3 (2. RESULTS), p. 4 (2. RESULTS), p. 4 (2. RESULTS), p. 5 (2. RESULTS), metrics p. 4 (2. RESULTS), p. 4 (Figure/Table caption), p. 10 (Figure/Table caption), p. 5 (2. RESULTS), p. 5 (2. RESULTS), p. 6 (2. RESULTS), baselines p. 5 (2. RESULTS), p. 5 (2. RESULTS), p. 4 (2. RESULTS), p. 6 (2. RESULTS), p. 4 (2. RESULTS), p. 6 (2. RESULTS), results p. 4 (2. RESULTS), p. 4 (2. RESULTS), p. 5 (2. RESULTS), p. 5 (2. RESULTS), p. 3 (2. RESULTS), p. 6 (2. RESULTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
