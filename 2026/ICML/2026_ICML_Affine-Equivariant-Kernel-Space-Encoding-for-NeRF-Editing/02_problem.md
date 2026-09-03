# Problem - Affine-Equivariant Kernel Space Encoding for NeRF Editing

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=fAj3MJghc0; PDF retrieval source: https://openreview.net/pdf/048e4b5756022f2faa8898f0f2d379b85079ab58.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Preliminary)): This limitation restricts their applicability in interactive and physically grounded settings.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Neural scene representations achieve high-fidelity rendering by encoding 3D scenes as continuous functions, but their latent spaces are typically implicit and globally entangled, making localized ...
- **p. 1 / Abstract - extractive body cue:** While several works introduce explicit control structures or point-based latent representations to improve editability, these approaches often suffer from limited locality, sensitivity to deformations, or ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce Affine-Equivariant Kernel Space Encoding (EKS), a spatial encoding for neural radiance fields that provides localized, deformation-aware feature representations.
- **p. 1 / Abstract - extractive body cue:** Instead of querying latent features directly at discrete points or grid vertices, our encoding aggregates features through a field of anisotropic Gaussian kernels, each defining ...
- **p. 1 / Abstract - extractive body cue:** This kernel-based formulation enables stable feature interpolation 1Poznan University of Technology.
- **p. 2 / 1. Introduction - extractive body cue:** This limitation restricts their applicability in interactive and physically grounded settings.
- **p. 2 / 1. Introduction - extractive body cue:** Motivated by these observations, we address a fundamental limitation in NeRF editing task: the absence of a transformation-aware space encoding.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | This limitation restricts their applicability in interactive and physically grounded settings. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | The model, alongside the standard NeRF input, takes a set of trainable Gaussians G and outputs colour c and density σ at ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | model, alongside, standard, NeRF, input, takes, trainable, Gaussians, outputs, colour | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | query, point, output, feature, vector, obtained, concatenating, trilinearly | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: model, alongside, standard, NeRF, input, takes, trainable, Gaussians, outputs, colour | p. 4 (4. Proposed Method), p. 4 (3. Preliminary), p. 3 (3. Preliminary) |
| Decision / output variable | geometry/map/query r; body terms: introduce, Affine-Equivariant, Kernel, Space, Encoding, EKS, novel, positional | p. 2 (1. Introduction), p. 6 (4. Proposed Method), p. 4 (4. Proposed Method) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Gaussian, features, sampled, hash-grid, encoding, kernel, centres, formally | p. 5 (4. Proposed Method), p. 6 (4. Proposed Method), p. 6 (4. Proposed Method) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 6 (4. Proposed Method), p. 5 (4. Proposed Method), p. 6 (4. Proposed Method) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 6 (5. Experiments), p. 6 (5. Experiments), p. 7 (5. Experiments) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** Motivated by these observations, we address a fundamental limitation in NeRF editing task: the absence of a transformation-aware space encoding.
- **p. 3 / 3. Preliminary - extractive body cue:** Hash Grid Encoding Many NeRF variants adopt the Hash Grid Encoding (M¨uller et al., 2022), to improve scalability and spatial precision which captures high-frequency scene ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 6 (4. Proposed Method), p. 4 (4. Proposed Method), p. 5 (4. Proposed Method), p. 5 (4. Proposed Method)): In this work, we introduce Affine-Equivariant Kernel Space Encoding (EKS), a novel positional encoding mechanism for NeRFs.

- **p. 6 / 4. Proposed Method - extractive body cue:** Interpolation between these modified Gaussians then enables the system to synthesize novel views of the edited scene.
- **p. 4 / 4. Proposed Method - extractive body cue:** Our method, called EKS, integrates affine-equvariant transformation properties of Gaussian kernels and a neural network-based rendering procedure into a single system.
- **p. 5 / 4. Proposed Method - extractive body cue:** Our method preserves relative feature structure under spatial transformations and yields visibly improved results with no holes and distortions. following section).
- **p. 5 / 4. Proposed Method - extractive body cue:** To address this limitation, we introduce a Hash Grid Feature Distillation mechanism, which decouples the feature representation from the underlying grid vertices and transfers it ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 2 | Figure 2. Physical simulations. From left to right: (1) Rigid body simulation of falling leaves. (2) Soft body ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | By representing latent features with anisotropic Gaussian kernels and aggregating them using Mahalanobis-distance-based neighbourhoods, our method preserves local ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | Figure 3. Evolution of two physical simulations. From left to right: (1) A rubber duck falling onto a ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | Figure 5. KNN Comparisons. Comparison of neighbourhood changes under deformation using Euclidean distance KNN (top) versus our proposed ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (4. Proposed Method), p. 4 (3. Preliminary), p. 3 (3. Preliminary), p. 5 (4. Proposed Method). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Preliminary), interface p. 4 (4. Proposed Method), p. 4 (3. Preliminary), p. 3 (3. Preliminary), p. 5 (4. Proposed Method), objective p. 5 (4. Proposed Method), p. 6 (4. Proposed Method), p. 6 (4. Proposed Method).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
