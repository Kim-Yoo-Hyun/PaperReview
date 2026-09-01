# Problem - DexTrack: Towards Generalizable Neural Tracking Control for Dexterous Manipulation from Human References

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ajSmXqgS24; PDF retrieval source: https://arxiv.org/pdf/2502.09614. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION)): However, challenges remain due to noisy kinematic references, differences in morphology between human and robotic hands, complex dynamics with rich contacts, and diverse object geometry and skills.

## PDF Body Digest

- **p. 2 / 1 INTRODUCTION - extractive body cue:** However, challenges remain due to noisy kinematic references, differences in morphology between human and robotic hands, complex dynamics with rich contacts, and diverse object geometry ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Achieving human-level robotic dexterous manipulation is challenging due to two main difficulties: the intricate dynamics of contact-rich manipulation, which complicates optimization (Pang & Tedrake, 2021; ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Published as a conference paper at ICLR 2025 We demonstrate the superiority of our method and compare it with previous methods on challenging manipulation tracking ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We propose a data-driven way to generate homotopy paths, enabling solving challenging tracking problems.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Our contributions are threefold: • We present a generalizable neural tracking controller that progressively improves its performance through iterative mining and incorporating high-quality tracking demonstrations. ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Based upon the previous observations, we propose DexTrack, a novel neural tracking controller for dexterous manipulation, guided by human references.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To make sure the data flywheel functions effectively, we introduce two key designs.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, challenges remain due to noisy kinematic references, differences in morphology between human and robotic hands, complex dynamics with rich contacts, and ... | rigid/articulated object와 robot manipulator contact scene | body wording is the source claim |
| Observation / input | To achieve the challenging goal above, we draw three key observations: 1) learning is crucial for handling heterogeneous reference motion noises and ... | RGB-D/point cloud, object state와 contact/task observation | exact sensor/frame/preprocessing from PDF |
| State / latent | achieve, challenging, goal, above, draw, three, observations, learning, crucial, handling | object geometry, affordance, contact mode 또는 end-effector state | notation and tensor shape require body check |
| Output / action | Dexterous, manipulation, tracking, involves, controlling, robotic, hand, mimic | grasp, pose, force 또는 end-effector trajectory | exact unit/frame/decoder require body check |
| Target outcome | completion, contact success and robustness | task completion, contact success, pose/force error와 generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | object geometry/contact state; body terms: achieve, challenging, goal, above, draw, three, observations, learning, crucial, handling | p. 2 (1 INTRODUCTION), p. 3 (3 METHOD), p. 3 (3 METHOD) |
| Decision / output variable | grasp/pose/force/trajectory; body terms: contributions, threefold, present, generalizable, neural, tracking, controller, progressively | p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Objective / loss / cost | task/contact/pose objective; cue terms: not recovered | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | completion, contact success and robustness | p. 17 (B.1 DEXTEROUS MANIPULATION TRACKING CONTROL), p. 7 (4 EXPERIMENTS), p. 24 (C ADDITIONAL EXPERIMENTAL DETAILS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Achieving human-level robotic dexterous manipulation is challenging due to two main difficulties: the intricate dynamics of contact-rich manipulation, which complicates optimization (Pang & Tedrake, 2021; ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** Published as a conference paper at ICLR 2025 We demonstrate the superiority of our method and compare it with previous methods on challenging manipulation tracking ...
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We propose a data-driven way to generate homotopy paths, enabling solving challenging tracking problems.

## What the Paper Changes

PDF contribution framing (p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION)): Our contributions are threefold: • We present a generalizable neural tracking controller that progressively improves its performance through iterative mining and incorporating high-quality tracking demonstrations. • We introduce a train ...

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Based upon the previous observations, we propose DexTrack, a novel neural tracking controller for dexterous manipulation, guided by human references.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** To make sure the data flywheel functions effectively, we introduce two key designs.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** We propose a data-driven way to generate homotopy paths, enabling solving challenging tracking problems.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 19 | Figure 10: Failure cases in real-world experiments. Please refer to our website for animated | reported limitation/failure wording; scope must be verified |
| body cue at p. 19 | Method soap shovel brush roller knife spoon PPO (w/o sup., tracking rew) 33.3/0/0 25.0/0.0/0.0 25.0/0/0 25.0/25.0/0.0 0/0/0 25.0/0/0 ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | A key limitation is the time-consuming process of acquiring high-quality demonstrations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | 6 CONCLUSIONS AND LIMITATIONS We propose DexTrack to develop a generalizable tracking controller for dexterous manipulation. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1 INTRODUCTION), p. 3 (3 METHOD), p. 3 (3 METHOD), p. 2 (1 INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), interface p. 2 (1 INTRODUCTION), p. 3 (3 METHOD), p. 3 (3 METHOD), p. 2 (1 INTRODUCTION), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
