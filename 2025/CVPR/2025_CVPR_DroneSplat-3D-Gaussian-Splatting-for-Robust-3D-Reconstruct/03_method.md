# Method - DroneSplat: 3D Gaussian Splatting for Robust 3D Reconstruction from In-the-Wild Drone Imagery

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2025/html/Tang_DroneSplat_3D_Gaussian_Splatting_for_Robust_3D_Reconstruction_from_In-the-Wild_CVPR_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2025/papers/Tang_DroneSplat_3D_Gaussian_Splatting_for_Robust_3D_Reconstruction_from_In-the-Wild_CVPR_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.2. Adaptive Local-Global Masking), p. 4 (3.2. Adaptive Local-Global Masking), p. 5 (3.2. Adaptive Local-Global Masking), p. 3 (3.2. Adaptive Local-Global Masking), p. 3 (3.2. Adaptive Local-Global Masking), p. 5 (3.2. Adaptive Local-Global Masking)): For each image Ii in the training set I, we use the segmentation model S to obtain S(Ii) = {m1 i , m2 i , · · · , mNi ...

## Method Body Digest

- **p. 4 / 3.2. Adaptive Local-Global Masking - extractive body cue:** For each image Ii in the training set I, we use the segmentation model S to obtain S(Ii) = {m1 i , m2 i , ...
- **p. 4 / 3.2. Adaptive Local-Global Masking - extractive body cue:** To establish an accurate and appropriate threshold across different scenarios and training stages, we propose an adaptive method to adjust threshold based on real-time residuals ...
- **p. 5 / 3.2. Adaptive Local-Global Masking - extractive body cue:** Specifically, we select a center point and four edge points of mj k as point prompts, which are then input into Segment Anything Model v2 ...
- **p. 3 / 3.2. Adaptive Local-Global Masking - extractive body cue:** The training loss can be defined as follows: \m a thcal {L} = (1-\lambda _{dssim})\mathcal {M}\mathcal {L}_{\text {L1}} + \lambda _{dssim}\mathcal {M}\mathcal {L}_{\text {D-SSIM}} \label ...
- **p. 3 / 3.2. Adaptive Local-Global Masking - extractive body cue:** Note that all residuals mentioned later are calculated independently and are not involved in the loss function.
- **p. 5 / 3.2. Adaptive Local-Global Masking - extractive body cue:** To address this, we employ the video segmentation capabilities of Segment Anything Model v2 [27].
- **p. 6 / 3.3. Voxel-guided Gaussian Splatting - extractive body cue:** Therefore, we additionally incorporate a voxelguided optimization strategy to direct the optimization of 3DGS under limited view constraints.
- **p. 3 / 3.1. Preliminaries - extractive body cue:** 3DGS is optimized by a combination of D-SSIM [36] and L1 loss computed from the rendered color and the ground truth color: \m a thcal ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we introduce DroneSplat, a robust 3D gaussian splatting framework tailored for inthe-wild drone imagery.
- **p. 2 / 1. Introduction - extractive body cue:** For the issue of viewpoint sparsity, our framework employs a multi-view stereo model to provide rich geometric priors by predicting dense 3D points.
- **p. 4 / 3.2. Adaptive Local-Global Masking - extractive body cue:** To establish an accurate and appropriate threshold across different scenarios and training stages, we propose an adaptive method to adjust threshold based on real-time residuals ...

## Source Evidence Cues

- **p. 4 / 3.2. Adaptive Local-Global Masking - extractive body cue:** For each image Ii in the training set I, we use the segmentation model S to obtain S(Ii) = {m1 i , m2 i , ...
- **p. 4 / 3.2. Adaptive Local-Global Masking - extractive body cue:** To establish an accurate and appropriate threshold across different scenarios and training stages, we propose an adaptive method to adjust threshold based on real-time residuals ...
- **p. 5 / 3.2. Adaptive Local-Global Masking - extractive body cue:** Specifically, we select a center point and four edge points of mj k as point prompts, which are then input into Segment Anything Model v2 ...
- **p. 3 / 3.2. Adaptive Local-Global Masking - extractive body cue:** The training loss can be defined as follows: \m a thcal {L} = (1-\lambda _{dssim})\mathcal {M}\mathcal {L}_{\text {L1}} + \lambda _{dssim}\mathcal {M}\mathcal {L}_{\text {D-SSIM}} \label ...
- **p. 3 / 3.2. Adaptive Local-Global Masking - extractive body cue:** Note that all residuals mentioned later are calculated independently and are not involved in the loss function.
- **p. 5 / 3.2. Adaptive Local-Global Masking - extractive body cue:** To address this, we employ the video segmentation capabilities of Segment Anything Model v2 [27].
- **p. 6 / 3.3. Voxel-guided Gaussian Splatting - extractive body cue:** Therefore, we additionally incorporate a voxelguided optimization strategy to direct the optimization of 3DGS under limited view constraints.
- **Detected method headings:** 3. Method (p. 3); Method (p. 7); Method (p. 8)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | For each image Ii in the training set I, we use the segmentation model S to obtain S(Ii) = {m1 i , ... | p. 4 (3.2. Adaptive Local-Global Masking), p. 4 (3.2. Adaptive Local-Global Masking) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To establish an accurate and appropriate threshold across different scenarios and training stages, we propose an adaptive method to adjust threshold based ... | p. 4 (3.2. Adaptive Local-Global Masking), p. 5 (3.2. Adaptive Local-Global Masking) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Specifically, we select a center point and four edge points of mj k as point prompts, which are then input into Segment ... | p. 5 (3.2. Adaptive Local-Global Masking), p. 3 (3.2. Adaptive Local-Global Masking) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.1. Preliminaries - extractive body cue:** 3DGS is optimized by a combination of D-SSIM [36] and L1 loss computed from the rendered color and the ground truth color: \m a thcal ...
- **p. 6 / 3.3. Voxel-guided Gaussian Splatting - extractive body cue:** Therefore, we additionally incorporate a voxelguided optimization strategy to direct the optimization of 3DGS under limited view constraints.
- **p. 3 / 3.2. Adaptive Local-Global Masking - extractive body cue:** Note that all residuals mentioned later are calculated independently and are not involved in the loss function.
- **p. 5 / 3.3. Voxel-guided Gaussian Splatting - extractive body cue:** To reconstruct a 3D model with accurate geometry in regions with limited view constraints, we utilize a learningbased multi-view stereo method, DUSt3R [35], to obtain ...
- **p. 6 / 3.3. Voxel-guided Gaussian Splatting - extractive body cue:** The gradient for such Gaussians decays exponentially with increasing distance from the voxel center.
- **p. 8 / Method - extractive body cue:** Our method reconstructs the static scenes with correct geometry even under limited view constraints.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3.2. Adaptive Local-Global Masking), p. 3 (3.2. Adaptive Local-Global Masking), p. 5 (3.3. Voxel-guided Gaussian Splatting), p. 6 (3.3. Voxel-guided Gaussian Splatting), p. 6 (3.3. Voxel-guided Gaussian Splatting), p. 8 (Method).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, posed, drone, imagery, wild, scene, goal, identify, eliminate, dynamic, distractors, Specifically, select, center | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Given, posed, drone, imagery, wild, scene, goal, identify, eliminate, dynamic | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | address, challenges, introduce, DroneSplat, robust, gaussian, splatting, framework, tailored, inthe-wild | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | DGS, optimized, combination, D-SSIM, loss, computed, rendered, color, ground, truth | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.2. Adaptive Local-Global Masking - extractive body cue:** Given a few posed drone imagery of a wild scene, our goal is to identify and eliminate dynamic distractors.
- **p. 5 / 3.2. Adaptive Local-Global Masking - extractive body cue:** Specifically, we select a center point and four edge points of mj k as point prompts, which are then input into Segment Anything Model v2 ...
- **p. 7 / Method - extractive body cue:** However, when the novel view significantly differs from the input views, the results are still suboptimal.
- **p. 8 / Method - extractive body cue:** Our approach shows competitive results compared to state-of-the-art sparse-view reconstruction methods.
- **p. 5 / 3.3. Voxel-guided Gaussian Splatting - extractive body cue:** When processing more than two images, DUSt3R applies a point cloud alignment as post-processing to generate a dense point cloud.
- **p. 2 / 1. Introduction - extractive body cue:** Similar to challenges faced in sparse-view 3D reconstruction [15, 48], radiance fields may overfit to the inputs in limited view constraints, leading to poor rendering ...
- **p. 4 / 3.2. Adaptive Local-Global Masking - extractive body cue:** The sampled point cloud is used to initialize Gaussian primitives, which is then optimized using a voxel-guided strategy.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | For the current training frame, we calculate the mathematical expectation and variance of the pixel-wise average residual: \mathb b | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | To establish an accurate and appropriate threshold across different scenarios and training stages, we propose an adaptive method to adjust threshold based ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.2. Adaptive Local-Global Masking - extractive body cue:** For each image Ii in the training set I, we use the segmentation model S to obtain S(Ii) = {m1 i , m2 i , ...
- **p. 4 / 3.2. Adaptive Local-Global Masking - extractive body cue:** To establish an accurate and appropriate threshold across different scenarios and training stages, we propose an adaptive method to adjust threshold based on real-time residuals ...
- **p. 3 / 3.2. Adaptive Local-Global Masking - extractive body cue:** The training loss can be defined as follows: \m a thcal {L} = (1-\lambda _{dssim})\mathcal {M}\mathcal {L}_{\text {L1}} + \lambda _{dssim}\mathcal {M}\mathcal {L}_{\text {D-SSIM}} \label ...
- **p. 6 / 3.3. Voxel-guided Gaussian Splatting - extractive body cue:** Therefore, we additionally incorporate a voxelguided optimization strategy to direct the optimization of 3DGS under limited view constraints.
- **p. 6 / 4.1. Setups - extractive body cue:** For our method, we train the model with 7,000 iterations and all results are obtained using a NVIDIA A100 GPU.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** image, training, segmentation, model, obtain, mNi, where, represents, mask, j-th, object, denotes, number, masks, establish, accurate, appropriate, threshold, across, different.
- **Relevant PDF headings:** 3. Method (p. 3); Method (p. 7); Method (p. 8).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | The On-the-go dataset [29] includes multiple casually captured scenes with varying ratios of occlusions. | p. 6 (4.1. Setups), p. 6 (4.1. Setups) |
| Semantic / temporal fusion | As shown in Figure 6 and Figure 7, our approach outperforms all baseline method on both DroneSplat(dynamic) datatset and NeRF On-the-go dataset. | p. 6 (4.2. Comparison), p. 7 (Figure/Table caption) |
| Robot query / planning handoff | Our method achieves the highest quantitative results, effectively eliminating dynamic distractors while preserving static details. | p. 6 (4.2. Comparison), p. 6 (4.2. Comparison) |

## Failure and Ablation Link

- **p. 6 / 4.2. Comparison - extractive body cue:** While RobustNeRF and NeRF On-the-go successfully remove distractors, they fail to retain fine details.
- **p. 6 / 4.2. Comparison - extractive body cue:** Both the baselines and our method are trained on images with dynamic distractors and evaluated on images without distractors.
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 11. The ablations of Voxel-guided 3DGS on the Drone- splat(static) and UrbanScene3D dataset. The 1st , 2nd and 3rd best results are highlighted. 11, ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5. The effect of Complement Global Masking. At t = n, the white car waiting at a red light is not identified by the ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. The effect of Adaptive Local Masking. (a) repre- sent the renderings of the same frame across different iterations t, and (b) show the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 10. The ablations of our method on the DroneS- plat(dynamic) and NeRF On-the-go dataset. The 1st , 2nd and 3rd best results are highlighted. ...
- **p. 8 / 5. Conclusions - extractive body cue:** We present DroneSplat, a novel framework for robust 3D reconstruction from in-the-wild drone imagery.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.2. Adaptive Local-Global Masking), p. 4 (3.2. Adaptive Local-Global Masking), p. 5 (3.2. Adaptive Local-Global Masking), p. 3 (3.2. Adaptive Local-Global Masking), p. 3 (3.2. Adaptive Local-Global Masking), p. 5 (3.2. Adaptive Local-Global Masking), objective p. 3 (3.1. Preliminaries), p. 6 (3.3. Voxel-guided Gaussian Splatting), p. 3 (3.2. Adaptive Local-Global Masking), p. 5 (3.3. Voxel-guided Gaussian Splatting), p. 6 (3.3. Voxel-guided Gaussian Splatting), p. 8 (Method), temporal p. 4 (3.2. Adaptive Local-Global Masking), p. 4 (3.2. Adaptive Local-Global Masking), p. 5 (3.2. Adaptive Local-Global Masking), p. 5 (3.2. Adaptive Local-Global Masking), p. 6 (4.1. Setups), p. 7 (Method).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
