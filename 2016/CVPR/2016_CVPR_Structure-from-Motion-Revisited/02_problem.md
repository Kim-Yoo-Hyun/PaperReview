# Problem - Structure-from-Motion Revisited

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content_cvpr_2016/html/Schonberger_Structure-From-Motion_Revisited_CVPR_2016_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content_cvpr_2016/papers/Schonberger_Structure-From-Motion_Revisited_CVPR_2016_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction)): While the existing systems have advanced the state of the art tremendously, robustness, accuracy, completeness, and scalability remain the key problems in incremental SfM that prevent its use as a ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Incremental Structure-from-Motion is a prevalent strategy for 3D reconstruction from unordered image collections.
- **p. 1 / Abstract - extractive PDF cue:** While incremental reconstruction systems have tremendously advanced in all regards, robustness, accuracy, completeness, and scalability remain the key problems towards building a truly general-purpose pipeline.
- **p. 1 / Abstract - extractive PDF cue:** We propose a new SfM technique that improves upon the state of the art to make a further step towards this ultimate goal.
- **p. 1 / Abstract - extractive PDF cue:** The full reconstruction pipeline is released to the public as an open-source implementation.
- **p. 1 / 1. Introduction - extractive PDF cue:** Structure-from-Motion (SfM) from unordered images has seen tremendous evolution over the years.
- **p. 1 / 1. Introduction - extractive PDF cue:** In this paper, we propose a new SfM algorithm to approach this ultimate goal.
- **p. 2 / 2.2. Incremental Reconstruction - extractive PDF cue:** We propose a novel robust next best image selection method for accurate pose estimation and reliable triangulation in Sec.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | While the existing systems have advanced the state of the art tremendously, robustness, accuracy, completeness, and scalability remain the key problems in ... | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | The outputs are pose estimates P = {Pc ∈SE(3) / c = 1...NP } for registered images and the reconstructed scene structure ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF |
| State / latent | outputs, pose, estimates, registered, images, reconstructed, scene, structure, points, While | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | input, reconstruction, stage, scene, graph, SfM, algorithm, ultimate | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: outputs, pose, estimates, registered, images, reconstructed, scene, structure, points, While | p. 2 (2.2. Incremental Reconstruction), p. 1 (1. Introduction), p. 2 (2.2. Incremental Reconstruction) |
| Decision / output variable | path/waypoint/velocity; body terms: SfM, algorithm, ultimate, goal, novel, robust, next, best | p. 1 (1. Introduction), p. 2 (2.2. Incremental Reconstruction), p. 3 (2.2. Incremental Reconstruction) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: methods, suffer, limited, robustness, high, computational, cost, SfM | p. 3 (2.2. Incremental Reconstruction), p. 3 (2.2. Incremental Reconstruction) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 2 (2.2. Incremental Reconstruction), p. 3 (2.2. Incremental Reconstruction), p. 3 (2.2. Incremental Reconstruction) |
| Success / guarantee | goal reach with collision-free execution | p. 7 (5. Experiments), p. 7 (5. Experiments), p. 8 (7.82 M) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** While the existing systems have advanced the state of the art tremendously, robustness, accuracy, completeness, and scalability remain the key problems in incremental SfM that ...

## What the Paper Changes

PDF contribution framing (p. 1 (1. Introduction), p. 2 (2.2. Incremental Reconstruction), p. 3 (2.2. Incremental Reconstruction), p. 2 (2.2. Incremental Reconstruction), p. 1 (1. Introduction)): In this paper, we propose a new SfM algorithm to approach this ultimate goal.

- **p. 2 / 2.2. Incremental Reconstruction - extractive PDF cue:** We propose a novel robust next best image selection method for accurate pose estimation and reliable triangulation in Sec.
- **p. 3 / 2.2. Incremental Reconstruction - extractive PDF cue:** 4.5, we propose a method to identify and parameterize highly overlapping images for efficient BA of dense collections.
- **p. 2 / 2.2. Incremental Reconstruction - extractive PDF cue:** Triangulation is a crucial step in SfM, as it increases the stability of the existing model through redundancy [58] and it enables registration of new ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Inspired by these works, increasingly largescale reconstruction systems have been developed for hundreds of thousands [1] and millions [20, 62, 51, 50] to recently a ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | The proposed components of the algorithm improve the state of the art in terms of completeness, robustness, accuracy, ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Figure 3. Scores for different number of points (left and right) with different distributions (top and bottom) in ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Robust and Efficient Triangulation. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | The reconstruction quality is comparable for all choices of V > 0.3 and increasingly degrades for a smaller ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (2.2. Incremental Reconstruction), p. 1 (1. Introduction), p. 2 (2.2. Incremental Reconstruction), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), interface p. 2 (2.2. Incremental Reconstruction), p. 1 (1. Introduction), p. 2 (2.2. Incremental Reconstruction), p. 1 (1. Introduction), objective p. 3 (2.2. Incremental Reconstruction), p. 3 (2.2. Incremental Reconstruction).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
