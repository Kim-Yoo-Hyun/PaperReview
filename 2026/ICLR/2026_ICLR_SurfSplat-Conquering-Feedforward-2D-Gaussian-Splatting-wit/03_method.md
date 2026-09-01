# Method - SurfSplat: Conquering Feedforward 2D Gaussian Splatting with Surface Continuity Priors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=o1sF4XaFdY; PDF retrieval source: https://openreview.net/pdf/2b748f586856383d970839527439157443d1cc87.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES), p. 15 (A.1 ENCODER ARCHITECTURE), p. 5 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES), p. 15 (A.1 ENCODER ARCHITECTURE)): In the multi-view branch, input images are first converted into low-resolution feature maps, which are then processed by multiple layers of self- and cross-attention Vaswani et al.

## Method Body Digest

- **p. 4 / 3.1 PRELIMINARIES - extractive PDF cue:** In the multi-view branch, input images are first converted into low-resolution feature maps, which are then processed by multiple layers of self- and cross-attention Vaswani ...
- **p. 4 / 3.1 PRELIMINARIES - extractive PDF cue:** To integrate these complementary sources effectively, we adopt a dual-path for feature extraction within our model architecture.
- **p. 15 / A.1 ENCODER ARCHITECTURE - extractive PDF cue:** This module outputs multi-view-aware features  F i N i=1, where F i ∈R H s × W s ×C.
- **p. 5 / 3.1 PRELIMINARIES - extractive PDF cue:** To address these issues, we start by an observation: most visible geometry in real-world scenes consists of smooth, continuous surfaces.
- **p. 6 / 3.1 PRELIMINARIES - extractive PDF cue:** To address this, we propose a forced alpha blending strategy that explicitly constrains each Gaussian's opacity.
- **p. 15 / A.1 ENCODER ARCHITECTURE - extractive PDF cue:** We adopt a dual-branch encoder design to extract both monocular and multi-view features for robust 3D reasoning, following the architecture proposed by DepthSplat Xu et ...
- **p. 6 / 3.1 PRELIMINARIES - extractive PDF cue:** Published as a conference paper at ICLR 2026 We then use the neural network to predict scale multipliers ˆσu, ˆσv, which are constrained to lie ...
- **p. 4 / 3.1 PRELIMINARIES - extractive PDF cue:** The fused features are subsequently used to construct cost volumes Chen et al.

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** In summary, the main contributions of this work are as follows: • We propose SurfSplat, a feedforward network that reconstructs 3D scenes using 2D Gaussian ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Our model leverages a surface continuity prior and forced alpha blending to significantly improve reconstruction quality. • We introduce HRRC, a high-resolution rendering-based metric that ...
- **p. 6 / 3.1 PRELIMINARIES - extractive PDF cue:** 3.6 HIGH-RESOLUTION RENDERING CONSISTENCY (HRRC) To better evaluate the geometric fidelity of reconstructed 3D scenes, we propose a novel evaluation metric: High-Resolution Rendering Consistency (HRRC).

## Source Evidence Cues

