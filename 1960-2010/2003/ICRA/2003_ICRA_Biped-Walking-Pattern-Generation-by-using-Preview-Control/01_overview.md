# Biped Walking Pattern Generation by using Preview Control of Zero-Moment Point

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1109/ROBOT.2003.1241826.
> PDF retrieval source: https://doi.org/10.1109/ROBOT.2003.1241826. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2003 / ICRA
- Authors: S. Kajita, F. Kanehiro, K. Kaneko, K. Fujiwara, K. Harada, K. Yokoi, H. Hirukawa
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Robotics, humanoid, locomotion, ZMP, Control
- Official paper: https://api.crossref.org/works/10.1109/ROBOT.2003.1241826
- Full-text retrieval: https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=1241826
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 요약·기여는 [이번 대조 판본](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=1241826) 기준이다.

> DOC-QA2 targeted source review: 2026-10-23; PDF pp. 3, 5. 손상 구간·직접 연결된 표 분류만 원문 이미지와 대조했다. 전체 주장 정독·실험 검증·reading status 승격을 뜻하지 않는다. [URL·PDF hash·수정 기록](../../../../work/sources/pdf_note_review_followup_2026-10-23.json).

## Why This Paper Is Here

Kajita 등은 미래의 목표 영모멘트점 궤적을 미리 고려해 이족 로봇의 무게중심 움직임을 생성한다. [PDF 1쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=1241826#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We introduce a new method of a biped walking pattern generation by using a preview control of the zeromoment point (ZMP).
- **p. 1 / Abstract - extractive body cue:** First, the dynamics of a biped robot is modeled as a running cart on a table which gives a convenient representation to treat ZMP.
- **p. 1 / Abstract - extractive body cue:** After reviewing conventional methods of ZMP based pattern generation, we formalize the problem as the design of a ZMP tracking servo controller.
- **p. 1 / Abstract - extractive body cue:** It is shown that we can realize such controller by adopting the preview control theory that uses the future reference.
- **p. 1 / Abstract - extractive body cue:** It is also shown that a preview controller can be used to compensate the ZMP error caused by the difference between a simple model and ...
- **p. 3 / 1 Introduction - extractive body cue:** However, we must consider an xu ZMP reference Servo Controller Dynamic ZMP equation (12) p ref p x + - p ZMP CoM Figure 4: ...
- **p. 1 / 1 Introduction - extractive body cue:** Most of the inverted pendulum based methods suffer with this problem while the ZMP based methods can handle such situation [15].

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** In this paper we introduce a novel walking pattern generation that allows arbitrary foot placements as a mixture of the ZMP based and the inverted ...
- **p. 1 / 1 Introduction - extractive body cue:** However, since our method generated a stable gait by changing foot placements from the original assignment, it was not applicable to a situation like a ...
- **p. 2 / 1 Introduction - extractive body cue:** It is also shown that by using the preview controller, we can take into account of the precise multibody dynamics although our method is based ...
- **p. 5 / 1 Introduction - extractive body cue:** To evaluate our method we used the physical parameters of HRP-2 prototype (HRP-2P) shown in Figure 9[22].
- **p. 1 / Abstract - extractive body cue:** We introduce a new method of a biped walking pattern generation by using a preview control of the zeromoment point (ZMP).
- **p. 1 / Abstract - extractive body cue:** First, the dynamics of a biped robot is modeled as a running cart on a table which gives a convenient representation to treat ZMP.
- **p. 4 / 1 Introduction - extractive body cue:** To obtain a smooth ZMP trajectory in double support, we used cubic spline.
- **p. 3 / 1 Introduction - extractive body cue:** However, we must consider an xu ZMP reference Servo Controller Dynamic ZMP equation (12) p ref p x + - p ZMP CoM Figure 4: ...

## Observation, State, and Output Interface

미래 ZMP 기준을 이용하는 선형 이차 미리보기 제어로 질량중심 궤적을 만든다. 6쪽의 계단 보행은 OpenHRP 안의 HRP-2P 시뮬레이션이다. 팔 파지나 모바일 매니퓰레이터 동작을 시험하지 않았다. [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=1241826#page=4) · [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=1241826#page=6)

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The preview control is made of three terms, the integral action on the tracking error, the state feedback and the preview action using the future reference. | 미래 ZMP 기준 궤적과 보행 모형의 상태 | p. 4 (1 Introduction), p. 2 (1 Introduction) |
| State/latent | preview, control, made, three, terms, integral, action, tracking, error, state, feedback, future | 카트·테이블 근사와 다물체 모형의 ZMP 오차 | p. 4 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Output/action | (7) 2.2 ZMP equations and cart-table model To control the ZMP, it should be the outputs of the system while it appears as the inputs of the 3D-LIPM in the last section. | 질량중심·보행 기준 궤적 | p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction) |
| Objective/outcome | (10) We can verify that this yields the same equation to Eq. | OpenHRP의 ZMP 추종 및 계단 보행 | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction) |

