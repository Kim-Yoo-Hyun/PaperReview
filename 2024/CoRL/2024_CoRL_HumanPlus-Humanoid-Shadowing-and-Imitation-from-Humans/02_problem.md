# Problem - HumanPlus: Humanoid Shadowing and Imitation from Humans

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=WnSl42M9Z4; PDF retrieval source: https://arxiv.org/pdf/2406.10454. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction)): This problem is further exacerbated by the lack of off-the-shelf and integrated hardware platforms.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** One of the key arguments for building robots that have similar form factors to human beings is that we can leverage the massive human data ...
- **p. 1 / Abstract - extractive body cue:** Yet, doing so has remained challenging in practice due to the complexities in humanoid perception and control, lingering physical gaps between humanoids and humans in ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce a full-stack system for humanoids to learn motion and autonomous skills from human data.
- **p. 1 / Abstract - extractive body cue:** We first train a low-level policy in simulation via reinforcement learning using existing 40-hour human motion datasets.
- **p. 1 / Abstract - extractive body cue:** This policy transfers to the real world and allows humanoid robots to follow hu1.
- **p. 2 / 1. Introduction - extractive body cue:** This problem is further exacerbated by the lack of off-the-shelf and integrated hardware platforms.
- **p. 2 / 1. Introduction - extractive body cue:** Traditional approaches, such as decoupling the problem into perception, planning and tracking, and separate modularization of control for arms and legs [10, 10, 23, 40], ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This problem is further exacerbated by the lack of off-the-shelf and integrated hardware platforms. | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | Using state-of-the-art human body and hand pose estimation algorithms [58, 81], we can estimate real-time human motion and retarget it to humanoid ... | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF body |
| State / latent | state-of-the-art, human, body, hand, pose, estimation, algorithms, estimate, real-time, motion | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | complex, dynamics, high-dimensional, state, action, spaces, humanoids, pose | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: state-of-the-art, human, body, hand, pose, estimation, algorithms, estimate, real-time, motion | p. 2 (1. Introduction), p. 5 (5. Shadowing of Human Motion), p. 2 (1. Introduction) |
| Decision / output variable | joint/whole-body action; body terms: present, full-stack, system, humanoids, learn, motion, autonomous, skills | p. 2 (1. Introduction), p. 3 (1. Introduction), p. 3 (1. Introduction) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: PPO, train, Humanoid, Shadowing, Transformer, simulation, maximizing, discounted | p. 7 (6. Imitation of Human Skills) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (5. Shadowing of Human Motion), p. 7 (5. Shadowing of Human Motion), p. 7 (6. Imitation of Human Skills) |
| Success / guarantee | motion/task success and recovery | p. 10 (8.1. Comparisons with Other Teleoperation), p. 9 (8.1. Comparisons with Other Teleoperation), p. 9 (8. Experiments on Shadowing) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** Traditional approaches, such as decoupling the problem into perception, planning and tracking, and separate modularization of control for arms and legs [10, 10, 23, 40], ...
- **p. 3 / 1. Introduction - extractive body cue:** Shadowing provides an efficient data collection pipeline for diverse real-world tasks, bypassing the sim-to-real gap of RGB perception.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 3 (1. Introduction), p. 3 (1. Introduction), p. 4 (4. Human Body and Hand Data), p. 1 (Body text (section boundary not confidently recovered))): In this paper, we present a full-stack system for humanoids to learn motion and autonomous skills from human data.

- **p. 3 / 1. Introduction - extractive body cue:** Core to this system is both (1) a real-time shadowing system that allows human operators to whole-body control humanoids using a single RGB camera and ...
- **p. 3 / 1. Introduction - extractive body cue:** Using forward dynamics prediction on image features, our method shows improved performance by regularizing on image feature spaces and preventing the vision-based skill policy from ...
- **p. 4 / 4. Human Body and Hand Data - extractive body cue:** Each of the humanoid hip and shoulder joints consists of 3 orthogonal revolute joints, so can be viewed as one spherical joints.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Our system enables robots to shadow fast, diverse motions from a human operator, including boxing and playing table tennis, and to learn autonomous skills like ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | Table 4: Robustness Evaluation. Our low-level policy (Ours) can withstand large disturbance forces, has a shorter recovery time, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Table 3: Teleop Comparisons & User Studies. We report averaged completion time for 6 participants on 2 tasks. ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Throughout the development of our system, we encountered several limitations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | It fails the Wear a Shoe and Walk task completely, where depth perception is crucial. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1. Introduction), p. 5 (5. Shadowing of Human Motion), p. 2 (1. Introduction), p. 3 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction), interface p. 2 (1. Introduction), p. 5 (5. Shadowing of Human Motion), p. 2 (1. Introduction), p. 3 (1. Introduction), objective p. 7 (6. Imitation of Human Skills).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (17 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** This problem is further exacerbated by the lack of off-the-shelf and integrated hardware platforms. (p. 2, 1. Introduction).
- **Formulation-changing contribution:** In this paper, we present a full-stack system for humanoids to learn motion and autonomous skills from human data. (p. 2, 1. Introduction).
- **Assumption/failure evidence:** It fails the Wear a Shoe and Walk task completely, where depth perception is crucial. (p. 10, 9. Experiments on Imitation).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
