# SplaTAM: Splat Track & Map 3D Gaussians for Dense RGB-D SLAM

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Keetha_SplaTAM_Splat_Track__Map_3D_Gaussians_for_Dense_RGB-D_CVPR_2024_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Keetha_SplaTAM_Splat_Track__Map_3D_Gaussians_for_Dense_RGB-D_CVPR_2024_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, geometry, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/CVPR2024/html/Keetha_SplaTAM_Splat_Track__Map_3D_Gaussians_for_Dense_RGB-D_CVPR_2024_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/CVPR2024/papers/Keetha_SplaTAM_Splat_Track__Map_3D_Gaussians_for_Dense_RGB-D_CVPR_2024_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, this is difficult for implicit map representations, as the network is subject to global changes during gradient-based optimization for the unmapped space. • Explicit map: We can arbitrarily increase the map ...를 문제로 두고, We show across all our experiments on simulated and real data that our approach, SplaTAM, achieves state-of-the-art results compared to all previous approaches for camera pose estimation, map estimation, and novel-view synthesis.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Dense simultaneous localization and mapping (SLAM) is crucial for robotics and augmented reality applications.
- **p. 1 / Abstract - extractive body cue:** However, current methods are often hampered by the nonvolumetric or implicit way they represent a scene.
- **p. 1 / Abstract - extractive body cue:** This work introduces SplaTAM, an approach that, for the first time, leverages explicit volumetric representations, i.e., 3D Gaussians, to enable high-fidelity reconstruction from a single ...
- **p. 1 / Abstract - extractive body cue:** SplaTAM employs a simple online tracking and mapping system tailored to the underlying Gaussian representation.
- **p. 1 / Abstract - extractive body cue:** It utilizes a silhouette mask to elegantly capture the presence of scene density.
- **p. 2 / 1. Introduction - extractive body cue:** However, this is difficult for implicit map representations, as the network is subject to global changes during gradient-based optimization for the unmapped space. • Explicit ...
- **p. 2 / 1. Introduction - extractive body cue:** However, current methods use implicit neural representations to model the volumetric radiance fields, which causes a number of issues in the SLAM setting - they ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** We show across all our experiments on simulated and real data that our approach, SplaTAM, achieves state-of-the-art results compared to all previous approaches for camera ...
- **p. 2 / 1. Introduction - extractive body cue:** We introduce several simple modifications that make splatting even faster for SLAM, including the removal of view-dependent appearance and the use of isotropic Gaussians.
- **p. 4 / 3. Method - extractive body cue:** We propose to similarly differentiably render depth: D( \ m a thb f {p}) = \ s um _{i = 1}^{n} d_i f_i(\mathbf {p}) \prod ...
- **p. 3 / 3. Method - extractive body cue:** The core of our approach is the ability to render high-fidelity color, depth, and silhouette images from our underlying Gaussian Map 21359
- **p. 4 / 3. Method - extractive body cue:** This differentiable rendering allows us to directly calculate the gradients in the underlying scene representation (Gaussians) and camera parameters with respect to the error between ...
- **p. 4 / 3. Method - extractive body cue:** E.g. the camera parameters are initialized using the following: E_ { t+ 1} = E_t + (E_t - E_{t \text {-} 1} ) (7) The ...
- **p. 4 / 3. Method - extractive body cue:** We begin with a brief overview and then describe each module in detail.
- **p. 3 / 3. Method - extractive body cue:** By modeling the world as a collection of 3D Gaussians which can be rendered into highfidelity color and depth images, we are able to directly ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We propose to similarly differentiably render depth: D( \ m a thb f {p}) = \ s um _{i = 1}^{n} d_i f_i(\mathbf {p}) \prod _{j=1}^{i-1} (1 - f_j(\mathbf {p})), (4) which ... | camera/depth stream, pose, map와 language goal | p. 4 (3. Method), p. 4 (3. Method) |
| State/latent | similarly, differentiably, render, depth, mathbf, prod, compared, against, input, return, gradients, respect | robot pose, free-space/semantic map와 local goal | p. 4 (3. Method), p. 4 (3. Method), p. 3 (3. Method) |
| Output/action | We add new Gaussians to the map based on the rendered silhouette and input depth. | collision-free trajectory 또는 velocity command | p. 4 (3. Method), p. 3 (3. Method), p. 2 (1. Introduction) |
| Objective/outcome | E.g. the camera parameters are initialized using the following: E_ { t+ 1} = E_t + (E_t - E_{t \text {-} 1} ) (7) The camera pose is then updated iteratively by ... | goal reach, safety, localization error와 replanning latency | p. 4 (3. Method), p. 4 (3. Method), p. 5 (3. Method) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** We show across all our experiments on simulated and real data that our approach, SplaTAM, achieves state-of-the-art results compared to all previous approaches for camera ...
- **p. 2 / 1. Introduction - extractive body cue:** We introduce several simple modifications that make splatting even faster for SLAM, including the removal of view-dependent appearance and the use of isotropic Gaussians.
- **p. 4 / 3. Method - extractive body cue:** We propose to similarly differentiably render depth: D( \ m a thb f {p}) = \ s um _{i = 1}^{n} d_i f_i(\mathbf {p}) \prod ...
- **p. 3 / 3. Method - extractive body cue:** The core of our approach is the ability to render high-fidelity color, depth, and silhouette images from our underlying Gaussian Map 21359
- **p. 4 / 3. Method - extractive body cue:** This differentiable rendering allows us to directly calculate the gradients in the underlying scene representation (Gaussians) and camera parameters with respect to the error between ...
- **p. 6 / 5. Results & Discussion - extractive body cue:** Compared to prior methods in this category [30, 54], SplaTAM still significantly outperforms, decreasing the trajectory error of the prior SOTA in this category [30] ...
- **p. 6 / 5. Results & Discussion - extractive body cue:** Our approach achieves much better results than the other baselines Vox-Fusion [46] and NICESLAM [54], improving over both by around 10dB in PSNR.
- **p. 7 / 5. Results & Discussion - extractive body cue:** Both the RGB and depth work together to achieve excellent results.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 6 (5. Results & Discussion), p. 6 (5. Results & Discussion) |
| Embodiment/environment | Replica [35] is the simplest benchmark as it contains synthetic scenes, highly accurate and complete (synthetic) depth maps, and small displacements between consecutive camera poses. | hardware/simulator version and reset protocol | p. 5 (4. Experimental Setup), p. 6 (5. Results & Discussion) |
| Dataset/benchmark | In this section, we first discuss our evaluation results on camera pose estimation for the four benchmark datasets. | role, split, size and leakage | p. 5 (4. Experimental Setup), p. 6 (5. Results & Discussion), p. 5 (5. Results & Discussion), p. 6 (5. Results & Discussion) |
| Metric | Using only an RGB loss successfully tracks the camera trajectory (although with more than 5x the error as using both). | definition, denominator, direction and uncertainty | p. 7 (5. Results & Discussion), p. 8 (5. Results & Discussion), p. 6 (5. Results & Discussion) |
| Baseline/ablation | The main baseline method we compare to is Point-SLAM [30], the previous state-of-the-art (SOTA) method for dense radiance-field-based SLAM. | fair input/data/compute/action matching | p. 5 (4. Experimental Setup), p. 6 (5. Results & Discussion), p. 6 (5. Results & Discussion) |

