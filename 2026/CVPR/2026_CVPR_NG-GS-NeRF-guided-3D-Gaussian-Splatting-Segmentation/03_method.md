# Method - NG-GS: NeRF-guided 3D Gaussian Splatting Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/He_NG-GS_NeRF-guided_3D_Gaussian_Splatting_Segmentation_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/He_NG-GS_NeRF-guided_3D_Gaussian_Splatting_Segmentation_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (4.1. Edge Gaussian Continuity), p. 3 (4. Method), p. 3 (4. Method), p. 4 (4.1. Edge Gaussian Continuity), p. 5 (4.1. Edge Gaussian Continuity), p. 5 (4.2. NeRF-GS Joint Optimization)): Through RBF interpolation, the discrete Gaussian features are fused into continuous features f inter, which are then fed into the NeRF module to reinforce spatial coherence across the representation.

## Method Body Digest

- **p. 4 / 4.1. Edge Gaussian Continuity - extractive PDF cue:** Through RBF interpolation, the discrete Gaussian features are fused into continuous features f inter, which are then fed into the NeRF module to reinforce spatial ...
- **p. 3 / 4. Method - extractive PDF cue:** To efficiently encode multi-scale spatial information, we incorporate multi-resolution hash encoding (MRHE), which enhances the representation capacity while maintaining computational efficiency. • NeRF-GS Joint Optimization: ...
- **p. 3 / 4. Method - extractive PDF cue:** A joint optimization strategy is employed, where alignment loss and spatial continuity loss are used to harmonize the outputs of 3DGS and NeRF.
- **p. 4 / 4.1. Edge Gaussian Continuity - extractive PDF cue:** After applying an L1 normalization on these weights, we use them to form the interpolation feature for each query point: f inter i = X ...
- **p. 5 / 4.1. Edge Gaussian Continuity - extractive PDF cue:** We use it to replace the traditional trigonometric function encoding in NeRF to extract high-dimensional features of ray upsampling points.
- **p. 5 / 4.2. NeRF-GS Joint Optimization - extractive PDF cue:** The boundary alignment loss function is a key constraint to ensure the coordinated operation of NeRF and 3DGS in the boundary region, which enforces consistency ...
- **p. 6 / 4.2. NeRF-GS Joint Optimization - extractive PDF cue:** The gradient smoothness loss function achieves visual smoothness by minimizing the magnitude of color gradients, thereby penalizing abrupt color variations.
- **p. 5 / 4.2. NeRF-GS Joint Optimization - extractive PDF cue:** NeRF projects a 3D scene onto a 2D image using volume rendering equations and calculates pixel colors using continuous integration.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** With the proposed NG-GS framework, we make the following main contributions: • we develop a continuous feature field construction module that combines RBF interpolation with ...
- **p. 1 / 1. Introduction - extractive PDF cue:** To overcome these challenges, we propose a novel NeRF-Guided 3DGS (NG-GS) segmentation framework, aiming to achieve model continuity at object boundaries.
- **p. 1 / 1. Introduction - extractive PDF cue:** (a) Mask (b) Mutated (c) Continuation (d) Our method Figure 1.

## Source Evidence Cues

