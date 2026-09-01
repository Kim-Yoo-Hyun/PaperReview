# Problem - OnlineSplatter: Pose-Free Online 3D Reconstruction for Free-Moving Objects

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (27 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=Y9AdTCCEgI; PDF retrieval source: https://openreview.net/pdf/561349dc7bef7809d41f05247cf1a1df95e7712f.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction)): Eliminating camera pose as input remains a key challenge in 3D reconstruction.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Free-moving object reconstruction from monocular video remains challenging, particularly without reliable pose or depth cues and under arbitrary object motion.
- **p. 1 / Abstract - extractive PDF cue:** We introduce OnlineSplatter, a novel online feed-forward framework generating highquality, object-centric 3D Gaussians directly from RGB frames without requiring camera pose, depth priors, or bundle ...
- **p. 1 / Abstract - extractive PDF cue:** Our approach anchors reconstruction using the first frame and progressively refines the object representation through a dense Gaussian primitive field, maintaining constant computational cost regardless ...
- **p. 1 / Abstract - extractive PDF cue:** Our core contribution is a dual-key memory module combining latent appearance-geometry keys with explicit directional keys, robustly fusing current frame features with temporally aggregated object ...
- **p. 1 / Abstract - extractive PDF cue:** This design enables effective handling of free-moving objects via spatial-guided memory readout and an efficient sparsification mechanism, ensuring comprehensive yet compact object coverage.
- **p. 2 / 1 Introduction - extractive PDF cue:** Eliminating camera pose as input remains a key challenge in 3D reconstruction.
- **p. 2 / 1 Introduction - extractive PDF cue:** Motivated by these challenges, we propose OnlineSplatter, a feed-forward framework for online reconstruction of freely moving objects.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Eliminating camera pose as input remains a key challenge in 3D reconstruction. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Moreover, to control memory growth as observations accumulate, we propose an attention-based memory module that fuses incoming frame features with a compact ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | Moreover, control, memory, growth, observations, accumulate, attention-based, module, fuses, incoming | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | After, encoding, input, image, timestep, features, OnlineSplatter, Transformer | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Moreover, control, memory, growth, observations, accumulate, attention-based, module, fuses, incoming | p. 2 (1 Introduction), p. 5 (3 Method), p. 3 (3 Method) |
| Decision / output variable | geometry/map/query r; body terms: address, limitations, novel, object-centric, memory, mechanism, Dual-Key, Object | p. 5 (3 Method), p. 4 (3 Method), p. 2 (1 Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: objectives, present, challenging, optimization, landscape, gradients, second, objective | p. 7 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 4 (3 Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (3 Method), p. 5 (3 Method), p. 3 (3 Method) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 8 (4.2 Results), p. 8 (4.2 Results), p. 9 (4.2 Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1 Introduction - extractive PDF cue:** Motivated by these challenges, we propose OnlineSplatter, a feed-forward framework for online reconstruction of freely moving objects.
- **p. 3 / 1 Introduction - extractive PDF cue:** Optimization-based methods typically require global bundle adjustment across all frames, which poses fundamental limitations for real-time applications.
- **p. 3 / 1 Introduction - extractive PDF cue:** Earlier methods like FvOR [50] combine learned object pose priors with alternating pose-shape optimization to reconstruct unknown objects from just a few images.

## What the Paper Changes

PDF contribution framing (p. 5 (3 Method), p. 4 (3 Method), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (3 Method)): To address these limitations, we propose a novel object-centric memory mechanism, Dual-Key 3D Object Memory, that consists of a key-value memory bank.

- **p. 4 / 3 Method - extractive PDF cue:** The input to our framework consists of a stream of RGB images {Vt}N t=0, where object masks {Mt}N t=0 are generated and applied to remove ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Our contributions are: (i) a novel feed-forward framework for object-centric online 3D reconstruction that operates on monocular RGB streams in real-time, eliminating the need for ...
- **p. 2 / 1 Introduction - extractive PDF cue:** Motivated by these challenges, we propose OnlineSplatter, a feed-forward framework for online reconstruction of freely moving objects.
- **p. 3 / 3 Method - extractive PDF cue:** To differentiate and contextualize these tokens, we introduce 3

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | 5 Limitations and Future Work Our current framework has some limitations that warrant attention. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Baselines using explicit frame selection often exhibit unstable or stagnant performance. | reported limitation/failure wording; scope must be verified |
| body cue at p. 17 | Figure 5: Impact of Training Data Quantity and Quality. C.2 Impact of Ray Alignment Loss in Geometrical Supervision. ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Future work could explore hybrid representations that maintain both rendering efficiency and mesh compatibility. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (1 Introduction), p. 5 (3 Method), p. 3 (3 Method), p. 4 (3 Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), interface p. 2 (1 Introduction), p. 5 (3 Method), p. 3 (3 Method), p. 4 (3 Method), objective p. 7 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method), p. 7 (3 Method), p. 4 (3 Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
