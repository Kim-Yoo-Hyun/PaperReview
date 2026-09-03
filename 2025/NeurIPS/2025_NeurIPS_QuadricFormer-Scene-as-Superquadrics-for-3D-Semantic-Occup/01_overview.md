# QuadricFormer: Scene as Superquadrics for 3D Semantic Occupancy Prediction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=eZNdkwJYbN.
> PDF retrieval source: https://arxiv.org/pdf/2506.10977. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: sensor fusion, LiDAR, semantic, alignment, 3D Vision
- Official paper: https://openreview.net/forum?id=eZNdkwJYbN
- Full-text retrieval: https://arxiv.org/pdf/2506.10977
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Despite promising applications, 3D semantic occupancy prediction faces efficiency challenges due to its dense 3D predictions [4, 31].를 문제로 두고, 3 Proposed Approach In this section, we present our method based on the superquadric representation for efficient 3D semantic occupancy prediction.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D occupancy prediction is crucial for robust autonomous driving systems as it enables comprehensive perception of environmental structures and semantics.
- **p. 1 / Abstract - extractive body cue:** Most existing methods employ dense voxel-based scene representations, ignoring the sparsity of driving scenes and resulting in inefficiency.
- **p. 1 / Abstract - extractive body cue:** Recent works explore object-centric representations based on sparse Gaussians, but their ellipsoidal shape prior limits the modeling of diverse structures.
- **p. 1 / Abstract - extractive body cue:** In real-world driving scenes, objects exhibit rich geometries (e.g., cuboids, cylinders, and irregular shapes), necessitating excessive ellipsoidal Gaussians densely packed for accurate modeling, which leads ...
- **p. 1 / Abstract - extractive body cue:** To address this, we propose to use geometrically expressive superquadrics as scene primitives, enabling efficient representation of complex structures with fewer primitives through their inherent ...
- **p. 2 / 1 Introduction - extractive body cue:** Despite promising applications, 3D semantic occupancy prediction faces efficiency challenges due to its dense 3D predictions [4, 31].
- **p. 2 / 1 Introduction - extractive body cue:** Real-world driving scenarios contain objects with rich structural variations, which cannot be accurately represented by a few ellipsoidal Gaussian.

## Core Idea

