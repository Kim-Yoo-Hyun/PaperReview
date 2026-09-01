# Problem - In-Place Scene Labelling and Understanding with Implicit Scene Representation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (14 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2103.15875; PDF retrieval source: https://arxiv.org/pdf/2103.15875. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction)): Semantic scene understanding means attaching class laFusion via Learning Label Denoising Super-Resolution Label Propagation Label Synthesis Label Interpolation Figure 1: Neural radiance fields (NeRF) jointly encoding appearance and geom ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Semantic labelling is highly correlated with geometry and radiance reconstruction, as scene entities with similar shape and appearance are more likely to come from similar ...
- **p. 1 / Abstract - extractive PDF cue:** Recent implicit neural reconstruction techniques are appealing as they do not require prior training data, but the same fully self-supervised approach is not possible for ...
- **p. 1 / Abstract - extractive PDF cue:** We extend neural radiance fields (NeRF) to jointly encode semantics with appearance and geometry, so that complete and accurate 2D semantic labels can be achieved ...
- **p. 1 / Abstract - extractive PDF cue:** The intrinsic multi-view consistency and smoothness of NeRF benefit semantics by enabling sparse labels to efficiently propagate.
- **p. 1 / Abstract - extractive PDF cue:** We show the benefit of this approach when labels are either sparse or very noisy in room-scale scenes.
- **p. 1 / 1. Introduction - extractive PDF cue:** Semantic scene understanding means attaching class laFusion via Learning Label Denoising Super-Resolution Label Propagation Label Synthesis Label Interpolation Figure 1: Neural radiance fields (NeRF) jointly ...
- **p. 2 / 1. Introduction - extractive PDF cue:** In addition, multi-view consistency is inherent to the training process and enables the network to produce accurate semantic labels of the scene, including for views ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Semantic scene understanding means attaching class laFusion via Learning Label Denoising Super-Resolution Label Propagation Label Synthesis Label Interpolation Figure 1: Neural radiance ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Given multiple images of a static scene with known camera intrinsics and extrinsics, NeRF [16] uses MLPs to implicitly represent the continuous ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | Given, multiple, images, static, scene, known, camera, intrinsics, extrinsics, NeRF | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | chosen, multi-class, cross-entropy, loss, encourage, rendered, semantic, labels | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Given, multiple, images, static, scene, known, camera, intrinsics, extrinsics, NeRF | p. 2 (3.1. Preliminaries), p. 2 (1. Introduction), p. 3 (3.3. Network Training) |
| Decision / output variable | geometry/map/query r; body terms: addition, multi-view, consistency, inherent, training, process, enables, network | p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: chosen, multi-class, cross-entropy, loss, encourage, rendered, semantic, labels | p. 3 (3.3. Network Training), p. 3 (3.1. Preliminaries) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (3.3. Network Training), p. 3 (3.3. Network Training) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 5 (4.4. Semantic Fusion), p. 8 (4.4. Semantic Fusion), p. 4 (4.4. Semantic Fusion) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive PDF cue:** Semantic scene understanding means attaching class laFusion via Learning Label Denoising Super-Resolution Label Propagation Label Synthesis Label Interpolation Figure 1: Neural radiance fields (NeRF) jointly ...

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (3.1. Preliminaries)): In addition, multi-view consistency is inherent to the training process and enables the network to produce accurate semantic labels of the scene, including for views that are substantially different from ...

- **p. 1 / 1. Introduction - extractive PDF cue:** In this paper, we show how to design a scene-specific network for joint geometric and semantic prediction and train it on images from a single ...
- **p. 1 / 1. Introduction - extractive PDF cue:** Unlike scene geometry, however, semantic classes are a human-defined concept and it is not possible to semantically label a novel scene in a purely self-supervised ...
- **p. 2 / 3.1. Preliminaries - extractive PDF cue:** Specifically, σ(x) is designed to be a function of only 3D position while the radiance c(x, d) is a function of both 3D position and ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 4 | batch size of rays is set to 1024 due to memory limitations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | Given multiple noisy or partial semantic labels, the network can fuse them into a joint implicit 3D space ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Quantitative results shown in Table 1 also confirm that accurate denoised labels are obtained after training-as-fusion. | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | After training using only these noisy labels, we obtain denoised semantic labels by rendering back to the same ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (3.1. Preliminaries), p. 2 (1. Introduction), p. 3 (3.3. Network Training), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), interface p. 2 (3.1. Preliminaries), p. 2 (1. Introduction), p. 3 (3.3. Network Training), p. 1 (1. Introduction), objective p. 3 (3.3. Network Training), p. 3 (3.1. Preliminaries).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
