# Method - Certifiably-Correct Mapping for Safe Navigation Despite Odometry Drift

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p007.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p007.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 1 (Abstract)): Accurate state estimation and mapping are essential for safe robotic navigation, as planners and controllers rely on perception outputs to ensure the safety of planned trajectories (or control actions.

## Method Body Digest

- **p. 1 / 1. INTRODUCTION - extractive body cue:** Accurate state estimation and mapping are essential for safe robotic navigation, as planners and controllers rely on perception outputs to ensure the safety of planned ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** In Section IV and V we introduce the deflation mechanism for both map representations, In Section VI we propose methods to use the certified maps ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** Assuming the odometry algorithm reports the pose and the covariance of the incremental transform, we propose deflating the supposedly safe region (Sc. is deflated relative ...
- **p. 1 / Abstract - extractive body cue:** Accurate perception, state estimation and mapping, are essential for safe robotic navigation as planners and con- {rollers rely on these components for safety-critical decisions.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Overview of notation and objectives.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Various methods have been developed to certify that controllers meet predefined safety specifications [1, 2], and when real-time obstacle detection is necessary, it is often ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** The primary goals of these advancements have been to enhance localization and mapping accuracy, improve robustness under diverse environmental conditions, and develop algorithms with lower ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** These methods reduce odometry drift by optimizing each submap within its own coordinate frame.

## Design Rationale

- **p. 2 / 1. INTRODUCTION - extractive body cue:** In Section IV and V we introduce the deflation mechanism for both map representations, In Section VI we propose methods to use the certified maps ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** In contrast to [27], this paper assumes that the incremental pose estimate is bounded in a Lie-algebraic sense, which allows ‘our methods to be applied ...
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Our main contributions are as follows:

## Source Evidence Cues

- **p. 1 / 1. INTRODUCTION - extractive body cue:** Accurate state estimation and mapping are essential for safe robotic navigation, as planners and controllers rely on perception outputs to ensure the safety of planned ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** In Section IV and V we introduce the deflation mechanism for both map representations, In Section VI we propose methods to use the certified maps ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** Assuming the odometry algorithm reports the pose and the covariance of the incremental transform, we propose deflating the supposedly safe region (Sc. is deflated relative ...
- **p. 1 / Abstract - extractive body cue:** Accurate perception, state estimation and mapping, are essential for safe robotic navigation as planners and con- {rollers rely on these components for safety-critical decisions.
- **Detected method headings:** B. Proposed Approach (p. 5); B. Proposed Approach (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Map / localization state | sensor stream을 pose와 world map으로 누적한다 | camera/depth/LiDAR, odometry, history | mapping, localization, scene graph 또는 map update를 수행 | pose/map/free-space state | Accurate state estimation and mapping are essential for safe robotic navigation, as planners and controllers rely on perception outputs to ensure the ... | p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION) |
| Global / local decision | goal과 risk를 고려해 route를 정한다 | map, goal, obstacle/risk estimate | graph search, local planning, language grounding 또는 replanning을 수행 | path/waypoint/local goal | In Section IV and V we introduce the deflation mechanism for both map representations, In Section VI we propose methods to use ... | p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION) |
| Motion execution / recovery | route를 velocity/action으로 실행하고 실패에 대응한다 | path와 current pose/feedback | tracking, collision check, recovery 또는 replan을 수행 | velocity/base command | Assuming the odometry algorithm reports the pose and the covariance of the incremental transform, we propose deflating the supposedly safe region (Sc. ... | p. 2 (1. INTRODUCTION), p. 1 (Abstract) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / 1. INTRODUCTION - extractive body cue:** Overview of notation and objectives.
- **p. 1 / 1. INTRODUCTION - extractive body cue:** Various methods have been developed to certify that controllers meet predefined safety specifications [1, 2], and when real-time obstacle detection is necessary, it is often ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** The primary goals of these advancements have been to enhance localization and mapping accuracy, improve robustness under diverse environmental conditions, and develop algorithms with lower ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** These methods reduce odometry drift by optimizing each submap within its own coordinate frame.
- **Formal bridge:** sensor/map state and goal -> path/waypoint/velocity -> path cost, risk or goal utility -> goal reach with collision-free execution.
- **Equation/algorithm anchors:** p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Accurate, state, estimation, mapping, essential, safe, robotic, navigation, planners, controllers, rely, perception, outputs, ensure | camera/depth stream, pose, map와 language goal | body cue; exact tensor/frame verify |
| State/latent | Accurate, state, estimation, mapping, essential, safe, robotic, navigation, planners, controllers | robot pose, free-space/semantic map와 local goal | body cue; notation verify |
| Action/output | Section, introduce, deflation, mechanism, representations, methods, certified, maps, acheive, safe | collision-free trajectory 또는 velocity command | body cue; unit/decoder verify |
| Objective/constraint | Overview, notation, objectives, Various, methods, have, been, developed, certify, controllers | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 1 / 1. INTRODUCTION - extractive body cue:** Accurate state estimation and mapping are essential for safe robotic navigation, as planners and controllers rely on perception outputs to ensure the safety of planned ...
- **p. 1 / 1. INTRODUCTION - extractive body cue:** (6) depicts the map produced by curret state-of-the-art methods, where dae to edometry dif the map is eoncous: aie thatthe safe region (axonding to the ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** + We prove the correctness and applicability ofthis frame~ \work on two popular and state-of-the-art mapping frameworks: the polytopic SFCs of [8] and the ESDFs ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** + Beyond providing the theoretical analysis and proofs of correctness, we validate and compare our approach with state-of the-art baseline methods through extensive simulations on ...
- **Normalized interface:** observation=camera/depth stream, pose, map와 language goal; state=robot pose, free-space/semantic map와 local goal; output/action=collision-free trajectory 또는 velocity command.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | map-level start-goal plan과 local controller horizon을 계층적으로 분리한다. | By deflating the safe region based on the incremental odometry error at each timestep, we ensure that the map remains accurate and ... | episode/sequence/action-chunk boundary |
| Rate / latency | mapping/localization, global planner, local planner와 base controller rate를 구분한다. | (D) depicts the ideal ‘mapping outpu, where a the kth timestep the map Vy is composed of the Krnoven safe region Sy ... | Hz/fps, inference time and control rate |
| Memory | map/scene graph, pose history와 current local goal. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | map update, collision checking, path search와 replanning frequency가 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / 1. INTRODUCTION - extractive body cue:** In these systems, raw measurements are typically processed by a frontend into a more compact representation, while a backend uses nonlinear optimization methods to compute ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** Accurate, state, estimation, mapping, essential, safe, robotic, navigation, planners, controllers, rely, perception, outputs, ensure, safety, planned, trajectories, control, actions, Section.
- **Relevant PDF headings:** B. Proposed Approach (p. 5); B. Proposed Approach (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Map / localization state | Real-world experiments with a robotic rover show that, while baseline methods result in collisions with previously mapped obstacles, the proposed framework enables ... | p. 1 (Abstract), p. 2 (1. INTRODUCTION) |
| Global / local decision | Simulations using the Replica dataset highlight the efficacy of our methods compared to state of-the-art techniques. | p. 1 (Abstract), p. 1 (Abstract) |
| Motion execution / recovery | Although recent advances have achieved significant accuracy improvements (11, 12, 13, 14, 15}, formal error analysis is often lacking. | p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION) |

## Failure and Ablation Link

- **p. 1 / 1. INTRODUCTION - extractive body cue:** Without quantified error bounds, guaranteeing the safety of a closed-loop robotic system remains a challenge.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** Instead, by deflating a safe region Sj, the region that is certifiably safe shrinks, eventually becomes an empty set, and is removed from memory (i... ...
- **p. 1 / Abstract - extractive body cue:** Accurate perception, state estimation and mapping, are essential for safe robotic navigation as planners and con- {rollers rely on these components for safety-critical decisions.
- **p. 1 / Abstract - extractive body cue:** However, existing mapping approaches often assume perfect pose estimates, an unrealistic assumption that ean lead to incorrect fbstacle maps and therefore collisions.
- **p. 1 / Abstract - extractive body cue:** Real-world experiments with a robotic rover show that, while baseline methods result in collisions with previously mapped obstacles, the proposed framework enables the rover to ...
- **p. 2 / 1. INTRODUCTION - extractive body cue:** The rover uses an onboard safety filter to prevent collisions.
- **p. 2 / 1. INTRODUCTION - extractive body cue:** Unlike baseline methods which result in collisions, our approach prevents crashes by deflating the safe regions appropriately.

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 1 (Abstract), objective p. 1 (1. INTRODUCTION), p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), temporal p. 1 (Abstract), p. 1 (1. INTRODUCTION), p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (24 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Accurate state estimation and mapping are essential for safe robotic navigation, as planners and controllers rely on perception outputs to ensure the safety of planned trajectories (or control actions. (p. 1, 1. INTRODUCTION).
- **Objective/update evidence:** Overview of notation and objectives. (p. 1, 1. INTRODUCTION).
- **Temporal/runtime evidence:** These methods reduce odometry drift by optimizing each submap within its own coordinate frame. (p. 2, experimental results).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
