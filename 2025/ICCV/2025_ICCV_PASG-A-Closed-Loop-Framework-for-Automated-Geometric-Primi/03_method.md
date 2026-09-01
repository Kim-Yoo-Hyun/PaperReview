# Method - PASG: A Closed-Loop Framework for Automated Geometric Primitive Extraction and Semantic Anchoring in Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhu_PASG_A_Closed-Loop_Framework_for_Automated_Geometric_Primitive_Extraction_and_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhu_PASG_A_Closed-Loop_Framework_for_Automated_Geometric_Primitive_Extraction_and_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 4 (3.2. Geometry Primitive Extraction), p. 5 (3.3. Task-Oriented Semantic Annotation), p. 3 (Method), p. 3 (2.2. Spatial Reasoning for Manipulation), p. 4 (3.2. Geometry Primitive Extraction), p. 5 (3.2. Geometry Primitive Extraction)): To enable this, we first acquire multi-view RGB images ( \ math cal {I} = \{I_1,...,I_n\} ) from the object's 3D mesh data, which are then resized and fed into ...

## Method Body Digest

- **p. 4 / 3.2. Geometry Primitive Extraction - extractive PDF cue:** To enable this, we first acquire multi-view RGB images ( \ math cal {I} = \{I_1,...,I_n\} ) from the object's 3D mesh data, which are ...
- **p. 5 / 3.3. Task-Oriented Semantic Annotation - extractive PDF cue:** Specifically, we use VLMs to analyze geometric and physical features from multi-view images ( \mathcal {I} ) to infer potential manipulation tasks ( \ math ...
- **p. 3 / Method - extractive PDF cue:** Normative interaction primitive and semantic coupling across different frameworks in robotic manipulation tasks: PASG as the first automated closed-loop framework with primitive extraction, semantic anchoring, ...
- **p. 3 / 2.2. Spatial Reasoning for Manipulation - extractive PDF cue:** Through automated extraction of primitives using VFMs and hierarchical semantic alignment with VLMs, PASG achieves closed-loop optimization of spatial reasoning paradigms in open-world scenarios.
- **p. 4 / 3.2. Geometry Primitive Extraction - extractive PDF cue:** Keypoint Extraction For geometric keypoint ( \mathcal {K}_{\text {raw}} ) detection, we extract representative geometric positions including centers ( \ math cal {C} = \{c_1,...,c_n\} ...
- **p. 5 / 3.2. Geometry Primitive Extraction - extractive PDF cue:** Principal Axis Calibration For standardized axis representation, most 3D objects in datasets provide pre-aligned main axes.
- **p. 6 / 3.4. Semantic-guide Reasoning in Manipulation - extractive PDF cue:** Specifically, through our manipulation experiments (in Section 4.2), we validate that the PASG pipeline can reliably identify interaction primitives across diverse object categories.
- **p. 3 / Method - extractive PDF cue:** OmniManip employs computational constraint optimization and scene rendering for VLM validation, while our method directly detects annotation-primitive misalignment for efficient self-correction. addresses this limitation by ...

## Design Rationale

- **p. 2 / 1. Introduction - extractive PDF cue:** Our contributions are as follows: • We propose a novel framework that automatically annotates hierarchical semantics for object interaction primitives, bridging the gap between low-level ...
- **p. 2 / 1. Introduction - extractive PDF cue:** To address these challenges, as shown in Fig 1, we propose PASG, a closed-loop framework establishing the mapping between spatial primitives and functional semantics.
- **p. 3 / Method - extractive PDF cue:** OmniManip employs computational constraint optimization and scene rendering for VLM validation, while our method directly detects annotation-primitive misalignment for efficient self-correction. addresses this limitation by ...

## Source Evidence Cues

- **p. 4 / 3.2. Geometry Primitive Extraction - extractive PDF cue:** To enable this, we first acquire multi-view RGB images ( \ math cal {I} = \{I_1,...,I_n\} ) from the object's 3D mesh data, which are ...
- **p. 5 / 3.3. Task-Oriented Semantic Annotation - extractive PDF cue:** Specifically, we use VLMs to analyze geometric and physical features from multi-view images ( \mathcal {I} ) to infer potential manipulation tasks ( \ math ...
- **p. 3 / Method - extractive PDF cue:** Normative interaction primitive and semantic coupling across different frameworks in robotic manipulation tasks: PASG as the first automated closed-loop framework with primitive extraction, semantic anchoring, ...
- **p. 3 / 2.2. Spatial Reasoning for Manipulation - extractive PDF cue:** Through automated extraction of primitives using VFMs and hierarchical semantic alignment with VLMs, PASG achieves closed-loop optimization of spatial reasoning paradigms in open-world scenarios.
- **p. 4 / 3.2. Geometry Primitive Extraction - extractive PDF cue:** Keypoint Extraction For geometric keypoint ( \mathcal {K}_{\text {raw}} ) detection, we extract representative geometric positions including centers ( \ math cal {C} = \{c_1,...,c_n\} ...
- **p. 5 / 3.2. Geometry Primitive Extraction - extractive PDF cue:** Principal Axis Calibration For standardized axis representation, most 3D objects in datasets provide pre-aligned main axes.
- **p. 6 / 3.4. Semantic-guide Reasoning in Manipulation - extractive PDF cue:** Specifically, through our manipulation experiments (in Section 4.2), we validate that the PASG pipeline can reliably identify interaction primitives across diverse object categories.
- **Detected method headings:** Method (p. 3); 3. Method (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Multimodal task encoding | vision·language·proprioception·3D context를 결합한다 | image/video, instruction, state/history | pretrained encoder, adapter, attention, grounding 또는 fusion을 적용 | task-conditioned context | To enable this, we first acquire multi-view RGB images ( \ math cal {I} = \{I_1,...,I_n\} ) from the object's 3D mesh ... | p. 4 (3.2. Geometry Primitive Extraction), p. 5 (3.3. Task-Oriented Semantic Annotation) |
| Action / skill decoding | context에서 continuous action 또는 skill을 생성한다 | context와 history | autoregressive, diffusion, flow, value-guided 또는 skill decoder를 적용 | action, pose, option 또는 action chunk | Specifically, we use VLMs to analyze geometric and physical features from multi-view images ( \mathcal {I} ) to infer potential manipulation tasks ... | p. 5 (3.3. Task-Oriented Semantic Annotation), p. 3 (Method) |
| Receding execution / feedback | 예측을 부분 실행하고 다시 관측한다 | action chunk와 current observation | execute, replan, terminate, recover 또는 memory update를 수행 | next action/feedback state | Normative interaction primitive and semantic coupling across different frameworks in robotic manipulation tasks: PASG as the first automated closed-loop framework with primitive ... | p. 3 (Method), p. 3 (2.2. Spatial Reasoning for Manipulation) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 3 / Method - extractive PDF cue:** OmniManip employs computational constraint optimization and scene rendering for VLM validation, while our method directly detects annotation-primitive misalignment for efficient self-correction. addresses this limitation by ...
- **p. 3 / 2.2. Spatial Reasoning for Manipulation - extractive PDF cue:** Spatial reasoning in manipulation involves inferring interaction constraints from object's spatial primitives to guide robot actions.
- **p. 4 / 3.1. Semantic Primitives in Robotic Manipulation - extractive PDF cue:** These specify object orientation and motion constraints: • Primary Axis ( a_p ) The principal orientation axis of the object, usually dictated by its geometry ...
- **p. 5 / 3.3. Task-Oriented Semantic Annotation - extractive PDF cue:** \mat h cal { R}_ {i j}^o(P_{ij}^o, A_{ij}^o) \implies g_{ij} \label {eq:constraint} (2) where P _{ i j}^o \subseteq \mathcal {P}^o denotes point primitives and ...
- **p. 5 / 3.3. Task-Oriented Semantic Annotation - extractive PDF cue:** Each task t_i is decomposed into sub-stages with explicit operation goals per stage: \ mathc al { G}_i = \{g_{i1},...,g_{ik}\} \label {eq:subgoals} (1) To identify ...
- **p. 4 / 3.1. Semantic Primitives in Robotic Manipulation - extractive PDF cue:** (e.g. the spout tip over a cup for pouring) • Grasp Point ( p_g ): A location on the object optimized for a secure hold ...
- **Formal bridge:** multimodal context o,l,p/history -> action, pose, option or chunk a -> policy/action modeling objective -> instruction-conditioned task success.
- **Equation/algorithm anchors:** p. 3 (2.2. Spatial Reasoning for Manipulation), p. 3 (3.1. Semantic Primitives in Robotic Manipulation), p. 4 (3.1. Semantic Primitives in Robotic Manipulation), p. 5 (3.3. Task-Oriented Semantic Annotation), p. 5 (3.3. Task-Oriented Semantic Annotation).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | contributions, follows, novel, framework, automatically, annotates, hierarchical, semantics, object, interaction, primitives, bridging, between, low-level | image/video, language instruction, proprioception과 history | body cue; exact tensor/frame verify |
| State/latent | contributions, follows, novel, framework, automatically, annotates, hierarchical, semantics, object, interaction | language-grounded task state와 action-policy context | body cue; notation verify |
| Action/output | contributions, follows, novel, framework, automatically, annotates, hierarchical, semantics, object, interaction | continuous action, pose 또는 action chunk | body cue; unit/decoder verify |
| Objective/constraint | OmniManip, employs, computational, constraint, optimization, scene, rendering, VLM, validation, while | policy/action modeling objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Introduction - extractive PDF cue:** Our contributions are as follows: • We propose a novel framework that automatically annotates hierarchical semantics for object interaction primitives, bridging the gap between low-level ...
- **p. 3 / 2.2. Spatial Reasoning for Manipulation - extractive PDF cue:** Spatial reasoning in manipulation involves inferring interaction constraints from object's spatial primitives to guide robot actions.
- **p. 3 / 3.1. Semantic Primitives in Robotic Manipulation - extractive PDF cue:** In robotic manipulation tasks, spatial primitives of objects serve as fundamental building blocks for planning and executing actions.
- **p. 4 / 3.1. Semantic Primitives in Robotic Manipulation - extractive PDF cue:** Point Interaction Primitives ( \mathcal {P} ) denote specific object locations critical for manipulation. • Anchor Point ( p_a ): A reference position that determines ...
- **p. 4 / 3.1. Semantic Primitives in Robotic Manipulation - extractive PDF cue:** Overview of PASG To further integrate operational task semantics, we categorize interaction primitives into two functionally distinct classes based on manipulation requirements: point-based ( \mathcal ...
- **p. 6 / 3.3. Task-Oriented Semantic Annotation - extractive PDF cue:** Keypoints and Axes Annotated Output.
- **p. 6 / 3.4. Semantic-guide Reasoning in Manipulation - extractive PDF cue:** Specifically, through our manipulation experiments (in Section 4.2), we validate that the PASG pipeline can reliably identify interaction primitives across diverse object categories.
- **Normalized interface:** observation=image/video, language instruction, proprioception과 history; state=language-grounded task state와 action-policy context; output/action=continuous action, pose 또는 action chunk.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | instruction-conditioned task horizon; action chunk/skill termination 여부는 paper-specific. | Unlike SOFAR's predefined directional priors, PASG framework focuses on fine-grained keypoints and functional vectors to construct hierarchical semantic anchoring, achieving deeper integration ... | episode/sequence/action-chunk boundary |
| Rate / latency | policy inference/decoder rate와 low-level control rate가 분리된다; numeric value 확인 필요. | Normative interaction primitive and semantic coupling across different frameworks in robotic manipulation tasks: PASG as the first automated closed-loop framework with primitive ... | Hz/fps, inference time and control rate |
| Memory | image-language-proprioception history, transformer context 또는 persistent memory. | not recovered | window and reset |
| Compute | multimodal encoder, decoder/sampling steps와 action horizon이 latency를 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** enable, first, acquire, multi-view, RGB, images, math, I_1, I_n, object, mesh, data, then, resized, segmentation, model, Specifically, VLMs, analyze, geometric.
- **Relevant PDF headings:** Method (p. 3); 3. Method (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multimodal task encoding | RoboTwin provides standardized benchmarks that ensure both reproducibility and practical relevance. | p. 7 (4.2. Manipulation Task Evaluation), p. 7 (4.3. Object-based Spatial-Semantic Reasoning) |
| Action / skill decoding | Results of this comparison are summarized in Table 2, the PASG-based policy achieves competitive performance compared to manual annotations, and even outperforms ... | p. 7 (4.2. Manipulation Task Evaluation), p. 8 (4.3. Object-based Spatial-Semantic Reasoning) |
| Receding execution / feedback | Results of this comparison are summarized in Table 2, the PASG-based policy achieves competitive performance compared to manual annotations, and even outperforms ... | p. 7 (4.2. Manipulation Task Evaluation), p. 8 (4.3. Object-based Spatial-Semantic Reasoning) |

## Failure and Ablation Link

- **p. 8 / 4.3. Object-based Spatial-Semantic Reasoning - extractive PDF cue:** Data Effectiveness Study Data Effectiveness To evaluate the effectiveness of finetuning data, we conducted a progressive scaling experiment: fine-tune the model with randomly sampled subsets ...
- **p. 7 / 4.3. Object-based Spatial-Semantic Reasoning - extractive PDF cue:** We first generate 6,979 questions from a designated pool of base objects, allocating 80% (5,583 questions) as the fine-tuning training set to establish a foundational ...
- **p. 8 / 4.3. Object-based Spatial-Semantic Reasoning - extractive PDF cue:** Finetune We fine-tuned Qwen-2.5VL [6] using Low-Rank Adaptation (LoRA) to assess whether the VQA benchmark supports knowledge transfer in primitive compositional reasoning.
- **p. 8 / 5. Conclusion - extractive PDF cue:** It overcomes key limitations in existing systems through geometry-aware feature aggregation, dynamic coupling of primitives with functional affordances, and selfcorrective mechanisms to reduce error propagation.
- **p. 3 / Figure/Table caption - extractive PDF cue:** Table 1. Normative interaction primitive and semantic coupling across different frameworks in robotic manipulation tasks: PASG as the first automated closed-loop framework with primitive extraction, ...
- **p. 8 / 5. Conclusion - extractive PDF cue:** PASG's ability to generate diverse interaction primitives enhances task flexibility and robustness, making it suitable for real-world applications.
- **p. 7 / 4.2. Manipulation Task Evaluation - extractive PDF cue:** Each task is executed 100 times using randomly initialized seeds to ensure robustness of the evaluation.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 4 (3.2. Geometry Primitive Extraction), p. 5 (3.3. Task-Oriented Semantic Annotation), p. 3 (Method), p. 3 (2.2. Spatial Reasoning for Manipulation), p. 4 (3.2. Geometry Primitive Extraction), p. 5 (3.2. Geometry Primitive Extraction), objective p. 3 (Method), p. 3 (2.2. Spatial Reasoning for Manipulation), p. 4 (3.1. Semantic Primitives in Robotic Manipulation), p. 5 (3.3. Task-Oriented Semantic Annotation), p. 5 (3.3. Task-Oriented Semantic Annotation), p. 4 (3.1. Semantic Primitives in Robotic Manipulation), temporal p. 3 (Method), p. 3 (Method), p. 5 (3.3. Task-Oriented Semantic Annotation), p. 6 (3.3. Task-Oriented Semantic Annotation), p. 6 (3.4. Semantic-guide Reasoning in Manipulation), p. 7 (4.2. Manipulation Task Evaluation).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
