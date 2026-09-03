# Rh-3DGS: Robust Open-Vocabulary Scene Understanding via Riemannian Huber Distillation and Manifold-Aware Sampling

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=bjtuHOb3vN.
> PDF retrieval source: https://openreview.net/pdf/8310d4c5a6346eaadb420914138e1711121a0ff8.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: semantic, alignment, 3D Vision
- Official paper: https://openreview.net/forum?id=bjtuHOb3vN
- Full-text retrieval: https://openreview.net/pdf/8310d4c5a6346eaadb420914138e1711121a0ff8.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 (a) RGB(View-1) + zoom-in box (b) Baseline mask (View-1) (c) Baseline multi-view inconsistency (View-1 vs View-2) Problem: Boundary ambiguity & view inconsistency (d) VCD (f) LIC (h) Our multi-view stable(View-1 vs View-2) ...를 문제로 두고, We propose Visibility-Calibrated Distillation (VCD).를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Open-vocabulary 3D scene understanding answers free-form text queries over reconstructed scenes.
- **p. 1 / Abstract - extractive body cue:** However, lifting dense 2D foundationmodel embeddings into 3D Gaussian Splatting (3DGS) is still challenging.
- **p. 1 / Abstract - extractive body cue:** Existing 3DGS-based methods often average normalized embeddings in Euclidean space.
- **p. 1 / Abstract - extractive body cue:** This ignores their hyperspherical geometry and can cause feature collapse.
- **p. 1 / Abstract - extractive body cue:** They also distill supervision from all views equally, which amplifies occlusion noise and mixed-depth artifacts.
- **p. 1 / 1. Introduction - extractive body cue:** (a) RGB(View-1) + zoom-in box (b) Baseline mask (View-1) (c) Baseline multi-view inconsistency (View-1 vs View-2) Problem: Boundary ambiguity & view inconsistency (d) VCD (f) ...

## Core Idea

- **p. 4 / 4.3. Visibility-Calibrated Distillation (VCD) - extractive body cue:** We propose Visibility-Calibrated Distillation (VCD).
- **p. 5 / 4.4. Visibility-Weighted Fr´echet Mean (VFM) - extractive body cue:** We propose Visibility-Weighted Fr´echet Mean (VFM).
- **p. 4 / 4.3. Visibility-Calibrated Distillation (VCD) - extractive body cue:** Low accumulated opacity often indicates weak or unstable contributions.
- **p. 3 / 4.1. Problem Formulation and Notation - extractive body cue:** Each Gaussian stores a lowdimensional semantic latent fi ∈Rd and a lightweight decoder maps it to the teacher feature space: hi = Dec(fi) ∈ RD.
- **p. 4 / 4.2. Overview - extractive body cue:** We optimize the model end-to-end: L = Lrgb + λsem LVFM + λcon LLIC, (4) where Lrgb is the photometric loss, LVFM is the reweighted ...
- **p. 4 / 4.1. Problem Formulation and Notation - extractive body cue:** Rh-3DGS 𝒊 radius 𝜸 same semantic (in 𝓝) excluded 𝑳𝑳𝑰𝑪 Local consistency Build 𝓝𝒓𝒔𝒆𝒎(𝒊) 𝒙𝒊, sem(𝒊) 𝒇𝒊 LIC semantic radius graph Posed RGB images {𝐼𝑣} ...
- **p. 5 / 4.4. Visibility-Weighted Fr´echet Mean (VFM) - extractive body cue:** Instead, we enforce manifold consistency in the loss.
- **p. 5 / 4.3. Visibility-Calibrated Distillation (VCD) - extractive body cue:** The model cannot reduce the loss by shrinking weights.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Rh-3DGS 𝒊 radius 𝜸 same semantic (in 𝓝) excluded 𝑳𝑳𝑰𝑪 Local consistency Build 𝓝𝒓𝒔𝒆𝒎(𝒊) 𝒙𝒊, sem(𝒊) 𝒇𝒊 LIC semantic radius graph Posed RGB images {𝐼𝑣} + cameras {𝑃𝑣} Inputs Frozen Teacher (SAM/CLIP) ... | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (4.1. Problem Formulation and Notation), p. 3 (4.1. Problem Formulation and Notation) |
| State/latent | Rh-3DGS, radius, same, semantic, excluded, Local, consistency, Build, LIC, graph, Posed, RGB | geometry, map, object/relationship state | p. 4 (4.1. Problem Formulation and Notation), p. 3 (4.1. Problem Formulation and Notation), p. 4 (4.3. Visibility-Calibrated Distillation (VCD)) |
| Output/action | The rasterizer also outputs the accumulated opacity Av,u and depth moments D(1) v,u, D(2) v,u (with the same compositing weights). | point map, pose, scene graph, affordance 또는 query result | p. 3 (4.1. Problem Formulation and Notation), p. 4 (4.3. Visibility-Calibrated Distillation (VCD)), p. 3 (4.1. Problem Formulation and Notation) |
| Objective/outcome | We optimize the model end-to-end: L = Lrgb + λsem LVFM + λcon LLIC, (4) where Lrgb is the photometric loss, LVFM is the reweighted semantic distillation loss, and LLIC regularizes local ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (4.2. Overview), p. 4 (4.1. Problem Formulation and Notation), p. 3 (4.1. Problem Formulation and Notation) |