- **p. 4 / 4.1. Edge Gaussian Continuity - extractive PDF cue:** Through RBF interpolation, the discrete Gaussian features are fused into continuous features f inter, which are then fed into the NeRF module to reinforce spatial ...
- **p. 3 / 4. Method - extractive PDF cue:** To efficiently encode multi-scale spatial information, we incorporate multi-resolution hash encoding (MRHE), which enhances the representation capacity while maintaining computational efficiency. • NeRF-GS Joint Optimization: ...
- **p. 3 / 4. Method - extractive PDF cue:** A joint optimization strategy is employed, where alignment loss and spatial continuity loss are used to harmonize the outputs of 3DGS and NeRF.
- **p. 4 / 4.1. Edge Gaussian Continuity - extractive PDF cue:** After applying an L1 normalization on these weights, we use them to form the interpolation feature for each query point: f inter i = X ...
- **p. 5 / 4.1. Edge Gaussian Continuity - extractive PDF cue:** We use it to replace the traditional trigonometric function encoding in NeRF to extract high-dimensional features of ray upsampling points.
- **p. 5 / 4.2. NeRF-GS Joint Optimization - extractive PDF cue:** The boundary alignment loss function is a key constraint to ensure the coordinated operation of NeRF and 3DGS in the boundary region, which enforces consistency ...
- **p. 6 / 4.2. NeRF-GS Joint Optimization - extractive PDF cue:** The gradient smoothness loss function achieves visual smoothness by minimizing the magnitude of color gradients, thereby penalizing abrupt color variations.
- **Detected method headings:** 4. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Through RBF interpolation, the discrete Gaussian features are fused into continuous features f inter, which are then fed into the NeRF module ... | p. 4 (4.1. Edge Gaussian Continuity), p. 3 (4. Method) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To efficiently encode multi-scale spatial information, we incorporate multi-resolution hash encoding (MRHE), which enhances the representation capacity while maintaining computational efficiency. • ... | p. 3 (4. Method), p. 3 (4. Method) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | A joint optimization strategy is employed, where alignment loss and spatial continuity loss are used to harmonize the outputs of 3DGS and ... | p. 3 (4. Method), p. 4 (4.1. Edge Gaussian Continuity) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 4.2. NeRF-GS Joint Optimization - extractive PDF cue:** The gradient smoothness loss function achieves visual smoothness by minimizing the magnitude of color gradients, thereby penalizing abrupt color variations.
- **p. 5 / 4.2. NeRF-GS Joint Optimization - extractive PDF cue:** The boundary alignment loss function is a key constraint to ensure the coordinated operation of NeRF and 3DGS in the boundary region, which enforces consistency ...
- **p. 3 / 4. Method - extractive PDF cue:** A joint optimization strategy is employed, where alignment loss and spatial continuity loss are used to harmonize the outputs of 3DGS and NeRF.
- **p. 5 / 4.2. NeRF-GS Joint Optimization - extractive PDF cue:** NeRF projects a 3D scene onto a 2D image using volume rendering equations and calculates pixel colors using continuous integration.
- **p. 3 / 4. Method - extractive PDF cue:** To efficiently encode multi-scale spatial information, we incorporate multi-resolution hash encoding (MRHE), which enhances the representation capacity while maintaining computational efficiency. • NeRF-GS Joint Optimization: ...
- **p. 4 / 4.1. Edge Gaussian Continuity - extractive PDF cue:** through a multi-view consistency process [37], where mij ∈[0, 1] represents the foreground probability derived from segmentation models (e.g., SAM) applied to multiview images.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (4.2. NeRF-GS Joint Optimization), p. 6 (4.2. NeRF-GS Joint Optimization), p. 3 (4. Method), p. 5 (4.2. NeRF-GS Joint Optimization), p. 4 (4.1. Edge Gaussian Continuity), p. 4 (4.1. Edge Gaussian Continuity).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | NG-GS, framework, make, following, main, contributions, develop, continuous, feature, field, construction, module, combines, RBF | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | NG-GS, framework, make, following, main, contributions, develop, continuous, feature, field | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | NG-GS, framework, make, following, main, contributions, develop, continuous, feature, field | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | gradient, smoothness, loss, function, achieves, visual, minimizing, magnitude, color, gradients | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive PDF cue:** With the proposed NG-GS framework, we make the following main contributions: • we develop a continuous feature field construction module that combines RBF interpolation with ...
- **p. 5 / 4.2. NeRF-GS Joint Optimization - extractive PDF cue:** These parameters dynamically adjust the hidden layers based on external conditions. ˆh(l) = ReLU  γ(l) ⊙h(l) + β(l) , (14) where ⊙is the element-wise ...
- **p. 3 / 3.1. NeRF - extractive PDF cue:** It takes a trained 3DGS model as input, and identifies boundary Gaussian points with the help of a 2D segmentation model.
- **p. 3 / 4. Method - extractive PDF cue:** A joint optimization strategy is employed, where alignment loss and spatial continuity loss are used to harmonize the outputs of 3DGS and NeRF.
- **p. 4 / 4.1. Edge Gaussian Continuity - extractive PDF cue:** This method generates smooth feature transitions between boundary Gaussian points, providing continuous feature field input for NeRF.
- **p. 4 / 4.1. Edge Gaussian Continuity - extractive PDF cue:** This module takes the trained 3DGS model G = {gi}Ng i=1 as input and produces spatially continuous features for the future NeRF process.
- **p. 5 / 4.2. NeRF-GS Joint Optimization - extractive PDF cue:** The interpolated feature f inter is input as a condition vector c of the NeRF network.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | This ensures that the final segmentation maintains both high-frequency details and smooth transitions across views. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | As illustrated in Figure 2, the framework operates in two core stages: • Edge Gaussian Continuity: We first identify ambiguous Gaussians located ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4.2. NeRF-GS Joint Optimization - extractive PDF cue:** The boundary alignment loss function is a key constraint to ensure the coordinated operation of NeRF and 3DGS in the boundary region, which enforces consistency ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Through, RBF, interpolation, discrete, Gaussian, features, fused, continuous, inter, then, NeRF, module, reinforce, spatial, coherence, across, representation, efficiently, encode, multi-scale.
- **Relevant PDF headings:** 4. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | NVOS consists of eight scenes picked from the LLFF [21] dataset. | p. 6 (5.1. Implementation Details), p. 6 (5.1. Implementation Details) |
| Semantic / temporal fusion | The proposed method is compared against a range of state-of-the-art baselines, which are categorized into mask-based and feedforward-based approaches. | p. 6 (5.1. Implementation Details), p. 6 (5.2. Quantitative Results) |
| Robot query / planning handoff | Red bounding boxes highlight key areas where our method has achieved significant improvements in boundary segmentation and spatial continuity. | p. 7 (5.3. Qualitative Results), p. 7 (5.4. Computational Efficiency Analysis) |

