# Problem - NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2003.08934; PDF retrieval source: https://arxiv.org/pdf/2003.08934. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction)): In this work, we address the long-standing problem of view synthesis in a new way by directly optimizing parameters of a continuous 5D scene representation to minimize the error of ...

## PDF Body Digest

- **p. 1 / 1 Introduction - extractive body cue:** In this work, we address the long-standing problem of view synthesis in a new way by directly optimizing parameters of a continuous 5D scene representation ...
- **p. 1 / 1 Introduction - extractive body cue:** We represent a static scene as a continuous 5D function that outputs the radiance emitted in each direction (θ, φ) at each point (x, y, ...
- **p. 1 / 1 Introduction - extractive body cue:** Our method optimizes a deep fully-connected neural network without any convolutional layers (often referred to as a multilayer perceptron or MLP) to represent this function ...
- **p. 1 / 1 Introduction - extractive body cue:** To render this neural radiance field (NeRF) ⋆.
- **p. 2 / 1 Introduction - extractive body cue:** Input Images Optimize NeRF Render new views Fig.
- **p. 2 / 1 Introduction - extractive body cue:** We address these issues by transforming input 5D coordinates with a positional encoding that enables the MLP to represent higher frequency functions, and we propose ...
- **p. 2 / 1 Introduction - extractive body cue:** Crucially, our method overcomes the prohibitive storage costs of discretized voxel grids when modeling complex scenes at high-resolutions.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | In this work, we address the long-standing problem of view synthesis in a new way by directly optimizing parameters of a continuous ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Here, we visualize the set of 100 input views of the synthetic Drums scene randomly captured on a surrounding hemisphere, and we ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | Here, visualize, input, views, synthetic, Drums, scene, randomly, captured, surrounding | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Input, Images, Optimize, NeRF, Render, views, Fig, believe | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Here, visualize, input, views, synthetic, Drums, scene, randomly, captured, surrounding | p. 2 (1 Introduction), p. 18 (A Additional Implementation Details), p. 2 (1 Introduction) |
| Decision / output variable | geometry/map/query r; body terms: address, issues, transforming, input, coordinates, positional, encoding, enables | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Training, Details, real, scene, data, regularize, network, adding | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 17 (A Additional Implementation Details) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 9 (6 Results), p. 10 (6 Results), p. 10 (6 Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** In this work, we address the long-standing problem of view synthesis in a new way by directly optimizing parameters of a continuous 5D scene representation ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 17 (A Additional Implementation Details), p. 3 (1 Introduction)): We address these issues by transforming input 5D coordinates with a positional encoding that enables the MLP to represent higher frequency functions, and we propose a hierarchical sampling procedure to ...

- **p. 1 / 1 Introduction - extractive body cue:** Our method optimizes a deep fully-connected neural network without any convolutional layers (often referred to as a multilayer perceptron or MLP) to represent this function ...
- **p. 2 / 1 Introduction - extractive body cue:** Crucially, our method overcomes the prohibitive storage costs of discretized voxel grids when modeling complex scenes at high-resolutions.
- **p. 17 / A Additional Implementation Details - extractive body cue:** Volume Bounds Our method renders views by querying the neural radiance field representation at continuous 5D coordinates along camera rays.
- **p. 3 / 1 Introduction - extractive body cue:** As far as we know, this paper presents the first continuous neural scene representation that is able to render high-resolution photorealistic novel views of real ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 14 | Another direction for future work is interpretability: sampled representations such as voxel grids and meshes admit reasoning about ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | Neural Volumes cannot capture the details on the Microphone's grille or Lego's gears, and it completely fails to ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 13 | LLFF specifically provides a "sampling guideline" to not exceed 64 pixels of disparity between input views, so it ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | The real dataset consists of handheld forward-facing captures of 8 realworld scenes (NV cannot be evaluated on this ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (1 Introduction), p. 18 (A Additional Implementation Details), p. 2 (1 Introduction), p. 14 (9) Complete Model). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1 Introduction), interface p. 2 (1 Introduction), p. 18 (A Additional Implementation Details), p. 2 (1 Introduction), p. 14 (9) Complete Model), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
