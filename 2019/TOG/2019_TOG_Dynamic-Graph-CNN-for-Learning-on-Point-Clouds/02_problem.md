# Problem - Dynamic Graph CNN for Learning on Point Clouds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1801.07829; PDF retrieval source: https://arxiv.org/pdf/1801.07829. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): This independence, however, neglects the geometric relationships among points, presenting a fundamental limitation that cannot capture local features.

## PDF Body Digest

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Point clouds, or scattered collections of points in 2D or 3D, are arguably the simplest shape representation; they also comprise the output of 3D sensing ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** With the advent of fast 3D point cloud acquisition, recent pipelines for graphics and vision often process point clouds directly, bypassing expensive mesh reconstruction or ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** A few of the many recent applications of point cloud processing and analysis include indoor navigation [Zhu et al.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** 2017], self-driving vehicles [Liang et al.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** 2008b], and shape synthesis and modeling [Golovinskiy et al.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This independence, however, neglects the geometric relationships among points, presenting a fundamental limitation that cannot capture local features.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** This approach, however, usually introduces quantization artifacts and excessive memory usage, making it difficult to go to capture high-resolution or fine-grained features.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This independence, however, neglects the geometric relationships among points, presenting a fundamental limitation that cannot capture local features. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Point clouds provide a flexible geometric representation suitable for countless applications in computer graphics; they also comprise the raw output of most ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Point, clouds, provide, flexible, geometric, representation, suitable, countless, applications, computer | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Point, clouds, scattered, collections, points, arguably, simplest, shape | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Point, clouds, provide, flexible, geometric, representation, suitable, countless, applications, computer | p. 1 (Body text (section not recovered)), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Decision / output variable | geometry/map/query r; body terms: summarize, contributions, follows, present, novel, operation, learning, point | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (Body text (section not recovered)) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Permission, make, digital, hard, copies, part, personal, classroom | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (Body text (section not recovered)) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 10 (4 EVALUATION), p. 7 (4 EVALUATION), p. 7 (4 EVALUATION) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive body cue:** This approach, however, usually introduces quantization artifacts and excessive memory usage, making it difficult to go to capture high-resolution or fine-grained features.

## What the Paper Changes

PDF body contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (Body text (section not recovered)), p. 1 (Body text (section not recovered))): We summarize the key contributions of our work as follows: • We present a novel operation for learning from point clouds, EdgeConv, to better capture local geometric features of point ...

- **p. 2 / 1 INTRODUCTION - extractive body cue:** To address these drawbacks, we propose a novel simple operation, called EdgeConv, which captures local geometric structure while maintaining permutation invariance.
- **p. 1 / Body text (section not recovered) - extractive body cue:** To this end, we propose a new neural network module dubbed EdgeConv suitable for CNN-based high-level tasks on point clouds including classification and segmentation.
- **p. 1 / Body text (section not recovered) - extractive body cue:** We show the performance of our model on standard benchmarks including ModelNet40, ShapeNetPart, and S3DIS.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | This confirms our hypothesis that for certain density, with large k the Euclidean distance fails to approximate geodesic ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | We further evaluate the robustness of our model (trained on 1,024 points with k = 20) to point ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Our model is robust to partial data. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 1 (Body text (section not recovered)), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (Body text (section not recovered)). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), interface p. 1 (Body text (section not recovered)), p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (Body text (section not recovered)), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
