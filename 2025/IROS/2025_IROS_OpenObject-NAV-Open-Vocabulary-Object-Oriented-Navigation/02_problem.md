# Problem - OpenObject-NAV: Open-Vocabulary Object-Oriented Navigation Based on Dynamic Carrier-Relationship Scene Graph

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2409.18743; PDF retrieval source: https://arxiv.org/pdf/2409.18743. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION)): However, they struggle to represent everyday dynamic environments due to two key challenges.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** In everyday life, frequently used objects like cups often have unfixed positions and multiple instances within the same category, and their carriers frequently change as ...
- **p. 1 / Abstract - extractive PDF cue:** As a result, it becomes challenging for a robot to efficiently navigate to a specific instance.
- **p. 1 / Abstract - extractive PDF cue:** To tackle this challenge, the robot must capture and update scene changes and plans continuously.
- **p. 1 / Abstract - extractive PDF cue:** However, current object navigation approaches primarily focus on semantic-level and lack the ability to dynamically update scene representation.
- **p. 1 / Abstract - extractive PDF cue:** This paper captures the relationships between frequently used objects and their static carriers.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** However, they struggle to represent everyday dynamic environments due to two key challenges.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** However, they are often limited to searching for semantic-level objects and lack the capability to update scenes.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, they struggle to represent everyday dynamic environments due to two key challenges. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | The robot selects the next action at ∈A based on the current state St according to a specific policy π(·) in (8). ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | robot, selects, next, action, current, state, according, specific, policy, Given | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | Leveraging, LLM, commonsense, understanding, object-carrier, relationships, unlikely, placed | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: robot, selects, next, action, current, state, according, specific, policy, Given | p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Decision / output variable | path/waypoint/velocity; body terms: summary, contributions, follows, present, adaptable, carrier, relationship, scene | p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: cost, function, defined, follows, Length, Let, represent, position | p. 4 (III. METHOD), p. 4 (III. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD) |
| Success / guarantee | goal reach with collision-free execution | p. 4 (1. Does the carrier-relationship scene graph (CRSG) im), p. 4 (1. Does the carrier-relationship scene graph (CRSG) im), p. 5 (1. Does the carrier-relationship scene graph (CRSG) im) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive PDF cue:** However, they are often limited to searching for semantic-level objects and lack the capability to update scenes.

## What the Paper Changes

PDF contribution framing (p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): In summary, our contributions are as follows: • We present an adaptable carrier relationship scene graph (CRSG) that primarily describes the dynamic carrier and carried relationships between objects. • We ...

- **p. 3 / III. METHOD - extractive PDF cue:** The OpenObject-NAV system framework consists of two main modules.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** 2Zibo Zheng are with School of Mechanical Engineering, University of Nottingham Ningbo China, Ningbo, 315100, China. †: Equal contribution.
- **p. 1 / I. INTRODUCTION - extractive PDF cue:** This update enables efficient point-to-point navigation for the third task. dynamic and subject to interference, making it challenging to efficiently and effectively navigate to them.
- **p. 2 / I. INTRODUCTION - extractive PDF cue:** Based on the CRSG, we designed an object-oriented navigation strategy, modeling the object search process as a Markov Decision Process (MDP) [21].

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 4 | If the robot fails to reach the target, the SPL score is zero. | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | VLMap Ours ConceptGraph Result: Success Result: Success Result: Failed ---Find a chair Result: Failed ---Find yellow bottle Result: ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), interface p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), objective p. 4 (III. METHOD), p. 4 (III. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
