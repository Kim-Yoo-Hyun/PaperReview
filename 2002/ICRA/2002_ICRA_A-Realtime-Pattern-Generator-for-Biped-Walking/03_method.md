# Method - A Realtime Pattern Generator for Biped Walking

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/ROBOT.2002.1013335; PDF retrieval source: https://www.cs.cmu.edu/~cga/legs/kuff1e.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction)): In this paper, we take the standpoint of the second approach, and introduce a new modeling which represents the dynamics of a robot with limited parameters.

## Method Body Digest

- **p. 1 / 1 Introduction - extractive body cue:** In this paper, we take the standpoint of the second approach, and introduce a new modeling which represents the dynamics of a robot with limited ...
- **p. 2 / 1 Introduction - extractive body cue:** Let (τr, τp, f) be the actuator torque and force associated with the state variables (θr, θp, r).
- **p. 3 / 1 Introduction - extractive body cue:** Therefore, the 3D-LIPM with zero input torque can be considered as a dynamics under the central force field.
- **p. 3 / 1 Introduction - extractive body cue:** Since the 3DLIPM is a dynamics under the central force field, the motion along Y ′ and X′ is also governed by the identical equations ...
- **p. 1 / 1 Introduction - extractive body cue:** Therefore, it mainly relies on the accuracy of the model data [3, 5, 10, 14].
- **p. 2 / 1 Introduction - extractive body cue:** (11) Therefore, we have the same dynamics of Eq.
- **p. 4 / 1 Introduction - extractive body cue:** The initial body state (x(n) i , v(n) i ) and the final body state (x(n) f , v(n) f ) have the relationship given ...
- **p. 1 / 1 Introduction - extractive body cue:** 2 Derivation of 3D Linear Inverted Pendulum Mode 2.1 Motion equation of a 3D inverted pendulum When a biped robot is supporting its body on ...

## Design Rationale

- **p. 1 / 1 Introduction - extractive body cue:** It allows a separate controller design for the sagittal (x-z) and the lateral (y-z) motions and simplifies a walking pattern generation a great deal.

## Source Evidence Cues

- **p. 1 / 1 Introduction - extractive body cue:** In this paper, we take the standpoint of the second approach, and introduce a new modeling which represents the dynamics of a robot with limited ...
- **p. 2 / 1 Introduction - extractive body cue:** Let (τr, τp, f) be the actuator torque and force associated with the state variables (θr, θp, r).
- **p. 3 / 1 Introduction - extractive body cue:** Therefore, the 3D-LIPM with zero input torque can be considered as a dynamics under the central force field.
- **p. 3 / 1 Introduction - extractive body cue:** Since the 3DLIPM is a dynamics under the central force field, the motion along Y ′ and X′ is also governed by the identical equations ...
- **p. 1 / 1 Introduction - extractive body cue:** Therefore, it mainly relies on the accuracy of the model data [3, 5, 10, 14].
- **p. 2 / 1 Introduction - extractive body cue:** (11) Therefore, we have the same dynamics of Eq.
- **p. 4 / 1 Introduction - extractive body cue:** The initial body state (x(n) i , v(n) i ) and the final body state (x(n) f , v(n) f ) have the relationship given ...
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | In this paper, we take the standpoint of the second approach, and introduce a new modeling which represents the dynamics of a ... | p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | Let (τr, τp, f) be the actuator torque and force associated with the state variables (θr, θp, r). | p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | Therefore, the 3D-LIPM with zero input torque can be considered as a dynamics under the central force field. | p. 3 (1 Introduction), p. 3 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 1 / 1 Introduction - extractive body cue:** 2 Derivation of 3D Linear Inverted Pendulum Mode 2.1 Motion equation of a 3D inverted pendulum When a biped robot is supporting its body on ...
- **p. 2 / 1 Introduction - extractive body cue:** (4) Substituting these constraints into Eqs.
- **p. 2 / 1 Introduction - extractive body cue:** (9) and (10) are independent linear equations.
- **p. 3 / 1 Introduction - extractive body cue:** (14) With a given initial condition, these equations determine trajectories in 3D space.
- **p. 3 / 1 Introduction - extractive body cue:** Since the 3DLIPM is a dynamics under the central force field, the motion along Y ′ and X′ is also governed by the identical equations ...
- **p. 4 / 1 Introduction - extractive body cue:** (16) into this definition and calculating the foothold of x(2) i which minimizes N, we obtain a proper control law, x(2) i = (aCT (xd ...
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Let, actuator, torque, force, associated, state, variables, Therefore, D-LIPM, zero, input, considered, dynamics, under | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | Let, actuator, torque, force, associated, state, variables, Therefore, D-LIPM, zero | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | allows, separate, controller, design, sagittal, lateral, motions, simplifies, walking, pattern | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | Derivation, Linear, Inverted, Pendulum, Mode, Motion, equation, When, biped, robot | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / 1 Introduction - extractive body cue:** Let (τr, τp, f) be the actuator torque and force associated with the state variables (θr, θp, r).
- **p. 3 / 1 Introduction - extractive body cue:** Therefore, the 3D-LIPM with zero input torque can be considered as a dynamics under the central force field.
- **p. 3 / 1 Introduction - extractive body cue:** and Tani introduced a two-dimensional version of this dynamics mode[6], and Hara, Yokokawa and Sadao extended it to three dimensions in the case of zero ...
- **p. 1 / 1 Introduction - extractive body cue:** Since the controller knows little about the system structure, this approach much relies on a feedback control [1, 6, 9, 12, 13, 15].
- **p. 1 / Abstract - extractive body cue:** Experimental results of realtime walking control of a 12 d.o.f. biped robot HRP-2L using an input device such as a game pad are also shown.
- **p. 2 / 1 Introduction - extractive body cue:** (10) in the case of an inclined constraint plane when the following new constraint is introduced about the inputs as, urx + upy = 0.
- **p. 4 / 1 Introduction - extractive body cue:** The initial body state (x(n) i , v(n) i ) and the final body state (x(n) f , v(n) f ) have the relationship given ...
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | Input Device Server Measured joint angles Control values Goal joint angles Desired pose and ZMP Request Input Device State Foothold, Rotational angle ... | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | From straightforward calculations, we get ¨y = g zc y -kx zc (x¨y -¨xy) - 1 mzc ur, (5) ¨x = g ... | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not recovered | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | Input Device Server Measured joint angles Control values Goal joint angles Desired pose and ZMP Request Input Device State Foothold, Rotational angle ... | hardware, batch and throughput |

## Training vs Inference

- training/inference separation cue 없음

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** take, standpoint, second, introduce, modeling, represents, dynamics, robot, limited, parameters, Let, actuator, torque, force, associated, state, variables, Therefore, D-LIPM, zero.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | of realtime bipped walking 4.1 Biped robot HRP-2L The biped robot HRP-2L, which is the leg module for HRP-21, is used for ... | p. 5 (4 Experiments), p. 5 (4 Experiments) |
| Balance-aware whole-body execution | no linked comparison cue | 본문 anchor 없음 |
| Recovery / adaptation | From the experimental results, the effectiveness of the proposed realtime walk generation method was confirmed. | p. 6 (4 Experiments), p. 6 (4 Experiments) |

## Failure and Ablation Link

- **p. 6 / 4 Experiments - extractive body cue:** Although we assume an ideal robot, which can step towards any direction at all time, in the former section, HRP-2L has the limit of joint ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), objective p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), temporal p. 6 (4 Experiments), p. 2 (1 Introduction), p. 5 (4 Experiments), p. 6 (4 Experiments), p. 5 (C D), p. 2 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?
