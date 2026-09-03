# Structure-from-Motion Revisited

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content_cvpr_2016/html/Schonberger_Structure-From-Motion_Revisited_CVPR_2016_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content_cvpr_2016/papers/Schonberger_Structure-From-Motion_Revisited_CVPR_2016_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2016 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, 3D reconstruction, SLAM, geometry
- Official paper: https://openaccess.thecvf.com/content_cvpr_2016/html/Schonberger_Structure-From-Motion_Revisited_CVPR_2016_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content_cvpr_2016/papers/Schonberger_Structure-From-Motion_Revisited_CVPR_2016_paper.pdf
- Code/Project: https://colmap.github.io/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 While the existing systems have advanced the state of the art tremendously, robustness, accuracy, completeness, and scalability remain the key problems in incremental SfM that prevent its use as a general-purpose method.를 문제로 두고, In this paper, we propose a new SfM algorithm to approach this ultimate goal.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Incremental Structure-from-Motion is a prevalent strategy for 3D reconstruction from unordered image collections.
- **p. 1 / Abstract - extractive body cue:** While incremental reconstruction systems have tremendously advanced in all regards, robustness, accuracy, completeness, and scalability remain the key problems towards building a truly general-purpose pipeline.
- **p. 1 / Abstract - extractive body cue:** We propose a new SfM technique that improves upon the state of the art to make a further step towards this ultimate goal.
- **p. 1 / Abstract - extractive body cue:** The full reconstruction pipeline is released to the public as an open-source implementation.
- **p. 1 / 1. Introduction - extractive body cue:** Structure-from-Motion (SfM) from unordered images has seen tremendous evolution over the years.

## Core Idea

- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we propose a new SfM algorithm to approach this ultimate goal.
- **p. 2 / 2.2. Incremental Reconstruction - extractive body cue:** We propose a novel robust next best image selection method for accurate pose estimation and reliable triangulation in Sec.
- **p. 3 / 2.2. Incremental Reconstruction - extractive body cue:** 4.5, we propose a method to identify and parameterize highly overlapping images for efficient BA of dense collections.
- **p. 2 / 2.2. Incremental Reconstruction - extractive body cue:** Triangulation is a crucial step in SfM, as it increases the stability of the existing model through redundancy [58] and it enables registration of new ...
- **p. 1 / 1. Introduction - extractive body cue:** Inspired by these works, increasingly largescale reconstruction systems have been developed for hundreds of thousands [1] and millions [20, 62, 51, 50] to recently a ...
- **p. 2 / 2.2. Incremental Reconstruction - extractive body cue:** Starting from a metric reconstruction, new images can be registered to the current model by solving the Perspective-n-Point (PnP) problem [18] using feature correspondences to ...
- **p. 2 / 2.2. Incremental Reconstruction - extractive body cue:** Without further refinement, SfM usually drifts quickly to a non-recoverable state.
- **p. 3 / 2.2. Incremental Reconstruction - extractive body cue:** and a loss function ρj to potentially down-weight outliers.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The outputs are pose estimates P = {Pc ∈SE(3) / c = 1...NP } for registered images and the reconstructed scene structure as a set of points X = {Xk ∈R3 / ... | camera/depth stream, pose, map와 language goal | p. 2 (2.2. Incremental Reconstruction), p. 1 (1. Introduction) |
| State/latent | outputs, pose, estimates, registered, images, reconstructed, scene, structure, points, While, existing, systems | robot pose, free-space/semantic map와 local goal | p. 2 (2.2. Incremental Reconstruction), p. 1 (1. Introduction), p. 2 (2.2. Incremental Reconstruction) |
| Output/action | While the existing systems have advanced the state of the art tremendously, robustness, accuracy, completeness, and scalability remain the key problems in incremental SfM that prevent its use as a general-purpose method. | collision-free trajectory 또는 velocity command | p. 1 (1. Introduction), p. 2 (2.2. Incremental Reconstruction), p. 1 (1. Introduction) |
| Objective/outcome | These methods suffer from limited robustness or high computational cost for use in SfM, which we address by proposing a robust and efficient triangulation method in Sec. | goal reach, safety, localization error와 replanning latency | p. 2 (2.2. Incremental Reconstruction), p. 2 (2.2. Incremental Reconstruction), p. 3 (2.2. Incremental Reconstruction) |

## Main Claims and Actual Contribution

- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we propose a new SfM algorithm to approach this ultimate goal.
- **p. 2 / 2.2. Incremental Reconstruction - extractive body cue:** We propose a novel robust next best image selection method for accurate pose estimation and reliable triangulation in Sec.
- **p. 3 / 2.2. Incremental Reconstruction - extractive body cue:** 4.5, we propose a method to identify and parameterize highly overlapping images for efficient BA of dense collections.
- **p. 2 / 2.2. Incremental Reconstruction - extractive body cue:** Triangulation is a crucial step in SfM, as it increases the stability of the existing model through redundancy [58] and it enables registration of new ...
- **p. 1 / 1. Introduction - extractive body cue:** Inspired by these works, increasingly largescale reconstruction systems have been developed for hundreds of thousands [1] and millions [20, 62, 51, 50] to recently a ...
- **p. 8 / 7.82 M - extractive body cue:** For all datasets, we significantly outperform any other method in terms of completeness, especially for the larger models.
- **p. 8 / 7.82 M - extractive body cue:** In addition, we achieve the best pose accuracy for the Quad dataset: DISCO 1.16m, Bundler 1.01m, VisualSFM 0.89m, and Ours 0.85m.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Scores for different number of points (left and right) with different distributions (top and bottom) in the image for L = 3. late ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 8 (7.82 M), p. 8 (7.82 M) |
| Embodiment/environment | An experiment on the Dubrovnik dataset (Fig. | hardware/simulator version and reset protocol | p. 7 (5. Experiments), p. 7 (5. Experiments) |
| Dataset/benchmark | For each dataset, we report the largest reconstructed component. | role, split, size and leakage | p. 7 (5. Experiments), p. 7 (5. Experiments), p. 8 (7.82 M), p. 8 (7.82 M) |
| Metric | After each image registration, we measure the number of registered images shared between the strategies (intersection over union) and the reconstruction error as the median distance to the ground-truth camera locations. | definition, denominator, direction and uncertainty | p. 7 (5. Experiments), p. 7 (5. Experiments), p. 8 (7.82 M) |
| Baseline/ablation | We run experiments on a large variety of datasets to evaluate both the proposed components and the overall system compared to state-of-the-art incremental (Bundler [53], VisualSFM [62]) and global SfM systems (DISCO ... | fair input/data/compute/action matching | p. 7 (5. Experiments), p. 8 (7.82 M), p. 8 (7.82 M) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 6. Conclusion - extractive body cue:** The proposed components of the algorithm improve the state of the art in terms of completeness, robustness, accuracy, and efficiency.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Scores for different number of points (left and right) with different distributions (top and bottom) in the image for L = 3. late ...
- **p. 7 / 5. Experiments - extractive body cue:** Robust and Efficient Triangulation.
- **p. 8 / 7.82 M - extractive body cue:** The reconstruction quality is comparable for all choices of V > 0.3 and increasingly degrades for a smaller V .

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 While the existing systems have advanced the state of the art tremendously, robustness, accuracy, completeness, and scalability remain the key problems in incremental SfM that prevent its use as a general-purpose method.를 문제로 두고, In this paper, we propose a new SfM algorithm to approach this ultimate goal.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (2.2. Incremental Reconstruction), p. 2 (2.2. Incremental Reconstruction), p. 3 (2.2. Incremental Reconstruction), p. 3 (2.2. Incremental Reconstruction), p. 8 (7.82 M) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
