# Method - RoboPanoptes: The All-Seeing Robot with Whole-body Dexterity

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p042.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p042.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 4 (VI. WHOLE-Bopy VisUoMOTOR POLICY), p. 4 (VI. WHOLE-Bopy VisUoMOTOR POLICY)): Using the collected demonstrations, we can train a wholebody visuomotor policy that infers whole-body actions (i.e., rine joint angle sequences) given whole-body vision (i.e., images from 21 cameras).

## Method Body Digest

- **p. 4 / VI. WHOLE-Bopy VisUoMOTOR POLICY - extractive body cue:** Using the collected demonstrations, we can train a wholebody visuomotor policy that infers whole-body actions (i.e., rine joint angle sequences) given whole-body vision (i.e., images ...
- **p. 4 / VI. WHOLE-Bopy VisUoMOTOR POLICY - extractive body cue:** Compared to a common manipulation system, RoboPanoptes needs to handle significantly more complex observation spaces due to the following factors:
- **p. 2 / 1. Ivrropuction - extractive body cue:** Consequently, the policy must efficiently process this complex and high-dimensional input space to infer the appropriate actions.
- **p. 2 / 1. Ivrropuction - extractive body cue:** + A whole-body visuomotor policy that efficiently processes ‘whole-body visual input through cross-attenton transformers and view-dependent positional encoding, while improving resilience to sensor failures through ...
- **p. 4 / V. DATA COLLECTION INTERFACE - extractive body cue:** The joint angles of the leader robot are recorded as target actions, while the images and joint angles of the follower robot are recorded as ...
- **p. 1 / Abstract - extractive body cue:** al feedback of its own and the environment's state.
- **p. 1 / Abstract - extractive body cue:** At its core, RoboPanoptes uses whole-body visuomotor policy that learns complex manipulation s tly from human demonstrations, efficiently aggregating information from the distributed cameras while ...
- **p. 3 / C. Whole-body Sensing - extractive body cue:** [26] further develop a laser-ranging sensor ring design for human-robot interaction, Kim et al.

## Design Rationale

- **p. 2 / 1. Ivrropuction - extractive body cue:** In summary, our primary contribution is the RoboPanoptes system, demonstrating novel whole-body dexterity capabilities through whole-body vision.
- **p. 1 / Abstract - extractive body cue:** We present RoboPanoptes!, a capable yet practical robot system that achieves whole-body dexterity through wholebody vision.
- **p. 3 / IV. MODULAR HARDWARE DESIGN - extractive body cue:** RoboPanoptes' hardware consists of nine modular body units and one head unit.

## Source Evidence Cues

- **p. 4 / VI. WHOLE-Bopy VisUoMOTOR POLICY - extractive body cue:** Using the collected demonstrations, we can train a wholebody visuomotor policy that infers whole-body actions (i.e., rine joint angle sequences) given whole-body vision (i.e., images ...
- **p. 4 / VI. WHOLE-Bopy VisUoMOTOR POLICY - extractive body cue:** Compared to a common manipulation system, RoboPanoptes needs to handle significantly more complex observation spaces due to the following factors:
- **Detected method headings:** VI. WHOLE-Bopy VisUoMOTOR POLICY (p. 4)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Scene / interaction state | base·arm·object 관계를 표현한다 | egocentric RGB-D, language goal, proprioception | map, object, reachability, contact 또는 affordance state를 구성 | base-arm interaction state | Using the collected demonstrations, we can train a wholebody visuomotor policy that infers whole-body actions (i.e., rine joint angle sequences) given whole-body ... | p. 4 (VI. WHOLE-Bopy VisUoMOTOR POLICY), p. 4 (VI. WHOLE-Bopy VisUoMOTOR POLICY) |
| Base-arm task decision | 접근·도킹·grasp·manipulation sequence를 결정한다 | interaction state와 task instruction | keypoint, option, trajectory, grasp 또는 joint planning을 수행 | base path plus arm/gripper plan | Compared to a common manipulation system, RoboPanoptes needs to handle significantly more complex observation spaces due to the following factors: | p. 4 (VI. WHOLE-Bopy VisUoMOTOR POLICY) |
| Execution / correction | 부분 실행 후 observation으로 계획을 수정한다 | current pose, visual/force feedback | tracking, regrasp, docking correction, recovery 또는 replan을 수행 | next mobile-manipulation action | Using the collected demonstrations, we can train a wholebody visuomotor policy that infers whole-body actions (i.e., rine joint angle sequences) given whole-body ... | p. 4 (VI. WHOLE-Bopy VisUoMOTOR POLICY) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- objective/update PDF body cue not selected; no claim inferred - inspect equations and algorithm boxes
- **Formal bridge:** base-arm-object state and language/task goal -> base plus arm/gripper action -> long-horizon task utility under reachability/contact constraints -> task completion and recovery.
- **Equation/algorithm anchors:** none selected.
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Consequently, policy, must, efficiently, process, complex, high-dimensional, input, space, infer, appropriate, actions, whole-body, visuomotor | egocentric RGB-D, language/task goal, base-arm proprioception | body cue; exact tensor/frame verify |
| State/latent | Consequently, policy, must, efficiently, process, complex, high-dimensional, input, space, infer | map/object/contact state와 base-arm coordination decision | body cue; notation verify |
| Action/output | summary, primary, contribution, RoboPanoptes, system, demonstrating, novel, whole-body, dexterity, capabilities | base motion plus arm/gripper action | body cue; unit/decoder verify |
| Objective/constraint | not stated or recoverable in the selected PDF body | long-horizon task utility under reachability/contact constraints | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1. Ivrropuction - extractive body cue:** Consequently, the policy must efficiently process this complex and high-dimensional input space to infer the appropriate actions.
- **p. 2 / 1. Ivrropuction - extractive body cue:** + A whole-body visuomotor policy that efficiently processes ‘whole-body visual input through cross-attenton transformers and view-dependent positional encoding, while improving resilience to sensor failures through ...
- **p. 4 / V. DATA COLLECTION INTERFACE - extractive body cue:** The joint angles of the leader robot are recorded as target actions, while the images and joint angles of the follower robot are recorded as ...
- **p. 4 / VI. WHOLE-Bopy VisUoMOTOR POLICY - extractive body cue:** Using the collected demonstrations, we can train a wholebody visuomotor policy that infers whole-body actions (i.e., rine joint angle sequences) given whole-body vision (i.e., images ...
- **p. 1 / Abstract - extractive body cue:** al feedback of its own and the environment's state.
- **p. 1 / Abstract - extractive body cue:** At its core, RoboPanoptes uses whole-body visuomotor policy that learns complex manipulation s tly from human demonstrations, efficiently aggregating information from the distributed cameras while ...
- **p. 3 / C. Whole-body Sensing - extractive body cue:** [26] further develop a laser-ranging sensor ring design for human-robot interaction, Kim et al.
- **Normalized interface:** observation=egocentric RGB-D, language/task goal, base-arm proprioception; state=map/object/contact state와 base-arm coordination decision; output/action=base motion plus arm/gripper action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | paper-specific horizon; exact value was not selected from the PDF body. | + T4: Introducing random camera latency, with a 10% chance per time step and delays sampled from a uniform distribution L¢(0,0.55) (2 ... | episode/sequence/action-chunk boundary |
| Rate / latency | paper-specific inference/control rate; exact value was not selected from the PDF body. | + T2: Random camera dropout during execution, simulating for each camera a 5% failure rate at each time step (5 rollouts); Le., ... | Hz/fps, inference time and control rate |
| Memory | paper-specific history/state memory; exact value was not selected from the PDF body. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | representation, optimization/inference steps와 hardware가 latency를 결정한다; exact profile was not selected from the PDF body. | + T4: Introducing random camera latency, with a 10% chance per time step and delays sampled from a uniform distribution L¢(0,0.55) (2 ... | hardware, batch and throughput |

## Training vs Inference

- **p. 4 / VI. WHOLE-Bopy VisUoMOTOR POLICY - extractive body cue:** Using the collected demonstrations, we can train a wholebody visuomotor policy that infers whole-body actions (i.e., rine joint angle sequences) given whole-body vision (i.e., images ...
- **p. 9 / B. Sweeping Task - extractive body cue:** + ResNet Encodes: A whole-body visuomotor policy with a ResNet-34 [15] vision encoder trained from seratch instead of using a pretrained vision encoder.

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** collected, demonstrations, train, wholebody, visuomotor, policy, infers, whole-body, actions, rine, joint, angle, sequences, given, vision, images, cameras, Compared, common, manipulation.
- **Relevant PDF headings:** VI. WHOLE-Bopy VisUoMOTOR POLICY (p. 4).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Scene / interaction state | Performance: ‘The training dataset contains 147 demonstration episodes, with each demonstration averaging 15s. | p. 7 (A. Unboxing Task), p. 8 (B. Sweeping Task) |
| Base-arm task decision | overall 94.4% success rate, outperforming all baselines. | p. 8 (A. Unboxing Task), p. 4 (VI. WHOLE-Bopy VisUoMOTOR POLICY) |
| Execution / correction | RoboPanoptes achieves a 96.6% success rate, outperforming all baselines. | p. 9 (B. Sweeping Task), p. 9 (C. Stowing Task) |

## Failure and Ablation Link

- **p. 6 / VII. PRACTICAL Cons - extractive body cue:** Variants using all of RoboPanoptes' cameras but without view-dependent pesitional encoding or without blink traning serve as ablations of our design.
- **p. 6 / VII. PRACTICAL Cons - extractive body cue:** In contrast, USB cameras provide a reliable and standardized interface and, through UVC, are compatible across a wide range of devices without the need for ...
- **p. 7 / A. Unboxing Task - extractive body cue:** + w/o Blink Training: A whole-body visuomotor policy trained without randomized camera dropouts.
- **p. 7 / A. Unboxing Task - extractive body cue:** + w/o Camera Pose: A whole-body visuomotor policy trained without view-dependent positional encoding.
- **p. 8 / B. Sweeping Task - extractive body cue:** For sweeping a large object, the task success rate is measured by whether the object is dragged into the target zone without being knocked down.
- **p. 9 / C. Stowing Task - extractive body cue:** before, one using only a top-down camera and one without
- **p. 9 / B. Sweeping Task - extractive body cue:** Occasionally, we observe the robot getting stuck in a pose without interacting with any object.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (VI. WHOLE-Bopy VisUoMOTOR POLICY), p. 4 (VI. WHOLE-Bopy VisUoMOTOR POLICY), objective 본문 anchor 없음, temporal p. 7 (A. Unboxing Task), p. 7 (A. Unboxing Task), p. 4 (V. DATA COLLECTION INTERFACE), p. 5 (21 Whole), p. 5 (21 Whole), p. 6 (21 Whole).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (13 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** + A whole-body visuomotor policy that efficiently processes ‘whole-body visual input through cross-attenton transformers and view-dependent positional encoding, while improving resilience to sensor failures through blink training Our ha ... (p. 2, 1. Ivrropuction).
- **Objective/update evidence:** Compared to a common manipulation system, RoboPanoptes needs to handle significantly more complex observation spaces due to the following factors: (p. 4, VI. WHOLE-Bopy VisUoMOTOR POLICY).
- **Temporal/runtime evidence:** + T4: Introducing random camera latency, with a 10% chance per time step and delays sampled from a uniform distribution L¢(0,0.55) (2 rollouts). (p. 7, A. Unboxing Task).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