- **p. 4 / 3.1 PRELIMINARIES - extractive PDF cue:** In the multi-view branch, input images are first converted into low-resolution feature maps, which are then processed by multiple layers of self- and cross-attention Vaswani ...
- **p. 4 / 3.1 PRELIMINARIES - extractive PDF cue:** To integrate these complementary sources effectively, we adopt a dual-path for feature extraction within our model architecture.
- **p. 15 / A.1 ENCODER ARCHITECTURE - extractive PDF cue:** This module outputs multi-view-aware features  F i N i=1, where F i ∈R H s × W s ×C.
- **p. 5 / 3.1 PRELIMINARIES - extractive PDF cue:** To address these issues, we start by an observation: most visible geometry in real-world scenes consists of smooth, continuous surfaces.
- **p. 6 / 3.1 PRELIMINARIES - extractive PDF cue:** To address this, we propose a forced alpha blending strategy that explicitly constrains each Gaussian's opacity.
- **p. 15 / A.1 ENCODER ARCHITECTURE - extractive PDF cue:** We adopt a dual-branch encoder design to extract both monocular and multi-view features for robust 3D reasoning, following the architecture proposed by DepthSplat Xu et ...
- **p. 6 / 3.1 PRELIMINARIES - extractive PDF cue:** Published as a conference paper at ICLR 2026 We then use the neural network to predict scale multipliers ˆσu, ˆσv, which are constrained to lie ...
- **Detected method headings:** 3 METHOD (p. 4); A.1 ENCODER ARCHITECTURE (p. 15)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | In the multi-view branch, input images are first converted into low-resolution feature maps, which are then processed by multiple layers of self- ... | p. 4 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To integrate these complementary sources effectively, we adopt a dual-path for feature extraction within our model architecture. | p. 4 (3.1 PRELIMINARIES), p. 15 (A.1 ENCODER ARCHITECTURE) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | This module outputs multi-view-aware features  F i N i=1, where F i ∈R H s × W s ×C. | p. 15 (A.1 ENCODER ARCHITECTURE), p. 5 (3.1 PRELIMINARIES) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 3.1 PRELIMINARIES - extractive PDF cue:** The fused features are subsequently used to construct cost volumes Chen et al.
- **p. 4 / 3.1 PRELIMINARIES - extractive PDF cue:** When combined with the camera intrinsics, these features can be projected into 3D space and assigned accurate Gaussian attributes, enabling end-to-end training via differentiable rasterization ...
- **p. 5 / 3.1 PRELIMINARIES - extractive PDF cue:** Published as a conference paper at ICLR 2026 when trained solely through gradient-based supervision.
- **p. 6 / 3.1 PRELIMINARIES - extractive PDF cue:** 3.5 TRAINING LOSS Our training loss is an image-level loss computed directly between the rendered image and the ground-truth image.
- **p. 6 / 3.1 PRELIMINARIES - extractive PDF cue:** (9) With this design, instead of directly regressing Gaussian attributes, our method derives them from predicted 3D positions, guided by a physically grounded constraint to ...
- **p. 15 / A.1 ENCODER ARCHITECTURE - extractive PDF cue:** These warped volumes are compared to Fi via dot-product similarity to construct a cost volume Ci ∈R H s × W s ×D.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (3.1 PRELIMINARIES), p. 5 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES), p. 5 (3.1 PRELIMINARIES).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | behavior, rapidly, boosts, image, quality, near-input, viewpoints, under, alpha-blending, rendering, rule, occluded, Gaussians, contribute | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | behavior, rapidly, boosts, image, quality, near-input, viewpoints, under, alpha-blending, rendering | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summary, main, contributions, follows, SurfSplat, feedforward, network, reconstructs, scenes, Gaussian | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | fused, features, subsequently, construct, cost, volumes, Chen, When, combined, camera | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / 3.1 PRELIMINARIES - extractive PDF cue:** This behavior rapidly boosts image quality for near-input viewpoints, but under the alpha-blending rendering rule, occluded Gaussians contribute minimally to the output: C = X ...
- **p. 4 / 3.1 PRELIMINARIES - extractive PDF cue:** Given a collection of V input images {Iv}V v=1 with corresponding camera intrinsics {kv}V v=1 and poses {Tv}V v=1, the network fθ predicts Gaussian parameters ...
- **p. 4 / 3.1 PRELIMINARIES - extractive PDF cue:** Given sparse input images, our dual-path encoder processes them through both single-view and multi-view branches.
- **p. 6 / 3.1 PRELIMINARIES - extractive PDF cue:** Conventional metrics-such as PSNR, SSIM, and LPIPS-are typically computed at the same resolution as the input images (e.g., 256 × 256).
- **p. 15 / A.1 ENCODER ARCHITECTURE - extractive PDF cue:** For estimating the remaining Gaussian attributes-such as scale multipliers, high-frequency SH coefficients, and opacity-we apply an additional DPT head, conditioned on a concatenation of the ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** In contrast, feedforward approaches employ pretrained models to directly predict per-pixel 3D Gaussians from sparse inputs-often as few as two images-without any preprocessing.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** In summary, the main contributions of this work are as follows: • We propose SurfSplat, a feedforward network that reconstructs 3D scenes using 2D Gaussian ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | This rotation aligns the canonical frame with the estimated local surface, giving the updated surfel rotation: Rsurf = RR0 = R. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Following the standard COLMAP coordinate convention, where the camera frame has x pointing right, y downward, and z inward, we assume that ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / 3.1 PRELIMINARIES - extractive PDF cue:** To address this, we propose a forced alpha blending strategy that explicitly constrains each Gaussian's opacity.
- **p. 6 / 3.1 PRELIMINARIES - extractive PDF cue:** Published as a conference paper at ICLR 2026 We then use the neural network to predict scale multipliers ˆσu, ˆσv, which are constrained to lie ...
- **p. 8 / 4 EXPERIMENT - extractive PDF cue:** All other layers are trained with a learning rate of 2 × 10-4.
- **p. 7 / 4 EXPERIMENT - extractive PDF cue:** Both datasets provide precomputed camera poses and we adhere to the official train-test splits used in prior work.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** multi-view, branch, input, images, first, converted, low-resolution, feature, maps, then, processed, multiple, layers, self-, cross-attention, Vaswani, integrate, complementary, sources, effectively.
- **Relevant PDF headings:** 3 METHOD (p. 4); A.1 ENCODER ARCHITECTURE (p. 15).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Both datasets provide precomputed camera poses and we adhere to the official train-test splits used in prior work. | p. 7 (4 EXPERIMENT), p. 7 (4 EXPERIMENT) |
| Semantic / temporal fusion | We compare our method to state-of-the-art sparse-view generalizable methods for novel view synthesis, including PixelSplat Charatan et al. | p. 8 (4 EXPERIMENT), p. 8 (4 EXPERIMENT) |
| Robot query / planning handoff | Since using more primitives generally improves performance, we focus our core comparisons on the latter group to ensure a fair comparison. | p. 8 (4 EXPERIMENT), p. 9 (4 EXPERIMENT) |

