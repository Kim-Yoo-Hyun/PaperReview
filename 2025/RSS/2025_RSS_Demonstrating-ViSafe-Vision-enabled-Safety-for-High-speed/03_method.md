# Method - Demonstrating ViSafe: Vision-enabled Safety for High-speed Detect and Avoid

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (13 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p002.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p002.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Method in One Sentence

PDF body method statement (p. 7 (C. Supervisory Safety Controller), p. 6 (C. Supervisory Safety Controller), p. 6 (C. Supervisory Safety Controller)): We use a simple PD controller as our nominal controller, where the computed desired safe control ujaje is then converted into low-level drone control actions in the form of velocity ...

## Method Body Digest

- **p. 7 / C. Supervisory Safety Controller - extractive body cue:** We use a simple PD controller as our nominal controller, where the computed desired safe control ujaje is then converted into low-level drone control actions ...
- **p. 6 / C. Supervisory Safety Controller - extractive body cue:** Our supervisory controller enforces our safety and actuation constraints, We devise this controller using our defined control barrier function, First, let our safe set be ...
- **p. 6 / C. Supervisory Safety Controller - extractive body cue:** Considering these three key requirements, we used a Control Barrier Function (CBF) based Quadratic Program (QP) for our supervisory safety controller.
- **p. 6 / C. Supervisory Safety Controller - extractive body cue:** Note that the non-linear constraint h(x) <0 is not necessarily a subset of d > dhiresk when d > 0.
- **p. 7 / C. Supervisory Safety Controller - extractive body cue:** As can be observed, the constraints on hare affine in w and fit the form of a QP, as defined in Eq.
- **p. 2 / 4) First-of-its-kind real-world flight tests demonstrating that - extractive body cue:** These logics involve generating cost tables for agent states and possible actions through simulation and optimization [8].
- **p. 2 / 2) Custom-built SWaP-C hardware that simultaneously - extractive body cue:** streams multiple camera inputs, provides state estimation, performs deep learning model edge inference, and computes avoidance maneuvers on board in real time.
- **p. 4 / IV. ViSafe FRAMEWORK - extractive body cue:** 2) is as follows: While the visual detection module (Seetion IV-A) provides an mage-level intruder detection, the intruder state information is transformed to the North ...

## Design Rationale

- **p. 2 / 4) First-of-its-kind real-world flight tests demonstrating that - extractive body cue:** There are variants of this algorithm for different agent types in different airspaces (ACAS Xa, Xu), etc. ‘The key factor driving the development of ACAS ...
- **p. 1 / Abstract - extractive body cue:** Assured safe-separation is essential for achi y operatloa of alrborve vehicles in a shared ip resource-constrained aerial systems with this fty-critical capability, we present ViSafe, ...
- **p. 2 / I. INTRopI - extractive body cue:** We present ViSafe, a vision-only airborne collision avoidance system to impart see-and-avoid capabilities to sUAS.

## Source Evidence Cues

