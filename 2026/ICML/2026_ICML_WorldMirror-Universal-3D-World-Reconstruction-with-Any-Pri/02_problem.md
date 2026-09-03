# Problem - WorldMirror: Universal 3D World Reconstruction with Any-Prior Prompting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (23 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=HFNJOpXHfm; PDF retrieval source: https://openreview.net/pdf/d37648c3826e3031b270765b6a36790ab19140f8.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction)): Pow3R (Jang et al., 2025) enables prior-conditioned binocular reconstruction but outputs only point maps, while VGGT (Wang et al., 2025a) predicts multiple geometric quantities but lacks the ability to incorporate ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** We present WorldMirror, a unified feed-forward model for comprehensive 3D geometric prediction tasks.
- **p. 1 / Abstract - extractive body cue:** Unlike existing methods constrained to image-only inputs or customized for a specific task, our framework flexibly integrates diverse geometric priors, including camera poses, intrinsics, and ...
- **p. 1 / Abstract - extractive body cue:** Remarkably, prior injection yields universal gains across all tasks, suggesting that input flexibility and multi-task prediction are mutually reinforcing.
- **p. 1 / Abstract - extractive body cue:** WorldMirror achieves state-of-the-art performance across diverse benchmarks from camera, point map, depth, and surface normal estimation
- **p. 1 / 1. Introduction - extractive body cue:** Visual geometry learning is fundamental to augmented reality, robotics, and autonomous navigation.
- **p. 2 / 1. Introduction - extractive body cue:** Pow3R (Jang et al., 2025) enables prior-conditioned binocular reconstruction but outputs only point maps, while VGGT (Wang et al., 2025a) predicts multiple geometric quantities but ...
- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we introduce WorldMirror, a unified end-to-end framework that performs comprehensive 3D tasks while flexibly leveraging any available geometric modalities.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Pow3R (Jang et al., 2025) enables prior-conditioned binocular reconstruction but outputs only point maps, while VGGT (Wang et al., 2025a) predicts multiple ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | (2) We propose Multi-modal Tokenization, which treats multiple input types including RGB images, camera intrinsics, poses, and depth as tokens, enabling seamless ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Multi-modal, Tokenization, treats, multiple, input, types, including, RGB, images, camera | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | multi-task, architecture, curriculum, learning, produces, comprehensive, geometric, outputs | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Multi-modal, Tokenization, treats, multiple, input, types, including, RGB, images, camera | p. 2 (1. Introduction), p. 3 (3. Method), p. 3 (3. Method) |
| Decision / output variable | geometry/map/query r; body terms: summarize, contributions, follows, present, WorldMirror, unified, end-to-end, framework | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: model, trained, end-to-end, minimizing, composite, loss, function, integrates | p. 5 (4. Model Training), p. 5 (3.2. Unified Spatial Prediction), p. 6 (4. Model Training), p. 6 (4. Model Training) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (4. Model Training), p. 6 (4. Model Training), p. 3 (3.1. Multi-modal Tokenization) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (5.1. Evaluation on Different Tasks), p. 7 (5.1. Evaluation on Different Tasks), p. 17 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** To address these challenges, we introduce WorldMirror, a unified end-to-end framework that performs comprehensive 3D tasks while flexibly leveraging any available geometric modalities.
- **p. 1 / 1. Introduction - extractive body cue:** Current methods remain fragmented, typically assuming RGB images as the sole input and ignoring auxiliary cues such as camera intrin1.

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method), p. 4 (3.1. Multi-modal Tokenization), p. 4 (3.2. Unified Spatial Prediction)): We summarize our contributions as follows: (1) We present WorldMirror, a unified end-to-end framework for 3D geometry that jointly addresses flexible prior conditioning and comprehensive multi-task prediction within a single ...

- **p. 2 / 1. Introduction - extractive body cue:** (3) We introduce a Unified Spatial Prediction architecture with a decoupled sequential training that effectively coordinates multi-task training across camera poses, depth, normals, point maps, ...
- **p. 3 / 3. Method - extractive body cue:** We introduce two core components: (1) Multi-modal Tokenization (Sec.
- **p. 4 / 3.1. Multi-modal Tokenization - extractive body cue:** Besides real photos, our method generalizes well to AI-created videos spanning diverse styles. dropped tokens to zero.
- **p. 4 / 3.2. Unified Spatial Prediction - extractive body cue:** To address these issues, we introduce a decoupled modeling strategy that separates geometry prediction from appearance reconstruction, along with a curriculum learning scheme that progressively ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 16 | Table 12. Robustness evaluation of WorldMirror with noisy priors on 7-Scenes and DTU datasets. The model exhibits graceful ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Trained with dynamic resolutions, our model generalizes robustly across varying resolutions and consistently surpasses baselines. | reported limitation/failure wording; scope must be verified |
| body cue at p. 23 | Figure 11. Visual Comparisons of In-The-Wild Multi-View 3D Reconstruction. WorldMirror delivers superior reconstruction fidelity with in-the-wild images as ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1. Introduction), p. 3 (3. Method), p. 3 (3. Method), p. 5 (3.2. Unified Spatial Prediction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), interface p. 2 (1. Introduction), p. 3 (3. Method), p. 3 (3. Method), p. 5 (3.2. Unified Spatial Prediction), objective p. 5 (4. Model Training), p. 5 (3.2. Unified Spatial Prediction), p. 6 (4. Model Training), p. 6 (4. Model Training).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
