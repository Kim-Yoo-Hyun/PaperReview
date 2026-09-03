# Evaluation - SEGS-SLAM: Structure-enhanced 3D Gaussian Splatting SLAM with Appearance Embedding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wen_SEGS-SLAM_Structure-enhanced_3D_Gaussian_Splatting_SLAM_with_Appearance_Embedding_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wen_SEGS-SLAM_Structure-enhanced_3D_Gaussian_Splatting_SLAM_with_Appearance_Embedding_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5.2. Results Analysis), p. 6 (5.2. Results Analysis), p. 7 (5.2. Results Analysis), p. 8 (5.3. Ablation Studies), p. 2 (3. Extensive evaluations on various public datasets demon), p. 8 (5.3. Ablation Studies)): The best results are marked as best score , second best score and third best score . '-' denotes that the system does not provide valid results. based on 3D-GS, ...

## Evaluation Body Digest

- **p. 6 / 5.1. Experiment Setup - extractive body cue:** The top scene is office2 from the Replica datasets, and the bottom is fr3/office from TUM RGB-D datasets.
- **p. 6 / 5.2. Results Analysis - extractive body cue:** The TUM RGB-D dataset presents a greater challenge compared with the Replica dataset, with highly cluttered scene structures and substantial lighting variations.
- **p. 7 / 5.2. Results Analysis - extractive body cue:** The top scene is room1 from the Replica dataset, and the bottom is V201 from the EuRoC MAV dataset.
- **p. 8 / 5.3. Ablation Studies - extractive body cue:** Replica is an easier dataset, in which PSNR already exceeds 37 without AfME, indicating that scene is well-reconstructed.
- **p. 5 / 5.1. Experiment Setup - extractive body cue:** We use the images and poses of keyframes as the training set, while the remaining images and poses serve as the test set.
- **p. 7 / 5.2. Results Analysis - extractive body cue:** Camera Type RGB-D Monocular Stereo Datasets Replica TUM R Avg.
- **p. 8 / 5.4. Limitations - extractive body cue:** Currently, AFME is only capable of handling static scenes.
- **p. 7 / 5.2. Results Analysis - extractive body cue:** The best results are marked as best score , second best score and third best score . '-' denotes that the system does not provide ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 3. Extensive evaluations on various public datasets demon (p. 2); 5. Experiment (p. 5); 5.1. Experiment Setup (p. 5); 5.2. Results Analysis (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.2. Results Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | The best results are marked as best score , second best score and third best score . '-' denotes that the system does not ... | p. 7 (5.2. Results Analysis) |
| 5.2. Results Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | 1, where SEGS-SLAM significantly outperforms comparison methods, achieving the highest average rendering quality on both TUM RGB-D and Replica datasets. | p. 6 (5.2. Results Analysis) |
| 5.2. Results Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | Notably, SEGS-SLAM continues to significantly outperform comparison methods on the TUM RGB-D dataset. | p. 7 (5.2. Results Analysis) |
| 5.3. Ablation Studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | 4, our full method (5) outperforms the model without AfME (4) in terms of PSNR scores. | p. 8 (5.3. Ablation Studies) |
| 3. Extensive evaluations on various public datasets demon | EMPIRICAL / SOURCE-REPORTED EVALUATION | strate that our method significantly surpasses state-ofthe-art (SOTA) methods in photorealistic mapping quality across monocular, stereo, and RGB-D cameras, while maintaining competitive tracking accuracy. | p. 2 (3. Extensive evaluations on various public datasets demon) |

## Dataset / Benchmark Role

- **p. 6 / 5.1. Experiment Setup - extractive body cue:** The top scene is office2 from the Replica datasets, and the bottom is fr3/office from TUM RGB-D datasets.
- **p. 6 / 5.2. Results Analysis - extractive body cue:** The TUM RGB-D dataset presents a greater challenge compared with the Replica dataset, with highly cluttered scene structures and substantial lighting variations.
- **p. 7 / 5.2. Results Analysis - extractive body cue:** The top scene is room1 from the Replica dataset, and the bottom is V201 from the EuRoC MAV dataset.
- **p. 8 / 5.3. Ablation Studies - extractive body cue:** Replica is an easier dataset, in which PSNR already exceeds 37 without AfME, indicating that scene is well-reconstructed.
- **p. 5 / 5.1. Experiment Setup - extractive body cue:** We use the images and poses of keyframes as the training set, while the remaining images and poses serve as the test set.
- **p. 7 / 5.2. Results Analysis - extractive body cue:** Camera Type RGB-D Monocular Stereo Datasets Replica TUM R Avg.
- **p. 8 / 5.4. Limitations - extractive body cue:** Currently, AFME is only capable of handling static scenes.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Our method SEGS-SLAM outperforms SOTA methods (GS-ICP SLAM [11], Photo-SLAM [14], SplaTAM [16], MonoGS [26]) in photorealistic mapping quality across monocular, stereo, and ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of our method. Our method supports monocular, stereo, and RGB-D cameras. The input image stream is processed by the localization and geometric ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Visualization of the Photo-SLAM's 3D Gaussians and of our method's anchor points using only SEPM after 30k iterations. SEPM enhances the underlying structure ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. AE [25] and the proposed AfME. The differences be- tween them are: (1) AE uses image indexes as input, whereas AfME leverages camera ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5. The visualization of AfME controlling appearance. The rendering viewpoints in the top three images above are same, and only the input to AfME ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative evaluation of our method compared to SOTA methods for RGB-D camera on Replica and TUM RGB-D datasets. Best results are marked as ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6. We show comparisons of ours to SOTA methods for RGB-D camera. The top scene is office2 from the Replica datasets, and the bottom ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Quantitative evaluation of our method compared to SOTA methods for Monocular (Mono) and Stereo cameras on Replica, TUM RGB-D, and EuRoC MAV datasets. ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The top scene is office2 from the Replica datasets, and the bottom is fr3/office from TUM RGB-D datasets. | embodiment, simulator version and control stack | p. 6 (5.1. Experiment Setup), p. 6 (5.2. Results Analysis) |
| Task/environment | The TUM RGB-D dataset presents a greater challenge compared with the Replica dataset, with highly cluttered scene structures and substantial lighting variations. | reset, timeout, object/scene variation | p. 6 (5.2. Results Analysis), p. 7 (5.2. Results Analysis) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 4 (4.1. Structure-Enhanced Photorealistic Mapping), p. 2 (1. Introduction) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 4 (2.1 Test on the right half of each), p. 5 (4.2. Appearance-from-Motion Embedding) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The best results are marked as best score , second best score and third best score . '-' denotes that the system does not ... | definition/direction/unit from same section | p. 7 (5.2. Results Analysis) |
| strate that our method significantly surpasses state-ofthe-art (SOTA) methods in photorealistic mapping quality across monocular, stereo, and RGB-D cameras, while maintaining competitive tracking accuracy. | definition/direction/unit from same section | p. 2 (3. Extensive evaluations on various public datasets demon) |
| 3, our method demonstrates competitive accuracy in tracking for monocular, stereo, and RGB-D cameras when compared with SOTA methods. | definition/direction/unit from same section | p. 6 (5.2. Results Analysis) |
| The best results are marked as best score . ders finer details in highly textured regions, as demonstrated by the curtain at the bottom ... | definition/direction/unit from same section | p. 8 (5.3. Ablation Studies) |
| This highlights the advantage of indirect visual SLAM in terms of localization accuracy. | definition/direction/unit from same section | p. 6 (5.2. Results Analysis) |
| 4, our full method (5) outperforms the model without AfME (4) in terms of PSNR scores. | definition/direction/unit from same section | p. 8 (5.3. Ablation Studies) |
| Table 2. Quantitative evaluation of our method compared to SOTA methods for Monocular (Mono) and Stereo cameras on Replica, TUM RGB-D, and EuRoC MAV ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Moreover, following FreGS [47], we activate FPR once the structure of anchor points stabilizes and terminate it based on the completion of anchor point ... | definition/direction/unit from same section | p. 5 (5.1. Experiment Setup) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Quantitative evaluation of our method compared to SOTA methods for RGB-D camera on Replica and TUM RGB-D datasets. | comparison identity and matched condition | p. 6 (5.1. Experiment Setup) |
| 3, our method demonstrates competitive accuracy in tracking for monocular, stereo, and RGB-D cameras when compared with SOTA methods. | comparison identity and matched condition | p. 6 (5.2. Results Analysis) |
| Notably, SEGS-SLAM continues to significantly outperform comparison methods on the TUM RGB-D dataset. | comparison identity and matched condition | p. 7 (5.2. Results Analysis) |
| 4, our full method (5) outperforms the model without AfME (4) in terms of PSNR scores. | comparison identity and matched condition | p. 8 (5.3. Ablation Studies) |
| Figure 1. Our method SEGS-SLAM outperforms SOTA methods (GS-ICP SLAM [11], Photo-SLAM [14], SplaTAM [16], MonoGS [26]) in photorealistic mapping quality across monocular, stereo, ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| We first list the baseline methods used to evaluate photorealistic mapping. | comparison identity and matched condition | p. 5 (5.1. Experiment Setup) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To evaluate the effect of the proposed FPR on photorealistic mapping metrics, we train an additional model for our method without FPR. | component/input/data sensitivity | p. 8 (5.3. Ablation Studies) |
| Figure 9. Ablation of AfME (Top) and FPR (Bottom). It is evident that with the introduction of AfME, the lighting conditions at novel views ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| The variant without SEPM, AfME, and FPR directly uses the original 3D-GS [17]. | component/input/data sensitivity | p. 7 (5.3. Ablation Studies) |
| To evaluate the impact of SEPM on photorealistic mapping metrics, we additionally train two variants of our method: one without SEPM, AfME, and FPR, ... | component/input/data sensitivity | p. 7 (5.3. Ablation Studies) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Second, we propose Appearancefrom-Motion embedding (AfME), which takes poses as input and eliminates the need for training on the left half of each ground-truth ... | The best results are marked as best score , second best score and third best score . '-' denotes that the system does not ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5.2. Results Analysis), p. 6 (5.2. Results Analysis), p. 7 (5.2. Results Analysis), p. 8 (5.3. Ablation Studies), p. 2 (3. Extensive evaluations on various public datasets demon), p. 8 (5.3. Ablation Studies) |
| Primary metric/result | 1, where SEGS-SLAM significantly outperforms comparison methods, achieving the highest average rendering quality on both TUM RGB-D and Replica datasets. | numeric claim only at cited anchor | p. 6 (5.2. Results Analysis) |