## Explicit Limitations and Failure Boundary

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3. Renderings on ScanNet++ [49]. Our method, SplaTAM, renders color & depth for the novel & train views with fidelity comparable to the ground ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. SplaTAM enables precise camera tracking and high-fidelity reconstruction for dense simultaneous localization and mapping (SLAM) in challenging real-world scenarios. SplaTAM achieves this by ...
- **p. 6 / 5. Results & Discussion - extractive body cue:** However, all current SLAM benchmarks don't have a hold-out set of images separate from the camera trajectory that the SLAM algorithm estimates, so they cannot ...
- **p. 7 / 5. Results & Discussion - extractive body cue:** In contrast, Point-SLAM [30] fails at camera-pose tracking and overfits to the training views, and isn't able to successfully render novel views at all.
- **p. 7 / 5. Results & Discussion - extractive body cue:** Since Point-SLAM [30] fails to successfully estimate the camera poses and build a good map, it also completely fails on the task of novel-view synthesis.
- **p. 8 / 5. Results & Discussion - extractive body cue:** Silhouette is critical as without it tracking completely fails.
- **p. 6 / 5. Results & Discussion - extractive body cue:** On ScanNet++ [49], both SOTA SLAM approaches Point-SLAM [30] and ORB-SLAM3 [3] (RGB-D variant) completely fail to correctly track the camera pose due to the ...

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, this is difficult for implicit map representations, as the network is subject to global changes during gradient-based optimization for the unmapped space. • Explicit map: We can arbitrarily increase the map ...를 문제로 두고, We show across all our experiments on simulated and real data that our approach, SplaTAM, achieves state-of-the-art results compared to all previous approaches for camera pose estimation, map estimation, and novel-view synthesis.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 4 (3. Method), p. 4 (3. Method), p. 3 (3. Method), p. 3 (3. Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
