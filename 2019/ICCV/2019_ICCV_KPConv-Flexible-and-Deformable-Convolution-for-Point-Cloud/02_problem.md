# Problem - KPConv: Flexible and Deformable Convolution for Point Clouds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1904.08889; PDF retrieval source: https://arxiv.org/pdf/1904.08889. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction)): Input points with a constant scalar feature (in grey) are convolved through a KPConv that is defined by a set of kernel points (in black) with filter weights on each ...

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** We present Kernel Point Convolution1 (KPConv), a new design of point convolution, i.e. that operates on point clouds without any intermediate representation.
- **p. 1 / Abstract - extractive PDF cue:** The convolution weights of KPConv are located in Euclidean space by kernel points, and applied to the input points close to them.
- **p. 1 / Abstract - extractive PDF cue:** Its capacity to use any number of kernel points gives KPConv more flexibility than fixed grid convolutions.
- **p. 1 / Abstract - extractive PDF cue:** Furthermore, these locations are continuous in space and can be learned by the network.
- **p. 1 / Abstract - extractive PDF cue:** Therefore, KPConv can be extended to deformable convolutions that learn to adapt kernel points to local geometry.
- **p. 1 / 1. Introduction - extractive PDF cue:** Input points with a constant scalar feature (in grey) are convolved through a KPConv that is defined by a set of kernel points (in black) ...
- **p. 2 / 1. Introduction - extractive PDF cue:** KPConv also consists of a set of local 3D filters, but overcomes previous point convolution limitations as shown in related work.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Input points with a constant scalar feature (in grey) are convolved through a KPConv that is defined by a set of kernel ... | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Input points with a constant scalar feature (in grey) are convolved through a KPConv that is defined by a set of kernel ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | Input, points, constant, scalar, feature, grey, convolved, through, KPConv, defined | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | robustness, convolution, varying, densities, ensured, combination, radius, neighborhoods | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: Input, points, constant, scalar, feature, grey, convolved, through, KPConv, defined | p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Decision / output variable | geometry/map/query r; body terms: Furthermore, deformable, version, convolution, consists, learning, local, shifts | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: not recovered | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | 본문 anchor 없음 |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 14 (Figure/Table caption), p. 6 (Figure/Table caption), p. 6 (4.2. 3D Scene Segmentation) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive PDF cue:** KPConv also consists of a set of local 3D filters, but overcomes previous point convolution limitations as shown in related work.
- **p. 2 / 1. Introduction - extractive PDF cue:** Deformable KPConv thrives on more difficult tasks, like large segmentation datasets offering many object instances and greater diversity.

## What the Paper Changes

PDF contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 5 (3.4. Kernel Point Network Architectures), p. 5 (3.4. Kernel Point Network Architectures)): Furthermore, we propose a deformable version of our convolution [7], which consists of learning local shifts applied to the kernel points (see Figure 3).

- **p. 2 / 1. Introduction - extractive PDF cue:** KPConv also consists of a set of local 3D filters, but overcomes previous point convolution limitations as shown in related work.
- **p. 1 / 1. Introduction - extractive PDF cue:** Various approaches have been proposed to handle such data, and can be grouped into different categories that we will develop in the related work section.
- **p. 5 / 3.4. Kernel Point Network Architectures - extractive PDF cue:** Combining analogy with successful image networks and empirical studies, we designed two network architectures for the classification and the segmentation tasks.
- **p. 5 / 3.4. Kernel Point Network Architectures - extractive PDF cue:** Our convolutional blocks are designed like bottleneck ResNet blocks [12] with a KPConv replacing the image convolution, batch normalization and leaky ReLu activation.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | We use Scannet dataset (same parameters as before) and use the official validation set, because the test set ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 1 (1. Introduction), p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
