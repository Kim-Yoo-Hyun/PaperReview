# Problem - Tensor Field Networks: Rotation- and Translation-Equivariant Neural Networks for 3D Point Clouds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1802.08219; PDF retrieval source: https://arxiv.org/pdf/1802.08219. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 1 (Abstract), p. 1 (Abstract)): We introduce tensor field neural networks, which are locally equivariant to 3D rotations, translations, and permutations of points at every layer.

## PDF Body Digest

- **p. 1 / Abstract - extractive PDF cue:** We introduce tensor field neural networks, which are locally equivariant to 3D rotations, translations, and permutations of points at every layer.
- **p. 1 / Abstract - extractive PDF cue:** 3D rotation equivariance removes the need for data augmentation to identify features in arbitrary orientations.
- **p. 1 / Abstract - extractive PDF cue:** Our network uses filters built from spherical harmonics; due to the mathematical consequences of this filter choice, each layer accepts as input (and guarantees as ...
- **p. 1 / Abstract - extractive PDF cue:** We demonstrate the capabilities of tensor field networks with tasks in geometry, physics, and chemistry.
- **p. 1 / Abstract - extractive PDF cue:** 1 Motivation Convolutional neural networks are translation-equivariant, which means that features can be identified anywhere in a given input.
- **p. 1 / Abstract - extractive PDF cue:** In this paper, we present a family of networks that enjoy richer equivariance: the symmetries of 3D Euclidean space.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | We introduce tensor field neural networks, which are locally equivariant to 3D rotations, translations, and permutations of points at every layer. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | Our network uses filters built from spherical harmonics; due to the mathematical consequences of this filter choice, each layer accepts as input ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF |
| State / latent | network, uses, filters, built, spherical, harmonics, mathematical, consequences, filter, choice | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Motivation, Convolutional, neural, networks, translation-equivariant, means, features, identified | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: network, uses, filters, built, spherical, harmonics, mathematical, consequences, filter, choice | p. 1 (Abstract), p. 2 (Abstract), p. 1 (Abstract) |
| Decision / output variable | geometry/map/query r; body terms: present, family, networks, enjoy, richer, equivariance, symmetries, Euclidean | p. 1 (Abstract), p. 1 (Abstract) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: progress, arXiv | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (Abstract) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 9 (Figure/Table caption), p. 7 (Figure/Table caption), p. 1 (Abstract) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / Abstract - extractive PDF cue:** 3D rotation equivariance removes the need for data augmentation to identify features in arbitrary orientations.

## What the Paper Changes

PDF contribution framing (p. 1 (Abstract), p. 1 (Abstract)): In this paper, we present a family of networks that enjoy richer equivariance: the symmetries of 3D Euclidean space.

- **p. 1 / Abstract - extractive PDF cue:** We introduce tensor field neural networks, which are locally equivariant to 3D rotations, translations, and permutations of points at every layer.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | Any network that relies solely upon distances (such as SchNet [2]) or angles between points (such as ANI-1 ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 1 (Abstract), p. 2 (Abstract), p. 1 (Abstract), p. 2 (Abstract). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 1 (Abstract), p. 1 (Abstract), interface p. 1 (Abstract), p. 2 (Abstract), p. 1 (Abstract), p. 2 (Abstract), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
