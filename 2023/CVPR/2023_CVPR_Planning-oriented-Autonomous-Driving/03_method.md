# Method - Planning-oriented Autonomous Driving

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2212.10156; PDF retrieval source: https://arxiv.org/pdf/2212.10156. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (2. Methodology), p. 5 (2. Methodology), p. 2 (2. Methodology), p. 4 (2. Methodology), p. 4 (2. Methodology), p. 3 (2. Methodology)): Detailedly, F t ds is passed through a self-attention layer to model responses between distant grids, then a crossattention layer models interactions between agent features Gt and per-grid features.

## Method Body Digest

- **p. 5 / 2. Methodology - extractive PDF cue:** Detailedly, F t ds is passed through a self-attention layer to model responses between distant grids, then a crossattention layer models interactions between agent features ...
- **p. 5 / 2. Methodology - extractive PDF cue:** To further conserve training memory, each block follows a downsample-upsample manner with an attention module in between to conduct pixel-agent interaction at 1/8 downscaled feature, ...
- **p. 2 / 2. Methodology - extractive PDF cue:** 2, UniAD comprises four transformer decoder-based perception and prediction modules and one planner in the end.
- **p. 4 / 2. Methodology - extractive PDF cue:** Each block takes as input the rich agent features Gt and the state (dense feature) F t-1 from the previous layer, and generates F t ...
- **p. 4 / 2. Methodology - extractive PDF cue:** This target trajectory optimization is only conducted in training and does not affect inference.
- **p. 3 / 2. Methodology - extractive PDF cue:** It is composed of N layers, and each layer captures three types of interactions: agent-agent, 3
- **p. 3 / 2. Methodology - extractive PDF cue:** Prediction: Motion Forecasting Recent studies have proven the effectiveness of transformer structure on the motion task [43,44,63,69,70,84,99], inspired by which we propose MotionFormer in the ...
- **p. 4 / 2. Methodology - extractive PDF cue:** The cost function regularizes the target trajectory to obey kinematic constraints.

## Design Rationale

- **p. 4 / 2. Methodology - extractive PDF cue:** To address this, we present OccFormer to incorporate both scene-level and agent-level semantics in two aspects: (1) a dense scene feature acquires agent-level features via ...
- **p. 2 / 1. Introduction - extractive PDF cue:** (b) we present UniAD, a comprehensive end-to-end system that leverages a wide span of tasks.
- **p. 2 / 1. Introduction - extractive PDF cue:** Through extensive ablations, we verify the superiority of our method over previous state-of-the-arts in all aspects.

## Source Evidence Cues

