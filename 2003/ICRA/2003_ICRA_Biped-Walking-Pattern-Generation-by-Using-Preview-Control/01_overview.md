# Biped Walking Pattern Generation by using Preview Control of Zero-Moment Point

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://doi.org/10.1109/ROBOT.2003.1241826.
> PDF retrieval source: https://doi.org/10.1109/ROBOT.2003.1241826. Reading tracker status/evidence was not changed.

- Year/Venue: 2003 / ICRA
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: CORE
- Tags: Robotics, humanoid, locomotion, ZMP, Control
- Official paper: https://doi.org/10.1109/ROBOT.2003.1241826
- Full-text retrieval: https://doi.org/10.1109/ROBOT.2003.1241826
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 However, we must consider an xu ZMP reference Servo Controller Dynamic ZMP equation (12) p ref p x + - p ZMP CoM Figure 4: Pattern generation as ZMP tracking control 0 ...를 문제로 두고, In this paper we introduce a novel walking pattern generation that allows arbitrary foot placements as a mixture of the ZMP based and the inverted pendulum based approaches.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

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

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The preview control is made of three terms, the integral action on the tracking error, the state feedback and the preview action using the future reference. | proprioception, reference pose/motion, visual or language command | p. 4 (1 Introduction), p. 2 (1 Introduction) |
| State/latent | preview, control, made, three, terms, integral, action, tracking, error, state, feedback, future | whole-body pose, balance/contact state와 skill/mode | p. 4 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Output/action | (7) 2.2 ZMP equations and cart-table model To control the ZMP, it should be the outputs of the system while it appears as the inputs of the 3D-LIPM in the last section. | joint/whole-body action, motion target 또는 task trajectory | p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction) |
| Objective/outcome | (10) We can verify that this yields the same equation to Eq. | tracking, balance, skill/task success와 recovery | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** In this paper we introduce a novel walking pattern generation that allows arbitrary foot placements as a mixture of the ZMP based and the inverted ...
- **p. 1 / 1 Introduction - extractive body cue:** However, since our method generated a stable gait by changing foot placements from the original assignment, it was not applicable to a situation like a ...
- **p. 2 / 1 Introduction - extractive body cue:** It is also shown that by using the preview controller, we can take into account of the precise multibody dynamics although our method is based ...
- **p. 5 / 1 Introduction - extractive body cue:** To evaluate our method we used the physical parameters of HRP-2 prototype (HRP-2P) shown in Figure 9[22].
- **p. 1 / Abstract - extractive body cue:** We introduce a new method of a biped walking pattern generation by using a preview control of the zeromoment point (ZMP).
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 11: Modified ZMP of multibody model These information are stored to the buffer memory and loaded to use after delay time of T ∗NL. ...
- **p. 4 / 1 Introduction - extractive body cue:** We can see a smooth trajectory of CoM (dashed line) is generated and the resulted ZMP (bold line) follows the reference (thin line) with good ...
- **p. 4 / 1 Introduction - extractive body cue:** When the ZMP reference can be previewed for NL step future at every sampling time, the optimal controller which minimizes the performance index (14) is ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 6 (Figure/Table caption), p. 4 (1 Introduction) |
| Embodiment/environment | ZMP τ x x cz xp m O Figure 3: A cart-table model 3 Walking pattern generation for given ZMP 3.1 Pattern generation as an inverse problem When we represent a robot ... | hardware/simulator version and reset protocol | p. 3 (1 Introduction), p. 2 (1 Introduction) |
| Dataset/benchmark | 2 Dynamic Models of Biped Robot 2.1 3D Linear Inverted Pendulum Mode and Zero-moment point When we apply a constraint control to an inverted pendulum such that the mass should move along ... | role, split, size and leakage | p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction) |
| Metric | We can see a smooth trajectory of CoM (dashed line) is generated and the resulted ZMP (bold line) follows the reference (thin line) with good accuracy. | definition, denominator, direction and uncertainty | p. 4 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction) |
| Baseline/ablation | not recovered | fair input/data/compute/action matching | 본문 anchor 없음 |

## Explicit Limitations and Failure Boundary

- **p. 5 / 1 Introduction - extractive body cue:** 0 2 4 6 8 0 0.5 1 x [m] ZMP multibody ZMP cart-table CoM 0 2 4 6 8 -0.1 -0.05 0 0.05 0.1 ...
- **p. 4 / 1 Introduction - extractive body cue:** In this case, the resulted ZMP (bold line) does not 1623
- **p. 4 / 1 Introduction - extractive body cue:** We see the controller does not need the information of far future because the magnitude of the preview gain Gp becomes very small in the ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 humanoid 문제를 이해하기 위해 읽는다. 본문은 However, we must consider an xu ZMP reference Servo Controller Dynamic ZMP equation (12) p ref p x + - p ZMP CoM Figure 4: Pattern generation as ZMP tracking control 0 ...를 문제로 두고, In this paper we introduce a novel walking pattern generation that allows arbitrary foot placements as a mixture of the ZMP based and the inverted pendulum based approaches.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
