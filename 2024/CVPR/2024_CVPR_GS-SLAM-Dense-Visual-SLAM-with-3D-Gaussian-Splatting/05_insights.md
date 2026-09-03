# Insights — GS-SLAM: Dense Visual SLAM with 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Yan_GS-SLAM_Dense_Visual_SLAM_with_3D_Gaussian_Splatting_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Yan_GS-SLAM_Dense_Visual_SLAM_with_3D_Gaussian_Splatting_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** Overall, our contributions include: • We propose GS-SLAM, the first 3D Gaussian Splatting(3DGS)-based dense RGB-D SLAM approach, which takes advantage of the fast splatting rendering ...
- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose GS-SLAM, the first RGB-D dense SLAM system that first utilizes 3D Gaussian scene representation coupled with the splatting rendering technique ...
- **p. 3 / 3.1. 3D Gaussian Scene Representation - extractive body cue:** Our goal is to optimize a scene representation that captures the geometry and appearance of the scene, resulting in a detailed dense map and high-quality ...
- **p. 4 / 3.2. Adaptive 3D Gaussian Expanding Mapping - extractive body cue:** apply the proposed adaptive expansion strategy to add new or delete noisy 3D Gaussians from the whole scene representations to render RGB-D images with resolution ...
- **p. 5 / 3.3. Tracking and Bundle Adjustment - extractive body cue:** Further, we use this coarse camera pose and depth observation to select reliable 3D Gaussians, which guides GS-SLAM to render informative areas with clear geometric ...
- **p. 4 / 3.2. Adaptive 3D Gaussian Expanding Mapping - extractive body cue:** The 3D Gaussians are initialized and then optimized using the first RGB-D image with rendering loss.
- **p. 5 / 3.3. Tracking and Bundle Adjustment - extractive body cue:** For pose optimization stability, we only optimize the scene representation S in the first half of the iterations.
- **Contribution anchor:** p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. 3D Gaussian Scene Representation), p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping), p. 5 (3.3. Tracking and Bundle Adjustment), p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** However, these methods face serious challenges in obtaining fine-grained dense maps.
- **p. 1 / 1. Introduction - extractive body cue:** In practical mapping and tracking steps, these methods only render a small set of pixels to reduce optimization time, which leads to the reconstructed dense ...
- **p. 2 / 1. Introduction - extractive body cue:** We enhance scene reconstruction by introducing an adaptive strategy for managing 3D Gaussian elements, which optimizes mapping by focusing on current observations and minimizes errors ...
- **p. 8 / 5. Conclusion and Limitations - extractive body cue:** We believe GS-SLAM has the potential to extend to larger scale with some improvements and will explore this in future work.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of the proposed method. We aim to use 3D Gaussians to represent the scene and use the rendered RGB-D image for inverse ...
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** We further evaluate the rendering performance using the peak signal-to-noise ratio (PSNR), SSIM [43], and LPIPS [52] by following [27].
- **Boundary to test:** We believe GS-SLAM has the potential to extend to larger scale with some improvements and will explore this in future work.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | Overall, our contributions include: • We propose GS-SLAM, the first 3D Gaussian Splatting(3DGS)-based dense RGB-D SLAM approach, which takes advantage of the fast splatting rendering technique to boost the mapping optimizing and ... | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Reported outcome | Our method achieves the best or second performance in 7 of 8 scenes and outperforms the second-best method Point-SLAM [27] by 0.4 cm on average at 8.34 FPS. | p. 6 (4.2. Evaluation of Localization and Mapping), p. 7 (4.5. Ablation Study) |
| Failure/limitation | We believe GS-SLAM has the potential to extend to larger scale with some improvements and will explore this in future work. | p. 8 (5. Conclusion and Limitations), p. 3 (Figure/Table caption) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- 이 논문의 재사용 가능한 지점은 apply the proposed adaptive expansion strategy to add new or delete noisy 3D Gaussians from the whole scene representations to render RGB-D images with resolution H ⇥W, and then the updated 3D ...를 We aim to estimate the camera poses {Pi}N i=1 of every frame and simultaneously reconstruct a dense scene map by giving an input sequential RGB-D stream {Ii, Di}M i=1 with known camera ...로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 robot pose, free-space/semantic map와 local goal가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 We believe GS-SLAM has the potential to extend to larger scale with some improvements and will explore this in future work.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: Overall, our contributions include: • We propose GS-SLAM, the first 3D Gaussian Splatting(3DGS)-based dense RGB-D SLAM approach, which takes advantage of the fast splatting rendering technique to boost the mapping optimizing and ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `SLAM, Gaussian Splatting, geometry`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** We believe GS-SLAM has the potential to extend to larger scale with some improvements and will explore this in future work.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: Following [11, 27, 41, 48, 55], we use 8 scenes from the Replica dataset for localization, mesh reconstruction, and rendering quality comparison..
3. Compare against the body-reported baseline or a matched simpler baseline: 3 report the mapping evaluation results of our method with other current state-of-the-art visual SLAM methods..
4. Report the body metric and its denominator/aggregation: For localization, we use the absolute trajectory (ATE, cm) error [33] to measure the accuracy of the estimated camera poses..
5. Re-run the body-reported ablation/failure condition: We perform the ablation of GS-SLAM on the Replica dataset #Room0 subset to evaluate the effectiveness of coarse-to-fine tracking, and expansion mapping strategy..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping), p. 5 (3.3. Tracking and Bundle Adjustment), p. 4 (3.2. Adaptive 3D Gaussian Expanding Mapping); the primary result is directionally consistent at p. 6 (4.2. Evaluation of Localization and Mapping), p. 7 (4.5. Ablation Study), p. 8 (Figure/Table caption); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Overall, contributions, include mechanism이 3 report the mapping evaluation results of our method with other current state-of-the-art visual SLAM methods. 대비 For localization, we use the absolute trajectory (ATE, cm) error [33] to measure the accuracy of the estimated ...을 개선하고, We believe GS-SLAM has the potential to extend to larger scale with some improvements and will ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
