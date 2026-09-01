# Problem - Momentum Control with Hierarchical Inverse Dynamics on a Torque-Controlled Humanoid

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1410.7284; PDF retrieval source: https://arxiv.org/pdf/1410.7284. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (2.1 Modelling Assumptions and Problem Formulation)): However, the quasi-static assumption can be a limitation for dynamic motions.

## PDF Body Digest

- **p. 1 / 1 Introduction - extractive PDF cue:** 1We expect autonomous legged robots to perform complex tasks in persistent interaction with an uncertain and changing environment (e.g. in a disaster relief scenario).
- **p. 1 / 1 Introduction - extractive PDF cue:** Therefore, we need to design algorithms that can generate precise but compliant motions while optimizing the interactions with the environment.
- **p. 1 / 1 Introduction - extractive PDF cue:** In this context, the choice of a control strategy for legged robots is of primary importance as it can drastically improve performance in the face ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Robots with torque control capabilities [4,12], including humanoids [5,25,28], are becoming increasingly available and torque control algorithms are therefore necessary to fully exploit their capabilities.
- **p. 1 / 1 Introduction - extractive PDF cue:** Indeed, such algorithms often offer high performance for motion control while guaranteeing a certain level of compliance [4, 16,33,34].
- **p. 2 / 1 Introduction - extractive PDF cue:** However, the quasi-static assumption can be a limitation for dynamic motions.
- **p. 2 / 1 Introduction - extractive PDF cue:** However, pseudo-inverse-based controllers are limited as they cannot properly handle inequality constraints such as torque limits or friction cone constraints.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, the quasi-static assumption can be a limitation for dynamic motions. | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | Therefore it is not possible to directly control interaction forces during multi-contact tasks or to close a feedback loop directly around the ... | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF |
| State / latent | Therefore, possible, directly, control, interaction, forces, during, multi-contact, tasks, close | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | Friction, cone, feet, slip, constraint, ground, reaction, forces | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: Therefore, possible, directly, control, interaction, forces, during, multi-contact, tasks, close | p. 2 (1 Introduction), p. 3 (2.1 Modelling Assumptions and Problem Formulation), p. 3 (2.1 Modelling Assumptions and Problem Formulation) |
| Decision / output variable | joint/whole-body action; body terms: leads, main, contribution, where, experiments, extensive, quantitative, analysis | p. 3 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: every, control, cycle, equations, motion, Equation, constraints, physical | p. 4 (2.1 Modelling Assumptions and Problem Formulation), p. 17 (6.2 Relation to other balancing approaches), p. 3 (2.1 Modelling Assumptions and Problem Formulation), p. 3 (2.1 Modelling Assumptions and Problem Formulation), p. 4 (2.1 Modelling Assumptions and Problem Formulation), p. 6 (3.1 Linear and angular momentum models) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 17 (6.2 Relation to other balancing approaches), p. 3 (2.1 Modelling Assumptions and Problem Formulation), p. 3 (2.1 Modelling Assumptions and Problem Formulation) |
| Success / guarantee | motion/task success and recovery | p. 11 (5.2.2 Comparison of momentum controllers), p. 11 (5.2.2 Comparison of momentum controllers), p. 8 (4.3 State estimation) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive PDF cue:** However, pseudo-inverse-based controllers are limited as they cannot properly handle inequality constraints such as torque limits or friction cone constraints.
- **p. 3 / 1 Introduction - extractive PDF cue:** We also proposed a method to simplify the optimization problem by factoring the dynamics equations of the robot such that we could significantly reduce computational ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Balancing experiments in various conditions demonstrate performances that are comparable to, if not better than, current state of the art balancing algorithms, even when the ...
- **p. 4 / 2.1 Modelling Assumptions and Problem Formulation - extractive PDF cue:** Desired contact forces can be directly expressed as equalities on the generalized forces λ.

## What the Paper Changes

PDF contribution framing (p. 3 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction)): This leads us to the main contribution of this paper, where we show experiments with extensive quantitative analysis for various tasks (Sections 4 and 5).

- **p. 1 / 1 Introduction - extractive PDF cue:** Recent contributions have also demonstrated the relevance of torque control approaches for humanoid robots [13,28,36].
- **p. 2 / 1 Introduction - extractive PDF cue:** It has been shown in several contributions [39,21] that the regulation of momentum could be very powerful for control on humanoids.
- **p. 2 / 1 Introduction - extractive PDF cue:** In a recent contribution [11], we have demonstrated that hierarchical inverse dynamics controllers could be efficiently used on a torquecontrolled humanoid robot.
- **p. 3 / 1 Introduction - extractive PDF cue:** Contribution In this contribution, we extend our preliminary work and present extensive experimental evaluations.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 17 | Also, separating the EoM from kinematic contact constraints allows to keep solutions consistent with the dynamics even in ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 17 | On the other hand, it allows for prioritization of inequality constraints, which we exploit e.g. to give more ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 16 | The bottom plot shows the CoP of the stance foot, which saturates close to the heel during the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Moving the CoP across this link makes the foot bend and causes the robot to fall. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1 Introduction), p. 3 (2.1 Modelling Assumptions and Problem Formulation), p. 3 (2.1 Modelling Assumptions and Problem Formulation), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (2.1 Modelling Assumptions and Problem Formulation), interface p. 2 (1 Introduction), p. 3 (2.1 Modelling Assumptions and Problem Formulation), p. 3 (2.1 Modelling Assumptions and Problem Formulation), p. 2 (1 Introduction), objective p. 4 (2.1 Modelling Assumptions and Problem Formulation), p. 17 (6.2 Relation to other balancing approaches), p. 3 (2.1 Modelling Assumptions and Problem Formulation), p. 3 (2.1 Modelling Assumptions and Problem Formulation), p. 4 (2.1 Modelling Assumptions and Problem Formulation), p. 6 (3.1 Linear and angular momentum models).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