## Main Claims and Actual Contribution

- 단순화한 카트·테이블 동역학에서 영모멘트점 추종을 미래 기준값을 사용하는 서보 제어 문제로 구성했다. [PDF 2쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=1241826#page=2) · [PDF 3쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=1241826#page=3) · [PDF 4쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=1241826#page=4)
- 정밀 다물체 모형과 단순 모형의 차이에서 생기는 영모멘트점 오차를 보상하고 시뮬레이션 보행으로 확인했다. [PDF 5쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=1241826#page=5) · [PDF 6쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=1241826#page=6) · [PDF 7쪽](https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=1241826#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 6 (Figure/Table caption), p. 4 (1 Introduction) |
| Embodiment/environment | Cart-table model로 pattern을 설계하고 HRP-2P physical parameters를 사용한 multibody model과 비교한다. | Fig. 3은 모델 도식; simulator version/reset 규약은 이 그림에서 확인되지 않음 | PDF p. 3 Fig. 3, p. 5 §3.4 / Fig. 9 |
| Dataset/benchmark | 2 Dynamic Models of Biped Robot 2.1 3D Linear Inverted Pendulum Mode and Zero-moment point When we apply a constraint control to an inverted pendulum such that the mass should move along ... | role, split, size and leakage | p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction) |
| Metric | We can see a smooth trajectory of CoM (dashed line) is generated and the resulted ZMP (bold line) follows the reference (thin line) with good accuracy. | definition, denominator, direction and uncertainty | p. 4 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction) |
| Baseline/ablation | not stated or recoverable in the selected PDF body | fair input/data/compute/action matching | 본문 anchor 없음 |

## Explicit Limitations and Failure Boundary

- **p. 5 / 1 Introduction - extractive body cue:** 0 2 4 6 8 0 0.5 1 x [m] ZMP multibody ZMP cart-table CoM 0 2 4 6 8 -0.1 -0.05 0 0.05 0.1 ...
- **p. 4 / 1 Introduction - extractive body cue:** In this case, the resulted ZMP (bold line) does not 1623
- **p. 4 / 1 Introduction - extractive body cue:** We see the controller does not need the information of far future because the magnitude of the preview gain Gp becomes very small in the ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 3 (1 Introduction), p. 1 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (7 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Most of the inverted pendulum based methods suffer with this problem while the ZMP based methods can handle such situation [15]. (p. 1, 1 Introduction).
- **Actual contribution:** In this paper we introduce a novel walking pattern generation that allows arbitrary foot placements as a mixture of the ZMP based and the inverted pendulum based approaches. (p. 2, 1 Introduction).
- **Evaluation boundary (DOC-QA2):** PDF p. 3 Fig. 3은 controller model이며 실험 결과가 아니다. PDF p. 5 §3.4는 HRP-2P parameters의 multibody model에서 cart-table model과의 ZMP 차이를 분석한다. 이를 이 구간만으로 실기기 rollout 검증으로 승격하지 않는다.
- **Explicit failure boundary:** In this case, the resulted ZMP (bold line) does not 1623 (p. 4, 1 Introduction).
