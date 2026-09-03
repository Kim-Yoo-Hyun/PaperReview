# Efficient Continuous Group Convolutions for Local SE(3) Equivariance in 3D Point Clouds

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/.
> PDF retrieval source: https://openreview.net/attachment?id=c6RR0bqNVI&name=pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / 3DV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: equivariant, point cloud, 3D Vision
- Official paper: https://3dvconf.github.io/2025/accepted-papers/
- Full-text retrieval: https://openreview.net/attachment?id=c6RR0bqNVI&name=pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 The relative orientations of different objects in the scene cannot be captured by global equivariance as obtained by existing architectures or by data augmentation techniques.를 문제로 두고, In this paper, we propose using a finite subset F(x) ⊂ SE(3), referred to as a frame, to solve the group equivariant integral, which allows for exact equivariance (as opposed to approaches ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Extending the translation equivariance property of convolutional neural networks to larger symmetry groups has been shown to reduce sample complexity and enable more discriminative feature ...
- **p. 1 / Abstract - extractive body cue:** Further, exploiting additional symmetries facilitates greater weight sharing than standard convolutions, leading to an enhanced network expressivity without an increase in parameter count.
- **p. 1 / Abstract - extractive body cue:** However, extending the equivariant properties of a convolution layer comes at a computational cost.
- **p. 1 / Abstract - extractive body cue:** In particular, for 3D data, expanding equivariance to the SE(3) group (rotation and translation) results in a 6D convolution operation, which is not tractable for ...
- **p. 1 / Abstract - extractive body cue:** While efforts have been made to develop efficient SE(3) equivariant networks, existing approaches rely on discretization or only introduce global rotation equivariance.
- **p. 2 / 1. Introduction - extractive body cue:** The relative orientations of different objects in the scene cannot be captured by global equivariance as obtained by existing architectures or by data augmentation techniques.
- **p. 1 / 1. Introduction - extractive body cue:** Approaches learning directly from 3D data often take inspiration from the success in 2D vision and address two of the main challenges in such data ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we propose using a finite subset F(x) ⊂ SE(3), referred to as a frame, to solve the group equivariant integral, which allows ...
- **p. 3 / 3.1. Group equivariant convolution - extractive body cue:** Further, considering Y = G/H as quotient space with H = {g ∈G/gy0 = y0} as the stabilizer subgroup StabG(y0), which consists of group elements ...
- **p. 4 / 3.2. Efficient group convolution - extractive body cue:** To achieve exact equivariance with tractable computational load, we propose a carefully constructed grid F(xj) ⊂SE(3) specific to each point xj ∈R3.
- **p. 4 / 3.1. Group equivariant convolution - extractive body cue:** equivariance, the feature maps need to be lifted to the group itself Y = G since then the stabilizer subgroup only consists of the trivial ...
- **p. 5 / 3.2. Efficient group convolution - extractive body cue:** Therefore, we propose to perform a stochastic approximation of Eq.
- **p. 3 / 3.1. Group equivariant convolution - extractive body cue:** A more formal definition of a convolution layer is then given as a learnable kernel operator Φ : X →Y that transforms feature maps f ...
- **p. 3 / 3.1. Group equivariant convolution - extractive body cue:** We say that an operator Φ is equivariant to a specific Group G if it commutes with group representations on the input and output feature ...
- **p. 5 / 3.2. Efficient group convolution - extractive body cue:** (7) during training by only sampling a subset of the elements of F(x) for input and output domains of the feature maps.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | (Note that the definition given is cross-correlation instead of convolution since this aligns better with template-matching.) It is well known that convolution layers are translation equivariant due to the shifted kernel, i.e., ... | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3.1. Group equivariant convolution), p. 3 (3.1. Group equivariant convolution) |
| State/latent | Note, definition, given, cross-correlation, instead, convolution, since, aligns, better, template-matching, well, known | geometry, map, object/relationship state | p. 3 (3.1. Group equivariant convolution), p. 3 (3.1. Group equivariant convolution), p. 5 (3.2. Efficient group convolution) |
| Output/action | We say that an operator Φ is equivariant to a specific Group G if it commutes with group representations on the input and output feature maps, meaning ∀g ∈G : ρY(g) ◦Φ ... | point map, pose, scene graph, affordance 또는 query result | p. 3 (3.1. Group equivariant convolution), p. 5 (3.2. Efficient group convolution), p. 1 (1. Introduction) |
| Objective/outcome | One solution is to use ∥x -y∥as input to the kernel at the cost of losing the capacity to capture directional features. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (3.1. Group equivariant convolution), p. 3 (3.1. Group equivariant convolution), p. 4 (3.2. Efficient group convolution) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we propose using a finite subset F(x) ⊂ SE(3), referred to as a frame, to solve the group equivariant integral, which allows ...
- **p. 3 / 3.1. Group equivariant convolution - extractive body cue:** Further, considering Y = G/H as quotient space with H = {g ∈G/gy0 = y0} as the stabilizer subgroup StabG(y0), which consists of group elements ...
- **p. 4 / 3.2. Efficient group convolution - extractive body cue:** To achieve exact equivariance with tractable computational load, we propose a carefully constructed grid F(xj) ⊂SE(3) specific to each point xj ∈R3.
- **p. 4 / 3.1. Group equivariant convolution - extractive body cue:** equivariance, the feature maps need to be lifted to the group itself Y = G since then the stabilizer subgroup only consists of the trivial ...
- **p. 5 / 3.2. Efficient group convolution - extractive body cue:** Therefore, we propose to perform a stochastic approximation of Eq.
- **p. 6 / 4.2. Shape classification - extractive body cue:** When we look at the SO(3) / SO(3) setup, all three methods achieve good performance; MC and Ours are able to outperform STD, while Ours ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative results. Global equivariant methods such as VN, or FA struggle with out-of-distribution models. Our method, on the other hand, achieves almost perfect ...
- **p. 6 / 4.2. Shape classification - extractive body cue:** MC, although it can also achieve competitive performance, for most of the cases, the drop in performance is significant compared to the I / I ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (4.2. Shape classification), p. 7 (Figure/Table caption) |
| Embodiment/environment | We test our method on ScanNet [14], a dataset composed of several indoor 3D scene scans, to show its applicability to real-world scenarios. | hardware/simulator version and reset protocol | p. 7 (4.3. Semantic segmentation), p. 5 (4.2. Shape classification) |
| Dataset/benchmark | 4.3.2 Scene understanding Scenes consist of multiple parts or objects with arbitrary orientations, making local equivariance essential for generalizing to unseen configurations. | role, split, size and leakage | p. 7 (4.3. Semantic segmentation), p. 5 (4.2. Shape classification), p. 7 (4.3. Semantic segmentation), p. 6 (4.3. Semantic segmentation) |
| Metric | Our model only takes as input point coordinates, and performance is measured with overall accuracy. | definition, denominator, direction and uncertainty | p. 5 (4.2. Shape classification), p. 6 (4.2. Shape classification), p. 6 (4.2. Shape classification) |
| Baseline/ablation | When comparing to current state-of-the-art local equivariant methods, we can see that while they also outperform global equivariant methods by a large margin, our method gives superior results, with E2PN [48] reaching ... | fair input/data/compute/action matching | p. 7 (4.3. Semantic segmentation), p. 5 (4.2. Shape classification), p. 6 (4.2. Shape classification) |

