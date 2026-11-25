# Evaluation - QuadricFormer: Scene as Superquadrics for 3D Semantic Occupancy Prediction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://neurips.cc/virtual/2025/poster/116903; PDF retrieval source: https://arxiv.org/pdf/2506.10977. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA2 targeted source review: 2026-10-23; PDF pp. 4. 손상 구간·직접 연결된 표 분류만 원문 이미지와 대조했다. 전체 주장 정독·실험 검증·reading status 승격을 뜻하지 않는다. [URL·PDF hash·수정 기록](../../../work/sources/pdf_note_review_followup_2026-10-23.json).

> DOC-QA3 (2026-10-23): Eq. (4)의 z 지수는 공개 CUDA primitive와 다르다. [u/v 기호 대응·실제 호출 경로](./03_method.md)에 기록했다. 이는 representation 정의의 정적 대조이며 occupancy 성능·gradient 검증 결과가 아니다.


## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 7 (Figure/Table caption), p. 1 (Figure/Table caption)): The results demonstrate that increasing the crop & split number consistently improves performance.

## Evaluation Body Digest

- **p. 7 / 4 Experiments - extractive body cue:** The dataset is officially split into 700 sequences for training, 150 for validation, and 150 for testing.
- **p. 7 / 4 Experiments - extractive body cue:** 4.1 Datasets and Metrics NuScenes [3] comprises 1,000 urban driving sequences collected in Boston and Singapore.
- **p. 11 / B Additional Experiments - extractive body cue:** Such diversity enables superquadrics to flexibly model complex object geometries in 3D scenes. n oitate g e v e d a m n a m ...
- **p. 8 / 4 Experiments - extractive body cue:** We train our model for 20 epochs on nuScenes with a batch of 8.
- **p. 8 / 4 Experiments - extractive body cue:** This further highlights the superior efficiency of our approach for the complex structures in real-world applications.
- **p. 9 / 4 Experiments - extractive body cue:** This confirms that reallocating primitives from low to high occupancy regions effectively enhances the accuracy and efficiency of our 3D scene representation.
- **p. 10 / B Additional Experiments - extractive body cue:** We visualize the position distributions of scene primitives using 1600 superquadrics versus 6400 Gaussians in Figure 8.
- **p. 10 / B Additional Experiments - extractive body cue:** In contrast, our superquadric-based method learns well-structured spatial arrangements, enabling it to effectively model the scene structure with significantly fewer primitives.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 7); B Additional Experiments (p. 10).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results demonstrate that increasing the crop & split number consistently improves performance. | p. 9 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Compared to other methods, our approach achieves state-of-the-art performance. | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our model is able to predict high-fidelity shapes and achieves comprehensive occupancy results. numbers of Superquarics are set to 1600 in our main results ... | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Moreover, our method achieves high-quality performance using only 1600 superquadrics, compared to 6400 Gaussians. | p. 9 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1: 3D semantic occupancy prediction results on nuScenes. * means supervised by dense occupancy annotations as opposed to original LiDAR segmentation labels. Ch. ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 4 Experiments - extractive body cue:** The dataset is officially split into 700 sequences for training, 150 for validation, and 150 for testing.
- **p. 7 / 4 Experiments - extractive body cue:** 4.1 Datasets and Metrics NuScenes [3] comprises 1,000 urban driving sequences collected in Boston and Singapore.
- **p. 11 / B Additional Experiments - extractive body cue:** Such diversity enables superquadrics to flexibly model complex object geometries in 3D scenes. n oitate g e v e d a m n a m ...
- **p. 8 / 4 Experiments - extractive body cue:** We train our model for 20 epochs on nuScenes with a batch of 8.
- **p. 8 / 4 Experiments - extractive body cue:** This further highlights the superior efficiency of our approach for the complex structures in real-world applications.
- **p. 9 / 4 Experiments - extractive body cue:** This confirms that reallocating primitives from low to high occupancy regions effectively enhances the accuracy and efficiency of our 3D scene representation.
- **p. 10 / B Additional Experiments - extractive body cue:** We visualize the position distributions of scene primitives using 1600 superquadrics versus 6400 Gaussians in Figure 8.
- **p. 10 / B Additional Experiments - extractive body cue:** In contrast, our superquadric-based method learns well-structured spatial arrangements, enabling it to effectively model the scene structure with significantly fewer primitives.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Considering the ellipsoidal shape prior of Gaussians, we propose leveraging expressive superquadrics to build an efficient and powerful object-centric representation. Our QuadricFormer achieves ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Comparisons between different representations. (a) Quadric-based method represents the same object with a smaller number of primitives and greater shape expressiveness. (b) Quadric-based ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3: Overall Framework of QuadricFormer.We use several quadric-encoder blocks to update superquadrics, and employ a pruning-and-splitting module to further enhance modeling efficiency. superquadrics allow ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: 3D semantic occupancy prediction results on nuScenes. * means supervised by dense occupancy annotations as opposed to original LiDAR segmentation labels. Ch. denotes ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Performance and efficiency comparison with Gaussian-based methods. The latency and memory are tested on an NVIDIA 4090 GPU with batch size one during ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: 3D Superquadrics and occupancy visualizations on nuScenes. Our model is able to predict high-fidelity shapes and achieves comprehensive occupancy results. numbers of Superquarics ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Effect of the ϵ range. Range of ϵ mIoU IoU (0.01, 2) 20.39 31.13 (0.01, 5)
- **p. 9 / Figure/Table caption - extractive body cue:** Table 4: Effect of the pruning-splitting module. Crop & Split Number mIoU IoU 0 19.41 39.77 200

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The dataset is officially split into 700 sequences for training, 150 for validation, and 150 for testing. | embodiment, simulator version and control stack | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Task/environment | 4.1 Datasets and Metrics NuScenes [3] comprises 1,000 urban driving sequences collected in Boston and Singapore. | reset, timeout, object/scene variation | p. 7 (4 Experiments), p. 11 (B Additional Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (6 Superquadrics), p. 3 (6 Superquadrics) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (6 Superquadrics), p. 5 (6 Superquadrics) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 5: Qualitative comparisons. QuadricFormer predicts more flexible and adaptive shapes. Effect of the pruning-splitting module. We conduct ablation studies on the effect of ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| The evaluation metrics adhere to common practice, namely mean Intersection-over-Union (mIoU) and Intersection-over-Union (IoU): mIoU = 1 /C′/ X i∈C′ TPi TPi + FPi ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| We observe that setting the range of (0.1, 2) yields the best results, achieving the highest mIoU (20.51) and IoU (31.25). | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Specifically, our method achieves the highest mIoU (up to 21.11) and IoU (up to 32.13), surpassing all Gaussian-based approaches. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Range of ϵ mIoU IoU (0.01, 2) 20.39 31.13 (0.01, 5) 20.25 30.63 (0.1, 2) 20.51 31.25 (0.1, 5) 19.86 30.65 Table 4: Effect ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| Figure 2: Comparisons between different representations. (a) Quadric-based method represents the same object with a smaller number of primitives and greater shape expressiveness. (b) ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| The figure illustrates how varying ϵ1 and ϵ2 produces a wide range of shapes, from star-like and rounded shapes to square-like structures. | definition/direction/unit from same section | p. 11 (B Additional Experiments) |
| Figure 1: Considering the ellipsoidal shape prior of Gaussians, we propose leveraging expressive superquadrics to build an efficient and powerful object-centric representation. Our QuadricFormer ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to other methods, our approach achieves state-of-the-art performance. | comparison identity and matched condition | p. 8 (4 Experiments) |
| QuadricFormer consistently outperforms prior methods in both 3D semantic occupancy prediction and computational efficiency. | comparison identity and matched condition | p. 8 (4 Experiments) |
| Moreover, our method achieves high-quality performance using only 1600 superquadrics, compared to 6400 Gaussians. | comparison identity and matched condition | p. 9 (4 Experiments) |
| Figure 2: Comparisons between different representations. (a) Quadric-based method represents the same object with a smaller number of primitives and greater shape expressiveness. (b) ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |
| Figure 1: Considering the ellipsoidal shape prior of Gaussians, we propose leveraging expressive superquadrics to build an efficient and powerful object-centric representation. Our QuadricFormer ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Table 1: 3D semantic occupancy prediction results on nuScenes. * means supervised by dense occupancy annotations as opposed to original LiDAR segmentation labels. Ch. ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 4.4 Ablation Study Effect of the ϵ range. | component/input/data sensitivity | p. 8 (4 Experiments) |
| We conduct ablation studies on the effect of the pruningsplitting module, as shown in Table 4. | component/input/data sensitivity | p. 9 (4 Experiments) |
| The table explores the effect of different ϵ ranges on 3D semantic occupancy prediction performance. | component/input/data sensitivity | p. 8 (4 Experiments) |
| Effect of the pruning-splitting module. | component/input/data sensitivity | p. 9 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| 3 Proposed Approach In this section, we present our method based on the superquadric representation for efficient 3D semantic occupancy prediction. | The results demonstrate that increasing the crop & split number consistently improves performance. | PDF body cue; verify exact table/figure and matched conditions | p. 9 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 7 (Figure/Table caption), p. 1 (Figure/Table caption) |
| Primary metric/result | Compared to other methods, our approach achieves state-of-the-art performance. | numeric claim only at cited anchor | p. 8 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 4 Experiments - extractive body cue:** Each sequence spans a duration of 20 seconds with RGB images captured by 6 surrounding cameras, and the key frames are annotated at a 2 ...
- **p. 7 / 4 Experiments - extractive body cue:** 4.2 Implementation Details The input images are at resolutions of 900×1600 for nuScenes with random flipping and photometric distortion augmentations.
- **p. 8 / 4 Experiments - extractive body cue:** We train our model for 20 epochs on nuScenes with a batch of 8.
- **p. 8 / 4 Experiments - extractive body cue:** For similar or even fewer primitives (e.g., 1600 or 3200), our method achieves a latency as low as 162 ms and 2554 MB memory consumption, ...
- **p. 3 / 6 Superquadrics - extractive body cue:** 2.2 Object-centric scene representations Existing 3D scene representations primarily use voxel-based frameworks for fine-grained volumetric modeling [36, 19], excelling in semantic prediction tasks.
- **p. 3 / 6 Superquadrics - extractive body cue:** When combined with six pose parameters for translation and rotation, a superquadric can represent a complete 3D object using only 11 parameters.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | With random initialization, QuadricFormer cannot fully learn accurate superquadric positions, leaving some superquadrics in empty regions and reducing representation efficiency. | p. 9 (5 Conclusion) |

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| For optimization, we train our model using AdamW with weight decay of 0.01, and maximum learning rate of 4 × 10-4, which decays with ... | p. 8 (4 Experiments) |
| The latency and memory are tested on an NVIDIA 4090 GPU with batch size one during inference, in accordance with Gaussian-based methods [15, 12]. | p. 7 (6 Superquadrics) |
| We employ ResNet101-DCN with FCOS3D checkpoint for nuScenes. | p. 7 (4 Experiments) |
| We train our model for 20 epochs on nuScenes with a batch of 8. | p. 8 (4 Experiments) |
| §3.2 Eq. (4)는 두 shape exponent를 더한 superquadric implicit surface를 정의한다. x/y 항을 합한 뒤 ε₂/ε₁ 승을 취하며, 렌더링된 원문의 z 항 지수는 2/ε₂로 표기되어 있다. 관행적인 superquadric 식으로 임의 변경하지 않았다. | PDF p. 4 Eq. (4); representation 정의이며 evaluation metric이 아님 |
| 1, the occupancy probability distribution of the Gaussian G can be viewed as a set of iso-probability surfaces defined by: g(x) = -1 2 ... | p. 4 (6 Superquadrics) |
| Image Encoder Quadric Encoder Sparse Conv. | p. 5 (6 Superquadrics) |
| Voxelization Cross Attn FFN Quadric Decoder x B Blocks Pos. | p. 5 (6 Superquadrics) |

## Limitations and Verification Questions

- **p. 9 / 5 Conclusion - extractive body cue:** With random initialization, QuadricFormer cannot fully learn accurate superquadric positions, leaving some superquadrics in empty regions and reducing representation efficiency.

- **Evidence anchors reviewed:** datasets p. 7 (4 Experiments), p. 7 (4 Experiments), p. 11 (B Additional Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), metrics p. 9 (Figure/Table caption), p. 7 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 3 (Figure/Table caption), baselines p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 3 (Figure/Table caption), p. 1 (Figure/Table caption), p. 7 (Figure/Table caption), results p. 9 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 7 (Figure/Table caption), p. 1 (Figure/Table caption).

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)
