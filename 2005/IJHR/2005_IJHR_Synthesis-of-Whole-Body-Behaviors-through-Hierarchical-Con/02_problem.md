# Problem - Synthesis of Whole-Body Behaviors through Hierarchical Control of Behavioral Primitives

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://ai.stanford.edu/~lsentis/files/publications.html; PDF retrieval source: https://ai.stanford.edu/manips/publications/pdfs/Sentis_2005_IJHR.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): Controlling humanoids in these environments requires us to synthesize and change complex whole-body behaviors on-demand in the presence of high uncertainty.

## PDF Body Digest

- **p. 1 / 1. Introduction - extractive body cue:** Emerging applications of humanoids demand higher and higher degrees of autonomy for efficient interactions in human-populated environments.
- **p. 1 / 1. Introduction - extractive body cue:** Controlling humanoids in these environments requires us to synthesize and change complex whole-body behaviors on-demand in the presence of high uncertainty.
- **p. 1 / 1. Introduction - extractive body cue:** To synthesize whole-body behaviors on-demand we have developed a behavior-oriented methodology where multiple behavioral primitives are controlled simultaneously.
- **p. 1 / 1. Introduction - extractive body cue:** New behaviors are created by adding or removing individual, or collections of, pre-designed behavioral primitives, without the need to interrupt the movement.
- **p. 1 / 1. Introduction - extractive body cue:** To guarantee the safety of the robot and its environment we have designed a control hierarchy among primitives, where the control of the most critical ...
- **p. 2 / 1. Introduction - extractive body cue:** Section 4 presents a multi-level prioritized framework that allows us to establish multiple priority levels among categories.
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we will describe in detail this hierarchy based on projecting the control of lower priority primitives into the motion null-space of higher ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Controlling humanoids in these environments requires us to synthesize and change complex whole-body behaviors on-demand in the presence of high uncertainty. | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | Emerging applications of humanoids demand higher and higher degrees of autonomy for efficient interactions in human-populated environments. | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF body |
| State / latent | Emerging, applications, humanoids, demand, higher, degrees, autonomy, efficient, interactions, human-populated | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | December, WSPC/INSTRUCTION, FILE, ijhr-II-v4, guaranteed, while, non-safety, related | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: Emerging, applications, humanoids, demand, higher, degrees, autonomy, efficient, interactions, human-populated | p. 1 (1. Introduction), p. 1 (Body text (section not recovered)), p. 2 (1. Introduction) |
| Decision / output variable | joint/whole-body action; body terms: contrast, methodology, integrates, constraints, control, formulation, primary, controls | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3. Integration of constraints) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: accomplish, task, handle, constraint, efficiently, apply, control, described | p. 6 (3. Integration of constraints), p. 7 (4. Multi-level hierarchy), p. 7 (4. Multi-level hierarchy), p. 1 (1. Introduction), p. 1 (Body text (section not recovered)), p. 2 (1. Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (4. Multi-level hierarchy), p. 1 (1. Introduction), p. 1 (Body text (section not recovered)) |
| Success / guarantee | motion/task success and recovery | p. 11 (4.3. Movement feasibility), p. 12 (X Direction), p. 12 (X Direction) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** Section 4 presents a multi-level prioritized framework that allows us to establish multiple priority levels among categories.
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we will describe in detail this hierarchy based on projecting the control of lower priority primitives into the motion null-space of higher ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 5 (3. Integration of constraints), p. 6 (4. Multi-level hierarchy), p. 1 (1. Introduction)): In contrast, our methodology integrates constraints in the control formulation as primary controls and projects the operational tasks and the posture primitives into the constraint motion null-space, thus eliminating the ...

- **p. 2 / 1. Introduction - extractive body cue:** In Section 2 we describe previous related work, and also lay the mathematical foundations for this research based on our previous work.9 In Section 3 ...
- **p. 5 / 3. Integration of constraints - extractive body cue:** Based on the operational space formulation for redundant robots, further represented by the torque decomposition Γ = J T F + N T Γnull, (9) ...
- **p. 6 / 4. Multi-level hierarchy - extractive body cue:** We propose a multi-level control hierarchy that extends the task and posture decomposition previously described.
- **p. 1 / 1. Introduction - extractive body cue:** New behaviors are created by adding or removing individual, or collections of, pre-designed behavioral primitives, without the need to interrupt the movement.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 13 | Our research has addressed a wide set of constraints, such as joint-limits, collision avoidance, and self-collision avoidance, based ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Collision avoidance and control of multiple task primitives: This sequence depicts a robot avoiding an obstacle that is ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | However, the center of gravity horizontal position cannot be maintained (a), because its control is directly affected by ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | Because the hierarchy assigns higher priority to the center of gravity task, it maintains its desired goal position ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (1. Introduction), p. 1 (Body text (section not recovered)), p. 2 (1. Introduction), p. 5 (3. Integration of constraints). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 1 (1. Introduction), p. 1 (Body text (section not recovered)), p. 2 (1. Introduction), p. 5 (3. Integration of constraints), objective p. 6 (3. Integration of constraints), p. 7 (4. Multi-level hierarchy), p. 7 (4. Multi-level hierarchy), p. 1 (1. Introduction), p. 1 (Body text (section not recovered)), p. 2 (1. Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
