# Problem - PLANA3R: Zero-shot Metric Planar 3D Reconstruction via Feed-forward Planar Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=YTwRZP8mNO; PDF retrieval source: https://openreview.net/pdf/97ce495e96b390789b58ad6d64e1a93cade2a0cf.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction)): However, these approaches face two key limitations: • Annotation dependence for feedforward methods: Learning feedforward models [36, 24, 28] typically requires accurate plane masks and 3D plane annotations from monocular ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** This paper addresses metric 3D reconstruction of indoor scenes by exploiting their inherent geometric regularities with compact representations.
- **p. 1 / Abstract - extractive PDF cue:** Using planar 3D primitives - a well-suited representation for man-made environments - we introduce PLANA3R, a pose-free framework for metric Planar 3D Reconstruction from unposed ...
- **p. 1 / Abstract - extractive PDF cue:** Our approach employs Vision Transformers to extract a set of sparse planar primitives, estimate relative camera poses, and supervise geometry learning via planar splatting, where ...
- **p. 1 / Abstract - extractive PDF cue:** Unlike prior feedforward methods that require 3D plane annotations during training, PLANA3R learns planar 3D structures without explicit plane supervision, enabling scalable training on large-scale ...
- **p. 1 / Abstract - extractive PDF cue:** We validate PLANA3R on multiple indoor-scene datasets with metric supervision and demonstrate strong generalization to out-of-domain indoor environments across diverse tasks under metric evaluation protocols, ...
- **p. 2 / 1 Introduction - extractive PDF cue:** However, these approaches face two key limitations: • Annotation dependence for feedforward methods: Learning feedforward models [36, 24, 28] typically requires accurate plane masks and ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Factors such as the difficulty of accurate camera pose estimation from indoor images [28, 11, 1] and structural distortions in the resulting 3D reconstructions [22, ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, these approaches face two key limitations: • Annotation dependence for feedforward methods: Learning feedforward models [36, 24, 28] typically requires accurate ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Our goal is to train a network F outputs a set of sparse 3D planar primitives and the 6-DoF relative camera pose ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | goal, train, network, outputs, sparse, planar, primitives, DoF, relative, camera | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | input, image, predicted, primitives, derive, patched, depth, maps | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: goal, train, network, outputs, sparse, planar, primitives, DoF, relative, camera | p. 4 (3 Method), p. 4 (3 Method), p. 5 (3 Method) |
| Decision / output variable | geometry/map/query r; body terms: address, challenges, facilitate, training, introduce, patch, loss, designed | p. 5 (3 Method), p. 2 (1 Introduction), p. 4 (3 Method) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: outline, training, objectives, Sec, After, warm-up, phase, introduce | p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 24 (A.2 Implementation Details) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (3 Method), p. 6 (3 Method), p. 24 (A.2 Implementation Details) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 7 (4 Experiment), p. 7 (4 Experiment), p. 8 (4 Experiment) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive PDF cue:** Factors such as the difficulty of accurate camera pose estimation from indoor images [28, 11, 1] and structural distortions in the resulting 3D reconstructions [22, ...
- **p. 3 / 1 Introduction - extractive PDF cue:** The regular geometry and semantic consistency of indoor environments provide an ideal context for developing models that generalize across scenes and accurately estimate metric information.

## What the Paper Changes

PDF contribution framing (p. 5 (3 Method), p. 2 (1 Introduction), p. 4 (3 Method), p. 4 (3 Method), p. 5 (3 Method)): To address these challenges and facilitate training, we introduce a patch loss designed to stabilize primitive positioning and orientation: Lpatch ∗ = α1

- **p. 2 / 1 Introduction - extractive PDF cue:** Once the model is trained, our method generates a set of 3D planar primitives that approximate indoor scenes far more efficiently than per-scene optimization methods ...
- **p. 4 / 3 Method - extractive PDF cue:** The input consists of two images I1, I2 ∈R3×H×W with camera intrinsics K1 and K2.
- **p. 4 / 3 Method - extractive PDF cue:** The core innovation of our method lies in the sparse primitive prediction architecture outlined in Sec.
- **p. 5 / 3 Method - extractive PDF cue:** After the warm-up phase, we introduce a rendering loss.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 25 | While this represents a limitation in our current analysis, it also highlights the urgent need for better benchmarks ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Figure 2: Overview of our PLANA3R. Given two images captured from the same scene, PLANA3R outputs a set ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | This process does not require merging the primitives and can be performed with a single feed-forward pass. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | 4.4 Multi-view Reconstruction with More Than Two Views PLANA3R currently supports multi-view reconstruction in a pairwise manner, but ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), interface p. 4 (3 Method), p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method), objective p. 4 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 6 (3 Method), p. 24 (A.2 Implementation Details).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
