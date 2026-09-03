# Problem - MR-COGraphs: Communication-efficient Multi-Robot Open-vocabulary Mapping System via 3D Scene Graphs

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2412.18381; PDF retrieval source: https://arxiv.org/pdf/2412.18381. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): However, current open-vocabulary 3D map representations demand significant data storage [9][11], which becomes a communication bottleneck for multi-robot mapping systems.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Collaborative perception in unknown environments is crucial for multi-robot systems.
- **p. 1 / Abstract - extractive body cue:** With the emergence of foundation models, robots can now not only perceive geometric information but also achieve open-vocabulary scene understanding.
- **p. 1 / Abstract - extractive body cue:** However, existing map representations that support open-vocabulary queries often involve large data volumes, which becomes a bottleneck for multi-robot transmission in communication-limited environments.
- **p. 1 / Abstract - extractive body cue:** To address this challenge, we develop a method to construct a graph-structured 3D representation called COGraph, where nodes represent objects with semantic features and edges ...
- **p. 1 / Abstract - extractive body cue:** Before transmission, a data-driven feature encoder is applied to compress the feature dimensions of the COGraph.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, current open-vocabulary 3D map representations demand significant data storage [9][11], which becomes a communication bottleneck for multi-robot mapping systems.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This data explosion makes it difficult for multiple robots to share and update maps in real time.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, current open-vocabulary 3D map representations demand significant data storage [9][11], which becomes a communication bottleneck for multi-robot mapping systems. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | 3D back projection is conducted using FO images, depth images, and poses derived from SLAM. | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | back, projection, conducted, images, depth, poses, derived, SLAM, observation, conduct | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | III-D, Segmentation, Model, depth, seg-image, Robot, COGraph-3, COGraph-512 | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: back, projection, conducted, images, depth, poses, derived, SLAM, observation, conduct | p. 4 (III. METHOD), p. 4 (III. METHOD), p. 1 (I. INTRODUCTION) |
| Decision / output variable | path/waypoint/velocity; body terms: fulfill, requirements, above, Communication-efficient, Multi-Robot, Open-vocabulary, Scene, Graphs-based | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: Comparison, original, decoded, features, when, encoder, decoder, trained | p. 4 (III. METHOD), p. 4 (III. METHOD) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (III. METHOD), p. 4 (III. METHOD), p. 5 (III. METHOD) |
| Success / guarantee | goal reach with collision-free execution | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** This data explosion makes it difficult for multiple robots to share and update maps in real time.
- **p. 2 / I. INTRODUCTION - extractive body cue:** mapping works [14] [18] have explored the collaborative construction of 3D scene graphs, they do not consider open-vocabulary capabilities and have yet to address the ...

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (III. METHOD), p. 1 (I. INTRODUCTION)): To fulfill the requirements above, we propose a Communication-efficient Multi-Robot Open-vocabulary 3D Scene Graphs-based Mapping (MR-COGraphs) System with the following contributions: • A data-efficient open-vocabulary 3D scene graph c ...

- **p. 2 / I. INTRODUCTION - extractive body cue:** 1, we propose a graph-structured open-vocabulary representation called COGraph (detailed in Section III-A).
- **p. 3 / III. METHOD - extractive body cue:** COGraphs Representation The proposed COGraph consists of the robot name, nodes, and edges.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Recent advances in visual foundation models (e.g., SAM [2]) and vision-language models (e.g., CLIP [3]) have enabled the development of open-vocabulary 3D map representations.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 6 | demonstrate that our feature compression process does not compromise the object finding rate and query success rate across ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | 2) Metrics: Unlike multi-robot SLAM, our localization module relies on a ready-made SLAM algorithm, and the graph-structured map ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Fig. 3. Comparison of the original and decoded features when the encoder and decoder are trained on household-related ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | In this section, we 1) conduct experimental evaluations comparing our approach with state-of-the-art methods (Section IVA), 2) analyze ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (III. METHOD), p. 4 (III. METHOD), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 4 (III. METHOD), p. 4 (III. METHOD), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), objective p. 4 (III. METHOD), p. 4 (III. METHOD).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
