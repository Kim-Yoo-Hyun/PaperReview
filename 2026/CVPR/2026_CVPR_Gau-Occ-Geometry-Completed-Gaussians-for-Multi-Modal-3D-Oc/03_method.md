# Method - Gau-Occ: Geometry-Completed Gaussians for Multi-Modal 3D Occupancy Prediction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Lv_Gau-Occ_Geometry-Completed_Gaussians_for_Multi-Modal_3D_Occupancy_Prediction_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Lv_Gau-Occ_Geometry-Completed_Gaussians_for_Multi-Modal_3D_Occupancy_Prediction_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

PDF body method statement (p. 4 (3.4. Gaussian Anchor Fusion (GAF)), p. 3 (3.1. 3D Semantic Gaussian Scene Representation), p. 2 (3. Proposed Approach), p. 3 (3.2. LiDAR Completion Diffuser (LCD)), p. 2 (3. Proposed Approach), p. 5 (3.4. Gaussian Anchor Fusion (GAF))): To unify precise LiDAR geometry with rich image semantics, we propose Gaussian Anchor Fusion (GAF), a geometry-conditioned multi-modal fusion module that extracts, samples, and aggregates features for each Gaussian anchor.

## Method Body Digest

- **p. 4 / 3.4. Gaussian Anchor Fusion (GAF) - extractive body cue:** To unify precise LiDAR geometry with rich image semantics, we propose Gaussian Anchor Fusion (GAF), a geometry-conditioned multi-modal fusion module that extracts, samples, and aggregates ...
- **p. 3 / 3.1. 3D Semantic Gaussian Scene Representation - extractive body cue:** Each Gaussian then anchors multi-view image features via our Gaussian Anchor Fusion (GAF), producing geometry-aligned multi-modal representations.
- **p. 2 / 3. Proposed Approach - extractive body cue:** We propose Gau-Occ, a compact representation of 3D scenes using semantic Gaussians that jointly encode LiDAR geometry and multi-view semantics.
- **p. 3 / 3.2. LiDAR Completion Diffuser (LCD) - extractive body cue:** We propose the LiDAR Completion Diffuser (LCD), a local diffusion model that reconstructs dense, geometrically consistent point clouds from sparse scans.
- **p. 2 / 3. Proposed Approach - extractive body cue:** The completed points are then voxelized into sparse features that initialize density-aware Gaussians.
- **p. 5 / 3.4. Gaussian Anchor Fusion (GAF) - extractive body cue:** Crossattention is then performed between the LiDAR anchor (as query) and the modulated visual tokens (as keys/values): a(l) i = softmax
- **p. 5 / 3.4. Gaussian Anchor Fusion (GAF) - extractive body cue:** 3, instead of applying another attention block, we aggregate them via a geometry-aware VLAD-style [17] resampler using codewords {Cm}M m=1 that act as learnable semantic ...
- **p. 3 / 3.1. 3D Semantic Gaussian Scene Representation - extractive body cue:** Following [14], we optimize the model with a joint objective LCE + LLov, combining cross-entropy and Lov´aszSoftmax losses to enhance segmentation accuracy and class balance.

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are: • We propose Gau-Occ, a compact Gaussian-based framework that unifies LiDAR and multi-view images for 3D semantic occupancy prediction. • ...
- **p. 1 / 1. Introduction - extractive body cue:** We propose Gau-Occ, a framework that leverages learnable semantic Gaussian anchors for efficient scene representation.
- **p. 2 / 1. Introduction - extractive body cue:** Second, we propose the Gaussian Anchor Fusion (GAF) module, which aligns multi-view image semantics with a LiDAR-anchored 3D structural prior.

## Source Evidence Cues

