# Method - NeRF Is a Valuable Assistant for 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Fang_NeRF_Is_a_Valuable_Assistant_for_3D_Gaussian_Splatting_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Fang_NeRF_Is_a_Valuable_Assistant_for_3D_Gaussian_Splatting_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (4.3. Joint Optimization in Dual-branch), p. 5 (4.3. Joint Optimization in Dual-branch), p. 5 (4.3. Joint Optimization in Dual-branch), p. 4 (4.3. Joint Optimization in Dual-branch)): To synchronize optimization, we propose rendering NeRF using only partial rays in each iteration.

## Method Body Digest

- **p. 4 / 4.3. Joint Optimization in Dual-branch - extractive PDF cue:** To synchronize optimization, we propose rendering NeRF using only partial rays in each iteration.
- **p. 5 / 4.3. Joint Optimization in Dual-branch - extractive PDF cue:** (10) For the GS branch, we use an L1 norm loss Lrgb gs and SSIM loss LSSIM gs for rendered images, along with a volume ...
- **p. 5 / 4.3. Joint Optimization in Dual-branch - extractive PDF cue:** (11) For dual-branch collaborative loss, we use L1 norm Lrgb joint to constrain the rendered pixel values along GS-Rays in the NeRF branch with corresponding ...
- **p. 4 / 4.3. Joint Optimization in Dual-branch - extractive PDF cue:** NeRF requires dense sampling and network queries, which preclude rendering an entire image in a single pass like in 3DGS.
- **p. 5 / 4.3. Joint Optimization in Dual-branch - extractive PDF cue:** During joint training, we design loss functions for single-branch optimization and dual-branch collaboration.
- **p. 4 / 4.3. Joint Optimization in Dual-branch - extractive PDF cue:** This design ensures that the sampling points in the NeRF branch are distributed as closely as possible to the Gaussian spheres, thereby aligning the scene ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Moreover, the weak correlation between discrete Gaussians results in a lack of smooth spatial transitions [7, 8, 40], which negatively affects the visual quality of ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To address this, we propose explicitly modeling their discrepancies by optimizing residual vectors for both features and positions to personalize and enhance 3DGS performance.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** To this end, we propose NeRF-GS, a novel framework that integrates the NeRF network into the training of the 3DGS model, leveraging specific NeRF properties ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To address this, we propose explicitly modeling their discrepancies by optimizing residual vectors for both features and positions to personalize and enhance 3DGS performance.
- **p. 4 / 4.3. Joint Optimization in Dual-branch - extractive PDF cue:** To synchronize optimization, we propose rendering NeRF using only partial rays in each iteration.

## Source Evidence Cues

