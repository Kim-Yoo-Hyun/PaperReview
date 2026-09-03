# Method - FROSS: Faster-Than-Real-Time Online 3D Semantic Scene Graph Generation from RGB-D Images

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (5 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Hou_FROSS_Faster-Than-Real-Time_Online_3D_Semantic_Scene_Graph_Generation_from_RGB-D_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Hou_FROSS_Faster-Than-Real-Time_Online_3D_Semantic_Scene_Graph_Generation_from_RGB-D_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (8. Statistics of the ReplicaSSG Dataset)): Evaluation results of two 2D SG generation models across three datasets. ‘RT-DETR+EGTR' represents the EGTR model with RT-DETR as its object detector backbone.

## Method Body Digest

- **p. 3 / 8. Statistics of the ReplicaSSG Dataset - extractive body cue:** Evaluation results of two 2D SG generation models across three datasets. ‘RT-DETR+EGTR' represents the EGTR model with RT-DETR as its object detector backbone.
- **p. 3 / 8. Statistics of the ReplicaSSG Dataset - extractive body cue:** All relationship metrics are evaluated with graph constraints as described in [38].
- **p. 1 / Body text (section not recovered) - extractive body cue:** FROSS: Faster-than-Real-Time Online 3D Semantic Scene Graph Generation from RGB-D Images Supplementary Material
- **p. 2 / 8. Statistics of the ReplicaSSG Dataset - extractive body cue:** The statistics of the proposed ReplicaSSG Dataset are presented in Figures 6-9.

## Design Rationale

- **p. 2 / 7.3. 2D Scene Graph Generation Performance - extractive body cue:** In this section, we present the evaluation of two models: the original EGTR [12] 2D SG generation model and our modified version employed in FROSS, ...

## Source Evidence Cues

- **p. 3 / 8. Statistics of the ReplicaSSG Dataset - extractive body cue:** Evaluation results of two 2D SG generation models across three datasets. ‘RT-DETR+EGTR' represents the EGTR model with RT-DETR as its object detector backbone.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | Evaluation results of two 2D SG generation models across three datasets. ‘RT-DETR+EGTR' represents the EGTR model with RT-DETR as its object detector ... | p. 3 (8. Statistics of the ReplicaSSG Dataset) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | Evaluation results of two 2D SG generation models across three datasets. ‘RT-DETR+EGTR' represents the EGTR model with RT-DETR as its object detector ... | p. 3 (8. Statistics of the ReplicaSSG Dataset) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | Evaluation results of two 2D SG generation models across three datasets. ‘RT-DETR+EGTR' represents the EGTR model with RT-DETR as its object detector ... | p. 3 (8. Statistics of the ReplicaSSG Dataset) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / 8. Statistics of the ReplicaSSG Dataset - extractive body cue:** All relationship metrics are evaluated with graph constraints as described in [38].
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 3 (8. Statistics of the ReplicaSSG Dataset).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | FROSS, Faster-than-Real-Time, Online, Semantic, Scene, Graph, Generation, RGB-D, Images, Supplementary, Material, statistics, ReplicaSSG, Dataset | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | FROSS, Faster-than-Real-Time, Online, Semantic, Scene, Graph, Generation, RGB-D, Images, Supplementary | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | section, present, evaluation, models, original, EGTR, generation, model, modified, version | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | relationship, metrics, evaluated, graph, constraints, described | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / Body text (section not recovered) - extractive body cue:** FROSS: Faster-than-Real-Time Online 3D Semantic Scene Graph Generation from RGB-D Images Supplementary Material
- **p. 2 / 8. Statistics of the ReplicaSSG Dataset - extractive body cue:** The statistics of the proposed ReplicaSSG Dataset are presented in Figures 6-9.
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | FROSS: Faster-than-Real-Time Online 3D Semantic Scene Graph Generation from RGB-D Images Supplementary Material | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | More specifically, Figure 6 and 7 illustrate the occurrence frequency of objects and relationships across all categories in the dataset. | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not recovered | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Evaluation, generation, models, across, three, datasets, RT-DETR, EGTR, represents, model, object, detector, backbone, relationship, metrics, evaluated, graph, constraints, described, FROSS.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Qualitative results of FROSS on four scenes in the ReplicaSSG dataset. | p. 2 (7.1. Object and Predicate Performance per Class), p. 5 (8. Statistics of the ReplicaSSG Dataset) |
| Global / local decision | The per-class performance comparison of FROSS and other baselines is presented in Tables 6 and 7. | p. 1 (7.1. Object and Predicate Performance per Class), p. 1 (7.1. Object and Predicate Performance per Class) |
| Motion execution / recovery | The above observations reveal that the integration of RT-DETR as the object detection backbone results in substantial processing efficiency improvements, with only ... | p. 2 (7.3. 2D Scene Graph Generation Performance), p. 2 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 2 / 7.3. 2D Scene Graph Generation Performance - extractive body cue:** The latter replaces the object detection backbone in the original EGTR with RT-DETR [44] object detector.
- **p. 1 / 6. Detailed Evaluation Metric - extractive body cue:** The only difference is the exclusion of the ‘none' relationship category, as FROSS does not predict it.
- **p. 1 / 7.1. Object and Predicate Performance per Class - extractive body cue:** While addressing this issue could potentially enhance FROSS's performance, we leave it as future work, as class imbalance is not the primary focus of this ...
- **p. 2 / 7.2. Additional Qualitative Results - extractive body cue:** These results further demonstrate FROSS's robustness in diverse scene conditions.
- **p. 2 / 7.2. Additional Qualitative Results - extractive body cue:** Misclassified objects are likely caused by occlusions from certain viewpoints or unusual viewing angles.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (8. Statistics of the ReplicaSSG Dataset), objective p. 3 (8. Statistics of the ReplicaSSG Dataset), temporal p. 1 (Body text (section not recovered)), p. 2 (8. Statistics of the ReplicaSSG Dataset), p. 4 (8. Statistics of the ReplicaSSG Dataset).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
