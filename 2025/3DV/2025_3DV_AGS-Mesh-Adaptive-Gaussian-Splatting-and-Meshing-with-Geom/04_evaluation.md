# Evaluation - AGS-Mesh: Adaptive Gaussian Splatting and Meshing with Geometric Priors for Indoor Room Reconstruction Using Smartphones

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://api.crossref.org/works/10.1109/3dv66043.2025.00104; PDF retrieval source: https://openreview.net/attachment?id=fTJrKaBKZk&name=pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

장면의 스케일에 적응하는 옥트리 기반 표면 추출을 적용하고 실내 스캔에서 메시의 정확도와 완전성을 비교했다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125632#page=5) · [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125632#page=6) · [PDF 7쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=11125632#page=7)

## Evaluation Body Digest

- **p. 6 / 5. Experiments - extractive body cue:** We focus on real-world indoor scenes captured using a mobile device.
- **p. 6 / 5. Experiments - extractive body cue:** We select two datasets containing iPhone captures with depth data: a) MuSHRoom [37] dataset: a real-world indoor dataset with different trajectories for training and evaluation; ...
- **p. 7 / 5.2. Novel View Synthesis - extractive body cue:** We demonstrate our method with two Gaussian-based methods DN-Splatter [43] and 2DGS [19] with qualitative visuals of the reconstructed meshes for the "honka" (top) and ...
- **p. 7 / 5.2. Novel View Synthesis - extractive body cue:** The reported results are based on two distinct evaluation datasets: a test set obtained by uniformly sampling every 10 frames within the same training sequence, ...
- **p. 8 / 5.3. Ablation Studies - extractive body cue:** Results are averaged over three scenes.
- **p. 8 / 5.3. Ablation Studies - extractive body cue:** Novel view synthesis comparisons on the MuSHRoom dataset.
- **p. 6 / 5. Experiments - extractive body cue:** For mesh reconstruction evaluation, we follow the evaluation protocol from [37, 45] and report Accuracy (Acc.), Completion (Comp.), Chamfer-L1 distance (C-L1), Normal Consistency (NC), and ...
- **p. 7 / 5.3. Ablation Studies - extractive body cue:** Our more effective filtering strategy, using adaptive depth and normal supervision, further enhances meshing quality, resulting in a 2.12% increase in the F-score.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Detected evaluation headings:** 5. Experiments (p. 6); 5.1. 3D Reconstruction Evaluation (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.3. Ablation Studies | BENCHMARK / DATASET | We observe that utilizing noisy depths significantly improves the baseline. | p. 7 (5.3. Ablation Studies) |
| 5.1. 3D Reconstruction Evaluation | BENCHMARK / DATASET | Our results demonstrate that the novel adaptive depth and normal regularization terms we propose (also showcased in the ablation study Table 3) improve mesh ... | p. 6 (5.1. 3D Reconstruction Evaluation) |
| 5.1. 3D Reconstruction Evaluation | BENCHMARK / DATASET | We demonstrate that our method can outperform the traditional volumetric fusion. | p. 6 (5.1. 3D Reconstruction Evaluation) |
| Figure/Table caption | BENCHMARK / DATASET | Table 1. Mesh reconstruction evaluation on MuSHRoom. The mesh metrics are averaged over 6 scenes: "coffee room", "honka", "kokko", "sauna", "computer", and "vr room". ... | p. 7 (Figure/Table caption) |
| 5.3. Ablation Studies | BENCHMARK / DATASET | Ablation on supervision strategy and mesh performance (MuSHRoom). | p. 8 (5.3. Ablation Studies) |

## Dataset / Benchmark Role

- **p. 6 / 5. Experiments - extractive body cue:** We focus on real-world indoor scenes captured using a mobile device.
- **p. 6 / 5. Experiments - extractive body cue:** We select two datasets containing iPhone captures with depth data: a) MuSHRoom [37] dataset: a real-world indoor dataset with different trajectories for training and evaluation; ...
- **p. 7 / 5.2. Novel View Synthesis - extractive body cue:** We demonstrate our method with two Gaussian-based methods DN-Splatter [43] and 2DGS [19] with qualitative visuals of the reconstructed meshes for the "honka" (top) and ...
- **p. 7 / 5.2. Novel View Synthesis - extractive body cue:** The reported results are based on two distinct evaluation datasets: a test set obtained by uniformly sampling every 10 frames within the same training sequence, ...
- **p. 8 / 5.3. Ablation Studies - extractive body cue:** Results are averaged over three scenes.
- **p. 8 / 5.3. Ablation Studies - extractive body cue:** Novel view synthesis comparisons on the MuSHRoom dataset.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. We present AGS-Mesh, a method that adaptively integrates geometric priors into Gaussian Splatting for indoor room reconstruction using a mobile device. We enhance ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Demonstration of iPhone and Kinect sensor depths. The iPhone struggles to capture accurate depth values for (a) objects at a far distance, and ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Pipeline Overview. Our approach leverages geometric consistency between normals derived from raw sensor depths and those predicted by a pretrained model to filter ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Mesh reconstruction evaluation on MuSHRoom. The mesh metrics are averaged over 6 scenes: "coffee room", "honka", "kokko", "sauna", "computer", and "vr room". The ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Novel view synthesis evaluation on the MuSHRoom dataset. The reported results are based on two distinct evaluation datasets: a test set obtained by ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. We demonstrate our method with two Gaussian-based methods DN-Splatter [43] and 2DGS [19] with qualitative visuals of the reconstructed meshes for the "honka" ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 5. Novel view synthesis comparisons on the MuSHRoom dataset. From left to right: 2DGS [19] baseline, 2DGS with our proposed DNC and ANR optimization ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Ablation on supervision strategy and mesh perfor- mance (MuSHRoom). Results are averaged over three scenes. Input Acc. ↓ Comp. ↓ C-L1 ↓ NC ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We focus on real-world indoor scenes captured using a mobile device. | embodiment, simulator version and control stack | p. 6 (5. Experiments), p. 6 (5. Experiments) |
| Task/environment | We select two datasets containing iPhone captures with depth data: a) MuSHRoom [37] dataset: a real-world indoor dataset with different trajectories for training and ... | reset, timeout, object/scene variation | p. 6 (5. Experiments), p. 7 (5.2. Novel View Synthesis) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 6 (4.4. Mesh Extraction), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (4. Method), p. 4 (4. Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For mesh reconstruction evaluation, we follow the evaluation protocol from [37, 45] and report Accuracy (Acc.), Completion (Comp.), Chamfer-L1 distance (C-L1), Normal Consistency (NC), ... | definition/direction/unit from same section | p. 6 (5. Experiments) |
| Table 1. Mesh reconstruction evaluation on MuSHRoom. The mesh metrics are averaged over 6 scenes: "coffee room", "honka", "kokko", "sauna", "computer", and "vr room". ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Our more effective filtering strategy, using adaptive depth and normal supervision, further enhances meshing quality, resulting in a 2.12% increase in the F-score. | definition/direction/unit from same section | p. 7 (5.3. Ablation Studies) |
| From left to right: 2DGS [19] baseline, 2DGS with our proposed DNC and ANR optimization strategies, reference evaluation image, l2 error contributions, 2DGS + ... | definition/direction/unit from same section | p. 8 (5.3. Ablation Studies) |
| Figure 2. Demonstration of iPhone and Kinect sensor depths. The iPhone struggles to capture accurate depth values for (a) objects at a far distance, ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Ablation on supervision strategy and mesh performance (MuSHRoom). | definition/direction/unit from same section | p. 8 (5.3. Ablation Studies) |
| We evaluate mesh reconstruction performance and novel-view synthesis quality. | definition/direction/unit from same section | p. 6 (5. Experiments) |
| Figure 1. We present AGS-Mesh, a method that adaptively integrates geometric priors into Gaussian Splatting for indoor room reconstruction using a mobile device. We ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We compared our method to the following baselines: a) Traditional 3D reconstruction method Volumetric Fusion [9]. b) state-of-the-art NeRF-based method Nerfacto [41]; c) its ... | comparison identity and matched condition | p. 6 (5. Experiments) |
| Figure 6. Qualitative comparison with our optimization strat- egy. IsoOctree mesh extraction can efficiently generate a smoother surface compared to the TSDF [61] baseline. ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| For all TSDF based meshing baselines, we use the opensource implementation from Open3D [61] similar to prior work [19] with truncation distance of 0.03, ... | comparison identity and matched condition | p. 6 (5. Experiments) |
| We observe that utilizing noisy depths significantly improves the baseline. | comparison identity and matched condition | p. 7 (5.3. Ablation Studies) |
| We note that monocular depth supervision greatly under-performs compared to directly using noisy sensor depth readings for indoor room reconstruction. | comparison identity and matched condition | p. 8 (5.3. Ablation Studies) |
| Figure 9. Novel view synthesis comparisons on the MuSHRoom dataset. From left to right: 2DGS [19] baseline, 2DGS with our proposed DNC and ANR ... | comparison identity and matched condition | p. 17 (Figure/Table caption) |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Our results demonstrate that the novel adaptive depth and normal regularization terms we propose (also showcased in the ablation study Table 3) improve mesh ... | component/input/data sensitivity | p. 6 (5.1. 3D Reconstruction Evaluation) |
| Ablation on supervision strategy and mesh performance (MuSHRoom). | component/input/data sensitivity | p. 8 (5.3. Ablation Studies) |
| Ablation on monocular and sensor depth supervision on the "vr room" scene from MuSHRoom. | component/input/data sensitivity | p. 8 (5.3. Ablation Studies) |
| Figure 8. Qualitative visuals of our Depth Normal Consistency (DNR) and Adaptive Normal Regularization (ANR) terms. We visualize sensor depth and normals obtained from ... | component/input/data sensitivity | p. 16 (Figure/Table caption) |
| Figure 3. Pipeline Overview. Our approach leverages geometric consistency between normals derived from raw sensor depths and those predicted by a pretrained model to ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We summarize our contributions with the following statements: • We propose a novel regularization strategy for indoor room reconstruction that adaptively filters geometric priors ... | We observe that utilizing noisy depths significantly improves the baseline. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5.3. Ablation Studies), p. 6 (5.1. 3D Reconstruction Evaluation), p. 6 (5.1. 3D Reconstruction Evaluation), p. 7 (Figure/Table caption), p. 8 (5.3. Ablation Studies) |
| Primary metric/result | Our results demonstrate that the novel adaptive depth and normal regularization terms we propose (also showcased in the ablation study Table 3) improve mesh ... | numeric claim only at cited anchor | p. 6 (5.1. 3D Reconstruction Evaluation) |

