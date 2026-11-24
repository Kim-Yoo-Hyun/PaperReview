# Rh-3DGS: Robust Open-Vocabulary Scene Understanding via Riemannian Huber Distillation and Manifold-Aware Sampling

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://icml.cc/virtual/2026/poster/62937.
> PDF retrieval source: https://openreview.net/pdf/8310d4c5a6346eaadb420914138e1711121a0ff8.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: Xinpeng Zhao, Jie Jiang, Fengyuan Zhang, Lixin Zhan, Dong Wang, Qinyuan Bu, Jiahang Tu, Guangzhen Yao
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: semantic, alignment, 3D Vision
- Official paper: https://icml.cc/virtual/2026/poster/62937
- Published PDF: https://raw.githubusercontent.com/mlresearch/v306/main/assets/zhao26s/zhao26s.pdf
- Full-text retrieval at original review: https://openreview.net/pdf/8310d4c5a6346eaadb420914138e1711121a0ff8.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (27 pages; PyMuPDF text; title-token overlap first two pages=1.0)
- 요약 대조 판본: 2026-11-24 한 줄 요약과 핵심 기여 두 개를 게재본 해당 쪽과 대조했다. [본문](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhao26s/zhao26s.pdf)

## Why This Paper Is Here

Rh-3DGS는 관측 방향과 가시성에 따라 달라지는 시각언어 특징의 신뢰도를 고려해 가우시안 장면에 의미 정보를 증류한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhao26s/zhao26s.pdf#page=1) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhao26s/zhao26s.pdf#page=4)

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

- 단위구 위의 특징을 가시성으로 가중해 결합하고 리만 공간의 Huber 손실로 이상 관측의 영향을 줄인다. [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhao26s/zhao26s.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhao26s/zhao26s.pdf#page=5) · [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhao26s/zhao26s.pdf#page=6)
- 국소 의미 일관성을 함께 적용해 개방 어휘 분할과 경계 보존을 평가하고 신뢰도 처리의 효과를 비교했다. [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhao26s/zhao26s.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v306/acc326bcb01ce154c084938f42db80259d168431/assets/zhao26s/zhao26s.pdf#page=8)

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

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1. Introduction), p. 3 (4.1. Problem Formulation and Notation), p. 4 (4.2. Overview), p. 4 (4.1. Problem Formulation and Notation), p. 5 (4.4. Visibility-Weighted Fr´echet Mean (VFM)), p. 5 (4.3. Visibility-Calibrated Distillation (VCD))이다.
