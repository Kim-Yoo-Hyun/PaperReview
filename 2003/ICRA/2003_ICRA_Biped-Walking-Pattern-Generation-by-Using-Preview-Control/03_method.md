# Method - Biped Walking Pattern Generation by using Preview Control of Zero-Moment Point

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/ROBOT.2003.1241826; PDF retrieval source: https://doi.org/10.1109/ROBOT.2003.1241826. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 1 (Abstract), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction)): First, the dynamics of a biped robot is modeled as a running cart on a table which gives a convenient representation to treat ZMP.

## Method Body Digest

- **p. 1 / Abstract - extractive body cue:** First, the dynamics of a biped robot is modeled as a running cart on a table which gives a convenient representation to treat ZMP.
- **p. 2 / 1 Introduction - extractive body cue:** It is also shown that by using the preview controller, we can take into account of the precise multibody dynamics although our method is based ...
- **p. 4 / 1 Introduction - extractive body cue:** To obtain a smooth ZMP trajectory in double support, we used cubic spline.
- **p. 3 / 1 Introduction - extractive body cue:** However, we must consider an xu ZMP reference Servo Controller Dynamic ZMP equation (12) p ref p x + - p ZMP CoM Figure 4: ...
- **p. 1 / 1 Introduction - extractive body cue:** The first group requires the precise knowledge of robot dynamics including mass, location of center of mass and inertia of each link to prepare walking ...
- **p. 2 / 1 Introduction - extractive body cue:** (7) 2.2 ZMP equations and cart-table model To control the ZMP, it should be the outputs of the system while it appears as the inputs ...
- **p. 3 / 1 Introduction - extractive body cue:** Then the inverse FFT returns the resulted CoM trajectory into time domain.
- **p. 2 / 1 Introduction - extractive body cue:** (10) We can verify that this yields the same equation to Eq.

## Design Rationale

- **p. 2 / 1 Introduction - extractive body cue:** In this paper we introduce a novel walking pattern generation that allows arbitrary foot placements as a mixture of the ZMP based and the inverted ...
- **p. 1 / 1 Introduction - extractive body cue:** However, since our method generated a stable gait by changing foot placements from the original assignment, it was not applicable to a situation like a ...
- **p. 2 / 1 Introduction - extractive body cue:** It is also shown that by using the preview controller, we can take into account of the precise multibody dynamics although our method is based ...

## Source Evidence Cues

