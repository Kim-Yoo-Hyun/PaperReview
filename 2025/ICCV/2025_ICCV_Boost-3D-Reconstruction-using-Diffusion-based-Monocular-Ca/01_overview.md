# Boost 3D Reconstruction using Diffusion-based Monocular Camera Calibration

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=0.833); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Deng_Boost_3D_Reconstruction_using_Diffusion-based_Monocular_Camera_Calibration_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Deng_Boost_3D_Reconstruction_using_Diffusion-based_Monocular_Camera_Calibration_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, Diffusion
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Deng_Boost_3D_Reconstruction_using_Diffusion-based_Monocular_Camera_Calibration_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Deng_Boost_3D_Reconstruction_using_Diffusion-based_Monocular_Camera_Calibration_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=0.833)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 While it shows some limitations in focal estimation, this leads to slightly less accurate visualizations.를 문제로 두고, In contrast, our method is specifically designed to recover camera intrinsics.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 6. Implementation Details - extractive body cue:** Our models are built on the pretrained Stable Diffusion V2.1 model [53].
- **p. 1 / 6. Implementation Details - extractive body cue:** To train camera intrinsic estimation model, we employ the AdamW optimizer with a learning rate of 3e-5 and train the model for 30,000 iterations with ...
- **p. 1 / 6. Implementation Details - extractive body cue:** For metric depth estimation, we use the same optimizer and learning rate with a total batch size of 96, and the training process takes approximately ...
- **p. 1 / 6. Implementation Details - extractive body cue:** For all of our downstream 3D vision tasks, we did not use the ground truth camera image but instead relied on intrinsic parameters predicted by ...
- **p. 1 / 6.1. Camera intrinsic prediction - extractive body cue:** We train our model on a diverse range of datasets, ensuring balance by selecting one dataset per batch with equal probability and sampling from it.
- **p. 2 / 7.3. Metrologie - extractive body cue:** While it shows some limitations in focal estimation, this leads to slightly less accurate visualizations.
- **p. 1 / 6.3. More implementation details and discussions - extractive body cue:** 9: We assess the generalization ability across five zeroshot datasets by aligning the predicted depth ˆd to the groundtruth depth d with a scale factor ...

## Core Idea

- **p. 2 / 6.3. More implementation details and discussions - extractive body cue:** In contrast, our method is specifically designed to recover camera intrinsics.
- **p. 2 / 7.5. Mesh Reconstruction - extractive body cue:** We present the reconstruction result of Pisa tower in Fig.
- **p. 3 / 7.6. Single view 3D reconstuction - extractive body cue:** We present the predicted metric depth in both outdoor and indoor scenes.
- **p. 3 / 7.6. Single view 3D reconstuction - extractive body cue:** Our method provides more detailed results and recovers accurate metric depths. camera intrinsics and metric depth map.
- **p. 4 / 7.7. The Importance of Principal Point Evaluation - extractive body cue:** And our method is inherently capable of solving for both fx and fy and we take this into account to Table 11.
- **p. 2 / 6.3. More implementation details and discussions - extractive body cue:** Method Waymo RGBD ScanNet MVS Scenes11 Average ef eb ef eb ef eb ef eb ef eb ef eb Ours-small 0.138 0.033 0.051 0.012 0.084 ...
- **p. 1 / 6. Implementation Details - extractive body cue:** For metric depth estimation, we use the same optimizer and learning rate with a total batch size of 96, and the training process takes approximately ...
- **p. 2 / 6.3. More implementation details and discussions - extractive body cue:** 10: From a single input image, we first estimate the camera intrinsics and metric depth map, transform them into a 3D point cloud using the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | 10: From a single input image, we first estimate the camera intrinsics and metric depth map, transform them into a 3D point cloud using the pinhole camera model, and calculate the 3D ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (6.3. More implementation details and discussions), p. 1 (6.2. Metric depth prediction) |
| State/latent | single, input, image, first, estimate, camera, intrinsics, metric, depth, transform, them, point | geometry, map, object/relationship state | p. 2 (6.3. More implementation details and discussions), p. 1 (6.2. Metric depth prediction), p. 2 (6.3. More implementation details and discussions) |
| Output/action | Based on this setting, we treat the metric depth with different scale factor for indoor and outdoor: s = {sin, sout}, and the depth label become ds = d/si with si ∈s ... | point map, pose, scene graph, affordance 또는 query result | p. 1 (6.2. Metric depth prediction), p. 2 (6.3. More implementation details and discussions), p. 1 (6.2. Metric depth prediction) |
| Objective/outcome | Method Waymo RGBD ScanNet MVS Scenes11 Average ef eb ef eb ef eb ef eb ef eb ef eb Ours-small 0.138 0.033 0.051 0.012 0.084 0.023 0.080 0.010 0.071 0.014 0.085 0.017 ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 2 (6.3. More implementation details and discussions), p. 1 (6.1. Camera intrinsic prediction), p. 1 (6. Implementation Details) |

