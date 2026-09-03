# Method - DualSplat: Robust 3D Gaussian Splatting via Pseudo-Mask Bootstrapping from Reconstruction Failures

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Wang_DualSplat_Robust_3D_Gaussian_Splatting_via_Pseudo-Mask_Bootstrapping_from_Reconstruction_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_DualSplat_Robust_3D_Gaussian_Splatting_via_Pseudo-Mask_Bootstrapping_from_Reconstruction_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 5 (3.4. Reconstruction Failures to Object-Level Priors), p. 4 (3.2. Overview), p. 5 (3.4. Reconstruction Failures to Object-Level Priors), p. 4 (3.2. Overview), p. 3 (3.2. Overview), p. 3 (3.2. Overview)): We use DINOv2 [17] as the feature extraction backbone.

## Method Body Digest

- **p. 5 / 3.4. Reconstruction Failures to Object-Level Priors - extractive body cue:** We use DINOv2 [17] as the feature extraction backbone.
- **p. 4 / 3.2. Overview - extractive body cue:** FiT3D ❄ FiT3D ❄ Training images Render images Cosine Similarity Threshold Filtering Pseudo-Masks Similarity images MLP stop grad Input Process Training images Render images Grad ...
- **p. 5 / 3.4. Reconstruction Failures to Object-Level Priors - extractive body cue:** (14) Concretely, fi is the cached feature of the ground-truth training view, and f ′ i is computed from the current rendering during optimization.
- **p. 4 / 3.2. Overview - extractive body cue:** After the first training, Mask Filter produces confidence-weighted pseudo-masks.
- **p. 3 / 3.2. Overview - extractive body cue:** We begin by training an initial 3DGS model and comparing each rendered image with its ground-truth training view.
- **p. 3 / 3.2. Overview - extractive body cue:** However, while such artifacts are human-discernible, some of them can be challenging for deep neural networks to identify.
- **p. 3 / 3.1. Preliminaries - extractive body cue:** The Gaussian parameters are optimized by minimizing the photometric reconstruction loss between the rendered image and its reference image: L = (1 -λD-SSIM) L1 + ...
- **p. 3 / 3.1. Preliminaries - extractive body cue:** For handling transients, a common practice is to estimate a per-pixel binary mask M and suppress transient regions during loss computation: Lmasked = (1-λD-SSIM) M⊙L1+λD-SSIM ...

## Design Rationale

- **p. 3 / 3.2. Overview - extractive body cue:** Our method is built on a Failure-to-Prior principle: reconstruction failures caused by view-inconsistent transients are not merely artifacts to suppress, but signals that can be ...
- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are as follows:
- **p. 2 / 1. Introduction - extractive body cue:** We address this problem by introducing a novel Failureto-Prior paradigm.

## Source Evidence Cues

