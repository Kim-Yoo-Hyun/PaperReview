# Evaluation - Sensor-Invariant Tactile Representation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=RnJY9WcpA3; PDF retrieval source: https://arxiv.org/pdf/2502.19638. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 10 (Figure/Table caption), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 24 (Figure/Table caption)): Table 1: Results of object classification accuracy on 16 classes for model transfer and no-transfer performance. We report the mean and standard deviation of transfer accuracy percent among the sensor ...

## Evaluation Body Digest

- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** 5.3 OBJECT CLASSIFICATION We compare SITR with baselines using our real-world classification dataset from Section 4.2 and report top-1 accuracy.
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** 5, we reconstruct normal maps for objects in our real-world classification dataset and integrate them to generate their corresponding height maps.
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** 6 presents the t-SNE visualization of the SITR features for the contacts in our real-world classification dataset.
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** We attribute this to DIGIT's distinct optical design, which differs from the GelSight designs in our simulation dataset.
- **p. 24 / A.6.3 EFFECT OF SIMULATION DATASET SIZE - extractive PDF cue:** We evaluate how the size of the simulation dataset and the variety of sensor configurations impact classification transfer performance on inter-set classification.
- **p. 16 / A.2 SIMULATED DATASET - extractive PDF cue:** Light shape point area Light orientation sides corners Light angle 5◦ 30◦ Light color rand rand Gel stiffness low high Gel specularity low high Camera ...
- **p. 17 / A.2 SIMULATED DATASET - extractive PDF cue:** The samples can be retrieved from our dataset with the sensor IDs and contact IDs provided.
- **p. 17 / A.2 SIMULATED DATASET - extractive PDF cue:** Published as a conference paper at ICLR 2025 As discussed in Section 4.1, we construct a large-scale simulated dataset that includes a wide range of ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** contact-rich manipulation scene.
- **Input boundary:** tactile image/force, vision과 proprioceptive history.
- **Output/decision under evaluation:** grasp/contact action, force command 또는 object motion.
- **Primary target:** slip/contact success, force/pose error와 robustness.
- **Detected evaluation headings:** 5 EXPERIMENTS (p. 6); A.1 IMPLEMENTATION DETAILS (p. 14); A.2 SIMULATED DATASET (p. 16); A.3 CLASSIFICATION DATASET SAMPLES (p. 18); A.4 POSE ESTIMATION DATASET SAMPLES (p. 20); A.6.3 EFFECT OF SIMULATION DATASET SIZE (p. 24).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1: Results of object classification accuracy on 16 classes for model transfer and no-transfer performance. We report the mean and standard deviation of ... | p. 8 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 8: Ablation study examining the impact of SCL and varying contrastive temperature τ on SITR's performance. Subplots (i) and (ii) show classification accuracy ... | p. 10 (Figure/Table caption) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 1, SITR outperforms all baselines by a large margin regarding classification accuracy when transferred across sensors. | p. 7 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Published as a conference paper at ICLR 2025 Method Intra-sensor set ↑ Inter-sensor set ↑ Wedge-Mini ↑ No transfer ↑ ViT-Base Scratch 36.90 ± ... | p. 8 (5 EXPERIMENTS) |
| 5 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We also find that compared to ViT trained from scratch, the ViT pre-trained on ImageNet only marginally improves this task. | p. 9 (5 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** 5.3 OBJECT CLASSIFICATION We compare SITR with baselines using our real-world classification dataset from Section 4.2 and report top-1 accuracy.
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** 5, we reconstruct normal maps for objects in our real-world classification dataset and integrate them to generate their corresponding height maps.
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** 6 presents the t-SNE visualization of the SITR features for the contacts in our real-world classification dataset.
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** We attribute this to DIGIT's distinct optical design, which differs from the GelSight designs in our simulation dataset.
- **p. 24 / A.6.3 EFFECT OF SIMULATION DATASET SIZE - extractive PDF cue:** We evaluate how the size of the simulation dataset and the variety of sensor configurations impact classification transfer performance on inter-set classification.
- **p. 16 / A.2 SIMULATED DATASET - extractive PDF cue:** Light shape point area Light orientation sides corners Light angle 5◦ 30◦ Light color rand rand Gel stiffness low high Gel specularity low high Camera ...
- **p. 17 / A.2 SIMULATED DATASET - extractive PDF cue:** The samples can be retrieved from our dataset with the sensor IDs and contact IDs provided.
- **p. 17 / A.2 SIMULATED DATASET - extractive PDF cue:** Published as a conference paper at ICLR 2025 As discussed in Section 4.1, we construct a large-scale simulated dataset that includes a wide range of ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: Vision-based tactile sensors vary in both optical design and physical properties. Even with the same contact object, a screw, the tactile images produced ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2: Our sensor-invariant representation learning framework. Each tactile image x is paired with a set of calibration images c. We patchify and linearly project ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3: Calibration images used in SITR, obtained by pressing two objects-a 4mm ball and a cube corner-at nine different lo- cations each in a ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4: Demonstration of our physics-based rendering (PBR) model to simulate GelSight sen- sors. We parameterize the sensor's optical design in the environment. We use ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5: Reconstruction examples for various sensors. The top row shows input tactile images, the middle row presents 3D reconstructions, and the bottom row shows ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 1: Results of object classification accuracy on 16 classes for model transfer and no-transfer performance. We report the mean and standard deviation of transfer ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 6: t-SNE visualization of the feature space. We qualitatively show that our contrastive loss term helps cluster those similar contacts from different sensors together. ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 2: Results of pose estimation with 6 objects. We report the mean and standard deviation of transfer pose estimation root mean square error (RMSE) ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 5.3 OBJECT CLASSIFICATION We compare SITR with baselines using our real-world classification dataset from Section 4.2 and report top-1 accuracy. | embodiment, simulator version and control stack | p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Task/environment | 5, we reconstruct normal maps for objects in our real-world classification dataset and integrate them to generate their corresponding height maps. | reset, timeout, object/scene variation | p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Observation/sensor | tactile image/force, vision과 proprioceptive history | calibration, preprocessing, privileged input | p. 4 (1 INTRODUCTION), p. 4 (1 INTRODUCTION) |
| Output/decision | grasp/contact action, force command 또는 object motion | action frame, controller and termination | p. 14 (A.1.2 ARCHITECTURE), p. 14 (A.1.2 ARCHITECTURE) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Let Aij represent the performance (e.g., classification accuracy or pose estimation error) when trained on Si and evaluated on Sj. | definition/direction/unit from same section | p. 6 (5 EXPERIMENTS) |
| 6 ABLATIONS 6.1 NUMBER AND TYPE OF CALIBRATION IMAGES Figure 7: Ablation study on the number and type of calibration images used in SITR, ... | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| Table 1: Results of object classification accuracy on 16 classes for model transfer and no-transfer performance. We report the mean and standard deviation of ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| We separately feed 2 tactile images of the same object into the frozen SITR encoder, concatenate their features, and train a decoder to learn ... | definition/direction/unit from same section | p. 8 (5 EXPERIMENTS) |
| Figure 8: Ablation study examining the impact of SCL and varying contrastive temperature τ on SITR's performance. Subplots (i) and (ii) show classification accuracy ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |
| We report the mean and standard deviation of transfer pose estimation root mean square error (RMSE) in mm among the sensor sets specified. | definition/direction/unit from same section | p. 9 (5 EXPERIMENTS) |
| Published as a conference paper at ICLR 2025 We also compute the score when training and testing on the same sensor i = j ... | definition/direction/unit from same section | p. 7 (5 EXPERIMENTS) |
| Table 5: Ablation study showing the impact of different loss terms on classification accuracy trans- ferability. A.6.2 CHOICE OF SUPERVISION SIGNAL There are alternative ... | definition/direction/unit from same section | p. 24 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As shown in Table 1, SITR outperforms all baselines by a large margin regarding classification accuracy when transferred across sensors. | comparison identity and matched condition | p. 7 (5 EXPERIMENTS) |
| As shown in Table 2, SITR demonstrates strong performance on the pose estimation when tested on a different sensor, reducing the RMSE by about ... | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |
| Specifically, we compared models with and without the SCL term and tested 9 | comparison identity and matched condition | p. 9 (5 EXPERIMENTS) |
| 5.3 OBJECT CLASSIFICATION We compare SITR with baselines using our real-world classification dataset from Section 4.2 and report top-1 accuracy. | comparison identity and matched condition | p. 7 (5 EXPERIMENTS) |
| For baseline models, we use similar pipelines as detailed in Section A.1. | comparison identity and matched condition | p. 8 (5 EXPERIMENTS) |
| We also find that compared to ViT trained from scratch, the ViT pre-trained on ImageNet only marginally improves this task. | comparison identity and matched condition | p. 9 (5 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 6.2 CONTRASTIVE LOSS AND TEMPERATURE We conduct an ablation study to assess the effect of SCL and varying contrastive temperatures τ on SITR's performance. | component/input/data sensitivity | p. 9 (5 EXPERIMENTS) |
| 6 ABLATIONS 6.1 NUMBER AND TYPE OF CALIBRATION IMAGES Figure 7: Ablation study on the number and type of calibration images used in SITR, ... | component/input/data sensitivity | p. 9 (5 EXPERIMENTS) |
| Table 5: Ablation study showing the impact of different loss terms on classification accuracy trans- ferability. A.6.2 CHOICE OF SUPERVISION SIGNAL There are alternative ... | component/input/data sensitivity | p. 24 (Figure/Table caption) |
| Though, these reconstructions are naturally constrained by the resolution and sensitivity limitations of the sensors. | component/input/data sensitivity | p. 7 (5 EXPERIMENTS) |
| Baseline: We compare our SITR with ViTs that are either trained from scratch or fine-tuned from ImageNet weights to show the effectiveness of our ... | component/input/data sensitivity | p. 7 (5 EXPERIMENTS) |
| This indicates that SITR successfully aligns the tactile signals from different sensors, highlighting its capacity to eliminate sensor-variant features. | component/input/data sensitivity | p. 8 (5 EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this section, we introduce our framework for training Sensor-Invariant Tactile Representation (SITR). | Table 1: Results of object classification accuracy on 16 classes for model transfer and no-transfer performance. We report the mean and standard deviation of ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 10 (Figure/Table caption), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 24 (Figure/Table caption) |
| Primary metric/result | Figure 8: Ablation study examining the impact of SCL and varying contrastive temperature τ on SITR's performance. Subplots (i) and (ii) show classification accuracy ... | numeric claim only at cited anchor | p. 10 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** 5.3 OBJECT CLASSIFICATION We compare SITR with baselines using our real-world classification dataset from Section 4.2 and report top-1 accuracy.
- **p. 8 / 5 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2025 Method Intra-sensor set ↑ Inter-sensor set ↑ Wedge-Mini ↑ No transfer ↑ ViT-Base Scratch 36.90 ± 22.19 ...
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2025 Method Inter-sensor set ↓ Wedge-Mini ↓ No transfer ↓ ViT-Base Scratch 1.63 ± 0.20 1.69 ± 0.13 ...
- **p. 24 / A.6.3 EFFECT OF SIMULATION DATASET SIZE - extractive PDF cue:** Sensor Variations Samples per sensor 1K 5K 10K 10 45.82 ± 21.12 57.00 ± 21.55 61.44 ± 22.81 50 55.86 ± 25.04 68.55 ± 11.96 ...
- **p. 15 / A.1.2 ARCHITECTURE - extractive PDF cue:** Published as a conference paper at ICLR 2025 • ViT: For all ViT encoders, we linearly project the class token to an output of 16 ...
- **p. 24 / A.6.1 CONTRIBUTION OF LOSS TERMS - extractive PDF cue:** Method Classification (%) Normal loss only 84.21 ± 14.01 SCL loss only 78.86 ± 18.72 Normal + SCL losses 91.43 ± 9.88 Table 5: Ablation ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Despite these limitations, the preservation of dense surface features demonstrates the robustness of SITR in accurately modeling the contact geometry across varying sensor inputs. | p. 7 (5 EXPERIMENTS) |
| body limitation/failure cue | Another direction of future work is incorporating marker-based tactile information to SITR. | p. 10 (7 DISCUSSION) |
| body limitation/failure cue | Though, these reconstructions are naturally constrained by the resolution and sensitivity limitations of the sensors. | p. 7 (5 EXPERIMENTS) |
| body limitation/failure cue | Our experimental results demonstrate that SITR outperforms baseline models and other related tactile representations in different downstream tasks, showcasing robust transferability and effectiveness. | p. 10 (8 CONCLUSION) |
| body limitation/failure cue | We choose case (18*) for SITR since increasing the number of calibration images does not incur additional inference costs, as calibration tokens are computed ... | p. 9 (5 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| This section outlines the detailed implementation steps, including pre-processing, architecture, training settings, and decoder choices for all models. | p. 14 (A.1 IMPLEMENTATION DETAILS) |
| For each downstream task, we freeze the SITR encoder and only train the downstream task-specific decoder on a single sensor. | p. 6 (5 EXPERIMENTS) |
| The transfer performance across all sensors in the set is computed as Transfer Performance = 1 n(n -1) n X i=1 n X j=1 ... | p. 6 (5 EXPERIMENTS) |
| We describe model configurations and decoders for each task in Section A.1. | p. 7 (5 EXPERIMENTS) |
| We freeze our SITR encoder and train the downstream classifier using crossentropy loss. | p. 7 (5 EXPERIMENTS) |
| We separately feed 2 tactile images of the same object into the frozen SITR encoder, concatenate their features, and train a decoder to learn ... | p. 8 (5 EXPERIMENTS) |
| We choose case (18*) for SITR since increasing the number of calibration images does not incur additional inference costs, as calibration tokens are computed ... | p. 9 (5 EXPERIMENTS) |
| The SITR encoder is frozen during this process. | p. 14 (A.1.2 ARCHITECTURE) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** Despite these limitations, the preservation of dense surface features demonstrates the robustness of SITR in accurately modeling the contact geometry across varying sensor inputs.
- **p. 10 / 7 DISCUSSION - extractive PDF cue:** Another direction of future work is incorporating marker-based tactile information to SITR.
- **p. 7 / 5 EXPERIMENTS - extractive PDF cue:** Though, these reconstructions are naturally constrained by the resolution and sensitivity limitations of the sensors.
- **p. 10 / 8 CONCLUSION - extractive PDF cue:** Our experimental results demonstrate that SITR outperforms baseline models and other related tactile representations in different downstream tasks, showcasing robust transferability and effectiveness.
- **p. 9 / 5 EXPERIMENTS - extractive PDF cue:** We choose case (18*) for SITR since increasing the number of calibration images does not incur additional inference costs, as calibration tokens are computed only ...

- **PDF anchors reviewed:** datasets p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 24 (A.6.3 EFFECT OF SIMULATION DATASET SIZE), p. 16 (A.2 SIMULATED DATASET), metrics p. 6 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 8 (Figure/Table caption), p. 8 (5 EXPERIMENTS), p. 10 (Figure/Table caption), p. 9 (5 EXPERIMENTS), baselines p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), results p. 8 (Figure/Table caption), p. 10 (Figure/Table caption), p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS), p. 9 (5 EXPERIMENTS), p. 24 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
