# Method - GaussianGrow: Geometry-aware Gaussian Growing from 3D Point Clouds with Text Guidance

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_GaussianGrow_Geometry-aware_Gaussian_Growing_from_3D_Point_Clouds_with_Text_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_GaussianGrow_Geometry-aware_Gaussian_Growing_from_3D_Point_Clouds_with_Text_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3.3. Iterative Inpainting and Refinement), p. 5 (3.2. Appearance Generation), p. 4 (3.2. Appearance Generation), p. 3 (3.2. Appearance Generation), p. 3 (3.2. Appearance Generation), p. 4 (3.2. Appearance Generation)): To systematically identify the unseen regions, we propose a visibility-based optimization approach that predicts camera poses observing the largest invisible regions in the point cloud.

## Method Body Digest

- **p. 5 / 3.3. Iterative Inpainting and Refinement - extractive body cue:** To systematically identify the unseen regions, we propose a visibility-based optimization approach that predicts camera poses observing the largest invisible regions in the point cloud.
- **p. 5 / 3.2. Appearance Generation - extractive body cue:** Our optimization strategy follows a two-phase approach that first addresses the six cardinal views V = {vi}6 i=1 before focusing on overlap regions.
- **p. 4 / 3.2. Appearance Generation - extractive body cue:** To optimize these poses for enhanced appearance generation, we make them learnable through an optimization strategy that enforces alignment between the normal vectors of intersecting ...
- **p. 3 / 3.2. Appearance Generation - extractive body cue:** The commonly used setting for multiview diffusion models is to generate six cardinal views.
- **p. 3 / 3.2. Appearance Generation - extractive body cue:** In practice, we adopt Hunyuan3D-Paint [46] as the multi-view diffusion model for view synthesis.
- **p. 4 / 3.2. Appearance Generation - extractive body cue:** Pose Optimization for Additional Views.
- **p. 6 / 3.3. Iterative Inpainting and Refinement - extractive body cue:** This iteration continues until all Gaussians are generated, where we empirically find that six iterations are sufficient for most models.
- **p. 5 / 3.3. Iterative Inpainting and Refinement - extractive body cue:** This differentiable formulation enables efficient gradient descent optimization of learnable camera poses, enabling the systematic discovery of viewpoints that reveal largest unseen regions of the ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Our contributions can be summarized as follows: • We propose GaussianGrow, a novel approach that generates 3D Gaussians by learning to grow them from easily ...
- **p. 2 / 1. Introduction - extractive body cue:** Bridging the gap between point cloud geometries and 3D Gaussian Splatting appearances, we introduce a novel perspective that rethinks Gaussian generation by growing 3D Gaussians ...
- **p. 3 / 3. Method - extractive body cue:** We present GaussianGrow, a novel generative model for 3D Gaussian Splatting by learning to grow 3D Gaussians from 3D point cloud geometries.

## Source Evidence Cues

