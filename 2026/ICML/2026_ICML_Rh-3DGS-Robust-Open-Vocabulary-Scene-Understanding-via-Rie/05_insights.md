# Insights — Rh-3DGS: Robust Open-Vocabulary Scene Understanding via Riemannian Huber Distillation and Manifold-Aware Sampling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=bjtuHOb3vN; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/331577. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 4 / 4.3. Visibility-Calibrated Distillation (VCD) - extractive body cue:** We propose Visibility-Calibrated Distillation (VCD).
- **p. 5 / 4.4. Visibility-Weighted Fr´echet Mean (VFM) - extractive body cue:** We propose Visibility-Weighted Fr´echet Mean (VFM).
- **p. 4 / 4.3. Visibility-Calibrated Distillation (VCD) - extractive body cue:** Low accumulated opacity often indicates weak or unstable contributions.
- **p. 3 / 4.1. Problem Formulation and Notation - extractive body cue:** Each Gaussian stores a lowdimensional semantic latent fi ∈Rd and a lightweight decoder maps it to the teacher feature space: hi = Dec(fi) ∈ RD.
- **p. 4 / 4.2. Overview - extractive body cue:** We optimize the model end-to-end: L = Lrgb + λsem LVFM + λcon LLIC, (4) where Lrgb is the photometric loss, LVFM is the reweighted ...
- **p. 4 / 4.1. Problem Formulation and Notation - extractive body cue:** Rh-3DGS 𝒊 radius 𝜸 same semantic (in 𝓝) excluded 𝑳𝑳𝑰𝑪 Local consistency Build 𝓝𝒓𝒔𝒆𝒎(𝒊) 𝒙𝒊, sem(𝒊) 𝒇𝒊 LIC semantic radius graph Posed RGB images {𝐼𝑣} ...
- **p. 5 / 4.4. Visibility-Weighted Fr´echet Mean (VFM) - extractive body cue:** Instead, we enforce manifold consistency in the loss.
- **Contribution anchor:** p. 4 (4.3. Visibility-Calibrated Distillation (VCD)), p. 5 (4.4. Visibility-Weighted Fr´echet Mean (VFM)), p. 4 (4.3. Visibility-Calibrated Distillation (VCD)), p. 3 (4.1. Problem Formulation and Notation), p. 4 (4.2. Overview), p. 4 (4.1. Problem Formulation and Notation)

### Strongest assumption and failure boundary

