# Problem - Depth Map Prediction from a Single Image using a Multi-Scale Deep Network

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1406.2283; PDF retrieval source: https://arxiv.org/pdf/1406.2283. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1 Introduction), p. 1 (1 Introduction)): Moreover, the task is inherently ambiguous, and a technically ill-posed problem: Given an image, an infinite number of possible world scenes may have produced it.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** Predicting depth is an essential component in understanding the 3D geometry of a scene.
- **p. 1 / Abstract - extractive PDF cue:** While for stereo images local correspondence suffices for estimation, finding depth relations from a single image is less straightforward, requiring integration of both global and ...
- **p. 1 / Abstract - extractive PDF cue:** Moreover, the task is inherently ambiguous, with a large source of uncertainty coming from the overall scale.
- **p. 1 / Abstract - extractive PDF cue:** In this paper, we present a new method that addresses this task by employing two deep network stacks: one that makes a coarse global prediction ...
- **p. 1 / Abstract - extractive PDF cue:** We also apply a scale-invariant error to help measure depth relations rather than scale.
- **p. 1 / 1 Introduction - extractive PDF cue:** Moreover, the task is inherently ambiguous, and a technically ill-posed problem: Given an image, an infinite number of possible world scenes may have produced it.
- **p. 1 / 1 Introduction - extractive PDF cue:** While there is much prior work on estimating depth based on stereo images or motion [17], there has been relatively little on estimating depth from ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Moreover, the task is inherently ambiguous, and a technically ill-posed problem: Given an image, an infinite number of possible world scenes may ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Both stacks are applied to the original input, but in addition, the coarse network's output is passed to the fine network as ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | stacks, applied, original, input, addition, coarse, network, output, passed, fine | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | final, output, resolution, compared, input, itself, downsampled, original | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: stacks, applied, original, input, addition, coarse, network, output, passed, fine | p. 2 (3 Approach), p. 3 (3 Approach), p. 3 (3 Approach) |
| Decision / output variable | geometry/map/query r; body terms: present, estimating, depth, single, image, fine-scale, network, stack | p. 2 (1 Introduction), p. 3 (3 Approach), p. 4 (3 Approach) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: per-sample, training, loss, addition, performance, evaluation, tried, scale-invariant | p. 4 (3 Approach), p. 4 (3 Approach), p. 5 (3 Approach), p. 2 (3 Approach), p. 3 (3 Approach) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (3 Approach), p. 5 (3 Approach), p. 5 (3 Approach) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 5 (4 Experiments), p. 7 (5 Results), p. 6 (5 Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive PDF cue:** While there is much prior work on estimating depth based on stereo images or motion [17], there has been relatively little on estimating depth from ...

## What the Paper Changes

PDF contribution framing (p. 2 (1 Introduction), p. 3 (3 Approach), p. 4 (3 Approach), p. 1 (1 Introduction), p. 2 (3 Approach)): In this paper we present a new approach for estimating depth from a single image.

- **p. 3 / 3 Approach - extractive PDF cue:** The fine-scale network stack consists of convolutional layers only, along with one pooling stage for the first layer edge features.
- **p. 4 / 3 Approach - extractive PDF cue:** In addition to the scale-invariant error, we also measure the performance of our method according to several error metrics have been proposed in prior works, ...
- **p. 1 / 1 Introduction - extractive PDF cue:** Thus, stereo depth estimation can be reduced to developing robust image point correspondences - which can often be found using local appearance features.
- **p. 2 / 3 Approach - extractive PDF cue:** Similarly, the lower and middle layers are designed to combine information from different parts of the image through max-pooling operations to a small spatial dimension.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | In future work, we plan to extend our method to incorporate further 3D geometry information, such as surface ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | Although the fine-scale network does not improve in the error measurements, its effect is clearly visible in the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | Again, the fine-scale network does not improve much over the coarse one in the error metrics, but differences ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (3 Approach), p. 3 (3 Approach), p. 3 (3 Approach), p. 2 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1 Introduction), p. 1 (1 Introduction), interface p. 2 (3 Approach), p. 3 (3 Approach), p. 3 (3 Approach), p. 2 (1 Introduction), objective p. 4 (3 Approach), p. 4 (3 Approach), p. 5 (3 Approach), p. 2 (3 Approach), p. 3 (3 Approach).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
