# Evaluation - Ov3R: Open-Vocabulary Semantic 3D Reconstruction from RGB Videos

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Gong_Ov3R_Open-Vocabulary_Semantic_3D_Reconstruction_from_RGB_Videos_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Gong_Ov3R_Open-Vocabulary_Semantic_3D_Reconstruction_from_RGB_Videos_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (4. Experiments), p. 6 (4. Experiments), p. 7 (Figure/Table caption)): Table 4. Open-vocabulary 3D semantic segmentation results on ScanNetv2. On top: methods running on ground truth 3D re- constructions. At the bottom: methods running on CLIP3R recon- structions. Here, "Ov3R" ...

## Evaluation Body Digest

- **p. 6 / 4. Experiments - extractive body cue:** For the 3D reconstruction task, we follow [35] and train CLIP3R on ScanNet++ [58], Aria Synthetic Environments [2], and CO3D-v2 [44], which provide diverse scenarios ...
- **p. 6 / 4. Experiments - extractive body cue:** We evaluate 3D reconstruction performance on Replica [48] and 7Scenes [46].
- **p. 6 / 4. Experiments - extractive body cue:** We adopt standard metrics including Accuracy (cm), completion (cm) for 3D reconstruction, Absolute Trajectory Error (ATE RMSE) for tracking accuracy, and Frame Per Second (FPS) ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 7. Efficiency of each component in Ov3R. Measurements taken on a 2000-frame sequence. Total refers to the full framework running sequentially (SAM2 + CLIP3R ...
- **p. 6 / 4. Experiments - extractive body cue:** For open-vocabulary 3D segmentation, we follow OVO protocol [36] and use mean Intersection Over Union (mIoU) and mean Accuracy (mAcc) between the ground truth 3D ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. CLIP3R Overview. I2P integrates object-level CLIP features with visual embeddings to predict local pointmaps. L2W then aligns these local pointmaps to global scene ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Open-vocabulary 3D semantic segmentation results on ScanNetv2. On top: methods running on ground truth 3D re- constructions. At the bottom: methods running on ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 6. Ablation study of 2D-3D OV. We report the advance- ment brought by different fusion strategies. shown in Figure 6, Ov3R accurately identifies the ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 4. Open-vocabulary 3D semantic segmentation results on ScanNetv2. On top: methods running on ground truth 3D re- constructions. At the bottom: methods running ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 7. Efficiency of each component in Ov3R. Measurements taken on a 2000-frame sequence. Total refers to the full framework running sequentially (SAM2 + ... | p. 8 (Figure/Table caption) |
| 4. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | We evaluate 3D reconstruction performance on Replica [48] and 7Scenes [46]. | p. 6 (4. Experiments) |
| 4. Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Additionally, we report camera tracking results from CLIP3R on both Replica and 7Scenes. | p. 6 (4. Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 2. 3D reconstruction and tracking results on 7Scenes. The results are divided into two groups: 3R methods with low FPS, and real-time 3R ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 4. Experiments - extractive body cue:** For the 3D reconstruction task, we follow [35] and train CLIP3R on ScanNet++ [58], Aria Synthetic Environments [2], and CO3D-v2 [44], which provide diverse scenarios ...
- **p. 6 / 4. Experiments - extractive body cue:** We evaluate 3D reconstruction performance on Replica [48] and 7Scenes [46].

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Ov3R is an Open-Vocabulary Semantic 3D Reconstruction Framework. It consists of two novel feed-forward modules, CLIP3R and 2D-3D OVS, and excels in both ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of Ov3R. Given RGB-only videos, we first apply CLIP3R to produce scene points while SAM predicts 2D segments. Each 2D segment is ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. CLIP3R Overview. I2P integrates object-level CLIP features with visual embeddings to predict local pointmaps. L2W then aligns these local pointmaps to global scene ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. 2D-3D OVS Overview. After matching 2D and 3D segments across images and pointmaps, CLIP3R, DINO, and 3D-CLIP features are combined into a 2D-3D ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. 3D reconstruction and tracking results on Replica. Methods are grouped into: 3R methods with low FPS, SLAM approaches, and real-time 3R models. Here, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. Qualitative results - Dense Pointmaps on Replica. Compared to competing methods, Ov3R demonstrates superior complete- ness and geometric alignment, particularly visible in the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. 3D reconstruction and tracking results on 7Scenes. The results are divided into two groups: 3R methods with low FPS, and real-time 3R models. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 3. Open-vocabulary 3D semantic segmentation results on Replica dataset. On top: methods running on ground truth 3D reconstructions. At the bottom: methods running on ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For the 3D reconstruction task, we follow [35] and train CLIP3R on ScanNet++ [58], Aria Synthetic Environments [2], and CO3D-v2 [44], which provide diverse ... | embodiment, simulator version and control stack | p. 6 (4. Experiments), p. 6 (4. Experiments) |
| Task/environment | We evaluate 3D reconstruction performance on Replica [48] and 7Scenes [46]. | reset, timeout, object/scene variation | p. 6 (4. Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (3.2. 2D-3D OVS), p. 7 (Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We adopt standard metrics including Accuracy (cm), completion (cm) for 3D reconstruction, Absolute Trajectory Error (ATE RMSE) for tracking accuracy, and Frame Per Second ... | definition/direction/unit from same section | p. 6 (4. Experiments) |
| Table 7. Efficiency of each component in Ov3R. Measurements taken on a 2000-frame sequence. Total refers to the full framework running sequentially (SAM2 + ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| For open-vocabulary 3D segmentation, we follow OVO protocol [36] and use mean Intersection Over Union (mIoU) and mean Accuracy (mAcc) between the ground truth ... | definition/direction/unit from same section | p. 6 (4. Experiments) |
| Figure 3. CLIP3R Overview. I2P integrates object-level CLIP features with visual embeddings to predict local pointmaps. L2W then aligns these local pointmaps to global ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Table 4. Open-vocabulary 3D semantic segmentation results on ScanNetv2. On top: methods running on ground truth 3D re- constructions. At the bottom: methods running ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 6. Ablation study of 2D-3D OV. We report the advance- ment brought by different fusion strategies. shown in Figure 6, Ov3R accurately identifies ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 4. Open-vocabulary 3D semantic segmentation results on ScanNetv2. On top: methods running on ground truth 3D re- constructions. At the bottom: methods running ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| We start by assessing the quality of 3D reconstructions produced by Ov3R against state-of-the-art methods. | comparison identity and matched condition | p. 6 (4.1. 3D Reconstruction) |
| Figure 5. Qualitative results - Dense Pointmaps on Replica. Compared to competing methods, Ov3R demonstrates superior complete- ness and geometric alignment, particularly visible in ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Table 5. Ablation study of CLIP3R on Replica. We study the impact of CLIP-insertion in I2P (CLIP-insert) and the CLIP- semantic supervision in L2W ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 6. Ablation study of 2D-3D OV. We report the advance- ment brought by different fusion strategies. shown in Figure 6, Ov3R accurately identifies ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| However, we argue that replacing SAM2 with faster variants [62] would allow Ov3R to meet real-time constraints. | component/input/data sensitivity | p. 8 (4.5. Runtime Analysis) |
| Figure 4. 2D-3D OVS Overview. After matching 2D and 3D segments across images and pointmaps, CLIP3R, DINO, and 3D-CLIP features are combined into a ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |
| Table 5. Ablation study of CLIP3R on Replica. We study the impact of CLIP-insertion in I2P (CLIP-insert) and the CLIP- semantic supervision in L2W ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Table 6. Ablation study of 2D-3D OV. We report the advance- ment brought by different fusion strategies. shown in Figure 6, Ov3R accurately identifies ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions are as follows: • We present Ov3R, a novel framework that unifies 3R models and open-vocabulary 3D semantic segmentation. • We ... | Table 4. Open-vocabulary 3D semantic segmentation results on ScanNetv2. On top: methods running on ground truth 3D re- constructions. At the bottom: methods running ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (4. Experiments), p. 6 (4. Experiments), p. 7 (Figure/Table caption) |
| Primary metric/result | Table 7. Efficiency of each component in Ov3R. Measurements taken on a 2000-frame sequence. Total refers to the full framework running sequentially (SAM2 + ... | numeric claim only at cited anchor | p. 8 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 4. Experiments - extractive body cue:** We evaluate 3D reconstruction performance on Replica [48] and 7Scenes [46].
- **p. 6 / 4. Experiments - extractive body cue:** Additionally, we report camera tracking results from CLIP3R on both Replica and 7Scenes.
- **p. 6 / 4. Experiments - extractive body cue:** The 2D-3D OVS model is trained for 15 epochs, with batch size 512.
- **p. 8 / 4.5. Runtime Analysis - extractive body cue:** Both our modules, CLIP3R and 2D-3D OVS, run at about 15 FPS, with the segmentation model represents the main bottleneck.
- **p. 7 / Method - extractive body cue:** 3D reconstruction and tracking results on 7Scenes.
- **p. 7 / Method - extractive body cue:** Overall, Ov3R outperforms all state-of-the-art methods while maintaining up to 15 FPS processing speed.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Ov3R inherits one of the limitations of 3R models, i.e., the suboptimal accuracy of the retrieved camera poses. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Future research will aim to overcome this limitation by integrating techniques from the SLAM literature, such as global bundle adjustment. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Figure 4. 2D-3D OVS Overview. After matching 2D and 3D segments across images and pointmaps, CLIP3R, DINO, and 3D-CLIP features are combined into a ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | Table 4. Open-vocabulary 3D semantic segmentation results on ScanNetv2. On top: methods running on ground truth 3D re- constructions. At the bottom: methods running ... | p. 7 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The 2D-3D OVS model is trained for 15 epochs, with batch size 512. | p. 6 (4. Experiments) |
| At inference time, the similarity between fused descriptors and a set of text embeddings corresponding to semantic classes is computed to select the class ... | p. 6 (Method) |
| This is achieved by processing images with a shared encoder Eimg and two decoders Dkey and Dsup for the keyframe and remaining images, respectively. | p. 3 (3.1. CLIP3R) |
| It employs a pointmap encoder Epts, a registration decoder Dreg, and a scene decoder Dsce, sharing the same structure as the encoder and decoder ... | p. 3 (3.1. CLIP3R) |
| These features are then processed by the keyframe decoder Dkey and the supporting decoder Dsup from the original I2P. | p. 4 (3.1. CLIP3R) |
| The 3D features obtained by this distilled encoder naturally align with the CLIP latent space. | p. 5 (3.2. 2D-3D OVS) |
| This 3D encoder is pre-trained on triplets of point clouds, corresponding images, and text using natural language supervision. | p. 5 (3.2. 2D-3D OVS) |
| We run experiments on the 8 standard scenes of Replica, annotated with 51 different semantic classes, and evaluate the results directly in 3D space ... | p. 7 (4.3. Open-Vocabulary 3D Semantic Segmentation) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive body cue:** Ov3R inherits one of the limitations of 3R models, i.e., the suboptimal accuracy of the retrieved camera poses.
- **p. 8 / 5. Conclusion - extractive body cue:** Future research will aim to overcome this limitation by integrating techniques from the SLAM literature, such as global bundle adjustment.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. 2D-3D OVS Overview. After matching 2D and 3D segments across images and pointmaps, CLIP3R, DINO, and 3D-CLIP features are combined into a 2D-3D ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Open-vocabulary 3D semantic segmentation results on ScanNetv2. On top: methods running on ground truth 3D re- constructions. At the bottom: methods running on ...

- **Evidence anchors reviewed:** datasets p. 6 (4. Experiments), p. 6 (4. Experiments), metrics p. 6 (4. Experiments), p. 8 (Figure/Table caption), p. 6 (4. Experiments), p. 4 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), baselines p. 7 (Figure/Table caption), p. 6 (4.1. 3D Reconstruction), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), results p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (4. Experiments), p. 6 (4. Experiments), p. 7 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