## Failure and Ablation Link

- **p. 9 / Figure/Table caption - extractive PDF cue:** Figure 5: Ablation study: Visualization of recon- structed 3D scenes. Our full model yields contin- uous and coherent surfaces, while ablated variants exhibit visible artifacts ...
- **p. 9 / 4 EXPERIMENT - extractive PDF cue:** We also train a variant with the surface continuity prior but without forced alpha blending.
- **p. 15 / Figure/Table caption - extractive PDF cue:** Table 6: Ablations study on hyperparameter sensitivity. 256×256 (Standard) 512×512 (HRRC) 1024×1024 (HRRC) Average
- **p. 10 / 4 EXPERIMENT - extractive PDF cue:** Across these experiments, the relative performance rankings remained fully consistent with those observed under HRRC evaluation, even without any bicubic upsampling.
- **p. 8 / 4 EXPERIMENT - extractive PDF cue:** (2024b), but use a lower learning rate of 2 × 10-6 for the pretrained Depth Anything V2 backbone.
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Illustration for model architecture. Given sparse input images, our dual-path encoder processes them through both single-view and multi-view branches. The fused features are ...
- **p. 10 / 5 CONCLUSION - extractive PDF cue:** These limitations open opportunities for future research on joint pose elimination and compact, adaptive representations.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES), p. 15 (A.1 ENCODER ARCHITECTURE), p. 5 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES), p. 15 (A.1 ENCODER ARCHITECTURE), objective p. 4 (3.1 PRELIMINARIES), p. 4 (3.1 PRELIMINARIES), p. 5 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES), p. 15 (A.1 ENCODER ARCHITECTURE), temporal p. 5 (3.1 PRELIMINARIES), p. 5 (3.1 PRELIMINARIES), p. 6 (3.1 PRELIMINARIES), p. 1 (ABSTRACT), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
