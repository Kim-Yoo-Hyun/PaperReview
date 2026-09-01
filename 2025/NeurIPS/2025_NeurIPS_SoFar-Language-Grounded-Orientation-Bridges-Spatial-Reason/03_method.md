# Method - SoFar: Language-Grounded Orientation Bridges Spatial Reasoning and Object Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (46 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=kmv7yg6QXv; PDF retrieval source: https://openreview.net/pdf/44ce67ddf7a771b623a5a1cba738c147c2617eb1.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 5 (1 Introduction)): For the 3D point clouds, we follow [26, 136, 89] to first sample Ns seed points using farthest point sampling (FPS) and then group inputs with KNN for point feature ...

## Method Body Digest

- **p. 4 / 1 Introduction - extractive PDF cue:** For the 3D point clouds, we follow [26, 136, 89] to first sample Ns seed points using farthest point sampling (FPS) and then group inputs ...
- **p. 4 / 1 Introduction - extractive PDF cue:** 2.3 PointSO: A Cross-Modal 3D Transformer for Semantic Orientation Prediction We introduce PointSO, a plain Transformer-based architecture [114] with cross-modal 3D-language fusion as our orientation ...
- **p. 5 / 1 Introduction - extractive PDF cue:** Position & Orientation Information Extraction Given a language query Q, we first prompt a visionlanguage model FVLM to extract a task-relevant set of object phrases ...
- **p. 3 / 1 Introduction - extractive PDF cue:** To support this, we introduce OrienText300K, a curated dataset of 3D models annotated with diverse language-guided orientation labels.
- **p. 3 / 1 Introduction - extractive PDF cue:** In summary, we propose Semantic Orientation as a new representation that bridges spatial reasoning and robotic manipulation, enabling open-vocabulary, template-free orientation understanding for unseen objects.
- **p. 5 / 1 Introduction - extractive PDF cue:** 3.1 Scene Graph with 6-DoF Information To integrate both the positional & orientational interaction relationships of objects, we use a scene graph with 6-DoF information ...
- **p. 2 / 1 Introduction - extractive PDF cue:** To this end, we design both the model architecture and the dataset accordingly.
- **p. 4 / 1 Introduction - extractive PDF cue:** The optimization is to minimize the negative cosine similarity Lcos(v, k) = 1 - v·k ∥v∥·∥k∥between predicted and the ground truth semantic orientations: min θSO ...

## Design Rationale

- **p. 2 / 1 Introduction - extractive PDF cue:** We propose PointSO, a generalizable cross-modal 3D Transformer [114, 26, 89, 91] for semantic orientation prediction.
- **p. 2 / 1 Introduction - extractive PDF cue:** In addition, we introduce Open6DOR V2, a large-scale benchmark for 6-DoF object rearrangement in simulation, which supports both open-loop and closed-loop control.
- **p. 3 / 1 Introduction - extractive PDF cue:** Finally, we present two new benchmarks, Open6DOR V2 and 6-DoF SpatialBench, to evaluate 6-DoF rearrangement and spatial reasoning.

## Source Evidence Cues

