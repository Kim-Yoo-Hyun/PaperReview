# SG-NeRF: Neural Surface Reconstruction with Scene Graph Optimization

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/8870_ECCV_2024_paper.php.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/08870.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: NeRF, 3D reconstruction, 3D Vision
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/8870_ECCV_2024_paper.php
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/08870.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Outlier images can happen when repetitive patterns or textureless regions are present, resulting in SfM failures.를 문제로 두고, In this paper, we propose a novel framework that jointly optimizes the neural radiance field with a scene graph to alleviate the influence of outliers.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** 3D mapping and reconstruction from multi-view images is crucial for a wide range of applications, such as virtual and augmented reality.
- **p. 1 / 1 Introduction - extractive body cue:** Given a set of unorganized images captured around an object, most pipelines proceed in two stages for obtaining the reconstruction.
- **p. 1 / 1 Introduction - extractive body cue:** 2 This work was done during the author's internship at Chohotech Co. ltd..
- **p. 2 / 1 Introduction - extractive body cue:** Dong et al. … NeuS BARF* Neuralangelo SCNeRF* Ours Images L2G-NeRF* Joint-TensoRF* Fig.
- **p. 2 / 1 Introduction - extractive body cue:** 1: 3D surface reconstruction (meshes) from images with camera poses that present significant noise.
- **p. 3 / 1 Introduction - extractive body cue:** Outlier images can happen when repetitive patterns or textureless regions are present, resulting in SfM failures.
- **p. 3 / 1 Introduction - extractive body cue:** The images are casually captured without being carefully selected, which can lead to failures of state-of-the-art SfM systems. - Accordingly, we propose a novel method ...

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** In this paper, we propose a novel framework that jointly optimizes the neural radiance field with a scene graph to alleviate the influence of outliers.
- **p. 3 / 1 Introduction - extractive body cue:** The images are casually captured without being carefully selected, which can lead to failures of state-of-the-art SfM systems. - Accordingly, we propose a novel method ...
- **p. 2 / 1 Introduction - extractive body cue:** Our method works effectively and can produce high-quality 3D reconstructions. produce a sparse scene representation.
- **p. 5 / 3 Method - extractive body cue:** 3.1 Scene Graph A scene graph G = (V, E) in SfM consists of a set of nodes V and edges E.
- **p. 5 / 3 Method - extractive body cue:** Lastly, we introduce a coarse-to-fine training strategy to ensure an efficient and stable training process (Sec.
- **p. 7 / 3 Method - extractive body cue:** Below, we first briefly review the radiance field representation and then introduce our joint optimization scheme.
- **p. 5 / 3 Method - extractive body cue:** Then, we present our joint optimization method for training the radiance field and updating the scene graph (Sec.
- **p. 5 / 3 Method - extractive body cue:** Given the training images, we first apply a widely used Structure-from-Motion (SfM) algorithm, i.e., COLMAP [40], to construct an initial scene graph of the images, ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Specifically, for each scene, the input is a set of RGB images I = {I1, I2, ..., In}, and the output is a 3D surface reconstruction S of the scene. | camera/depth stream, pose, map와 language goal | p. 5 (3 Method), p. 7 (3 Method) |
| State/latent | Specifically, scene, input, RGB, images, output, surface, reconstruction, network, takes, location, viewing | robot pose, free-space/semantic map와 local goal | p. 5 (3 Method), p. 7 (3 Method), p. 5 (3 Method) |
| Output/action | The network takes a 3D location and viewing direction as input and generates the corresponding density and RGB color (i.e., radiance) as output. | collision-free trajectory 또는 velocity command | p. 7 (3 Method), p. 5 (3 Method), p. 9 (3 Method) |
| Objective/outcome | The IoU loss aims to maximize the intersection-over-union between the two MoGs that correspond to the matched keypoints. | goal reach, safety, localization error와 replanning latency | p. 8 (3 Method), p. 8 (3 Method), p. 9 (3 Method) |

## Main Claims and Actual Contribution

- **p. 3 / 1 Introduction - extractive body cue:** In this paper, we propose a novel framework that jointly optimizes the neural radiance field with a scene graph to alleviate the influence of outliers.
- **p. 3 / 1 Introduction - extractive body cue:** The images are casually captured without being carefully selected, which can lead to failures of state-of-the-art SfM systems. - Accordingly, we propose a novel method ...
- **p. 2 / 1 Introduction - extractive body cue:** Our method works effectively and can produce high-quality 3D reconstructions. produce a sparse scene representation.
- **p. 5 / 3 Method - extractive body cue:** 3.1 Scene Graph A scene graph G = (V, E) in SfM consists of a set of nodes V and edges E.
- **p. 5 / 3 Method - extractive body cue:** Lastly, we introduce a coarse-to-fine training strategy to ensure an efficient and stable training process (Sec.
- **p. 13 / 7.71 3.77† - extractive body cue:** While BARF* achieves the best results in scene 37, it is more likely to impose negative impact on camera poses, thereby has worse performance in ...
- **p. 11 / 4 Experiments - extractive body cue:** Overall, our method achieves the best reconstruction results.
- **p. 12 / 4 Experiments - extractive body cue:** In contrast, our method shows robustness to pose errors and outperforms NeuS by 61% in Chamfer distance and by 15% in F-score.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 13 (7.71 3.77†), p. 11 (4 Experiments) |
| Embodiment/environment | We then report the comparisons with state-of-the-art methods on both the proposed dataset and a widely used benchmark, DTU dataset [21] (Sec. | hardware/simulator version and reset protocol | p. 10 (4 Experiments), p. 13 (7.71 3.77†) |
| Dataset/benchmark | After SfM, to prune the scene graph, we set the angular threshold to τ = 70 degrees for our dataset. | role, split, size and leakage | p. 10 (4 Experiments), p. 13 (7.71 3.77†), p. 10 (4 Experiments), p. 11 (4 Experiments) |
| Metric | Table 3: Quantitative results of our ablation studies. We individually remove the use of sparsification by thresholding (w/o τ), confidence estimation (w/o CS), Intersection- over-Union loss (w/o IoU), and coarse-to-fine optimization st ... | definition, denominator, direction and uncertainty | p. 14 (Figure/Table caption), p. 12 (4 Experiments), p. 14 (7.71 3.77†) |
| Baseline/ablation | We then report the comparisons with state-of-the-art methods on both the proposed dataset and a widely used benchmark, DTU dataset [21] (Sec. | fair input/data/compute/action matching | p. 10 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: 3D surface reconstruction (meshes) from images with camera poses that present significant noise. Directly training radiance fields with noisy poses can lead to ...
- **p. 14 / 5 Conclusion - extractive body cue:** Even though our method can greatly refine the inlier poses, the improvement on outlier poses is moderate (whose effect is still largely alleviated with the ...
- **p. 13 / 4 Experiments - extractive body cue:** Please also note that there are several failure cases from the competitors indicating completely incorrect reconstruction.
- **p. 10 / 4 Experiments - extractive body cue:** Most of these poses tend to come with a large angular deviation and cannot be rectified through local optimization.
- **p. 12 / 4 Experiments - extractive body cue:** The subpar performance of the competitors is due to their pose optimization processes, namely, local optimizations, which cannot rectify the poses with significant errors.
- **p. 12 / 4 Experiments - extractive body cue:** As shown, our method is more robust to outlier poses, producing less distortion and better geometric detail.
- **p. 13 / 7.71 3.77† - extractive body cue:** Why our method is robust to outliers.

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 Outlier images can happen when repetitive patterns or textureless regions are present, resulting in SfM failures.를 문제로 두고, In this paper, we propose a novel framework that jointly optimizes the neural radiance field with a scene graph to alleviate the influence of outliers.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (1 Introduction), p. 3 (1 Introduction), p. 7 (3 Method), p. 5 (3 Method), p. 5 (3 Method), p. 8 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