- **p. 7 / C. Supervisory Safety Controller - extractive body cue:** We use a simple PD controller as our nominal controller, where the computed desired safe control ujaje is then converted into low-level drone control actions ...
- **p. 6 / C. Supervisory Safety Controller - extractive body cue:** Our supervisory controller enforces our safety and actuation constraints, We devise this controller using our defined control barrier function, First, let our safe set be ...
- **p. 6 / C. Supervisory Safety Controller - extractive body cue:** Considering these three key requirements, we used a Control Barrier Function (CBF) based Quadratic Program (QP) for our supervisory safety controller.
- **Detected method headings:** C. Supervisory Safety Controller (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF cue | Anchor |
|---|---|---|---|---|---|---|
| Risk / failure representation | unsafe state와 uncertainty를 계산한다 | observation, nominal command, history | barrier, risk model, failure classifier, uncertainty 또는 safe set을 추정 | risk/margin/failure state | We use a simple PD controller as our nominal controller, where the computed desired safe control ujaje is then converted into low-level ... | p. 7 (C. Supervisory Safety Controller), p. 6 (C. Supervisory Safety Controller) |
| Filtering / recovery | nominal command를 안전 command로 바꾼다 | nominal action과 safety constraint | QP shield, backup policy, correction, stop 또는 recovery plan을 선택 | safe/recovery action | Our supervisory controller enforces our safety and actuation constraints, We devise this controller using our defined control barrier function, First, let our ... | p. 6 (C. Supervisory Safety Controller), p. 6 (C. Supervisory Safety Controller) |
| Monitoring / re-entry | 실행 결과를 다시 risk decision에 반영한다 | executed action과 next observation | threshold, update, replan, abort 또는 return-to-task를 수행 | continue/correct/abort state | Considering these three key requirements, we used a Control Barrier Function (CBF) based Quadratic Program (QP) for our supervisory safety controller. | p. 6 (C. Supervisory Safety Controller) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 6 / C. Supervisory Safety Controller - extractive body cue:** Our supervisory controller enforces our safety and actuation constraints, We devise this controller using our defined control barrier function, First, let our safe set be ...
- **p. 6 / C. Supervisory Safety Controller - extractive body cue:** Note that the non-linear constraint h(x) <0 is not necessarily a subset of d > dhiresk when d > 0.
- **p. 7 / C. Supervisory Safety Controller - extractive body cue:** As can be observed, the constraints on hare affine in w and fit the form of a QP, as defined in Eq.
- **Formal bridge:** state/history and risk h(s) -> filtered/recovery action u_safe -> task utility subject to safety constraint -> low violation/failure probability with useful intervention.
- **Equation/algorithm anchors:** p. 6 (C. Supervisory Safety Controller), p. 6 (C. Supervisory Safety Controller), p. 7 (C. Supervisory Safety Controller).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | logics, involve, generating, cost, tables, agent, states, possible, actions, through, simulation, optimization, streams, multiple | observation, uncertainty/risk estimate와 task command | body cue; exact tensor/frame verify |
| State/latent | logics, involve, generating, cost, tables, agent, states, possible, actions, through | safe set, recovery state 또는 constraint margin | body cue; notation verify |
| Action/output | There, variants, algorithm, different, agent, types, airspaces, ACAS, factor, driving | shielded, recovery 또는 safe action | body cue; unit/decoder verify |
| Objective/constraint | supervisory, controller, enforces, safety, actuation, constraints, devise, defined, control, barrier | task utility subject to safety constraint | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 4) First-of-its-kind real-world flight tests demonstrating that - extractive body cue:** These logics involve generating cost tables for agent states and possible actions through simulation and optimization [8].
- **p. 2 / 2) Custom-built SWaP-C hardware that simultaneously - extractive body cue:** streams multiple camera inputs, provides state estimation, performs deep learning model edge inference, and computes avoidance maneuvers on board in real time.
- **p. 4 / IV. ViSafe FRAMEWORK - extractive body cue:** 2) is as follows: While the visual detection module (Seetion IV-A) provides an mage-level intruder detection, the intruder state information is transformed to the North ...
- **p. 1 / Abstract - extractive body cue:** By leveraging perceptual. input-focused ‘control barrier functions (CBF) to design, encode, and enforce safety thresholds, ViSafe can provide provably safe runtime guarantees for self-separation in ...
- **p. 3 / 4) First-of-its-kind real-world flight tests demonstrating that - extractive body cue:** Moreover, our technique can factor in nominal control inputs, which incorporate the liveness requirement of reaching a goal.
- **p. 3 / B. Control Barrier Functions for Aerial Collision Avoidance - extractive body cue:** In these modular approaches, frame ‘optical flow or image registration methods [35, 45, 48], while regression-based motion compensation and morphological operations were utilized to highlight ...
- **p. 4 / IV. ViSafe FRAMEWORK - extractive body cue:** This modified control action is then ‘converted into low-level drone commands and executed
- **Normalized interface:** observation=observation, uncertainty/risk estimate와 task command; state=safe set, recovery state 또는 constraint margin; output/action=shielded, recovery 또는 safe action.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 현재 command의 one-step safety 또는 recovery trajectory horizon; exact lookahead 확인 필요. | Furthermore, we also upgraded the SWaP-C hardware, implementing efficient multi-camera image sharing (with zero memory copies) and further opti mizing the deep ... | episode/sequence/action-chunk boundary |
| Rate / latency | nominal policy와 safety monitor/filter의 runtime rate를 별도로 기록한다. | Additionally, since our visual detection module can be sensitive to the intruder being above or below the horizon, we investigate both possibilities ... | Hz/fps, inference time and control rate |
| Memory | risk score, recent trajectory/history와 recovery state. | Furthermore, we also upgraded the SWaP-C hardware, implementing efficient multi-camera image sharing (with zero memory copies) and further opti mizing the deep ... | window and reset |
| Compute | risk inference, barrier/QP solve 또는 backup policy selection이 latency를 결정한다. | Each 3D intruder track is configured to propagate the intruder position and velocity to the downstream supervisory safety controller at a frequency ... | hardware, batch and throughput |

## Training vs Inference

- **p. 6 / C. Supervisory Safety Controller - extractive body cue:** Our supervisory controller enforces our safety and actuation constraints, We devise this controller using our defined control barrier function, First, let our safe set be ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** simple, controller, nominal, where, computed, desired, safe, control, ujaje, then, converted, low-level, drone, actions, form, velocity, setpoints, executed, ownship, agent.
- **Relevant PDF headings:** C. Supervisory Safety Controller (p. 6).
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Risk / failure representation | These experiments are performed in both a high-fidelity digital-twin simulation and real-world settings. | p. 7 (A. Experiment Design), p. 7 (A. Experiment Design) |
| Filtering / recovery | Fig. 6. Horizontal rate of closure comparisons across diferent weather conditions in the digital twin: Higher values ind apart, showcasing diverging & ... | p. 10 (Figure/Table caption) |
| Monitoring / re-entry | 3) Inaecuracies in vision-based inference: Vision-based state estimation is not perfect; therefore, false positives can often throw the safety module off, We ... | p. 10 (VI. LEARNED CHALLENGES AND LIMITATIONS), p. 7 (A. Experiment Design) |

## Failure and Ablation Link

- **p. 10 / VI. LEARNED CHALLENGES AND LIMITATIONS - extractive body cue:** 3) Inaecuracies in vision-based inference: Vision-based state estimation is not perfect; therefore, false positives can often throw the safety module off, We had to use ...
- **p. 7 / A. Experiment Design - extractive body cue:** The ViSafeenabled ego agent is tested against an airborne intruder in various collision geometries.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 4. These experiments are performed in both a high-fidelity digital-twin simulation and real-world settings. Table I shows the various agents, collision geometries, commanded ground ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **PDF anchors reviewed:** method p. 7 (C. Supervisory Safety Controller), p. 6 (C. Supervisory Safety Controller), p. 6 (C. Supervisory Safety Controller), objective p. 6 (C. Supervisory Safety Controller), p. 6 (C. Supervisory Safety Controller), p. 7 (C. Supervisory Safety Controller), temporal p. 4 (A. Visual Detection Module), p. 7 (A. Experiment Design), p. 5 (B. Multi View Fusion & Coordinate Frame Conversion), p. 6 (C. Supervisory Safety Controller), p. 1 (Abstract), p. 1 (Abstract).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
