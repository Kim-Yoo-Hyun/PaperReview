# Problem - LAMP: Implicit Language Map for Robot Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2602.11862; PDF retrieval source: https://arxiv.org/pdf/2602.11862. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): This limitation arises from the inherent difficulty of densely and explicitly storing information on large scales.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Recent advances in vision-language models have made zero-shot navigation feasible, enabling robots to interpret and follow natural language instructions without requiring labeling.
- **p. 1 / Abstract - extractive body cue:** However, existing methods that explicitly store language vectors in grid or node-based maps struggle to scale to large environments due to excessive memory requirements and ...
- **p. 1 / Abstract - extractive body cue:** We introduce LAMP (Language Map), a novel neural language field-based navigation framework that learns a continuous, language-driven map and directly leverages it for fine-grained path ...
- **p. 1 / Abstract - extractive body cue:** Unlike prior approaches, our method encodes language features as an implicit neural field rather than storing them explicitly at every location.
- **p. 1 / Abstract - extractive body cue:** By combining this implicit representation with a sparse graph, LAMP supports efficient coarse path planning and then performs gradient-based optimization in the learned field to ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** This limitation arises from the inherent difficulty of densely and explicitly storing information on large scales.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, current language map representations are limited to small environments and encounter significant challenges for large-scale deployment.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This limitation arises from the inherent difficulty of densely and explicitly storing information on large scales. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | To address this gap, we propose an implicit language map representation that continuously models language vectors from RGB-only input, facilitating memoryefficient path ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | address, implicit, language, representation, continuously, models, vectors, RGB-only, input, facilitating | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | Implicit, Language, Map, Construction, robot, traverses, environment, collects | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: address, implicit, language, representation, continuously, models, vectors, RGB-only, input, facilitating | p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Decision / output variable | path/waypoint/velocity; body terms: summarize, main, contributions, LAMP, Language, Map, follows, introduce | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: posterior, over, network, parameters, proportional, zobs, train, minimizing | p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (III. METHOD), p. 3 (III. METHOD), p. 5 (III. METHOD) |
| Success / guarantee | goal reach with collision-free execution | p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 3 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** However, current language map representations are limited to small environments and encounter significant challenges for large-scale deployment.
- **p. 2 / I. INTRODUCTION - extractive body cue:** (b) The node-based approach fails to capture important object details when node spacing is too coarse and cannot guarantee precise path planning.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Although the implicit map provides a continuous function for language vectors in unobserved areas, mapping camera poses to language vectors in a highly nonlinear manner ...

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 4 (III. METHOD)): We summarize our main contributions of LAMP (Language Map) as follows: • We introduce LAMP, the first implicit language map leveraging a language-driven continuous field for finegrained path generation using ...

- **p. 1 / I. INTRODUCTION - extractive body cue:** To address this gap, we propose an implicit language map representation that continuously models language vectors from RGB-only input, facilitating memoryefficient path planning that supports ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Building on the strengths of our implicit language map, we propose methods to construct and utilize this representation more effectively.
- **p. 3 / III. METHOD - extractive body cue:** By dynamically generating embeddings through FΘ, our method significantly reduces storage while preserving language features.
- **p. 4 / III. METHOD - extractive body cue:** To address this, we propose a graph sampling method that retains only the most informative nodes, scored by three criteria.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 2 | Fig. 1. Comparison of three language map representation methods. (a) The grid-based approach struggles to accurately represent objects ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | In the Extinguisher scene, the node-based method fails because it does not directly observe the goal, whereas our ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Even with this increased memory usage, the grid-based approach captures large objects but fails to detect smaller ones. | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | In contrast, the node-based method needs about 70 times more memory than our method to reach a similar ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), objective p. 4 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
