# Method - Thickness-aware E(3)-Equivariant 3D Mesh Neural Networks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=Ya2ksKuNMh; PDF retrieval source: https://openreview.net/pdf/9288751ce812b90a105565d83b7d5b425b2f11d7.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (4.2.1. ENCODER), p. 5 (4.2.3. THICKNESS PROCESSOR), p. 6 (4.2.3. THICKNESS PROCESSOR), p. 3 (4. Methodology), p. 5 (4.2.3. THICKNESS PROCESSOR), p. 6 (4.2.4. DECODER)): The outputs of the geometric encoders, z(0) i ∈Rd and e(0) ij ∈ Rd, are later used as the input embeddings for the first layer (l = 0) of the ...

## Method Body Digest

- **p. 4 / 4.2.1. ENCODER - extractive PDF cue:** The outputs of the geometric encoders, z(0) i ∈Rd and e(0) ij ∈ Rd, are later used as the input embeddings for the first layer ...
- **p. 5 / 4.2.3. THICKNESS PROCESSOR - extractive PDF cue:** In addition, to account for thickness-related interactions, we introduce a thickness edge ei,thick connecting vi to T (vi), with its feature fi,thick ∈R2 defined as: ...
- **p. 6 / 4.2.3. THICKNESS PROCESSOR - extractive PDF cue:** The embedding for this thickness edge ei,thick ∈Rd is initialized in the first layer using a dedicated encoder, ϕthick, which maps the thickness edge feature ...
- **p. 3 / 4. Methodology - extractive PDF cue:** T-EMNN consists of an encoder (Sec.
- **p. 5 / 4.2.3. THICKNESS PROCESSOR - extractive PDF cue:** By training on real-world data, the model dynamically adapts to identify the optimal threshold τ that captures interactions between opposing surfaces without relying on manual ...
- **p. 6 / 4.2.4. DECODER - extractive PDF cue:** First, the geometric and spatial embeddings are concatenated and processed as follows: zfinal i = ϕcombine([zi, zcoord i ]) ∈Rd, (19) where ϕcombine integrates geometric ...
- **p. 4 / 4.2.1. ENCODER - extractive PDF cue:** For every node vi ∈V and edge eij ∈E within the surface mesh M = (V, E), we encode their features using respective MLP encoders.
- **p. 5 / 4.2.2. SURFACE PROCESSOR - extractive PDF cue:** Then, the update rule for the node embeddings z(l) i ∈Rd is defined as: zsurf,(l) i ←f V surf(z(l) i , X j∈N(i) e(l+1) ij ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** The key contributions of this study are as follows: • Thickness-Aware Framework: We propose a Thicknessaware E(3)-Equivariant 3D Mesh Neural Networks (TEMNN) that accurately models ...
- **p. 1 / 1. Introduction - extractive PDF cue:** To quantitatively illustrate the significance of these interactions, we present an analysis in Fig.
- **p. 3 / 4. Methodology - extractive PDF cue:** T-EMNN consists of an encoder (Sec.

## Source Evidence Cues

- **p. 4 / 4.2.1. ENCODER - extractive PDF cue:** The outputs of the geometric encoders, z(0) i ∈Rd and e(0) ij ∈ Rd, are later used as the input embeddings for the first layer ...
- **p. 5 / 4.2.3. THICKNESS PROCESSOR - extractive PDF cue:** In addition, to account for thickness-related interactions, we introduce a thickness edge ei,thick connecting vi to T (vi), with its feature fi,thick ∈R2 defined as: ...
- **p. 6 / 4.2.3. THICKNESS PROCESSOR - extractive PDF cue:** The embedding for this thickness edge ei,thick ∈Rd is initialized in the first layer using a dedicated encoder, ϕthick, which maps the thickness edge feature ...
- **p. 3 / 4. Methodology - extractive PDF cue:** T-EMNN consists of an encoder (Sec.
- **p. 5 / 4.2.3. THICKNESS PROCESSOR - extractive PDF cue:** By training on real-world data, the model dynamically adapts to identify the optimal threshold τ that captures interactions between opposing surfaces without relying on manual ...
- **p. 6 / 4.2.4. DECODER - extractive PDF cue:** First, the geometric and spatial embeddings are concatenated and processed as follows: zfinal i = ϕcombine([zi, zcoord i ]) ∈Rd, (19) where ϕcombine integrates geometric ...
- **p. 4 / 4.2.1. ENCODER - extractive PDF cue:** For every node vi ∈V and edge eij ∈E within the surface mesh M = (V, E), we encode their features using respective MLP encoders.
- **Detected method headings:** 4. Methodology (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | The outputs of the geometric encoders, z(0) i ∈Rd and e(0) ij ∈ Rd, are later used as the input embeddings for ... | p. 4 (4.2.1. ENCODER), p. 5 (4.2.3. THICKNESS PROCESSOR) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | In addition, to account for thickness-related interactions, we introduce a thickness edge ei,thick connecting vi to T (vi), with its feature fi,thick ... | p. 5 (4.2.3. THICKNESS PROCESSOR), p. 6 (4.2.3. THICKNESS PROCESSOR) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The embedding for this thickness edge ei,thick ∈Rd is initialized in the first layer using a dedicated encoder, ϕthick, which maps the ... | p. 6 (4.2.3. THICKNESS PROCESSOR), p. 3 (4. Methodology) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 4.2.2. SURFACE PROCESSOR - extractive PDF cue:** Then, the update rule for the node embeddings z(l) i ∈Rd is defined as: zsurf,(l) i ←f V surf(z(l) i , X j∈N(i) e(l+1) ij ...
- **p. 5 / 4.2.2. SURFACE PROCESSOR - extractive PDF cue:** The update rule for the edge embeddings e(l) ij ∈Rd is defined as: e(l+1) ij ←f M surf(e(l) ij , z(l) i , z(l) j ...
- **p. 6 / 4.2.3. THICKNESS PROCESSOR - extractive PDF cue:** For subsequent layers, e(l) i,thick ∈Rd is updated using the output from the previous layer e(l-1) i,thick.
- **p. 6 / 4.2.3. THICKNESS PROCESSOR - extractive PDF cue:** Then, the updated embedding of node vi, z(l+1) i ∈Rd, is then computed as: z(l+1) i ←f V thick(zsurf,(l) i , e(l+1) i,thick), (18) where ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (4.2.2. SURFACE PROCESSOR), p. 5 (4.2.2. SURFACE PROCESSOR), p. 6 (4.2.3. THICKNESS PROCESSOR), p. 6 (4.2.3. THICKNESS PROCESSOR).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | transformed, coordinates, xinv, along, stored, allow, seamless, mapping, between, input, output, spaces, outputs, geometric | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | transformed, coordinates, xinv, along, stored, allow, seamless, mapping, between, input | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | contributions, study, follows, Thickness-Aware, Framework, Thicknessaware, Equivariant, Mesh, Neural, Networks | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | Then, update, rule, node, embeddings, defined, zsurf, surf, where, another | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 4. Methodology - extractive PDF cue:** The transformed coordinates xinv i , along with the stored xi and R, allow seamless mapping between the input and output spaces.
- **p. 4 / 4.2.1. ENCODER - extractive PDF cue:** The outputs of the geometric encoders, z(0) i ∈Rd and e(0) ij ∈ Rd, are later used as the input embeddings for the first layer ...
- **p. 3 / 3.1. Notations - extractive PDF cue:** The goal of this study is to predict the deformation of each node along the x, y, and z axes, given the shape and the ...
- **p. 2 / 1. Introduction - extractive PDF cue:** The key contributions of this study are as follows: • Thickness-Aware Framework: We propose a Thicknessaware E(3)-Equivariant 3D Mesh Neural Networks (TEMNN) that accurately models ...
- **p. 3 / 3.1. Notations - extractive PDF cue:** Formally, the deformation at a node vi is represented as ∆xi = [∆xi, ∆yi, ∆zi], which is the output of the model.
- **p. 5 / 4.2.3. THICKNESS PROCESSOR - extractive PDF cue:** To address this, we define a Thickness threshold τ that dynamically regulates the interactions between nodes.
- **p. 5 / 4.2.2. SURFACE PROCESSOR - extractive PDF cue:** The updated node embeddings zsurf,(l) i ∈Rd serve as the input for the corresponding l-th layer of the thickness processor.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | To evaluate the dynamic capabilities of our framework-particularly the thickness processor-we conduct next-timestep deformation prediction using the Deforming Plate dataset (Pfaff et ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The overall framework is shown in Fig. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | Model Performance in In-Distribution and Out-of-Distribution Settings, averaged over 3 seeds with standard deviation (in parentheses). | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 4.2.3. THICKNESS PROCESSOR - extractive PDF cue:** By training on real-world data, the model dynamically adapts to identify the optimal threshold τ that captures interactions between opposing surfaces without relying on manual ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** outputs, geometric, encoders, later, input, embeddings, first, layer, processor, modules, addition, account, thickness-related, interactions, introduce, thickness, edge, thick, connecting, feature.
- **Relevant PDF headings:** 4. Methodology (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We evaluate T-EMNN using a dataset from real-world injection molding applications. | p. 6 (5.1. Dataset Description), p. 6 (5.1. Dataset Description) |
| Semantic / temporal fusion | 8, all baseline models exhibit improved performance when incorporating thickness edges compared to their counterparts without them. | p. 8 (5.4.2. IMPACT OF THICKNESS-AWARE FRAMEWORK), p. 8 (5.4.1. MAIN RESULTS) |
| Robot query / planning handoff | The results demonstrate that spatial information alone is sufficient to achieve strong performance in terms of R2 score, highlighting its importance in ... | p. 7 (5.4.1. MAIN RESULTS), p. 7 (5.4.1. MAIN RESULTS) |

## Failure and Ablation Link

- **p. 6 / 5.2. Baselines - extractive PDF cue:** Building upon EGNN, EMNN (Trang et al., 2024) optimizes this framework for mesh data by generating E(3)-invariant messages that incorporate geometric information from mesh faces.
- **p. 7 / 5.3. Evaluation Settings - extractive PDF cue:** Thickness-aware E(3)-Equivariant 3D Mesh Neural Networks Table 1.
- **p. 7 / 5.4.1. MAIN RESULTS - extractive PDF cue:** However, when the coordinate system lacks E(3)-equivariant properties, performance significantly deteriorates when testing data exhibits a different coordinate distribution (i.e., out-of-distribution results of (a) in ...
- **p. 8 / 5.4.2. IMPACT OF THICKNESS-AWARE FRAMEWORK - extractive PDF cue:** Ablation Study of Thickness Edge Features.
- **p. 8 / 5.4.2. IMPACT OF THICKNESS-AWARE FRAMEWORK - extractive PDF cue:** 8, all baseline models exhibit improved performance when incorporating thickness edges compared to their counterparts without them.
- **p. 14 / Figure/Table caption - extractive PDF cue:** Figure 14. Comparisons between volume mesh and surface mesh. The methods used for comparison are based on the MGN framework with coordinate embeddings from our ...
- **p. 14 / Figure/Table caption - extractive PDF cue:** Figure 13. R2 scores for all test data. In the shape IDs, ‘s' indicates seen shapes included in the training data, while ‘us' refers to ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (4.2.1. ENCODER), p. 5 (4.2.3. THICKNESS PROCESSOR), p. 6 (4.2.3. THICKNESS PROCESSOR), p. 3 (4. Methodology), p. 5 (4.2.3. THICKNESS PROCESSOR), p. 6 (4.2.4. DECODER), objective p. 5 (4.2.2. SURFACE PROCESSOR), p. 5 (4.2.2. SURFACE PROCESSOR), p. 6 (4.2.3. THICKNESS PROCESSOR), p. 6 (4.2.3. THICKNESS PROCESSOR), temporal p. 8 (5.4.3. EVALUATION UNDER DYNAMIC SETTING), p. 3 (4. Methodology), p. 3 (4. Methodology), p. 4 (4. Methodology), p. 5 (4.2.3. THICKNESS PROCESSOR), p. 6 (5.2. Baselines).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