- Numeric sentences retained from the body:
- **p. 7 / 5.2. Novel View Synthesis - extractive body cue:** The mesh metrics are averaged over 6 scenes: "coffee room", "honka", "kokko", "sauna", "computer", and "vr room".
- **p. 7 / 5.2. Novel View Synthesis - extractive body cue:** The reported results are based on two distinct evaluation datasets: a test set obtained by uniformly sampling every 10 frames within the same training sequence, ...
- **p. 7 / 5.2. Novel View Synthesis - extractive body cue:** Results are averaged over 6 scenes.
- **p. 6 / 4.4. Mesh Extraction - extractive body cue:** To achieve this, we employ a point cloud hint: we back-project our output depth maps from all training images into a point cloud and expand ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 2. Demonstration of iPhone and Kinect sensor depths. The iPhone struggles to capture accurate depth values for (a) objects at a far distance, ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | Lastly, the DNC and ANR terms help preserve details for objects and reduce overall noise. | p. 8 (5.3. Ablation Studies) |
| body limitation/failure cue | Figure 8. Qualitative visuals of our Depth Normal Consistency (DNR) and Adaptive Normal Regularization (ANR) terms. We visualize sensor depth and normals obtained from ... | p. 16 (Figure/Table caption) |

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| More settings and implementation details can be seen in the supplementary materials. | p. 6 (5. Experiments) |
| We implement our method using two recent open-source Gaussian splatting frameworks 2DGS [19] and Splatfacto [41] (a 3DGS re-implementation). | p. 6 (5. Experiments) |
| The mesh metrics are averaged over 6 scenes: "coffee room", "honka", "kokko", "sauna", "computer", and "vr room". | p. 7 (5.2. Novel View Synthesis) |

