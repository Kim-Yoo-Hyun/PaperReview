# Problem - SceneGraphLoc: Cross-Modal Coarse Visual Localization on 3D Scene Graphs

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/1255_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01255.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction)): The challenge with current state-of-the-art image-based coarse localization methods, such as AnyLoc [55], is their dependency on extensive image databases, which are not only storage-heavy but also slow to query, ...

## PDF Body Digest

- **p. 1 / 1 Introduction - extractive PDF cue:** Coarse visual localization, or place recognition, is a fundamental component in computer vision and robotics applications, defined as the task of identifying the approximate location ...
- **p. 2 / 1 Introduction - extractive PDF cue:** The training phase is represented by orange arrows, while blue arrows denote the inference phase.
- **p. 2 / 1 Introduction - extractive PDF cue:** During training, a query image and its associated 3D scene graph form a positive sample within a contrastive learning framework, where negative samples are generated ...
- **p. 2 / 1 Introduction - extractive PDF cue:** The objective is to learn the embeddings of both the graph and the image so that embeddings of the positive pair are drawn closer, whereas ...
- **p. 2 / 1 Introduction - extractive PDF cue:** In the inference phase, the task involves assigning the correct scene graph to a given query image from a selection of multiple graphs, achieved by ...
- **p. 2 / 1 Introduction - extractive PDF cue:** The challenge with current state-of-the-art image-based coarse localization methods, such as AnyLoc [55], is their dependency on extensive image databases, which are not only storage-heavy ...
- **p. 2 / 1 Introduction - extractive PDF cue:** This paper addresses the novel challenge of localizing a query image within a database that is represented not by conventional images but by the 3D ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The challenge with current state-of-the-art image-based coarse localization methods, such as AnyLoc [55], is their dependency on extensive image databases, which are ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | SceneGraphLoc, a new method for the coarse localization of an input image given a reference map represented by a database of 3D ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | SceneGraphLoc, coarse, localization, input, image, given, reference, represented, database, scene | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | Cross-modal, approaches, attempt, bridge, different, types, data, often | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: SceneGraphLoc, coarse, localization, input, image, given, reference, represented, database, scene | p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Decision / output variable | path/waypoint/velocity; body terms: enables, creation, small, efficient, databases, significantly, accelerates, coarse | p. 2 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: objective, learn, embeddings, graph, image, positive, pair, drawn | p. 2 (1 Introduction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Success / guarantee | goal reach with collision-free execution | p. 11 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive PDF cue:** This paper addresses the novel challenge of localizing a query image within a database that is represented not by conventional images but by the 3D ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Introducing a novel problem: cross-modal localization of a query image within 3D scene graphs incorporating a mixture of modalities.

## What the Paper Changes

PDF contribution framing (p. 2 (1 Introduction), p. 3 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction)): This method enables the creation of small, efficient databases and significantly accelerates the coarse localization process.

- **p. 3 / 1 Introduction - extractive PDF cue:** The primary contributions of this paper are as follows: 1.
- **p. 2 / 1 Introduction - extractive PDF cue:** This paper addresses the novel challenge of localizing a query image within a database that is represented not by conventional images but by the 3D ...
- **p. 3 / 1 Introduction - extractive PDF cue:** Introducing a novel problem: cross-modal localization of a query image within 3D scene graphs incorporating a mixture of modalities.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| no explicit assumption/failure cue | domain stress test only | not a paper claim |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), interface p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), objective p. 2 (1 Introduction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