- **p. 4 / 3.4. Gaussian Anchor Fusion (GAF) - extractive body cue:** To unify precise LiDAR geometry with rich image semantics, we propose Gaussian Anchor Fusion (GAF), a geometry-conditioned multi-modal fusion module that extracts, samples, and aggregates ...
- **p. 3 / 3.1. 3D Semantic Gaussian Scene Representation - extractive body cue:** Each Gaussian then anchors multi-view image features via our Gaussian Anchor Fusion (GAF), producing geometry-aligned multi-modal representations.
- **p. 2 / 3. Proposed Approach - extractive body cue:** We propose Gau-Occ, a compact representation of 3D scenes using semantic Gaussians that jointly encode LiDAR geometry and multi-view semantics.
- **p. 3 / 3.2. LiDAR Completion Diffuser (LCD) - extractive body cue:** We propose the LiDAR Completion Diffuser (LCD), a local diffusion model that reconstructs dense, geometrically consistent point clouds from sparse scans.
- **p. 2 / 3. Proposed Approach - extractive body cue:** The completed points are then voxelized into sparse features that initialize density-aware Gaussians.
- **p. 5 / 3.4. Gaussian Anchor Fusion (GAF) - extractive body cue:** Crossattention is then performed between the LiDAR anchor (as query) and the modulated visual tokens (as keys/values): a(l) i = softmax
- **p. 5 / 3.4. Gaussian Anchor Fusion (GAF) - extractive body cue:** 3, instead of applying another attention block, we aggregate them via a geometry-aware VLAD-style [17] resampler using codewords {Cm}M m=1 that act as learnable semantic ...
- **Detected method headings:** 3. Proposed Approach (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | To unify precise LiDAR geometry with rich image semantics, we propose Gaussian Anchor Fusion (GAF), a geometry-conditioned multi-modal fusion module that extracts, ... | p. 4 (3.4. Gaussian Anchor Fusion (GAF)), p. 3 (3.1. 3D Semantic Gaussian Scene Representation) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Each Gaussian then anchors multi-view image features via our Gaussian Anchor Fusion (GAF), producing geometry-aligned multi-modal representations. | p. 3 (3.1. 3D Semantic Gaussian Scene Representation), p. 2 (3. Proposed Approach) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | We propose Gau-Occ, a compact representation of 3D scenes using semantic Gaussians that jointly encode LiDAR geometry and multi-view semantics. | p. 2 (3. Proposed Approach), p. 3 (3.2. LiDAR Completion Diffuser (LCD)) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.1. 3D Semantic Gaussian Scene Representation - extractive body cue:** Following [14], we optimize the model with a joint objective LCE + LLov, combining cross-entropy and Lov´aszSoftmax losses to enhance segmentation accuracy and class balance.
- **p. 3 / 3.2. LiDAR Completion Diffuser (LCD) - extractive body cue:** Given a raw LiDAR scan P = {Pi ∈R3}NP i=1, the completion objective is to generate a densified point cloud P′ = {P ′ i}NP ...
- **p. 2 / 3. Proposed Approach - extractive body cue:** This produces view-consistent, semantically discriminative anchor features that update Gaussian attributes.
- **원문 대조:** Point-cloud feature와 image feature를 concatenate한 뒤 2-layer FFN이 Gaussian의 position offset, scale, rotation, semantic attribute를 갱신한다. Position은 기존 μ_i에 예측 offset을 더하고, refined Gaussian을 splat해 occupancy를 예측한다. ([PDF p. 5](https://openaccess.thecvf.com/content/CVPR2026/papers/Lv_Gau-Occ_Geometry-Completed_Gaussians_for_Multi-Modal_3D_Occupancy_Prediction_CVPR_2026_paper.pdf#page=5), §3.4 Gaussian Anchor Fusion, Eq. (17)).
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3.1. 3D Semantic Gaussian Scene Representation), p. 3 (3.2. LiDAR Completion Diffuser (LCD)), p. 2 (3. Proposed Approach), p. 5 (3.4. Gaussian Anchor Fusion (GAF)).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Given, sparse, LiDAR, point, cloud, multi-view, images, task, predict, voxelized, semantic, occupancy, grid, R/C/ | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Given, sparse, LiDAR, point, cloud, multi-view, images, task, predict, voxelized | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summary, contributions, Gau-Occ, compact, Gaussian-based, framework, unifies, LiDAR, multi-view, images | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Following, optimize, model, joint, objective, LCE, LLov, combining, cross-entropy, Lov | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 3.1. 3D Semantic Gaussian Scene Representation - extractive body cue:** Given a sparse LiDAR point cloud P = {Pi ∈R3}NP i=1 and multi-view images I = {Ij ∈R3×H×W }NI j=1, the task is to predict ...
- **p. 4 / 3.2. LiDAR Completion Diffuser (LCD) - extractive body cue:** The denoising network ˆϵθ learns to predict the injected noise conditioned on the sparse input P: Ldiff =
- **p. 3 / 3.2. LiDAR Completion Diffuser (LCD) - extractive body cue:** We propose the LiDAR Completion Diffuser (LCD), a local diffusion model that reconstructs dense, geometrically consistent point clouds from sparse scans.
- **p. 2 / 1. Introduction - extractive body cue:** In summary, our contributions are: • We propose Gau-Occ, a compact Gaussian-based framework that unifies LiDAR and multi-view images for 3D semantic occupancy prediction. • ...
- **p. 4 / 3.4. Gaussian Anchor Fusion (GAF) - extractive body cue:** To unify precise LiDAR geometry with rich image semantics, we propose Gaussian Anchor Fusion (GAF), a geometry-conditioned multi-modal fusion module that extracts, samples, and aggregates ...
- **p. 1 / 1. Introduction - extractive body cue:** Recent advances in 3D Gaussian [24, 25] primitives demonstrate that such representations can model scene geometry and semantics with high expressiveness from multi-view observations [6, ...
- **p. 3 / 3.2. LiDAR Completion Diffuser (LCD) - extractive body cue:** Given a raw LiDAR scan P = {Pi ∈R3}NP i=1, the completion objective is to generate a densified point cloud P′ = {P ′ i}NP ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Early-fusion schemes either project points into multiple image views [41] or lift dense image features into volumetric grids [38], while transformer-based fusion ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Removing GVR (Row 3) and directly feeding the original, unaggregated tokens Xi to cross-attention leads to markedly higher latency and memory usage, ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | Early-fusion schemes either project points into multiple image views [41] or lift dense image features into volumetric grids [38], while transformer-based fusion ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | We further conduct a comprehensive ablation study on the GAF module, focusing on two core components governing cross-modal fusion: (1) GGS (Geometry-Guided ... | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** unify, precise, LiDAR, geometry, rich, image, semantics, Gaussian, Anchor, Fusion, GAF, geometry-conditioned, multi-modal, module, extracts, samples, aggregates, features, then, anchors.
- **Relevant PDF headings:** 3. Proposed Approach (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We evaluate Gau-Occ on three widely adopted benchmarks: SurroundOcc-nuScenes [2, 46], Occ3DnuScenes [40], and KITTI-360 [28]. | p. 5 (4.1. Datasets and Metrics), p. 6 (4.2. Quantitative Results) |
| Semantic / temporal fusion | As shown, Gau-Occ outperforms the strongest LiDAR-only baseline, L2COcc [43], by +1.3 IoU and +0.6 mIoU. | p. 6 (4.2. Quantitative Results), p. 6 (4.3. Qualitative Comparison) |
| Robot query / planning handoff | Across modalities, LiDARonly approaches generally outperform camera-only methods due to geometric cues, and multi-modal systems further improve performance. | p. 5 (4.2. Quantitative Results), p. 5 (4.2. Quantitative Results) |

## Failure and Ablation Link

- **p. 7 / 4.4. Ablation Study - extractive body cue:** We further conduct a comprehensive ablation study on the GAF module, focusing on two core components governing cross-modal fusion: (1) GGS (Geometry-Guided Sampling), which conditions ...
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Visualization of ablations on GAF components. sistency during fusion.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** IoU↑ mIoU↑ 1 P DS + RS 41.5 29.6 2 PD(P) DS + RS 43.1 31.9 3 P′ RS 43.9 32.4 4 P′ DS + ...
- **p. 5 / 4.2. Quantitative Results - extractive body cue:** While DAOcc benefits from detection-level supervision, the proposed Gau-Occ attains superior accuracy without additional priors, highlighting advantage of geometrycomplete Gaussian anchors and structure-aware fusion.
- **p. 6 / 4.3. Qualitative Comparison - extractive body cue:** For example, in Case 1, Gau-Occ is the only method that reconstructs lower building outlines and terrain surfaces cleanly; in Case 2, it recovers distant ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1. Overview of Gau-Occ. Sparse LiDAR scans are first completed by a pretrained LiDAR Completion Diffuser (LCD) to recover occluded geometry. The completed points ...
- **p. 5 / 4.2. Quantitative Results - extractive body cue:** Gau-Occ also achieves clear gains on safety-critical classes such as bus, car, bicycle, and motorcycle, benefiting from precise Geo-VLAD resampling and geometry-aware FiLM modulation that ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (3.4. Gaussian Anchor Fusion (GAF)), p. 3 (3.1. 3D Semantic Gaussian Scene Representation), p. 2 (3. Proposed Approach), p. 3 (3.2. LiDAR Completion Diffuser (LCD)), p. 2 (3. Proposed Approach), p. 5 (3.4. Gaussian Anchor Fusion (GAF)), objective p. 3 (3.1. 3D Semantic Gaussian Scene Representation), p. 3 (3.2. LiDAR Completion Diffuser (LCD)), p. 2 (3. Proposed Approach), p. 5 (3.4. Gaussian Anchor Fusion (GAF)), temporal p. 1 (1. Introduction), p. 8 (4.4. Ablation Study), p. 4 (3.2. LiDAR Completion Diffuser (LCD)), p. 1 (1. Introduction), p. 2 (2.1. Semantic Occupancy Prediction), p. 2 (2.2. LiDAR-Camera Fusion in 3D Perception).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
