# IGL-Nav: Incremental 3D Gaussian Localization for Image-goal Navigation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Guo_IGL-Nav_Incremental_3D_Gaussian_Localization_for_Image-goal_Navigation_ICCV_2025_paper.html.
> PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Guo_IGL-Nav_Incremental_3D_Gaussian_Localization_for_Image-goal_Navigation_ICCV_2025_paper.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: NEXT
- Tags: 3D Vision, Navigation, Gaussian Splatting
- Official paper: https://openaccess.thecvf.com/content/ICCV2025/html/Guo_IGL-Nav_Incremental_3D_Gaussian_Localization_for_Image-goal_Navigation_ICCV_2025_paper.html
- Full-text retrieval: https://openaccess.thecvf.com/content/ICCV2025/papers/Guo_IGL-Nav_Incremental_3D_Gaussian_Localization_for_Image-goal_Navigation_ICCV_2025_paper.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 To address these limitations, RNRMap [14] introduces a renderable neural radiance map representation.를 문제로 두고, To this end, we propose IGL-Nav, an Incremental 3D Gaussian Localization framework that (1) progressively constructs 3DGS through feed-forward prediction, eliminating offline optimization; and (2) enables efficient hierarchical goal sea ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Visual navigation with an image as goal is a fundamental and challenging problem.
- **p. 1 / Abstract - extractive body cue:** Conventional methods either rely on end-to-end RL learning or modular-based policy with topological graph or BEV map as memory, which cannot fully model the geometric ...
- **p. 1 / Abstract - extractive body cue:** In order to efficiently and accurately localize the goal image in 3D space, we build our navigation system upon the renderable 3D gaussian (3DGS) representation.
- **p. 1 / Abstract - extractive body cue:** However, due to the computational intensity of 3DGS optimization and the large search space of 6-DoF camera pose, directly leveraging 3DGS for image localization during ...
- **p. 1 / Abstract - extractive body cue:** To this end, we propose IGL-Nav, an Incremental 3D Gaussian Localization framework for efficient and 3D-aware image-goal navigation.
- **p. 1 / 1. Introduction - extractive body cue:** To address these limitations, RNRMap [14] introduces a renderable neural radiance map representation.
- **p. 2 / 1. Introduction - extractive body cue:** Despite these compelling properties, adapting 3DGS representations for image-goal navigation presents significant challenges.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose IGL-Nav, an Incremental 3D Gaussian Localization framework that (1) progressively constructs 3DGS through feed-forward prediction, eliminating offline optimization; and (2) ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we propose to leverage 3D Gaussian Splatting (3DGS) [10] as the scene representation for imagegoal navigation.
- **p. 3 / 3.1. Problem Statement - extractive body cue:** A is the set of actions, which consists of move forward, turn left, turn right and stop.
- **p. 3 / 3.2. Incremental Scene Representation - extractive body cue:** To accommodate streaming video input while effectively leveraging camera pose and depth priors, we present the first feedforward 3DGS reconstruction model for monocular RGB-D sequences, ...
- **p. 4 / 3.3.1. Coarse Target Localization - extractive body cue:** To solve this problem, we propose to further discretize the 3D embeddings Et and Eg.
- **p. 3 / 3.2. Incremental Scene Representation - extractive body cue:** We first concatenate the normalized RGB and depth images, and then extract dense monocular scene embedding E′ t with a UNet-based encoder E.
- **p. 5 / 3.3.2. Fine Target Localization - extractive body cue:** Then we formulate the optimization loss as: L = 1 Q Q-1 X i=0 (/Xi g -Xi/2) (9) where Q is the number of matching ...
- **p. 5 / 3.3.1. Coarse Target Localization - extractive body cue:** We use focal loss [17] to supervise the activation map after 3D convolution.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Incremental Scene Representation Scene Embedding 𝑬௧ Coarse-to-fine Navigation Reaching Target Local Policy Action Renderingbased Stopper Exploration Current RGB-D Input Target Image Activation Map Target Embedding 𝑬௚ Occupancy Map + Cam ... | camera/depth stream, pose, map와 language goal | p. 5 (3.3.1. Coarse Target Localization), p. 3 (3.2. Incremental Scene Representation) |
| State/latent | Incremental, Scene, Representation, Embedding, Coarse-to-fine, Navigation, Reaching, Target, Local, Policy, Action, Renderingbased | robot pose, free-space/semantic map와 local goal | p. 5 (3.3.1. Coarse Target Localization), p. 3 (3.2. Incremental Scene Representation), p. 3 (3.1. Problem Statement) |
| Output/action | Our incremental reconstruction model is essentially a mapping fθ from observations to 3DGS parameters, including position µk, opacity αk, covariance Σk and spherical harmonics ck: fθ : (It, Dt) 7→{(µk, αk, Σk, ... | collision-free trajectory 또는 velocity command | p. 3 (3.2. Incremental Scene Representation), p. 3 (3.1. Problem Statement), p. 5 (3.3.1. Coarse Target Localization) |
| Objective/outcome | Additionally, we apply cross-entropy loss to supervise the outputs nearby target pose in the activation map. | goal reach, safety, localization error와 replanning latency | p. 5 (3.3.1. Coarse Target Localization), p. 5 (3.3.2. Fine Target Localization), p. 3 (3.2. Incremental Scene Representation) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** To this end, we propose IGL-Nav, an Incremental 3D Gaussian Localization framework that (1) progressively constructs 3DGS through feed-forward prediction, eliminating offline optimization; and (2) ...
- **p. 2 / 1. Introduction - extractive body cue:** In this paper, we propose to leverage 3D Gaussian Splatting (3DGS) [10] as the scene representation for imagegoal navigation.
- **p. 3 / 3.1. Problem Statement - extractive body cue:** A is the set of actions, which consists of move forward, turn left, turn right and stop.
- **p. 3 / 3.2. Incremental Scene Representation - extractive body cue:** To accommodate streaming video input while effectively leveraging camera pose and depth priors, we present the first feedforward 3DGS reconstruction model for monocular RGB-D sequences, ...
- **p. 4 / 3.3.1. Coarse Target Localization - extractive body cue:** To solve this problem, we propose to further discretize the 3D embeddings Et and Eg.
- **p. 7 / 4.3. Analysis of IGL-Nav - extractive body cue:** It is shown that using a 3-level subdivision achieves best performance, because a finer discretization will reduce quantization error and improve the accuracy of coarse ...
- **p. 6 / 4.2. Comparison with State-of-the-art - extractive body cue:** IGL-Nav establishes new state-of-the-art performance and outperforms previous methods by a large margin on all metrics, which validates the effectiveness of 3D gaussian representation and ...
- **p. 7 / 4.2. Comparison with State-of-the-art - extractive body cue:** SR: Success Rate, SPL: Success weighted by Path Length.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4.3. Analysis of IGL-Nav), p. 6 (4.2. Comparison with State-of-the-art) |
| Embodiment/environment | We further deploy IGL-Nav on real-world robotic platform to test its generalization ability. | hardware/simulator version and reset protocol | p. 8 (4.4. Real-world Deployment), p. 6 (4.1. Experimental Setup) |
| Dataset/benchmark | For image-goal navigation, we follow the public Gibson [31] image-goal navigation dataset within the Habitat simulator [25] introduced by NRNS [7]. | role, split, size and leakage | p. 8 (4.4. Real-world Deployment), p. 6 (4.1. Experimental Setup), p. 6 (4.1. Experimental Setup), p. 8 (4.4. Real-world Deployment) |
| Metric | SR: Success Rate, SPL: Success weighted by Path Length. | definition, denominator, direction and uncertainty | p. 7 (4.2. Comparison with State-of-the-art), p. 7 (4.3. Analysis of IGL-Nav), p. 6 (4.2. Comparison with State-of-the-art) |
| Baseline/ablation | IGL-Nav establishes new state-of-the-art performance and outperforms previous methods by a large margin on all metrics, which validates the effectiveness of 3D gaussian representation and the proposed coarse-to-fine target localization ... | fair input/data/compute/action matching | p. 6 (4.2. Comparison with State-of-the-art), p. 7 (4.2. Comparison with State-of-the-art), p. 6 (4. Experiment) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 5. Conclusion - extractive body cue:** A limitation of IGL-Nav is that it requires depth and camera intrinsics of goal image.
- **p. 7 / 4.3. Analysis of IGL-Nav - extractive body cue:** As shown in Table 3, with predicted depth and camera intrinsics, the performance of IGLNav is still robust.

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 To address these limitations, RNRMap [14] introduces a renderable neural radiance map representation.를 문제로 두고, To this end, we propose IGL-Nav, an Incremental 3D Gaussian Localization framework that (1) progressively constructs 3DGS through feed-forward prediction, eliminating offline optimization; and (2) enables efficient hierarchical goal sea ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.1. Problem Statement), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3.2. Incremental Scene Representation) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (10 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** To address these limitations, RNRMap [14] introduces a renderable neural radiance map representation. (p. 1, 1. Introduction).
- **Actual contribution:** To this end, we propose IGL-Nav, an Incremental 3D Gaussian Localization framework that (1) progressively constructs 3DGS through feed-forward prediction, eliminating offline optimization; and (2) enables efficient hierarchical goal sea ... (p. 2, 1. Introduction).
- **Evaluation boundary:** It is shown that using a 3-level subdivision achieves best performance, because a finer discretization will reduce quantization error and improve the accuracy of coarse localization. (p. 7, 4.3. Analysis of IGL-Nav).
- **Explicit failure boundary:** A limitation of IGL-Nav is that it requires depth and camera intrinsics of goal image. (p. 8, 5. Conclusion).
