# Evaluation - Novel Demonstration Generation with Gaussian Splatting Enables Robust One-Shot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p146.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p146.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (Figure/Table caption), p. 7 (A. Experimental Setup), p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), p. 1 (Figure/Table caption), p. 4 (Figure/Table caption)): Fig. 11: Performance on cross embodiment experiments. We evaluate the learned policy directly on the URSe robot and achieve a nearly 100% success rate that surpasses the 2D augmentation methods,

## Evaluation Body Digest

- **p. 7 / A. Experimental Setup - extractive body cue:** We design five manipulation tasks for real-world evaluation: Pick Object, Close Drawer, Pick-PlaceClose, Dual Pick-Place and Sweep, whose details are elaborated in Sec.
- **p. 6 / A. Experimental Setup - extractive body cue:** 5, Concretely, we collect the expert demonstration on Franka Research 3 (FR3) Robot.
- **p. 6 / A. Experimental Setup - extractive body cue:** In Sweep task, the robot should first pick up a broom and then sweeps the chocolate beans into a dustpan.
- **p. 7 / A. Experimental Setup - extractive body cue:** We also condluct extensive real-world experiments to prove the effectiveness of our data generation pipeline in terms of different types of generalization.
- **p. 7 / A. Experimental Setup - extractive body cue:** Success rate (SR) is chosen as the evaluation metric in all experiments.
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 9: Performance when changing lighting conditions and appearance. We report the success rate of different policies
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 11: Performance on cross embodiment experiments. We evaluate the learned policy directly on the URSe robot and achieve a nearly 100% success rate that ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: Main results. Top left: We present the average success rate across five tasks. Our method shows promising scalability as the number of demonstration ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** demonstration으로 정의된 robot task distribution.
- **Input boundary:** observation history와 expert trajectory/action.
- **Output/decision under evaluation:** predicted action 또는 action chunk.
- **Primary target:** imitation error, task success, robustness와 compounding error.
- **Detected evaluation headings:** A. Experimental Setup (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 11: Performance on cross embodiment experiments. We evaluate the learned policy directly on the URSe robot and achieve a nearly 100% success rate ... | p. 10 (Figure/Table caption) |
| A. Experimental Setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | Success rate (SR) is chosen as the evaluation metric in all experiments. | p. 7 (A. Experimental Setup) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 7: Main results. Top left: We present the average success rate across five tasks. Our method shows promising scalability as the number of ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 9: Performance when changing lighting conditions and appearance. We report the success rate of different policies | p. 9 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 1: Starting from a single expert demonstration and multi-view images, our method generates diverse and visu realistic data for policy learning, enabling robust ... | p. 1 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / A. Experimental Setup - extractive body cue:** We design five manipulation tasks for real-world evaluation: Pick Object, Close Drawer, Pick-PlaceClose, Dual Pick-Place and Sweep, whose details are elaborated in Sec.
- **p. 6 / A. Experimental Setup - extractive body cue:** 5, Concretely, we collect the expert demonstration on Franka Research 3 (FR3) Robot.
- **p. 6 / A. Experimental Setup - extractive body cue:** In Sweep task, the robot should first pick up a broom and then sweeps the chocolate beans into a dustpan.
- **p. 7 / A. Experimental Setup - extractive body cue:** We also condluct extensive real-world experiments to prove the effectiveness of our data generation pipeline in terms of different types of generalization.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Starting from a single expert demonstration and multi-view images, our method generates diverse and visu realistic data for policy learning, enabling robust performance ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Method overview. We start from a single manually collected demonstration and multi-view images that capture the whole scene. ‘The former provides task-related keyframes, ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Comparison of frame alignment results between ICP and fine-grained optimization with differentiable ren- dering. The semi-transparent orange overlay represents the ground truth rendered ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 4: Illustration of frame alignment with differentiable rendering. The loss is calculated between the mask rendered using Gaussian Splatting and the mask rendered with ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Real-world experiment setup. We employ a Franka Research 3 Robot and two eye-on-base RealSense D43Si
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Task illustration. We design five manipulation tasks for real-world evaluation: Pick Object, Close Drawer, Pick-Place- Close, Dual Pick-Place and Sweep, whose details are ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: Main results. Top left: We present the average success rate across five tasks. Our method shows promising scalability as the number of demonstration ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 8: Illustration of real-world experiments for different generalization types. The data is collected in the original setting, ‘When deploying the trained policy, we modify ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We design five manipulation tasks for real-world evaluation: Pick Object, Close Drawer, Pick-PlaceClose, Dual Pick-Place and Sweep, whose details are elaborated in Sec. | embodiment, simulator version and control stack | p. 7 (A. Experimental Setup), p. 6 (A. Experimental Setup) |
| Task/environment | 5, Concretely, we collect the expert demonstration on Franka Research 3 (FR3) Robot. | reset, timeout, object/scene variation | p. 6 (A. Experimental Setup), p. 6 (A. Experimental Setup) |
| Observation/sensor | observation history와 expert trajectory/action | calibration, preprocessing, privileged input | p. 4 (A. Reconstruction and Preprocessing), p. 6 (C. Policy Training) |
| Output/decision | predicted action 또는 action chunk | action frame, controller and termination | p. 6 (C. Policy Training), p. 2 (B. Data Augmentation for Policy Learning) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Success rate (SR) is chosen as the evaluation metric in all experiments. | definition/direction/unit from same section | p. 7 (A. Experimental Setup) |
| Fig. 9: Performance when changing lighting conditions and appearance. We report the success rate of different policies | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Fig. 11: Performance on cross embodiment experiments. We evaluate the learned policy directly on the URSe robot and achieve a nearly 100% success rate ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| Fig. 7: Main results. Top left: We present the average success rate across five tasks. Our method shows promising scalability as the number of ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Fig. 3: Comparison of frame alignment results between ICP and fine-grained optimization with differentiable ren- dering. The semi-transparent orange overlay represents the ground truth ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Fig. 1: Starting from a single expert demonstration and multi-view images, our method generates diverse and visu realistic data for policy learning, enabling robust ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Task setups are illustrated in Fig. | definition/direction/unit from same section | p. 6 (A. Experimental Setup) |
| We employ a 3D SpaceMouse to collect teleoperated demonstrations at a frequency of 10 Hz, Policy inference is carried out on an NVIDIA RTX4090 ... | definition/direction/unit from same section | p. 6 (A. Experimental Setup) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 3: Comparison of frame alignment results between ICP and fine-grained optimization with differentiable ren- dering. The semi-transparent orange overlay represents the ground truth ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| no ablation sentence selected | not reported; proposed stress test only | verify ablation section |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our method enables autonomous editing of the reconstructed scene to generate diverse demonstrations with various configurations. | Fig. 11: Performance on cross embodiment experiments. We evaluate the learned policy directly on the URSe robot and achieve a nearly 100% success rate ... | PDF body cue; verify exact table/figure and matched conditions | p. 10 (Figure/Table caption), p. 7 (A. Experimental Setup), p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), p. 1 (Figure/Table caption), p. 4 (Figure/Table caption) |
| Primary metric/result | Success rate (SR) is chosen as the evaluation metric in all experiments. | numeric claim only at cited anchor | p. 7 (A. Experimental Setup) |

