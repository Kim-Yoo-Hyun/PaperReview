# Insights — VarSplat: Uncertainty-aware 3D Gaussian Splatting for Robust RGB-D SLAM

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Tran_VarSplat_Uncertainty-aware_3D_Gaussian_Splatting_for_Robust_RGB-D_SLAM_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Tran_VarSplat_Uncertainty-aware_3D_Gaussian_Splatting_for_Robust_RGB-D_SLAM_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions can be shown as follows: • We introduce VarSplat, an RGB-D 3DGS-SLAM system that learns per-splat appearance variance σ2 to render ...
- **p. 3 / 3. Method - extractive body cue:** To address these issues, we introduce a novel uncertainty quantification pipeline based on per-pixel uncertainty map rendering.
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we introduce VarSplat, an uncertainty-aware RGB-D SLAM system leveraging 3D Gaussian Splatting.
- **p. 4 / 3.1. Per-pixel uncertainty rendering - extractive body cue:** By sharing the same single-pass rasterization as color and depth, V enables efficient, online, in-the-loop reliability estimation.
- **p. 5 / 3.3. Downstream Pose Estimation - extractive body cue:** Ltrack = X λc  f wp⊙∥ˆI -I∥1  +(1-λc)∥ˆD-D∥1 (17) where 0 ≤λc ≤1 balances the contribution between photometric and geometric losses, and f ...
- **p. 4 / 3.2. Mapping - extractive body cue:** To stay consistent with the Gaussian view, we use square L2 (MSE) for variance loss Lvar.
- **p. 4 / 3.2. Mapping - extractive body cue:** For color supervision, we use a weighted combination of L1 and SSIM [16], while depth loss is L1 between rendered and ground-truth depth.
- **Contribution anchor:** p. 2 (1. Introduction), p. 3 (3. Method), p. 2 (1. Introduction), p. 4 (3.1. Per-pixel uncertainty rendering), p. 5 (3.3. Downstream Pose Estimation), p. 4 (3.2. Mapping)

### Strongest assumption and failure boundary

- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we introduce VarSplat, an uncertainty-aware RGB-D SLAM system leveraging 3D Gaussian Splatting.
- **p. 2 / 1. Introduction - extractive body cue:** Despite these advances, a key limitation exists: measurement reliability is rarely modeled explicitly.
- **p. 8 / 5. Conclusion - extractive body cue:** Limitations and future works are provided in Supplementary Material.
- **p. 7 / 4.2. Quantitative Evaluation - extractive body cue:** These results also show that using the per-pixel uncertainty map to regularize the photometric loss does not degrade mesh reconstruction quality.
- **p. 8 / 5. Conclusion - extractive body cue:** Across four datasets, this integration achieves robust and competitive-to-superior performance.
- **p. 6 / 4.2. Quantitative Evaluation - extractive body cue:** On ScanNet++, VarSplat improves ATE RMSE by about 18% over the second best method and ensures robustness in long sequences where others like SplaTAM fail ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. VarSplat. Given RGB-D inputs, each 3D Gaussian jointly learns position, orientation, scale, color, opacity, and appearance variance σ2. During mapping, σ2 is optimized ...
- **Boundary to test:** Limitations and future works are provided in Supplementary Material.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | In summary, our contributions can be shown as follows: • We introduce VarSplat, an RGB-D 3DGS-SLAM system that learns per-splat appearance variance σ2 to render differentiable per-pixel uncertainty map V while maintaining ... | p. 2 (1. Introduction), p. 3 (3. Method) |
| Reported outcome | VarSplat achieves the highest accuracy with robustness on large motion camera. | p. 6 (4.2. Quantitative Evaluation), p. 6 (4.2. Quantitative Evaluation) |
| Failure/limitation | Limitations and future works are provided in Supplementary Material. | p. 8 (5. Conclusion), p. 7 (4.2. Quantitative Evaluation) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `camera/depth stream, pose, map와 language goal → robot pose, free-space/semantic map와 local goal → collision-free trajectory 또는 velocity command`.
- 이 논문의 재사용 가능한 지점은 VarSplat is an RGB-D SLAM approach that jointly estimates camera poses and incrementally updates 3D Gaussian Splatting (3DGS) map from input frames, following the general pipeline of [48, 51].를 However, pose estimation through photometric optimization can suffer from unreliable observations in low-texture regions, reflective surfaces, and areas near depth discontinuities, which can destabilize this process and potential drift.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 robot pose, free-space/semantic map와 local goal가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Limitations and future works are provided in Supplementary Material.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: In summary, our contributions can be shown as follows: • We introduce VarSplat, an RGB-D 3DGS-SLAM system that learns per-splat appearance variance σ2 to render differentiable per-pixel uncertainty map V while maintaining ...
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `World models, safety, uncertainty, and recovery`; tags: `Gaussian Splatting, geometry, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Limitations and future works are provided in Supplementary Material.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: In this section, we evaluate VarSplat against existing baselines on both synthetic and real-world datasets..
3. Compare against the body-reported baseline or a matched simpler baseline: VarSplat outperforms both 3DGS and NeRF baselines. *Photo-SLAM [11] use ORB-SLAM3 features [2] for tracking and loop closure..
4. Report the body metric and its denominator/aggregation: VarSplat achieves the highest accuracy with robustness on large motion camera..
5. Re-run the body-reported ablation/failure condition: Figure 3. Uncertainty ablation on ScanNet (scene0181). Without uncertainty, tracking jitters, loop detection has long-range drift, and registration ghosts submaps. With VarSplat enabled, the trajectory is smooth and overlaps align..
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (3.2. Mapping), p. 4 (3.2. Mapping), p. 5 (3.3. Downstream Pose Estimation); the primary result is directionally consistent at p. 6 (4.2. Quantitative Evaluation), p. 6 (4.2. Quantitative Evaluation), p. 7 (4.2. Quantitative Evaluation); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 summary, contributions, follows mechanism이 VarSplat outperforms both 3DGS and NeRF baselines. *Photo-SLAM [11] use ORB-SLAM3 features [2] for tracking and ... 대비 VarSplat achieves the highest accuracy with robustness on large motion camera.을 개선하고, Limitations and future works are provided in Supplementary Material. 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