- **p. 1 / Abstract - extractive body cue:** First, the dynamics of a biped robot is modeled as a running cart on a table which gives a convenient representation to treat ZMP.
- **p. 2 / 1 Introduction - extractive body cue:** It is also shown that by using the preview controller, we can take into account of the precise multibody dynamics although our method is based ...
- **p. 4 / 1 Introduction - extractive body cue:** To obtain a smooth ZMP trajectory in double support, we used cubic spline.
- **p. 3 / 1 Introduction - extractive body cue:** However, we must consider an xu ZMP reference Servo Controller Dynamic ZMP equation (12) p ref p x + - p ZMP CoM Figure 4: ...
- **p. 1 / 1 Introduction - extractive body cue:** The first group requires the precise knowledge of robot dynamics including mass, location of center of mass and inertia of each link to prepare walking ...
- **p. 2 / 1 Introduction - extractive body cue:** (7) 2.2 ZMP equations and cart-table model To control the ZMP, it should be the outputs of the system while it appears as the inputs ...
- **p. 3 / 1 Introduction - extractive body cue:** Then the inverse FFT returns the resulted CoM trajectory into time domain.
- **Detected method headings:** none reliably recovered

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Reference / embodiment interface | human/task reference를 robot-compatible state로 바꾼다 | reference motion, visual/language input, body state | retargeting, pose/skill conditioning 또는 multimodal encoding을 수행 | whole-body context | First, the dynamics of a biped robot is modeled as a running cart on a table which gives a convenient representation to ... | p. 1 (Abstract), p. 2 (1 Introduction) |
| Balance-aware whole-body execution | reference를 contact·balance-aware command로 변환한다 | context, body state, contact | policy, WBC, inverse dynamics 또는 hierarchical control을 적용 | joint target/torque | It is also shown that by using the preview controller, we can take into account of the precise multibody dynamics although our ... | p. 2 (1 Introduction), p. 4 (1 Introduction) |
| Recovery / adaptation | mismatch·disturbance·fall 뒤 behavior를 복구한다 | feedback/history와 failure state | adaptation, motion completion, reinitialization 또는 safe stop을 수행 | recovery command | To obtain a smooth ZMP trajectory in double support, we used cubic spline. | p. 4 (1 Introduction), p. 3 (1 Introduction) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / 1 Introduction - extractive body cue:** (10) We can verify that this yields the same equation to Eq.
- **p. 2 / 1 Introduction - extractive body cue:** (9) In the following part of this paper, we will refer the above equations as the ZMP equations.
- **p. 3 / 1 Introduction - extractive body cue:** By applying the Fast Fourier Transformation (FFT) to the ZMP reference, the ZMP equations can be solved in frequency domain.
- **p. 3 / 1 Introduction - extractive body cue:** They showed the ZMP equation can be discretized as a trinomial expression, and it can be efficiently solved by an algorithm of O(N) for the ...
- **p. 4 / 1 Introduction - extractive body cue:** When the ZMP reference can be previewed for NL step future at every sampling time, the optimal controller which minimizes the performance index (14) is ...
- **p. 4 / 1 Introduction - extractive body cue:** Although this sounds curious, we don't have to violate the law of causality.
- **Formal bridge:** whole-body pose/contact/reference state -> joint/whole-body action -> tracking/balance/task objective -> motion/task success and recovery.
- **Equation/algorithm anchors:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | preview, control, made, three, terms, integral, action, tracking, error, state, feedback, future, reference, ZMP | proprioception, reference pose/motion, visual or language command | body cue; exact tensor/frame verify |
| State/latent | preview, control, made, three, terms, integral, action, tracking, error, state | whole-body pose, balance/contact state와 skill/mode | body cue; notation verify |
| Action/output | introduce, novel, walking, pattern, generation, allows, arbitrary, foot, placements, mixture | joint/whole-body action, motion target 또는 task trajectory | body cue; unit/decoder verify |
| Objective/constraint | verify, yields, same, equation, following, part, will, refer, above, equations | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 1 Introduction - extractive body cue:** The preview control is made of three terms, the integral action on the tracking error, the state feedback and the preview action using the future ...
- **p. 2 / 1 Introduction - extractive body cue:** (7) 2.2 ZMP equations and cart-table model To control the ZMP, it should be the outputs of the system while it appears as the inputs ...
- **p. 3 / 1 Introduction - extractive body cue:** However, we must consider an xu ZMP reference Servo Controller Dynamic ZMP equation (12) p ref p x + - p ZMP CoM Figure 4: ...
- **p. 4 / 1 Introduction - extractive body cue:** Assuming the controller in Figure 4, the output must be calculated from the future input!
- **p. 5 / 1 Introduction - extractive body cue:** It should be noted that even ZMP tracking performance is poor, the system still remains stable thanks to the term of the state feedback.
- **p. 2 / 1 Introduction - extractive body cue:** Even in the case of the sloped constraint where kx, ky̸ = 0, we can obtain the same dynamics by applying additional constraint τxx + ...
- **p. 1 / 1 Introduction - extractive body cue:** Since the controller knows little about the system structure, this approach much relies on a feedback control [6, 10, 7, 8].
- **Normalized interface:** observation=proprioception, reference pose/motion, visual or language command; state=whole-body pose, balance/contact state와 skill/mode; output/action=joint/whole-body action, motion target 또는 task trajectory.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | reference motion/skill horizon과 high-frequency whole-body control horizon이 분리된다. | However, since our method generated a stable gait by changing foot placements from the original assignment, it was not applicable to a ... | episode/sequence/action-chunk boundary |
| Rate / latency | motion policy/WBC/torque loop의 계층별 rate; numeric value 확인 필요. | The only parameter which governs those dynamics is zc, i.e., the z intersection of the constraint plane and the inclination of the ... | Hz/fps, inference time and control rate |
| Memory | body pose, contact, reference/history와 fall/recovery state. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | high-DOF policy, retargeting과 inverse-dynamics/QP solve가 latency를 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- training/inference separation PDF body cue not selected; no claim inferred

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** First, dynamics, biped, robot, modeled, running, cart, table, gives, convenient, representation, treat, ZMP, preview, controller, take, account, precise, multibody, although.
- **Relevant PDF headings:** not reliably recovered.
- Exact equation text is not copied into the note; equation number, variable definition and role must be checked at the cited page.

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Reference / embodiment interface | ZMP τ x x cz xp m O Figure 3: A cart-table model 3 Walking pattern generation for given ZMP 3.1 Pattern ... | p. 3 (1 Introduction), p. 2 (1 Introduction) |
| Balance-aware whole-body execution | no linked comparison cue | 본문 anchor 없음 |
| Recovery / adaptation | Figure 11: Modified ZMP of multibody model These information are stored to the buffer memory and loaded to use after delay time ... | p. 6 (Figure/Table caption), p. 4 (1 Introduction) |

## Failure and Ablation Link

- **p. 5 / 1 Introduction - extractive body cue:** 0 2 4 6 8 0 0.5 1 x [m] ZMP multibody ZMP cart-table CoM 0 2 4 6 8 -0.1 -0.05 0 0.05 0.1 ...
- **p. 4 / 1 Introduction - extractive body cue:** In this case, the resulted ZMP (bold line) does not 1623
- **p. 4 / 1 Introduction - extractive body cue:** We see the controller does not need the information of far future because the magnitude of the preview gain Gp becomes very small in the ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (Abstract), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), objective p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 4 (1 Introduction), temporal p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (7 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Assuming the controller in Figure 4, the output must be calculated from the future input! (p. 4, 1 Introduction).
- **Objective/update evidence:** (10) We can verify that this yields the same equation to Eq. (p. 2, 1 Introduction).
- **Temporal/runtime evidence:** However, since our method generated a stable gait by changing foot placements from the original assignment, it was not applicable to a situation like a walking on stepping-stones where the ... (p. 1, 1 Introduction).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
