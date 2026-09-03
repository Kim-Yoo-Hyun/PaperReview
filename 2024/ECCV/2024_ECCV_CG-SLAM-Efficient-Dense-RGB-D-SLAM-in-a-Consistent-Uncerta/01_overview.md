# CG-SLAM: Efficient Dense RGB-D SLAM in a Consistent Uncertainty-aware 3D Gaussian Field

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3580_ECCV_2024_paper.php.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03580.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: World models, safety, uncertainty, and recovery
- Tier: REFERENCE
- Tags: Gaussian Splatting, geometry, 3D Vision
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3580_ECCV_2024_paper.php
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03580.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

World models, safety, uncertainty, and recovery의 navigation 문제를 이해하기 위해 읽는다. 본문은 Traditional visual SLAM systems [24] have shown accurate tracking performance across various scenes, while the underlying 3D representations (e.g., point cloud, mesh, and surfel) demonstrate limitations in facilitating highly free scene ...를 문제로 두고, Overall, our contributions can be summarized as follows: - We present a new GPU-accelerated framework for real-time dense RGB-D SLAM based on a thorough theoretical analysis of camera pose derivatives in 3D ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** Dense visual Localization and Mapping (Visual SLAM) is a long-standing problem in 3D computer vision over recent decades, which targets performing pose tracking and scene ...
- **p. 1 / 1 Introduction - extractive body cue:** Traditional visual SLAM systems [24] have shown accurate tracking performance across various scenes, while the underlying 3D representations (e.g., point cloud, mesh, and surfel) demonstrate ...
- **p. 1 / 1 Introduction - extractive body cue:** Inspired by the Neural Radiance Field (NeRF) [29] in surface reconstruction and view rendering, some novel NeRF-based SLAM methods [17,28,37,61] have ∗Jiarui Hu and Xianhao ...
- **p. 2 / 1 Introduction - extractive body cue:** FPS ≈15 Hz Mean PSNR: 33.27 dB Mean PSNR: 34.60 dB Acc: 1.10 cm RMSE: 0.29 cm Acc: 1.28 cm RMSE: 0.31 cm Fig.
- **p. 2 / 1 Introduction - extractive body cue:** 1: CG-SLAM, which adopts a well-designed 3D Gaussian field, can simultaneously achieve state-of-the-art performance in localization, reconstruction and rendering.
- **p. 2 / 1 Introduction - extractive body cue:** At the same time, we observed that solely employing alpha-blending depth cannot
- **p. 2 / 1 Introduction - extractive body cue:** As a photorealistic view synthesis technique, the 3D Gaussian field is prone to overfitting the input images due to strong anisotropy and the lack of ...

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** Overall, our contributions can be summarized as follows: - We present a new GPU-accelerated framework for real-time dense RGB-D SLAM based on a thorough theoretical ...
- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we introduce a real-time Gaussian splatting SLAM system, i.e., CG-SLAM, based on a novel uncertainty-aware 3D Gaussian field with high consistency and ...
- **p. 7 / 3 Method - extractive body cue:** To mitigate drastic changes in positions of Gaussian primitives during optimization, we proposed a geometry variance loss term (Eq.
- **p. 7 / 3 Method - extractive body cue:** Hence, we propose an uncertainty model suitable for RGB-D observations from two perspectives: rendering images and Gaussian primitives.
- **p. 6 / 3 Method - extractive body cue:** Fast Gaussian splatting rasterizer enables efficient pixel-by-pixel parallel rendering, and is fully differentiable, which provides a useful GPU-accelerated framework.
- **p. 9 / 3 Method - extractive body cue:** Given the fixed scene representation, the camera pose is initially guessed via the constant speed assumption where the last pose is transformed by the last ...
- **p. 9 / 3 Method - extractive body cue:** In initialization, we densely project Gaussian primitives into 3D space based on depth observations of the first frame.
- **p. 5 / 3 Method - extractive body cue:** Finally, by minimizing the re-rendering loss from low-uncertainty primitives, we can build a real-time and accurate tracking module (Sec.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Hence, we propose an uncertainty model suitable for RGB-D observations from two perspectives: rendering images and Gaussian primitives. | camera/depth stream, pose, map와 language goal | p. 7 (3 Method), p. 7 (3 Method) |
| State/latent | Hence, uncertainty, model, suitable, RGB-D, observations, perspectives, rendering, images, Gaussian, primitives, alpha | robot pose, free-space/semantic map와 local goal | p. 7 (3 Method), p. 7 (3 Method), p. 8 (3 Method) |
| Output/action | \ l abe l {eq -1 0 } U = \sum _{i=1}^N \alpha _i T_i (~d_i - D~)^2~, (10) where D represents depth observations from the camera sensor. | collision-free trajectory 또는 velocity command | p. 7 (3 Method), p. 8 (3 Method), p. 8 (3 Method) |
| Objective/outcome | Finally, by minimizing the re-rendering loss from low-uncertainty primitives, we can build a real-time and accurate tracking module (Sec. | goal reach, safety, localization error와 replanning latency | p. 5 (3 Method), p. 7 (3 Method), p. 8 (3 Method) |

## Main Claims and Actual Contribution

- **p. 3 / 1 Introduction - extractive body cue:** Overall, our contributions can be summarized as follows: - We present a new GPU-accelerated framework for real-time dense RGB-D SLAM based on a thorough theoretical ...
- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we introduce a real-time Gaussian splatting SLAM system, i.e., CG-SLAM, based on a novel uncertainty-aware 3D Gaussian field with high consistency and ...
- **p. 7 / 3 Method - extractive body cue:** To mitigate drastic changes in positions of Gaussian primitives during optimization, we proposed a geometry variance loss term (Eq.
- **p. 7 / 3 Method - extractive body cue:** Hence, we propose an uncertainty model suitable for RGB-D observations from two perspectives: rendering images and Gaussian primitives.
- **p. 6 / 3 Method - extractive body cue:** Fast Gaussian splatting rasterizer enables efficient pixel-by-pixel parallel rendering, and is fully differentiable, which provides a useful GPU-accelerated framework.
- **p. 9 / 4 Experiments - extractive body cue:** In this section, we describe our experimental setup and validate that the proposed system can achieve improvement in both accuracy (Sec.
- **p. 11 / 4 Experiments - extractive body cue:** Our system achieves better tracking accuracy and lower variance in different scenarios. "-" indicates unavailable results because the related work is not open source.
- **p. 10 / 4 Experiments - extractive body cue:** 2, despite noisy and sparse depth information in the real-world TUM-RGBD dataset [44], our method still achieves better or competitive performance in 5 selected scenarios.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (4 Experiments), p. 11 (4 Experiments) |
| Embodiment/environment | We examined the generalization of our method on real-world TUM [44] and ScanNet [10] datasets, which contain 5 and 6 challenging scenes respectively. | hardware/simulator version and reset protocol | p. 10 (4 Experiments), p. 10 (4 Experiments) |
| Dataset/benchmark | Our system consistently achieved the best performance in this dataset, both for 8 individual scenes and for the average. | role, split, size and leakage | p. 10 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments) |
| Metric | This plot illustrates that the uncertainty model helps improve tracking accuracy while avoiding some extreme errors. | definition, denominator, direction and uncertainty | p. 14 (56.50 MB), p. 10 (4 Experiments), p. 10 (4 Experiments) |
| Baseline/ablation | We primarily consider state-of-the-art NeRF-SLAM works, including NICE-SLAM [61], Co-SLAM [50], Point-SLAM [37], and Vox-Fusion [56], as baselines. | fair input/data/compute/action matching | p. 10 (4 Experiments), p. 11 (4 Experiments), p. 13 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 14 / 5 Conclusion - extractive body cue:** Considerable memory usage is one limitation of the Gaussianbased system.
- **p. 11 / 4 Experiments - extractive body cue:** Our method achieves state-of-the-art tracking results in 6 scenes and exceeds other methods on average. "-" indicates failure results in Vox-Fusion [56].
- **p. 14 / 56.50 MB - extractive body cue:** The experimental results demonstrate the effectiveness of our anisotropy regularization term. "-" indicates a failure situation.
- **p. 12 / 4 Experiments - extractive body cue:** Due to the inherent limitation of 3D Gaussian representation, our method is slightly worse in completion.
- **p. 12 / 4 Experiments - extractive body cue:** This reason results in a considerable memory footprint in the Gaussian-based SLAM system, which is a common limitation in other Gaussian-based research topics.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 3: Uncertainty of the Gaussian Primitives. Uncertainty of a Gaussian prim- itive is derived from its dominated pixels and corresponding depth biases, reflecting the ...
- **p. 13 / 56.50 MB - extractive body cue:** Oppositely, excessive regularization (Isotropic Gaussians) will degrade rendering and subsequently affect the photometric loss, leading to poor tracking performance.

## Why Read It

World models, safety, uncertainty, and recovery의 navigation 문제를 이해하기 위해 읽는다. 본문은 Traditional visual SLAM systems [24] have shown accurate tracking performance across various scenes, while the underlying 3D representations (e.g., point cloud, mesh, and surfel) demonstrate limitations in facilitating highly free scene ...를 문제로 두고, Overall, our contributions can be summarized as follows: - We present a new GPU-accelerated framework for real-time dense RGB-D SLAM based on a thorough theoretical analysis of camera pose derivatives in 3D ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 3 (1 Introduction), p. 7 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