## Main Claims and Actual Contribution

- **p. 4 / 4.3. Visibility-Calibrated Distillation (VCD) - extractive body cue:** We propose Visibility-Calibrated Distillation (VCD).
- **p. 5 / 4.4. Visibility-Weighted Fr´echet Mean (VFM) - extractive body cue:** We propose Visibility-Weighted Fr´echet Mean (VFM).
- **p. 4 / 4.3. Visibility-Calibrated Distillation (VCD) - extractive body cue:** Low accumulated opacity often indicates weak or unstable contributions.
- **p. 6 / 5.2. Quantitative Results - extractive body cue:** Rh-3DGS achieves the best results on both tables.
- **p. 7 / 5.2. Quantitative Results - extractive body cue:** Rh-3DGS again achieves the best performance.
- **p. 7 / 5.2. Quantitative Results - extractive body cue:** Rh-3DGS achieves the best results across all splits.
- **p. 8 / 5.4. Ablation Study - extractive body cue:** The full model (VCD+VFM+LIC) achieves the best performance (81.62 mIoU, 58.11 mBIoU).
- **p. 6 / 5.2. Quantitative Results - extractive body cue:** We also observe consistent improvements in rendering metrics.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (5.2. Quantitative Results), p. 7 (5.2. Quantitative Results) |
| Embodiment/environment | We evaluate Rh-3DGS on three benchmarks: (i) LERF (Kerr et al., 2023), multi-view scenes with maskbased open-vocabulary queries; (ii) 3D-OVS (Liu et al., 2023), a standardized benchmark for open-vocabulary 3D segmentation; (iii) ... | hardware/simulator version and reset protocol | p. 6 (5.1. Experimental Setup), p. 6 (5. Experiments) |
| Dataset/benchmark | Quantitative mIoU(%) and mBIoU(%) results on the LERF dataset. | role, split, size and leakage | p. 6 (5.1. Experimental Setup), p. 6 (5. Experiments), p. 7 (5.2. Quantitative Results), p. 7 (5.2. Quantitative Results) |
| Metric | For ScanNet, we report mIoU and mAcc (mean per-class accuracy). | definition, denominator, direction and uncertainty | p. 6 (5.1. Experimental Setup), p. 6 (5.1. Experimental Setup), p. 9 (Figure/Table caption) |
| Baseline/ablation | Compared with the strongest baseline, Rh-3DGS improves mIoU from 76.07 to 82.07 and mBIoU from 55.45 to 67.66. | fair input/data/compute/action matching | p. 6 (5.2. Quantitative Results), p. 8 (5.4. Ablation Study), p. 6 (5. Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overview of Rh-3DGS. Given posed RGB images, a frozen teacher (e.g., SAM/CLIP) provides per-pixel semantic embeddings. Learnable 3D Gaussians are optimized through a ...
- **p. 9 / 6. Conclusion - extractive body cue:** Future work will extend to dynamic scenes, multi-teacher distillation, and more efficient implementations.
- **p. 8 / 5.4. Ablation Study - extractive body cue:** 9, activating LIC from the beginning is less effective because pseudoinstances are unstable in the early stage.
- **p. 8 / 6. Conclusion - extractive body cue:** We present Rh-3DGS for robust open-vocabulary 3D semantics in 3D Gaussian Splatting.
- **p. 9 / 6. Conclusion - extractive body cue:** Rh-3DGS localizes semantic regions with clean boundaries under clutter and occlusion. sions and mixed-depth rays.
- **p. 7 / 5.2. Quantitative Results - extractive body cue:** Rh-3DGS gest that our semantic training does not hurt radiance-field reconstruction.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Motivation on LERF (teatime, "bag of cookies"). Baseline 3DGS produces boundary bleeding and multi-view in- consistent masks under occlusion and mixed-depth rays (b-c). ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 (a) RGB(View-1) + zoom-in box (b) Baseline mask (View-1) (c) Baseline multi-view inconsistency (View-1 vs View-2) Problem: Boundary ambiguity & view inconsistency (d) VCD (f) LIC (h) Our multi-view stable(View-1 vs View-2) ...를 문제로 두고, We propose Visibility-Calibrated Distillation (VCD).를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 3 (4.1. Problem Formulation and Notation), p. 4 (4.2. Overview), p. 4 (4.1. Problem Formulation and Notation), p. 5 (4.4. Visibility-Weighted Fr´echet Mean (VFM)), p. 5 (4.3. Visibility-Calibrated Distillation (VCD)) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
