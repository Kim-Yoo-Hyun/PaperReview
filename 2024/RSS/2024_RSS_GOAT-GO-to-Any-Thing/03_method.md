# Method - GOAT: GO to Any Thing

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p073.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p073.html. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (IV. GOAT METHOD), p. 4 (IV. GOAT METHOD), p. 3 (IV. GOAT METHOD), p. 3 (IV. GOAT METHOD)): For language goals, we first extract an object category from the language description (by prompting with Mistral 7B [30] in our experiments), then match CLIP features of the language description ...

## Method Body Digest

- **p. 4 / IV. GOAT METHOD - extractive body cue:** For language goals, we first extract an object category from the language description (by prompting with Mistral 7B [30] in our experiments), then match CLIP ...
- **p. 4 / IV. GOAT METHOD - extractive body cue:** Similarly, for image goals, we first extract an object category from the image with MaskRCNN, then match keypoints of the goal image with keypoints of ...
- **p. 3 / IV. GOAT METHOD - extractive body cue:** If no instance is localized, the global policy outputs an exploration goal.
- **p. 3 / IV. GOAT METHOD - extractive body cue:** In this semantic map representation, the first C channels store the unique instance ids of the projected objects.
- **p. 4 / IV. GOAT METHOD - extractive body cue:** We take a simple approach: when new observations are received from the sensors, we overwrite the relevant cells in the semantic map based on the ...
- **p. 3 / IV. GOAT METHOD - extractive body cue:** It takes as input the current depth image Dt, RGB image It, and pose reading xt from onboard sensors.
- **p. 4 / IV. GOAT METHOD - extractive body cue:** We use frontierbased exploration [60], which selects the closest unexplored region as the goal. g) Local Policy: Given a long-term goal output by the global ...
- **p. 4 / IV. GOAT METHOD - extractive body cue:** Every time an object oi is detected in the incoming RGB observation I, the depth image is used to project the location of the detected ...

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** This enables GOAT to distinguish between different instances of the same category to enable navigation to targets specified by images and fine-grained language descriptions.

## Source Evidence Cues