- **p. 4 / 4.3. Joint Optimization in Dual-branch - extractive PDF cue:** To synchronize optimization, we propose rendering NeRF using only partial rays in each iteration.
- **p. 5 / 4.3. Joint Optimization in Dual-branch - extractive PDF cue:** (10) For the GS branch, we use an L1 norm loss Lrgb gs and SSIM loss LSSIM gs for rendered images, along with a volume ...
- **p. 5 / 4.3. Joint Optimization in Dual-branch - extractive PDF cue:** (11) For dual-branch collaborative loss, we use L1 norm Lrgb joint to constrain the rendered pixel values along GS-Rays in the NeRF branch with corresponding ...
- **p. 4 / 4.3. Joint Optimization in Dual-branch - extractive PDF cue:** NeRF requires dense sampling and network queries, which preclude rendering an entire image in a single pass like in 3DGS.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To synchronize optimization, we propose rendering NeRF using only partial rays in each iteration. | p. 4 (4.3. Joint Optimization in Dual-branch), p. 5 (4.3. Joint Optimization in Dual-branch) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | (10) For the GS branch, we use an L1 norm loss Lrgb gs and SSIM loss LSSIM gs for rendered images, along ... | p. 5 (4.3. Joint Optimization in Dual-branch), p. 5 (4.3. Joint Optimization in Dual-branch) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | (11) For dual-branch collaborative loss, we use L1 norm Lrgb joint to constrain the rendered pixel values along GS-Rays in the NeRF ... | p. 5 (4.3. Joint Optimization in Dual-branch), p. 4 (4.3. Joint Optimization in Dual-branch) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4.3. Joint Optimization in Dual-branch - extractive PDF cue:** (10) For the GS branch, we use an L1 norm loss Lrgb gs and SSIM loss LSSIM gs for rendered images, along with a volume ...
- **p. 5 / 4.3. Joint Optimization in Dual-branch - extractive PDF cue:** During joint training, we design loss functions for single-branch optimization and dual-branch collaboration.
- **p. 4 / 4.3. Joint Optimization in Dual-branch - extractive PDF cue:** To synchronize optimization, we propose rendering NeRF using only partial rays in each iteration.
- **p. 4 / 4.3. Joint Optimization in Dual-branch - extractive PDF cue:** This design ensures that the sampling points in the NeRF branch are distributed as closely as possible to the Gaussian spheres, thereby aligning the scene ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (4.3. Joint Optimization in Dual-branch), p. 5 (4.3. Joint Optimization in Dual-branch).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Moreover, weak, correlation, between, discrete, Gaussians, lack, smooth, spatial, transitions, negatively, affects, visual, quality | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Moreover, weak, correlation, between, discrete, Gaussians, lack, smooth, spatial, transitions | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | NeRF-GS, novel, framework, integrates, NeRF, network, training, DGS, model, leveraging | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | branch, norm, loss, Lrgb, SSIM, LSSIM, rendered, images, along, volume | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1. Introduction - extractive PDF cue:** Moreover, the weak correlation between discrete Gaussians results in a lack of smooth spatial transitions [7, 8, 40], which negatively affects the visual quality of ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To address this, we propose explicitly modeling their discrepancies by optimizing residual vectors for both features and positions to personalize and enhance 3DGS performance.
- **p. 2 / 1. Introduction - extractive PDF cue:** To this end, we propose NeRF-GS, a novel framework that integrates the NeRF network into the training of the 3DGS model, leveraging specific NeRF properties ...
- **p. 4 / 4.3. Joint Optimization in Dual-branch - extractive PDF cue:** To synchronize optimization, we propose rendering NeRF using only partial rays in each iteration.
- **p. 4 / 4.3. Joint Optimization in Dual-branch - extractive PDF cue:** NeRF requires dense sampling and network queries, which preclude rendering an entire image in a single pass like in 3DGS.
- **p. 5 / 4.3. Joint Optimization in Dual-branch - extractive PDF cue:** (10) For the GS branch, we use an L1 norm loss Lrgb gs and SSIM loss LSSIM gs for rendered images, along with a volume ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | 3 demonstrate our method's superior capability in capturing high-frequency textures and fine geometric details while better reflecting lighting conditions. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Additionally, we compare metrics for training time (minutes), storage size (MB), and rendering speed (FPS) to assess the model's compactness and efficiency. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4.3. Joint Optimization in Dual-branch - extractive PDF cue:** (11) For dual-branch collaborative loss, we use L1 norm Lrgb joint to constrain the rendered pixel values along GS-Rays in the NeRF branch with corresponding ...
- **p. 5 / 5.1. Implementation Details - extractive PDF cue:** Additionally, we compare metrics for training time (minutes), storage size (MB), and rendering speed (FPS) to assess the model's compactness and efficiency.
- **p. 7 / 5.2. Comparison - extractive PDF cue:** We report the FPS, model size (MB), training time (minutes) and PSNR.
- **p. 8 / 5.3. Qualitative Analysis of NeRF-GS - extractive PDF cue:** This suggests that integrating the NeRF branch is a worthwhile trade-off despite the increase in training time.
- **p. 8 / 5.3. Qualitative Analysis of NeRF-GS - extractive PDF cue:** We also compare it with an extendedtraining version of 3DGSL, showing NeRF-GS outperforms 3DGS even with similar training time.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** synchronize, optimization, rendering, NeRF, only, partial, rays, iteration, branch, norm, loss, Lrgb, SSIM, LSSIM, rendered, images, along, volume, regularization, Lvol.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We report experimental results on real-world datasets, including Mip-NeRF360 (all 9 scenes) [5], Tanks&Temples [29] DeepBlending [23], and the Blender dataset [41]. | p. 5 (5.1. Implementation Details), p. 5 (5.1. Implementation Details) |
| Semantic / temporal fusion | Comparative results are shown in Table 1, where our approach significantly outperforms the vanilla 3DGS model and other state-of-the-art methods across PSNR, ... | p. 5 (5.2. Comparison), p. 5 (5.2. Comparison) |
| Robot query / planning handoff | Notably, compared to other methods that incorporate NeRF-like concepts, such as VDGS and Hash-GS, NeRF-GS achieves even more substantial improvements. | p. 5 (5.2. Comparison), p. 5 (5.2. Comparison) |

## Failure and Ablation Link

- **p. 8 / 5.3. Qualitative Analysis of NeRF-GS - extractive PDF cue:** Ablation of different components in NeRF-GS on Tank&Temples and DeepBlending datasets.
- **p. 8 / 5.4. Ablation Studies - extractive PDF cue:** Moreover, to examine the effect of feature sharing, we directly train the GS branch with learnable feature parameters, remarked as ‘w/o Feature Share'.
- **p. 5 / 5.1. Implementation Details - extractive PDF cue:** Our method is focused on enhancing GS branch performance, so we primarily compare it with 3DGS [27] and its variants, including C3DGS [44], Scaffold-GS [35], ...
- **p. 6 / 5.2. Comparison - extractive PDF cue:** Our method demonstrates a significant advantage over 3DGS and its variants, achieving a more faithful representation of scene details. validating NeRF-GS as a robust framework ...
- **p. 7 / 5.3. Qualitative Analysis of NeRF-GS - extractive PDF cue:** When associations between two branches are directly removed, such as feature sharing, loss constraints during joint training, etc., the NeRF-GS shows large visual quality degradation.
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of NeRF-GS. (a) We first pretrain a Hash-based NeRF network to acquire continuous spatial encoding capabilities and implicit scene representation. (b) Utilizing ...
- **p. 8 / 7. Conclusion - extractive PDF cue:** These strategies effectively address several limitations of 3DGS, including initialization dependency, limited spatial awareness, insufficient Gaussian sphere correlation, and overfitting in sparse-view scenes.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (4.3. Joint Optimization in Dual-branch), p. 5 (4.3. Joint Optimization in Dual-branch), p. 5 (4.3. Joint Optimization in Dual-branch), p. 4 (4.3. Joint Optimization in Dual-branch), objective p. 5 (4.3. Joint Optimization in Dual-branch), p. 5 (4.3. Joint Optimization in Dual-branch), p. 4 (4.3. Joint Optimization in Dual-branch), p. 4 (4.3. Joint Optimization in Dual-branch), temporal p. 5 (5.2. Comparison), p. 5 (5.1. Implementation Details), p. 6 (5.2. Comparison), p. 7 (5.2. Comparison), p. 7 (5.2. Comparison), p. 8 (5.3. Qualitative Analysis of NeRF-GS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
