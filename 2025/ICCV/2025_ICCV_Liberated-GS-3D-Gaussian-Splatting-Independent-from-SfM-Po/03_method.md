# Method - Liberated-GS: 3D Gaussian Splatting Independent from SfM Point Clouds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Pan_Liberated-GS_3D_Gaussian_Splatting_Independent_from_SfM_Point_Clouds_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Pan_Liberated-GS_3D_Gaussian_Splatting_Independent_from_SfM_Point_Clouds_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (3. Method), p. 2 (3. Method), p. 3 (3.2. Effective Depth Alignment), p. 4 (3.2. Effective Depth Alignment), p. 4 (3.2. Effective Depth Alignment), p. 5 (3.3. Progressive Segmented Initialization)): … …… Importance Resampling Progressive Segmented Initialization RGB Images Random Init Monocular Depth Estimator Coarse Gaussian Model Estimate Render Rendered Depth Estimated Depth Align Ensembled Depth Effective Depth Alignment Erosio ...

## Method Body Digest

- **p. 3 / 3. Method - extractive body cue:** … …… Importance Resampling Progressive Segmented Initialization RGB Images Random Init Monocular Depth Estimator Coarse Gaussian Model Estimate Render Rendered Depth Estimated Depth Align Ensembled ...
- **p. 2 / 3. Method - extractive body cue:** The optimization stage remains unchanged.
- **p. 3 / 3.2. Effective Depth Alignment - extractive body cue:** As the coarse model is not fully optimized, direct alpha-blending introduces noise.
- **p. 4 / 3.2. Effective Depth Alignment - extractive body cue:** This implies that the resulting coarse Gaussian model offers a rough estimate of the scene's depth.
- **p. 4 / 3.2. Effective Depth Alignment - extractive body cue:** (a) Rendered Depth from an under-optimized 3DGS model can achieve view-consistent recovery in well-observed areas but underperforms in low-texture regions.
- **p. 5 / 3.3. Progressive Segmented Initialization - extractive body cue:** Besides, we downsample the training images to further reduce redundant 3D Gaussians.
- **p. 5 / 3.2. Effective Depth Alignment - extractive body cue:** Since we do not have SfM points as ground truth, the rendered depths from the coarse Gaussian Model serve as references.
- **p. 6 / 3.3. Progressive Segmented Initialization - extractive body cue:** we optimize the photometric loss to refine the ensembled depths {D1, D2, . . . , Dki} for all previous views.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** The contributions of our method are as follows. • We propose Librated-GS, a novel initialization approach to eliminate the reliance on SfM points of 3D ...
- **p. 2 / 3. Method - extractive body cue:** 3.3, we present a progressive segmented initialization with importance resampling.
- **p. 3 / 3. Method - extractive body cue:** To address this, we propose an unbiased depth rendering method detailed in Sec.

## Source Evidence Cues

