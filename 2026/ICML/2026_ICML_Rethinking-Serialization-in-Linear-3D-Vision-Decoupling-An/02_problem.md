# Problem - Rethinking Serialization in Linear 3D Vision: Decoupling Anisotropic Geometry from Isotropic Semantics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=MSVQM8Ub2y; PDF retrieval source: https://openreview.net/pdf/fa9e033b756ac063d19be2b3bb91daea759e1ae1.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction)): Effective 3D point cloud understanding must reconcile local anisotropic geometry with global isotropic semantics, but the irregular and unordered nature of point sets makes this difficult.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Current linear State-Space Models (SSMs) for 3D point clouds typically rely on 1D serialization schemes (e.g., Hilbert curves) for global modeling.
- **p. 1 / Abstract - extractive body cue:** In dense scenes, such imposed order can disrupt spatial continuity and induce what we call serialization bias.
- **p. 1 / Abstract - extractive body cue:** We propose AnIsoNet, a framework that decouples anisotropic geometry from isotropic semantics via two dedicated modules: Local Anisotropy Geometric Modeling (LAGM) and Global Isotropy Semantic ...
- **p. 1 / Abstract - extractive body cue:** LAGM uses ellipsoidal encoding to capture local directionality without relying on global order.
- **p. 1 / Abstract - extractive body cue:** GISA is configured according to dataset-level geometric density: dense-scene datasets use Identity Mode to avoid additional geometry-driven re-serialization, whereas sparseobject datasets use Morton serialization to ...
- **p. 1 / 1. Introduction - extractive body cue:** Effective 3D point cloud understanding must reconcile local anisotropic geometry with global isotropic semantics, but the irregular and unordered nature of point sets makes this ...
- **p. 2 / 1. Introduction - extractive body cue:** However, unlike Transformers that support noncausal attention, the strict recurrent path dependency of SSMs (where state ht strictly depends on ht-1) introduces a new serialization ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Effective 3D point cloud understanding must reconcile local anisotropic geometry with global isotropic semantics, but the irregular and unordered nature of point ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | In Mamba (Gu & Dao, 2024), the state evolves as: ht = ¯A · ht-1 + ¯Bt · xt, yt = Ct ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Mamba, Dao, state, evolves, ht-1, where, recurrent, hidden, inputdependent, step | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Current, State-Space, Models, SSMs, typically, force, point, clouds | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Mamba, Dao, state, evolves, ht-1, where, recurrent, hidden, inputdependent, step | p. 5 (3.1. Overview), p. 5 (3.1. Overview), p. 3 (3.1. Overview) |
| Decision / output variable | geometry/map/query r; body terms: observation, AnIsoNet, decouples, local, anisotropic, geometry, modeling, global | p. 2 (1. Introduction), p. 3 (3.1. Overview), p. 3 (3.1. Overview) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: objective, LAGM, capture, local, anisotropy, within, k-NN, neighborhoods | p. 3 (3.1. Overview), p. 3 (3.1. Overview), p. 4 (3.1. Overview), p. 4 (3.1. Overview), p. 5 (3.1. Overview), p. 5 (3.1. Overview) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.1. Overview), p. 5 (3.1. Overview), p. 5 (3.1. Overview) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 8 (4.4. Efficiency Analysis), p. 8 (4.4. Efficiency Analysis), p. 6 (4.2. Main Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** However, unlike Transformers that support noncausal attention, the strict recurrent path dependency of SSMs (where state ht strictly depends on ht-1) introduces a new serialization ...
- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are as follows: • We identify serialization bias as a key bottleneck in 3D SSMs and propose a decoupling paradigm that addresses local ...
- **p. 1 / 1. Introduction - extractive body cue:** Early architectures, exemplified by PointNet++ (Qi et al., 2017b), prioritized local anisotropy through hierarchical grouping, yet struggled to maintain long-range global semantic coherence.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 3 (3.1. Overview), p. 3 (3.1. Overview), p. 2 (1. Introduction), p. 5 (3.1. Overview)): Based on this observation, we propose AnIsoNet, which decouples local anisotropic geometry modeling from global semantic aggregation.

- **p. 3 / 3.1. Overview - extractive body cue:** The framework consists of two complementary modules: 1.
- **p. 3 / 3.1. Overview - extractive body cue:** To address this limitation, we propose AnIsoNet, a unified framework that decouples these two processes (Figure 2).
- **p. 2 / 1. Introduction - extractive body cue:** Our contributions are as follows: • We identify serialization bias as a key bottleneck in 3D SSMs and propose a decoupling paradigm that addresses local ...
- **p. 5 / 3.1. Overview - extractive body cue:** The recurrence ht = f(ht-1, xt) inherently requires a sequential ordering, so 3D point clouds must be artificially serialized and the contribution of xs to ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | A mismatched mode therefore causes noticeable degradation rather than collapse. | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Because our claim concerns robustness rather than strict permutation invariance, we directly test the task-relevant notion of robustness ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (3.1. Overview), p. 5 (3.1. Overview), p. 3 (3.1. Overview), p. 3 (3.1. Overview). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), interface p. 5 (3.1. Overview), p. 5 (3.1. Overview), p. 3 (3.1. Overview), p. 3 (3.1. Overview), objective p. 3 (3.1. Overview), p. 3 (3.1. Overview), p. 4 (3.1. Overview), p. 4 (3.1. Overview), p. 5 (3.1. Overview), p. 5 (3.1. Overview).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
