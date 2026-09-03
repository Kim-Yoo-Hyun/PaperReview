# Method - Open-Vocabulary Spatio-Temporal Scene Graph for Robot Perception and Teleoperation Planning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_5.html; PDF retrieval source: https://arxiv.org/pdf/2509.23107. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 2 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 2 (III. METHODOLOGY)): The planner outputs a sequence of high-level actions π = (a1, . . . , aM) with grounded arguments (e.g., centroids and sizes), which are parsed into skill parameters for ...

## Method Body Digest

- **p. 4 / III. METHODOLOGY - extractive body cue:** The planner outputs a sequence of high-level actions π = (a1, . . . , aM) with grounded arguments (e.g., centroids and sizes), which are ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** User commands are used to query node features, filtering relevant nodes to form an ST-OVSG subgraph, which is then serialized into JSON and provided to ...
- **p. 2 / III. METHODOLOGY - extractive body cue:** Problem Formulation We aim to construct a temporally indexed, semantically enriched representation of dynamic 3D environments, enabling LVLM-based robot planner to plan action based on ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** Su is then serialized into a lightweight JSON-style description that lists, for each node, its class y, centroid c, size s, salient spatial relations, and ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** An image encoder Φv and a text encoder Φt (e.g., CLIP [27]) are adopted to extract masked visual features f img i = Φv(Irgb n ...
- **p. 2 / III. METHODOLOGY - extractive body cue:** In teleoperation settings, the LVLM planner operates remotely together with the robot, while a
- **p. 4 / III. METHODOLOGY - extractive body cue:** However, when multiple candidate pairs overlap or are ambiguous, resolve them by minimizing a simple geometric cost.
- **p. 4 / III. METHODOLOGY - extractive body cue:** The cost is cspa j,k,n = wiou (1 -IoU(uj,k,n, zj,k,n)) + warea

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** The main contributions of this work can be summarized as follows: 1) We propose ST-OVSG, a novel spatio-temporal openvocabulary scene graph, which explicitly models both ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To address this, we propose Spatio-Temporal OpenVocabulary Scene Graph (ST-OVSG), an open-vocabulary spatio-temporal scene graph designed for teleoperation.
- **p. 3 / III. METHODOLOGY - extractive body cue:** To address this, we propose ST-OVSG that integrates object nodes, spatial relations, and temporal correspondences.

## Source Evidence Cues

