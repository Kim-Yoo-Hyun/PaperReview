# Evaluation - OpenIns3D: Snap and Lookup for 3D Open-vocabulary Instance Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/7914_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/07914.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 11 (4 Experiments), p. 12 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), p. 13 (4 Experiments)): Significant improvements are achieved on the S3DIS dataset, and competitive results are observed on ScanNetv2 (B/N: Base/Novel).

## Evaluation Body Digest

- **p. 12 / 4 Experiments - extractive body cue:** Model 2D AP AP50 AP25 OpenScene [23] (2D Fusion) ✓ 10.9 15.6 17.3 OpenScene [23] (2D/3D Ens.) ✓ 8.2 10.4 13.3 OpenMask3D [30] ✓ 13.1 ...
- **p. 11 / 4 Experiments - extractive body cue:** For 3D instance segmentation, compared to works in the PLA family [9,10,34] and the latest work Open3DIS [22], OpenIns3D does not require aligned images as ...
- **p. 9 / 4 Experiments - extractive body cue:** Among them, S3DIS, ScanNetv2, and ScanNet200 are indoor point cloud datasets generated from RGBD images, Replica is a photo-realistic 3D indoor scene reconstruction, while STPLS3D ...
- **p. 11 / 4 Experiments - extractive body cue:** With the enhanced recognition capability, the performance of 3D open-vocabulary Object Detection among the ScanNet dataset has also achieved state-of-the-art results by a large margin.
- **p. 12 / 4 Experiments - extractive body cue:** It also shows certain limitations on small objects that are not well-reconstructed in 3D scenes.
- **p. 9 / 4 Experiments - extractive body cue:** We exclusively used the 3D data with colour from these datasets and did not employ any 2D images, poses, or depth maps.
- **p. 10 / 4 Experiments - extractive body cue:** We also explored the performance of OpenIns3D on a more challenging dataset with more class categories.
- **p. 10 / 4 Experiments - extractive body cue:** For STPLIS3D, we followed Mask3D to split the large outdoor scene into patches of 50m \times 50 m and lifted the camera up to 10m.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 9).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Significant improvements are achieved on the S3DIS dataset, and competitive results are observed on ScanNetv2 (B/N: Base/Novel). | p. 11 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Model use 2D APhead APcommon APtail AP AP50 AP25 OpenScene (2D Fusion) [23] ✓ 13.4 11.6 9.9 11.7 15.2 17.8 OpenScene (2D/3D Ens.) [23] ... | p. 12 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | With the enhanced recognition capability, the performance of 3D open-vocabulary Object Detection among the ScanNet dataset has also achieved state-of-the-art results by a large ... | p. 11 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | In summary, OpenIns3D demonstrates the best performance among all existing methods if only 3D data is used as input and outperforms many existing state-of-the-art ... | p. 12 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Additionally, Look Enforced Lookup provided a final improvement to the results. | p. 13 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 12 / 4 Experiments - extractive body cue:** Model 2D AP AP50 AP25 OpenScene [23] (2D Fusion) ✓ 10.9 15.6 17.3 OpenScene [23] (2D/3D Ens.) ✓ 8.2 10.4 13.3 OpenMask3D [30] ✓ 13.1 ...
- **p. 11 / 4 Experiments - extractive body cue:** For 3D instance segmentation, compared to works in the PLA family [9,10,34] and the latest work Open3DIS [22], OpenIns3D does not require aligned images as ...
- **p. 9 / 4 Experiments - extractive body cue:** Among them, S3DIS, ScanNetv2, and ScanNet200 are indoor point cloud datasets generated from RGBD images, Replica is a photo-realistic 3D indoor scene reconstruction, while STPLS3D ...
- **p. 11 / 4 Experiments - extractive body cue:** With the enhanced recognition capability, the performance of 3D open-vocabulary Object Detection among the ScanNet dataset has also achieved state-of-the-art results by a large margin.
- **p. 12 / 4 Experiments - extractive body cue:** It also shows certain limitations on small objects that are not well-reconstructed in 3D scenes.
- **p. 9 / 4 Experiments - extractive body cue:** We exclusively used the 3D data with colour from these datasets and did not employ any 2D images, poses, or depth maps.
- **p. 10 / 4 Experiments - extractive body cue:** We also explored the performance of OpenIns3D on a more challenging dataset with more class categories.
- **p. 10 / 4 Experiments - extractive body cue:** For STPLIS3D, we followed Mask3D to split the large outdoor scene into patches of 50m \times 50 m and lifted the camera up to 10m.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Complex Queries 3D Instance Segmentation with OpenIns3D. Abstract. In this work, we introduce OpenIns3D, a new 3D-input-only framework for 3D open-vocabulary scene understanding. ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: High-level Illustrations of OpenIns3D and Quantitative Results. (a) OpenIns3D follows the "Mask-Snap-Lookup" steps for open-vocabulary scene under- standing. (b) A list of SOTA ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Four Categories of Open-Vocabulary 3D Scene Understanding Mod- els. a) 3D feature distillation frameworks, where 2D images are used as a bridge to ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1. In summary, our contributions are: - OpenIns3D employs a distinct pipeline that operates without the need for well-aligned images. This approach achieves state-of-the-art ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: General Pipeline of OpenIns3D OpenIns3D first processes point clouds with MPM to generate 3D mask proposals and mask scores. The Snap module (detailed ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 5: Snap and Mask2Pixel Maps. Multiscale snaps are conducted to render images with different levels of detail for scene understanding, including wide-corner snaps, wide-angle ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 6: Mask2Pixel Guided Lookup Il- lustration. IoUs between the 2D detec- tion results and the projected masks are the guidance to assign class names ...
- **p. 10 / Figure/Table caption - extractive body cue:** Table 1: Zero-shot object classification on ScanNetv2. OpenIns3D's Snap and Lookup approach for mask classification, surpasses all previous methods, including the latest language-aligned large-scale 3D ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Model 2D AP AP50 AP25 OpenScene [23] (2D Fusion) ✓ 10.9 15.6 17.3 OpenScene [23] (2D/3D Ens.) ✓ 8.2 10.4 13.3 OpenMask3D [30] ✓ ... | embodiment, simulator version and control stack | p. 12 (4 Experiments), p. 11 (4 Experiments) |
| Task/environment | For 3D instance segmentation, compared to works in the PLA family [9,10,34] and the latest work Open3DIS [22], OpenIns3D does not require aligned images ... | reset, timeout, object/scene variation | p. 11 (4 Experiments), p. 9 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (1 Introduction), p. 2 (1 Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (Body text (section not recovered)), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Following the evaluation on ScanNetv2, we assessed the class-agnostic mask quality using the average precision (AP) score. | definition/direction/unit from same section | p. 12 (4 Experiments) |
| We followed their evaluation scheme and reported the Top-1 accuracy of instance classification on ScanNetv2. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| 35.2 11.8 3.0 45.1 27.6 10.5 61.5 2.6 71.9 0.3 33.6 29.9 4.7 11.5 72.2 92.4 86.1 34.0 CLIP2 [35] 38.5 32.6 67.2 69.3 ... | definition/direction/unit from same section | p. 10 (4 Experiments) |
| Fig. 4: General Pipeline of OpenIns3D OpenIns3D first processes point clouds with MPM to generate 3D mask proposals and mask scores. The Snap module ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| OpenIns3D demonstrates robust performance when compared to 2D-input-free models. | definition/direction/unit from same section | p. 12 (4 Experiments) |
| The cross-domain models also demonstrate impressive performance on both datasets when compared with the baseline. | definition/direction/unit from same section | p. 13 (4 Experiments) |
| Among them, S3DIS, ScanNetv2, and ScanNet200 are indoor point cloud datasets generated from RGBD images, Replica is a photo-realistic 3D indoor scene reconstruction, while ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| We compare our zero-shot performance on the novel categories defined in the PLA-family work. | definition/direction/unit from same section | p. 11 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| For STPLS3D, we compared OpenIns3D with baseline models whose classification module is PointCLIP and PointCLIPV2 [43] (Table 5). | comparison identity and matched condition | p. 10 (4 Experiments) |
| In SPTLS3D, OpenIns3D outperforms the baseline model PointCLIPV2 by 9.3 % in AP. | comparison identity and matched condition | p. 11 (4 Experiments) |
| In the case of ScanNet200, OpenIns3D attains the highest performance compared to all other 3D input baselines. | comparison identity and matched condition | p. 12 (4 Experiments) |
| In summary, OpenIns3D demonstrates the best performance among all existing methods if only 3D data is used as input and outperforms many existing state-of-the-art ... | comparison identity and matched condition | p. 12 (4 Experiments) |
| The cross-domain models also demonstrate impressive performance on both datasets when compared with the baseline. | comparison identity and matched condition | p. 13 (4 Experiments) |
| For a fair comparison, we followed their category splits and compared our results on novel classes, as demonstrated in Table 2. | comparison identity and matched condition | p. 10 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| For the S3DIS, ScanNetv2, Scannet200, and STPLS datasets, the MPM module is trained without utilizing any category labels, and | component/input/data sensitivity | p. 9 (4 Experiments) |
| The top 0.5 m of the scene is removed for S3DIS, as the rooms are enclosed. | component/input/data sensitivity | p. 10 (4 Experiments) |
| 5.2 Ablation study Mask quality ablation. | component/input/data sensitivity | p. 12 (4 Experiments) |
| Projection and 2D backbone ablation. | component/input/data sensitivity | p. 13 (4 Experiments) |
| OpenIns3D: 3D Open-vocabulary Instance Segmentation 13 Table 7: Rendering and Inference Time Ablations. | component/input/data sensitivity | p. 13 (4 Experiments) |
| Figure 1. In summary, our contributions are: - OpenIns3D employs a distinct pipeline that operates without the need for well-aligned images. This approach achieves ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To this end, we introduce OpenIns3D, a framework designed to effectively perform 3D open-vocabulary scene understanding tasks without relying on 2D aligned images. | Significant improvements are achieved on the S3DIS dataset, and competitive results are observed on ScanNetv2 (B/N: Base/Novel). | PDF body cue; verify exact table/figure and matched conditions | p. 11 (4 Experiments), p. 12 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), p. 13 (4 Experiments) |
| Primary metric/result | Model use 2D APhead APcommon APtail AP AP50 AP25 OpenScene (2D Fusion) [23] ✓ 13.4 11.6 9.9 11.7 15.2 17.8 OpenScene (2D/3D Ens.) [23] ... | numeric claim only at cited anchor | p. 12 (4 Experiments) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Table 6: 3D instance segmentation results on the ScanNet200 validation set. OpenIns3D demonstrates robust performance when compared to 2D-input-free models. However, notable limitations emerge ... | p. 12 (Figure/Table caption) |
| body limitation/failure cue | It also shows certain limitations on small objects that are not well-reconstructed in 3D scenes. | p. 12 (4 Experiments) |
| body limitation/failure cue | For 3D instance segmentation, compared to works in the PLA family [9,10,34] and the latest work Open3DIS [22], OpenIns3D does not require aligned images ... | p. 11 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| OpenIns3D requires less rendering and inference time. | p. 13 (4 Experiments) |
| OpenIns3D: 3D Open-vocabulary Instance Segmentation 13 Table 7: Rendering and Inference Time Ablations. | p. 13 (4 Experiments) |
| More implementation details are presented in the supplementary materials. | p. 10 (4 Experiments) |
| (a) OpenIns3D follows the "Mask-Snap-Lookup" steps for open-vocabulary scene understanding. | p. 2 (1 Introduction) |
| Overall, OpenIns3D comprises three core steps: Mask, Snap, and Lookup. | p. 3 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 12 / Figure/Table caption - extractive body cue:** Table 6: 3D instance segmentation results on the ScanNet200 validation set. OpenIns3D demonstrates robust performance when compared to 2D-input-free models. However, notable limitations emerge when ...
- **p. 12 / 4 Experiments - extractive body cue:** It also shows certain limitations on small objects that are not well-reconstructed in 3D scenes.
- **p. 11 / 4 Experiments - extractive body cue:** For 3D instance segmentation, compared to works in the PLA family [9,10,34] and the latest work Open3DIS [22], OpenIns3D does not require aligned images as ...

- **Evidence anchors reviewed:** datasets p. 12 (4 Experiments), p. 11 (4 Experiments), p. 9 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 9 (4 Experiments), metrics p. 12 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments), p. 6 (Figure/Table caption), p. 12 (4 Experiments), p. 13 (4 Experiments), baselines p. 10 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), p. 10 (4 Experiments), results p. 11 (4 Experiments), p. 12 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), p. 13 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
