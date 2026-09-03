# Method - SC-OmniGS: Self-Calibrating Omnidirectional Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=7idCpuEAiR; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/113436. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 3 (1 INTRODUCTION), p. 1 (ABSTRACT)): To summarize, the main contributions of this work include: • We proposed the first system for self-calibrating omnidirectional radiance fields, which jointly optimizes 3D Gaussians, omnidirectional camera poses, and camera ...

## Method Body Digest

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To summarize, the main contributions of this work include: • We proposed the first system for self-calibrating omnidirectional radiance fields, which jointly optimizes 3D Gaussians, ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Moreover, considering omnidirectional images in the equirectangular projection have an unbalanced spatial resolution, we introduce weighted spherical photometric loss to ensure the spatially equivalent optimization.
- **p. 1 / ABSTRACT - extractive body cue:** Furthermore, we introduce a differentiable omnidirectional camera model in order to rectify the distortion of real-world data for performance enhancement.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** It can also facilitate other applications such as GS-based omnidirectional SLAM. • We introduced a novel differentiable omnidirectional camera model that effectively tackles the complex ...
- **p. 1 / ABSTRACT - extractive body cue:** Overall, the omnidirectional camera intrinsic model, extrinsic poses, and 3D Gaussians are jointly optimized by minimizing weighted spherical photometric loss.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We jointly optimize 3D Gaussians, camera poses, and camera models by minimizing photometric loss between rendered and undistorted omnidirectional images.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Crucially, we derive omnidirectional camera pose gradients within the rendering procedure, enabling the optimization of noisy camera poses and even learning from scratch.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** (2023b), have demonstrated the feasibility and efficiency of reconstructing omnidirectional radiance fields in large scenes using sparse and wide-baseline 360-degree image inputs.

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To summarize, the main contributions of this work include: • We proposed the first system for self-calibrating omnidirectional radiance fields, which jointly optimizes 3D Gaussians, ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we propose SC-OmniGS, a novel system that self-calibrates the omnidirectional camera model and poses along with omnidirectional radiance field reconstruction.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** It can also facilitate other applications such as GS-based omnidirectional SLAM. • We introduced a novel differentiable omnidirectional camera model that effectively tackles the complex ...

## Source Evidence Cues

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To summarize, the main contributions of this work include: • We proposed the first system for self-calibrating omnidirectional radiance fields, which jointly optimizes 3D Gaussians, ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Moreover, considering omnidirectional images in the equirectangular projection have an unbalanced spatial resolution, we introduce weighted spherical photometric loss to ensure the spatially equivalent optimization.
- **p. 1 / ABSTRACT - extractive body cue:** Furthermore, we introduce a differentiable omnidirectional camera model in order to rectify the distortion of real-world data for performance enhancement.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** It can also facilitate other applications such as GS-based omnidirectional SLAM. • We introduced a novel differentiable omnidirectional camera model that effectively tackles the complex ...
- **p. 1 / ABSTRACT - extractive body cue:** Overall, the omnidirectional camera intrinsic model, extrinsic poses, and 3D Gaussians are jointly optimized by minimizing weighted spherical photometric loss.
- **Detected method headings:** C.1 PSEUDO-CODE OF DIFFERENTIABLE OMNIDIRECTIONAL CAMERA MODEL (p. 14)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To summarize, the main contributions of this work include: • We proposed the first system for self-calibrating omnidirectional radiance fields, which jointly ... | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Moreover, considering omnidirectional images in the equirectangular projection have an unbalanced spatial resolution, we introduce weighted spherical photometric loss to ensure the ... | p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Furthermore, we introduce a differentiable omnidirectional camera model in order to rectify the distortion of real-world data for performance enhancement. | p. 1 (ABSTRACT), p. 3 (1 INTRODUCTION) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / ABSTRACT - extractive body cue:** Overall, the omnidirectional camera intrinsic model, extrinsic poses, and 3D Gaussians are jointly optimized by minimizing weighted spherical photometric loss.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We jointly optimize 3D Gaussians, camera poses, and camera models by minimizing photometric loss between rendered and undistorted omnidirectional images.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Crucially, we derive omnidirectional camera pose gradients within the rendering procedure, enabling the optimization of noisy camera poses and even learning from scratch.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** (2023b), have demonstrated the feasibility and efficiency of reconstructing omnidirectional radiance fields in large scenes using sparse and wide-baseline 360-degree image inputs.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | rectify, distortion, patterns, input, image, differentiable, omnidirectional, camera, model, comprising, learnable, spherical, grid, regress | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | rectify, distortion, patterns, input, image, differentiable, omnidirectional, camera, model, comprising | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summarize, main, contributions, include, first, system, self-calibrating, omnidirectional, radiance, fields | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Overall, omnidirectional, camera, intrinsic, model, extrinsic, poses, Gaussians, jointly, optimized | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To rectify distortion patterns in the input image, we propose a differentiable omnidirectional camera model comprising a learnable 3D spherical grid to regress the camera ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** (2023b), have demonstrated the feasibility and efficiency of reconstructing omnidirectional radiance fields in large scenes using sparse and wide-baseline 360-degree image inputs.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** We thus obtain undistorted omnidirectional images by re-sampling input images based on the learned omnidirectional camera model.
- **p. 1 / ABSTRACT - extractive body cue:** Rather than converting 360-degree images to cube maps and performing perspective image calibration, we treat 360-degree images as a whole sphere and derive a mathematical ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | The initial learning rates for each camera quaternion q and translation t are set to 0.01, with exponential decay to 1.6e-4 and ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Calibration w/o Perturb w/ Perturb train test train test PSNR ↑SSIM ↑LPIPS ↓PSNR ↑SSIM ↑LPIPS ↓PSNR ↑SSIM ↑LPIPS ↓PSNR ↑SSIM ↑LPIPS ↓ ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | The initial learning rates for each camera quaternion q and translation t are set to 0.01, with exponential decay to 1.6e-4 and ... | hardware, batch and throughput |

