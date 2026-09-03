# Method - VLMaps: Visual-Language Maps for Robot Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2210.05714; PDF retrieval source: https://arxiv.org/pdf/2210.05714. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (III. METHOD), p. 2 (III. METHOD), p. 4 (III. METHOD), p. 2 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD)): Zero-Shot Spatial Goal Navigation from Language In this section, we describe our approach to long-horizon (spatial) goal navigation, given a set of landmark descriptions specified by natural language instructions such ...

## Method Body Digest

- **p. 4 / III. METHOD - extractive body cue:** Zero-Shot Spatial Goal Navigation from Language In this section, we describe our approach to long-horizon (spatial) goal navigation, given a set of landmark descriptions specified ...
- **p. 2 / III. METHOD - extractive body cue:** We propose VLMaps as one such representation, which can be constructed using off-the-shelf visual-language models (VLMs) and standard 3D reconstruction libraries.
- **p. 4 / III. METHOD - extractive body cue:** The robot code can express functions or logic structures (if-then-else statements or for/while loops) and parameterize API calls (e.g., robot.move_to(target_name) or robot.turn(degrees).
- **p. 2 / III. METHOD - extractive body cue:** The LSeg visual encoder maps an image such that the embedding of each pixel lies in the CLIP feature space.
- **p. 3 / III. METHOD - extractive body cue:** LSeg Text Encoder (Frozen) "chair", "table", "floor", "wall", ...
- **p. 3 / III. METHOD - extractive body cue:** Therefore, the resulting features contain the averaged embeddings from multiple views of the same object.
- **p. 3 / III. METHOD - extractive body cue:** By applying the argmax operator along the row direction to S and reshaping the resulting vector to shape ¯H× ¯W, we get the final segmentation ...
- **p. 3 / III. METHOD - extractive body cue:** Open-Vocabulary Label Set ( entries) VLMap Creation LSeg Visual Encoder (Frozen) Input Depth Camera Pose Global Point Cloud Input Image Each Point Top-down Projection VLMap ...

## Design Rationale

- **p. 2 / III. METHOD - extractive body cue:** We propose VLMaps as one such representation, which can be constructed using off-the-shelf visual-language models (VLMs) and standard 3D reconstruction libraries.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Extensive experiments show that using VLMaps enables more effective long-horizon multi-object goal navigation than baseline alternatives, e.g., CoW [12] and LM-Nav [13], and, in particular, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** A key aspect of VLMaps is that they are spatial, which enables them to: • Localize spatial goals beyond object-centric ones, e.g., "in between the ...

## Source Evidence Cues

- **p. 4 / III. METHOD - extractive body cue:** Zero-Shot Spatial Goal Navigation from Language In this section, we describe our approach to long-horizon (spatial) goal navigation, given a set of landmark descriptions specified ...
- **p. 2 / III. METHOD - extractive body cue:** We propose VLMaps as one such representation, which can be constructed using off-the-shelf visual-language models (VLMs) and standard 3D reconstruction libraries.
- **p. 4 / III. METHOD - extractive body cue:** The robot code can express functions or logic structures (if-then-else statements or for/while loops) and parameterize API calls (e.g., robot.move_to(target_name) or robot.turn(degrees).
- **p. 2 / III. METHOD - extractive body cue:** The LSeg visual encoder maps an image such that the embedding of each pixel lies in the CLIP feature space.
- **p. 3 / III. METHOD - extractive body cue:** LSeg Text Encoder (Frozen) "chair", "table", "floor", "wall", ...
- **p. 3 / III. METHOD - extractive body cue:** Therefore, the resulting features contain the averaged embeddings from multiple views of the same object.
- **Detected method headings:** III. METHOD (p. 2)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | Zero-Shot Spatial Goal Navigation from Language In this section, we describe our approach to long-horizon (spatial) goal navigation, given a set of ... | p. 4 (III. METHOD), p. 2 (III. METHOD) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | We propose VLMaps as one such representation, which can be constructed using off-the-shelf visual-language models (VLMs) and standard 3D reconstruction libraries. | p. 2 (III. METHOD), p. 4 (III. METHOD) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | The robot code can express functions or logic structures (if-then-else statements or for/while loops) and parameterize API calls (e.g., robot.move_to(target_name) or robot.turn(degrees). | p. 4 (III. METHOD), p. 2 (III. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / III. METHOD - extractive body cue:** By applying the argmax operator along the row direction to S and reshaping the resulting vector to shape ¯H× ¯W, we get the final segmentation ...
- **p. 3 / III. METHOD - extractive body cue:** Open-Vocabulary Label Set ( entries) VLMap Creation LSeg Visual Encoder (Frozen) Input Depth Camera Pose Global Point Cloud Input Image Each Point Top-down Projection VLMap ...
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 3 (III. METHOD), p. 3 (III. METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Zero-Shot, Spatial, Goal, Navigation, Language, section, describe, long-horizon, given, landmark, descriptions, specified, natural, instructions | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Zero-Shot, Spatial, Goal, Navigation, Language, section, describe, long-horizon, given, landmark | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | VLMaps, representation, constructed, off-the-shelf, visual-language, models, VLMs, standard, reconstruction, libraries | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | applying, argmax, operator, along, direction, reshaping, resulting, vector, shape, final | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / III. METHOD - extractive body cue:** Zero-Shot Spatial Goal Navigation from Language In this section, we describe our approach to long-horizon (spatial) goal navigation, given a set of landmark descriptions specified ...
- **p. 3 / III. METHOD - extractive body cue:** Open-Vocabulary Label Set ( entries) VLMap Creation LSeg Visual Encoder (Frozen) Input Depth Camera Pose Global Point Cloud Input Image Each Point Top-down Projection VLMap ...
- **p. 4 / III. METHOD - extractive body cue:** In this work, we re-purpose these models for mobile robot planning, by priming them with several input examples of natural language commands (formatted as comments) ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** When paired with large language models (LLMs) in Socratic fashion [14], VLMaps can translate natural language instructions into a sequence of open-vocabulary goals, directly localized ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Classic methods for robot navigation [4], [5] build geometric maps for path planning and can parse goals from natural language commands [6], [7], but struggle ...
- **p. 3 / III. METHOD - extractive body cue:** Each element Rij represents the label index of the input language list L at the grid map location (i,j).
- **p. 2 / III. METHOD - extractive body cue:** To build the map, we, for each RGB-D frame, back-project all the depth pixels u=(u,v) to form a local depth point cloud that we transform ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | To evaluate the long-horizon navigation capabilities of the agents, we compute the success rate (SR) of continuously reaching one to four subgoals ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | The only assumption we make is access to odometry, which is readily available from RGB-D SLAM systems and enables us to build ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | Among the successful trials, six of them are spatial goals like "move between the chair and the wooden box" or "move to ... | hardware, batch and throughput |

## Training vs Inference

- training/inference separation PDF body cue not selected; no claim inferred

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Zero-Shot, Spatial, Goal, Navigation, Language, section, describe, long-horizon, given, landmark, descriptions, specified, natural, instructions, move, first, left, side, counter, then.
- **Relevant PDF headings:** III. METHOD (p. 2).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | We use the Habitat simulator [45] with the Matterport3D dataset [46] for the evaluation of multi-object and spatial goal navigation tasks. | p. 4 (IV. EXPERIMENTS), p. 4 (IV. EXPERIMENTS) |
| Global / local decision | Our method outperforms other baselines in this task. | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| Motion execution / recovery | Subgoals in a Row 1 2 3 4 LM-Nav [13] 5 5 0 0 CoW [12] 33 5 0 0 CLIP Map ... | p. 5 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: VLMaps is a spatial map representation in which pretrained visual- language model features are fused into a 3D reconstruction of the physical world. ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: VLMaps enables a robot to perform complex zero-shot spatial goal navigation tasks given natural language commands, without additional data collection or model finetuning. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 3: System overview. A VLMap is created by fusing pretrained visual-language features into the reconstruction of the environment to enable visual-spatial-language-based reasoning. By providing ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We observe that failure cases are caused by: 1) inaccurate depth, which introduces noise during the map creation and decreases the landmark indexing accuracy and ...
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 2: VLMaps enables a robot to perform complex zero-shot spatial goal navigation tasks given natural language commands, without additional data collection or model finetuning. ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** This is because when the drone does not have access to a customized obstacle map, it fails to benefit from flying over ground objects to ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (III. METHOD), p. 2 (III. METHOD), p. 4 (III. METHOD), p. 2 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD), objective p. 3 (III. METHOD), p. 3 (III. METHOD), temporal p. 5 (IV. EXPERIMENTS), p. 2 (III. METHOD), p. 2 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (IV. EXPERIMENTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (11 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Open-Vocabulary Label Set ( entries) VLMap Creation LSeg Visual Encoder (Frozen) Input Depth Camera Pose Global Point Cloud Input Image Each Point Top-down Projection VLMap Per-Pixel Embedding Pixel-Text Similarity Argmax ... (p. 3, III. METHOD).
- **Objective/update evidence:** The LSeg visual encoder maps an image such that the embedding of each pixel lies in the CLIP feature space. (p. 2, III. METHOD).
- **Temporal/runtime evidence:** To evaluate the long-horizon navigation capabilities of the agents, we compute the success rate (SR) of continuously reaching one to four subgoals in a sequence, shown in Tab. (p. 5, IV. EXPERIMENTS).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
