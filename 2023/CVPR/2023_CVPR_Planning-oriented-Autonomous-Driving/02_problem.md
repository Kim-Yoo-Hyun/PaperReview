# Problem - Planning-oriented Autonomous Driving

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2212.10156; PDF retrieval source: https://arxiv.org/pdf/2212.10156. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction)): Although such a design simplifies the R&D difficulty across teams, it bares the risk of information loss across modules, error accumulation and feature misalignment due to the isolation of optimization ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Modern autonomous driving system is characterized as modular tasks in sequential order, i.e., perception, prediction, and planning.
- **p. 1 / Abstract - extractive body cue:** In order to perform a wide diversity of tasks and achieve advanced-level intelligence, contemporary approaches either deploy standalone models for individual tasks, or design a ...
- **p. 1 / Abstract - extractive body cue:** However, they might suffer from accumulative errors or deficient task coordination.
- **p. 1 / Abstract - extractive body cue:** Instead, we argue that a favorable framework should be devised and optimized in pursuit of the ultimate goal, i.e., planning of the self-driving car.
- **p. 1 / Abstract - extractive body cue:** Oriented at this, we revisit the key components within perception and prediction, and prioritize the tasks such that all these tasks contribute to planning.
- **p. 1 / 1. Introduction - extractive body cue:** Although such a design simplifies the R&D difficulty across teams, it bares the risk of information loss across modules, error accumulation and feature misalignment due ...
- **p. 2 / 1. Introduction - extractive body cue:** The choice and priority of preceding tasks should be determined in favor of planning.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Although such a design simplifies the R&D difficulty across teams, it bares the risk of information loss across modules, error accumulation and ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | MapFormer also has N stacked layers whose output results of each layer are all supervised, while only the updated queries QM in ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | MapFormer, stacked, layers, whose, output, layer, supervised, while, only, updated | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | block, takes, input, rich, agent, features, state, dense | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: MapFormer, stacked, layers, whose, output, layer, supervised, while, only, updated | p. 3 (2. Methodology), p. 3 (2. Methodology), p. 4 (2. Methodology) |
| Decision / output variable | geometry/map/query r; body terms: address, present, OccFormer, incorporate, scene-level, agent-level, semantics, aspects | p. 4 (2. Methodology), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: cost, function, regularizes, target, trajectory, obey, kinematic, constraints | p. 4 (2. Methodology), p. 5 (2.4. Planning), p. 4 (2. Methodology), p. 5 (2.5. Learning), p. 3 (2. Methodology) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (2.4. Planning), p. 3 (2. Methodology), p. 3 (2. Methodology) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (3.3. Qualitative Results), p. 7 (3.3. Qualitative Results), p. 6 (3.2. Modular Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** The choice and priority of preceding tasks should be determined in favor of planning.

## What the Paper Changes

PDF body contribution framing (p. 4 (2. Methodology), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (2. Methodology), p. 3 (2. Methodology)): To address this, we present OccFormer to incorporate both scene-level and agent-level semantics in two aspects: (1) a dense scene feature acquires agent-level features via an exquisitely designed attention module ...

- **p. 2 / 1. Introduction - extractive body cue:** (b) we present UniAD, a comprehensive end-to-end system that leverages a wide span of tasks.
- **p. 2 / 1. Introduction - extractive body cue:** Through extensive ablations, we verify the superiority of our method over previous state-of-the-arts in all aspects.
- **p. 3 / 2. Methodology - extractive body cue:** Prediction: Motion Forecasting Recent studies have proven the effectiveness of transformer structure on the motion task [43,44,63,69,70,84,99], inspired by which we propose MotionFormer in the ...
- **p. 3 / 2. Methodology - extractive body cue:** Besides queries encoding other agents surrounding the ego-vehicle, we introduce one particular ego-vehicle query in the query set to explicitly model the self-driving vehicle itself, ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 24 | Figure 14. Failure cases 2. In this case, the planner is over-cautious about the incoming vehicle in the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 24 | Figure 13. Failure cases 1. Here we present a long-tail scenario, where a large trailer with a white ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Besides, we analyze that failure cases of UniAD are mainly under some long-tail scenarios such as large trucks ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | In Exp.1012, only when the two tasks are introduced simultaneously (Exp.12), both metrics of the planning L2 and ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (2. Methodology), p. 3 (2. Methodology), p. 4 (2. Methodology), p. 2 (2. Methodology). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 3 (2. Methodology), p. 3 (2. Methodology), p. 4 (2. Methodology), p. 2 (2. Methodology), objective p. 4 (2. Methodology), p. 5 (2.4. Planning), p. 4 (2. Methodology), p. 5 (2.5. Learning), p. 3 (2. Methodology).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