## Limitations and Verification Questions

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Demonstration of iPhone and Kinect sensor depths. The iPhone struggles to capture accurate depth values for (a) objects at a far distance, and ...
- **p. 8 / 5.3. Ablation Studies - extractive body cue:** Lastly, the DNC and ANR terms help preserve details for objects and reduce overall noise.
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 8. Qualitative visuals of our Depth Normal Consistency (DNR) and Adaptive Normal Regularization (ANR) terms. We visualize sensor depth and normals obtained from a ...

- **Evidence anchors reviewed:** datasets p. 6 (5. Experiments), p. 6 (5. Experiments), p. 7 (5.2. Novel View Synthesis), p. 7 (5.2. Novel View Synthesis), p. 8 (5.3. Ablation Studies), p. 8 (5.3. Ablation Studies), metrics p. 6 (5. Experiments), p. 7 (Figure/Table caption), p. 7 (5.3. Ablation Studies), p. 8 (5.3. Ablation Studies), p. 3 (Figure/Table caption), p. 8 (5.3. Ablation Studies), baselines p. 6 (5. Experiments), p. 8 (Figure/Table caption), p. 6 (5. Experiments), p. 7 (5.3. Ablation Studies), p. 8 (5.3. Ablation Studies), p. 17 (Figure/Table caption), results p. 7 (5.3. Ablation Studies), p. 6 (5.1. 3D Reconstruction Evaluation), p. 6 (5.1. 3D Reconstruction Evaluation), p. 7 (Figure/Table caption), p. 8 (5.3. Ablation Studies).

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)