- **p. 3 / 6 Superquadrics - extractive body cue:** 3 Proposed Approach In this section, we present our method based on the superquadric representation for efficient 3D semantic occupancy prediction.
- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we propose an efficient and expressive object-centric 3D representation using superquadrics [1] as scene primitives.
- **p. 2 / 1 Introduction - extractive body cue:** Building on this representation, we introduce QuadricFormer, a superquadric-based framework for efficient 3D semantic occupancy prediction.
- **p. 1 / Abstract - extractive body cue:** To address this, we propose to use geometrically expressive superquadrics as scene primitives, enabling efficient representation of complex structures with fewer primitives through their inherent ...
- **p. 1 / 12800 Gaussians - extractive body cue:** 20.02 mIoU 1600 Superquadrics 20.12 mIoU GaussianFormer QuadricFormer Figure 1: Considering the ellipsoidal shape prior of Gaussians, we propose leveraging expressive superquadrics to build an ...
- **p. 5 / 6 Superquadrics - extractive body cue:** Superquadrics Image Input Image Features 3D Occupancy Refined Superquadrics Figure 3: Overall Framework of QuadricFormer.We use several quadric-encoder blocks to update superquadrics, and employ a ...
- **p. 6 / 6 Superquadrics - extractive body cue:** (11) We then use 3D sparse convolution Econv for superquadric feature self-encoding and deformable attention Eattn for interaction between superquadric and image features: FQ = ...
- **p. 6 / 6 Superquadrics - extractive body cue:** To address this, we introduce a pruning-splitting module after initial training.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Furthermore, surface-based methods rely on the explicit structure from point cloud inputs, whereas visual inputs introduce structural uncertainty, making deterministic modeling unstable. | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (6 Superquadrics), p. 3 (6 Superquadrics) |
| State/latent | Furthermore, surface-based, methods, rely, explicit, structure, point, cloud, inputs, whereas, visual, introduce | geometry, map, object/relationship state | p. 5 (6 Superquadrics), p. 3 (6 Superquadrics), p. 4 (6 Superquadrics) |
| Output/action | Differently, we present the first superquadric-based framework for holistic scene reconstruction directly from multi-view images, delivering state-of-the-art performance with superior efficiency. | point map, pose, scene graph, affordance 또는 query result | p. 3 (6 Superquadrics), p. 4 (6 Superquadrics), p. 5 (6 Superquadrics) |
| Objective/outcome | (14) For optimization, we adopt the cross entropy loss and the lovaszsoftmax [2] loss for training. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 6 (6 Superquadrics), p. 5 (6 Superquadrics), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 3 / 6 Superquadrics - extractive body cue:** 3 Proposed Approach In this section, we present our method based on the superquadric representation for efficient 3D semantic occupancy prediction.
- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we propose an efficient and expressive object-centric 3D representation using superquadrics [1] as scene primitives.
- **p. 2 / 1 Introduction - extractive body cue:** Building on this representation, we introduce QuadricFormer, a superquadric-based framework for efficient 3D semantic occupancy prediction.
- **p. 1 / Abstract - extractive body cue:** To address this, we propose to use geometrically expressive superquadrics as scene primitives, enabling efficient representation of complex structures with fewer primitives through their inherent ...
- **p. 1 / 12800 Gaussians - extractive body cue:** 20.02 mIoU 1600 Superquadrics 20.12 mIoU GaussianFormer QuadricFormer Figure 1: Considering the ellipsoidal shape prior of Gaussians, we propose leveraging expressive superquadrics to build an ...
- **p. 9 / 4 Experiments - extractive body cue:** The results demonstrate that increasing the crop & split number consistently improves performance.
- **p. 8 / 4 Experiments - extractive body cue:** Compared to other methods, our approach achieves state-of-the-art performance.
- **p. 8 / 4 Experiments - extractive body cue:** Our model is able to predict high-fidelity shapes and achieves comprehensive occupancy results. numbers of Superquarics are set to 1600 in our main results for ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (4 Experiments), p. 8 (4 Experiments) |
| Embodiment/environment | The dataset is officially split into 700 sequences for training, 150 for validation, and 150 for testing. | hardware/simulator version and reset protocol | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Dataset/benchmark | Such diversity enables superquadrics to flexibly model complex object geometries in 3D scenes. n oitate g e v e d a m n a m niarret kla w e dis talf re ... | role, split, size and leakage | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 11 (B Additional Experiments), p. 8 (4 Experiments) |
| Metric | Figure 5: Qualitative comparisons. QuadricFormer predicts more flexible and adaptive shapes. Effect of the pruning-splitting module. We conduct ablation studies on the effect of the pruning- splitting module, as shown in Table ... | definition, denominator, direction and uncertainty | p. 9 (Figure/Table caption), p. 7 (4 Experiments), p. 8 (4 Experiments) |
| Baseline/ablation | Compared to other methods, our approach achieves state-of-the-art performance. | fair input/data/compute/action matching | p. 8 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 9 / 5 Conclusion - extractive body cue:** With random initialization, QuadricFormer cannot fully learn accurate superquadric positions, leaving some superquadrics in empty regions and reducing representation efficiency.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Despite promising applications, 3D semantic occupancy prediction faces efficiency challenges due to its dense 3D predictions [4, 31].를 문제로 두고, 3 Proposed Approach In this section, we present our method based on the superquadric representation for efficient 3D semantic occupancy prediction.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 5 (6 Superquadrics), p. 6 (6 Superquadrics), p. 6 (6 Superquadrics), p. 1 (Abstract) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
