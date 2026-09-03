# VTGaussian-SLAM: RGBD SLAM for Large Scale Scenes with Splatting View-Tied 3D Gaussians

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=vkmi3jZtYG.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/168040. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICML
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, Gaussian Splatting
- Official paper: https://openreview.net/forum?id=vkmi3jZtYG
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/168040
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 This obstacle makes 3DGS still hard to scale up to extremely large scenes in SLAM, remaining the challenge of improving the rendering quality, tracking accuracy, and scalability of 3DGS in tracking cameras ...를 문제로 두고, Our main contributions are listed below. • We propose view-tied Gaussian splatting that significantly reduces storage but improves rendering quality with 3DGS in SLAM. • We introduce a novel RGBD SLAM algorithm ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Jointly estimating camera poses and mapping scenes from RGBD images is a fundamental task in simultaneous localization and mapping (SLAM).
- **p. 1 / Abstract - extractive body cue:** State-of-the-art methods employ 3D Gaussians to represent a scene, and render these Gaussians through splatting for higher efficiency and better rendering.
- **p. 1 / Abstract - extractive body cue:** However, these methods cannot scale up to extremely large scenes, due to the inefficient tracking and mapping strategies that need to optimize all 3D Gaussians ...
- **p. 1 / Abstract - extractive body cue:** To resolve this issue, we propose novel tracking and mapping strategies to work with a novel 3D representation, dubbed view-tied 3D Gaussians, for RGBD SLAM ...
- **p. 1 / Abstract - extractive body cue:** View-tied 3D Gaussians is a kind of simplified Gaussians, which is tied to depth pixels, without needing to learn locations, rotations, and multi-dimensional variances.
- **p. 1 / 1. Introduction - extractive body cue:** This obstacle makes 3DGS still hard to scale up to extremely large scenes in SLAM, remaining the challenge of improving the rendering quality, tracking accuracy, ...
- **p. 1 / 1. Introduction - extractive body cue:** To overcome this challenge, we propose an RGBD SLAM system with splatting view-tied 3D Gaussians.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are listed below. • We propose view-tied Gaussian splatting that significantly reduces storage but improves rendering quality with 3DGS in SLAM. • ...
- **p. 1 / 1. Introduction - extractive body cue:** Our method introduces a novel point-based volume representation, dubbed view-tied 3D Gaussians, to represent the color and 1
- **p. 1 / 1. Introduction - extractive body cue:** To overcome this challenge, we propose an RGBD SLAM system with splatting view-tied 3D Gaussians.
- **p. 3 / 3.2. View-tied Gaussians - extractive body cue:** Our view-tied Gaussians aim to achieve memory efficiency in SLAM, which enables us to improve the rendering quality by using many more Gaussians to represent ...
- **p. 3 / 3.2. View-tied Gaussians - extractive body cue:** This not only enables us to use more Gaussians to represent local details, but also removes the need to maintain the appearance and geometry consistency ...
- **p. 5 / 3.4. Mapping Scenes - extractive body cue:** We minimize the rendering errors with respect to observations, min {g}k ρ//Vi-V ′ i //1+τLS(Vi, V ′ i )+σUi//Di-D′ i//1, (2) where LS is the ...
- **p. 4 / 3.3. Tracking Cameras - extractive body cue:** At each frame out of a 2000 frame video, the average error of relative pose to the previous frame is pretty small, while the average ...
- **p. 4 / 3.3. Tracking Cameras - extractive body cue:** Although better renderings are helpful for more accurate camera pose estimations, the higher accuracy is merely meaningful relative to the neighboring frames, resulting in a ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We minimize the rendering errors with respect to observations, min {g}k ρ//Vi-V ′ i //1+τLS(Vi, V ′ i )+σUi//Di-D′ i//1, (2) where LS is the SSIM loss, Ui is a mask which ... | camera/depth stream, pose, map와 language goal | p. 5 (3.4. Mapping Scenes), p. 4 (3.3. Tracking Cameras) |
| State/latent | minimize, rendering, errors, respect, observations, Vi-V, Ui//Di-D, i//1, where, SSIM, loss, mask | robot pose, free-space/semantic map와 local goal | p. 5 (3.4. Mapping Scenes), p. 4 (3.3. Tracking Cameras), p. 3 (3.2. View-tied Gaussians) |
| Output/action | We optimize pi to minimize rendering errors, min pi αWi//Vi -V ′ i //1 + βWi//Di -D′ i//1, (1) where {V ′ i , D′ i} = splat({g}o ∈So, pi) are rendered ... | collision-free trajectory 또는 velocity command | p. 4 (3.3. Tracking Cameras), p. 3 (3.2. View-tied Gaussians), p. 3 (3.2. View-tied Gaussians) |
| Objective/outcome | We minimize the rendering errors with respect to observations, min {g}k ρ//Vi-V ′ i //1+τLS(Vi, V ′ i )+σUi//Di-D′ i//1, (2) where LS is the SSIM loss, Ui is a mask which ... | goal reach, safety, localization error와 replanning latency | p. 5 (3.4. Mapping Scenes), p. 5 (3.5. Bundle Adjustment), p. 3 (3.3. Tracking Cameras) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our main contributions are listed below. • We propose view-tied Gaussian splatting that significantly reduces storage but improves rendering quality with 3DGS in SLAM. • ...
- **p. 1 / 1. Introduction - extractive body cue:** Our method introduces a novel point-based volume representation, dubbed view-tied 3D Gaussians, to represent the color and 1
- **p. 1 / 1. Introduction - extractive body cue:** To overcome this challenge, we propose an RGBD SLAM system with splatting view-tied 3D Gaussians.
- **p. 3 / 3.2. View-tied Gaussians - extractive body cue:** Our view-tied Gaussians aim to achieve memory efficiency in SLAM, which enables us to improve the rendering quality by using many more Gaussians to represent ...
- **p. 3 / 3.2. View-tied Gaussians - extractive body cue:** This not only enables us to use more Gaussians to represent local details, but also removes the need to maintain the appearance and geometry consistency ...
- **p. 7 / 4.1. Comparisons - extractive body cue:** Based on the camera poses, our method also significantly improves the rendering quality on ScanNet, as shown in Fig.
- **p. 8 / 4.2. Ablation Studies and Analysis - extractive body cue:** The comparisons show that our viewtied Gaussians not only significantly reduce the size of each Gaussian (number of parameters) but also achieve good rendering quality ...
- **p. 9 / 4.2. Ablation Studies and Analysis - extractive body cue:** 8 show that our selection strategy achieves the best performance.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4.1. Comparisons), p. 8 (4.2. Ablation Studies and Analysis) |
| Embodiment/environment | TUM-RGBD, ScanNet, and ScanNet++ are real-world datasets. | hardware/simulator version and reset protocol | p. 5 (4. Experiments and Analysis), p. 5 (4. Experiments and Analysis) |
| Dataset/benchmark | 1, mapping scenes with rendered images in Tab. | role, split, size and leakage | p. 5 (4. Experiments and Analysis), p. 5 (4. Experiments and Analysis), p. 6 (4.1. Comparisons), p. 6 (4.1. Comparisons) |
| Metric | Then we measure the reconstruction performance with F1-score, the harmonic mean of the Precision (P) and Recall (R), using a distance threshold of 1 cm for all evaluations. | definition, denominator, direction and uncertainty | p. 6 (4. Experiments and Analysis), p. 5 (4. Experiments and Analysis), p. 6 (4. Experiments and Analysis) |
| Baseline/ablation | Compared to previous GS-based SLAM methods, our method can use many more Gaussians tied at each pixel on depth images to fit sudden color change without needing to maintain the consistency of ... | fair input/data/compute/action matching | p. 7 (4.1. Comparisons), p. 6 (4.1. Comparisons), p. 6 (4. Experiments and Analysis) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4.2. Ablation Studies and Analysis - extractive body cue:** We cannot use a large number of Gaussians 8
- **p. 7 / 4.1. Comparisons - extractive body cue:** However, relying on data-driven priors, LoopSplat (Zhu et al., 2024) reported more accurate camera tracking in terms of average accuracy, while our method does not ...
- **p. 23 / Figure/Table caption - extractive body cue:** Table 22. Impact of depth noise and movability of Gaussians on the rendering performance in PSNR ↑, SSIM ↑, and LPIPS ↓on Replica (Straub et ...

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 This obstacle makes 3DGS still hard to scale up to extremely large scenes in SLAM, remaining the challenge of improving the rendering quality, tracking accuracy, and scalability of 3DGS in tracking cameras ...를 문제로 두고, Our main contributions are listed below. • We propose view-tied Gaussian splatting that significantly reduces storage but improves rendering quality with 3DGS in SLAM. • We introduce a novel RGBD SLAM algorithm ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 5 (3.4. Mapping Scenes), p. 4 (3.3. Tracking Cameras), p. 4 (3.3. Tracking Cameras) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
