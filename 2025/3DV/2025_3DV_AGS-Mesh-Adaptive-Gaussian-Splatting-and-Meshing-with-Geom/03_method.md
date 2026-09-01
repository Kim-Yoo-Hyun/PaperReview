# Method - AGS-Mesh: Adaptive Gaussian Splatting and Meshing with Geometric Priors for Indoor Room Reconstruction Using Smartphones

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=fTJrKaBKZk&name=pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (4.1. Regularization with Depth Normal Consistency), p. 4 (4.1. Regularization with Depth Normal Consistency), p. 5 (4.1. Regularization with Depth Normal Consistency), p. 5 (4.2. Adaptive Normal Regularization), p. 6 (4.4. Mesh Extraction), p. 6 (4.4. Mesh Extraction)): To filter inaccurate depth estimates, we check the orientation consistency between Nd and Np generated from pre-train model with an angle threshold τd for filtering: Df = ( 0 if ...

## Method Body Digest

- **p. 4 / 4.1. Regularization with Depth Normal Consistency - extractive PDF cue:** To filter inaccurate depth estimates, we check the orientation consistency between Nd and Np generated from pre-train model with an angle threshold τd for filtering: ...
- **p. 4 / 4.1. Regularization with Depth Normal Consistency - extractive PDF cue:** We propose an adaptive depth regularization method based on the consistency of normals derived from noisy depth images and those from pretrained networks.
- **p. 5 / 4.1. Regularization with Depth Normal Consistency - extractive PDF cue:** Furthermore, we propose an adaptive TSDF and octree-based Marching Cubes meshing strategy enabling the extraction of smoother and more geometrically detailed meshes.
- **p. 5 / 4.2. Adaptive Normal Regularization - extractive PDF cue:** The ANR strategy is designed to first regularize Gaussian normals using the fully pre-trained normals Np, and subsequently relax the training by relying only on ...
- **p. 6 / 4.4. Mesh Extraction - extractive PDF cue:** Next, we apply the IsoOctree meshing algorithm [24], which starts with a uniform grid and progressively subdivides the volume into finer regions based on a ...
- **p. 6 / 4.4. Mesh Extraction - extractive PDF cue:** To achieve this, we employ a point cloud hint: we back-project our output depth maps from all training images into a point cloud and expand ...
- **p. 5 / 4.2. Adaptive Normal Regularization - extractive PDF cue:** To allow the gradients from the normal loss during optimization to directly influence the Gaussian geometry, ˆN is estimated from rendered depth maps as in ...
- **p. 5 / 4.3. Optimization - extractive PDF cue:** Take 3DGS [26] as an example, the final optimization loss is expressed as: L = Lcolor + λdLD + λnLN (10) where Lcolor is the ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** We summarize our contributions with the following statements: • We propose a novel regularization strategy for indoor room reconstruction that adaptively filters geometric priors from ...
- **p. 4 / 4. Method - extractive PDF cue:** Our method consists of two adaptive supervision strategies for Gaussian Splatting-based methods that effectively combine supervision signals from geometric priors obtained from mobile devices and ...
- **p. 4 / 4. Method - extractive PDF cue:** Lastly, in Section 4.4, we propose a novel octree-based mesh extraction method that enhances surface quality and detail preservation compared to previous approaches.

## Source Evidence Cues

- **p. 4 / 4.1. Regularization with Depth Normal Consistency - extractive PDF cue:** To filter inaccurate depth estimates, we check the orientation consistency between Nd and Np generated from pre-train model with an angle threshold τd for filtering: ...
- **p. 4 / 4.1. Regularization with Depth Normal Consistency - extractive PDF cue:** We propose an adaptive depth regularization method based on the consistency of normals derived from noisy depth images and those from pretrained networks.
- **p. 5 / 4.1. Regularization with Depth Normal Consistency - extractive PDF cue:** Furthermore, we propose an adaptive TSDF and octree-based Marching Cubes meshing strategy enabling the extraction of smoother and more geometrically detailed meshes.
- **p. 5 / 4.2. Adaptive Normal Regularization - extractive PDF cue:** The ANR strategy is designed to first regularize Gaussian normals using the fully pre-trained normals Np, and subsequently relax the training by relying only on ...
- **p. 6 / 4.4. Mesh Extraction - extractive PDF cue:** Next, we apply the IsoOctree meshing algorithm [24], which starts with a uniform grid and progressively subdivides the volume into finer regions based on a ...
- **p. 6 / 4.4. Mesh Extraction - extractive PDF cue:** To achieve this, we employ a point cloud hint: we back-project our output depth maps from all training images into a point cloud and expand ...
- **Detected method headings:** 4. Method (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To filter inaccurate depth estimates, we check the orientation consistency between Nd and Np generated from pre-train model with an angle threshold ... | p. 4 (4.1. Regularization with Depth Normal Consistency), p. 4 (4.1. Regularization with Depth Normal Consistency) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | We propose an adaptive depth regularization method based on the consistency of normals derived from noisy depth images and those from pretrained ... | p. 4 (4.1. Regularization with Depth Normal Consistency), p. 5 (4.1. Regularization with Depth Normal Consistency) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Furthermore, we propose an adaptive TSDF and octree-based Marching Cubes meshing strategy enabling the extraction of smoother and more geometrically detailed meshes. | p. 5 (4.1. Regularization with Depth Normal Consistency), p. 5 (4.2. Adaptive Normal Regularization) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4.2. Adaptive Normal Regularization - extractive PDF cue:** To allow the gradients from the normal loss during optimization to directly influence the Gaussian geometry, ˆN is estimated from rendered depth maps as in ...
- **p. 5 / 4.3. Optimization - extractive PDF cue:** Take 3DGS [26] as an example, the final optimization loss is expressed as: L = Lcolor + λdLD + λnLN (10) where Lcolor is the ...
- **p. 4 / 4. Method - extractive PDF cue:** In Section 4.2, we carefully utilize the pretrained monocular normal estimates for normal supervision, mitigating regularization in cases where the pretrained estimates - due to ...
- **p. 4 / 4. Method - extractive PDF cue:** We describe the overall optimization process in Section 4.3.
- **p. 6 / 4.4. Mesh Extraction - extractive PDF cue:** 6, we show that the underlying geometry from an optimized Gaussian scene can be further refined with this IsoOctree-based method.
- **p. 6 / 4.4. Mesh Extraction - extractive PDF cue:** Next, we apply the IsoOctree meshing algorithm [24], which starts with a uniform grid and progressively subdivides the volume into finer regions based on a ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (4.2. Adaptive Normal Regularization), p. 5 (4.3. Optimization).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | achieve, employ, point, cloud, hint, back-project, output, depth, maps, training, images, expand, voxel, width | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | achieve, employ, point, cloud, hint, back-project, output, depth, maps, training | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summarize, contributions, following, statements, novel, regularization, strategy, indoor, room, reconstruction | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | allow, gradients, normal, loss, during, optimization, directly, influence, Gaussian, geometry | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 4.4. Mesh Extraction - extractive PDF cue:** To achieve this, we employ a point cloud hint: we back-project our output depth maps from all training images into a point cloud and expand ...
- **p. 2 / 1. Introduction - extractive PDF cue:** We summarize our contributions with the following statements: • We propose a novel regularization strategy for indoor room reconstruction that adaptively filters geometric priors from ...
- **p. 4 / 4. Method - extractive PDF cue:** We first predict normal estimates from a pretrained monocular estimation model [14] for input RGB images captured with a mobile device.
- **p. 4 / 4. Method - extractive PDF cue:** Lastly, in Section 4.4, we propose a novel octree-based mesh extraction method that enhances surface quality and detail preservation compared to previous approaches.
- **p. 5 / 4.1. Regularization with Depth Normal Consistency - extractive PDF cue:** Furthermore, we propose an adaptive TSDF and octree-based Marching Cubes meshing strategy enabling the extraction of smoother and more geometrically detailed meshes.
- **p. 3 / 3.1. Geometric Priors from Handheld Devices - extractive PDF cue:** Although these models learn from large-scale image-geometry pairs, they struggle to achieve the same accuracy in metric depth compared to physical sensors found in devices ...
- **p. 3 / 3.1. Geometric Priors from Handheld Devices - extractive PDF cue:** In the case of the iPhone, the resolution of the physical sensors is usually very small (e.g., only 16 × 16); however, sophisticated post-processing and ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | The reported results are based on two distinct evaluation datasets: a test set obtained by uniformly sampling every 10 frames within the ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | To filter inaccurate depth estimates, we check the orientation consistency between Nd and Np generated from pre-train model with an angle threshold ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | The reported results are based on two distinct evaluation datasets: a test set obtained by uniformly sampling every 10 frames within the ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 4.1. Regularization with Depth Normal Consistency - extractive PDF cue:** To filter inaccurate depth estimates, we check the orientation consistency between Nd and Np generated from pre-train model with an angle threshold τd for filtering: ...
- **p. 4 / 4.1. Regularization with Depth Normal Consistency - extractive PDF cue:** We propose an adaptive depth regularization method based on the consistency of normals derived from noisy depth images and those from pretrained networks.
- **p. 5 / 4.2. Adaptive Normal Regularization - extractive PDF cue:** The ANR strategy is designed to first regularize Gaussian normals using the fully pre-trained normals Np, and subsequently relax the training by relying only on ...
- **p. 6 / 4.4. Mesh Extraction - extractive PDF cue:** To achieve this, we employ a point cloud hint: we back-project our output depth maps from all training images into a point cloud and expand ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** filter, inaccurate, depth, estimates, check, orientation, consistency, between, generated, pre-train, model, angle, threshold, filtering, otherwise, where, arccos, During, training, first.
- **Relevant PDF headings:** 4. Method (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We focus on real-world indoor scenes captured using a mobile device. | p. 6 (5. Experiments), p. 6 (5. Experiments) |
| Semantic / temporal fusion | We compared our method to the following baselines: a) Traditional 3D reconstruction method Volumetric Fusion [9]. b) state-of-the-art NeRF-based method Nerfacto [41]; ... | p. 6 (5. Experiments), p. 8 (Figure/Table caption) |
| Robot query / planning handoff | We observe that utilizing noisy depths significantly improves the baseline. | p. 7 (5.3. Ablation Studies), p. 6 (5.1. 3D Reconstruction Evaluation) |

## Failure and Ablation Link

- **p. 6 / 5.1. 3D Reconstruction Evaluation - extractive PDF cue:** Our results demonstrate that the novel adaptive depth and normal regularization terms we propose (also showcased in the ablation study Table 3) improve mesh quality ...
- **p. 8 / 5.3. Ablation Studies - extractive PDF cue:** Ablation on supervision strategy and mesh performance (MuSHRoom).
- **p. 8 / 5.3. Ablation Studies - extractive PDF cue:** Ablation on monocular and sensor depth supervision on the "vr room" scene from MuSHRoom.
- **p. 16 / Figure/Table caption - extractive PDF cue:** Figure 8. Qualitative visuals of our Depth Normal Consistency (DNR) and Adaptive Normal Regularization (ANR) terms. We visualize sensor depth and normals obtained from a ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Pipeline Overview. Our approach leverages geometric consistency between normals derived from raw sensor depths and those predicted by a pretrained model to filter ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Demonstration of iPhone and Kinect sensor depths. The iPhone struggles to capture accurate depth values for (a) objects at a far distance, and ...
- **p. 8 / 5.3. Ablation Studies - extractive PDF cue:** Lastly, the DNC and ANR terms help preserve details for objects and reduce overall noise.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (4.1. Regularization with Depth Normal Consistency), p. 4 (4.1. Regularization with Depth Normal Consistency), p. 5 (4.1. Regularization with Depth Normal Consistency), p. 5 (4.2. Adaptive Normal Regularization), p. 6 (4.4. Mesh Extraction), p. 6 (4.4. Mesh Extraction), objective p. 5 (4.2. Adaptive Normal Regularization), p. 5 (4.3. Optimization), p. 4 (4. Method), p. 4 (4. Method), p. 6 (4.4. Mesh Extraction), p. 6 (4.4. Mesh Extraction), temporal p. 7 (5.2. Novel View Synthesis), p. 4 (4.1. Regularization with Depth Normal Consistency), p. 5 (4.4. Mesh Extraction), p. 5 (4.3. Optimization), p. 6 (5. Experiments), p. 6 (5.1. 3D Reconstruction Evaluation).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
