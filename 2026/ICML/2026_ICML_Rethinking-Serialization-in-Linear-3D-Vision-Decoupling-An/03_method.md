# Method - Rethinking Serialization in Linear 3D Vision: Decoupling Anisotropic Geometry from Isotropic Semantics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=MSVQM8Ub2y; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/328620. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.1. Overview), p. 4 (3.1. Overview), p. 3 (3.1. Overview), p. 3 (3.1. Overview), p. 5 (3.1. Overview), p. 5 (3.1. Overview)): Following the DeLA architecture (Chen et al., 2023), we use dataset-specific hierarchical LAGM encoders (Figure 2a).

## Method Body Digest

- **p. 4 / 3.1. Overview - extractive PDF cue:** Following the DeLA architecture (Chen et al., 2023), we use dataset-specific hierarchical LAGM encoders (Figure 2a).
- **p. 4 / 3.1. Overview - extractive PDF cue:** The projected ESE feature is injected into the stage representation and then aggregated on the k-NN graph.
- **p. 3 / 3.1. Overview - extractive PDF cue:** The framework consists of two complementary modules: 1.
- **p. 3 / 3.1. Overview - extractive PDF cue:** Current 3D State-Space Models (SSMs) typically force point clouds into a single 1D sequence via space-filling curves, conflating local geometric modeling with global semantic aggregation.
- **p. 5 / 3.1. Overview - extractive PDF cue:** Unlike standard DeltaNet (Yang et al., 2024) which maintains a matrix state S ∈RD×D to capture cross-dimensional interactions, we employ a dimension-wise vector state st ...
- **p. 5 / 3.1. Overview - extractive PDF cue:** The small-decay limit therefore serves only as intuition for this high-retention regime; it should not be read as strict order invariance of intermediate states or ...
- **p. 3 / 3.1. Overview - extractive PDF cue:** The objective of LAGM is to capture local anisotropy within k-NN neighborhoods, independent of any global serialization order.
- **p. 3 / 3.1. Overview - extractive PDF cue:** For a point cloud P = {pi}N i=1 with coordinates pi ∈R3, the local neighborhood of point pi is defined as Nk(i) = arg min ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Based on this observation, we propose AnIsoNet, which decouples local anisotropic geometry modeling from global semantic aggregation.
- **p. 3 / 3.1. Overview - extractive PDF cue:** The framework consists of two complementary modules: 1.
- **p. 3 / 3.1. Overview - extractive PDF cue:** To address this limitation, we propose AnIsoNet, a unified framework that decouples these two processes (Figure 2).

## Source Evidence Cues