- Numeric sentences retained from the body:
- **p. 5 / 5.1. Experiment Setup - extractive body cue:** The machine is equipped with an NVIDIA RTX 4090 GPU and a Ryzen 5995WX CPU.
- **p. 8 / 5.4. Limitations - extractive body cue:** Additionally, while our method achieves real-time tracking and rendering at 17 and 400 FPS, respectively, it exhibits reduced rendering speed due to the increased number ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | One limitation of our method is that a poorly structured point cloud leads to a decline in photorealistic mapping quality. | p. 8 (5.4. Limitations) |
| body limitation/failure cue | GS-SLAM∗denotes the result of GS-SLAM is taken from [42], all others are obtained in our experiments. '-' denotes the system does not provide valid ... | p. 6 (5.1. Experiment Setup) |
| body limitation/failure cue | The best results are marked as best score , second best score and third best score . '-' denotes that the system does not ... | p. 7 (5.2. Results Analysis) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The machine is equipped with an NVIDIA RTX 4090 GPU and a Ryzen 5995WX CPU. | p. 5 (5.1. Experiment Setup) |
| Except for the non-open-source GS-SLAM [42], all methods compared in this paper are run on the same machine using their official code. | p. 5 (5.1. Experiment Setup) |
| While some methods [11, 13, 16, This ICCV paper is the Open Access version, provided by the Computer Vision Foundation. | p. 1 (1. Introduction) |
| Visual simultaneous localization and mapping (SLAM) is a fundamental problem in 3D computer vision, with wide applications in autonomous driving, robotics, virtual reality, and ... | p. 1 (1. Introduction) |
| (1) Other parameters of k 3D Gaussians are decoded using individual MLPs, denoted as Mα, Mc, Mq, and Ms, respectively. | p. 3 (3.1. Structured 3D Gaussian Splatting) |
| 4 (b), the input of the encoder Mθa is the the camera pose (R, t). | p. 4 (4.2. Appearance-from-Motion Embedding) |
| On the other hand, AfME encodes the camera poses to model appearance variations. | p. 4 (4. SEGS-SLAM) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5.4. Limitations - extractive body cue:** One limitation of our method is that a poorly structured point cloud leads to a decline in photorealistic mapping quality.
- **p. 6 / 5.1. Experiment Setup - extractive body cue:** GS-SLAM∗denotes the result of GS-SLAM is taken from [42], all others are obtained in our experiments. '-' denotes the system does not provide valid results.
- **p. 7 / 5.2. Results Analysis - extractive body cue:** The best results are marked as best score , second best score and third best score . '-' denotes that the system does not provide ...

- **Evidence anchors reviewed:** datasets p. 6 (5.1. Experiment Setup), p. 6 (5.2. Results Analysis), p. 7 (5.2. Results Analysis), p. 8 (5.3. Ablation Studies), p. 5 (5.1. Experiment Setup), p. 7 (5.2. Results Analysis), metrics p. 7 (5.2. Results Analysis), p. 2 (3. Extensive evaluations on various public datasets demon), p. 6 (5.2. Results Analysis), p. 8 (5.3. Ablation Studies), p. 6 (5.2. Results Analysis), p. 8 (5.3. Ablation Studies), baselines p. 6 (5.1. Experiment Setup), p. 6 (5.2. Results Analysis), p. 7 (5.2. Results Analysis), p. 8 (5.3. Ablation Studies), p. 1 (Figure/Table caption), p. 5 (5.1. Experiment Setup), results p. 7 (5.2. Results Analysis), p. 6 (5.2. Results Analysis), p. 7 (5.2. Results Analysis), p. 8 (5.3. Ablation Studies), p. 2 (3. Extensive evaluations on various public datasets demon), p. 8 (5.3. Ablation Studies).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