- **p. 4 / 1 Introduction - extractive PDF cue:** For the 3D point clouds, we follow [26, 136, 89] to first sample Ns seed points using farthest point sampling (FPS) and then group inputs ...
- **p. 4 / 1 Introduction - extractive PDF cue:** 2.3 PointSO: A Cross-Modal 3D Transformer for Semantic Orientation Prediction We introduce PointSO, a plain Transformer-based architecture [114] with cross-modal 3D-language fusion as our orientation ...
- **p. 5 / 1 Introduction - extractive PDF cue:** Position & Orientation Information Extraction Given a language query Q, we first prompt a visionlanguage model FVLM to extract a task-relevant set of object phrases ...
- **p. 3 / 1 Introduction - extractive PDF cue:** To support this, we introduce OrienText300K, a curated dataset of 3D models annotated with diverse language-guided orientation labels.
- **p. 3 / 1 Introduction - extractive PDF cue:** In summary, we propose Semantic Orientation as a new representation that bridges spatial reasoning and robotic manipulation, enabling open-vocabulary, template-free orientation understanding for unseen objects.
- **p. 5 / 1 Introduction - extractive PDF cue:** 3.1 Scene Graph with 6-DoF Information To integrate both the positional & orientational interaction relationships of objects, we use a scene graph with 6-DoF information ...
- **p. 2 / 1 Introduction - extractive PDF cue:** To this end, we design both the model architecture and the dataset accordingly.
- **Detected method headings:** 0.63 Method (p. 29)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | For the 3D point clouds, we follow [26, 136, 89] to first sample Ns seed points using farthest point sampling (FPS) and ... | p. 4 (1 Introduction), p. 4 (1 Introduction) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | 2.3 PointSO: A Cross-Modal 3D Transformer for Semantic Orientation Prediction We introduce PointSO, a plain Transformer-based architecture [114] with cross-modal 3D-language fusion ... | p. 4 (1 Introduction), p. 5 (1 Introduction) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Position & Orientation Information Extraction Given a language query Q, we first prompt a visionlanguage model FVLM to extract a task-relevant set ... | p. 5 (1 Introduction), p. 3 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / 1 Introduction - extractive PDF cue:** The optimization is to minimize the negative cosine similarity Lcos(v, k) = 1 - v·k ∥v∥·∥k∥between predicted and the ground truth semantic orientations: min θSO ...
- **p. 2 / 1 Introduction - extractive PDF cue:** These annotations are from Objaverse [20] and generated automatically by prompting GPT-4o [48] with rich semantic queries covering both intra-object spatial reasoning and inter-object manipulation ...
- **p. 6 / 1 Introduction - extractive PDF cue:** 77.1 70.4 33.3 4.2 44.4 3.7 43.3 77.1 63.0 30.6 12.5 50.0 11.1 45.0 81.3 81.5 44.4 20.8 50.0 22.2 53.9 85.4 85.2 52.8 29.2 ...
- **p. 7 / 1 Introduction - extractive PDF cue:** Method Position Track Rotation Track 6-DoF Track Time Cost (s) Level 0 Level 1 Overall Level 0 Level 1 Level 2 Overall Position Rotation Overall ...
- **p. 1 / Abstract - extractive PDF cue:** While spatial reasoning has made progress in object localization relationships, it often overlooks object orientation-a key factor in 6-DoF fine-grained manipulation.
- **p. 4 / 1 Introduction - extractive PDF cue:** Optimization Let FSO represent the PointSO model parameterized by θSO (the CLIP is kept frozen and thus its parameters are not included).
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 4 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Pose, Estimation, Category, Instance, Template, Needed, Only, axis, relationship, instruction, unclear, Blow, Wind, Top | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | Pose, Estimation, Category, Instance, Template, Needed, Only, axis, relationship, instruction | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | PointSO, generalizable, cross-modal, Transformer, semantic, orientation, prediction, addition, introduce, Open6DOR | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | optimization, minimize, negative, cosine, similarity, Lcos, between, predicted, ground, truth | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / Abstract - extractive PDF cue:** X Y Z Pose Estimation Category / Instance Template Needed Only axis, the relationship with instruction is unclear "Blow Wind" "Top" "Back" "Pick up" "Fan" ...
- **p. 4 / 1 Introduction - extractive PDF cue:** For the 3D point clouds, we follow [26, 136, 89] to first sample Ns seed points using farthest point sampling (FPS) and then group inputs ...
- **p. 4 / 1 Introduction - extractive PDF cue:** 4, PointSO takes the object's 3D point clouds and a language description as inputs, and predicts the corresponding semantic orientation. "Drilling" "Handle" "top" Transformer Block ...
- **p. 5 / 1 Introduction - extractive PDF cue:** Given RGB-D images and language instructions, SOFAR first leverages a VLM to identify relevant object phrases and semantic orientations.
- **p. 5 / 1 Introduction - extractive PDF cue:** 3.2 Spatial-Aware Task Reasoning We encode the 6-DoF scene graph G into descriptive language and input it to the VLM alongside the RGB image I ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Traditional orientation, defined relative to a base frame or template model [104, 58, 120, 16], is insufficient for open-world manipulation guided by language instructions [108, ...
- **p. 3 / 1 Introduction - extractive PDF cue:** An object X can be associated with multiple semantic orientations by varying the language input, forming a set SX = {sX ℓ1, sX ℓ2, . ...
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Furthermore, leveraging the error detection and re-planning capabilities of VLMs [48, 1], we can make multiple attempts following a single-step execution failure ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Traditional pose representations rely on pre-defined frames or templates, limiting generalization and semantic grounding. | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** point, clouds, follow, first, sample, seed, points, farthest, sampling, FPS, then, group, inputs, KNN, feature, embedding, local, geometric, extraction, network.
- **Relevant PDF headings:** 0.63 Method (p. 29).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | We migrate its scenes into a robosuite-based simulation environment [151], following the task interface defined by LIBERO [64], and name this new ... | p. 8 (4 Experiments), p. 7 (4 Experiments) |
| Action / skill decoding | 7, SOFAR consistently outperforms baselines across all tracks, especially on orientation and 6-DoF tasks, while maintaining low planning overhead. | p. 7 (4 Experiments), p. 8 (4 Experiments) |
| Receding execution / feedback | SOFAR consistently outperforms other methods across both tracks, achieving over 18% improvement. | p. 9 (4 Experiments), p. 8 (4 Experiments) |

## Failure and Ablation Link

- **p. 32 / Figure/Table caption - extractive PDF cue:** Table 11: Ablation study of multi-modal fusion in PointSO. All experiments are conducted with the PointSO-Base variant. Fusion Method 45° 30° 15° 5°
- **p. 7 / 4 Experiments - extractive PDF cue:** The tasks are divided into three tracks-position, orientation, and comprehensive & 6-DoF-each with simple and hard variants.
- **p. 7 / 4 Experiments - extractive PDF cue:** We train different model variants on OrienText300K, and the results in Table 2 report performance across different angular thresholds ranging from 45° to 5°.
- **p. 8 / 4 Experiments - extractive PDF cue:** We present success rates for the "Variant Aggregation" and "Visual Matching" approaches.
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 3: Visualization of OrienText300K data construction and validation results. In summary, we propose Semantic Orientation as a new representation that bridges spatial reasoning and ...
- **p. 29 / Figure/Table caption - extractive PDF cue:** Table 7: Zeroshot articulate object manipulation evaluation within the SAPIEN [123] simulator using PartNet-Mobility Dataset. Notably, while the baseline methods use distinct training and testing ...
- **p. 32 / Figure/Table caption - extractive PDF cue:** Table 12: Ablation study of open vocabulary detection modules on Open6DOR perception tasks.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 5 (1 Introduction), objective p. 4 (1 Introduction), p. 2 (1 Introduction), p. 6 (1 Introduction), p. 7 (1 Introduction), p. 1 (Abstract), p. 4 (1 Introduction), temporal p. 8 (4 Experiments), p. 1 (Abstract), p. 1 (Abstract), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
