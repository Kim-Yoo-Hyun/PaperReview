# Method - GroundFlow: A Plug-in Module for Temporal Reasoning on 3D Point Cloud Sequential Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Lin_GroundFlow_A_Plug-in_Module_for_Temporal_Reasoning_on_3D_Point_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Lin_GroundFlow_A_Plug-in_Module_for_Temporal_Reasoning_on_3D_Point_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 5 (3.3. Training Objective), p. 5 (3.3. Training Objective)): Following the SG3D benchmark [52], we use the same cross-entropy loss to optimize the dual-stream model and the query-based model.

## Method Body Digest

- **p. 5 / 3.3. Training Objective - extractive PDF cue:** Following the SG3D benchmark [52], we use the same cross-entropy loss to optimize the dual-stream model and the query-based model.
- **p. 5 / 3.3. Training Objective - extractive PDF cue:** In addition to the loss of token predictions when pre-trained on other datasets, an extra cross-entropy loss is incorporated to fine-tune the model on SG3D ...
- **p. 5 / 3.3. Training Objective - extractive PDF cue:** As defined in Equation 7, the loss compares the predicted object score f(P, S) and the ground truth score O.
- **p. 1 / 1. Introduction - extractive PDF cue:** As shown, GroundFlow module's output ˆJt will be treated as input in the next step t + 1. studied task that requires the agent to ...
- **p. 2 / 1. Introduction - extractive PDF cue:** This framework sequentially takes each step instruction and processes only the current step instruction as input rather than handling all prior text instructions simultaneously.
- **p. 2 / 1. Introduction - extractive PDF cue:** As shown in Figure 1, 3DVG methods typically process all text instructions as a single, undifferentiated input, which works for traditional visual grounding tasks but ...
- **p. 1 / 1. Introduction - extractive PDF cue:** 3D Visual Grounding (3DVG) [13, 42, 48, 49, 53] is a widely Previous Ours (GroundFlow) T : Task Description P : 3D Point Cloud St ...
- **p. 5 / 3.3. Training Objective - extractive PDF cue:** For the 3D LLM LEO [24], which is state-ofthe-art method in SG3D benchmark, we follow the original approach.

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** In summary, we make the following contributions: • We propose the GroundFlow module with a recurrent framework, which can be integrated into previous 3DVG baselines ...
- **p. 2 / 1. Introduction - extractive PDF cue:** In addition, we propose GroundFlow module, which can be built on top of the existing 3DVG methods to perform temporal fusion with previous step embeddings, ...
- **p. 5 / 3.3. Training Objective - extractive PDF cue:** Detailed illustration of Memory component in GroundFlow, which enables the module to extract relevant information of both short-term ( ˆJt-1) and long-term ( ˆJm) effectively.

## Source Evidence Cues

- **p. 5 / 3.3. Training Objective - extractive PDF cue:** Following the SG3D benchmark [52], we use the same cross-entropy loss to optimize the dual-stream model and the query-based model.
- **p. 5 / 3.3. Training Objective - extractive PDF cue:** In addition to the loss of token predictions when pre-trained on other datasets, an extra cross-entropy loss is incorporated to fine-tune the model on SG3D ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Geometry / pose extraction | image·depth·point input에서 spatial state를 만든다 | RGB/RGB-D, point cloud, camera pose 또는 multi-view input | depth, pose, correspondence, point, mesh, Gaussian 또는 feature representation을 추정 | geometry/map/pose | Following the SG3D benchmark [52], we use the same cross-entropy loss to optimize the dual-stream model and the query-based model. | p. 5 (3.3. Training Objective), p. 5 (3.3. Training Objective) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | In addition to the loss of token predictions when pre-trained on other datasets, an extra cross-entropy loss is incorporated to fine-tune the ... | p. 5 (3.3. Training Objective) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | Following the SG3D benchmark [52], we use the same cross-entropy loss to optimize the dual-stream model and the query-based model. | p. 5 (3.3. Training Objective) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 5 / 3.3. Training Objective - extractive PDF cue:** As defined in Equation 7, the loss compares the predicted object score f(P, S) and the ground truth score O.
- **p. 5 / 3.3. Training Objective - extractive PDF cue:** In addition to the loss of token predictions when pre-trained on other datasets, an extra cross-entropy loss is incorporated to fine-tune the model on SG3D ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 5 (3.3. Training Objective), p. 5 (3.3. Training Objective).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | GroundFlow, module, output, will, treated, input, next, step, studied, task, requires, agent, locate, target | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | GroundFlow, module, output, will, treated, input, next, step, studied, task | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | summary, make, following, contributions, GroundFlow, module, recurrent, framework, integrated, previous | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | defined, Equation, loss, compares, predicted, object, score, ground, truth, addition | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1. Introduction - extractive PDF cue:** As shown, GroundFlow module's output ˆJt will be treated as input in the next step t + 1. studied task that requires the agent to ...
- **p. 2 / 1. Introduction - extractive PDF cue:** This framework sequentially takes each step instruction and processes only the current step instruction as input rather than handling all prior text instructions simultaneously.
- **p. 2 / 1. Introduction - extractive PDF cue:** As shown in Figure 1, 3DVG methods typically process all text instructions as a single, undifferentiated input, which works for traditional visual grounding tasks but ...
- **p. 1 / 1. Introduction - extractive PDF cue:** 3D Visual Grounding (3DVG) [13, 42, 48, 49, 53] is a widely Previous Ours (GroundFlow) T : Task Description P : 3D Point Cloud St ...
- **p. 5 / 3.3. Training Objective - extractive PDF cue:** For the 3D LLM LEO [24], which is state-ofthe-art method in SG3D benchmark, we follow the original approach.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | In addition, we propose GroundFlow module, which can be built on top of the existing 3DVG methods to perform temporal fusion with ... | episode/sequence/action-chunk boundary |
| Rate / latency | per-frame/streaming inference와 downstream policy/control rate가 분리된다. | For task accuracy, a sample is considered correct if the predicted sequence of objects for each step matches the ground-truth sequence. | Hz/fps, inference time and control rate |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | In addition, we propose GroundFlow module, which can be built on top of the existing 3DVG methods to perform temporal fusion with ... | window and reset |
| Compute | 3D reconstruction/fusion, point/feature memory와 query cost가 latency를 결정한다. | The models are trained for 50 epochs with batch size of 32 and evaluated on the last epoch using evaluation split of ... | hardware, batch and throughput |