## Explicit Limitations and Failure Boundary

- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative results. Global equivariant methods such as VN, or FA struggle with out-of-distribution models. Our method, on the other hand, achieves almost perfect ...
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 4. Additional Qualitative results. Global equivariant methods such as VN, or FA struggle with out-of-distribution models, especially up-side down models. Our method, on the ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 5. Additional Qualitative results. Global equivariant methods such as VN, or FA struggle with out-of-distribution models. Our method, on the other hand, achieves almost ...
- **p. 6 / 4.2. Shape classification - extractive body cue:** When compared to global equivariant networks, our method falls behind in the I / SO(3) setup and achieves similar performance on the z / SO(3) ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. While global equivariant designs ensure robustness to whole-scene rotations, they fail with randomly rotated scene parts or elements. In contrast, local equivariant operations ...
- **p. 8 / 5. Conclusions - extractive body cue:** Moreover, by restricting the receptive field of our convolution, our operation becomes local equivariant, allowing us to be robust to local transformations.
- **p. 16 / Figure/Table caption - extractive body cue:** Table 12. Robustness w.r.t. noise variations. Noise train test mAcc mIoU 0.005 0.005

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 The relative orientations of different objects in the scene cannot be captured by global equivariance as obtained by existing architectures or by data augmentation techniques.를 문제로 두고, In this paper, we propose using a finite subset F(x) ⊂ SE(3), referred to as a frame, to solve the group equivariant integral, which allows for exact equivariance (as opposed to approaches ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 4 (3.1. Group equivariant convolution), p. 3 (3.1. Group equivariant convolution), p. 3 (3.1. Group equivariant convolution) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