- **p. 1 / 1. Introduction - extractive body cue:** (a) RGB(View-1) + zoom-in box (b) Baseline mask (View-1) (c) Baseline multi-view inconsistency (View-1 vs View-2) Problem: Boundary ambiguity & view inconsistency (d) VCD (f) ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overview of Rh-3DGS. Given posed RGB images, a frozen teacher (e.g., SAM/CLIP) provides per-pixel semantic embeddings. Learnable 3D Gaussians are optimized through a ...
- **p. 9 / 6. Conclusion - extractive body cue:** Future work will extend to dynamic scenes, multi-teacher distillation, and more efficient implementations.
- **p. 8 / 5.4. Ablation Study - extractive body cue:** 9, activating LIC from the beginning is less effective because pseudoinstances are unstable in the early stage.
- **p. 8 / 6. Conclusion - extractive body cue:** We present Rh-3DGS for robust open-vocabulary 3D semantics in 3D Gaussian Splatting.
- **p. 9 / 6. Conclusion - extractive body cue:** Rh-3DGS localizes semantic regions with clean boundaries under clutter and occlusion. sions and mixed-depth rays.
- **p. 7 / 5.2. Quantitative Results - extractive body cue:** Rh-3DGS gest that our semantic training does not hurt radiance-field reconstruction.
- **Boundary to test:** Figure 2. Overview of Rh-3DGS. Given posed RGB images, a frozen teacher (e.g., SAM/CLIP) provides per-pixel semantic embeddings. Learnable 3D Gaussians are optimized through a differentiable rasterizer, which outputs RGB renders, semant ...

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | We propose Visibility-Calibrated Distillation (VCD). | p. 4 (4.3. Visibility-Calibrated Distillation (VCD)), p. 5 (4.4. Visibility-Weighted Fr´echet Mean (VFM)) |
| Reported outcome | Rh-3DGS achieves the best results on both tables. | p. 6 (5.2. Quantitative Results), p. 7 (5.2. Quantitative Results) |
| Failure/limitation | Figure 2. Overview of Rh-3DGS. Given posed RGB images, a frozen teacher (e.g., SAM/CLIP) provides per-pixel semantic embeddings. Learnable 3D Gaussians are optimized through a differentiable rasterizer, which outputs RGB renders, semant ... | p. 4 (Figure/Table caption), p. 9 (6. Conclusion) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `RGB-D, image set, point cloud, depth와 camera pose → geometry, map, object/relationship state → point map, pose, scene graph, affordance 또는 query result`.
- 이 논문의 재사용 가능한 지점은 Rh-3DGS 𝒊 radius 𝜸 same semantic (in 𝓝) excluded 𝑳𝑳𝑰𝑪 Local consistency Build 𝓝𝒓𝒔𝒆𝒎(𝒊) 𝒙𝒊, sem(𝒊) 𝒇𝒊 LIC semantic radius graph Posed RGB images {𝐼𝑣} + cameras {𝑃𝑣} Inputs Frozen Teacher (SAM/CLIP) ...를 The rasterizer also outputs the accumulated opacity Av,u and depth moments D(1) v,u, D(2) v,u (with the same compositing weights).로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 geometry, map, object/relationship state가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 Figure 2. Overview of Rh-3DGS. Given posed RGB images, a frozen teacher (e.g., SAM/CLIP) provides per-pixel semantic embeddings. Learnable 3D Gaussians are optimized through a differentiable rasterizer, which outputs RGB renders, semant ...에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: We propose Visibility-Calibrated Distillation (VCD).
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `ARCHIVE` in `Robotics-enabling 3D perception`; tags: `semantic, alignment, 3D Vision`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** Figure 2. Overview of Rh-3DGS. Given posed RGB images, a frozen teacher (e.g., SAM/CLIP) provides per-pixel semantic embeddings. Learnable 3D Gaussians are optimized through a differentiable rasterizer, which outputs RGB renders, semant ...; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: We evaluate Rh-3DGS on three benchmarks: (i) LERF (Kerr et al., 2023), multi-view scenes with maskbased open-vocabulary queries; (ii) 3D-OVS (Liu et al., 2023), a standardized benchmark for open-vocabulary 3D segmentation; (iii) ....
3. Compare against the body-reported baseline or a matched simpler baseline: Compared with the strongest baseline, Rh-3DGS improves mIoU from 76.07 to 82.07 and mBIoU from 55.45 to 67.66..
4. Report the body metric and its denominator/aggregation: For ScanNet, we report mIoU and mAcc (mean per-class accuracy)..
5. Re-run the body-reported ablation/failure condition: Figure 8. Sensitivity to loss weights on LERF (figurines). We sweep λVFM and λLIC and report mIoU. The best region is around our default setting. D.3. Ablation on LIC Positive-pair Construction LIC ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 3 (4.1. Problem Formulation and Notation), p. 4 (4.2. Overview), p. 4 (4.1. Problem Formulation and Notation); the primary result is directionally consistent at p. 6 (5.2. Quantitative Results), p. 7 (5.2. Quantitative Results), p. 7 (5.2. Quantitative Results); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 Visibility-Calibrated, Distillation, VCD mechanism이 Compared with the strongest baseline, Rh-3DGS improves mIoU from 76.07 to 82.07 and mBIoU from 55.45 ... 대비 For ScanNet, we report mIoU and mAcc (mean per-class accuracy).을 개선하고, Figure 2. Overview of Rh-3DGS. Given posed RGB images, a frozen teacher (e.g., SAM/CLIP) provides per-pixel ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
