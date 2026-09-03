# UW-GS: Distractor-Aware 3D Gaussian Splatting for Enhanced Underwater Scene Reconstruction

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/WACV2025/html/Wang_UW-GS_Distractor-Aware_3D_Gaussian_Splatting_for_Enhanced_Underwater_Scene_Reconstruction_WACV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/WACV2025/papers/Wang_UW-GS_Distractor-Aware_3D_Gaussian_Splatting_for_Enhanced_Underwater_Scene_Reconstruction_WACV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / WACV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/WACV2025/html/Wang_UW-GS_Distractor-Aware_3D_Gaussian_Splatting_for_Enhanced_Underwater_Scene_Reconstruction_WACV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/WACV2025/papers/Wang_UW-GS_Distractor-Aware_3D_Gaussian_Splatting_for_Enhanced_Underwater_Scene_Reconstruction_WACV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, underwater activities are often constrained by the limitations of current technologies, the scarcity of diving experts, and high operational costs.를 문제로 두고, To address this issue, we propose a novel approach for color appearance formation.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** 3D Gaussian splatting (3DGS) offers the capability to achieve real-time high quality 3D scene rendering.
- **p. 1 / Abstract - extractive body cue:** However, 3DGS assumes that the scene is in a clear medium environment and struggles to generate satisfactory representations in underwater scenes, where light absorption and ...
- **p. 1 / Abstract - extractive body cue:** To overcome these, we introduce a novel Gaussian Splatting-based method, UW-GS, designed specifically for underwater applications.
- **p. 1 / Abstract - extractive body cue:** It introduces a color appearance that models distance-dependent color variation, employs a new physics-based density control strategy to enhance clarity for distant objects, and uses ...
- **p. 1 / Abstract - extractive body cue:** Optimized with a well-designed loss function supporting for scattering media and strengthened by pseudo-depth maps, UW-GS outperforms existing methods with PSNR gains up to 1.26dB.
- **p. 1 / 1. Introduction - extractive body cue:** However, underwater activities are often constrained by the limitations of current technologies, the scarcity of diving experts, and high operational costs.
- **p. 2 / 1. Introduction - extractive body cue:** Finally, given the scarcity of underwater datasets, we collected a new dataset featuring four expansive areas of shallow underwater scenes, each presenting unique challenges compared ...

## Core Idea

- **p. 4 / 3.3. Color Appearance Model - extractive body cue:** To address this issue, we propose a novel approach for color appearance formation.
- **p. 1 / 1. Introduction - extractive body cue:** To address the aforementioned issues, we propose a new Gaussian Splatting (GS)-based method, UW-GS, specifically for underwater scenes.
- **p. 2 / 1. Introduction - extractive body cue:** We also incorporated pseudo-depth maps generated from DepthAnything [47], trained with more general scenes, to enhance the robustness of our method.
- **p. 3 / 3.1. Problem formulation - extractive body cue:** Therefore, we propose a new color appearance model and a physical-based density control module in UW-GS.
- **p. 4 / 3.3. Color Appearance Model - extractive body cue:** The left panel of Figure 2 illustrates the workflow of our method.
- **p. 4 / 3.1. Problem formulation - extractive body cue:** In the splatting process, the physical-based density control module addresses densification failures and the binary motion mask handle distractors. we propose a pixel-level mask, named ...
- **p. 5 / 3.5. Binary Motion Mask - extractive body cue:** Inspired by RobustNeRF [35], we introduce a Binary Motion Mask (BMM) ω into our reconstruction loss function to eliminate the distractors as the follows: LRec ...
- **p. 6 / 3.6. Loss Function - extractive body cue:** We use a synthetic ground truth depth map D that is predicted by DepthAnything [47], a novel monocular depth estimation model that can adapt to ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The 3D Gaussians with modified color will be sent to do 2D projection and then generate pixel color in rasterization module to output the final underwater image. | RGB-D, image set, point cloud, depth와 camera pose | p. 4 (3.2. Overview of UW-GS), p. 4 (3.3. Color Appearance Model) |
| State/latent | Gaussians, modified, color, will, sent, projection, then, generate, pixel, rasterization, module, output | geometry, map, object/relationship state | p. 4 (3.2. Overview of UW-GS), p. 4 (3.3. Color Appearance Model), p. 6 (3.6. Loss Function) |
| Output/action | Similar to [25], we use an additional MLP f with positon encoded depth and viewing direction input to estimate medium properties: (T D i , T B i , βd i , ... | point map, pose, scene graph, affordance 또는 query result | p. 4 (3.3. Color Appearance Model), p. 6 (3.6. Loss Function), p. 6 (3.6. Loss Function) |
| Objective/outcome | However, in underwater scenes, Equation 3 suggests that δLRec δcolor is calculated from T D · δLRec δcolorobject so that each Gaussian color gradient has an attenuation factor T D due to ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3.4. Physical-based Density Control), p. 6 (3.6. Loss Function), p. 5 (3.6. Loss Function) |