- **p. 5 / 3.3. Iterative Inpainting and Refinement - extractive body cue:** To systematically identify the unseen regions, we propose a visibility-based optimization approach that predicts camera poses observing the largest invisible regions in the point cloud.
- **p. 5 / 3.2. Appearance Generation - extractive body cue:** Our optimization strategy follows a two-phase approach that first addresses the six cardinal views V = {vi}6 i=1 before focusing on overlap regions.
- **p. 4 / 3.2. Appearance Generation - extractive body cue:** To optimize these poses for enhanced appearance generation, we make them learnable through an optimization strategy that enforces alignment between the normal vectors of intersecting ...
- **p. 3 / 3.2. Appearance Generation - extractive body cue:** The commonly used setting for multiview diffusion models is to generate six cardinal views.
- **p. 3 / 3.2. Appearance Generation - extractive body cue:** In practice, we adopt Hunyuan3D-Paint [46] as the multi-view diffusion model for view synthesis.
- **p. 4 / 3.2. Appearance Generation - extractive body cue:** Pose Optimization for Additional Views.
- **p. 6 / 3.3. Iterative Inpainting and Refinement - extractive body cue:** This iteration continues until all Gaussians are generated, where we empirically find that six iterations are sufficient for most models.
- **Detected method headings:** 2.1. 3D Generative Models (p. 2); 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To systematically identify the unseen regions, we propose a visibility-based optimization approach that predicts camera poses observing the largest invisible regions in ... | p. 5 (3.3. Iterative Inpainting and Refinement), p. 5 (3.2. Appearance Generation) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Our optimization strategy follows a two-phase approach that first addresses the six cardinal views V = {vi}6 i=1 before focusing on overlap ... | p. 5 (3.2. Appearance Generation), p. 4 (3.2. Appearance Generation) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | To optimize these poses for enhanced appearance generation, we make them learnable through an optimization strategy that enforces alignment between the normal ... | p. 4 (3.2. Appearance Generation), p. 3 (3.2. Appearance Generation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.3. Iterative Inpainting and Refinement - extractive body cue:** This differentiable formulation enables efficient gradient descent optimization of learnable camera poses, enabling the systematic discovery of viewpoints that reveal largest unseen regions of the ...
- **p. 5 / 3.3. Iterative Inpainting and Refinement - extractive body cue:** For each pair of Gaussians (gi, gj), where gi is unoptimized and gj is optimized, we formulate the occlusion loss as: Locc = X i,j ...
- **p. 3 / 3.1. Preliminary Preparation - extractive body cue:** We compute normals N = {ni}N i=1 through gradient prediction: ni = ∇fu(pi) ∥∇fu(pi)∥.
- **p. 3 / 3.1. Preliminary Preparation - extractive body cue:** The normal map Ni is obtained by inferring gradients at the zero-level set of the learned unsigned distance field.
- **p. 4 / 3.2. Appearance Generation - extractive body cue:** (2) Minimizing Lalign ensures that additional cameras are optimally positioned to align with local geometric structures, reducing projection distortions and enhancing view consistency.
- **p. 4 / 3.2. Appearance Generation - extractive body cue:** Specifically, for each overlap region Ri,j, we define the loss as one minus the absolute cosine similarity between the normal ng at a Gaussian g ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3.1. Preliminary Preparation), p. 3 (3.1. Preliminary Preparation), p. 4 (3.2. Appearance Generation), p. 5 (3.3. Iterative Inpainting and Refinement), p. 5 (3.3. Iterative Inpainting and Refinement).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | UDF, Field, Multi-View, Diffusion, Stable, ControlNet, Black, Red, Dragon, Depth, Map, Input, Point, Clouds | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | UDF, Field, Multi-View, Diffusion, Stable, ControlNet, Black, Red, Dragon, Depth | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, summarized, follows, GaussianGrow, novel, generates, Gaussians, learning, grow, them | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | differentiable, formulation, enables, efficient, gradient, descent, optimization, learnable, camera, poses | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.2. Appearance Generation - extractive body cue:** UDF Field Multi-View Diffusion Stable Diffusion ControlNet "Black and Red Dragon" Depth Map Input Point Clouds Normal Maps Position Maps Primary View Pose Optimization for ...
- **p. 3 / 3.1. Preliminary Preparation - extractive body cue:** To extract comprehensive geometric information from the input point cloud, we compute three geometric representation maps: depth, normal, and position maps, each serving a distinct ...
- **p. 6 / 3.3. Iterative Inpainting and Refinement - extractive body cue:** Visual comparison on the Objaverse dataset shows that GaussianGrow uses point clouds instead of meshes. the depth map Di rendered from vi, the rendered occluded ...
- **p. 3 / 3. Method - extractive body cue:** Given a point cloud input P = {pi}N i=1, GaussianGrow aims to learn high-fidelity Gaussian primitives G = {gi}M i=1, conditioned on a text prompt ...
- **p. 5 / 3.2. Appearance Generation - extractive body cue:** Given the reference appearance and the geometric maps at all the K = 10 views, the multi-view diffusion model finally generates high-fidelity appearance outputs I ...
- **p. 5 / 3.3. Iterative Inpainting and Refinement - extractive body cue:** To systematically identify the unseen regions, we propose a visibility-based optimization approach that predicts camera poses observing the largest invisible regions in the point cloud.
- **p. 6 / 3.3. Iterative Inpainting and Refinement - extractive body cue:** Due to noises and uneven density in the raw point cloud data, some points may remain difficult to observe after image inpainting-based Gaussian inpainting.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | With the proper initialization, the next step is to generate appearances for Gaussian optimization. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The next step is to generate high-quality appearances from both the pre-set six cardinal views and four additional views focusing on the ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** systematically, identify, unseen, regions, visibility-based, optimization, predicts, camera, poses, observing, largest, invisible, point, cloud, strategy, follows, two-phase, first, addresses, cardinal.
- **Relevant PDF headings:** 2.1. 3D Generative Models (p. 2); 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | To demonstrate robustness with real-world data, we also utilized the DeepFashion3D dataset 18974 | p. 7 (4.3. Point to Gaussian Generation), p. 7 (4.2. Text-to-3D Generation) |
| Semantic / temporal fusion | The retrieve-based GaussianGrow "Ours+Uni3D" achieves the best performance across all evaluation metrics, while the generative-based version "Ours+LGM" also achieves comparable performance compared ... | p. 7 (4.2. Text-to-3D Generation), p. 7 (4.1. Text-Guided Visual Synthesis) |
| Robot query / planning handoff | Moreover, applying the geometry of LGM to GaussianGrow also achieves significantly better performance by replacing the appearance of LGM with GaussianGrow. | p. 7 (4.2. Text-to-3D Generation), p. 7 (4.2. Text-to-3D Generation) |

## Failure and Ablation Link

- **p. 8 / 4.4. Ablation Study - extractive body cue:** Ablation results for key components of GaussianGrow.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** We evaluate our key components through ablation experiments.
- **p. 6 / 4. Experiments - extractive body cue:** Finally, we validate our design choices through detailed ablation studies in Sec.
- **p. 6 / 4.1. Text-Guided Visual Synthesis - extractive body cue:** Unlike many competing approaches that require complete mesh representations, GaussianGrow operates directly on point cloud inputs, without additional geometric information.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. The effect of Gaussian inpainting. Before Overlap Processing After Overlap Processing
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overview of GaussianGrow. Stage 1. We leverage depth-aware ControlNet for primary view generation, with a geometry- aware diffusion model for multi-view synthesis. Additional ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4. Spatial Inpainting. Due to noises and uneven density in the raw point cloud data, some points may remain difficult to observe after image ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3.3. Iterative Inpainting and Refinement), p. 5 (3.2. Appearance Generation), p. 4 (3.2. Appearance Generation), p. 3 (3.2. Appearance Generation), p. 3 (3.2. Appearance Generation), p. 4 (3.2. Appearance Generation), objective p. 5 (3.3. Iterative Inpainting and Refinement), p. 5 (3.3. Iterative Inpainting and Refinement), p. 3 (3.1. Preliminary Preparation), p. 3 (3.1. Preliminary Preparation), p. 4 (3.2. Appearance Generation), p. 4 (3.2. Appearance Generation), temporal p. 3 (3.2. Appearance Generation), p. 4 (3.2. Appearance Generation), p. 4 (3.2. Appearance Generation), p. 5 (3.2. Appearance Generation), p. 6 (3.3. Iterative Inpainting and Refinement), p. 6 (3.3. Iterative Inpainting and Refinement).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
