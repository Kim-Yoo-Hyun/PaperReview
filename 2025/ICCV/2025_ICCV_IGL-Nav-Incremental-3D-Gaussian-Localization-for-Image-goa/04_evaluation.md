# Evaluation - IGL-Nav: Incremental 3D Gaussian Localization for Image-goal Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Guo_IGL-Nav_Incremental_3D_Gaussian_Localization_for_Image-goal_Navigation_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Guo_IGL-Nav_Incremental_3D_Gaussian_Localization_for_Image-goal_Navigation_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.3. Analysis of IGL-Nav), p. 6 (4.2. Comparison with State-of-the-art), p. 7 (4.2. Comparison with State-of-the-art), p. 6 (4.1. Experimental Setup), p. 8 (4.3. Analysis of IGL-Nav), p. 8 (4.3. Analysis of IGL-Nav)): It is shown that using a 3-level subdivision achieves best performance, because a finer discretization will reduce quantization error and improve the accuracy of coarse localization.

## Evaluation Body Digest

- **p. 8 / 4.4. Real-world Deployment - extractive body cue:** We further deploy IGL-Nav on real-world robotic platform to test its generalization ability.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** The Gibson dataset includes 72 houses for training and 14 for validation.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** For image-goal navigation, we follow the public Gibson [31] image-goal navigation dataset within the Habitat simulator [25] introduced by NRNS [7].
- **p. 8 / 4.4. Real-world Deployment - extractive body cue:** The model is directly taken from the free-view image-goal setting (supervised) without any finetuning on real-world data.
- **p. 7 / 4.2. Comparison with State-of-the-art - extractive body cue:** The performance of IGL-Nav can be further boosted with training data on the free-view image-goal task.
- **p. 7 / 4.2. Comparison with State-of-the-art - extractive body cue:** SR: Success Rate, SPL: Success weighted by Path Length.
- **p. 7 / 4.3. Analysis of IGL-Nav - extractive body cue:** It is shown that using a 3-level subdivision achieves best performance, because a finer discretization will reduce quantization error and improve the accuracy of coarse ...
- **p. 6 / 4.2. Comparison with State-of-the-art - extractive body cue:** IGL-Nav establishes new state-of-the-art performance and outperforms previous methods by a large margin on all metrics, which validates the effectiveness of 3D gaussian representation and ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4. Experiment (p. 6); 4.1. Experimental Setup (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Analysis of IGL-Nav | EMPIRICAL / REAL-ROBOT OR HARDWARE | It is shown that using a 3-level subdivision achieves best performance, because a finer discretization will reduce quantization error and improve the accuracy of ... | p. 7 (4.3. Analysis of IGL-Nav) |
| 4.2. Comparison with State-of-the-art | EMPIRICAL / REAL-ROBOT OR HARDWARE | IGL-Nav establishes new state-of-the-art performance and outperforms previous methods by a large margin on all metrics, which validates the effectiveness of 3D gaussian representation ... | p. 6 (4.2. Comparison with State-of-the-art) |
| 4.2. Comparison with State-of-the-art | EMPIRICAL / REAL-ROBOT OR HARDWARE | SR: Success Rate, SPL: Success weighted by Path Length. | p. 7 (4.2. Comparison with State-of-the-art) |
| 4.1. Experimental Setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | For image-goal setting, we report results from the respective papers. | p. 6 (4.1. Experimental Setup) |
| 4.3. Analysis of IGL-Nav | EMPIRICAL / REAL-ROBOT OR HARDWARE | The agent is successfully guided to a free-view goal image captured by a cellphone in complex indoor environments. | p. 8 (4.3. Analysis of IGL-Nav) |

## Dataset / Benchmark Role

- **p. 8 / 4.4. Real-world Deployment - extractive body cue:** We further deploy IGL-Nav on real-world robotic platform to test its generalization ability.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** The Gibson dataset includes 72 houses for training and 14 for validation.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** For image-goal navigation, we follow the public Gibson [31] image-goal navigation dataset within the Habitat simulator [25] introduced by NRNS [7].
- **p. 8 / 4.4. Real-world Deployment - extractive body cue:** The model is directly taken from the free-view image-goal setting (supervised) without any finetuning on real-world data.
- **p. 7 / 4.2. Comparison with State-of-the-art - extractive body cue:** The performance of IGL-Nav can be further boosted with training data on the free-view image-goal task.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. IGL-Nav effectively guides the agent to reach free-view image goal via incremental 3D gaussian localization. agent to precisely understand spatial information, as well ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Illustration of IGL-Nav. (a) We maintain an incremental 3DGS scene representation with feed-forward prediction. (b) The coarse target localization is modeled as a ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Modeling of the camera pose space. (a) Line LR is almost always parallel to the ground. (b) Line AO′ is parallel to Plane ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Navigation pipeline of IGL-Nav. same shape after voxelization, which forms a 3D convolu- tional kernel K ∈RL×L×L×Cin×Cout. Here Cin refers to the output ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Image-goal Navigation Results. SR: Success Rate, SPL: Success weighted by Path Length. The best result in each column is bold, and the second ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Free-view Image-goal Navigation Results. SR: Success Rate, SPL: Success weighted by Path Length. Narrow FOV (50◦∼75◦) Wide FOV (75◦∼100◦)
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Performance of IGL-Nav when depth and camera intrin- sics are unavailable.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Rendering results of our incremental 3DGS. transferred from image-goal to free-view image-goal set- ting, IGL-Nav still maintains a huge performance lead com- pared ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We further deploy IGL-Nav on real-world robotic platform to test its generalization ability. | embodiment, simulator version and control stack | p. 8 (4.4. Real-world Deployment), p. 6 (4.1. Experimental Setup) |
| Task/environment | The Gibson dataset includes 72 houses for training and 14 for validation. | reset, timeout, object/scene variation | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 5 (3.3.1. Coarse Target Localization), p. 3 (3.2. Incremental Scene Representation) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 3 (3.1. Problem Statement), p. 5 (3.3.1. Coarse Target Localization) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| SR: Success Rate, SPL: Success weighted by Path Length. | definition/direction/unit from same section | p. 7 (4.2. Comparison with State-of-the-art) |
| It is shown that using a 3-level subdivision achieves best performance, because a finer discretization will reduce quantization error and improve the accuracy of ... | definition/direction/unit from same section | p. 7 (4.3. Analysis of IGL-Nav) |
| IGL-Nav establishes new state-of-the-art performance and outperforms previous methods by a large margin on all metrics, which validates the effectiveness of 3D gaussian representation ... | definition/direction/unit from same section | p. 6 (4.2. Comparison with State-of-the-art) |
| We also report the zero-shot performance of IGLNav for fair comparison. | definition/direction/unit from same section | p. 6 (4.1. Experimental Setup) |
| The agent is successfully guided to a free-view goal image captured by a cellphone in complex indoor environments. | definition/direction/unit from same section | p. 8 (4.3. Analysis of IGL-Nav) |
| The agent is guided with frontier location, activation map obtained with 3D convolution and iterative pose optimization during the exploration. | definition/direction/unit from same section | p. 8 (4.3. Analysis of IGL-Nav) |
| Figure 4. Navigation pipeline of IGL-Nav. same shape after voxelization, which forms a 3D convolu- tional kernel K ∈RL×L×L×Cin×Cout. Here Cin refers to the ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| IGL-Nav establishes new state-of-the-art performance and outperforms previous methods by a large margin on all metrics, which validates the effectiveness of 3D gaussian representation ... | comparison identity and matched condition | p. 6 (4.2. Comparison with State-of-the-art) |
| Rendering results of our incremental 3DGS. transferred from image-goal to free-view image-goal setting, IGL-Nav still maintains a huge performance lead compared with other state-of-the-art ... | comparison identity and matched condition | p. 7 (4.2. Comparison with State-of-the-art) |
| Then we compare IGL-Nav with state-of-the-art image-goal navigation methods. | comparison identity and matched condition | p. 6 (4. Experiment) |
| All ablation studies are conducted on the free-view image-goal setting. | comparison identity and matched condition | p. 7 (4.3. Analysis of IGL-Nav) |
| The model is directly taken from the free-view image-goal setting (supervised) without any finetuning on real-world data. | comparison identity and matched condition | p. 8 (4.4. Real-world Deployment) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Since some methods [7, 29, 30, 33] only release test code, we perform zeroshot transfer to apply them to the new setting without retraining. | component/input/data sensitivity | p. 6 (4.1. Experimental Setup) |
| All ablation studies are conducted on the free-view image-goal setting. | component/input/data sensitivity | p. 7 (4.3. Analysis of IGL-Nav) |
| We further conduct in-depth module-by-module analysis on our IGL-Nav framework with sufficient visualization results and ablation studies, which is divided into three parts according ... | component/input/data sensitivity | p. 7 (4.3. Analysis of IGL-Nav) |
| The model is directly taken from the free-view image-goal setting (supervised) without any finetuning on real-world data. | component/input/data sensitivity | p. 8 (4.4. Real-world Deployment) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To this end, we propose IGL-Nav, an Incremental 3D Gaussian Localization framework that (1) progressively constructs 3DGS through feed-forward prediction, eliminating offline optimization; and ... | It is shown that using a 3-level subdivision achieves best performance, because a finer discretization will reduce quantization error and improve the accuracy of ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.3. Analysis of IGL-Nav), p. 6 (4.2. Comparison with State-of-the-art), p. 7 (4.2. Comparison with State-of-the-art), p. 6 (4.1. Experimental Setup), p. 8 (4.3. Analysis of IGL-Nav), p. 8 (4.3. Analysis of IGL-Nav) |
| Primary metric/result | IGL-Nav establishes new state-of-the-art performance and outperforms previous methods by a large margin on all metrics, which validates the effectiveness of 3D gaussian representation ... | numeric claim only at cited anchor | p. 6 (4.2. Comparison with State-of-the-art) |

