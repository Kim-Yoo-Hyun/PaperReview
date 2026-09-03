# Problem - Habitat: A Platform for Embodied AI Research

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1904.01201; PDF retrieval source: https://arxiv.org/pdf/1904.01201. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): However, we also recognize that training robots in the real world is slow (the real world runs no faster than real time and cannot be parallelized), dangerous (poorly-trained agents can ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We present Habitat, a platform for research in embodied artificial intelligence (AI).
- **p. 1 / Abstract - extractive body cue:** Habitat enables training embodied agents (virtual robots) in highly efficient photorealistic 3D simulation.
- **p. 1 / Abstract - extractive body cue:** Specifically, Habitat consists of: (i) Habitat-Sim: a flexible, high-performance 3D simulator with configurable agents, sensors, and generic 3D dataset handling.
- **p. 1 / Abstract - extractive body cue:** Habitat-Sim is fast - when rendering a scene from Matterport3D, it achieves several thousand frames per second (fps) running single-threaded, and can reach over 10,000 ...
- **p. 1 / Abstract - extractive body cue:** (ii) Habitat-API: a modular high-level library for end-toend development of embodied AI algorithms - defining tasks (e.g. navigation, instruction following, question answering), configuring, training, and ...
- **p. 1 / 1. Introduction - extractive body cue:** However, we also recognize that training robots in the real world is slow (the real world runs no faster than real time and cannot be ...
- **p. 2 / 1. Introduction - extractive body cue:** In the context of embodied AI, simulators help overcome the aforementioned challenges - they can run orders of magnitude faster than real-time and can be ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, we also recognize that training robots in the real world is slow (the real world runs no faster than real time ... | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | RGB, depth, contact, GPS, compass sensors) attached to each agent. - Scenario and task API: allows portable definition of tasks and their ... | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF body |
| State / latent | RGB, depth, contact, GPS, compass, sensors, attached, agent, Scenario, task | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | bring, order, successful, robot, would, need, range, skills | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: RGB, depth, contact, GPS, compass, sensors, attached, agent, Scenario, task | p. 4 (3. Habitat Platform), p. 6 (4. PointGoal Navigation at Scale), p. 1 (1. Introduction) |
| Decision / output variable | method trajectory/action; body terms: Specifically, Habitat, consists, following, unified, embodied, agent, stack | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (Abstract) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: RGB, depth, contact, GPS, compass, sensors, attached, agent | p. 6 (4. PointGoal Navigation at Scale) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Success / guarantee | comparable score and protocol validity | p. 7 (5. Results and Findings), p. 7 (Figure/Table caption), p. 8 (5. Results and Findings) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** In the context of embodied AI, simulators help overcome the aforementioned challenges - they can run orders of magnitude faster than real-time and can be ...
- **p. 2 / 1. Introduction - extractive body cue:** Prior work (highlighted in blue boxes) has contributed a variety of datasets, simulation software, and task definitions.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (Abstract), p. 4 (3. Habitat Platform), p. 1 (Abstract)): Specifically, Habitat consists of the following: 1.

- **p. 2 / 1. Introduction - extractive body cue:** We propose a unified embodied agent stack with the Habitat platform, including generic dataset support, a highly performant simulator (Habitat-Sim), and a flexible API (Habitat-API) ...
- **p. 1 / Abstract - extractive body cue:** We present Habitat, a platform for research in embodied artificial intelligence (AI).
- **p. 4 / 3. Habitat Platform - extractive body cue:** RGB, depth, contact, GPS, compass sensors) attached to each agent. - Scenario and task API: allows portable definition of tasks and their evaluation protocols. - ...
- **p. 1 / Abstract - extractive body cue:** Habitat enables training embodied agents (virtual robots) in highly efficient photorealistic 3D simulation.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | Another planned avenue of future work involves procedural generation of 3D environments by leveraging a combination of 3D ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | Figure 10: Average number of collisions during successful navi- gation episodes for the different sensory configurations of the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | SLAM [20] does not require training and thus has a constant performance (0.59 on Gibson, 0.42 on Matterport3D). | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | RGB and RGBD agents suffer a significant performance degradation, while the Blind agent is least affected (as we ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (3. Habitat Platform), p. 6 (4. PointGoal Navigation at Scale), p. 1 (1. Introduction), p. 4 (3. Habitat Platform). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 4 (3. Habitat Platform), p. 6 (4. PointGoal Navigation at Scale), p. 1 (1. Introduction), p. 4 (3. Habitat Platform), objective p. 6 (4. PointGoal Navigation at Scale).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
