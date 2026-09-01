# Evaluation - AGS-Mesh: Adaptive Gaussian Splatting and Meshing with Geometric Priors for Indoor Room Reconstruction Using Smartphones

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=fTJrKaBKZk&name=pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5.3. Ablation Studies), p. 6 (5.1. 3D Reconstruction Evaluation), p. 6 (5.1. 3D Reconstruction Evaluation), p. 7 (Figure/Table caption), p. 8 (5.3. Ablation Studies)): We observe that utilizing noisy depths significantly improves the baseline.

## Evaluation Body Digest

- **p. 6 / 5. Experiments - extractive PDF cue:** We focus on real-world indoor scenes captured using a mobile device.
- **p. 6 / 5. Experiments - extractive PDF cue:** We select two datasets containing iPhone captures with depth data: a) MuSHRoom [37] dataset: a real-world indoor dataset with different trajectories for training and evaluation; ...
- **p. 7 / 5.2. Novel View Synthesis - extractive PDF cue:** We demonstrate our method with two Gaussian-based methods DN-Splatter [43] and 2DGS [19] with qualitative visuals of the reconstructed meshes for the "honka" (top) and ...
- **p. 7 / 5.2. Novel View Synthesis - extractive PDF cue:** The reported results are based on two distinct evaluation datasets: a test set obtained by uniformly sampling every 10 frames within the same training sequence, ...
- **p. 8 / 5.3. Ablation Studies - extractive PDF cue:** Results are averaged over three scenes.
- **p. 8 / 5.3. Ablation Studies - extractive PDF cue:** Novel view synthesis comparisons on the MuSHRoom dataset.
- **p. 6 / 5. Experiments - extractive PDF cue:** For mesh reconstruction evaluation, we follow the evaluation protocol from [37, 45] and report Accuracy (Acc.), Completion (Comp.), Chamfer-L1 distance (C-L1), Normal Consistency (NC), and ...
- **p. 7 / 5.3. Ablation Studies - extractive PDF cue:** Our more effective filtering strategy, using adaptive depth and normal supervision, further enhances meshing quality, resulting in a 2.12% increase in the F-score.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiments (p. 6); 5.1. 3D Reconstruction Evaluation (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.3. Ablation Studies | EMPIRICAL / REAL-ROBOT OR HARDWARE | We observe that utilizing noisy depths significantly improves the baseline. | p. 7 (5.3. Ablation Studies) |
| 5.1. 3D Reconstruction Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our results demonstrate that the novel adaptive depth and normal regularization terms we propose (also showcased in the ablation study Table 3) improve mesh ... | p. 6 (5.1. 3D Reconstruction Evaluation) |
| 5.1. 3D Reconstruction Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | We demonstrate that our method can outperform the traditional volumetric fusion. | p. 6 (5.1. 3D Reconstruction Evaluation) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1. Mesh reconstruction evaluation on MuSHRoom. The mesh metrics are averaged over 6 scenes: "coffee room", "honka", "kokko", "sauna", "computer", and "vr room". ... | p. 7 (Figure/Table caption) |
| 5.3. Ablation Studies | EMPIRICAL / REAL-ROBOT OR HARDWARE | Ablation on supervision strategy and mesh performance (MuSHRoom). | p. 8 (5.3. Ablation Studies) |

## Dataset / Benchmark Role

- **p. 6 / 5. Experiments - extractive PDF cue:** We focus on real-world indoor scenes captured using a mobile device.
- **p. 6 / 5. Experiments - extractive PDF cue:** We select two datasets containing iPhone captures with depth data: a) MuSHRoom [37] dataset: a real-world indoor dataset with different trajectories for training and evaluation; ...
- **p. 7 / 5.2. Novel View Synthesis - extractive PDF cue:** We demonstrate our method with two Gaussian-based methods DN-Splatter [43] and 2DGS [19] with qualitative visuals of the reconstructed meshes for the "honka" (top) and ...
- **p. 7 / 5.2. Novel View Synthesis - extractive PDF cue:** The reported results are based on two distinct evaluation datasets: a test set obtained by uniformly sampling every 10 frames within the same training sequence, ...
- **p. 8 / 5.3. Ablation Studies - extractive PDF cue:** Results are averaged over three scenes.
- **p. 8 / 5.3. Ablation Studies - extractive PDF cue:** Novel view synthesis comparisons on the MuSHRoom dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. We present AGS-Mesh, a method that adaptively integrates geometric priors into Gaussian Splatting for indoor room reconstruction using a mobile device. We enhance ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Demonstration of iPhone and Kinect sensor depths. The iPhone struggles to capture accurate depth values for (a) objects at a far distance, and ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Pipeline Overview. Our approach leverages geometric consistency between normals derived from raw sensor depths and those predicted by a pretrained model to filter ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Mesh reconstruction evaluation on MuSHRoom. The mesh metrics are averaged over 6 scenes: "coffee room", "honka", "kokko", "sauna", "computer", and "vr room". The ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2. Novel view synthesis evaluation on the MuSHRoom dataset. The reported results are based on two distinct evaluation datasets: a test set obtained by ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. We demonstrate our method with two Gaussian-based methods DN-Splatter [43] and 2DGS [19] with qualitative visuals of the reconstructed meshes for the "honka" ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5. Novel view synthesis comparisons on the MuSHRoom dataset. From left to right: 2DGS [19] baseline, 2DGS with our proposed DNC and ANR optimization ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3. Ablation on supervision strategy and mesh perfor- mance (MuSHRoom). Results are averaged over three scenes. Input Acc. ↓ Comp. ↓ C-L1 ↓ NC ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
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

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We compared our method to the following baselines: a) Traditional 3D reconstruction method Volumetric Fusion [9]. b) state-of-the-art NeRF-based method Nerfacto [41]; c) its ... | comparison identity and matched condition | p. 6 (5. Experiments) |
| Figure 6. Qualitative comparison with our optimization strat- egy. IsoOctree mesh extraction can efficiently generate a smoother surface compared to the TSDF [61] baseline. ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| For all TSDF based meshing baselines, we use the opensource implementation from Open3D [61] similar to prior work [19] with truncation distance of 0.03, ... | comparison identity and matched condition | p. 6 (5. Experiments) |
| We observe that utilizing noisy depths significantly improves the baseline. | comparison identity and matched condition | p. 7 (5.3. Ablation Studies) |
| We note that monocular depth supervision greatly under-performs compared to directly using noisy sensor depth readings for indoor room reconstruction. | comparison identity and matched condition | p. 8 (5.3. Ablation Studies) |
| Figure 9. Novel view synthesis comparisons on the MuSHRoom dataset. From left to right: 2DGS [19] baseline, 2DGS with our proposed DNC and ANR ... | comparison identity and matched condition | p. 17 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

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
- **p. 7 / 5.2. Novel View Synthesis - extractive PDF cue:** The mesh metrics are averaged over 6 scenes: "coffee room", "honka", "kokko", "sauna", "computer", and "vr room".
- **p. 7 / 5.2. Novel View Synthesis - extractive PDF cue:** The reported results are based on two distinct evaluation datasets: a test set obtained by uniformly sampling every 10 frames within the same training sequence, ...
- **p. 7 / 5.2. Novel View Synthesis - extractive PDF cue:** Results are averaged over 6 scenes.
- **p. 6 / 4.4. Mesh Extraction - extractive PDF cue:** To achieve this, we employ a point cloud hint: we back-project our output depth maps from all training images into a point cloud and expand ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 2. Demonstration of iPhone and Kinect sensor depths. The iPhone struggles to capture accurate depth values for (a) objects at a far distance, ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | Lastly, the DNC and ANR terms help preserve details for objects and reduce overall noise. | p. 8 (5.3. Ablation Studies) |
| body limitation/failure cue | Figure 8. Qualitative visuals of our Depth Normal Consistency (DNR) and Adaptive Normal Regularization (ANR) terms. We visualize sensor depth and normals obtained from ... | p. 16 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| More settings and implementation details can be seen in the supplementary materials. | p. 6 (5. Experiments) |
| We implement our method using two recent open-source Gaussian splatting frameworks 2DGS [19] and Splatfacto [41] (a 3DGS re-implementation). | p. 6 (5. Experiments) |
| The mesh metrics are averaged over 6 scenes: "coffee room", "honka", "kokko", "sauna", "computer", and "vr room". | p. 7 (5.2. Novel View Synthesis) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Demonstration of iPhone and Kinect sensor depths. The iPhone struggles to capture accurate depth values for (a) objects at a far distance, and ...
- **p. 8 / 5.3. Ablation Studies - extractive PDF cue:** Lastly, the DNC and ANR terms help preserve details for objects and reduce overall noise.
- **p. 16 / Figure/Table caption - extractive PDF cue:** Figure 8. Qualitative visuals of our Depth Normal Consistency (DNR) and Adaptive Normal Regularization (ANR) terms. We visualize sensor depth and normals obtained from a ...

- **PDF anchors reviewed:** datasets p. 6 (5. Experiments), p. 6 (5. Experiments), p. 7 (5.2. Novel View Synthesis), p. 7 (5.2. Novel View Synthesis), p. 8 (5.3. Ablation Studies), p. 8 (5.3. Ablation Studies), metrics p. 6 (5. Experiments), p. 7 (Figure/Table caption), p. 7 (5.3. Ablation Studies), p. 8 (5.3. Ablation Studies), p. 3 (Figure/Table caption), p. 8 (5.3. Ablation Studies), baselines p. 6 (5. Experiments), p. 8 (Figure/Table caption), p. 6 (5. Experiments), p. 7 (5.3. Ablation Studies), p. 8 (5.3. Ablation Studies), p. 17 (Figure/Table caption), results p. 7 (5.3. Ablation Studies), p. 6 (5.1. 3D Reconstruction Evaluation), p. 6 (5.1. 3D Reconstruction Evaluation), p. 7 (Figure/Table caption), p. 8 (5.3. Ablation Studies).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
