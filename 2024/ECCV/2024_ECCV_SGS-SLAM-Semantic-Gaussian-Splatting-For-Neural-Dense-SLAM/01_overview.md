# SGS-SLAM: Semantic Gaussian Splatting For Neural Dense SLAM

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/4516_ECCV_2024_paper.php.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/04516.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: Gaussian Splatting, semantic
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/4516_ECCV_2024_paper.php
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/04516.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (17 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 This challenge also brings difficulties in disentangling the representation of objects, making it non-trivial to segment, edit, and manipulate objects within the scene.를 문제로 두고, Overall, our work presents several key contributions, summarized as follows: - We introduce SGS-SLAM, the first semantic RGB-D SLAM system grounded in 3D Gaussians.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** Dense Visual Simultaneous Localization and Mapping (SLAM) is a crucial problem in the field of computer vision.
- **p. 1 / 1 Introduction - extractive body cue:** It aims to reconstruct a dense 3D map in an unseen environment while simultaneously tracking the camera poses.
- **p. 1 / 1 Introduction - extractive body cue:** Traditional visual SLAM systems [6,29,31,34] stand out in sparse mapping using point clouds and voxels, but fall short in dense reconstruction.
- **p. 1 / 1 Introduction - extractive body cue:** To extract dense geometric information for high-quality representation, learning-based SLAM methods [1,37] have gained wild attention.
- **p. 1 / 1 Introduction - extractive body cue:** They demonstrate proficiency in generating decent 3D global maps meanwhile exhibiting robustness on noises and outliers.
- **p. 2 / 1 Introduction - extractive body cue:** This challenge also brings difficulties in disentangling the representation of objects, making it non-trivial to segment, edit, and manipulate objects within the scene.
- **p. 1 / 1 Introduction - extractive body cue:** However, NeRF-based SLAM methods employ multi-layer perceptrons (MLPs) as the implicit neural representation of scenes, which introduces several challenging limitations.

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** Overall, our work presents several key contributions, summarized as follows: - We introduce SGS-SLAM, the first semantic RGB-D SLAM system grounded in 3D Gaussians.
- **p. 3 / 1 Introduction - extractive body cue:** Leveraging these benefits, our method enables precise editing and manipulation of specific scene elements while preserving the high fidelity of the overall rendering.
- **p. 4 / 3 Method - extractive body cue:** Like previous SLAM techniques, our method can be split into two processes: tracking and mapping.
- **p. 6 / 3 Method - extractive body cue:** Furthermore, the integration of semantic features within our method significantly advances optimal scene interpretation and precise object-level geometry, effectively mitigating the oversmoothing issues prevalent in ...
- **p. 8 / 3 Method - extractive body cue:** This enables the joint optimization of parameters across different channels, remarkably enhancing the efficiency and effectiveness of both mapping and segmentation processes.
- **p. 8 / 3 Method - extractive body cue:** Compared to existing NeRF-based approaches [16,20,47,48] that necessitate complex model architectures and feature fusion strategies, SGS-SLAM adopts explicit Gaussian representation for mapping, resulting in high ...
- **p. 4 / 3 Method - extractive body cue:** 3.1 introduces its multi-channel Gaussian representation for joint parameter optimization.
- **p. 4 / 3 Method - extractive body cue:** Mapping optimizes the scene representations based on the estimated camera pose.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Following this, the current pose is iteratively refined by minimizing the tracking loss between the ground truth color (CGT pix ), depth images (DGT pix ), and semantic map (SGT pix ) ... | camera/depth stream, pose, map와 language goal | p. 6 (3 Method), p. 5 (3 Method) |
| State/latent | Following, current, pose, iteratively, refined, minimizing, tracking, loss, between, ground, truth, color | robot pose, free-space/semantic map와 local goal | p. 6 (3 Method), p. 5 (3 Method), p. 5 (3 Method) |
| Output/action | This aspect of visibility is essential for camera pose estimation, as it relies on the current reconstructed map. | collision-free trajectory 또는 velocity command | p. 5 (3 Method), p. 5 (3 Method), p. 6 (3 Method) |
| Objective/outcome | After densification, the parameters of the map are optimized by minimizing the mapping loss: \mathc a l { L}_ {\rm m app i ng} = \mat h cal {U}_t \sum _{\rm pix} ... | goal reach, safety, localization error와 replanning latency | p. 7 (3 Method), p. 6 (3 Method), p. 6 (3 Method) |

## Main Claims and Actual Contribution

- **p. 3 / 1 Introduction - extractive body cue:** Overall, our work presents several key contributions, summarized as follows: - We introduce SGS-SLAM, the first semantic RGB-D SLAM system grounded in 3D Gaussians.
- **p. 3 / 1 Introduction - extractive body cue:** Leveraging these benefits, our method enables precise editing and manipulation of specific scene elements while preserving the high fidelity of the overall rendering.
- **p. 4 / 3 Method - extractive body cue:** Like previous SLAM techniques, our method can be split into two processes: tracking and mapping.
- **p. 6 / 3 Method - extractive body cue:** Furthermore, the integration of semantic features within our method significantly advances optimal scene interpretation and precise object-level geometry, effectively mitigating the oversmoothing issues prevalent in ...
- **p. 8 / 3 Method - extractive body cue:** This enables the joint optimization of parameters across different channels, remarkably enhancing the efficiency and effectiveness of both mapping and segmentation processes.
- **p. 13 / 4 Experiment - extractive body cue:** The results reveal that our optimization strategy can significantly improve the localization and mapping performance.
- **p. 11 / 4 Experiment - extractive body cue:** Our method significantly outperforms the NeRF-based approaches, achieving SOTA mIoU scores over 90%.
- **p. 11 / 4 Experiment - extractive body cue:** In comparison to these previous methods, SGS-SLAM demonstrates state-of-the-art performance, outperforming the initial baseline by more than 10%.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 13 (4 Experiment), p. 11 (4 Experiment) |
| Embodiment/environment | To compare with other neural implicit SLAM methods, we evaluate synthetic scenes from Replica dataset [35] and real-world scenes from ScanNet [4] and ScanNet++ [43] datasets. | hardware/simulator version and reset protocol | p. 8 (4 Experiment), p. 11 (4 Experiment) |
| Dataset/benchmark | Furthermore, the high-quality reconstruction of scenes and precise 3D semantic labeling generated by our system establish a strong foundation for downstream tasks such as scene editing, offering solid prior for robotics or ... | role, split, size and leakage | p. 8 (4 Experiment), p. 11 (4 Experiment), p. 14 (4 Experiment), p. 11 (4 Experiment) |
| Metric | Our method excels in achieving the highest level of depth L1 loss (cm) and minimal ATE error, surpassing baseline methods by 70% in terms of depth loss and 34% in terms of ... | definition, denominator, direction and uncertainty | p. 10 (4 Experiment), p. 8 (4 Experiment), p. 8 (4 Experiment) |
| Baseline/ablation | In comparison to these previous methods, SGS-SLAM demonstrates state-of-the-art performance, outperforming the initial baseline by more than 10%. | fair input/data/compute/action matching | p. 11 (4 Experiment), p. 9 (4 Experiment), p. 10 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 13 / 4 Experiment - extractive body cue:** Specifically, the system without appearance color cannot provide rendered views, whereas camera pose and depth can still be estimated by leveraging depth and
- **p. 14 / 4 Experiment - extractive body cue:** Addressing these limitations will be an objective for future research.
- **p. 14 / 4 Experiment - extractive body cue:** Limitations SGS-SLAM replies on depth and 2D semantic signal inputs for tracking and mapping.
- **p. 9 / 4 Experiment - extractive body cue:** The results demonstrate that our method delivers more high-fidelity and robust reconstructions.
- **p. 11 / 4 Experiment - extractive body cue:** Additionally, utilizing features from different channels of Gaussians, such as geometry, appearance, and semantic information, provides multiple levels of supervision, resulting in a more robust ...

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 This challenge also brings difficulties in disentangling the representation of objects, making it non-trivial to segment, edit, and manipulate objects within the scene.를 문제로 두고, Overall, our work presents several key contributions, summarized as follows: - We introduce SGS-SLAM, the first semantic RGB-D SLAM system grounded in 3D Gaussians.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 8 (3 Method), p. 4 (3 Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
