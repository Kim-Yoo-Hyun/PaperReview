# Evaluation - Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1703.06907; PDF retrieval source: https://arxiv.org/pdf/1703.06907. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS)): However, using a pre-trained model can significantly improve performance when less training data is used.

## Evaluation Body Digest

- **p. 4 / IV. EXPERIMENTS - extractive body cue:** The goals of our experiments are: (a) Evaluate the localization accuracy of our trained detectors in the real world, including in the presence of distractor ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Robotics experiments To demonstrate the potential of this technique for transferring robotic behaviors learned in simulation to the real world, 3Note the total number of ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** We did not control for lighting conditions or the rest of the scene around the table (e.g., all images contain part of the robot and ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Each of the eight geometric objects has 60 labeled images in the dataset: 20 with the object alone on the table, 20 in which one ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Even with over-fitting, the accuracy is comparable at a similar distance to the translation error in traditional techniques for pose estimation in clutter from a ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Though the accuracy of our trained detectors is promising, note that they are still over-fitting2 the simulated training data, where error is 0.3 cm to ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** Localization accuracy To evaluate the accuracy of learned detectors in the real world, we captured 480 webcam images of one or more geometric objects on ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** However, using a pre-trained model can significantly improve performance when less training data is used.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** robot/environment의 sequential decision process.
- **Input boundary:** state 또는 observation, action, reward와 transition history.
- **Output/decision under evaluation:** action policy와 induced trajectory.
- **Primary target:** expected return, task success, stability와 sample efficiency.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 4).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / SIMULATION | However, using a pre-trained model can significantly improve performance when less training data is used. | p. 5 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SIMULATION | 1Categories for which the best final performance was achieved for detector trained from scratch. | p. 4 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SIMULATION | Therefore no validation on real data can be done during training. few as 5, 000 training samples, but performance improves up to around 50, ... | p. 5 (IV. EXPERIMENTS) |
| IV. EXPERIMENTS | EMPIRICAL / SIMULATION | We report the performance of the best network. | p. 4 (IV. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 4 / IV. EXPERIMENTS - extractive body cue:** The goals of our experiments are: (a) Evaluate the localization accuracy of our trained detectors in the real world, including in the presence of distractor ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Robotics experiments To demonstrate the potential of this technique for transferring robotic behaviors learned in simulation to the real world, 3Note the total number of ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** We did not control for lighting conditions or the rest of the scene around the table (e.g., all images contain part of the robot and ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Each of the eight geometric objects has 60 labeled images in the dataset: 20 with the object alone on the table, 20 in which one ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Illustration of our approach. An object detector is trained on hundreds of thousands of low-fidelity rendered images with random camera positions, lighting conditions, ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2. The model architecture used in our experiments. Each vertical bar corresponds to a layer of the model. ReLU nonlinearities are used throughout, and ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. The geometric objects used in our experiments. the object and one or more distractors (also from among the geometric object set) on a ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4. Sensitivity of test error on real images to the number of simulated training examples used. Each training example corresponds to a single labeled ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 5. Sensitivity to amount of texture randomization. In each case, the detector was trained using 10, 000 random object positions and combina- tions of ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 6. Two representative executions of grasping objects using vision learned in simulation only. The object detector network estimates the positions of the object of ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7. A selection of randomly textured scenes used in the training phase of our method

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The goals of our experiments are: (a) Evaluate the localization accuracy of our trained detectors in the real world, including in the presence of ... | embodiment, simulator version and control stack | p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Task/environment | Robotics experiments To demonstrate the potential of this technique for transferring robotic behaviors learned in simulation to the real world, 3Note the total number ... | reset, timeout, object/scene variation | p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Observation/sensor | state 또는 observation, action, reward와 transition history | calibration, preprocessing, privileged input | p. 4 (III. METHOD), p. 2 (I. INTRODUCTION) |
| Output/decision | action policy와 induced trajectory | action frame, controller and termination | p. 3 (III. METHOD), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The goals of our experiments are: (a) Evaluate the localization accuracy of our trained detectors in the real world, including in the presence of ... | definition/direction/unit from same section | p. 4 (IV. EXPERIMENTS) |
| Even with over-fitting, the accuracy is comparable at a similar distance to the translation error in traditional techniques for pose estimation in clutter from ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Though the accuracy of our trained detectors is promising, note that they are still over-fitting2 the simulated training data, where error is 0.3 cm ... | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Localization accuracy To evaluate the accuracy of learned detectors in the real world, we captured 480 webcam images of one or more geometric objects ... | definition/direction/unit from same section | p. 4 (IV. EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Randomizing the position of the camera also consistently provides a slight accuracy boost, but reasonably high accuracy is achievable without it. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| Ablation study To evaluate the importance of different factors of our training methodology, we assessed the sensitivity of the algorithm to the following: • ... | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablation study To evaluate the importance of different factors of our training methodology, we assessed the sensitivity of the algorithm to the following: • ... | component/input/data sensitivity | p. 5 (IV. EXPERIMENTS) |
| Fig. 5. Sensitivity to amount of texture randomization. In each case, the detector was trained using 10, 000 random object positions and combina- tions ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our method avoids calibration and precise placement of the camera in the real world by randomizing characteristics of the cameras used to render images ... | However, using a pre-trained model can significantly improve performance when less training data is used. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Primary metric/result | 1Categories for which the best final performance was achieved for detector trained from scratch. | numeric claim only at cited anchor | p. 4 (IV. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** The goals of our experiments are: (a) Evaluate the localization accuracy of our trained detectors in the real world, including in the presence of distractor ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Therefore no validation on real data can be done during training. few as 5, 000 training samples, but performance improves up to around 50, 000 ...
- **p. 4 / III. METHOD - extractive body cue:** Model architecture and training Convolutional layers Fully connected layers (224 x 224 x 64) (112 x 112 x 128) (56 x 56 x 256) (28 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | However, their experiments - collision avoidance in hallways and open spaces - do not demonstrate the ability to deal with high-precision tasks. | p. 3 (II. RELATED WORK) |
| body limitation/failure cue | Our approach also does not rely on precise camera information or calibration, instead randomizing the position, orientation, and field of view of the camera ... | p. 3 (II. RELATED WORK) |
| body limitation/failure cue | The goals of our experiments are: (a) Evaluate the localization accuracy of our trained detectors in the real world, including in the presence of ... | p. 4 (IV. EXPERIMENTS) |
| body limitation/failure cue | Adding noise during pretraining appears to have a negligible effect. | p. 5 (IV. EXPERIMENTS) |
| body limitation/failure cue | Our object detectors are able to localize objects to within 1.5 cm (on average) in the real world and perform well in the presence ... | p. 5 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For each experiment, we performed a small hyperparameter search, evaluating combinations of two learning rates (1e-4 and 2e-4) and three batch sizes (25, 50, ... | p. 4 (IV. EXPERIMENTS) |
| In practice, we found that adding a small amount of random noise to images at training time improves convergence and makes training less susceptible ... | p. 5 (IV. EXPERIMENTS) |
| Domain randomization The purpose of domain randomization is to provide enough simulated variability at training time such that at test time the model is ... | p. 3 (III. METHOD) |
| Random textures are chosen among the following: (a) A random RGB value (b) A gradient between two random RGB values (c) A checker pattern ... | p. 3 (III. METHOD) |
| We found that using a learning rate of around 1e-4 (as opposed to the standard 1e-3 for Adam) improved convergence and helped avoid a ... | p. 4 (III. METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / II. RELATED WORK - extractive body cue:** However, their experiments - collision avoidance in hallways and open spaces - do not demonstrate the ability to deal with high-precision tasks.
- **p. 3 / II. RELATED WORK - extractive body cue:** Our approach also does not rely on precise camera information or calibration, instead randomizing the position, orientation, and field of view of the camera in ...
- **p. 4 / IV. EXPERIMENTS - extractive body cue:** The goals of our experiments are: (a) Evaluate the localization accuracy of our trained detectors in the real world, including in the presence of distractor ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Adding noise during pretraining appears to have a negligible effect.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Our object detectors are able to localize objects to within 1.5 cm (on average) in the real world and perform well in the presence of ...

- **Evidence anchors reviewed:** datasets p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), metrics p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), baselines p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), results p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** The goals of our experiments are: (a) Evaluate the localization accuracy of our trained detectors in the real world, including in the presence of distractor objects and partial occlusions (b) ... (p. 4, IV. EXPERIMENTS).
- **Metric evidence:** The goals of our experiments are: (a) Evaluate the localization accuracy of our trained detectors in the real world, including in the presence of distractor objects and partial occlusions (b) ... (p. 4, IV. EXPERIMENTS).
- **Baseline/ablation evidence:** Randomizing the position of the camera also consistently provides a slight accuracy boost, but reasonably high accuracy is achievable without it. (p. 5, IV. EXPERIMENTS).
- **Failure/negative evidence:** Ablation study To evaluate the importance of different factors of our training methodology, we assessed the sensitivity of the algorithm to the following: • Number of training images • Number ... (p. 5, IV. EXPERIMENTS).
