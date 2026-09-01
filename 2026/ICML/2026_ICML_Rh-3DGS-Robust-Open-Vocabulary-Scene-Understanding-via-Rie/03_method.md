# Method - Rh-3DGS: Robust Open-Vocabulary Scene Understanding via Riemannian Huber Distillation and Manifold-Aware Sampling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=bjtuHOb3vN; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/331577. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 3 (4.1. Problem Formulation and Notation), p. 4 (4.2. Overview), p. 4 (4.1. Problem Formulation and Notation), p. 5 (4.4. Visibility-Weighted Fr´echet Mean (VFM)), p. 5 (4.3. Visibility-Calibrated Distillation (VCD)), p. 3 (4.1. Problem Formulation and Notation)): Each Gaussian stores a lowdimensional semantic latent fi ∈Rd and a lightweight decoder maps it to the teacher feature space: hi = Dec(fi) ∈ RD.

## Method Body Digest

- **p. 3 / 4.1. Problem Formulation and Notation - extractive PDF cue:** Each Gaussian stores a lowdimensional semantic latent fi ∈Rd and a lightweight decoder maps it to the teacher feature space: hi = Dec(fi) ∈ RD.
- **p. 4 / 4.2. Overview - extractive PDF cue:** We optimize the model end-to-end: L = Lrgb + λsem LVFM + λcon LLIC, (4) where Lrgb is the photometric loss, LVFM is the reweighted ...
- **p. 4 / 4.1. Problem Formulation and Notation - extractive PDF cue:** Rh-3DGS 𝒊 radius 𝜸 same semantic (in 𝓝) excluded 𝑳𝑳𝑰𝑪 Local consistency Build 𝓝𝒓𝒔𝒆𝒎(𝒊) 𝒙𝒊, sem(𝒊) 𝒇𝒊 LIC semantic radius graph Posed RGB images {𝐼𝑣} ...
- **p. 5 / 4.4. Visibility-Weighted Fr´echet Mean (VFM) - extractive PDF cue:** Instead, we enforce manifold consistency in the loss.
- **p. 5 / 4.3. Visibility-Calibrated Distillation (VCD) - extractive PDF cue:** The model cannot reduce the loss by shrinking weights.
- **p. 3 / 4.1. Problem Formulation and Notation - extractive PDF cue:** We apply ℓ2 normalization to teacher/rendered pixel embeddings before computing hyperspherical (geodesic) losses.
- **p. 6 / 4.4. Visibility-Weighted Fr´echet Mean (VFM) - extractive PDF cue:** (20) We can anneal δ during training.
- **p. 3 / 4.1. Problem Formulation and Notation - extractive PDF cue:** Implementation note: we keep the rasterizer unchanged; hyperspherical geometry is used only in the distillation objective.

## Design Rationale

- **p. 4 / 4.3. Visibility-Calibrated Distillation (VCD) - extractive PDF cue:** We propose Visibility-Calibrated Distillation (VCD).
- **p. 5 / 4.4. Visibility-Weighted Fr´echet Mean (VFM) - extractive PDF cue:** We propose Visibility-Weighted Fr´echet Mean (VFM).
- **p. 4 / 4.3. Visibility-Calibrated Distillation (VCD) - extractive PDF cue:** Low accumulated opacity often indicates weak or unstable contributions.

## Source Evidence Cues

