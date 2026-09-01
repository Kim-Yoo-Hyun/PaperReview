# Problem - CoE: Deep Coupled Embedding for Non-Rigid Point Cloud Correspondences

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=pIDl4wuZoG&name=pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 4 (3. Background and Notation), p. 1 (1. Introduction), p. 4 (3. Background and Notation), p. 3 (3. Background and Notation)): (1), this modification greatly reduced the computational complexity, however it still involves difficult manifold optimisation for only approximately solving the original one.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** The interest in matching non-rigidly deformed shapes represented as raw point clouds is rising due to the proliferation of low-cost 3D sensors.
- **p. 1 / Abstract - extractive PDF cue:** Yet, the task is challenging since point clouds are irregular and there is a lack of intrinsic shape information.
- **p. 1 / Abstract - extractive PDF cue:** We propose to tackle these challenges by learning a new shape representation - a per-point high dimensional embedding, in an embedding space where semantically similar ...
- **p. 1 / Abstract - extractive PDF cue:** The learned embedding has multiple beneficial properties: it is aware of the underlying shape geometry and is robust to shape deformations and various shape artefacts, ...
- **p. 1 / Abstract - extractive PDF cue:** Consequently, this embedding can be directly employed to retrieve high-quality dense correspondences through a simple nearest neighbor search in the embedding space.
- **p. 4 / 3. Background and Notation - extractive PDF cue:** (1), this modification greatly reduced the computational complexity, however it still involves difficult manifold optimisation for only approximately solving the original one.
- **p. 1 / 1. Introduction - extractive PDF cue:** Most of them are designed for shapes represented as triangular meshes and cannot be extended to point clouds without performance degradation [7, 21, 28].

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | (1), this modification greatly reduced the computational complexity, however it still involves difficult manifold optimisation for only approximately solving the original one. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | All methods only take point clouds as input except the multimodal method SSMSM [7], which requires meshes. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | methods, only, take, point, clouds, input, except, multimodal, SSMSM, requires | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Inspired, classical, geometry, processing, technique, effective, simple, only | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: methods, only, take, point, clouds, input, except, multimodal, SSMSM, requires | p. 6 (4.2. Unsupervised Loss), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: summary, contributions, novel, unsupervised, learn, per-point, embeddings, directly | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3. Background and Notation) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Orthogonal, Loss, constraint, Off-diagonal, Similar, Finally, full, unsupervised | p. 5 (4.2. Unsupervised Loss), p. 5 (4.2. Unsupervised Loss), p. 6 (4.2. Unsupervised Loss) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (4.2. Unsupervised Loss), p. 5 (4.2. Unsupervised Loss), p. 6 (4.2. Unsupervised Loss) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (5.2. Near-isometric Shape Matching), p. 7 (5.2. Near-isometric Shape Matching), p. 8 (5.5. Robustness) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** Most of them are designed for shapes represented as triangular meshes and cannot be extended to point clouds without performance degradation [7, 21, 28].
- **p. 4 / 3. Background and Notation - extractive PDF cue:** (1) does not scale well with the size of the shape, it makes the optimisation problem very challenging or even intractable for high resolution shapes.
- **p. 3 / 3. Background and Notation - extractive PDF cue:** Given shapes S and T and their LBOs represented in stiffness matrices LS, LT and mass matrices MS, MT , the coupled diagonalisation problem can ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3. Background and Notation), p. 5 (4.2. Unsupervised Loss), p. 5 (4.2. Unsupervised Loss)): In summary, our contributions are: • We propose a novel unsupervised way to learn per-point embeddings directly from raw point clouds under various non-rigid deformations.

- **p. 2 / 1. Introduction - extractive PDF cue:** Inspired by classical geometry processing technique, our method is effective and simple that only requires to train a single network. • In our learned embedding ...
- **p. 4 / 3. Background and Notation - extractive PDF cue:** To overcome these issues, we propose to directly learn coupled embeddings without any ground truth correspondences and without any subspace parameterisation.
- **p. 5 / 4.2. Unsupervised Loss - extractive PDF cue:** Our unsupervised loss is inspired by the work of classical geometry processing [16, 22] and consists of three terms.
- **p. 5 / 4.2. Unsupervised Loss - extractive PDF cue:** To our best knowledge, this enables, for the first time, the practical application

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 15 | Figure 16. Qualitative results on DT4D-M. More qualitative non-isometric matching results (top) . Failure cases mainly due to ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Limitations, Future Work and Conclusion In this paper, we proposed an unsupervised method to learn high-quality, well-generalised embeddings ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 14 | Figure 13. Failure cases on FAUST. All three failure examples relate to the touching hands, where the points ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | Figure 7. Visualisation of a challenging pair with crossed legs. We show our full design can successfully handle ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 6 (4.2. Unsupervised Loss), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 4 (3. Background and Notation), p. 1 (1. Introduction), p. 4 (3. Background and Notation), p. 3 (3. Background and Notation), interface p. 6 (4.2. Unsupervised Loss), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), objective p. 5 (4.2. Unsupervised Loss), p. 5 (4.2. Unsupervised Loss), p. 6 (4.2. Unsupervised Loss).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