- Numeric sentences retained from the body:
- **p. 6 / A. Experimental Setup - extractive body cue:** We employ a 3D SpaceMouse to collect teleoperated demonstrations at a frequency of 10 Hz, Policy inference is carried out on an NVIDIA RTX4090 GPU. ...
- **p. 7 / A. Experimental Setup - extractive body cue:** Each policy is evaluated with 30 trials for a certain evaluation setting.
- **p. 6 / C. Policy Training - extractive body cue:** We denote 0, # (Ii, 4x) as the observation at the k-th frame of demonstrations D, and as our policy.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The drawer is placed in a Sem%Sem workspace, with a fixed orientation, The target object is located in a 1em> 10em workspace, whose rotation ... | p. 6 (A. Experimental Setup) |
| body limitation/failure cue | Fig. 1: Starting from a single expert demonstration and multi-view images, our method generates diverse and visu realistic data for policy learning, enabling robust ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Robustness when Facing Various Deployment Settings | p. 7 (B. Eficiency of Augmenting Demonstrations) |
| body limitation/failure cue | In particular, our policy achieves 100% success rate on the Pick Object task, showcasing strong robustness against various background appearance. | p. 8 (2) Scene Appearance) |
| body limitation/failure cue | Notably, our policy achieves nearly 100% success rate (on Close Drawer task, manifesting strong robustness against novel camera views and moving cameras, | p. 8 (4) 3200 generated demonstrations with camera view aug) |
| body limitation/failure cue | The data is collected in the original setting, ‘When deploying the trained policy, we modify object poses, lighting conditions, scene appearance, camera views, object ... | p. 9 (3) 6400 demonstrations generated by our pipeline with ob) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The latent of images and robot state is fed into a transformer encoder. | p. 6 (C. Policy Training) |
| Finally, an action decoder utilizes an MLP to convert the action latent into the action vector ay. | p. 6 (C. Policy Training) |
| Each policy is evaluated with 30 trials for a certain evaluation setting. | p. 7 (A. Experimental Setup) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / A. Experimental Setup - extractive body cue:** The drawer is placed in a Sem%Sem workspace, with a fixed orientation, The target object is located in a 1em> 10em workspace, whose rotation falls ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Starting from a single expert demonstration and multi-view images, our method generates diverse and visu realistic data for policy learning, enabling robust performance ...
- **p. 7 / B. Eficiency of Augmenting Demonstrations - extractive body cue:** Robustness when Facing Various Deployment Settings
- **p. 8 / 2) Scene Appearance - extractive body cue:** In particular, our policy achieves 100% success rate on the Pick Object task, showcasing strong robustness against various background appearance.
- **p. 8 / 4) 3200 generated demonstrations with camera view aug - extractive body cue:** Notably, our policy achieves nearly 100% success rate (on Close Drawer task, manifesting strong robustness against novel camera views and moving cameras,
- **p. 9 / 3) 6400 demonstrations generated by our pipeline with ob - extractive body cue:** The data is collected in the original setting, ‘When deploying the trained policy, we modify object poses, lighting conditions, scene appearance, camera views, object types, ...

- **PDF anchors reviewed:** datasets p. 7 (A. Experimental Setup), p. 6 (A. Experimental Setup), p. 6 (A. Experimental Setup), p. 7 (A. Experimental Setup), metrics p. 7 (A. Experimental Setup), p. 9 (Figure/Table caption), p. 10 (Figure/Table caption), p. 8 (Figure/Table caption), p. 4 (Figure/Table caption), p. 1 (Figure/Table caption), baselines p. 4 (Figure/Table caption), results p. 10 (Figure/Table caption), p. 7 (A. Experimental Setup), p. 8 (Figure/Table caption), p. 9 (Figure/Table caption), p. 1 (Figure/Table caption), p. 4 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