- **p. 5 / 2. Methodology - extractive PDF cue:** Detailedly, F t ds is passed through a self-attention layer to model responses between distant grids, then a crossattention layer models interactions between agent features ...
- **p. 5 / 2. Methodology - extractive PDF cue:** To further conserve training memory, each block follows a downsample-upsample manner with an attention module in between to conduct pixel-agent interaction at 1/8 downscaled feature, ...
- **p. 2 / 2. Methodology - extractive PDF cue:** 2, UniAD comprises four transformer decoder-based perception and prediction modules and one planner in the end.
- **p. 4 / 2. Methodology - extractive PDF cue:** Each block takes as input the rich agent features Gt and the state (dense feature) F t-1 from the previous layer, and generates F t ...
- **p. 4 / 2. Methodology - extractive PDF cue:** This target trajectory optimization is only conducted in training and does not affect inference.
- **p. 3 / 2. Methodology - extractive PDF cue:** It is composed of N layers, and each layer captures three types of interactions: agent-agent, 3
- **p. 3 / 2. Methodology - extractive PDF cue:** Prediction: Motion Forecasting Recent studies have proven the effectiveness of transformer structure on the motion task [43,44,63,69,70,84,99], inspired by which we propose MotionFormer in the ...
- **Detected method headings:** 2. Methodology (p. 2); Method (p. 7)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Detailedly, F t ds is passed through a self-attention layer to model responses between distant grids, then a crossattention layer models interactions ... | p. 5 (2. Methodology), p. 5 (2. Methodology) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | To further conserve training memory, each block follows a downsample-upsample manner with an attention module in between to conduct pixel-agent interaction at ... | p. 5 (2. Methodology), p. 2 (2. Methodology) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | 2, UniAD comprises four transformer decoder-based perception and prediction modules and one planner in the end. | p. 2 (2. Methodology), p. 4 (2. Methodology) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 2. Methodology - extractive PDF cue:** The cost function regularizes the target trajectory to obey kinematic constraints.
- **p. 5 / 2.4. Planning - extractive PDF cue:** To further avoid collisions, we optimize ˆτ based on Newton's method in inference only by the following: \ lab el { eq:p lan -argmin} \tau ...
- **p. 4 / 2. Methodology - extractive PDF cue:** The process is: \ l abe l { e q:no n-linear-argmin} \tilde {\mathbf {x}}^* = \arg \min _{\mathbf {x}} c(\mathbf {x}, \tilde {\mathbf {x}} ), ...
- **p. 5 / 2.4. Planning - extractive PDF cue:** The cost function f(·) is calculated by: \l abe l { e q:col-cos t} f ( \tau
- **p. 3 / 2. Methodology - extractive PDF cue:** This paradigm produces multi-agent trajectories in the frame with a single forward pass, which greatly saves the computational cost of aligning the whole scene to ...
- **p. 3 / 2. Methodology - extractive PDF cue:** MapFormer also has N stacked layers whose output results of each layer are all supervised, while only the updated queries QM in the last layer ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (2. Methodology), p. 5 (2.4. Planning), p. 4 (2. Methodology), p. 5 (2.5. Learning), p. 3 (2. Methodology).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | MapFormer, stacked, layers, whose, output, layer, supervised, while, only, updated, queries, last, forwarded, MotionFormer | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | MapFormer, stacked, layers, whose, output, layer, supervised, while, only, updated | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | address, present, OccFormer, incorporate, scene-level, agent-level, semantics, aspects, dense, scene | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | cost, function, regularizes, target, trajectory, obey, kinematic, constraints, further, avoid | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / 2. Methodology - extractive PDF cue:** MapFormer also has N stacked layers whose output results of each layer are all supervised, while only the updated queries QM in the last layer ...
- **p. 3 / 2. Methodology - extractive PDF cue:** Similar to [8], TrackFormer contains N layers and the final output state QA provides knowledge of Na valid agents for downstream prediction tasks.
- **p. 4 / 2. Methodology - extractive PDF cue:** Each block takes as input the rich agent features Gt and the state (dense feature) F t-1 from the previous layer, and generates F t ...
- **p. 2 / 2. Methodology - extractive PDF cue:** MapFormer takes map queries as semantic abstractions of road elements (e.g., lanes and dividers) and performs panoptic seg2
- **p. 4 / 2. Methodology - extractive PDF cue:** For each motion query Qi,k (defined later, and we omit subscripts i, k in the following context for simplicity), its interactions between other agents QA ...
- **p. 7 / Method - extractive PDF cue:** UniAD outperforms previous end-to-end MOT techniques (with image inputs only) on all metrics. †: Tracking-by-detection method with post-association, reimplemented with BEVFormer for a fair comparison.
- **p. 2 / 2. Methodology - extractive PDF cue:** Queries Q play the role of connecting the pipeline to model different interactions of entities in the driving scenario.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Specifically, at each time step, initialized detection queries are responsible for detecting newborn agents that are perceived for the first time, while ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | (11) Here λcoord, λobs, and σ are hyperparameters, and t indexes a timestep of future horizons. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 2. Methodology - extractive PDF cue:** To further conserve training memory, each block follows a downsample-upsample manner with an attention module in between to conduct pixel-agent interaction at 1/8 downscaled feature, ...
- **p. 4 / 2. Methodology - extractive PDF cue:** This target trajectory optimization is only conducted in training and does not affect inference.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Detailedly, passed, through, self-attention, layer, model, responses, between, distant, grids, then, crossattention, models, interactions, agent, features, per-grid, further, conserve, training.
- **Relevant PDF headings:** 2. Methodology (p. 2); Method (p. 7).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | We conduct experiments on the challenging nuScenes dataset [6]. | p. 6 (3. Experiments), p. 6 (3.2. Modular Results) |
| Semantic / temporal fusion | The first row (ID-0) serves as a vanilla multi-task baseline with separate task heads for comparison. | p. 6 (3.1. Joint Results), p. 6 (3.2. Modular Results) |
| Robot query / planning handoff | UniAD achieves the lowest L2 error and collision rate in all time intervals and even outperforms LiDAR-based methods (†) in most cases, ... | p. 7 (3.3. Qualitative Results), p. 6 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 6 / 3.1. Joint Results - extractive PDF cue:** We conduct extensive ablations as shown in Table 2 to prove the effectiveness and necessity of preceding tasks in the end-to-end pipeline.
- **p. 6 / 3. Experiments - extractive PDF cue:** In this section, we validate the effectiveness of our design in three aspects: joint results revealing the advantage of task coordination and its effect on ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 8. Ablation for designs in the motion forecasting module. All components contribute to the ultimate performance. "Scene- l. Anch." denotes rotated scene-level anchors. "Goal ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Pipeline of Unified Autonomous Driving (UniAD). It is exquisitely devised following planning-oriented philosophy. Instead of a simple stack of tasks, we investigate the ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 9. Ablation for designs in the occupancy prediction mod- ule. Cross-attention with masks and the reuse of mask feature helps improve the prediction. "Cross. ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 10. Ablation for designs in the planning module. Results demonstrate the necessity of each preceding task. "BEV Att." in- dicates attending to BEV feature. ...
- **p. 23 / Figure/Table caption - extractive PDF cue:** Figure 10. Critical case visualization. Here we demonstrate two critical cases. The first scenario (top) shows that the ego vehicle is yielding to two pedestrians ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (2. Methodology), p. 5 (2. Methodology), p. 2 (2. Methodology), p. 4 (2. Methodology), p. 4 (2. Methodology), p. 3 (2. Methodology), objective p. 4 (2. Methodology), p. 5 (2.4. Planning), p. 4 (2. Methodology), p. 5 (2.4. Planning), p. 3 (2. Methodology), p. 3 (2. Methodology), temporal p. 3 (2. Methodology), p. 5 (2.4. Planning), p. 3 (2. Methodology), p. 5 (2. Methodology), p. 7 (Method), p. 2 (2. Methodology).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