- **p. 5 / 3.4. Reconstruction Failures to Object-Level Priors - extractive body cue:** We use DINOv2 [17] as the feature extraction backbone.
- **p. 4 / 3.2. Overview - extractive body cue:** FiT3D ❄ FiT3D ❄ Training images Render images Cosine Similarity Threshold Filtering Pseudo-Masks Similarity images MLP stop grad Input Process Training images Render images Grad ...
- **p. 5 / 3.4. Reconstruction Failures to Object-Level Priors - extractive body cue:** (14) Concretely, fi is the cached feature of the ground-truth training view, and f ′ i is computed from the current rendering during optimization.
- **p. 4 / 3.2. Overview - extractive body cue:** After the first training, Mask Filter produces confidence-weighted pseudo-masks.
- **p. 3 / 3.2. Overview - extractive body cue:** We begin by training an initial 3DGS model and comparing each rendered image with its ground-truth training view.
- **p. 3 / 3.2. Overview - extractive body cue:** However, while such artifacts are human-discernible, some of them can be challenging for deep neural networks to identify.
- **Detected method headings:** 2.3. Pretrained Models (p. 3); 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | We use DINOv2 [17] as the feature extraction backbone. | p. 5 (3.4. Reconstruction Failures to Object-Level Priors), p. 4 (3.2. Overview) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | FiT3D ❄ FiT3D ❄ Training images Render images Cosine Similarity Threshold Filtering Pseudo-Masks Similarity images MLP stop grad Input Process Training images ... | p. 4 (3.2. Overview), p. 5 (3.4. Reconstruction Failures to Object-Level Priors) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | (14) Concretely, fi is the cached feature of the ground-truth training view, and f ′ i is computed from the current rendering ... | p. 5 (3.4. Reconstruction Failures to Object-Level Priors), p. 4 (3.2. Overview) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.1. Preliminaries - extractive body cue:** The Gaussian parameters are optimized by minimizing the photometric reconstruction loss between the rendered image and its reference image: L = (1 -λD-SSIM) L1 + ...
- **p. 3 / 3.1. Preliminaries - extractive body cue:** For handling transients, a common practice is to estimate a per-pixel binary mask M and suppress transient regions during loss computation: Lmasked = (1-λD-SSIM) M⊙L1+λD-SSIM ...
- **p. 4 / 3.2. Overview - extractive body cue:** (6) The resulting mask Mt is then applied in the masked reconstruction loss of Eq.
- **p. 4 / 3.4. Reconstruction Failures to Object-Level Priors - extractive body cue:** The primary objective of this step is to translate these firstpass failures into reliable object-level priors for the second reconstruction stage, rather than directly outputting ...
- **p. 5 / 3.4. Reconstruction Failures to Object-Level Priors - extractive body cue:** (15) The final MLP objective is LMLP = λrobustLrobust + λpriorLprior + Lreg.
- **p. 5 / 3.4. Reconstruction Failures to Object-Level Priors - extractive body cue:** These loss functions are combined as: Lrobust = exp  -max(0, Tdensify -t) βrobustness  (Lcos + Lres) .
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.4. Reconstruction Failures to Object-Level Priors), p. 3 (3.1. Preliminaries), p. 3 (3.1. Preliminaries), p. 4 (3.2. Overview), p. 4 (3.4. Reconstruction Failures to Object-Level Priors), p. 5 (3.4. Reconstruction Failures to Object-Level Priors).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | FiT3D, Training, images, Render, Cosine, Similarity, Threshold, Filtering, Pseudo-Masks, MLP, stop, grad, Input, Process | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | FiT3D, Training, images, Render, Cosine, Similarity, Threshold, Filtering, Pseudo-Masks, MLP | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | built, Failure-to-Prior, principle, reconstruction, failures, caused, view-inconsistent, transients, merely, artifacts | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Gaussian, parameters, optimized, minimizing, photometric, reconstruction, loss, between, rendered, image | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 3.2. Overview - extractive body cue:** FiT3D ❄ FiT3D ❄ Training images Render images Cosine Similarity Threshold Filtering Pseudo-Masks Similarity images MLP stop grad Input Process Training images Render images Grad ...
- **p. 5 / 3.4. Reconstruction Failures to Object-Level Priors - extractive body cue:** We therefore introduce a lightweight per-pixel MLP that predicts a transient probability map online during the second reconstruction: Mi = MLPmask(fi, di), (10) where fi ...
- **p. 2 / 1. Introduction - extractive body cue:** This coupling creates a fundamental circular dependency: accurate transient detection requires a wellreconstructed static scene to expose mismatches, yet clean reconstruction itself depends on reliable ...
- **p. 4 / 3.2. Overview - extractive body cue:** DualSplat performs two-stage 3D Gaussian Splatting to suppress transient distractions.
- **p. 5 / 3.4. Reconstruction Failures to Object-Level Priors - extractive body cue:** We use DINOv2 [17] as the feature extraction backbone.
- **p. 1 / 1. Introduction - extractive body cue:** Its success, however, relies on a basic assumption: all training views should depict a static scene under mutually consistent observations.
- **p. 1 / 1. Introduction - extractive body cue:** When this assumption is violated, 3DGS mistakenly absorbs these view-inconsistent observations into the scene representation by spawning spurious Gaussians, leading to ghosting artifacts and degraded ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | framework with lightweight online mask refinement, where supervision gradually shifts from pseudo-mask priors to self-consistency as geometry stabilizes. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | 1 with online suppression, our key difference is not the type of residual or feature cues, but when and how these cues ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.2. Overview - extractive body cue:** FiT3D ❄ FiT3D ❄ Training images Render images Cosine Similarity Threshold Filtering Pseudo-Masks Similarity images MLP stop grad Input Process Training images Render images Grad ...
- **p. 5 / 3.4. Reconstruction Failures to Object-Level Priors - extractive body cue:** (14) Concretely, fi is the cached feature of the ground-truth training view, and f ′ i is computed from the current rendering during optimization.
- **p. 4 / 3.2. Overview - extractive body cue:** After the first training, Mask Filter produces confidence-weighted pseudo-masks.
- **p. 3 / 3.2. Overview - extractive body cue:** We begin by training an initial 3DGS model and comparing each rendered image with its ground-truth training view.
- **p. 6 / 4.1. Setups - extractive body cue:** We inherit RobustSplat's progressive MLP training schedule and other hyperparameters in Stage II unless otherwise stated.
- **p. 5 / 3.4. Reconstruction Failures to Object-Level Priors - extractive body cue:** (14) Concretely, fi is the cached feature of the ground-truth training view, and f ′ i is computed from the current rendering during optimization.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** DINOv2, feature, extraction, backbone, FiT3D, Training, images, Render, Cosine, Similarity, Threshold, Filtering, Pseudo-Masks, MLP, stop, grad, Input, Process, flow, Local.
- **Relevant PDF headings:** 2.3. Pretrained Models (p. 3); 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | These datasets contain diverse outdoor scenes with varying transient densities, enabling a comprehensive assessment of robustness and reconstruction quality. | p. 5 (4.1. Setups), p. 7 (4.2. Distractor-free 3D Reconstruction) |
| Semantic / temporal fusion | 4.2, we compare our method against 3DGSbased baselines using both quantitative metrics and qualitative visualizations. | p. 5 (4.1. Setups), p. 6 (4.2. Distractor-free 3D Reconstruction) |
| Robot query / planning handoff | DualSplat achieves the best overall average performance. | p. 6 (4.2. Distractor-free 3D Reconstruction), p. 1 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 6 / 4.1. Setups - extractive body cue:** We additionally include a 3DGS [8] variant that directly applies the pseudo-masks without any additional refinement.
- **p. 5 / 4.1. Setups - extractive body cue:** 4.3 presents ablation studies to validate the contribution of each core component in handling occlusions and improving overall reconstruction quality.
- **p. 7 / 4.3. Ablation Study - extractive body cue:** We further decompose DualSplat into three main components and perform controlled ablations: (i) Delayed Densification (DD) for 3DGS; (ii) pseudo-mask application (PM), which directly applies ...
- **p. 7 / 4.3. Ablation Study - extractive body cue:** All ablations are retrained from the same initialization and schedule to ensure fair comparison.
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Visualization results using different pretrained mod- els as feature extractors. FiT3D, when used as the feature extrac- tor, produces the most distinct feature ...
- **p. 2 / 1. We propose a Failure-to-Prior paradigm for transient - extractive body cue:** robust 3DGS that breaks the circular dependency between transient detection and scene reconstruction by converting first-pass reconstruction failures into explicit priors.
- **p. 4 / 3.4. Reconstruction Failures to Object-Level Priors - extractive body cue:** The primary objective of this step is to translate these firstpass failures into reliable object-level priors for the second reconstruction stage, rather than directly outputting ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 5 (3.4. Reconstruction Failures to Object-Level Priors), p. 4 (3.2. Overview), p. 5 (3.4. Reconstruction Failures to Object-Level Priors), p. 4 (3.2. Overview), p. 3 (3.2. Overview), p. 3 (3.2. Overview), objective p. 3 (3.1. Preliminaries), p. 3 (3.1. Preliminaries), p. 4 (3.2. Overview), p. 4 (3.4. Reconstruction Failures to Object-Level Priors), p. 5 (3.4. Reconstruction Failures to Object-Level Priors), p. 5 (3.4. Reconstruction Failures to Object-Level Priors), temporal p. 2 (3. We develop a prior-guided second-stage reconstruction), p. 3 (3.2. Overview), p. 3 (3.2. Overview), p. 4 (3.2. Overview), p. 4 (3.4. Reconstruction Failures to Object-Level Priors), p. 5 (3.4. Reconstruction Failures to Object-Level Priors).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
