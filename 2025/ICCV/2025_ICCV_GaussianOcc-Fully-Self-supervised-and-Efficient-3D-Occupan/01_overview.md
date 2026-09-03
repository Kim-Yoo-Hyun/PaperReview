# GaussianOcc: Fully Self-supervised and Efficient 3D Occupancy Estimation with Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Gan_GaussianOcc_Fully_Self-supervised_and_Efficient_3D_Occupancy_Estimation_with_Gaussian_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Gan_GaussianOcc_Fully_Self-supervised_and_Efficient_3D_Occupancy_Estimation_with_Gaussian_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Gaussian Splatting, sensor fusion, LiDAR, 3D Vision
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Gan_GaussianOcc_Fully_Self-supervised_and_Efficient_3D_Occupancy_Estimation_with_Gaussian_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Gan_GaussianOcc_Fully_Self-supervised_and_Efficient_3D_Occupancy_Estimation_with_Gaussian_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, these approaches face two significant limitations.를 문제로 두고, In summary, our core contributions are as follows: • We introduce the first fully self-supervised method for efficient surrounding-view 3D occupancy estimation, featuring the exploration of Gaussian splatting. • We propose Gaussian ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We introduce GaussianOcc, a systematic method that investigates Gaussian splatting for fully self-supervised and efficient 3D occupancy estimation in surround views.
- **p. 1 / Abstract - extractive body cue:** First, traditional methods for self-supervised 3D occupancy estimation still require ground truth 6D ego pose from sensors during training.
- **p. 1 / Abstract - extractive body cue:** To address this limitation, we propose Gaussian Splatting for Projection (GSP) module to provide accurate scale information for fully self-supervised training from adjacent view projection.
- **p. 1 / Abstract - extractive body cue:** Additionally, existing methods rely on volume rendering for final 3D voxel representation learning using 2D signals (depth maps and semantic maps), which is time-consuming and ...
- **p. 1 / Abstract - extractive body cue:** We propose Gaussian Splatting from Voxel space (GSV) to leverage the fast rendering properties of Gaussian splatting.
- **p. 2 / 1. Introduction - extractive body cue:** However, these approaches face two significant limitations.
- **p. 2 / 1. Introduction - extractive body cue:** These limitations impede the development of a more general and efficient paradigm for self-supervised 3D occupancy estimation.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our core contributions are as follows: • We introduce the first fully self-supervised method for efficient surrounding-view 3D occupancy estimation, featuring the exploration ...
- **p. 2 / 1. Introduction - extractive body cue:** Instead, we propose performing Gaussian splatting directly from the 3D voxel space.
- **p. 4 / 3.2. Scale-aware training by Gaussian Splatting - extractive body cue:** We propose Gaussian splatting for projection in stage 1 for better scale-aware training as follows.
- **p. 5 / 4.2. Implementation details - extractive body cue:** Training details: We propose a two-stage training for fully self-supervised 3D occupancy estimation as indicated in Figure 2.
- **p. 1 / 1. Introduction - extractive body cue:** To facilitate 3D occupancy estimation, several benchmarks have been developed for supervised training [40-42, 44], though these require substantial effort in 3D annotation.
- **p. 4 / 3.3. Fast rendering by Gaussian Splatting - extractive body cue:** Overlap mask in nuScenes [3] and DDAD [13]. though we have the vertices at that region during the splatting rendering, after the optimization, the network ...
- **p. 5 / 4.2. Implementation details - extractive body cue:** For occupancy estimation, we use the same network as OccNeRF [53] to ensure a fair comparison.
- **p. 5 / 4.2. Implementation details - extractive body cue:** In the depth estimation benchmark, we use the network proposed by SimpleOcc, where the final output size is 256×256×16.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In the depth estimation benchmark, we use the network proposed by SimpleOcc, where the final output size is 256×256×16. | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (4.2. Implementation details), p. 5 (4.2. Implementation details) |
| State/latent | depth, estimation, benchmark, network, SimpleOcc, where, final, output, size, Gaussian, splatting, setting | geometry, map, object/relationship state | p. 5 (4.2. Implementation details), p. 5 (4.2. Implementation details), p. 4 (3.2. Scale-aware training by Gaussian Splatting) |
| Output/action | In our Gaussian splatting setting, we further upsample the final output to 512×512×32 for improved performance since we observe that a finer voxel grid leads to a finer rendered depth map, which ... | point map, pose, scene graph, affordance 또는 query result | p. 5 (4.2. Implementation details), p. 4 (3.2. Scale-aware training by Gaussian Splatting), p. 7 (Method) |
| Objective/outcome | GS loss means using the spatial context constraint by our proposed Gaussian splatting for projection. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 7 (Method), p. 3 (3.1. Preliminaries), p. 3 (3.2. Scale-aware training by Gaussian Splatting) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In summary, our core contributions are as follows: • We introduce the first fully self-supervised method for efficient surrounding-view 3D occupancy estimation, featuring the exploration ...
- **p. 2 / 1. Introduction - extractive body cue:** Instead, we propose performing Gaussian splatting directly from the 3D voxel space.
- **p. 4 / 3.2. Scale-aware training by Gaussian Splatting - extractive body cue:** We propose Gaussian splatting for projection in stage 1 for better scale-aware training as follows.
- **p. 5 / 4.2. Implementation details - extractive body cue:** Training details: We propose a two-stage training for fully self-supervised 3D occupancy estimation as indicated in Figure 2.
- **p. 1 / 1. Introduction - extractive body cue:** To facilitate 3D occupancy estimation, several benchmarks have been developed for supervised training [40-42, 44], though these require substantial effort in 3D annotation.
- **p. 5 / 4.3. Main results - extractive body cue:** In stage 1, GaussianOcc ‡ achieves top performance on the nuScenes dataset and delivers competitive results on the DDAD.
- **p. 5 / 4.3. Main results - extractive body cue:** 3D occupancy estimation in nuScenes: In Table 1, the proposed GaussianOcc achieves the best performance compared to other self-supervised methods.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Comparisons for self-supervised multi-camera depth estimation on the nuScenes [3] and DDAD datasets [13]. The results are averaged over all views without median ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 5 (4.3. Main results), p. 5 (4.3. Main results) |
| Embodiment/environment | Tasks, datasets, and metric nuScenes [3]: For 3D occupancy estimation, we utilize annotations from Occ3D [40]. | hardware/simulator version and reset protocol | p. 4 (4. Experiment), p. 5 (4.3. Main results) |
| Dataset/benchmark | We train the models for 12 epochs on both the nuScenes and DDAD. | role, split, size and leakage | p. 4 (4. Experiment), p. 5 (4.3. Main results), p. 5 (4.2. Implementation details) |
| Metric | Figure 6. The comparison for the depth map in the different set- ting, corresponding to the training strategy in Table 4 and render- ing type in Table 5. it, excluding regions that ... | definition, denominator, direction and uncertainty | p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 5 (4.3. Main results) |
| Baseline/ablation | 3D occupancy estimation in nuScenes: In Table 1, the proposed GaussianOcc achieves the best performance compared to other self-supervised methods. | fair input/data/compute/action matching | p. 5 (4.3. Main results), p. 5 (4.3. Main results), p. 7 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6. The comparison for the depth map in the different set- ting, corresponding to the training strategy in Table 4 and render- ing type ...
- **p. 5 / 4.3. Main results - extractive body cue:** As highlighted by the red rectangle, the sky region has a short-range depth value, but this does not appear in the rendered 3D occupancy estimation ...
- **p. 5 / 4.3. Main results - extractive body cue:** Note that RenderOcc [36] does not require the 3D occupancy label, but it is not a self-supervised method since it uses the ground truth depth ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, these approaches face two significant limitations.를 문제로 두고, In summary, our core contributions are as follows: • We introduce the first fully self-supervised method for efficient surrounding-view 3D occupancy estimation, featuring the exploration of Gaussian splatting. • We propose Gaussian ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 4 (3.3. Fast rendering by Gaussian Splatting), p. 4 (3.2. Scale-aware training by Gaussian Splatting), p. 5 (4.2. Implementation details) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