## Training vs Inference

- **p. 10 / 5 EXPERIMENTS - extractive body cue:** To further assess the robustness of our method against varying levels of camera perturbation, we conducted experiments using the same learning rate with increasing scales ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** summarize, main, contributions, include, first, system, self-calibrating, omnidirectional, radiance, fields, jointly, optimizes, Gaussians, camera, poses, models, provided, derivation, pose, gradients.
- **Relevant PDF headings:** C.1 PSEUDO-CODE OF DIFFERENTIABLE OMNIDIRECTIONAL CAMERA MODEL (p. 14).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We evaluated SG-OmniGS against several SOTA models on datasets of 360-degree images, including eight real-world multi-room scenes from 360Roam dataset (Huang et ... | p. 7 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Semantic / temporal fusion | Furthermore, when compared to other calibration baselines (see Barbershop in Table 1), SC-OmniGS consistently outperforms them with most increased rotation noise scales. | p. 10 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |
| Robot query / planning handoff | When trained with pose perturbation, our full model, incorporating both camera model and pose optimization, consistently achieves improvement in both training and ... | p. 10 (5 EXPERIMENTS), p. 8 (5 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 10 / 5 EXPERIMENTS - extractive body cue:** To validate the effectiveness of our camera calibration, we conducted ablation studies on a real scene Center, with and without perturbation to training cameras.
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Our method is able to effectively optimize the scene representation, displaying a low sensitivity to initial values.
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 6: Ablation study of weighted spherical photometric loss Lwsp. Without using Lwsp, the estimated poses of some cameras suffer obvious errors leading to performance ...
- **p. 16 / Figure/Table caption - extractive body cue:** Table 5: Ablation study. "Re-init" indicates re-initialization of 3D Gaussians; w/o Lwsp means we disable the spherical weight and calculate classical photometric loss for optimization; ...
- **p. 8 / 5 EXPERIMENTS - extractive body cue:** Additionally, we initialized all training cameras at the origin, enabling training the models from scratch without pose priors.
- **p. 10 / 5 EXPERIMENTS - extractive body cue:** When the input camera poses are estimated by SfM without perturbation, we can slightly increase the quality of radiance field reconstruction by camera pose refinement, ...
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** 2) Following 360Roam (Huang et al., 2022), we replaced the ray sampling functions of NeRF-based methods (BARF, L2G-NeRF, CamP) with omnidirectional ray sampling to support ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (ABSTRACT), p. 3 (1 INTRODUCTION), p. 1 (ABSTRACT), objective p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), temporal p. 7 (5 EXPERIMENTS), p. 10 (5 EXPERIMENTS), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (2 RELATED WORK).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
