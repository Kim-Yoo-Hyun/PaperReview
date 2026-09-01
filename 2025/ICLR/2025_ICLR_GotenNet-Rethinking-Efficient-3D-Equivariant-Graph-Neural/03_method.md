# Method - GotenNet: Rethinking Efficient 3D Equivariant Graph Neural Networks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=5wxCQDtbMo; PDF retrieval source: https://openreview.net/pdf/a1396f1d1e7975177c314f3bddd7e718fc87796e.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 2 (B L), p. 2 (B L), p. 1 (ABSTRACT), p. 1 (ABSTRACT)): These mechanisms enhance transformer-based architectures by refining edge representations through high-degree steerable features, enabling the self-attention mechanism to leverage refined geometric relationships in determining node inte ...

## Method Body Digest

- **p. 2 / B L - extractive PDF cue:** These mechanisms enhance transformer-based architectures by refining edge representations through high-degree steerable features, enabling the self-attention mechanism to leverage refined geometric relationships in determining node ...
- **p. 2 / B L - extractive PDF cue:** First, we introduce a spherical-scalarization model with an efficient representation and embedding strategy designed specifically with geometric tensors, eliminating the need for irreps and CG ...
- **p. 1 / ABSTRACT - extractive PDF cue:** We introduce a unified structural embedding, incorporating geometryaware tensor attention and hierarchical tensor refinement that iteratively updates edge representations through inner product operations on high-degree ...
- **p. 1 / ABSTRACT - extractive PDF cue:** To address this gap, we propose a novel Geometric Tensor Network (GotenNet) that effectively models the geometric intricacies of 3D graphs while ensuring strict equivariance ...
- **p. 2 / B L - extractive PDF cue:** Most current architectures (Han et al., 2024; Wang et al., 2024; Liao & Smidt, 2023; Liao et al., 2024) either compromise on expressiveness for efficiency ...
- **p. 1 / ABSTRACT - extractive PDF cue:** We evaluated models on QM9, rMD17, MD22, and Molecule3D datasets, where the proposed model consistently outperforms state-of-the-art methods in both scalar and high-degree property predictions, ...
- **p. 2 / B L - extractive PDF cue:** Through rigorous evaluations on benchmark datasets-QM9, Molecule3D, rMD17, and MD22-our approach consistently outperforms state-of-the-art methods, even in its smallest configuration, establishing GotenNet as a versatile ...

## Design Rationale

- **p. 1 / ABSTRACT - extractive PDF cue:** To address this gap, we propose a novel Geometric Tensor Network (GotenNet) that effectively models the geometric intricacies of 3D graphs while ensuring strict equivariance ...
- **p. 2 / B L - extractive PDF cue:** To address these challenges, we propose a novel framework, the Geometric Tensor Network (GotenNet).
- **p. 2 / B L - extractive PDF cue:** First, we introduce a spherical-scalarization model with an efficient representation and embedding strategy designed specifically with geometric tensors, eliminating the need for irreps and CG ...

## Source Evidence Cues

