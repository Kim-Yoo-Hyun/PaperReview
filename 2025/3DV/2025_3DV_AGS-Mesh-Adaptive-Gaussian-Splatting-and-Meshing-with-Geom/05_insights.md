# Insights — AGS-Mesh: Adaptive Gaussian Splatting and Meshing with Geometric Priors for Indoor Room Reconstruction Using Smartphones

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://arxiv.org/pdf/2411.19271.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** We summarize our contributions with the following statements: • We propose a novel regularization strategy for indoor room reconstruction that adaptively filters geometric priors from ...
- **p. 4 / 4. Method - extractive body cue:** Our method consists of two adaptive supervision strategies for Gaussian Splatting-based methods that effectively combine supervision signals from geometric priors obtained from mobile devices and ...
- **p. 4 / 4. Method - extractive body cue:** Lastly, in Section 4.4, we propose a novel octree-based mesh extraction method that enhances surface quality and detail preservation compared to previous approaches.
- **p. 2 / 1. Introduction - extractive body cue:** Additionally, we propose an Adaptive Normal Regularization strategy (ANR) to refine normals by mitigating regularization in regions where monocular normal estimators struggle to provide accurate ...
- **p. 5 / 4.1. Regularization with Depth Normal Consistency - extractive body cue:** Furthermore, we propose an adaptive TSDF and octree-based Marching Cubes meshing strategy enabling the extraction of smoother and more geometrically detailed meshes.
- **p. 4 / 4.1. Regularization with Depth Normal Consistency - extractive body cue:** To filter inaccurate depth estimates, we check the orientation consistency between Nd and Np generated from pre-train model with an angle threshold τd for filtering: ...
- **p. 4 / 4.1. Regularization with Depth Normal Consistency - extractive body cue:** We propose an adaptive depth regularization method based on the consistency of normals derived from noisy depth images and those from pretrained networks.
- **Contribution anchor:** p. 2 (1. Introduction), p. 4 (4. Method), p. 4 (4. Method), p. 2 (1. Introduction), p. 5 (4.1. Regularization with Depth Normal Consistency), p. 4 (4.1. Regularization with Depth Normal Consistency)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** However, performance on room-scale reconstruction with data captured by a mobile device is still lacking.
- **p. 2 / 1. Introduction - extractive body cue:** Low-texture surfaces and sparse, outward-facing captures, common in indoor room datasets [37, 55], pose challenges and ambiguities for purely photometric-based reconstruction.
- **p. 4 / 3.2. Gaussian Splatting - extractive body cue:** However, as noted in prior research [35], this is just an approximation for perpixel depth estimates.
- **p. 1 / 1. Introduction - extractive body cue:** Traditional approaches have addressed the problem by creating textured meshes that can be rendered using conventional graphics pipelines.
- **p. 3 / 3.1. Geometric Priors from Handheld Devices - extractive body cue:** Depth and Normal Priors from Monocular Networks.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Demonstration of iPhone and Kinect sensor depths. The iPhone struggles to capture accurate depth values for (a) objects at a far distance, and ...
- **p. 8 / 5.3. Ablation Studies - extractive body cue:** Lastly, the DNC and ANR terms help preserve details for objects and reduce overall noise.
- **Boundary to test:** Figure 2. Demonstration of iPhone and Kinect sensor depths. The iPhone struggles to capture accurate depth values for (a) objects at a far distance, and (b) small objects, and edges. Instead, the ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We summarize our contributions with the following statements: • We propose a novel regularization strategy for indoor room reconstruction that adaptively filters geometric priors from mobile devices and off-the-shelf monocular estimator ... | p. 2 (1. Introduction), p. 4 (4. Method) |
| Reported outcome | We observe that utilizing noisy depths significantly improves the baseline. | p. 7 (5.3. Ablation Studies), p. 6 (5.1. 3D Reconstruction Evaluation) |
| Failure/limitation | Figure 2. Demonstration of iPhone and Kinect sensor depths. The iPhone struggles to capture accurate depth values for (a) objects at a far distance, and (b) small objects, and edges. Instead, the ... | p. 3 (Figure/Table caption), p. 8 (5.3. Ablation Studies) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 To achieve this, we employ a point cloud hint: we back-project our output depth maps from all training images into a point cloud and expand a voxel of width h if it ...를 We summarize our contributions with the following statements: • We propose a novel regularization strategy for indoor room reconstruction that adaptively filters geometric priors from mobile devices and off-the-shelf monocular estimator ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 2. Demonstration of iPhone and Kinect sensor depths. The iPhone struggles to capture accurate depth values for (a) objects at a far distance, and (b) small objects, and edges. Instead, the ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We summarize our contributions with the following statements: • We propose a novel regularization strategy for indoor room reconstruction that adaptively filters geometric priors from mobile devices and off-the-shelf monocular estimator ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `Gaussian Splatting, 3D reconstruction, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 2. Demonstration of iPhone and Kinect sensor depths. The iPhone struggles to capture accurate depth values for (a) objects at a far distance, and (b) small objects, and edges. Instead, the ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We focus on real-world indoor scenes captured using a mobile device..
3. Compare against the body-reported baseline or a matched simpler baseline: We compared our method to the following baselines: a) Traditional 3D reconstruction method Volumetric Fusion [9]. b) state-of-the-art NeRF-based method Nerfacto [41]; c) its depth regularized version Depth-Nerfacto with a depth supervis ....
4. Report the body metric and its denominator/aggregation: For mesh reconstruction evaluation, we follow the evaluation protocol from [37, 45] and report Accuracy (Acc.), Completion (Comp.), Chamfer-L1 distance (C-L1), Normal Consistency (NC), and F-scores (F1) with a threshold of 5cm..
5. Re-run the body-reported ablation/failure condition: Our results demonstrate that the novel adaptive depth and normal regularization terms we propose (also showcased in the ablation study Table 3) improve mesh quality by effectively filtering out uncertain priors..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (4.1. Regularization with Depth Normal Consistency), p. 4 (4.1. Regularization with Depth Normal Consistency), p. 5 (4.1. Regularization with Depth Normal Consistency); the primary result is directionally consistent at p. 7 (5.3. Ablation Studies), p. 6 (5.1. 3D Reconstruction Evaluation), p. 6 (5.1. 3D Reconstruction Evaluation); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summarize, contributions, following mechanism이 We compared our method to the following baselines: a) Traditional 3D reconstruction method Volumetric Fusion [9]. ... 대비 For mesh reconstruction evaluation, we follow the evaluation protocol from [37, 45] and report Accuracy (Acc.), Completion (Comp.), ...을 개선하고, Figure 2. Demonstration of iPhone and Kinect sensor depths. The iPhone struggles to capture accurate depth ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
