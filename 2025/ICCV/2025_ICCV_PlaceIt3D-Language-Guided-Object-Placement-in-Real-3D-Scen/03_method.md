# Method - PlaceIt3D: Language-Guided Object Placement in Real 3D Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Abdelreheem_PlaceIt3D_Language-Guided_Object_Placement_in_Real_3D_Scenes_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Abdelreheem_PlaceIt3D_Language-Guided_Object_Placement_in_Real_3D_Scenes_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 6 (4.4. Losses), p. 6 (4.4. Losses)): We use a combination of Binary Cross Entropy (BCE) and Dice [43] losses when comparing a ground truth mask ¯ M with a predicted mask M, so \Lo _{ se ...

## Method Body Digest

- **p. 6 / 4.4. Losses - extractive body cue:** We use a combination of Binary Cross Entropy (BCE) and Dice [43] losses when comparing a ground truth mask ¯ M with a predicted mask ...
- **p. 6 / 4.4. Losses - extractive body cue:** Finally, our total loss is defined as \Lo = \Lo _ {seg}(\bar {\mas k }_{l oc}, \mask _{loc}) + \Lo _{rot} + \Lo _{seg}(\bar {\mask ...
- **p. 1 / 1. Introduction - extractive body cue:** As in the shoe example, the goal is to find a valid placement of the object among multiple configurations that satisfy the instruction.
- **p. 1 / 1. Introduction - extractive body cue:** At two to three years old, neurotypical children learn to follow two-step instructions like "Get your shoes and put them on the shelf" [42].
- **p. 2 / 1. Introduction - extractive body cue:** Among the valid options, the model must follow the user's stated intent rather than default to common sense priors [36, 56].
- **p. 2 / 1. Introduction - extractive body cue:** The asset's size and shape restrict feasible placements; given the same scene and instruction, a large object has fewer valid locations than a small one.
- **p. 6 / 4.4. Losses - extractive body cue:** (2) The loss for the rotation prediction is given by \m a thca l {L}_ {rot} = \text {BCE}(\bar {\mask }_{rot}, \mask _{rot}), (3) where ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive body cue:** To advance research in this area, we make three key contributions, summarized here: • We introduce PLACEIT3D-benchmark for languageguided placement with 3,500 evaluation examples, each ...
- **p. 2 / 1. Introduction - extractive body cue:** Like the benchmark, it uses ScanNet scenes and PartObjaverse-Tiny assets. • We propose PLACEWIZARD, a proto-method for this task built on recent 3D LLMs [25].
- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we focus on the novel task of languageguided 3D object placement in a reconstructed real 3D scene.

## Source Evidence Cues

- **p. 6 / 4.4. Losses - extractive body cue:** We use a combination of Binary Cross Entropy (BCE) and Dice [43] losses when comparing a ground truth mask ¯ M with a predicted mask ...
- **p. 6 / 4.4. Losses - extractive body cue:** Finally, our total loss is defined as \Lo = \Lo _ {seg}(\bar {\mas k }_{l oc}, \mask _{loc}) + \Lo _{rot} + \Lo _{seg}(\bar {\mask ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | We use a combination of Binary Cross Entropy (BCE) and Dice [43] losses when comparing a ground truth mask ¯ M with ... | p. 6 (4.4. Losses), p. 6 (4.4. Losses) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Finally, our total loss is defined as \Lo = \Lo _ {seg}(\bar {\mas k }_{l oc}, \mask _{loc}) + \Lo _{rot} + ... | p. 6 (4.4. Losses) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | We use a combination of Binary Cross Entropy (BCE) and Dice [43] losses when comparing a ground truth mask ¯ M with ... | p. 6 (4.4. Losses) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / 4.4. Losses - extractive body cue:** We use a combination of Binary Cross Entropy (BCE) and Dice [43] losses when comparing a ground truth mask ¯ M with a predicted mask ...
- **p. 6 / 4.4. Losses - extractive body cue:** Finally, our total loss is defined as \Lo = \Lo _ {seg}(\bar {\mas k }_{l oc}, \mask _{loc}) + \Lo _{rot} + \Lo _{seg}(\bar {\mask ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 6 (4.4. Losses), p. 6 (4.4. Losses).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | shoe, example, goal, find, valid, placement, object, among, multiple, configurations, satisfy, instruction, three, years | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | shoe, example, goal, find, valid, placement, object, among, multiple, configurations | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | advance, research, area, make, three, contributions, summarized, here, introduce, PLACEIT3D-benchmark | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | combination, Binary, Cross, Entropy, BCE, Dice, losses, when, comparing, ground | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1. Introduction - extractive body cue:** As in the shoe example, the goal is to find a valid placement of the object among multiple configurations that satisfy the instruction.
- **p. 1 / 1. Introduction - extractive body cue:** At two to three years old, neurotypical children learn to follow two-step instructions like "Get your shoes and put them on the shelf" [42].
- **p. 2 / 1. Introduction - extractive body cue:** Among the valid options, the model must follow the user's stated intent rather than default to common sense priors [36, 56].
- **p. 2 / 1. Introduction - extractive body cue:** The asset's size and shape restrict feasible placements; given the same scene and instruction, a large object has fewer valid locations than a small one.
- **p. 6 / 4.4. Losses - extractive body cue:** (2) The loss for the rotation prediction is given by \m a thca l {L}_ {rot} = \text {BCE}(\bar {\mask }_{rot}, \mask _{rot}), (3) where ...
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | At two to three years old, neurotypical children learn to follow two-step instructions like "Get your shoes and put them on the ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | The asset is always placed on a horizontal surface, and only the yaw angle is considered, i.e. rotation around the vertical axis. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not recovered | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / 3.2.2. Benchmark metrics - extractive body cue:** To evaluate placement performance, we compute metrics that capture constraint validity overall and by subgroup: • Global Constraint Accuracy: The percentage of all constraints (across ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** combination, Binary, Cross, Entropy, BCE, Dice, losses, when, comparing, ground, truth, mask, predicted, text, Finally, total, loss, defined, shoe, example.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | PLACEIT3D-dataset-full has ∼4M examples: the 565 scenes x 140 objects x 50 prompts. | p. 5 (3.2.3. Benchmark statistics), p. 4 (3.2.3. Benchmark statistics) |
| Semantic / temporal fusion | Our method, row G, consistently outperforms both baselines across all overall evaluation metrics. | p. 7 (5.1. Quantitative results), p. 7 (5.1. Quantitative results) |
| Robot query / planning handoff | The inclusion of the anchor prediction head as an auxiliary sub-task also improves performance (row E vs row D). | p. 8 (5.1.1. Ablations), p. 8 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / 5.1.1. Ablations - extractive body cue:** We describe the different variants below.
- **p. 7 / 5.1.1. Ablations - extractive body cue:** This variant uses our proposed uniform spatial pooling approach instead of the original superpoints pooling.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. PLACEWIZARD overview. A point encoder extracts features from the 3D scene, which are then complemented with positional embeddings. Spatial pooling reduces feature dimensions, ...
- **p. 5 / 3.2.3. Benchmark statistics - extractive body cue:** For the visibility constraint we use the same procedure as the benchmark, but use two approximations for efficiency: the asset is replaced by its bounding ...
- **p. 8 / 6. Limitations and Future Work - extractive body cue:** Our novel task formulation currently has several limitations.
- **p. 8 / 6. Limitations and Future Work - extractive body cue:** Despite these limitations, we believe our work lays the groundwork for further research in this area.
- **p. 7 / 5.1. Quantitative results - extractive body cue:** Due to its frequent failure to accurately detect floor regions, we substitute in ground truth floor masks, while other anchor objects are selected based on ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 6 (4.4. Losses), p. 6 (4.4. Losses), objective p. 6 (4.4. Losses), p. 6 (4.4. Losses), temporal p. 1 (1. Introduction), p. 3 (3. Language-Guided 3D Object Placement), p. 3 (3.1. Physical plausibility and language constraints), p. 5 (3.2.3. Benchmark statistics), p. 5 (3.2.3. Benchmark statistics), p. 6 (4.2. Asset encoding).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
