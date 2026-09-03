# Method - GS-SLAM: Dense Visual SLAM with 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Yan_GS-SLAM_Dense_Visual_SLAM_with_3D_Gaussian_Splatting_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Yan_GS-SLAM_Dense_Visual_SLAM_with_3D_Gaussian_Splatting_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping), p. 5 (3.3. Tracking and Bundle Adjustment), p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping), p. 5 (3.3. Tracking and Bundle Adjustment), p. 3 (3. Methodology), p. 3 (3. Methodology)): apply the proposed adaptive expansion strategy to add new or delete noisy 3D Gaussians from the whole scene representations to render RGB-D images with resolution H ⇥W, and then the ...

## Method Body Digest

- **p. 4 / 3.2. Adaptive 3D Gaussian Expanding Mapping - extractive body cue:** apply the proposed adaptive expansion strategy to add new or delete noisy 3D Gaussians from the whole scene representations to render RGB-D images with resolution ...
- **p. 5 / 3.3. Tracking and Bundle Adjustment - extractive body cue:** Further, we use this coarse camera pose and depth observation to select reliable 3D Gaussians, which guides GS-SLAM to render informative areas with clear geometric ...
- **p. 4 / 3.2. Adaptive 3D Gaussian Expanding Mapping - extractive body cue:** The 3D Gaussians are initialized and then optimized using the first RGB-D image with rendering loss.
- **p. 5 / 3.3. Tracking and Bundle Adjustment - extractive body cue:** For pose optimization stability, we only optimize the scene representation S in the first half of the iterations.
- **p. 3 / 3. Methodology - extractive body cue:** 3.1, we first introduce 3D Gaussian as the scene representation S and the RGBD render by differentiable splatting rasterization.
- **p. 3 / 3. Methodology - extractive body cue:** For camera tracking of every input frame, we derive an analytical formula for backward optimization with rendering RGB-D loss.
- **p. 4 / 3.3. Tracking and Bundle Adjustment - extractive body cue:** Then, the accurate camera pose P is optimized by minimizing rendered color loss, i.e., Ltrack = M X m=1 ###Cm -ˆCm ### 1 , min ...
- **p. 3 / 3. Methodology - extractive body cue:** We further introduce an effective coarse-to-fine technique to minimize rendering losses to achieve efficient and accurate pose estimation in Sec.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** Overall, our contributions include: • We propose GS-SLAM, the first 3D Gaussian Splatting(3DGS)-based dense RGB-D SLAM approach, which takes advantage of the fast splatting rendering ...
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose GS-SLAM, the first RGB-D dense SLAM system that first utilizes 3D Gaussian scene representation coupled with the splatting rendering technique ...
- **p. 3 / 3.1. 3D Gaussian Scene Representation - extractive body cue:** Our goal is to optimize a scene representation that captures the geometry and appearance of the scene, resulting in a detailed dense map and high-quality ...

## Source Evidence Cues