- **p. 3 / 4.1. Problem Formulation and Notation - extractive PDF cue:** Each Gaussian stores a lowdimensional semantic latent fi ∈Rd and a lightweight decoder maps it to the teacher feature space: hi = Dec(fi) ∈ RD.
- **p. 4 / 4.2. Overview - extractive PDF cue:** We optimize the model end-to-end: L = Lrgb + λsem LVFM + λcon LLIC, (4) where Lrgb is the photometric loss, LVFM is the reweighted ...
- **p. 4 / 4.1. Problem Formulation and Notation - extractive PDF cue:** Rh-3DGS 𝒊 radius 𝜸 same semantic (in 𝓝) excluded 𝑳𝑳𝑰𝑪 Local consistency Build 𝓝𝒓𝒔𝒆𝒎(𝒊) 𝒙𝒊, sem(𝒊) 𝒇𝒊 LIC semantic radius graph Posed RGB images {𝐼𝑣} ...
- **p. 5 / 4.4. Visibility-Weighted Fr´echet Mean (VFM) - extractive PDF cue:** Instead, we enforce manifold consistency in the loss.
- **p. 5 / 4.3. Visibility-Calibrated Distillation (VCD) - extractive PDF cue:** The model cannot reduce the loss by shrinking weights.
- **p. 3 / 4.1. Problem Formulation and Notation - extractive PDF cue:** We apply ℓ2 normalization to teacher/rendered pixel embeddings before computing hyperspherical (geodesic) losses.
- **p. 6 / 4.4. Visibility-Weighted Fr´echet Mean (VFM) - extractive PDF cue:** (20) We can anneal δ during training.
- **Detected method headings:** 4. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Each Gaussian stores a lowdimensional semantic latent fi ∈Rd and a lightweight decoder maps it to the teacher feature space: hi = ... | p. 3 (4.1. Problem Formulation and Notation), p. 4 (4.2. Overview) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | We optimize the model end-to-end: L = Lrgb + λsem LVFM + λcon LLIC, (4) where Lrgb is the photometric loss, LVFM ... | p. 4 (4.2. Overview), p. 4 (4.1. Problem Formulation and Notation) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Rh-3DGS 𝒊 radius 𝜸 same semantic (in 𝓝) excluded 𝑳𝑳𝑰𝑪 Local consistency Build 𝓝𝒓𝒔𝒆𝒎(𝒊) 𝒙𝒊, sem(𝒊) 𝒇𝒊 LIC semantic radius graph Posed ... | p. 4 (4.1. Problem Formulation and Notation), p. 5 (4.4. Visibility-Weighted Fr´echet Mean (VFM)) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 4.2. Overview - extractive PDF cue:** We optimize the model end-to-end: L = Lrgb + λsem LVFM + λcon LLIC, (4) where Lrgb is the photometric loss, LVFM is the reweighted ...
- **p. 4 / 4.1. Problem Formulation and Notation - extractive PDF cue:** Rh-3DGS 𝒊 radius 𝜸 same semantic (in 𝓝) excluded 𝑳𝑳𝑰𝑪 Local consistency Build 𝓝𝒓𝒔𝒆𝒎(𝒊) 𝒙𝒊, sem(𝒊) 𝒇𝒊 LIC semantic radius graph Posed RGB images {𝐼𝑣} ...
- **p. 3 / 4.1. Problem Formulation and Notation - extractive PDF cue:** We apply ℓ2 normalization to teacher/rendered pixel embeddings before computing hyperspherical (geodesic) losses.
- **p. 3 / 4.1. Problem Formulation and Notation - extractive PDF cue:** Implementation note: we keep the rasterizer unchanged; hyperspherical geometry is used only in the distillation objective.
- **p. 5 / 4.4. Visibility-Weighted Fr´echet Mean (VFM) - extractive PDF cue:** (16) Robust pixel-wise geodesic objective.
- **p. 5 / 4.4. Visibility-Weighted Fr´echet Mean (VFM) - extractive PDF cue:** This adds cost and hurts real-time rendering.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (4.1. Problem Formulation and Notation), p. 3 (4.1. Problem Formulation and Notation), p. 3 (4.1. Problem Formulation and Notation), p. 4 (4.3. Visibility-Calibrated Distillation (VCD)), p. 5 (4.4. Visibility-Weighted Fr´echet Mean (VFM)), p. 5 (4.3. Visibility-Calibrated Distillation (VCD)).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Rh-3DGS, radius, same, semantic, excluded, Local, consistency, Build, LIC, graph, Posed, RGB, images, cameras | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Rh-3DGS, radius, same, semantic, excluded, Local, consistency, Build, LIC, graph | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | Visibility-Calibrated, Distillation, VCD, Visibility-Weighted, echet, Mean, VFM, Low, accumulated, opacity | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | optimize, model, end-to-end, Lrgb, LVFM, LLIC, where, photometric, loss, reweighted | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 4.1. Problem Formulation and Notation - extractive PDF cue:** Rh-3DGS 𝒊 radius 𝜸 same semantic (in 𝓝) excluded 𝑳𝑳𝑰𝑪 Local consistency Build 𝓝𝒓𝒔𝒆𝒎(𝒊) 𝒙𝒊, sem(𝒊) 𝒇𝒊 LIC semantic radius graph Posed RGB images {𝐼𝑣} ...
- **p. 3 / 4.1. Problem Formulation and Notation - extractive PDF cue:** The rasterizer also outputs the accumulated opacity Av,u and depth moments D(1) v,u, D(2) v,u (with the same compositing weights).
- **p. 4 / 4.3. Visibility-Calibrated Distillation (VCD) - extractive PDF cue:** It outputs a per-pixel weight map and reweights semantic supervision.
- **p. 3 / 4.1. Problem Formulation and Notation - extractive PDF cue:** We compute the expected depth ¯Dv,u = D(1) v,u Av,u+ϵ and ray variance Varv,u =  D(2) v,u Av,u+ϵ -¯D2 v,u  +, used by ...
- **p. 5 / 4.4. Visibility-Weighted Fr´echet Mean (VFM) - extractive PDF cue:** VCD down-weights mixed-depth and occlusion pixels.
- **p. 5 / 4.4. Visibility-Weighted Fr´echet Mean (VFM) - extractive PDF cue:** We propose Visibility-Weighted Fr´echet Mean (VFM).
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | 6, the full model runs at 301.64 FPS with 3.23 GB peak memory. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Compared to the baseline (328.59 FPS, 2.65 GB), all components add only 8.2% FPS drop and 0.58 GB memory, while improving mIoU ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | 6, the full model runs at 301.64 FPS with 3.23 GB peak memory. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | 6, the full model runs at 301.64 FPS with 3.23 GB peak memory. | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 4.4. Visibility-Weighted Fr´echet Mean (VFM) - extractive PDF cue:** (20) We can anneal δ during training.
- **p. 6 / 5.1. Experimental Setup - extractive PDF cue:** We implement all methods in PyTorch and train on a single NVIDIA GeForce RTX 4090 GPU.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Gaussian, stores, lowdimensional, semantic, latent, lightweight, decoder, maps, teacher, feature, space, Dec, optimize, model, end-to-end, Lrgb, LVFM, LLIC, where, photometric.
- **Relevant PDF headings:** 4. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We evaluate Rh-3DGS on three benchmarks: (i) LERF (Kerr et al., 2023), multi-view scenes with maskbased open-vocabulary queries; (ii) 3D-OVS (Liu et ... | p. 6 (5.1. Experimental Setup), p. 6 (5. Experiments) |
| Semantic / temporal fusion | Compared with the strongest baseline, Rh-3DGS improves mIoU from 76.07 to 82.07 and mBIoU from 55.45 to 67.66. | p. 6 (5.2. Quantitative Results), p. 8 (5.4. Ablation Study) |
| Robot query / planning handoff | Rh-3DGS achieves the best results on both tables. | p. 6 (5.2. Quantitative Results), p. 7 (5.2. Quantitative Results) |

## Failure and Ablation Link

- **p. 24 / Figure/Table caption - extractive PDF cue:** Figure 8. Sensitivity to loss weights on LERF (figurines). We sweep λVFM and λLIC and report mIoU. The best region is around our default setting. ...
- **p. 22 / Figure/Table caption - extractive PDF cue:** Figure 7. Scene editing with the learned 3D semantic field. We show the original renderings, the localized semantic region, and the edited renderings from multiple ...
- **p. 6 / 5. Experiments - extractive PDF cue:** Finally, we conduct ablation studies to analyze the impact of each component.
- **p. 8 / 5.4. Ablation Study - extractive PDF cue:** All variants use the same training schedule, teacher, resolution, and evaluation protocol.
- **p. 24 / Figure/Table caption - extractive PDF cue:** Table 10. Ablation of VCD weight components on LERF (figurines). Wop Wedge Wvar mIoU ↑ ✓ ✓ ✓
- **p. 8 / 5.4. Ablation Study - extractive PDF cue:** We ablate each component on LERF (figurines).
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of Rh-3DGS. Given posed RGB images, a frozen teacher (e.g., SAM/CLIP) provides per-pixel semantic embeddings. Learnable 3D Gaussians are optimized through a ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 3 (4.1. Problem Formulation and Notation), p. 4 (4.2. Overview), p. 4 (4.1. Problem Formulation and Notation), p. 5 (4.4. Visibility-Weighted Fr´echet Mean (VFM)), p. 5 (4.3. Visibility-Calibrated Distillation (VCD)), p. 3 (4.1. Problem Formulation and Notation), objective p. 4 (4.2. Overview), p. 4 (4.1. Problem Formulation and Notation), p. 3 (4.1. Problem Formulation and Notation), p. 3 (4.1. Problem Formulation and Notation), p. 5 (4.4. Visibility-Weighted Fr´echet Mean (VFM)), p. 5 (4.4. Visibility-Weighted Fr´echet Mean (VFM)), temporal p. 8 (5.4. Ablation Study), p. 8 (5.4. Ablation Study), p. 5 (4.4. Visibility-Weighted Fr´echet Mean (VFM)), p. 6 (4.5. Lightweight Consistency Contrast (LIC)), p. 1 (1. Introduction), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
