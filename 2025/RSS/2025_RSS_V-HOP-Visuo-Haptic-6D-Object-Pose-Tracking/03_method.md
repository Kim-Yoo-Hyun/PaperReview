# Method - V-HOP: Visuo-Haptic 6D Object Pose Tracking

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p037.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p037.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 3 (III. MeTHODOLOGY), p. 3 (III. MeTHODOLOGY)): Later, we introduce our visuo-haptic model and how it is trained.

## Method Body Digest

- **p. 3 / III. MeTHODOLOGY - extractive body cue:** Later, we introduce our visuo-haptic model and how it is trained.
- **p. 3 / III. MeTHODOLOGY - extractive body cue:** We first outline the core representations used in our haptic modality: gripper and object representations.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** A, Problem Definition We tackle the model-based visu tracking problem, assuming access to: + Visual observations: An RGB-D sensor observes the object in the environment. ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** 2) A sequence of RGB-D images O ~ {O,}{_. where each observation O, = 1;,.Dj] includes an RGB image I, and a depth map D,
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Recent state-of-the-art object pose estimation methods, such as FoundationPose {70}, have significantly advanced visual tracking by leveraging large-scale datasets.
- **p. 3 / III. MeTHODOLOGY - extractive body cue:** Our goal is to build a generalizable visuo-haptic pose tracker that accommodates diverse embodiments and ‘objects.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Accurately tracking object poses is a core capability for robotic manipulation, and would enable contact-tich and dexterous manipulations with efficent imitation or reinforcement learning (68, ...
- **p. 3 / III. MeTHODOLOGY - extractive body cue:** We propose V-HOP, a data-driven approach that fuses visual and haptic modalities to achieve accurate 6D object pose tracking.

## Design Rationale

- **p. 1 / 1. INTRODUCTION - extractive body cue:** First, we introduce a novel unified haptic representation that facilitates cross-embodiment learning.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** To address these challenges, we propose V-HOP (Fig.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** Second, we propose 4 transformer-based object pose tracker to fuse visual and haptic features.

## Source Evidence Cues

- **p. 3 / III. MeTHODOLOGY - extractive body cue:** Later, we introduce our visuo-haptic model and how it is trained.
- **p. 3 / III. MeTHODOLOGY - extractive body cue:** We first outline the core representations used in our haptic modality: gripper and object representations.
- **Detected method headings:** III. MeTHODOLOGY (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Multi-modal contact encoding | vision과 touch를 contact feature로 결합한다 | tactile image/force, vision, proprioception | tactile encoder, calibration, fusion 또는 temporal feature extraction을 수행 | contact feature/state | Later, we introduce our visuo-haptic model and how it is trained. | p. 3 (III. MeTHODOLOGY), p. 3 (III. MeTHODOLOGY) |
| Contact / dynamics inference | contact mode와 object response를 추정한다 | contact feature와 action history | mode classifier, force/dynamics model 또는 state estimator를 update | contact/force prediction | We first outline the core representations used in our haptic modality: gripper and object representations. | p. 3 (III. MeTHODOLOGY) |
| Force-aware action correction | interaction feedback으로 command를 보정한다 | predicted contact와 current wrench/touch | policy/control law가 action, force 또는 grasp를 재계산 | contact-safe action/torque | Later, we introduce our visuo-haptic model and how it is trained. | p. 3 (III. MeTHODOLOGY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update PDF body cue not selected; no claim inferred - inspect equations and algorithm boxes
- **Formal bridge:** visual/tactile/proprioceptive contact history -> contact-aware action/force -> contact prediction/control error -> slip/contact success and safe interaction.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Problem, Definition, tackle, model-based, visu, tracking, assuming, access, Visual, observations, RGB-D, sensor, observes, object | tactile image/force, vision과 proprioceptive history | body cue; exact tensor/frame verify |
| State/latent | Problem, Definition, tackle, model-based, visu, tracking, assuming, access, Visual, observations | contact geometry, force state 또는 latent dynamics | body cue; notation verify |
| Action/output | First, introduce, novel, unified, haptic, representation, facilitates, cross-embodiment, learning, address | grasp/contact action, force command 또는 object motion | body cue; unit/decoder verify |
| Objective/constraint | not stated or recoverable in the selected PDF body | contact prediction/control error | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. INTRODUCTION - extractive body cue:** A, Problem Definition We tackle the model-based visu tracking problem, assuming access to: + Visual observations: An RGB-D sensor observes the object in the environment. ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** 2) A sequence of RGB-D images O ~ {O,}{_. where each observation O, = 1;,.Dj] includes an RGB image I, and a depth map D,
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Recent state-of-the-art object pose estimation methods, such as FoundationPose {70}, have significantly advanced visual tracking by leveraging large-scale datasets.
- **p. 3 / III. MeTHODOLOGY - extractive body cue:** Our goal is to build a generalizable visuo-haptic pose tracker that accommodates diverse embodiments and ‘objects.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Accurately tracking object poses is a core capability for robotic manipulation, and would enable contact-tich and dexterous manipulations with efficent imitation or reinforcement learning (68, ...
- **p. 3 / III. MeTHODOLOGY - extractive body cue:** We propose V-HOP, a data-driven approach that fuses visual and haptic modalities to achieve accurate 6D object pose tracking.
- **Normalized interface:** observation=tactile image/force, vision과 proprioceptive history; state=contact geometry, force state 또는 latent dynamics; output/action=grasp/contact action, force command 또는 object motion.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | contact episode 또는 action chunk horizon; contact event timing이 핵심이다. | We validate our framework in our dataset and the Feelsight dataset, demonstrating significant per~ formance improvement on challenging sequences. | episode/sequence/action-chunk boundary |
| Rate / latency | tactile sampling/control loop가 visual policy rate와 다를 수 있다; numeric values 확인 필요. | Moreover, they typically process each frame independently, which can result in less coherent object pose tracking over sequences in real-world deployments. | Hz/fps, inference time and control rate |
| Memory | recent tactile/force history와 visual state; recurrent memory 여부 확인 필요. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | sensor fusion, contact inference와 high-frequency correction이 latency를 결정한다. | In terms of computational efficiency, V-HOP is appro: mately 10 times faster than NeuralFeels, achieving 32 FPS compared to NeuralFeels' 3 FPS ... | hardware, batch and throughput |

## Training vs Inference

- **p. 3 / III. MeTHODOLOGY - extractive body cue:** Later, we introduce our visuo-haptic model and how it is trained.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Later, introduce, visuo-haptic, model, trained, first, outline, core, representations, haptic, modality, gripper, object, Problem, Definition, tackle, model-based, visu, tracking, assuming.
- **Relevant PDF headings:** III. MeTHODOLOGY (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Multi-modal contact encoding | Our synthesized dataset exemplifies this principle and supports our robust real-world performance. | p. 5 (A. Multi-embodied Dataset), p. 5 (A. Multi-embodied Dataset) |
| Contact / dynamics inference | V-HOP achieves 1 32% lower ADD-S error compared to NeuralFeels and has a similar ADD-S-0.1d score. | p. 7 (experiment), p. 7 (experiment) |
| Force-aware action correction | Our results show that \V-HOP consistently outperforms FoundationPose in both ADD and ADD-S metrics under different levels of occlusion. ‘These results underscore ... | p. 7 (experiment), p. 7 (experiment) |

## Failure and Ablation Link

- **p. 7 / B. Bimanual Handover Experiment - extractive body cue:** For instance, a human may move the object during task execution, remove it from the gripper, or reposition it on the table (Fig.
- **p. 7 / B. Bimanual Handover Experiment - extractive body cue:** 1) If the grasp attempt fails, the robot must detect the failure based on the real-time object pose and reattempt the grasp.
- **p. 8 / C. Can-in-Mug Experiment - extractive body cue:** Successful execution hinges on precise pose estimation for both objects, as any noise in their poses can lead to failure.
- **p. 7 / B. Bimanual Handover Experiment - extractive body cue:** Inaccurate tracking results could lead to collision during the handover.
- **p. 9 / VI. RELATED Works - extractive body cue:** More recent works aim to overcome some of these limitations.
- **p. 9 / VI. RELATED Works - extractive body cue:** While model-free approaches [65, 69, 54] exist, they fall outside the scope of this work.
- **p. 5 / A. Multi-embodied Dataset - extractive body cue:** V) demonstrate robust performance and eliminate the need for costly real-world data collection,

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (III. MeTHODOLOGY), p. 3 (III. MeTHODOLOGY), objective 본문 anchor 없음, temporal p. 1 (Abstract), p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 7 (B. Bimanual Handover Experiment), p. 7 (experiment), p. 8 (B. Bimanual Handover Experiment).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** A, Problem Definition We tackle the model-based visu tracking problem, assuming access to: + Visual observations: An RGB-D sensor observes the object in the environment. + Haptic feedback: The object ... (p. 2, 1. INTRODUCTION).
- **Objective/update evidence:** Later, we introduce our visuo-haptic model and how it is trained. (p. 3, III. MeTHODOLOGY).
- **Temporal/runtime evidence:** The task requires the robot to perform the following sequence of actions: (p. 7, B. Bimanual Handover Experiment).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