## Main Claims and Actual Contribution

- **p. 2 / 6.3. More implementation details and discussions - extractive body cue:** In contrast, our method is specifically designed to recover camera intrinsics.
- **p. 2 / 7.5. Mesh Reconstruction - extractive body cue:** We present the reconstruction result of Pisa tower in Fig.
- **p. 3 / 7.6. Single view 3D reconstuction - extractive body cue:** We present the predicted metric depth in both outdoor and indoor scenes.
- **p. 3 / 7.6. Single view 3D reconstuction - extractive body cue:** Our method provides more detailed results and recovers accurate metric depths. camera intrinsics and metric depth map.
- **p. 4 / 7.7. The Importance of Principal Point Evaluation - extractive body cue:** And our method is inherently capable of solving for both fx and fy and we take this into account to Table 11.
- **p. 4 / 7.7. The Importance of Principal Point Evaluation - extractive body cue:** Despite targeting metric depth, we achieve performance comparable to SoTA affine-invariant depth methods.
- **p. 5 / 7.8. The Importance of camera image in metric - extractive body cue:** With intrinsic cues, our method achieves more accurate and better-aligned reconstructions. results on three additional datasets in Tab.12, complementing the findings in Tab.5.
- **p. 2 / 6.3. More implementation details and discussions - extractive body cue:** The results demonstrate that Dust3r achieves more accurate reconstruction when equipped with our estimated intrinsics.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 4 (7.7. The Importance of Principal Point Evaluation), p. 5 (7.8. The Importance of camera image in metric) |
| Embodiment/environment | Dataset Images Scene Intrinsic Training Set NuScenes [7] 28k Outdoor Calibrated KITTI [11] 18 k Outdoor Calibrated CityScapes [11] 23k Outdoor Calibrated NYUv2 [44] 6k Indoor Calibrated SUN3D [78] 33k Indoor Calibrated ... | hardware/simulator version and reset protocol | p. 1 (6.2. Metric depth prediction), p. 1 (6.2. Metric depth prediction) |
| Dataset/benchmark | NuScenes KITTI CityScapes NYUv2 eb 0.051 0.021 0.055 0.050 ˆeb 0.007 0.014 0.011 0.009 ensure more robust estimation and support future broader applications and datasets such as Diode [70]. | role, split, size and leakage | p. 1 (6.2. Metric depth prediction), p. 1 (6.2. Metric depth prediction), p. 4 (7.7. The Importance of Principal Point Evaluation), p. 2 (6.3. More implementation details and discussions) |
| Metric | Then we employ single-step diffusion at timestamp T to generate depth latent code ˆzd, which is then decoded into predicted metric depth ˆd. ground truth generated using COLMAP [58] from 60 images ... | definition, denominator, direction and uncertainty | p. 2 (6.3. More implementation details and discussions), p. 4 (7.7. The Importance of Principal Point Evaluation), p. 3 (7.6. Single view 3D reconstuction) |
| Baseline/ablation | 10: The pose estimation is compared against pseudo | fair input/data/compute/action matching | p. 1 (6.3. More implementation details and discussions), p. 1 (6.1. Camera intrinsic prediction), p. 2 (7.2. Relative Depth) |

## Explicit Limitations and Failure Boundary

- **p. 2 / 7.3. Metrologie - extractive body cue:** While it shows some limitations in focal estimation, this leads to slightly less accurate visualizations.
- **p. 2 / 6.3. More implementation details and discussions - extractive body cue:** This process is less robust and often converges to a local minimum.
- **p. 3 / 7.7. The Importance of Principal Point Evaluation - extractive body cue:** We have a significant amount of data where the principal point does not lie at the image center in certain datasets, and our model effectively ...
- **p. 3 / 7.6. Single view 3D reconstuction - extractive body cue:** We demonstrate the robustness of our intrinsic estimation and depth prediction through in-the-wild single-view 3D reconstructions.
- **p. 4 / 7.8. The Importance of camera image in metric - extractive body cue:** The camera image (intrinsic information) is essential for robust and accurate metric depth estimation.
- **p. 4 / 7.7. The Importance of Principal Point Evaluation - extractive body cue:** Our method accurately recovers real-world metrics while demonstrating robustness to variations in focal length.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 While it shows some limitations in focal estimation, this leads to slightly less accurate visualizations.를 문제로 두고, In contrast, our method is specifically designed to recover camera intrinsics.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (7.3. Metrologie), p. 1 (6.3. More implementation details and discussions), p. 2 (6.3. More implementation details and discussions), p. 1 (6. Implementation Details), p. 2 (6.3. More implementation details and discussions), p. 1 (6.2. Metric depth prediction) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
