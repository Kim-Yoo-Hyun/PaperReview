# Problem - MeshLLM: Empowering Large Language Models to Progressively Understand and Generate 3D Mesh

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (3 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Fang_MeshLLM_Empowering_Large_Language_Models_to_Progressively_Understand_and_Generate_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Fang_MeshLLM_Empowering_Large_Language_Models_to_Progressively_Understand_and_Generate_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1.2. Metric Details), p. 1 (2.1. Shape Novelty Analysis)): The evaluation of the generation of 3D mesh can be challenging due to the lack of direct correspondence with ground truth data.

## PDF Body Digest

- **p. 1 / Body text (section not recovered) - extractive body cue:** MeshLLM: Empowering Large Language Models to Progressively Understand and Generate 3D Mesh Supplementary Material
- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** We begin by densely sampling point clouds from the mesh and then apply farthest point sampling (FPS) and KNN to identify central points and point ...
- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** For mesh-derived dense point clouds, FPS begins with a random point and iteratively chooses the farthest point to yield N center points.
- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** These N points serve as centroids for KNN clustering.
- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** The face category is determined through a voting process based on the categories of these sampled points.
- **p. 1 / 1.2. Metric Details - extractive body cue:** The evaluation of the generation of 3D mesh can be challenging due to the lack of direct correspondence with ground truth data.
- **p. 1 / 2.1. Shape Novelty Analysis - extractive body cue:** This demonstrates that our model possesses generalization ability and creativity rather than merely replicating training samples.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The evaluation of the generation of 3D mesh can be challenging due to the lack of direct correspondence with ground truth data. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | For mesh-derived dense point clouds, FPS begins with a random point and iteratively chooses the farthest point to yield N center points. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | mesh-derived, dense, point, clouds, FPS, begins, random, iteratively, chooses, farthest | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | MeshLLM, introduce, progressive, training, strategy, begins, KNN-based, Primitive-Mesh | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: mesh-derived, dense, point, clouds, FPS, begins, random, iteratively, chooses, farthest | p. 1 (1.1. Construction of Primitive-Mesh), p. 1 (1.1. Construction of Primitive-Mesh) |
| Decision / output variable | geometry/map/query r; body terms: MeshLLM, introduce, progressive, training, strategy, begins, KNN-based, Primitive-Mesh | p. 2 (2.2. Training Strategy Analysis), p. 1 (1.1. Construction of Primitive-Mesh) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: strategy, provides, more, accurate, semantic, information, mesh, parts | p. 1 (1.1. Construction of Primitive-Mesh), p. 1 (1.2. Metric Details) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (1.1. Construction of Primitive-Mesh), p. 1 (1.1. Construction of Primitive-Mesh) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 1 (2.1. Shape Novelty Analysis), p. 1 (2.1. Shape Novelty Analysis), p. 2 (2.1. Shape Novelty Analysis) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 2.1. Shape Novelty Analysis - extractive body cue:** This demonstrates that our model possesses generalization ability and creativity rather than merely replicating training samples.

## What the Paper Changes

PDF body contribution framing (p. 2 (2.2. Training Strategy Analysis), p. 1 (1.1. Construction of Primitive-Mesh)): In MeshLLM, we introduce a progressive training strategy that begins with KNN-based Primitive-Mesh samples, followed by Semantic-based Primitive-Mesh samples, and concludes with training on specific mesh generation and understanding tasks.

- **p. 1 / 1.1. Construction of Primitive-Mesh - extractive body cue:** SamPart3D is pretrained on Objaverse [2] with a 3D backbone network designed to extract visual features.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 3 | Figure 3. Failure case. The limited semantic dataset size reduces text-geometry alignment for more fine-grained generations. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (1.1. Construction of Primitive-Mesh), p. 1 (1.1. Construction of Primitive-Mesh). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1.2. Metric Details), p. 1 (2.1. Shape Novelty Analysis), interface p. 1 (1.1. Construction of Primitive-Mesh), p. 1 (1.1. Construction of Primitive-Mesh), objective p. 1 (1.1. Construction of Primitive-Mesh), p. 1 (1.2. Metric Details).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
