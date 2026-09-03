# Method - Seeing Across Views: Benchmarking Spatial Reasoning of Vision-Language Models in Robotic Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (50 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=jXDZJAfRZB; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/247464. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 25 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 32 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 25 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 28 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 29 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 31 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS)): We then describe the four robotic subtasks, which extend spatial reasoning to manipulation scenarios: Action Planning, Step Execution, Trajectory Selection, and Affordance Recognition.

## Method Body Digest

- **p. 25 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** We then describe the four robotic subtasks, which extend spatial reasoning to manipulation scenarios: Action Planning, Step Execution, Trajectory Selection, and Affordance Recognition.
- **p. 32 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** They examine whether models can ground spatial understanding into action decisions, ranging from high-level planning to low-level execution, and from trajectory-level reasoning to grasp affordance ...
- **p. 25 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** The model is then asked to identify which candidate corresponds to the same object as the red box in the reference view.
- **p. 28 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** The question then asks the model: "Which of the following sets of coordinate triplets best describes the positions of the highlighted objects?" Coordinates are normalized ...
- **p. 29 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** The model must then integrate information across views and select the sequence most likely to achieve the goal.
- **p. 31 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** All candidate options are then expressed in these normalized directional terms, and the model must select the sequence that correctly achieves the task.
- **p. 31 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** The model is asked: "Which color-coded line represents the grasp candidate most likely to succeed?" All distractors are carefully designed: while they may appear physically ...
- **p. 18 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** To provide models with explicit geometric constraints, we augmented each view with predicted depth maps.

## Design Rationale

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To fill this gap, we introduce MV-RoboBench, a benchmark specifically designed to evaluate multiview spatial reasoning in robotic manipulation scenarios.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** 2 MV-ROBOBENCH 2.1 OVERVIEW We introduce MV-RoboBench, a benchmark designed to evaluate the multi-view reasoning capabilities of VLMs in robotic manipulation scenarios.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our key contributions are as follows: • We establish the first benchmark that integrates spatial and robotic reasoning with synchronized multi-view inputs in robotic manipulation ...

## Source Evidence Cues

- **p. 25 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** We then describe the four robotic subtasks, which extend spatial reasoning to manipulation scenarios: Action Planning, Step Execution, Trajectory Selection, and Affordance Recognition.
- **p. 32 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** They examine whether models can ground spatial understanding into action decisions, ranging from high-level planning to low-level execution, and from trajectory-level reasoning to grasp affordance ...
- **p. 25 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** The model is then asked to identify which candidate corresponds to the same object as the red box in the reference view.
- **p. 28 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** The question then asks the model: "Which of the following sets of coordinate triplets best describes the positions of the highlighted objects?" Coordinates are normalized ...
- **p. 29 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** The model must then integrate information across views and select the sequence most likely to achieve the goal.
- **p. 31 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** All candidate options are then expressed in these normalized directional terms, and the model must select the sequence that correctly achieves the task.
- **p. 31 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** The model is asked: "Which color-coded line represents the grasp candidate most likely to succeed?" All distractors are carefully designed: while they may appear physically ...
- **Detected method headings:** B.1 MODEL ACCESS AND INFERENCE PROTOCOL (p. 16)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Task / interface definition | method 비교에 필요한 task·state·action contract를 고정한다 | environment, embodiment, task variation, split | episode, instruction, observation/action schema와 reset rule을 정의 | benchmark episodes | We then describe the four robotic subtasks, which extend spatial reasoning to manipulation scenarios: Action Planning, Step Execution, Trajectory Selection, and Affordance ... | p. 25 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 32 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |
| Baseline harness | 같은 protocol로 method와 baseline을 실행한다 | episode와 method interface | baseline, ablation, seed, checkpoint와 rollout budget을 통제 | comparable trajectories/scores | They examine whether models can ground spatial understanding into action decisions, ranging from high-level planning to low-level execution, and from trajectory-level reasoning ... | p. 32 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 25 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |
| Metric / failure reporting | success 외에 generalization과 failure를 측정한다 | trajectory, log, task outcome | score aggregation, failure taxonomy, efficiency와 reproducibility audit을 적용 | comparison matrix | The model is then asked to identify which candidate corresponds to the same object as the red box in the reference view. | p. 25 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 28 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 18 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** To provide models with explicit geometric constraints, we augmented each view with predicted depth maps.
- **p. 20 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** While ERQA is domain-relevant, our analysis suggests that it exhibits low discriminative power for comparing current SOTA models: • Compressed Performance Range: The overall accuracy ...
- **p. 22 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** For the AgiWorld dataset, we randomly sampled image pairs with the constraint that the interval between two selected frames was at least ten frames.
- **p. 29 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** Only one option corresponds to a valid sequence that completes the task while minimizing collisions, whereas the distractors follow plausible but incorrect paths.
- **p. 33 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** This allows us to rigorously measure the "performance drop" caused by the loss of multi-view context.
- **p. 37 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** Overall, these failures indicate that current VLMs still lack robust modeling of robotic affordances and physical constraints, especially when such reasoning must be carried out ...
- **Formal bridge:** standardized episode e and interface -> method trajectory/action -> benchmark score and failure cost -> comparable score and protocol validity.
- **Equation/algorithm anchors:** p. 18 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 20 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 22 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 33 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 37 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Top, original, inputs, left, gripper, head, right, cameras, Bottom, blurry, synthesized, view, interpolated, extrinsics | standardized observation, action, task state와 evaluation split | body cue; exact tensor/frame verify |
| State/latent | Top, original, inputs, left, gripper, head, right, cameras, Bottom, blurry | benchmark state/goal와 method decision | body cue; notation verify |
| Action/output | fill, introduce, MV-RoboBench, benchmark, specifically, designed, evaluate, multiview, spatial, reasoning | policy/controller trajectory 또는 measured result | body cue; unit/decoder verify |
| Objective/constraint | provide, models, explicit, geometric, constraints, augmented, view, predicted, depth, maps | benchmark score and failure cost | equation anchor required |

