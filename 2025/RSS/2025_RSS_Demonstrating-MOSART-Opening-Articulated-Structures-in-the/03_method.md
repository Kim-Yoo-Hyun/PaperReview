# Method - Demonstrating MOSART: Opening Articulated Structures in the Real World

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (25 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p033.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p033.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 20 (A. Robot Utility Models)): We provide additional details about Robot Utility Models (RUM) [16].

## Method Body Digest

- **p. 20 / A. Robot Utility Models - extractive body cue:** We provide additional details about Robot Utility Models (RUM) [16].
- **p. 4 / A. Predicting Articulation Parameters - extractive body cue:** We also add additional heads to Mask RCNN; however, rather than directly predicting 3D outputs from the RGB-D input, we adopt a two-stage approach involving ...
- **p. 3 / A. Predicting Articulation Parameters - extractive body cue:** Researchers have extensively looked at different aspects: a) construction of various datasets (from simulation (40, 14, 20], real world images [76, 36, 1], and real ...
- **p. 2 / 1. Iyrropucrion - extractive body cue:** To our surprise, we find that the modular system outperforms this latest endto-end learning method (Section IV-B and Table 1) This result is particularly useful ...
- **p. 3 / 1. Iyrropucrion - extractive body cue:** The perception module outputs 3D articulation parameters in the robot frame using RGB-D images.
- **p. 4 / B. Generating Motion Plans - extractive body cue:** Recent papers have looked at different aspects: pick-moveplace tasks [85], high-level planning given natural language instructions [2], dynamic whole body control [18], building simulators [58], ...
- **p. 1 / Abstract - extractive body cue:** Our large-scale study reveals a number of surprising findings: a) modular systems outperform end-to-end learned systems for this task, even when the end-to-end learned systems ...
- **p. 2 / 1. Iyrropucrion - extractive body cue:** Very briefly, MOSART adapts a Mask RCNN model [28] for inferring articulation parameters, extends a trajectory optimization framework for producing whole body motion plans [26], ...

## Design Rationale

- **p. 2 / 1. Iyrropucrion - extractive body cue:** We considered two broad ways of putting together such a system: a modular approach and an end-to-end learning approach, bat ultimately favored a modular approach, ...
- **p. 4 / B. Generating Motion Plans - extractive body cue:** In contrast to these approaches, we develop a system that operates on novel object instances in novel environments in a zero-shot manner without requiring any ...
- **p. 1 / Front matter - extractive body cue:** g novel cabinets, drawers, and ovens

## Source Evidence Cues

