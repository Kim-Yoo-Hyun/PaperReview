# Problem - SEGS-SLAM: Structure-enhanced 3D Gaussian Splatting SLAM with Appearance Embedding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Wen_SEGS-SLAM_Structure-enhanced_3D_Gaussian_Splatting_SLAM_with_Appearance_Embedding_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Wen_SEGS-SLAM_Structure-enhanced_3D_Gaussian_Splatting_SLAM_with_Appearance_Embedding_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction)): However, AE has a notable limitation: its training involves each ground-truth image from the test set.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** 3D Gaussian splatting (3D-GS) has recently revolutionized novel view synthesis in the simultaneous localization and mapping (SLAM) problem.
- **p. 1 / Abstract - extractive body cue:** However, most existing algorithms fail to fully capture the underlying structure, resulting in structural inconsistency.
- **p. 1 / Abstract - extractive body cue:** Additionally, they struggle with abrupt appearance variations, leading to inconsistent visual quality.
- **p. 1 / Abstract - extractive body cue:** To address these problems, we propose SEGS-SLAM, a structure-enhanced 3D Gaussian Splatting SLAM, which achieves high-quality photorealistic mapping.
- **p. 1 / Abstract - extractive body cue:** Our main contributions are two-fold.
- **p. 2 / 1. Introduction - extractive body cue:** However, AE has a notable limitation: its training involves each ground-truth image from the test set.
- **p. 2 / 1. Introduction - extractive body cue:** To address the above limitations, this paper presents SEGS-SLAM, a novel 3D Gaussian Splatting SLAM system.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, AE has a notable limitation: its training involves each ground-truth image from the test set. | mapped 3D environment과 mobile robot | body wording is the source claim |
| Observation / input | Based on this observation, we propose incrementally voxelizing the point cloud Pk of each keyframe to construct anchor points, as follows: Vk ... | camera/depth stream, pose, map와 language goal | exact sensor/frame/preprocessing from PDF body |
| State / latent | observation, incrementally, voxelizing, point, cloud, keyframe, construct, anchor, points, follows | robot pose, free-space/semantic map와 local goal | notation and tensor shape require body check |
| Output / action | differences, between, them, uses, image, indexes, input, whereas | collision-free trajectory 또는 velocity command | exact unit/frame/decoder require body check |
| Target outcome | goal reach with collision-free execution | goal reach, safety, localization error와 replanning latency | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | sensor/map state and goal; body terms: observation, incrementally, voxelizing, point, cloud, keyframe, construct, anchor, points, follows | p. 4 (4.1. Structure-Enhanced Photorealistic Mapping), p. 2 (1. Introduction), p. 4 (2.1 Test on the right half of each) |
| Decision / output variable | path/waypoint/velocity; body terms: Second, Appearancefrom-Motion, embedding, AfME, takes, poses, input, eliminates | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (Abstract) |
| Objective / loss / cost | path cost, risk or goal utility; cue terms: optimization, learnable, parameters, MLP, achieved, minimizing, loss, SSIM | p. 3 (3.2. Localization and Geometry Mapping), p. 4 (4. SEGS-SLAM), p. 5 (4.4. Losses Design), p. 5 (4.3. Frequency Pyramid Regularization) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (4.3. Frequency Pyramid Regularization), p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Success / guarantee | goal reach with collision-free execution | p. 7 (5.2. Results Analysis), p. 2 (3. Extensive evaluations on various public datasets demon), p. 6 (5.2. Results Analysis) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** To address the above limitations, this paper presents SEGS-SLAM, a novel 3D Gaussian Splatting SLAM system.
- **p. 1 / 1. Introduction - extractive body cue:** Visual simultaneous localization and mapping (SLAM) is a fundamental problem in 3D computer vision, with wide applications in autonomous driving, robotics, virtual reality, and augmented ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (Abstract), p. 1 (Abstract), p. 4 (4. SEGS-SLAM)): Second, we propose Appearancefrom-Motion embedding (AfME), which takes poses as input and eliminates the need for training on the left half of each ground-truth image in the test set.

- **p. 2 / 1. Introduction - extractive body cue:** Motivated by this, we propose a structure-enhanced photorealistic mapping (SEPM) framework, which initializes anchor points using ORB-SLAM3 [3] point cloud, significantly enhancing the utilization of ...
- **p. 1 / Abstract - extractive body cue:** To address these problems, we propose SEGS-SLAM, a structure-enhanced 3D Gaussian Splatting SLAM, which achieves high-quality photorealistic mapping.
- **p. 1 / Abstract - extractive body cue:** Second, we propose Appearance-from-Motion embedding (AfME), enabling 3D Gaussians to better model image appearance variations across different camera poses.
- **p. 4 / 4. SEGS-SLAM - extractive body cue:** Visualization of the Photo-SLAM's 3D Gaussians and of our method's anchor points using only SEPM after 30k iterations.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 8 | One limitation of our method is that a poorly structured point cloud leads to a decline in photorealistic ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | GS-SLAM∗denotes the result of GS-SLAM is taken from [42], all others are obtained in our experiments. '-' denotes ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | The best results are marked as best score , second best score and third best score . '-' ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

navigation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (4.1. Structure-Enhanced Photorealistic Mapping), p. 2 (1. Introduction), p. 4 (2.1 Test on the right half of each), p. 5 (4.2. Appearance-from-Motion Embedding). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), interface p. 4 (4.1. Structure-Enhanced Photorealistic Mapping), p. 2 (1. Introduction), p. 4 (2.1 Test on the right half of each), p. 5 (4.2. Appearance-from-Motion Embedding), objective p. 3 (3.2. Localization and Geometry Mapping), p. 4 (4. SEGS-SLAM), p. 5 (4.4. Losses Design), p. 5 (4.3. Frequency Pyramid Regularization).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