- **p. 3 / 3. Method - extractive body cue:** … …… Importance Resampling Progressive Segmented Initialization RGB Images Random Init Monocular Depth Estimator Coarse Gaussian Model Estimate Render Rendered Depth Estimated Depth Align Ensembled ...
- **p. 2 / 3. Method - extractive body cue:** The optimization stage remains unchanged.
- **p. 3 / 3.2. Effective Depth Alignment - extractive body cue:** As the coarse model is not fully optimized, direct alpha-blending introduces noise.
- **p. 4 / 3.2. Effective Depth Alignment - extractive body cue:** This implies that the resulting coarse Gaussian model offers a rough estimate of the scene's depth.
- **p. 4 / 3.2. Effective Depth Alignment - extractive body cue:** (a) Rendered Depth from an under-optimized 3DGS model can achieve view-consistent recovery in well-observed areas but underperforms in low-texture regions.
- **p. 5 / 3.3. Progressive Segmented Initialization - extractive body cue:** Besides, we downsample the training images to further reduce redundant 3D Gaussians.
- **p. 5 / 3.2. Effective Depth Alignment - extractive body cue:** Since we do not have SfM points as ground truth, the rendered depths from the coarse Gaussian Model serve as references.
- **Detected method headings:** 3. Method (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | … …… Importance Resampling Progressive Segmented Initialization RGB Images Random Init Monocular Depth Estimator Coarse Gaussian Model Estimate Render Rendered Depth Estimated ... | p. 3 (3. Method), p. 2 (3. Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | The optimization stage remains unchanged. | p. 2 (3. Method), p. 3 (3.2. Effective Depth Alignment) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | As the coarse model is not fully optimized, direct alpha-blending introduces noise. | p. 3 (3.2. Effective Depth Alignment), p. 4 (3.2. Effective Depth Alignment) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 3.3. Progressive Segmented Initialization - extractive body cue:** we optimize the photometric loss to refine the ensembled depths {D1, D2, . . . , Dki} for all previous views.
- **p. 3 / 3. Method - extractive body cue:** … …… Importance Resampling Progressive Segmented Initialization RGB Images Random Init Monocular Depth Estimator Coarse Gaussian Model Estimate Render Rendered Depth Estimated Depth Align Ensembled ...
- **p. 4 / 3.2. Effective Depth Alignment - extractive body cue:** Visual comparison of depth maps and reprojected points with the standard alpha-blending method and our unbiased alphablending method. tion Gi, this problem is equivalent to ...
- **p. 5 / 3.2. Effective Depth Alignment - extractive body cue:** We solve for the scale si and shift ti using the closed-form linear regression solution: si, ti = arg min X pi(kj)=1 //Dalign(kj) -Drender(k′ j)//2 ...
- **p. 2 / 3. Method - extractive body cue:** The optimization stage remains unchanged.
- **p. 2 / 3. Method - extractive body cue:** 3.3, we present a progressive segmented initialization with importance resampling.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 6 (3.3. Progressive Segmented Initialization), p. 3 (3. Method), p. 4 (3.2. Effective Depth Alignment), p. 5 (3.2. Effective Depth Alignment), p. 5 (3.3. Progressive Segmented Initialization).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | pipeline, reconstruct, photo-realistic, scenes, posed, image, sequences, without, requiring, input, point, cloud, Specifically, taking | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | pipeline, reconstruct, photo-realistic, scenes, posed, image, sequences, without, requiring, input | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, follows, Librated-GS, novel, initialization, eliminate, reliance, SfM, points, Gaussian | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | optimize, photometric, loss, refine, ensembled, depths, Dki, previous, views, Importance | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 3. Method - extractive body cue:** We propose a pipeline to reconstruct photo-realistic scenes from posed image sequences without requiring an input point cloud.
- **p. 5 / 3.2. Effective Depth Alignment - extractive body cue:** Specifically, taking the current view I along with its rendered image Irender and depth map Drender from Eq.
- **p. 5 / 3.3. Progressive Segmented Initialization - extractive body cue:** For a sequence of n consecutively captured RGB images I = {I1, I2, . . . , In} with their corresponding ensembled depths D = ...
- **p. 2 / 1. Introduction - extractive body cue:** Moreover, [14] generates Gaussians for every pixel of each input image, which leads to substantial computational costs.
- **p. 4 / 3.2. Effective Depth Alignment - extractive body cue:** We compare the point cloud from different depths for single view and multiple views.
- **p. 4 / 3.2. Effective Depth Alignment - extractive body cue:** Consequently, approximating the Gaussian depth using the center depth can result in a point cloud with significant floaters when reprojected back into the world space, ...
- **p. 3 / 3. Method - extractive body cue:** To address this, we propose an unbiased depth rendering method detailed in Sec.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | We propose a pipeline to reconstruct photo-realistic scenes from posed image sequences without requiring an input point cloud. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | As highlighted in RAINGS [18], the sparse-large-variance (SLV) initialization enables effective signal prediction within few training steps. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Comparison of runtime between our pipeline and COLMAP on Scene03 (300 images, 1237×658 resolution) from OMMO [25] dataset. | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.3. Progressive Segmented Initialization - extractive body cue:** Besides, we downsample the training images to further reduce redundant 3D Gaussians.
- **p. 6 / 4.1. Experimental Setup - extractive body cue:** The number of pre-training steps is set to 5000 for indoor datasets and 10000 for outdoor datasets to achieve a roughly accurate scene structure.
- **p. 3 / 3.2. Effective Depth Alignment - extractive body cue:** As highlighted in RAINGS [18], the sparse-large-variance (SLV) initialization enables effective signal prediction within few training steps.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Importance, Resampling, Progressive, Segmented, Initialization, RGB, Images, Random, Init, Monocular, Depth, Estimator, Coarse, Gaussian, Model, Estimate, Render, Rendered, Estimated, Align.
- **Relevant PDF headings:** 3. Method (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | To validate the effectiveness of our method, extensive qualitative and quantitative comparison experiments are conducted on three real-world datasets, including two benchmark ... | p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup) |
| Semantic / temporal fusion | Our method demonstrates substantial improvements across all three metrics compared to all other methods, even outperforming 3DGS initialized with SfM point clouds. | p. 6 (4.2. Comparison), p. 6 (4.2. Comparison) |
| Robot query / planning handoff | Our method demonstrates substantial improvements across all three metrics compared to all other methods, even outperforming 3DGS initialized with SfM point clouds. | p. 6 (4.2. Comparison), p. 7 (4.2. Comparison) |

## Failure and Ablation Link

- **p. 8 / 4.2. Comparison - extractive body cue:** Ablation for proposed components in our framework on Mip-NeRF360 [5] dataset.
- **p. 6 / 4.2. Comparison - extractive body cue:** This quantitatively validates that our approach achieves superior rendering and geometry results even without additional high-quality point clouds.
- **p. 8 / 4.2. Comparison - extractive body cue:** Ablation for different depths used for initialization on Mip-NeRF360 [5] dataset.
- **p. 6 / 4.2. Comparison - extractive body cue:** Additionally, since [14] does not account for scale when utilizing monocular depth to estimate camera poses and generate 3D points, directly using the ground-truth poses ...
- **p. 8 / 4.2. Comparison - extractive body cue:** Depth PSNR↑ SSIM↑ LPIPS↓ Ensembled Depth 27.588 0.822 0.187 Aligned Depth 27.524 0.818 0.189 Estimated Depth 27.390 0.816 0.191 Rendered Depth 26.596 0.708 0.201 segmented ...
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Our initialization does not interfere with subsequent optimization.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Novel View Synthesis Comparison. We propose a novel Gaussian Splatting initialization pipeline to address the degradation in novel view rendering quality caused by ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (3. Method), p. 2 (3. Method), p. 3 (3.2. Effective Depth Alignment), p. 4 (3.2. Effective Depth Alignment), p. 4 (3.2. Effective Depth Alignment), p. 5 (3.3. Progressive Segmented Initialization), objective p. 6 (3.3. Progressive Segmented Initialization), p. 3 (3. Method), p. 4 (3.2. Effective Depth Alignment), p. 5 (3.2. Effective Depth Alignment), p. 2 (3. Method), p. 2 (3. Method), temporal p. 2 (3. Method), p. 3 (3.2. Effective Depth Alignment), p. 3 (3. Method), p. 4 (3.2. Effective Depth Alignment), p. 5 (3.3. Progressive Segmented Initialization), p. 5 (3.3. Progressive Segmented Initialization).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
