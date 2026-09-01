# Evaluation - Particle-Grid Neural Dynamics for Learning Deformable Object Models from RGB-D Videos

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (20 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p036.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p036.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (IV. EXPERIMENTS), p. 9 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 7 (A. Experiment Setup), p. 9 (Figure/Table caption), p. 6 (IV. EXPERIMENTS)): Our results demonstrate that it outperforms previous state-of-the-art approaches in dynamics prediction accuracy while remaining robust to incomplete camera views.

## Evaluation Body Digest

- **p. 6 / A. Experiment Setup - extractive body cue:** ‘€) Box: Two robot arms are used to open and close shipping boxes.
- **p. 6 / A. Experiment Setup - extractive body cue:** The robot performs various actions, cluding opening, closing, and rotating the bag.
- **p. 7 / A. Experiment Setup - extractive body cue:** With the robot end-effectors, and employs a Graph Neural Network (GNN) to predict particle motions.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** ‘+ Can we train a unified model for multiple instances within fan object category, and how well does it generalize to ‘unseen instances?
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** ‘+ How well does the particle-grid model leam the dynamics of various types of deformable objects?
- **p. 7 / A. Experiment Setup - extractive body cue:** Our method's prediction error is lower on both seen and unseen instances compared to the baseline.
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 8: Quantitative Comparisons on Planning. For four manipulation tasks-cloth lifting, box closing, rope manipulation, and plush toy relocating -we present the error curve and ...
- **p. 7 / A. Experiment Setup - extractive body cue:** We present the mean and standard deviation of ‘dynamics prediction error.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** uncertain robot state와 safe/unsafe operating region.
- **Input boundary:** observation, uncertainty/risk estimate와 task command.
- **Output/decision under evaluation:** shielded, recovery 또는 safe action.
- **Primary target:** task return과 violation/failure probability.
- **Detected evaluation headings:** IV. EXPERIMENTS (p. 5); A. Experiment Setup (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our results demonstrate that it outperforms previous state-of-the-art approaches in dynamics prediction accuracy while remaining robust to incomplete camera views. | p. 5 (IV. EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 8: Quantitative Comparisons on Planning. For four manipulation tasks-cloth lifting, box closing, rope manipulation, and plush toy relocating -we present the error curve ... | p. 9 (Figure/Table caption) |
| IV. EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | ‘+ Can the model improve the performance of 3D actionconditioned video prediction and model-based planning? | p. 5 (IV. EXPERIMENTS) |
| A. Experiment Setup | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our method consistently achieves lower error than the baseline, and its errr increase rate as the number of camera views decreases is also lower. | p. 7 (A. Experiment Setup) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 9: Qualitative Comparisons on Planning. For each of the four tasks, we visualize a representative planning sequence for both our method and the ... | p. 9 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / A. Experiment Setup - extractive body cue:** ‘€) Box: Two robot arms are used to open and close shipping boxes.
- **p. 6 / A. Experiment Setup - extractive body cue:** The robot performs various actions, cluding opening, closing, and rotating the bag.
- **p. 7 / A. Experiment Setup - extractive body cue:** With the robot end-effectors, and employs a Graph Neural Network (GNN) to predict particle motions.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** ‘+ Can we train a unified model for multiple instances within fan object category, and how well does it generalize to ‘unseen instances?
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** ‘+ How well does the particle-grid model leam the dynamics of various types of deformable objects?
- **p. 7 / A. Experiment Setup - extractive body cue:** Our method's prediction error is lower on both seen and unseen instances compared to the baseline.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Modeling deformable objects from RGB-D videos presents signi ‘Our Partice-Grid Neural Dynamics framework learns the behavior of deformable objects directly from real-world observations. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: Overview of proposed framework: Particle-Grid Neural Dynamics. (a) A diagram of our dynamics model. Given particle positions 7X, and velocities V_ fused from ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3: Qualitative Comparisons on Dynamics Prediction. Given inital states and actions, we show the prediction results of the GBND
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4: Quantitative Comparisons on Prediction under Partial Views. We compare our method with the GBND baseline in the cloth and paper bag categories while ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 8: Quantitative Comparisons on Planning. For four manipulation tasks-cloth lifting, box closing, rope manipulation, and plush toy relocating -we present the error curve and ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 9: Qualitative Comparisons on Planning. For each of the four tasks, we visualize a representative planning sequence for both our method and the GBND ...
- **p. 15 / Figure/Table caption - extractive body cue:** Fig. 10. Our experiments, including real-world data collection and manipulation tasks, are conducted in a workspace (Fig. 10a) equipped with four calibrated RealSense D455 cameras. ...
- **p. 18 / Figure/Table caption - extractive body cue:** Fig. 12: Additional Qualitative Comparisons on Generalization. In this experiment, we deploy the trained model on objects not seen during training, We visualize the video ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | ‘€) Box: Two robot arms are used to open and close shipping boxes. | embodiment, simulator version and control stack | p. 6 (A. Experiment Setup), p. 6 (A. Experiment Setup) |
| Task/environment | The robot performs various actions, cluding opening, closing, and rotating the bag. | reset, timeout, object/scene variation | p. 6 (A. Experiment Setup), p. 7 (A. Experiment Setup) |
| Observation/sensor | observation, uncertainty/risk estimate와 task command | calibration, preprocessing, privileged input | p. 2 (I. INTRODUCTION), p. 3 (B. Learning-Based Deformable Modeling) |
| Output/decision | shielded, recovery 또는 safe action | action frame, controller and termination | p. 2 (A. Physics-Based Deformable Modeling), p. 3 (B. Learning-Based Deformable Modeling) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 8: Quantitative Comparisons on Planning. For four manipulation tasks-cloth lifting, box closing, rope manipulation, and plush toy relocating -we present the error curve ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| We present the mean and standard deviation of ‘dynamics prediction error. | definition/direction/unit from same section | p. 7 (A. Experiment Setup) |
| and standard deviation of the prediction error over a 3-second horizon, The best results are highlighted | definition/direction/unit from same section | p. 7 (A. Experiment Setup) |
| Our results demonstrate that it outperforms previous state-of-the-art approaches in dynamics prediction accuracy while remaining robust to incomplete camera views. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| The red spheres indicate the position and orientation of robot ith ground truth final state images to highlight the prediction errors. | definition/direction/unit from same section | p. 6 (IV. EXPERIMENTS) |
| Fig. 9: Qualitative Comparisons on Planning. For each of the four tasks, we visualize a representative planning sequence for both our method and the ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| ‘+ Can the model improve the performance of 3D actionconditioned video prediction and model-based planning? | definition/direction/unit from same section | p. 5 (IV. EXPERIMENTS) |
| Fig. 2: Overview of proposed framework: Particle-Grid Neural Dynamics. (a) A diagram of our dynamics model. Given particle positions 7X, and velocities V_ fused ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our results demonstrate that it outperforms previous state-of-the-art approaches in dynamics prediction accuracy while remaining robust to incomplete camera views. | comparison identity and matched condition | p. 5 (IV. EXPERIMENTS) |
| baseline compared to our particle-grid neural dynamics model. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| Our model's predictions are more aligned with 1g higher-density particle predictions and fewer artifacts compared to the baseline. | comparison identity and matched condition | p. 6 (IV. EXPERIMENTS) |
| Our method's prediction error is lower on both seen and unseen instances compared to the baseline. | comparison identity and matched condition | p. 7 (A. Experiment Setup) |
| Fig. 8: Quantitative Comparisons on Planning. For four manipulation tasks-cloth lifting, box closing, rope manipulation, and plush toy relocating -we present the error curve ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| Fig, 5: Quantitative Comparisons on Generalization, Our method is compared with GBND on seen and unseen instances of the rope and cloth categories. | comparison identity and matched condition | p. 7 (A. Experiment Setup) |

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
| The model updates particle positions X,...+ with the predicted velocities Vs>.s¢ to perform iterative rollouts (b) Our framework enables 3D action-conditioned video prediction by ... | Our results demonstrate that it outperforms previous state-of-the-art approaches in dynamics prediction accuracy while remaining robust to incomplete camera views. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (IV. EXPERIMENTS), p. 9 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 7 (A. Experiment Setup), p. 9 (Figure/Table caption), p. 6 (IV. EXPERIMENTS) |
| Primary metric/result | Fig. 8: Quantitative Comparisons on Planning. For four manipulation tasks-cloth lifting, box closing, rope manipulation, and plush toy relocating -we present the error curve ... | numeric claim only at cited anchor | p. 9 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 7 / A. Experiment Setup - extractive body cue:** GBND [5S]. and particle-based baselines.
- **p. 3 / B. Learning-Based Deformable Modeling - extractive body cue:** Given particle positions 7X, and velocities V_ fused from multi-view depth images as input, our model predicts dense per-particle motion by first using. a point ...
- **p. 4 / B. Model Components - extractive body cue:** 4s inputs, then predict per-rid velocity vector vp. by
- **p. 5 / B. Model Components - extractive body cue:** Method Metric ‘Cloth Rope Phush Box Bag Bread MPM [121 O.176s0107 -0.13840072 -0.1630.148 022640020 0.0008 GBND ISS) / sey / OO7F0.033 0.0620, 0.078+0.028 0.03120.08 Panicle ...
- **p. 5 / B. Model Components - extractive body cue:** Neural Dynamics (GBND) [5S], and a particle-based dynat

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Our results demonstrate that it outperforms previous state-of-the-art approaches in dynamics prediction accuracy while remaining robust to incomplete camera views. | p. 5 (IV. EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For additional information on the experiment setups and baseline implementations, please refer to Appendix B. | p. 7 (A. Experiment Setup) |
| is grasped or nonprehensile interaction; the implementation details ofthese two types are given in Sec. | p. 3 (B. Learning-Based Deformable Modeling) |
| Given particle positions 7X, and velocities V_ fused from multi-view depth images as input, our model predicts dense per-particle motion by first using. a ... | p. 3 (B. Learning-Based Deformable Modeling) |
| (6) where f= is the neural network-based point encoder for extracting feature from the input particles (Sec. | p. 4 (B. Learning-Based Deformable Modeling) |
| We use PointNet [36] as the encoder for its efficiency and strong performance in extracting 3D point features. | p. 4 (B. Model Components) |
| Model training begins from a given point cloud at time t, followed by iterative dynamics model rollouts for K° steps. | p. 5 (B. Model Components) |
| With the collected tracking data, we define particle sets and their trajectories over a look-forward time window as Xenaueciae © RP", alongside corresponding robot, ... | p. 5 (B. Model Components) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Our results demonstrate that it outperforms previous state-of-the-art approaches in dynamics prediction accuracy while remaining robust to incomplete camera views.

- **PDF anchors reviewed:** datasets p. 6 (A. Experiment Setup), p. 6 (A. Experiment Setup), p. 7 (A. Experiment Setup), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 7 (A. Experiment Setup), metrics p. 9 (Figure/Table caption), p. 7 (A. Experiment Setup), p. 7 (A. Experiment Setup), p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 9 (Figure/Table caption), baselines p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 7 (A. Experiment Setup), p. 9 (Figure/Table caption), p. 7 (A. Experiment Setup), results p. 5 (IV. EXPERIMENTS), p. 9 (Figure/Table caption), p. 5 (IV. EXPERIMENTS), p. 7 (A. Experiment Setup), p. 9 (Figure/Table caption), p. 6 (IV. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
