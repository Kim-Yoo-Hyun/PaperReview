# Affine-Equivariant Kernel Space Encoding for NeRF Editing

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=fAj3MJghc0.
> PDF retrieval source: https://openreview.net/pdf/048e4b5756022f2faa8898f0f2d379b85079ab58.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2026 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: NeRF, equivariant, 3D Vision
- Official paper: https://openreview.net/forum?id=fAj3MJghc0
- Full-text retrieval: https://openreview.net/pdf/048e4b5756022f2faa8898f0f2d379b85079ab58.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This limitation restricts their applicability in interactive and physically grounded settings.를 문제로 두고, In this work, we introduce Affine-Equivariant Kernel Space Encoding (EKS), a novel positional encoding mechanism for NeRFs.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Neural scene representations achieve high-fidelity rendering by encoding 3D scenes as continuous functions, but their latent spaces are typically implicit and globally entangled, making localized ...
- **p. 1 / Abstract - extractive body cue:** While several works introduce explicit control structures or point-based latent representations to improve editability, these approaches often suffer from limited locality, sensitivity to deformations, or ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we introduce Affine-Equivariant Kernel Space Encoding (EKS), a spatial encoding for neural radiance fields that provides localized, deformation-aware feature representations.
- **p. 1 / Abstract - extractive body cue:** Instead of querying latent features directly at discrete points or grid vertices, our encoding aggregates features through a field of anisotropic Gaussian kernels, each defining ...
- **p. 1 / Abstract - extractive body cue:** This kernel-based formulation enables stable feature interpolation 1Poznan University of Technology.
- **p. 2 / 1. Introduction - extractive body cue:** This limitation restricts their applicability in interactive and physically grounded settings.
- **p. 2 / 1. Introduction - extractive body cue:** Motivated by these observations, we address a fundamental limitation in NeRF editing task: the absence of a transformation-aware space encoding.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In this work, we introduce Affine-Equivariant Kernel Space Encoding (EKS), a novel positional encoding mechanism for NeRFs.
- **p. 6 / 4. Proposed Method - extractive body cue:** Interpolation between these modified Gaussians then enables the system to synthesize novel views of the edited scene.
- **p. 4 / 4. Proposed Method - extractive body cue:** Our method, called EKS, integrates affine-equvariant transformation properties of Gaussian kernels and a neural network-based rendering procedure into a single system.
- **p. 5 / 4. Proposed Method - extractive body cue:** Our method preserves relative feature structure under spatial transformations and yields visibly improved results with no holes and distortions. following section).
- **p. 5 / 4. Proposed Method - extractive body cue:** To address this limitation, we introduce a Hash Grid Feature Distillation mechanism, which decouples the feature representation from the underlying grid vertices and transfers it ...
- **p. 4 / 4. Proposed Method - extractive body cue:** Specifically, we use a set of Gaussian kernels, enhanced with a trainable latent feature vector v ∈Rn.
- **p. 4 / 4. Proposed Method - extractive body cue:** We use a NeRF-based neural network F to predict colour and opacity from the nearest Gaussian features.
- **p. 6 / 4. Proposed Method - extractive body cue:** As a result, the latent features remain coherent after deformation, ensuring that modifications produce smooth, stable, and physically consistent updates in the rendered scene without ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The model, alongside the standard NeRF input, takes a set of trainable Gaussians G and outputs colour c and density σ at any query point, enabling neural rendering conditioned on nearby Gaussian ... | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (4. Proposed Method), p. 4 (3. Preliminary) |
| State/latent | model, alongside, standard, NeRF, input, takes, trainable, Gaussians, outputs, colour, density, query | geometry, map, object/relationship state | p. 4 (4. Proposed Method), p. 4 (3. Preliminary), p. 3 (3. Preliminary) |
| Output/action | The edited Gaussians are passed through the same rendering pipeline to generate the final image, with the view-direction input to F adjusted by the inverse rotation of the modified Gaussians. | point map, pose, scene graph, affordance 또는 query result | p. 4 (3. Preliminary), p. 3 (3. Preliminary), p. 5 (4. Proposed Method) |
| Objective/outcome | The Gaussian features v(x) are sampled from the hash-grid encoding at the kernel centres, formally described as: v (x) = k X i=1 wi(x, G) · Henc(µi; Φ), (8) At inference, we ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (4. Proposed Method), p. 6 (4. Proposed Method), p. 5 (4. Proposed Method) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In this work, we introduce Affine-Equivariant Kernel Space Encoding (EKS), a novel positional encoding mechanism for NeRFs.
- **p. 6 / 4. Proposed Method - extractive body cue:** Interpolation between these modified Gaussians then enables the system to synthesize novel views of the edited scene.
- **p. 4 / 4. Proposed Method - extractive body cue:** Our method, called EKS, integrates affine-equvariant transformation properties of Gaussian kernels and a neural network-based rendering procedure into a single system.
- **p. 5 / 4. Proposed Method - extractive body cue:** Our method preserves relative feature structure under spatial transformations and yields visibly improved results with no holes and distortions. following section).
- **p. 5 / 4. Proposed Method - extractive body cue:** To address this limitation, we introduce a Hash Grid Feature Distillation mechanism, which decouples the feature representation from the underlying grid vertices and transfers it ...
- **p. 6 / 5. Experiments - extractive body cue:** These baselines are selected to demonstrate that EKS not only achieves reconstruction quality comparable to or exceeding SOTA methods, while enabling editing with significantly fewer ...
- **p. 6 / 5. Experiments - extractive body cue:** For static scene reconstruction, EKS achieves quality comparable to state-of-the-art editable methods, and in some cases provides the best results among methods that support editing.
- **p. 7 / 5. Experiments - extractive body cue:** Quantitative comparisons (PSNR) on a (Chen et al., 2023) benchmark showing that EKS achieves best results in editing task.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (5. Experiments), p. 6 (5. Experiments) |
| Embodiment/environment | Additionally to synthetic data we trained our NeRF model trained on the Mip-NeRF 360 dataset (Barron et al., 2022), comprising five outdoor and four indoor real-world 360°scenes. | hardware/simulator version and reset protocol | p. 6 (5. Experiments), p. 7 (5. Experiments) |
| Dataset/benchmark | Example edits on real-world scenes. | role, split, size and leakage | p. 6 (5. Experiments), p. 7 (5. Experiments), p. 6 (5. Experiments), p. 7 (5. Experiments) |
| Metric | This demonstrates that our approach preserves rendering quality while enabling scene edits. | definition, denominator, direction and uncertainty | p. 6 (5. Experiments), p. 6 (5. Experiments), p. 7 (5. Experiments) |
| Baseline/ablation | We design our experiments to demonstrate that EKS maintains the reconstruction quality of state-of-the-art (SOTA) methods while enabling complex object modifications. | fair input/data/compute/action matching | p. 6 (5. Experiments), p. 6 (5. Experiments), p. 7 (5. Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Physical simulations. From left to right: (1) Rigid body simulation of falling leaves. (2) Soft body simulation of the Lego dozer being squished. ...
- **p. 8 / 6. Conclusions - extractive body cue:** By representing latent features with anisotropic Gaussian kernels and aggregating them using Mahalanobis-distance-based neighbourhoods, our method preserves local feature structure under affine transformations, addressing a ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. Evolution of two physical simulations. From left to right: (1) A rubber duck falling onto a pillow and deforming it. (2) A pirate ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5. KNN Comparisons. Comparison of neighbourhood changes under deformation using Euclidean distance KNN (top) versus our proposed Mahalanobis distance KNN (bottom). Mov- ing points ...
- **p. 6 / 5. Experiments - extractive body cue:** From left to right: (1) Physics-based simulation, showing an object falling onto a tilted table and bouncing off.
- **p. 7 / 5. Experiments - extractive body cue:** Whether simulating leaves falling from a plant, squashing a soft object, or draping cloth over complex geometry, our method maintains high rendering fidelity while enabling ...
- **p. 8 / 5. Experiments - extractive body cue:** Removing view-direction restoration leads to the largest performance drop, as the model fails to recover correct view-dependent appearance after deformation.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 This limitation restricts their applicability in interactive and physically grounded settings.를 문제로 두고, In this work, we introduce Affine-Equivariant Kernel Space Encoding (EKS), a novel positional encoding mechanism for NeRFs.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Preliminary), p. 4 (4. Proposed Method), p. 4 (4. Proposed Method), p. 5 (4. Proposed Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