- **p. 2 / B L - extractive PDF cue:** These mechanisms enhance transformer-based architectures by refining edge representations through high-degree steerable features, enabling the self-attention mechanism to leverage refined geometric relationships in determining node ...
- **p. 2 / B L - extractive PDF cue:** First, we introduce a spherical-scalarization model with an efficient representation and embedding strategy designed specifically with geometric tensors, eliminating the need for irreps and CG ...
- **p. 1 / ABSTRACT - extractive PDF cue:** We introduce a unified structural embedding, incorporating geometryaware tensor attention and hierarchical tensor refinement that iteratively updates edge representations through inner product operations on high-degree ...
- **p. 1 / ABSTRACT - extractive PDF cue:** To address this gap, we propose a novel Geometric Tensor Network (GotenNet) that effectively models the geometric intricacies of 3D graphs while ensuring strict equivariance ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | These mechanisms enhance transformer-based architectures by refining edge representations through high-degree steerable features, enabling the self-attention mechanism to leverage refined geometric relationships ... | p. 2 (B L), p. 2 (B L) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | First, we introduce a spherical-scalarization model with an efficient representation and embedding strategy designed specifically with geometric tensors, eliminating the need for ... | p. 2 (B L), p. 1 (ABSTRACT) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | We introduce a unified structural embedding, incorporating geometryaware tensor attention and hierarchical tensor refinement that iteratively updates edge representations through inner product ... | p. 1 (ABSTRACT), p. 1 (ABSTRACT) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / ABSTRACT - extractive PDF cue:** We introduce a unified structural embedding, incorporating geometryaware tensor attention and hierarchical tensor refinement that iteratively updates edge representations through inner product operations on high-degree ...
- **p. 2 / B L - extractive PDF cue:** Most current architectures (Han et al., 2024; Wang et al., 2024; Liao & Smidt, 2023; Liao et al., 2024) either compromise on expressiveness for efficiency ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 1 (ABSTRACT).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | evaluated, models, QM9, rMD17, MD22, Molecule3D, datasets, where, model, consistently, outperforms, state-of-the-art, methods, scalar | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | evaluated, models, QM9, rMD17, MD22, Molecule3D, datasets, where, model, consistently | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | address, novel, Geometric, Tensor, Network, GotenNet, effectively, models, intricacies, graphs | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | introduce, unified, structural, embedding, incorporating, geometryaware, tensor, attention, hierarchical, refinement | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / ABSTRACT - extractive PDF cue:** We evaluated models on QM9, rMD17, MD22, and Molecule3D datasets, where the proposed model consistently outperforms state-of-the-art methods in both scalar and high-degree property predictions, ...
- **p. 2 / B L - extractive PDF cue:** These mechanisms enhance transformer-based architectures by refining edge representations through high-degree steerable features, enabling the self-attention mechanism to leverage refined geometric relationships in determining node ...
- **p. 2 / B L - extractive PDF cue:** Through rigorous evaluations on benchmark datasets-QM9, Molecule3D, rMD17, and MD22-our approach consistently outperforms state-of-the-art methods, even in its smallest configuration, establishing GotenNet as a versatile ...
- **p. 1 / ABSTRACT - extractive PDF cue:** To address this gap, we propose a novel Geometric Tensor Network (GotenNet) that effectively models the geometric intricacies of 3D graphs while ensuring strict equivariance ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Experiments were conducted with an NVIDIA A100 GPU with 80GB video memory, 512GB RAM, and an AMD EPYC 7713P CPU. | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | Split Random Scaffold Task µ εHOMO εLUMO ∆ε std. log ∆ε GIN-Virtual .0882 .0692 .0632 .1036 .0592 -2.87 .2371 SchNet .0532 .0275 ... | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | Experiments were conducted with an NVIDIA A100 GPU with 80GB video memory, 512GB RAM, and an AMD EPYC 7713P CPU. | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** The x-axis shows the node count, while the y-axis shows the training time per batch in milliseconds.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** We analyze computational efficiency by measuring training time across varying node counts (10-140 nodes per graph).

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** mechanisms, enhance, transformer-based, architectures, refining, edge, representations, through, high-degree, steerable, features, enabling, self-attention, mechanism, leverage, refined, geometric, relationships, determining, node.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | This dataset contains over 29× more graphs than QM9, with approximately 1.6× and 1.9× increases in the average number of nodes and ... | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Semantic / temporal fusion | As shown in Table 1, even our smallest variant GotenNetS outperforms baseline methods on nine out of twelve targets while surpassing baselines ... | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Robot query / planning handoff | GotenNetB demonstrates further improvements, achieving best performance on eleven targets and significantly improving aggregated metrics, reducing standard MAE by over 16% and ... | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |

## Failure and Ablation Link

- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** The removal of any one of these components results in a significant degradation in performance, particularly in the cases without geometric encoding (row 4) or ...
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** 4.5 ABLATION STUDY Table 5: Ablation study on QM9 dataset. # L Lmax SE SEA GE HTR std log 4 2 ✓ ✓ ✓ ✓ ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** As shown in Table 1, even our smallest variant GotenNetS outperforms baseline methods on nine out of twelve targets while surpassing baselines on std.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** We evaluate three model variants - small (S), base (B), and large (L) - to analyze both performance and scaling behavior, with detailed specifications in ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Both GotenNetS and GotenNetB variants maintain consistent efficiency across all node counts, demonstrating their suitability for large-scale applications where computational overhead is critical.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Following the data splits from (Chmiela et al., 2023), we evaluate GotenNet against several baselines, including sDGML (Chmiela et al., 2018), ET (Thölke & De ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Architecture of GotenNet. The overall framework (a) includes an embedding, an interaction module, and a decoder; (b) shows the geometry-aware tensor attention (GATA); ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 2 (B L), p. 2 (B L), p. 1 (ABSTRACT), p. 1 (ABSTRACT), objective p. 1 (ABSTRACT), p. 2 (B L), temporal p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 1 (ABSTRACT), p. 2 (B L), p. 2 (B L), p. 3 (2 RELATED WORK).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
