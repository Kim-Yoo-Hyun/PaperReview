# Problem - Biped Walking Pattern Generation by using Preview Control of Zero-Moment Point

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/ROBOT.2003.1241826; PDF retrieval source: https://doi.org/10.1109/ROBOT.2003.1241826. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 3 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction)): However, we must consider an xu ZMP reference Servo Controller Dynamic ZMP equation (12) p ref p x + - p ZMP CoM Figure 4: Pattern generation as ZMP tracking ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We introduce a new method of a biped walking pattern generation by using a preview control of the zeromoment point (ZMP).
- **p. 1 / Abstract - extractive body cue:** First, the dynamics of a biped robot is modeled as a running cart on a table which gives a convenient representation to treat ZMP.
- **p. 1 / Abstract - extractive body cue:** After reviewing conventional methods of ZMP based pattern generation, we formalize the problem as the design of a ZMP tracking servo controller.
- **p. 1 / Abstract - extractive body cue:** It is shown that we can realize such controller by adopting the preview control theory that uses the future reference.
- **p. 1 / Abstract - extractive body cue:** It is also shown that a preview controller can be used to compensate the ZMP error caused by the difference between a simple model and ...
- **p. 3 / 1 Introduction - extractive body cue:** However, we must consider an xu ZMP reference Servo Controller Dynamic ZMP equation (12) p ref p x + - p ZMP CoM Figure 4: ...
- **p. 1 / 1 Introduction - extractive body cue:** Most of the inverted pendulum based methods suffer with this problem while the ZMP based methods can handle such situation [15].

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, we must consider an xu ZMP reference Servo Controller Dynamic ZMP equation (12) p ref p x + - p ZMP ... | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | The preview control is made of three terms, the integral action on the tracking error, the state feedback and the preview action ... | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF body |
| State / latent | preview, control, made, three, terms, integral, action, tracking, error, state | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | However, must, consider, ZMP, reference, Servo, Controller, Dynamic | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: preview, control, made, three, terms, integral, action, tracking, error, state | p. 4 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Decision / output variable | joint/whole-body action; body terms: introduce, novel, walking, pattern, generation, allows, arbitrary, foot | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: verify, yields, same, equation, following, part, will, refer | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (1 Introduction), p. 4 (1 Introduction), p. 4 (1 Introduction) |
| Success / guarantee | motion/task success and recovery | p. 4 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** Most of the inverted pendulum based methods suffer with this problem while the ZMP based methods can handle such situation [15].
- **p. 1 / 1 Introduction - extractive body cue:** Research on biped humanoid robots is currently one of the most exciting topics in the field of robotics and there are many ongoing projects [1, ...
- **p. 3 / 1 Introduction - extractive body cue:** On the other hand, a walking pattern generation is the inverse problem of this.

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 5 (1 Introduction), p. 1 (Abstract)): In this paper we introduce a novel walking pattern generation that allows arbitrary foot placements as a mixture of the ZMP based and the inverted pendulum based approaches.

- **p. 1 / 1 Introduction - extractive body cue:** However, since our method generated a stable gait by changing foot placements from the original assignment, it was not applicable to a situation like a ...
- **p. 2 / 1 Introduction - extractive body cue:** It is also shown that by using the preview controller, we can take into account of the precise multibody dynamics although our method is based ...
- **p. 5 / 1 Introduction - extractive body cue:** To evaluate our method we used the physical parameters of HRP-2 prototype (HRP-2P) shown in Figure 9[22].
- **p. 1 / Abstract - extractive body cue:** We introduce a new method of a biped walking pattern generation by using a preview control of the zeromoment point (ZMP).

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 5 | 0 2 4 6 8 0 0.5 1 x [m] ZMP multibody ZMP cart-table CoM 0 2 4 ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | In this case, the resulted ZMP (bold line) does not 1623 | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | We see the controller does not need the information of far future because the magnitude of the preview ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 3 (1 Introduction), p. 1 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction), interface p. 4 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), objective p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (7 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** Most of the inverted pendulum based methods suffer with this problem while the ZMP based methods can handle such situation [15]. (p. 1, 1 Introduction).
- **Formulation-changing contribution:** In this paper we introduce a novel walking pattern generation that allows arbitrary foot placements as a mixture of the ZMP based and the inverted pendulum based approaches. (p. 2, 1 Introduction).
- **Assumption/failure evidence:** In this case, the resulted ZMP (bold line) does not 1623 (p. 4, 1 Introduction).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
