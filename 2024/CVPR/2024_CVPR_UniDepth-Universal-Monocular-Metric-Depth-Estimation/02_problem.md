# Problem - UniDepth: Universal Monocular Metric Depth Estimation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2403.18913; PDF retrieval source: https://arxiv.org/pdf/2403.18913. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction)): However, relying only on this single additional module clearly results in challenges related to training stability and scale ambiguity.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Accurate monocular metric depth estimation (MMDE) is crucial to solving downstream tasks in 3D perception and modeling.
- **p. 1 / Abstract - extractive PDF cue:** However, the remarkable accuracy of recent MMDE methods is confined to their training domains.
- **p. 1 / Abstract - extractive PDF cue:** These methods fail to generalize to unseen domains even in the presence of moderate domain gaps, which hinders their practical applicability.
- **p. 1 / Abstract - extractive PDF cue:** We propose a new model, UniDepth, capable of reconstructing metric 3D scenes from solely single images across domains.
- **p. 1 / Abstract - extractive PDF cue:** Departing from the existing MMDE methods, UniDepth directly predicts metric 3D points from the input image at inference time without any additional information, striving for ...
- **p. 2 / 1. Introduction - extractive PDF cue:** However, relying only on this single additional module clearly results in challenges related to training stability and scale ambiguity.
- **p. 1 / 1. Introduction - extractive PDF cue:** Unlike existing methods, UniDepth delivers metric 3D predictions for any scene solely from a single image, waiving the need for extra information about scene or ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, relying only on this single additional module clearly results in challenges related to training stability and scale ambiguity. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | We introduce UniDepth, a novel approach that directly predicts 3D points in a scene with only one image as input. | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | introduce, UniDepth, novel, directly, predicts, points, scene, only, image, input | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | effective, pseudo-spherical, representation, output, space, disentangle, camera, depth | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: introduce, UniDepth, novel, directly, predicts, points, scene, only, image, input | p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: introduce, UniDepth, novel, directly, predicts, points, scene, only | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: bi-directional, loss, computed, Lcon, D1/E1, D2/E2, Therefore, geometric | p. 4 (3.3. Geometric Invariance Loss), p. 4 (3.3. Geometric Invariance Loss) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3.3. Geometric Invariance Loss), p. 4 (3.3. Geometric Invariance Loss) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (4.2. Comparison with the State of the Art), p. 5 (4.1. Experimental Setup), p. 8 (4.3. Ablation Study) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** Unlike existing methods, UniDepth delivers metric 3D predictions for any scene solely from a single image, waiving the need for extra information about scene or ...
- **p. 1 / 1. Introduction - extractive PDF cue:** While existing MMDE methods [3, 14, 16, 40, 41, 43, 61] have demonstrated remarkable accuracy across different benchmarks, they require training and testing on datasets ...
- **p. 2 / 1. Introduction - extractive PDF cue:** Moreover, we extensively test UniDepth and re-evaluate seven MMDE Stateof-the-Art (SotA) methods on ten different datasets in a fair and comparable zero-shot setup to lay ...

## What the Paper Changes

PDF contribution framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.3. Geometric Invariance Loss), p. 1 (1. Introduction)): We introduce UniDepth, a novel approach that directly predicts 3D points in a scene with only one image as input.

- **p. 2 / 1. Introduction - extractive PDF cue:** Additionally, we introduce a geometric invariance loss to enhance the robustness of depth estimation.
- **p. 2 / 1. Introduction - extractive PDF cue:** We propose an effective pseudo-spherical representation of the output space to disentangle the camera and depth dimensions of this space.
- **p. 4 / 3.3. Geometric Invariance Loss - extractive PDF cue:** To this end, we propose a geometric invariance loss to enforce the consistency of camera-prompted depth features of the same scene from different acquisition sensors.
- **p. 1 / 1. Introduction - extractive PDF cue:** Our approach, named UniDepth, is the first that attempts to solve this challenging task without restrictions on scene composition and setup and distinguishes itself through ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | This limitation is underscored by the marked variability observed for test sets strongly out-of-distribution, such as KITTI, when ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | The designed self-prompting camera allows camera-free test time application and renders the model more robust against camera noise. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | This pitfall is demonstrated by the drop in scale-dependent metrics, e.g. | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Moreover, ZoeDepth, which has a capacity similar to our ViT-based approach and is pre-trained on the diverse MiDaS ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), interface p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), objective p. 4 (3.3. Geometric Invariance Loss), p. 4 (3.3. Geometric Invariance Loss).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
