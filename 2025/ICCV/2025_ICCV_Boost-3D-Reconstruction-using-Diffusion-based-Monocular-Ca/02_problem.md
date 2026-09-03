# Problem - Boost 3D Reconstruction using Diffusion-based Monocular Camera Calibration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Deng_Boost_3D_Reconstruction_using_Diffusion-based_Monocular_Camera_Calibration_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Deng_Boost_3D_Reconstruction_using_Diffusion-based_Monocular_Camera_Calibration_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (7.3. Metrologie), p. 1 (6.3. More implementation details and discussions)): While it shows some limitations in focal estimation, this leads to slightly less accurate visualizations.

## PDF Body Digest

- **p. 1 / 6. Implementation Details - extractive body cue:** Our models are built on the pretrained Stable Diffusion V2.1 model [53].
- **p. 1 / 6. Implementation Details - extractive body cue:** To train camera intrinsic estimation model, we employ the AdamW optimizer with a learning rate of 3e-5 and train the model for 30,000 iterations with ...
- **p. 1 / 6. Implementation Details - extractive body cue:** For metric depth estimation, we use the same optimizer and learning rate with a total batch size of 96, and the training process takes approximately ...
- **p. 1 / 6. Implementation Details - extractive body cue:** For all of our downstream 3D vision tasks, we did not use the ground truth camera image but instead relied on intrinsic parameters predicted by ...
- **p. 1 / 6.1. Camera intrinsic prediction - extractive body cue:** We train our model on a diverse range of datasets, ensuring balance by selecting one dataset per batch with equal probability and sampling from it.
- **p. 2 / 7.3. Metrologie - extractive body cue:** While it shows some limitations in focal estimation, this leads to slightly less accurate visualizations.
- **p. 1 / 6.3. More implementation details and discussions - extractive body cue:** 9: We assess the generalization ability across five zeroshot datasets by aligning the predicted depth ˆd to the groundtruth depth d with a scale factor ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | While it shows some limitations in focal estimation, this leads to slightly less accurate visualizations. | 3D scene/object와 robot coordinate frame | body wording is the source claim |
| Observation / input | 10: From a single input image, we first estimate the camera intrinsics and metric depth map, transform them into a 3D point ... | RGB-D, image set, point cloud, depth와 camera pose | exact sensor/frame/preprocessing from PDF body |
| State / latent | single, input, image, first, estimate, camera, intrinsics, metric, depth, transform | geometry, map, object/relationship state | notation and tensor shape require body check |
| Output / action | Dust3r, delivers, less, accurate, intrinsic, estimation, because, focuses | point map, pose, scene graph, affordance 또는 query result | exact unit/frame/decoder require body check |
| Target outcome | spatial accuracy and downstream robot utility | geometric accuracy, semantic consistency와 planning/manipulation utility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | image/point input I/P and pose; body terms: single, input, image, first, estimate, camera, intrinsics, metric, depth, transform | p. 2 (6.3. More implementation details and discussions), p. 1 (6.2. Metric depth prediction), p. 2 (6.3. More implementation details and discussions) |
| Decision / output variable | geometry/map/query r; body terms: contrast, specifically, designed, recover, camera, intrinsics, present, reconstruction | p. 2 (6.3. More implementation details and discussions), p. 2 (7.5. Mesh Reconstruction), p. 3 (7.6. Single view 3D reconstuction) |
| Objective / loss / cost | geometric/semantic reconstruction or matching loss; cue terms: Waymo, RGBD, ScanNet, MVS, Scenes11, Average, Ours-small, Ours | p. 2 (6.3. More implementation details and discussions) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 1 (6.1. Camera intrinsic prediction), p. 1 (6. Implementation Details), p. 2 (6.3. More implementation details and discussions) |
| Success / guarantee | spatial accuracy and downstream robot utility | p. 2 (6.3. More implementation details and discussions), p. 4 (7.7. The Importance of Principal Point Evaluation), p. 3 (7.6. Single view 3D reconstuction) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 6.3. More implementation details and discussions - extractive body cue:** 9: We assess the generalization ability across five zeroshot datasets by aligning the predicted depth ˆd to the groundtruth depth d with a scale factor ...

## What the Paper Changes

PDF body contribution framing (p. 2 (6.3. More implementation details and discussions), p. 2 (7.5. Mesh Reconstruction), p. 3 (7.6. Single view 3D reconstuction), p. 3 (7.6. Single view 3D reconstuction), p. 4 (7.7. The Importance of Principal Point Evaluation)): In contrast, our method is specifically designed to recover camera intrinsics.

- **p. 2 / 7.5. Mesh Reconstruction - extractive body cue:** We present the reconstruction result of Pisa tower in Fig.
- **p. 3 / 7.6. Single view 3D reconstuction - extractive body cue:** We present the predicted metric depth in both outdoor and indoor scenes.
- **p. 3 / 7.6. Single view 3D reconstuction - extractive body cue:** Our method provides more detailed results and recovers accurate metric depths. camera intrinsics and metric depth map.
- **p. 4 / 7.7. The Importance of Principal Point Evaluation - extractive body cue:** And our method is inherently capable of solving for both fx and fy and we take this into account to Table 11.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 2 | While it shows some limitations in focal estimation, this leads to slightly less accurate visualizations. | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | This process is less robust and often converges to a local minimum. | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | We have a significant amount of data where the principal point does not lie at the image center ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 3 | We demonstrate the robustness of our intrinsic estimation and depth prediction through in-the-wild single-view 3D reconstructions. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

3d_perception writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (6.3. More implementation details and discussions), p. 1 (6.2. Metric depth prediction), p. 2 (6.3. More implementation details and discussions), p. 1 (6.2. Metric depth prediction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (7.3. Metrologie), p. 1 (6.3. More implementation details and discussions), interface p. 2 (6.3. More implementation details and discussions), p. 1 (6.2. Metric depth prediction), p. 2 (6.3. More implementation details and discussions), p. 1 (6.2. Metric depth prediction), objective p. 2 (6.3. More implementation details and discussions).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
