# WaterSplatting: Fast Underwater 3D Scene Reconstruction using Gaussian Splatting

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/.
> PDF retrieval source: https://openreview.net/attachment?id=Z9yn9YgNIz&name=pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / 3DV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, 3D reconstruction, 3D Vision
- Official paper: https://3dvconf.github.io/2025/accepted-papers/
- Full-text retrieval: https://openreview.net/attachment?id=Z9yn9YgNIz&name=pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 The underwater 3D scene reconstruction is a challenging, yet interesting problem with applications ranging from naval robots to VR experiences.를 문제로 두고, Loss Function Alignment: We propose a novel loss function designed to align 3DGS with human perception of High Dynamic Range (HDR) and low-light scenes.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** The underwater 3D scene reconstruction is a challenging, yet interesting problem with applications ranging from naval robots to VR experiences.
- **p. 1 / Abstract - extractive body cue:** The problem was successfully tackled by fully volumetric NeRF-based methods which can model both the geometry and the medium (water).
- **p. 1 / Abstract - extractive body cue:** Unfortunately, these methods are slow to train and do not offer real-time rendering.
- **p. 1 / Abstract - extractive body cue:** More recently, 3D Gaussian Splatting (3DGS) method offered a fast alternative to NeRFs.
- **p. 1 / Abstract - extractive body cue:** However, because it is an explicit method that renders only the geometry, it cannot render the medium and is therefore unsuited for underwater reconstruction.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Loss Function Alignment: We propose a novel loss function designed to align 3DGS with human perception of High Dynamic Range (HDR) and low-light scenes.
- **p. 2 / 1. Introduction - extractive body cue:** Splatting with Medium: We introduce a novel approach that combines the strengths of Gaussian Splatting (GS) and volume rendering.
- **p. 3 / 3.2. Splatting with Medium - extractive body cue:** We illustrate the pipeline of our method in Fig.
- **p. 4 / 3.3. Loss Function Alignment - extractive body cue:** For the case of our 3DGS-based model, we propose a regularized loss function LReg: we apply pixel-wise weight W = {wi,j} on both rendered estimate ...
- **p. 3 / 3.2. Splatting with Medium - extractive body cue:** Under the occlusion of both primitives and medium, our model acquires the transmittance along the ray and is capable of synthesizing medium component and object ...
- **p. 3 / 3.1. Preliminaries - extractive body cue:** For scene rendering in scattering media we use the revised underwater image formation model from [1] where the final image I is separated into a ...
- **p. 5 / 3.3. Loss Function Alignment - extractive body cue:** Integrating regularization into the LReg-DSSIM formulation becomes particularly critical for 3DGS optimization due to the discrete nature of its primitives, necessitating structural regularization to maintain ...
- **p. 3 / 3. Method - extractive body cue:** Then, we illustrate our proposed rendering model combining 3DGS with medium encoding in Sec.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The input to our model is a set of images with scattering medium and corresponding camera poses. | RGB-D, image set, point cloud, depth와 camera pose | p. 3 (3.2. Splatting with Medium), p. 3 (3.1. Preliminaries) |
| State/latent | input, model, images, scattering, medium, corresponding, camera, poses, meantime, DGS, prunes, primitives | geometry, map, object/relationship state | p. 3 (3.2. Splatting with Medium), p. 3 (3.1. Preliminaries), p. 4 (3.2. Splatting with Medium) |
| Output/action | In the meantime, 3DGS prunes primitives with low opacity for acceleration and periodically set αi close to zero for all Gaussians to moderate the increase of floaters close to the input cameras. | point map, pose, scene graph, affordance 또는 query result | p. 3 (3.1. Preliminaries), p. 4 (3.2. Splatting with Medium), p. 4 (3.3. Loss Function Alignment) |
| Objective/outcome | For the case of our 3DGS-based model, we propose a regularized loss function LReg: we apply pixel-wise weight W = {wi,j} on both rendered estimate ˆy and target image y, where wi,j ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 4 (3.3. Loss Function Alignment), p. 4 (3.3. Loss Function Alignment), p. 5 (3.3. Loss Function Alignment) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Loss Function Alignment: We propose a novel loss function designed to align 3DGS with human perception of High Dynamic Range (HDR) and low-light scenes.
- **p. 2 / 1. Introduction - extractive body cue:** Splatting with Medium: We introduce a novel approach that combines the strengths of Gaussian Splatting (GS) and volume rendering.
- **p. 3 / 3.2. Splatting with Medium - extractive body cue:** We illustrate the pipeline of our method in Fig.
- **p. 4 / 3.3. Loss Function Alignment - extractive body cue:** For the case of our 3DGS-based model, we propose a regularized loss function LReg: we apply pixel-wise weight W = {wi,j} on both rendered estimate ...
- **p. 3 / 3.2. Splatting with Medium - extractive body cue:** Under the occlusion of both primitives and medium, our model acquires the transmittance along the ray and is capable of synthesizing medium component and object ...
- **p. 7 / 4.1. Results - extractive body cue:** Our rendering without medium and depth maps significantly outperform those from the SeaThru-NeRF, especially in scenes that are farther from the camera.
- **p. 6 / 4.1. Results - extractive body cue:** Our method achieves better rendering quality and preserves finer distant geometric details while reducing the amount of floaters.
- **p. 7 / 4.1. Results - extractive body cue:** We also achieve higher PSNR values in both scenes.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4.1. Results), p. 6 (4.1. Results) |
| Embodiment/environment | SeaThru-NeRF Dataset: SeaThru-NeRF Dataset released by [18] contains real-world scenes acquired from four different scenes in sea: IUI3 Red Sea, Curac¸ao, Japanese Gardens Red Sea, and Panama. | hardware/simulator version and reset protocol | p. 5 (4. Experiments), p. 5 (4.1. Results) |
| Dataset/benchmark | These comparisons are made across validation sets for the SeaThru-NeRF dataset in Table 3. | role, split, size and leakage | p. 5 (4. Experiments), p. 5 (4.1. Results), p. 7 (4.2. Ablation Study), p. 6 (4.1. Results) |
| Metric | We present the alpha blending of depth as the depth map and the rendering without medium to demonstrate the ability to decouple the medium and the object for SeaThru-NeRF and our method. | definition, denominator, direction and uncertainty | p. 5 (4. Experiments), p. 7 (4.1. Results), p. 5 (4.1. Results) |
| Baseline/ablation | Our rendering without medium and depth maps significantly outperform those from the SeaThru-NeRF, especially in scenes that are farther from the camera. | fair input/data/compute/action matching | p. 7 (4.1. Results), p. 5 (4. Experiments), p. 5 (4.1. Results) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 5. Limitations - extractive body cue:** Although our method achieves good reconstruction quality, there are some limitations to consider.
- **p. 7 / 5. Limitations - extractive body cue:** However, in the foreground, our method prunes medium-role primitives well while SeaThru-NeRF cannot prevent the geometrical field from fitting the medium, resulting in wave-like artifacts.
- **p. 8 / 5. Limitations - extractive body cue:** Limitation: insufficient supervision.
- **p. 8 / 5. Limitations - extractive body cue:** Limitation: simulating distant medium with Gaussians.
- **p. 6 / 4.1. Results - extractive body cue:** Both traditional 3DGS and NeRF with a proposal sampler cannot handle semitransparent medium well.
- **p. 5 / 4.1. Results - extractive body cue:** However, ZipNeRF training takes orders of magnitude more time than our method and does not offer real-time rendering.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Splatting with Medium: We start rendering by casting a ray per pixel and collect the patch-intersected Gaussians along the ray and their color ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 The underwater 3D scene reconstruction is a challenging, yet interesting problem with applications ranging from naval robots to VR experiences.를 문제로 두고, Loss Function Alignment: We propose a novel loss function designed to align 3DGS with human perception of High Dynamic Range (HDR) and low-light scenes.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 4 (3.3. Loss Function Alignment), p. 3 (3.1. Preliminaries), p. 5 (3.3. Loss Function Alignment), p. 3 (3. Method), p. 4 (3.3. Loss Function Alignment), p. 5 (3.3. Loss Function Alignment) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