## Training vs Inference

- **p. 5 / 3.3. Training Objective - extractive PDF cue:** In addition to the loss of token predictions when pre-trained on other datasets, an extra cross-entropy loss is incorporated to fine-tune the model on SG3D ...
- **p. 5 / 4.2. Implementation Details - extractive PDF cue:** Due to GPU memory constraints, the batch size for LEO is reduced to 16.
- **p. 5 / 4.2. Implementation Details - extractive PDF cue:** The models are trained for 50 epochs with batch size of 32 and evaluated on the last epoch using evaluation split of the SG3D benchmark.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Following, SG3D, benchmark, same, cross-entropy, loss, optimize, dual-stream, model, query-based, addition, token, predictions, when, pre-trained, other, datasets, extra, incorporated, fine-tune.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | The benchmark utilizes real-world scenes from the SceneVerse [26], incorporating indoor scans from 5 different datasets - ScanNet [11], 3RScan [40], MultiScan ... | p. 5 (4.1. Dataset and Evaluation Metrics), p. 6 (4.2. Implementation Details) |
| Semantic / temporal fusion | However, the 3DVG methods combined with our proposed GroundFlow module outperform LEO across all five datasets, setting new state-of-the-art performance on SG3D ... | p. 6 (4.3. Comparison on SG3D Benchmark), p. 5 (4.2. Implementation Details) |
| Robot query / planning handoff | On the other hand, significant performance improvements can be observed when these models are integrated with GroundFlow, as shown in the rows ... | p. 6 (4.3. Comparison on SG3D Benchmark), p. 6 (4.3. Comparison on SG3D Benchmark) |

## Failure and Ablation Link

- **p. 7 / 4.4. Ablation Study - extractive PDF cue:** In Table 3, the performance without one of the memory parts is presented in the first and second rows.
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Detailed illustration of Memory component in Ground- Flow, which enables the module to extract relevant information of both short-term ( ˆJt-1) and long-term ...
- **p. 6 / 4.3. Comparison on SG3D Benchmark - extractive PDF cue:** Furthermore, the state-of-theart 3D large language model, LEO, after fine-tuning on the SG3D benchmark is also compared.
- **p. 6 / 4.3. Comparison on SG3D Benchmark - extractive PDF cue:** In fine-tuning stage, LEO predicts a special [GRD]t token at each step t, which is concatenated with object tokens and passed to the grounding head ...
- **p. 7 / 4.4. Ablation Study - extractive PDF cue:** Improvements after GroundFlow module is integrated in terms of task accuracy of 3D-VisTA and PQ3D across different step count subsets. various settings of short-term and ...
- **p. 8 / 4.5. Qualitative Visualization - extractive PDF cue:** These results highlight that the memory component in GroundFlow enables the model to retain important context over time, allowing it to accurately retrieve and apply ...
- **p. 6 / 4.3. Comparison on SG3D Benchmark - extractive PDF cue:** Their degraded performance is particularly reflected in their overall task accuracy, with three of the models are falling below 30%.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 5 (3.3. Training Objective), p. 5 (3.3. Training Objective), objective p. 5 (3.3. Training Objective), p. 5 (3.3. Training Objective), temporal p. 2 (1. Introduction), p. 5 (4.1. Dataset and Evaluation Metrics), p. 6 (4.3. Comparison on SG3D Benchmark), p. 7 (4.4. Ablation Study), p. 7 (4.4. Ablation Study), p. 8 (4.5. Qualitative Visualization).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