## Failure and Ablation Link

- **p. 8 / 5.4. Computational Efficiency Analysis - extractive PDF cue:** Ablation study of different components on NVOS dataset.
- **p. 8 / 5.5. Ablation Studies - extractive PDF cue:** It shows the performance changes on the NOVS dataset when different components are gradually removed from the original network.
- **p. 7 / 5.2. Quantitative Results - extractive PDF cue:** The results show that our method segments the boundaries of the object more clearly, without blurred Gaussians.
- **p. 8 / 6. Conclusion - extractive PDF cue:** Addressing current limitations, our future directions include extending the framework to dynamic scenes and real-time interactive applications, further bridging the gap between representation learning and ...
- **p. 8 / 5.6. Hyper-parameter Analysis - extractive PDF cue:** It is shown that τ=0.6 achieves the best balance between maintaining structural integrity and controlling background noise, resulting in excellent visual coherence and detail preservation.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (4.1. Edge Gaussian Continuity), p. 3 (4. Method), p. 3 (4. Method), p. 4 (4.1. Edge Gaussian Continuity), p. 5 (4.1. Edge Gaussian Continuity), p. 5 (4.2. NeRF-GS Joint Optimization), objective p. 6 (4.2. NeRF-GS Joint Optimization), p. 5 (4.2. NeRF-GS Joint Optimization), p. 3 (4. Method), p. 5 (4.2. NeRF-GS Joint Optimization), p. 3 (4. Method), p. 4 (4.1. Edge Gaussian Continuity), temporal p. 3 (4. Method), p. 3 (4. Method), p. 8 (6. Conclusion), p. 1 (Abstract), p. 1 (1. Introduction), p. 2 (2.1. 3DGS Reconstruction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
