# Method - WaterSplatting: Fast Underwater 3D Scene Reconstruction using Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=Z9yn9YgNIz&name=pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.3. Loss Function Alignment), p. 3 (3.1. Preliminaries), p. 5 (3.3. Loss Function Alignment), p. 3 (3. Method), p. 4 (3.3. Loss Function Alignment), p. 5 (3.3. Loss Function Alignment)): For the case of our 3DGS-based model, we propose a regularized loss function LReg: we apply pixel-wise weight W = {wi,j} on both rendered estimate ˆy and target image y, ...

## Method Body Digest

- **p. 4 / 3.3. Loss Function Alignment - extractive body cue:** For the case of our 3DGS-based model, we propose a regularized loss function LReg: we apply pixel-wise weight W = {wi,j} on both rendered estimate ...
- **p. 3 / 3.1. Preliminaries - extractive body cue:** For scene rendering in scattering media we use the revised underwater image formation model from [1] where the final image I is separated into a ...
- **p. 5 / 3.3. Loss Function Alignment - extractive body cue:** Integrating regularization into the LReg-DSSIM formulation becomes particularly critical for 3DGS optimization due to the discrete nature of its primitives, necessitating structural regularization to maintain ...
- **p. 3 / 3. Method - extractive body cue:** Then, we illustrate our proposed rendering model combining 3DGS with medium encoding in Sec.
- **p. 4 / 3.3. Loss Function Alignment - extractive body cue:** In low-light situations, [25] proposed a regularized L2 loss LReg-L2 = ((sg(ˆy) + ϵ)-1 ⊙(ˆy -y))2, (19) to boost the weight of the dark regions ...
- **p. 5 / 3.3. Loss Function Alignment - extractive body cue:** To model the smoothness of volumetric medium, we employ LReg-L2 as our pixel-level loss.
- **p. 3 / 3.1. Preliminaries - extractive body cue:** During optimization, 3DGS periodically densify Gaussians with high average gradient on 2D coordinates ˆµi across frames via splitting large ones and duplicating small ones.
- **p. 5 / 3.3. Loss Function Alignment - extractive body cue:** and the regularized D-SSIM loss LReg-DSSIM = LDSSIM(W ⊙y, W ⊙ˆy).

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Loss Function Alignment: We propose a novel loss function designed to align 3DGS with human perception of High Dynamic Range (HDR) and low-light scenes.
- **p. 2 / 1. Introduction - extractive body cue:** Splatting with Medium: We introduce a novel approach that combines the strengths of Gaussian Splatting (GS) and volume rendering.
- **p. 3 / 3.2. Splatting with Medium - extractive body cue:** We illustrate the pipeline of our method in Fig.

## Source Evidence Cues

