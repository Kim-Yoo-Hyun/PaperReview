# Problem - Dynamic Graph CNN for Learning on Point Clouds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1801.07829; PDF retrieval source: https://arxiv.org/pdf/1801.07829. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): This independence, however, neglects the geometric relationships among points, presenting a fundamental limitation that cannot capture local features.

## PDF Body Digest

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** Point clouds, or scattered collections of points in 2D or 3D, are arguably the simplest shape representation; they also comprise the output of 3D sensing ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** With the advent of fast 3D point cloud acquisition, recent pipelines for graphics and vision often process point clouds directly, bypassing expensive mesh reconstruction or ...
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** A few of the many recent applications of point cloud processing and analysis include indoor navigation [Zhu et al.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** 2017], self-driving vehicles [Liang et al.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** 2008b], and shape synthesis and modeling [Golovinskiy et al.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** This independence, however, neglects the geometric relationships among points, presenting a fundamental limitation that cannot capture local features.
- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** This approach, however, usually introduces quantization artifacts and excessive memory usage, making it difficult to go to capture high-resolution or fine-grained features.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This independence, however, neglects the geometric relationships among points, presenting a fundamental limitation that cannot capture local features. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | State-of-the-art deep neural networks are designed specifically to handle the irregularity of point clouds, directly manipulating raw point cloud data rather than ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | State-of-the-art, deep, neural, networks, designed, specifically, handle, irregularity, point, clouds | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | summarize, contributions, follows, present, novel, operation, learning, point | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: State-of-the-art, deep, neural, networks, designed, specifically, handle, irregularity, point, clouds | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Decision / output variable | geometry/map/query r; body terms: summarize, contributions, follows, present, novel, operation, learning, point | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: not recovered | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 10 (4 EVALUATION), p. 7 (4 EVALUATION), p. 7 (4 EVALUATION) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** This approach, however, usually introduces quantization artifacts and excessive memory usage, making it difficult to go to capture high-resolution or fine-grained features.

## What the Paper Changes

PDF contribution framing (p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION)): We summarize the key contributions of our work as follows: • We present a novel operation for learning from point clouds, EdgeConv, to better capture local geometric features of point ...

- **p. 2 / 1 INTRODUCTION - extractive PDF cue:** To address these drawbacks, we propose a novel simple operation, called EdgeConv, which captures local geometric structure while maintaining permutation invariance.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | This confirms our hypothesis that for certain density, with large k the Euclidean distance fails to approximate geodesic ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | We further evaluate the robustness of our model (trained on 1,024 points with k = 20) to point ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Our model is robust to partial data. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), interface p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