- **p. 4 / IV. GOAT METHOD - extractive body cue:** For language goals, we first extract an object category from the language description (by prompting with Mistral 7B [30] in our experiments), then match CLIP ...
- **p. 4 / IV. GOAT METHOD - extractive body cue:** Similarly, for image goals, we first extract an object category from the image with MaskRCNN, then match keypoints of the goal image with keypoints of ...
- **p. 3 / IV. GOAT METHOD - extractive body cue:** If no instance is localized, the global policy outputs an exploration goal.
- **p. 3 / IV. GOAT METHOD - extractive body cue:** In this semantic map representation, the first C channels store the unique instance ids of the projected objects.
- **Detected method headings:** IV. GOAT METHOD (p. 3)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Scene / interaction state | base·arm·object 관계를 표현한다 | egocentric RGB-D, language goal, proprioception | map, object, reachability, contact 또는 affordance state를 구성 | base-arm interaction state | For language goals, we first extract an object category from the language description (by prompting with Mistral 7B [30] in our experiments), ... | p. 4 (IV. GOAT METHOD), p. 4 (IV. GOAT METHOD) |
| Base-arm task decision | 접근·도킹·grasp·manipulation sequence를 결정한다 | interaction state와 task instruction | keypoint, option, trajectory, grasp 또는 joint planning을 수행 | base path plus arm/gripper plan | Similarly, for image goals, we first extract an object category from the image with MaskRCNN, then match keypoints of the goal image ... | p. 4 (IV. GOAT METHOD), p. 3 (IV. GOAT METHOD) |
| Execution / correction | 부분 실행 후 observation으로 계획을 수정한다 | current pose, visual/force feedback | tracking, regrasp, docking correction, recovery 또는 replan을 수행 | next mobile-manipulation action | If no instance is localized, the global policy outputs an exploration goal. | p. 3 (IV. GOAT METHOD), p. 3 (IV. GOAT METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / IV. GOAT METHOD - extractive body cue:** We take a simple approach: when new observations are received from the sensors, we overwrite the relevant cells in the semantic map based on the ...
- **Formal bridge:** base-arm-object state and language/task goal -> base plus arm/gripper action -> long-horizon task utility under reachability/contact constraints -> task completion and recovery.
- **Equation/algorithm anchors:** p. 4 (IV. GOAT METHOD).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | takes, input, current, depth, image, RGB, pose, reading, onboard, sensors, instance, localized, global, policy | egocentric RGB-D, language/task goal, base-arm proprioception | body cue; exact tensor/frame verify |
| State/latent | takes, input, current, depth, image, RGB, pose, reading, onboard, sensors | map/object/contact state와 base-arm coordination decision | body cue; notation verify |
| Action/output | enables, GOAT, distinguish, between, different, instances, same, category, enable, navigation | base motion plus arm/gripper action | body cue; unit/decoder verify |
| Objective/constraint | take, simple, when, observations, received, sensors, overwrite, relevant, cells, semantic | long-horizon task utility under reachability/contact constraints | equation anchor required |

## Observation–State–Action Interface

- **p. 3 / IV. GOAT METHOD - extractive body cue:** It takes as input the current depth image Dt, RGB image It, and pose reading xt from onboard sensors.
- **p. 3 / IV. GOAT METHOD - extractive body cue:** If no instance is localized, the global policy outputs an exploration goal.
- **p. 4 / IV. GOAT METHOD - extractive body cue:** We use frontierbased exploration [60], which selects the closest unexplored region as the goal. g) Local Policy: Given a long-term goal output by the global ...
- **p. 4 / IV. GOAT METHOD - extractive body cue:** Every time an object oi is detected in the incoming RGB observation I, the depth image is used to project the location of the detected ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The next instruction is to Go to a SINK (goal 3), the capitalization emphasizing that any object of the category SINK is a valid goal.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Consider a robot starting in an unseen environment as shown in Figure 1, and suppose it is asked to find a dining table image (goal ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** GOAT's performance can in part be attributed to the modular nature of the system: it leverages learning in the components in which it is required ...
- **Normalized interface:** observation=egocentric RGB-D, language/task goal, base-arm proprioception; state=map/object/contact state와 base-arm coordination decision; output/action=base motion plus arm/gripper action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value was not selected from the PDF body. | For each detected object instance, we also store the image in which the object was detected as part of the object instance ... | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value was not selected from the PDF body. | For example, if the majority of the objects used for training the object detector originated from North America, the system's performance may ... | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value was not selected from the PDF body. | For each detected object instance, we also store the image in which the object was detected as part of the object instance ... | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile was not selected from the PDF body. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- training/inference separation PDF body cue not selected; no claim inferred

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** language, goals, first, extract, object, category, description, prompting, Mistral, experiments, then, match, CLIP, features, instance, inferred, Memory, Similarly, image, MaskRCNN.
- **Relevant PDF headings:** IV. GOAT METHOD (p. 3).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Scene / interaction state | We evaluate the ability of the GOAT agent to tackle the GOAT task, i.e., reach a sequence of unseen multimodal object instances ... | p. 5 (V. RESULTS), p. 5 (V. RESULTS) |
| Base-arm task decision | GOAT w/o memory achieves 61% success rate with an SPL of only 0.19 compared to the 0.64 of GOAT. | p. 5 (V. RESULTS), p. 5 (V. RESULTS) |
| Execution / correction | GOAT w/o memory achieves 61% success rate with an SPL of only 0.19 compared to the 0.64 of GOAT. | p. 5 (V. RESULTS), p. 5 (V. RESULTS) |

## Failure and Ablation Link

- **p. 5 / V. RESULTS - extractive body cue:** Conversely, GOAT without memory shows no improvement from experience, while COW benefits but plateaus at much lower performance.
- **p. 5 / V. RESULTS - extractive body cue:** GOAT w/o Memory, an ablation that resets the semantic map and Object Instance Memory after every goal, allowing us to quantify the benefits of GOAT's ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 7. Online evaluation qualitative trajectories. We compare methods on the same sequence of 5 goals (top) in the same environment. GOAT localizes all goals ...
- **p. 10 / VII. DISCUSSION - extractive body cue:** environment is fully explored, failures are almost exclusively due to failures in matching the correct goal.
- **p. 10 / VII. DISCUSSION - extractive body cue:** The most common failure is a language goal being matched against the an object of the correct class, but the wrong instance (i.e.
- **p. 8 / VII. DISCUSSION - extractive body cue:** a) Modularity allows GOAT to Achieve Robust GeneralPurpose Navigation in the Real World: The GOAT system as a whole is a robust navigation platform, achieving ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (IV. GOAT METHOD), p. 4 (IV. GOAT METHOD), p. 3 (IV. GOAT METHOD), p. 3 (IV. GOAT METHOD), objective p. 4 (IV. GOAT METHOD), temporal p. 3 (IV. GOAT METHOD), p. 10 (VII. DISCUSSION), p. 2 (III. GOAT TASK), p. 2 (III. GOAT TASK), p. 3 (IV. GOAT METHOD), p. 4 (IV. GOAT METHOD).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** If no instance is localized, the global policy outputs an exploration goal. (p. 3, IV. GOAT METHOD).
- **Objective/update evidence:** We take a simple approach: when new observations are received from the sensors, we overwrite the relevant cells in the semantic map based on the updated occupancy information. (p. 4, IV. GOAT METHOD).
- **Temporal/runtime evidence:** For each detected object instance, we also store the image in which the object was detected as part of the object instance memory. c) Semantic Map Representation: The semantic map ... (p. 3, IV. GOAT METHOD).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