- **p. 4 / 3.3. Loss Function Alignment - extractive body cue:** For the case of our 3DGS-based model, we propose a regularized loss function LReg: we apply pixel-wise weight W = {wi,j} on both rendered estimate ...
- **p. 3 / 3.1. Preliminaries - extractive body cue:** For scene rendering in scattering media we use the revised underwater image formation model from [1] where the final image I is separated into a ...
- **p. 5 / 3.3. Loss Function Alignment - extractive body cue:** Integrating regularization into the LReg-DSSIM formulation becomes particularly critical for 3DGS optimization due to the discrete nature of its primitives, necessitating structural regularization to maintain ...
- **p. 3 / 3. Method - extractive body cue:** Then, we illustrate our proposed rendering model combining 3DGS with medium encoding in Sec.
- **p. 4 / 3.3. Loss Function Alignment - extractive body cue:** In low-light situations, [25] proposed a regularized L2 loss LReg-L2 = ((sg(ˆy) + ϵ)-1 ⊙(ˆy -y))2, (19) to boost the weight of the dark regions ...
- **p. 5 / 3.3. Loss Function Alignment - extractive body cue:** To model the smoothness of volumetric medium, we employ LReg-L2 as our pixel-level loss.
- **Detected method headings:** 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | For the case of our 3DGS-based model, we propose a regularized loss function LReg: we apply pixel-wise weight W = {wi,j} on ... | p. 4 (3.3. Loss Function Alignment), p. 3 (3.1. Preliminaries) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | For scene rendering in scattering media we use the revised underwater image formation model from [1] where the final image I is ... | p. 3 (3.1. Preliminaries), p. 5 (3.3. Loss Function Alignment) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Integrating regularization into the LReg-DSSIM formulation becomes particularly critical for 3DGS optimization due to the discrete nature of its primitives, necessitating structural ... | p. 5 (3.3. Loss Function Alignment), p. 3 (3. Method) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.3. Loss Function Alignment - extractive body cue:** For the case of our 3DGS-based model, we propose a regularized loss function LReg: we apply pixel-wise weight W = {wi,j} on both rendered estimate ...
- **p. 4 / 3.3. Loss Function Alignment - extractive body cue:** In low-light situations, [25] proposed a regularized L2 loss LReg-L2 = ((sg(ˆy) + ϵ)-1 ⊙(ˆy -y))2, (19) to boost the weight of the dark regions ...
- **p. 5 / 3.3. Loss Function Alignment - extractive body cue:** Integrating regularization into the LReg-DSSIM formulation becomes particularly critical for 3DGS optimization due to the discrete nature of its primitives, necessitating structural regularization to maintain ...
- **p. 3 / 3.1. Preliminaries - extractive body cue:** During optimization, 3DGS periodically densify Gaussians with high average gradient on 2D coordinates ˆµi across frames via splitting large ones and duplicating small ones.
- **p. 5 / 3.3. Loss Function Alignment - extractive body cue:** and the regularized D-SSIM loss LReg-DSSIM = LDSSIM(W ⊙y, W ⊙ˆy).
- **p. 3 / 3. Method - extractive body cue:** At last, we explain our proposed loss function to align 3DGS with human perception of HDR scenes in Sec.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (3.3. Loss Function Alignment), p. 3 (3. Method), p. 3 (3.1. Preliminaries), p. 4 (3.3. Loss Function Alignment), p. 5 (3.3. Loss Function Alignment), p. 5 (3.3. Loss Function Alignment).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | input, model, images, scattering, medium, corresponding, camera, poses, meantime, DGS, prunes, primitives, opacity, acceleration | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | input, model, images, scattering, medium, corresponding, camera, poses, meantime, DGS | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Loss, Function, Alignment, novel, designed, align, DGS, human, perception, High | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | case, DGS-based, model, regularized, loss, function, LReg, apply, pixel-wise, weight | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 3.2. Splatting with Medium - extractive body cue:** The input to our model is a set of images with scattering medium and corresponding camera poses.
- **p. 3 / 3.1. Preliminaries - extractive body cue:** In the meantime, 3DGS prunes primitives with low opacity for acceleration and periodically set αi close to zero for all Gaussians to moderate the increase ...
- **p. 4 / 3.2. Splatting with Medium - extractive body cue:** (11) The contributed color of the Gi to final output is Cobj i (r) = T obj i T med(si)αici = T obj i αiciexp(-σmedsi), ...
- **p. 4 / 3.3. Loss Function Alignment - extractive body cue:** For the case of our 3DGS-based model, we propose a regularized loss function LReg: we apply pixel-wise weight W = {wi,j} on both rendered estimate ...
- **p. 5 / 3.3. Loss Function Alignment - extractive body cue:** Our final proposed loss function is LReg = (1 -λ)LReg-L2 + λLReg-DSSIM .
- **p. 2 / 1. Introduction - extractive body cue:** The results of our evaluation demonstrate the effectiveness of our proposed method in achieving high-quality, efficient underwater reconstruction.
- **p. 2 / 1. Introduction - extractive body cue:** To address this issue, a NeRF approach, SeaThru-NeRF [18], was proposed, which uses two fields: one for the geometry and one for the volume in ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | During optimization, 3DGS periodically densify Gaussians with high average gradient on 2D coordinates ˆµi across frames via splitting large ones and duplicating ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | We reset opacity to 0.5 every 500 training steps and prune gaussians with opacity below 0.5 every 100 training steps. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | We also calculate the FPS and total training time using the same RTX 4080 GPU to illustrate the speed difference between baselines ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4. Experiments - extractive body cue:** We also calculate the FPS and total training time using the same RTX 4080 GPU to illustrate the speed difference between baselines and our method.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** case, DGS-based, model, regularized, loss, function, LReg, apply, pixel-wise, weight, rendered, estimate, target, image, where, pixel, coordinate, denotes, stopping, gradient.
- **Relevant PDF headings:** 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | SeaThru-NeRF Dataset: SeaThru-NeRF Dataset released by [18] contains real-world scenes acquired from four different scenes in sea: IUI3 Red Sea, Curac¸ao, Japanese ... | p. 5 (4. Experiments), p. 5 (4.1. Results) |
| Semantic / temporal fusion | Our rendering without medium and depth maps significantly outperform those from the SeaThru-NeRF, especially in scenes that are farther from the camera. | p. 7 (4.1. Results), p. 5 (4. Experiments) |
| Robot query / planning handoff | Our rendering without medium and depth maps significantly outperform those from the SeaThru-NeRF, especially in scenes that are farther from the camera. | p. 7 (4.1. Results), p. 6 (4.1. Results) |

## Failure and Ablation Link

- **p. 7 / 4.2. Ablation Study - extractive body cue:** We conduct a quantitative analysis on different combination of loss functions, between pixel-wise component {L1, L2, LReg-L1, LReg-L2} and frame-wise {LDSSIM, LReg-DSSIM}, as well as ...
- **p. 5 / 4. Experiments - extractive body cue:** We present the alpha blending of depth as the depth map and the rendering without medium to demonstrate the ability to decouple the medium and ...
- **p. 6 / 4.1. Results - extractive body cue:** For Restoration, we further show the rendered medium without rendering objects.
- **p. 6 / 4.1. Results - extractive body cue:** We compare our method with SeaThru-NeRF by showing both the full image and the rendering without the medium.
- **p. 7 / 4.1. Results - extractive body cue:** Our rendering without medium and depth maps significantly outperform those from the SeaThru-NeRF, especially in scenes that are farther from the camera.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 8. Limitation: insufficient supervision. Our method (left) has low-detail visuals in regions not sufficiently covered by train- ing views. SeaThru-NeRF [18] (right) is blurry ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Ablation Study Avg. over SeaThru-NeRF Scenes Configuration PSNR↑ SSIM↑ LPIPS↓ L1+LDSSIM 29.219 0.915

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.3. Loss Function Alignment), p. 3 (3.1. Preliminaries), p. 5 (3.3. Loss Function Alignment), p. 3 (3. Method), p. 4 (3.3. Loss Function Alignment), p. 5 (3.3. Loss Function Alignment), objective p. 4 (3.3. Loss Function Alignment), p. 4 (3.3. Loss Function Alignment), p. 5 (3.3. Loss Function Alignment), p. 3 (3.1. Preliminaries), p. 5 (3.3. Loss Function Alignment), p. 3 (3. Method), temporal p. 3 (3.1. Preliminaries), p. 5 (4. Experiments), p. 5 (4.1. Results), p. 6 (4.1. Results), p. 7 (4.2. Ablation Study), p. 7 (4.2. Ablation Study).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
