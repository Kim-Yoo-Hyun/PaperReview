# Problem - BEHAVIOR-1K: A Benchmark for Embodied AI with 1,000 Everyday Activities and Realistic Simulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (43 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v205/li23s.html; PDF retrieval source: https://arxiv.org/pdf/2403.09227. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction)): Concretely, the difficulties derive in part from the length of BEHAVIOR-1K's activities and the complexity of the physical manipulation required.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** We present BEHAVIOR-1K, a comprehensive simulation benchmark for human-centered robotics.
- **p. 1 / Abstract - extractive PDF cue:** BEHAVIOR-1K includes two components, guided and motivated by the results of an extensive survey on ‘what do you want robots to do for you?'.
- **p. 1 / Abstract - extractive PDF cue:** The first is the definition of 1,000 everyday activities, grounded in 50 scenes (houses, gardens, restaurants, offices, etc.) with more than 9,000 objects annotated with ...
- **p. 1 / Abstract - extractive PDF cue:** The second is OMNIGIBSON, a novel simulation environment that supports these activities via realistic physics simulation and rendering of rigid bodies, deformable bodies, and liquids.
- **p. 1 / Abstract - extractive PDF cue:** Our experiments indicate that the activities in BEHAVIOR-1K are long-horizon and dependent on complex manipulation skills, both of which remain a challenge for even state-of-the-art ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Concretely, the difficulties derive in part from the length of BEHAVIOR-1K's activities and the complexity of the physical manipulation required.
- **p. 2 / 1 Introduction - extractive PDF cue:** To calibrate the simulation-to-real gap of BEHAVIOR-1K, we provide an initial study on transferring solutions learned with a mobile manipulator in a simulated apartment to ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Concretely, the difficulties derive in part from the length of BEHAVIOR-1K's activities and the complexity of the physical manipulation required. | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | The policy outputs a discrete selection of a primitive applied on an object; • RL-Prim.Hist., a variant of RL-Prim. that takes in ... | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF |
| State / latent | policy, outputs, discrete, selection, primitive, applied, object, RL-Prim, Hist, variant | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | evaluate, strategies, selecting, action, primitives, real, world, optimal | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: policy, outputs, discrete, selection, primitive, applied, object, RL-Prim, Hist, variant | p. 7 (Method), p. 7 (Method), p. 8 (Method) |
| Decision / output variable | method trajectory/action; body terms: present, BEHAVIOR-1K, Benchmark, Everyday, Household, Activities, Virtual, Interactive | p. 2 (1 Introduction), p. 8 (Method), p. 2 (1 Introduction) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: agents, trained, sparse, task, success, reward, without, engineering | p. 7 (Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 7 (Method), p. 7 (Method) |
| Success / guarantee | comparable score and protocol validity | p. 7 (Method), p. 7 (Figure/Table caption), p. 8 (Method) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive PDF cue:** To calibrate the simulation-to-real gap of BEHAVIOR-1K, we provide an initial study on transferring solutions learned with a mobile manipulator in a simulated apartment to ...

## What the Paper Changes

PDF contribution framing (p. 2 (1 Introduction), p. 8 (Method), p. 2 (1 Introduction)): In this work, we present BEHAVIOR-1K, a Benchmark of 1,000 Everyday Household Activities in Virtual, Interactive, and Ecological Environments-the next generation of BEHAVIOR-100 [27].

- **p. 8 / Method - extractive PDF cue:** We also evaluate to what extent the simplifications we introduce in physics and actuation (grasping, motion execution) during training impact the performance of RL-Prim. during ...
- **p. 2 / 1 Introduction - extractive PDF cue:** We hope that the BEHAVIOR-1K benchmark, our survey, and our analysis will serve to support and guide the development of future embodied AI agents and ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | The failure cases are depicted in Fig. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | 6.1), policy failures (i.e., selecting the wrong action primitive) dominate. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | RL-VMC with end-to-end visuomotor control completely fails to solve any of the activities, whereas RL-Prim. and RL-Prim.Hist. with ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Furthermore, to accelerate training, the action primitives check only the feasibility (e.g., reachability, collisions) of the final configuration, ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 7 (Method), p. 7 (Method), p. 8 (Method), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), interface p. 7 (Method), p. 7 (Method), p. 8 (Method), p. 2 (1 Introduction), objective p. 7 (Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