## Main Claims and Actual Contribution

- **p. 4 / 3.3. Color Appearance Model - extractive body cue:** To address this issue, we propose a novel approach for color appearance formation.
- **p. 1 / 1. Introduction - extractive body cue:** To address the aforementioned issues, we propose a new Gaussian Splatting (GS)-based method, UW-GS, specifically for underwater scenes.
- **p. 2 / 1. Introduction - extractive body cue:** We also incorporated pseudo-depth maps generated from DepthAnything [47], trained with more general scenes, to enhance the robustness of our method.
- **p. 3 / 3.1. Problem formulation - extractive body cue:** Therefore, we propose a new color appearance model and a physical-based density control module in UW-GS.
- **p. 4 / 3.3. Color Appearance Model - extractive body cue:** The left panel of Figure 2 illustrates the workflow of our method.
- **p. 7 / 5. Results and Discussion - extractive body cue:** For the SeaThru-NeRF dataset, our method shows the best overall performance and achieves average 2.09dB and 2.70dB PSNR improvement compared to 3DGS and Seathru-NeRF respectively, ...
- **p. 8 / 5. Results and Discussion - extractive body cue:** The results are shown in Table 2 verifies that our architecture can achieve the overall best performance while others suffer from performance degradation.
- **p. 7 / 5. Results and Discussion - extractive body cue:** The limited improvement compared to 3DGS can be attributed to the unstable lighting from above the water surface.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (5. Results and Discussion), p. 8 (5. Results and Discussion) |
| Embodiment/environment | On the other hand, we will also use these three metrics in dynamic scenes after using motion mask provided from dataset to exclude moving objects. | hardware/simulator version and reset protocol | p. 7 (4. Experiment Configuration), p. 6 (4. Experiment Configuration) |
| Dataset/benchmark | We selected two challenging scenes from the IW dataset [39], which includes motion masks that aid in assessing reconstruction quality by excluding dynamic content. | role, split, size and leakage | p. 7 (4. Experiment Configuration), p. 6 (4. Experiment Configuration), p. 8 (5. Results and Discussion), p. 6 (4. Experiment Configuration) |
| Metric | Figure 1. Visual comparison between 3DGS [22] and our proposed UW-GS method. Left to right: Raw videos and the results of 3DGS and UW-GS, respectively. The top row, enhanced for visualization purposes, ... | definition, denominator, direction and uncertainty | p. 2 (Figure/Table caption), p. 7 (5. Results and Discussion), p. 6 (4. Experiment Configuration) |
| Baseline/ablation | We tested our method and compared with three state of the arts: Instant-NGP [33], SeaThru-NeRF [26], and original 3DGS [22]. | fair input/data/compute/action matching | p. 6 (4. Experiment Configuration), p. 7 (5. Results and Discussion), p. 7 (5. Results and Discussion) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Results and Discussion - extractive body cue:** The improvement of our method is not obvious in the shallow underwater scene because the disturbance of light from above the water cannot be neglected.
- **p. 7 / 5. Results and Discussion - extractive body cue:** The limited improvement compared to 3DGS can be attributed to the unstable lighting from above the water surface.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. The diagram of our proposed UW-GS approach, combining a novel color appearance model, physical-based density control and binary motion mask to 3DGS. Our ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Left: Diagram of 2D Position gradient calculation. Right: Illustration of densification failures (G2 highlighted in orange) that appear to be not cloned or ...
- **p. 7 / 5. Results and Discussion - extractive body cue:** Our approach illustrates effectiveness and robustness across various scenes.
- **p. 8 / 5. Results and Discussion - extractive body cue:** The results are shown in Table 2 verifies that our architecture can achieve the overall best performance while others suffer from performance degradation.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. Visual comparison between 3DGS [22] and our proposed UW-GS method. Left to right: Raw videos and the results of 3DGS and UW-GS, respectively. ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, underwater activities are often constrained by the limitations of current technologies, the scarcity of diving experts, and high operational costs.를 문제로 두고, To address this issue, we propose a novel approach for color appearance formation.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem formulation), p. 4 (3.1. Problem formulation), p. 1 (1. Introduction), p. 3 (3.1. Problem formulation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