## Observation–State–Action Interface

- **p. 19 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** Top: original inputs from left gripper, head, and right gripper cameras; Bottom: blurry synthesized view from interpolated extrinsics. "text": "Image context: Corresponding estimated depth map.
- **p. 10 / 1 INTRODUCTION - extractive body cue:** Our results suggest that scaling perception alone is insufficient-models require explicit reasoning mechanisms to transform multi-view observations into actionable, embodied understanding.
- **p. 18 / C.3 VISUAL AUGMENTATION VIA NOVEL VIEW SYNTHESIS - extractive body cue:** While effective for clean object-level inputs, they proved unsuitable for cluttered robotic scenes, as selecting accurate masks is non-trivial and the outputs often failed to ...
- **p. 20 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** ERQA focuses on embodied reasoning in simulated environments and includes categories such as Action Reasoning, State Estimation, and a subset of Multi-view Reasoning.
- **p. 10 / 1 INTRODUCTION - extractive body cue:** Moreover, even with access to depth or point cloud inputs, current models rarely demonstrate reliable multi-view consistency or explicit exploitation of geometric cues when answering ...
- **p. 30 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** Each instance provides synchronized multi-view observations together with a natural language description of the goal.
- **p. 33 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** While multi-view information provides critical depth cues and occlusion handling, these questions remain logically valid even when restricted to a single input image.
- **Normalized interface:** observation=standardized observation, action, task state와 evaluation split; state=benchmark state/goal와 method decision; output/action=policy/controller trajectory 또는 measured result.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | benchmark episode/task horizon과 method rollout horizon을 명시해야 한다. | We then add distractors from the same episode but different time steps, ensuring a non-trivial temporal gap in the gripper poses so ... | episode/sequence/action-chunk boundary |
| Rate / latency | benchmark step/control rate, reset and evaluation throughput을 분리한다. | For each ground truth gripper image, we first include the image from the opposite gripper at the same time step. | Hz/fps, inference time and control rate |
| Memory | episode logs, seed/split metadata와 method state/history. | not recovered | window and reset |
| Compute | environment throughput, policy inference와 evaluation parallelism이 결정한다. | not recovered | hardware, batch and throughput |

## Training vs Inference

- **p. 23 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** E.5.1 ANNOTATOR TRAINING AND TASK UNDERSTANDING All annotators participating in the construction of MV-RoboBench were senior undergraduate students or Ph.D. candidates in computer science or ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** then, describe, four, robotic, subtasks, extend, spatial, reasoning, manipulation, scenarios, Action, Planning, Step, Execution, Trajectory, Selection, Affordance, Recognition, They, examine.
- **Relevant PDF headings:** B.1 MODEL ACCESS AND INFERENCE PROTOCOL (p. 16).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Task / interface definition | F.10 SUMMARY OF BENCHMARK CONSTRUCTION Taken together, the eight subtasks provide a comprehensive evaluation of spatial and robotic reasoning in multi-view environments. | p. 32 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 18 (C.3 VISUAL AUGMENTATION VIA NOVEL VIEW SYNTHESIS) |
| Baseline harness | Table 7: Comparison of Single-View vs. Multi-View performance on selected subtasks. The values represent Multi-View accuracy, and values in parentheses indicate the ... | p. 33 (Figure/Table caption), p. 33 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS) |
| Metric / failure reporting | Table 7: Comparison of Single-View vs. Multi-View performance on selected subtasks. The values represent Multi-View accuracy, and values in parentheses indicate the ... | p. 33 (Figure/Table caption), p. 8 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4: Best-per-group model perfor- mance across MV-RoboBench subtasks. indicating that they fail to leverage multi-view infor- mation and effectively guess without spatial integration. In ...
- **p. 33 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** This suggests that effectively fusing discordant visual information requires strong spatial reasoning capabilities; without this, smaller models may be distracted by the increased visual context ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Accuracy of CoT-style augmentations on MV-RoboBench. ∆s and ∆r indicate changes on spatial and robotic tasks relative to the origin baseline. Variants: w ...
- **p. 24 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** Annotators carefully removed pairs containing occlusions, poor synchronization, or ambiguous spatial relationships to ensure that only high-quality candidates entered the QA generation stage.
- **p. 28 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** This abstraction allows spatial relations to be expressed consistently without requiring precise metric depth.
- **p. 31 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** We ensure that exactly one candidate is feasible across views and can complete the task without collisions; every instance is human-validated to confirm that the ...
- **p. 32 / C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS - extractive body cue:** Therefore, these tasks were excluded from the ablation.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 25 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 32 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 25 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 28 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 29 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 31 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), objective p. 18 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 20 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 22 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 29 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 33 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 37 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), temporal p. 27 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 27 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 30 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 32 (C.4 STRUCTURAL AUGMENTATION VIA DEPTH PRIORS), p. 18 (C.1 CHAIN-OF-THOUGHT (COT) PROMPTING), p. 18 (C.3 VISUAL AUGMENTATION VIA NOVEL VIEW SYNTHESIS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