- Numeric sentences retained from the body:
- **p. 5 / 3.3.2. Fine Target Localization - extractive body cue:** Then we formulate the optimization loss as: L = 1 Q Q-1 X i=0 (/Xi g -Xi/2) (9) where Q is the number of matching ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | A limitation of IGL-Nav is that it requires depth and camera intrinsics of goal image. | p. 8 (5. Conclusion) |
| body limitation/failure cue | As shown in Table 3, with predicted depth and camera intrinsics, the performance of IGLNav is still robust. | p. 7 (4.3. Analysis of IGL-Nav) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Since some methods [7, 29, 30, 33] only release test code, we perform zeroshot transfer to apply them to the new setting without retraining. | p. 6 (4.1. Experimental Setup) |
| We first concatenate the normalized RGB and depth images, and then extract dense monocular scene embedding E′ t with a UNet-based encoder E. | p. 3 (3.2. Incremental Scene Representation) |
| The task is considered successfully completed if the agent terminates within a horizontal neighborhood of the target pose, satisfying //P(Tfinal) -P(Tg)//2 < ϵ within ... | p. 3 (3.1. Problem Statement) |
| Moreover, during each comparison, we should compute the geometric similarity between two 3D pointclouds as well as their feature similarity, which is especially time-consuming ... | p. 4 (3.3.1. Coarse Target Localization) |
| By translating these embeddings to the discretized voxel grids and computing the extent of alignment between the translated embedding and Et, the coarse target ... | p. 4 (3.3.1. Coarse Target Localization) |
| Once the target is detected, we switch to fine localization to compute the precise target pose. | p. 6 (3.4. Navigation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive body cue:** A limitation of IGL-Nav is that it requires depth and camera intrinsics of goal image.
- **p. 7 / 4.3. Analysis of IGL-Nav - extractive body cue:** As shown in Table 3, with predicted depth and camera intrinsics, the performance of IGLNav is still robust.

- **PDF anchors reviewed:** datasets p. 8 (4.4. Real-world Deployment), p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 8 (4.4. Real-world Deployment), p. 7 (4.2. Comparison with State-of-the-art), metrics p. 7 (4.2. Comparison with State-of-the-art), p. 7 (4.3. Analysis of IGL-Nav), p. 6 (4.2. Comparison with State-of-the-art), p. 6 (4.1. Experimental Setup), p. 8 (4.3. Analysis of IGL-Nav), p. 8 (4.3. Analysis of IGL-Nav), baselines p. 6 (4.2. Comparison with State-of-the-art), p. 7 (4.2. Comparison with State-of-the-art), p. 6 (4. Experiment), p. 7 (4.3. Analysis of IGL-Nav), p. 8 (4.4. Real-world Deployment), results p. 7 (4.3. Analysis of IGL-Nav), p. 6 (4.2. Comparison with State-of-the-art), p. 7 (4.2. Comparison with State-of-the-art), p. 6 (4.1. Experimental Setup), p. 8 (4.3. Analysis of IGL-Nav), p. 8 (4.3. Analysis of IGL-Nav).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
