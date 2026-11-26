# Method - Biped Walking Pattern Generation by using Preview Control of Zero-Moment Point

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://api.crossref.org/works/10.1109/ROBOT.2003.1241826; PDF retrieval source: https://doi.org/10.1109/ROBOT.2003.1241826. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA2 targeted source review: 2026-10-23; PDF pp. 3. 손상 구간·직접 연결된 표 분류만 원문 이미지와 대조했다. 전체 주장 정독·실험 검증·reading status 승격을 뜻하지 않는다. [URL·PDF hash·수정 기록](../../../../work/sources/pdf_note_review_followup_2026-10-23.json).

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

미래 ZMP 기준 궤적과 보행 모형의 상태 → 카트·테이블 근사와 다물체 모형의 ZMP 오차 → 질량중심·보행 기준 궤적. [방법·평가의 원문 근거](./01_overview.md#observation-state-and-output-interface)

## Objective / Update Rule

- **p. 2 / 1 Introduction - extractive body cue:** (10) We can verify that this yields the same equation to Eq.
- **p. 2 / 1 Introduction - extractive body cue:** (9) In the following part of this paper, we will refer the above equations as the ZMP equations.
- **p. 3 / 1 Introduction - extractive body cue:** By applying the Fast Fourier Transformation (FFT) to the ZMP reference, the ZMP equations can be solved in frequency domain.
- **p. 3 / 1 Introduction - extractive body cue:** They showed the ZMP equation can be discretized as a trinomial expression, and it can be efficiently solved by an algorithm of O(N) for the ...
- **p. 4 / 1 Introduction - extractive body cue:** When the ZMP reference can be previewed for NL step future at every sampling time, the optimal controller which minimizes the performance index (14) is ...
- **p. 4 / 1 Introduction - extractive body cue:** Although this sounds curious, we don't have to violate the law of causality.
- **Formal bridge:** 미래 ZMP 기준 궤적과 보행 모형의 상태 → 카트·테이블 근사와 다물체 모형의 ZMP 오차 → 질량중심·보행 기준 궤적.
- **Equation/algorithm anchors:** p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | preview, control, made, three, terms, integral, action, tracking, error, state, feedback, future, reference, ZMP | 미래 ZMP 기준 궤적과 보행 모형의 상태 | body cue; exact tensor/frame verify |
| State/latent | preview, control, made, three, terms, integral, action, tracking, error, state | 카트·테이블 근사와 다물체 모형의 ZMP 오차 | body cue; notation verify |
| Action/output | introduce, novel, walking, pattern, generation, allows, arbitrary, foot, placements, mixture | 질량중심·보행 기준 궤적 | body cue; unit/decoder verify |
| Objective/constraint | verify, yields, same, equation, following, part, will, refer, above, equations | tracking/balance/task objective | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / 1 Introduction - extractive body cue:** The preview control is made of three terms, the integral action on the tracking error, the state feedback and the preview action using the future ...
- **p. 2 / 1 Introduction - extractive body cue:** (7) 2.2 ZMP equations and cart-table model To control the ZMP, it should be the outputs of the system while it appears as the inputs ...
- **p. 3 / 1 Introduction - extractive body cue:** However, we must consider an xu ZMP reference Servo Controller Dynamic ZMP equation (12) p ref p x + - p ZMP CoM Figure 4: ...
- **p. 4 / 1 Introduction - extractive body cue:** Assuming the controller in Figure 4, the output must be calculated from the future input!
- **p. 5 / 1 Introduction - extractive body cue:** It should be noted that even ZMP tracking performance is poor, the system still remains stable thanks to the term of the state feedback.
- **p. 2 / 1 Introduction - extractive body cue:** Even in the case of the sloped constraint where kx, ky̸ = 0, we can obtain the same dynamics by applying additional constraint τxx + ...
- **p. 1 / 1 Introduction - extractive body cue:** Since the controller knows little about the system structure, this approach much relies on a feedback control [6, 10, 7, 8].
- **Normalized interface:** observation=미래 ZMP 기준 궤적과 보행 모형의 상태; state=카트·테이블 근사와 다물체 모형의 ZMP 오차; output/action=질량중심·보행 기준 궤적.

## Temporal and Runtime Contract

| Contract | PDF body cue | Unresolved detail |
|---|---|---|
| Horizon | However, since our method generated a stable gait by changing foot placements from the original assignment, it was not applicable to a ... | episode/sequence/action-chunk boundary |
| Rate / latency | The only parameter which governs those dynamics is zc, i.e., the z intersection of the constraint plane and the inclination of the ... | Hz/fps, inference time and control rate |
| Memory | not stated or recoverable in the selected PDF body | window and reset |
| Compute | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- training/inference separation PDF body cue not selected; no claim inferred

## Method-Specific Formal Details

- **Body-defined terms:** First, dynamics, biped, robot, modeled, running, cart, table, gives, convenient, representation, treat, ZMP, preview, controller, take, account, precise, multibody, although.
- **Relevant PDF headings:** not reliably recovered.

## Evaluation Link

| 평가 근거 | 원문에서 추출한 내용 | 원문 위치 |
|---|---|---|
| 원문 대조 | Fig. 3의 cart-table은 fixed-height point-mass model이다. 주어진 ZMP reference에서 CoM trajectory를 구하는 inverse problem을 jerk input의 linear servo system으로 쓴다. 그림의 model을 실제 robot hardware로 분류하지 않는다. | PDF p. 3 §§3.1–3.2 / Fig. 3 |
| 원문 대조 | no linked comparison cue | 본문 anchor 없음 |
| 원문 대조 | Figure 11: Modified ZMP of multibody model These information are stored to the buffer memory and loaded to use after delay time ... | p. 6 (Figure/Table caption), p. 4 (1 Introduction) |

## Failure and Ablation Link

- **p. 5 / 1 Introduction - extractive body cue:** 0 2 4 6 8 0 0.5 1 x [m] ZMP multibody ZMP cart-table CoM 0 2 4 6 8 -0.1 -0.05 0 0.05 0.1 ...
- **p. 4 / 1 Introduction - extractive body cue:** In this case, the resulted ZMP (bold line) does not 1623
- **p. 4 / 1 Introduction - extractive body cue:** We see the controller does not need the information of far future because the magnitude of the preview gain Gp becomes very small in the ...

## Reproduction Checklist

[공통 검토 기준](../../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 1 (Abstract), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 3 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), objective p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 4 (1 Introduction), temporal p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction).

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (7 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Assuming the controller in Figure 4, the output must be calculated from the future input! (p. 4, 1 Introduction).
- **Objective/update evidence:** (10) We can verify that this yields the same equation to Eq. (p. 2, 1 Introduction).
- **Temporal/runtime evidence:** However, since our method generated a stable gait by changing foot placements from the original assignment, it was not applicable to a situation like a walking on stepping-stones where the ... (p. 1, 1 Introduction).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