- **p. 4 / III. METHODOLOGY - extractive body cue:** The planner outputs a sequence of high-level actions π = (a1, . . . , aM) with grounded arguments (e.g., centroids and sizes), which are ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** User commands are used to query node features, filtering relevant nodes to form an ST-OVSG subgraph, which is then serialized into JSON and provided to ...
- **p. 2 / III. METHODOLOGY - extractive body cue:** Problem Formulation We aim to construct a temporally indexed, semantically enriched representation of dynamic 3D environments, enabling LVLM-based robot planner to plan action based on ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** Su is then serialized into a lightweight JSON-style description that lists, for each node, its class y, centroid c, size s, salient spatial relations, and ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** An image encoder Φv and a text encoder Φt (e.g., CLIP [27]) are adopted to extract masked visual features f img i = Φv(Irgb n ...
- **p. 2 / III. METHODOLOGY - extractive body cue:** In teleoperation settings, the LVLM planner operates remotely together with the robot, while a
- **Detected method headings:** III. METHODOLOGY (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | The planner outputs a sequence of high-level actions π = (a1, . . . , aM) with grounded arguments (e.g., centroids and ... | p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | User commands are used to query node features, filtering relevant nodes to form an ST-OVSG subgraph, which is then serialized into JSON ... | p. 3 (III. METHODOLOGY), p. 2 (III. METHODOLOGY) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | Problem Formulation We aim to construct a temporally indexed, semantically enriched representation of dynamic 3D environments, enabling LVLM-based robot planner to plan ... | p. 2 (III. METHODOLOGY), p. 4 (III. METHODOLOGY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / III. METHODOLOGY - extractive body cue:** However, when multiple candidate pairs overlap or are ambiguous, resolve them by minimizing a simple geometric cost.
- **p. 4 / III. METHODOLOGY - extractive body cue:** The cost is cspa j,k,n = wiou (1 -IoU(uj,k,n, zj,k,n)) + warea
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 4 (III. METHODOLOGY).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | planner, outputs, sequence, high-level, actions, grounded, arguments, centroids, sizes, parsed, skill, parameters, downstream, controllers | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | planner, outputs, sequence, high-level, actions, grounded, arguments, centroids, sizes, parsed | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | main, contributions, summarized, follows, ST-OVSG, novel, spatio-temporal, openvocabulary, scene, graph | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | However, when, multiple, candidate, pairs, overlap, ambiguous, resolve, them, minimizing | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / III. METHODOLOGY - extractive body cue:** The planner outputs a sequence of high-level actions π = (a1, . . . , aM) with grounded arguments (e.g., centroids and sizes), which are ...
- **p. 4 / III. METHODOLOGY - extractive body cue:** Crucially, because each frame-level graph Mn stores both its capture timestamp τn and estimated latency ∆Tn, the planner can retrieve the scene state aligned with ...
- **p. 2 / III. METHODOLOGY - extractive body cue:** Problem Formulation We aim to construct a temporally indexed, semantically enriched representation of dynamic 3D environments, enabling LVLM-based robot planner to plan action based on ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Based on the tn-1+∆t moment scene feedback, the local operator issues natural-language commands.
- **p. 3 / III. METHODOLOGY - extractive body cue:** Meanwhile, the remote environment can evolve significantly, creating a mismatch between the state visible to the operator when issuing a command and the state available ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** These commands are sent over the data network to the remote side, where ST-OVSG temporally aligns the local commands with the remote observations to compensate ...
- **p. 3 / III. METHODOLOGY - extractive body cue:** G1:N is constructed incrementally, the resulting time-stamped, open-vocabulary scene graph supports object retrieval across time, latencyaware instruction grounding, and long-horizon planning in dynamic scenes.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | These graphs are linked across frames using the Hungarian algorithm [8] [9], producing a 4D scene graph with spatial and temporal edges ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | Spatio-Temporal Scene Representation Given a time-ordered set of posed RGB-D frames D = {(Irgb n , Id n, ∆tn, τn)}N n=1 where ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | Spatio-Temporal Scene Representation Given a time-ordered set of posed RGB-D frames D = {(Irgb n , Id n, ∆tn, τn)}N n=1 where ... | hardware, batch and throughput |

## Training vs Inference

- training/inference separation PDF body cue not selected; no claim inferred

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** planner, outputs, sequence, high-level, actions, grounded, arguments, centroids, sizes, parsed, skill, parameters, downstream, controllers, User, commands, query, node, features, filtering.
- **Relevant PDF headings:** III. METHODOLOGY (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Unlike static benchmarks, these videos feature continuous scene evolution, where objects are moved, occluded, rotated, duplicated, or removed. | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Global / local decision | With ST-OVSG, the average similarity score is 0.1702, compared to 0.164 without STOVSG. | p. 6 (IV. EXPERIMENTS), p. 2 (3) Extensive experiments demonstrate that ST-OVSG ef) |
| Motion execution / recovery | Our method achieved a node accuracy of 74%, outperforming ConceptGraphs [7], while edge accuracy reached 67%, slightly lower than 1Edge precision corresponds ... | p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 3. Execution process of the proposed method in a task. Left: users provide a natural-language grasp-and-place instruction at the local side (issue at 5.5s ...
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Unlike static benchmarks, these videos feature continuous scene evolution, where objects are moved, occluded, rotated, duplicated, or removed.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** With ST-OVSG, the average similarity score is 0.1702, compared to 0.164 without STOVSG.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** These scenarios are intentionally adversarial for non-latency-aware planners, which only operate on the most recent frame without historical alignment.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Failure cases were dominated by residual identity switches under long occlusions, missed detections of small or subtle objects, and unstable temporal associations caused by motion ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** In practice, many predicted actions were semantically correct but expressed with different phrasing or level of detail, which lowers embedding-based similarity without indicating execution failure.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Because our representation is designed for openvocabulary settings, automated evaluation of nodes and edges is unreliable: object categories and relational boundaries under open vocabulary cannot ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 2 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 2 (III. METHODOLOGY), objective p. 4 (III. METHODOLOGY), p. 4 (III. METHODOLOGY), temporal p. 3 (III. METHODOLOGY), p. 3 (III. METHODOLOGY), p. 5 (IV. EXPERIMENTS), p. 2 (3) Extensive experiments demonstrate that ST-OVSG ef), p. 2 (III. METHODOLOGY), p. 4 (III. METHODOLOGY).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** The planner outputs a sequence of high-level actions π = (a1, . . . , aM) with grounded arguments (e.g., centroids and sizes), which are parsed into skill parameters for ... (p. 4, III. METHODOLOGY).
- **Objective/update evidence:** The cost is cspa j,k,n = wiou (1 -IoU(uj,k,n, zj,k,n)) + warea (p. 4, III. METHODOLOGY).
- **Temporal/runtime evidence:** These graphs are linked across frames using the Hungarian algorithm [8] [9], producing a 4D scene graph with spatial and temporal edges and latency tags. (p. 3, III. METHODOLOGY).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