- **p. 4 / 3.1. Overview - extractive PDF cue:** Following the DeLA architecture (Chen et al., 2023), we use dataset-specific hierarchical LAGM encoders (Figure 2a).
- **p. 4 / 3.1. Overview - extractive PDF cue:** The projected ESE feature is injected into the stage representation and then aggregated on the k-NN graph.
- **p. 3 / 3.1. Overview - extractive PDF cue:** The framework consists of two complementary modules: 1.
- **p. 3 / 3.1. Overview - extractive PDF cue:** Current 3D State-Space Models (SSMs) typically force point clouds into a single 1D sequence via space-filling curves, conflating local geometric modeling with global semantic aggregation.
- **p. 5 / 3.1. Overview - extractive PDF cue:** Unlike standard DeltaNet (Yang et al., 2024) which maintains a matrix state S ∈RD×D to capture cross-dimensional interactions, we employ a dimension-wise vector state st ...
- **p. 5 / 3.1. Overview - extractive PDF cue:** The small-decay limit therefore serves only as intuition for this high-retention regime; it should not be read as strict order invariance of intermediate states or ...
- **Detected method headings:** 2.2. Linear Sequence Models & SSMs (p. 2); 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Following the DeLA architecture (Chen et al., 2023), we use dataset-specific hierarchical LAGM encoders (Figure 2a). | p. 4 (3.1. Overview), p. 4 (3.1. Overview) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | The projected ESE feature is injected into the stage representation and then aggregated on the k-NN graph. | p. 4 (3.1. Overview), p. 3 (3.1. Overview) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The framework consists of two complementary modules: 1. | p. 3 (3.1. Overview), p. 3 (3.1. Overview) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 3.1. Overview - extractive PDF cue:** The objective of LAGM is to capture local anisotropy within k-NN neighborhoods, independent of any global serialization order.
- **p. 3 / 3.1. Overview - extractive PDF cue:** For a point cloud P = {pi}N i=1 with coordinates pi ∈R3, the local neighborhood of point pi is defined as Nk(i) = arg min ...
- **p. 4 / 3.1. Overview - extractive PDF cue:** Right: gated state update mechanism with effective decay coefficient α and write gate β, enabling content-based retrieval through query projection.
- **p. 5 / 3.1. Overview - extractive PDF cue:** By contrast, GISA uses the content-based update in Eq.
- **p. 5 / 3.1. Overview - extractive PDF cue:** Although the GISA update has a recurrent form, it can be evaluated with a hardwarefriendly chunk-wise scan over Eq.
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 3 (3.1. Overview), p. 3 (3.1. Overview), p. 4 (3.1. Overview), p. 4 (3.1. Overview), p. 5 (3.1. Overview), p. 5 (3.1. Overview).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Mamba, Dao, state, evolves, ht-1, where, recurrent, hidden, inputdependent, step, size, continuous-time, transition, parameter | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Mamba, Dao, state, evolves, ht-1, where, recurrent, hidden, inputdependent, step | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | observation, AnIsoNet, decouples, local, anisotropic, geometry, modeling, global, semantic, aggregation | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | objective, LAGM, capture, local, anisotropy, within, k-NN, neighborhoods, independent, global | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 5 / 3.1. Overview - extractive PDF cue:** In Mamba (Gu & Dao, 2024), the state evolves as: ht = ¯A · ht-1 + ¯Bt · xt, yt = Ct · ht, (9) ...
- **p. 5 / 3.1. Overview - extractive PDF cue:** Unlike standard DeltaNet (Yang et al., 2024) which maintains a matrix state S ∈RD×D to capture cross-dimensional interactions, we employ a dimension-wise vector state st ...
- **p. 3 / 3.1. Overview - extractive PDF cue:** Current 3D State-Space Models (SSMs) typically force point clouds into a single 1D sequence via space-filling curves, conflating local geometric modeling with global semantic aggregation.
- **p. 3 / 3.1. Overview - extractive PDF cue:** LAGM: Local Anisotropy Geometric Modeling Our framework is built on a simple observation: 3D point cloud understanding requires local anisotropy for geometry but global isotropy ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Based on this observation, we propose AnIsoNet, which decouples local anisotropic geometry modeling from global semantic aggregation.
- **p. 4 / 3.1. Overview - extractive PDF cue:** The key point is that LAGM performs local anisotropic feature extraction before any global semantic aggregation.
- **p. 4 / 3.1. Overview - extractive PDF cue:** Right: gated state update mechanism with effective decay coefficient α and write gate β, enabling content-based retrieval through query projection.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | In our implementation, large point clouds are processed with a default maximum chunk size of 30K to control memory usage. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The framework consists of two complementary modules: 1. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | In our implementation, large point clouds are processed with a default maximum chunk size of 30K to control memory usage. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | All experiments are conducted on a single NVIDIA RTX 3090 GPU. | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Following, DeLA, architecture, Chen, dataset-specific, hierarchical, LAGM, encoders, Figure, projected, ESE, feature, injected, stage, representation, then, aggregated, k-NN, graph, framework.
- **Relevant PDF headings:** 2.2. Linear Sequence Models & SSMs (p. 2); 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Dataset Regime Protocol Identity/Default (%) Hilbert (%) Morton (%) S3DIS Dense scene Mode ablation 82.62 74.46 74.68 ScanObjectNN Sparse object Mode ablation ... | p. 7 (4.3. Analysis and Ablation), p. 8 (4.3. Analysis and Ablation) |
| Semantic / temporal fusion | Relative to linear-complexity baselines, it outperforms PCM (Zhang et al., 2025) by 3.0% and Sonata (lin.) by 10.3%. | p. 6 (4.2. Main Results), p. 7 (4.3. Analysis and Ablation) |
| Robot query / planning handoff | Overall, the figure shows that AnIsoNet improves accuracy while remaining in a much smaller parameter regime, rather than trading scale for performance. | p. 8 (4.4. Efficiency Analysis), p. 6 (4.1. Experimental Setup) |

## Failure and Ablation Link

- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of our AnIsoNet framework. (a) LAGM (Local Anisotropy Geometric Modeling) shows a representative hierarchical architecture; the number of stages is dataset-specific. Each ...
- **p. 6 / 4.2. Main Results - extractive PDF cue:** Underline denotes second-best without pre-training.
- **p. 6 / 4.2. Main Results - extractive PDF cue:** Compared with PTv3, it is 1.0% higher on the validation split without external pre-training.
- **p. 7 / 4.3. Analysis and Ablation - extractive PDF cue:** Replacing the spherical local encoding with the ellipsoidal variant improves the baseline from 73.48% to 74.44% (+0.96%), while adding GISA alone yields a larger gain ...
- **p. 7 / 4.3. Analysis and Ablation - extractive PDF cue:** Dataset Regime Protocol Identity/Default (%) Hilbert (%) Morton (%) S3DIS Dense scene Mode ablation 82.62 74.46 74.68 ScanObjectNN Sparse object Mode ablation 92.51 93.86 94.21 ...
- **p. 8 / 4.4. Efficiency Analysis - extractive PDF cue:** Its latency is not the lowest in the table-PointMamba is faster per forward pass-but AnIsoNet offers a stronger accuracy-resource trade-off, combining clearly better accuracy with ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Table 10. Cross-module ablation across benchmarks. ESE denotes the LAGM local encoder. S3DIS and ScanNetV2 report mIoU, while ScanObjectNN reports OA and mAcc.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.1. Overview), p. 4 (3.1. Overview), p. 3 (3.1. Overview), p. 3 (3.1. Overview), p. 5 (3.1. Overview), p. 5 (3.1. Overview), objective p. 3 (3.1. Overview), p. 3 (3.1. Overview), p. 4 (3.1. Overview), p. 5 (3.1. Overview), p. 5 (3.1. Overview), temporal p. 5 (3.1. Overview), p. 3 (3.1. Overview), p. 3 (3.1. Overview), p. 4 (3.1. Overview), p. 4 (3.1. Overview), p. 5 (3.1. Overview).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