- **p. 20 / A. Robot Utility Models - extractive body cue:** We provide additional details about Robot Utility Models (RUM) [16].
- **Detected method headings:** A. Robot Utility Models (p. 20)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Scene / interaction state | base·arm·object 관계를 표현한다 | egocentric RGB-D, language goal, proprioception | map, object, reachability, contact 또는 affordance state를 구성 | base-arm interaction state | We provide additional details about Robot Utility Models (RUM) [16]. | p. 20 (A. Robot Utility Models) |
| Base-arm task decision | 접근·도킹·grasp·manipulation sequence를 결정한다 | interaction state와 task instruction | keypoint, option, trajectory, grasp 또는 joint planning을 수행 | base path plus arm/gripper plan | We provide additional details about Robot Utility Models (RUM) [16]. | p. 20 (A. Robot Utility Models) |
| Execution / correction | 부분 실행 후 observation으로 계획을 수정한다 | current pose, visual/force feedback | tracking, regrasp, docking correction, recovery 또는 replan을 수행 | next mobile-manipulation action | We provide additional details about Robot Utility Models (RUM) [16]. | p. 20 (A. Robot Utility Models) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update cue 없음 - inspect equations and algorithm boxes
- **Formal bridge:** base-arm-object state and language/task goal -> base plus arm/gripper action -> long-horizon task utility under reachability/contact constraints -> task completion and recovery.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | additional, heads, Mask, RCNN, however, rather, directly, predicting, outputs, RGB-D, input, adopt, two-stage, involving | egocentric RGB-D, language/task goal, base-arm proprioception | body cue; exact tensor/frame verify |
| State/latent | additional, heads, Mask, RCNN, however, rather, directly, predicting, outputs, RGB-D | map/object/contact state와 base-arm coordination decision | body cue; notation verify |
| Action/output | considered, broad, ways, putting, together, system, modular, end-to-end, learning, ultimately | base motion plus arm/gripper action | body cue; unit/decoder verify |
| Objective/constraint | not recovered | long-horizon task utility under reachability/contact constraints | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / A. Predicting Articulation Parameters - extractive body cue:** We also add additional heads to Mask RCNN; however, rather than directly predicting 3D outputs from the RGB-D input, we adopt a two-stage approach involving ...
- **p. 3 / A. Predicting Articulation Parameters - extractive body cue:** Researchers have extensively looked at different aspects: a) construction of various datasets (from simulation (40, 14, 20], real world images [76, 36, 1], and real ...
- **p. 2 / 1. Iyrropucrion - extractive body cue:** To our surprise, we find that the modular system outperforms this latest endto-end learning method (Section IV-B and Table 1) This result is particularly useful ...
- **p. 3 / 1. Iyrropucrion - extractive body cue:** The perception module outputs 3D articulation parameters in the robot frame using RGB-D images.
- **p. 4 / B. Generating Motion Plans - extractive body cue:** Recent papers have looked at different aspects: pick-moveplace tasks [85], high-level planning given natural language instructions [2], dynamic whole body control [18], building simulators [58], ...
- **p. 1 / Abstract - extractive body cue:** Our large-scale study reveals a number of surprising findings: a) modular systems outperform end-to-end learned systems for this task, even when the end-to-end learned systems ...
- **p. 2 / 1. Iyrropucrion - extractive body cue:** Very briefly, MOSART adapts a Mask RCNN model [28] for inferring articulation parameters, extends a trajectory optimization framework for producing whole body motion plans [26], ...
- **Normalized interface:** observation=egocentric RGB-D, language/task goal, base-arm proprioception; state=map/object/contact state와 base-arm coordination decision; output/action=base motion plus arm/gripper action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value not recovered from the selected body cues. | 2nd vs Sth action from the current timestep), and whether initializing the policy with the simulation policy helps or not. ‘The best ... | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value not recovered from the selected body cues. | Very briefly, MOSART adapts a Mask RCNN model [28] for inferring articulation parameters, extends a trajectory optimization framework for producing whole body ... | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value not recovered from the selected body cues. | not recovered | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile 확인 필요. | not recovered | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** provide, additional, details, about, Robot, Utility, Models, RUM, heads, Mask, RCNN, however, rather, directly, predicting, outputs, RGB-D, input, adopt, two-stage.
- **Relevant PDF headings:** A. Robot Utility Models (p. 20).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Scene / interaction state | In each test, the robot is placed approximately 1.5m from the target object with the camera oriented so as to have the ... | p. 7 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| Base-arm task decision | This includes evaluating the quality of our MaskRCNN-based perception module (as well as a Detic-based perception model) on real world images, comparing ... | p. 6 (IV. EXPERIMENTS), p. 8 (Figure/Table caption) |
| Execution / correction | Overall, our system achieves a 61% success rate across 31 unseen cabinets and drawers in unseen real world environments. | p. 7 (IV. EXPERIMENTS), p. 3 (Figure/Table caption) |

## Failure and Ablation Link

- **p. 6 / IV. EXPERIMENTS - extractive body cue:** This includes evaluating the quality of our MaskRCNN-based perception module (as well as a Detic-based perception model) on real world images, comparing APM to two ...
- **p. 10 / Discussion - extractive body cue:** Other failures were during execution, where the handle would slip out, and during navigation, where navigating ‘on carpets was less accurate than on tiles.
- **p. 9 / V. Limitations - extractive body cue:** Finally, there are limitations of the embodiment we use (e.g. it cannot reach cabinets high up, or exert enough force to pull open fridge doors).
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 8. 59% of failures (ie. 7 failures) are due to perception, including various kinds of failures, such as failure to detect meshed cabinets (2/7), ...
- **p. 10 / Discussion - extractive body cue:** Grasping failures accounted for approximately 25% of all observed failures, underscoring the inherent difficulty of achieving precise, last-centimeter adjustments required for successful grasping.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** We then study the generalization of our pipeline to other articulation types and diverse handles (Section IV-E), before wwe analyze the failure modes of our ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** Section IV-F° provides a extensive discussion of the failure modes

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 20 (A. Robot Utility Models), objective 본문 anchor 없음, temporal p. 20 (B. Sim2Real Behavior Cloning), p. 2 (1. Iyrropucrion), p. 3 (1. Iyrropucrion), p. 3 (1. Iyrropucrion), p. 4 (A. Predicting Articulation Parameters), p. 4 (A. Predicting Articulation Parameters).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