- **p. 4 / 3.2. Adaptive 3D Gaussian Expanding Mapping - extractive body cue:** apply the proposed adaptive expansion strategy to add new or delete noisy 3D Gaussians from the whole scene representations to render RGB-D images with resolution ...
- **p. 5 / 3.3. Tracking and Bundle Adjustment - extractive body cue:** Further, we use this coarse camera pose and depth observation to select reliable 3D Gaussians, which guides GS-SLAM to render informative areas with clear geometric ...
- **p. 4 / 3.2. Adaptive 3D Gaussian Expanding Mapping - extractive body cue:** The 3D Gaussians are initialized and then optimized using the first RGB-D image with rendering loss.
- **p. 5 / 3.3. Tracking and Bundle Adjustment - extractive body cue:** For pose optimization stability, we only optimize the scene representation S in the first half of the iterations.
- **p. 3 / 3. Methodology - extractive body cue:** 3.1, we first introduce 3D Gaussian as the scene representation S and the RGBD render by differentiable splatting rasterization.
- **p. 3 / 3. Methodology - extractive body cue:** For camera tracking of every input frame, we derive an analytical formula for backward optimization with rendering RGB-D loss.
- **Detected method headings:** 3. Methodology (p. 3); 6.1 Method (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | apply the proposed adaptive expansion strategy to add new or delete noisy 3D Gaussians from the whole scene representations to render RGB-D ... | p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping), p. 5 (3.3. Tracking and Bundle Adjustment) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Further, we use this coarse camera pose and depth observation to select reliable 3D Gaussians, which guides GS-SLAM to render informative areas ... | p. 5 (3.3. Tracking and Bundle Adjustment), p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | The 3D Gaussians are initialized and then optimized using the first RGB-D image with rendering loss. | p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping), p. 5 (3.3. Tracking and Bundle Adjustment) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.2. Adaptive 3D Gaussian Expanding Mapping - extractive body cue:** apply the proposed adaptive expansion strategy to add new or delete noisy 3D Gaussians from the whole scene representations to render RGB-D images with resolution ...
- **p. 4 / 3.3. Tracking and Bundle Adjustment - extractive body cue:** Then, the accurate camera pose P is optimized by minimizing rendered color loss, i.e., Ltrack = M X m=1 ###Cm -ˆCm ### 1 , min ...
- **p. 3 / 3. Methodology - extractive body cue:** We further introduce an effective coarse-to-fine technique to minimize rendering losses to achieve efficient and accurate pose estimation in Sec.
- **p. 5 / 3.3. Tracking and Bundle Adjustment - extractive body cue:** 2, in the differentiable pose estimation step for each frame, we first take advantage of image regularity to render only a sparse set of pixels ...
- **p. 3 / 3. Methodology - extractive body cue:** For camera tracking of every input frame, we derive an analytical formula for backward optimization with rendering RGB-D loss.
- **p. 5 / 3.3. Tracking and Bundle Adjustment - extractive body cue:** The final camera pose P is obtained by optimizing tracking loss in Eq.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 4 (3.3. Tracking and Bundle Adjustment), p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping), p. 3 (3. Methodology), p. 3 (3. Methodology), p. 5 (3.3. Tracking and Bundle Adjustment), p. 5 (3.3. Tracking and Bundle Adjustment).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | apply, adaptive, expansion, strategy, delete, noisy, Gaussians, whole, scene, representations, render, RGB-D, images, resolution | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | apply, adaptive, expansion, strategy, delete, noisy, Gaussians, whole, scene, representations | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | Overall, contributions, include, GS-SLAM, first, Gaussian, Splatting, DGS, dense, RGB-D | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | apply, adaptive, expansion, strategy, delete, noisy, Gaussians, whole, scene, representations | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.2. Adaptive 3D Gaussian Expanding Mapping - extractive body cue:** apply the proposed adaptive expansion strategy to add new or delete noisy 3D Gaussians from the whole scene representations to render RGB-D images with resolution ...
- **p. 3 / 3. Methodology - extractive body cue:** We aim to estimate the camera poses {Pi}N i=1 of every frame and simultaneously reconstruct a dense scene map by giving an input sequential RGB-D ...
- **p. 4 / 3.2. Adaptive 3D Gaussian Expanding Mapping - extractive body cue:** Then, we can find a pixel with coordinate (u, v) where this ray intersects the image plane and corresponding depth observation D.
- **p. 5 / 3.3. Tracking and Bundle Adjustment - extractive body cue:** Further, we use this coarse camera pose and depth observation to select reliable 3D Gaussians, which guides GS-SLAM to render informative areas with clear geometric ...
- **p. 5 / 3.3. Tracking and Bundle Adjustment - extractive body cue:** Given the projected pixel's depth observation Di and the distance di that is between 3D Gaussians Gi and the camera image plane, the reliable 3D ...
- **p. 1 / 1. Introduction - extractive body cue:** In particular, iMAP [35] uses a single multi-layer perceptron (MLP) to represent the entire scene, which is updated globally with the loss between volume-rendered RGB-D ...
- **p. 2 / 1. Introduction - extractive body cue:** It is applied to synthesize novel view RGB images of static objects, achieving state-of-the-art visual quality for 1080p resolution at real-time speed.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | At the first frame of the RGB-D sequence, we first uniformly sample half pixels from a whole image with H ⇥W resolution ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | 2, in the differentiable pose estimation step for each frame, we first take advantage of image regularity to render only a sparse ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | Overall, our contributions include: • We propose GS-SLAM, the first 3D Gaussian Splatting(3DGS)-based dense RGB-D SLAM approach, which takes advantage of the ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4.1. Experimental Setup - extractive body cue:** GS-SLAM is implemented in Python using the PyTorch framework, incorporating CUDA code for Gaussian splatting and trained on a desktop PC with a 5.50GHz Intel ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** apply, adaptive, expansion, strategy, delete, noisy, Gaussians, whole, scene, representations, render, RGB-D, images, resolution, then, updated, Gaussian, optimized, minimizing, geometric.
- **Relevant PDF headings:** 3. Methodology (p. 3); 6.1 Method (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Following [11, 27, 41, 48, 55], we use 8 scenes from the Replica dataset for localization, mesh reconstruction, and rendering quality comparison. | p. 5 (4.1. Experimental Setup), p. 6 (4.3. Rendering Evaluation) |
| Global / local decision | 3 report the mapping evaluation results of our method with other current state-of-the-art visual SLAM methods. | p. 6 (4.2. Evaluation of Localization and Mapping), p. 6 (4.2. Evaluation of Localization and Mapping) |
| Motion execution / recovery | Our method achieves the best or second performance in 7 of 8 scenes and outperforms the second-best method Point-SLAM [27] by 0.4 ... | p. 6 (4.2. Evaluation of Localization and Mapping), p. 7 (4.5. Ablation Study) |

## Failure and Ablation Link

- **p. 7 / 4.5. Ablation Study - extractive body cue:** We perform the ablation of GS-SLAM on the Replica dataset #Room0 subset to evaluate the effectiveness of coarse-to-fine tracking, and expansion mapping strategy.
- **p. 7 / 4.5. Ablation Study - extractive body cue:** 7 shows the ablation of our proposed expansion strategy for mapping.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 8. Ablation of the coarse-to-fine tracking strategy on Replica #Room0. Setting #Room0 ATE# Depth L1# Precision" Recall " F1" PSNR" SSIM" LPIPS# Coarse
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Rendering and mesh visualization of the adaptive 3D Gaussian expansion ablation on Replica #Room0. (a) Tracking performance (b) Render performance
- **p. 8 / 5. Conclusion and Limitations - extractive body cue:** We believe GS-SLAM has the potential to extend to larger scale with some improvements and will explore this in future work.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of the proposed method. We aim to use 3D Gaussians to represent the scene and use the rendered RGB-D image for inverse ...
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** We further evaluate the rendering performance using the peak signal-to-noise ratio (PSNR), SSIM [43], and LPIPS [52] by following [27].

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping), p. 5 (3.3. Tracking and Bundle Adjustment), p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping), p. 5 (3.3. Tracking and Bundle Adjustment), p. 3 (3. Methodology), p. 3 (3. Methodology), objective p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping), p. 4 (3.3. Tracking and Bundle Adjustment), p. 3 (3. Methodology), p. 5 (3.3. Tracking and Bundle Adjustment), p. 3 (3. Methodology), p. 5 (3.3. Tracking and Bundle Adjustment), temporal p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping), p. 5 (3.3. Tracking and Bundle Adjustment), p. 2 (1. Introduction), p. 3 (3. Methodology), p. 3 (3.2. Adaptive 3D Gaussian Expanding Mapping), p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
