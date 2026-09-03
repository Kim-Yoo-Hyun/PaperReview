# OpenGS-Fusion: Open-Vocabulary Dense Mapping with Hybrid 3D Gaussian Splatting for Refined Object-Level Understanding

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2508.01150.
> PDF retrieval source: https://arxiv.org/pdf/2508.01150. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / IROS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: 3D Vision, Gaussian Splatting, semantic
- Official paper: https://arxiv.org/abs/2508.01150
- Full-text retrieval: https://arxiv.org/pdf/2508.01150
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, they lack the ability to synthesize novel views and struggle with high-fidelity reconstruction.를 문제로 두고, Our method enables versatile task-oriented interactions, such as 3D object extraction and editing in an interactive manner.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Recent advancements in 3D scene understanding have made significant strides in enabling interaction with scenes using open-vocabulary queries, particularly for VR/AR and robotic applications.
- **p. 1 / Abstract - extractive body cue:** Nevertheless, existing methods are hindered by rigid offline pipelines and the inability to provide precise 3D object-level understanding given open-ended queries.
- **p. 1 / Abstract - extractive body cue:** In this paper, we present OpenGS-Fusion, an innovative openvocabulary dense mapping framework that improves semantic modeling and refines object-level understanding.
- **p. 1 / Abstract - extractive body cue:** OpenGSFusion combines 3D Gaussian representation with a Truncated Signed Distance Field to facilitate lossless fusion of semantic features on-the-fly.
- **p. 1 / Abstract - extractive body cue:** Furthermore, we introduce a novel multimodal language-guided approach named MLLM-Assisted Adaptive Thresholding, which refines the segmentation of 3D objects by adaptively adjusting similarity thresholds, achieving ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, they lack the ability to synthesize novel views and struggle with high-fidelity reconstruction.
- **p. 1 / I. INTRODUCTION - extractive body cue:** A key factor in facilitating these tasks is the underlying scene representation that bridges the gap between 2D and 3D.

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our method enables versatile task-oriented interactions, such as 3D object extraction and editing in an interactive manner.
- **p. 2 / 2) Limited 3D Object-Level Understanding. Most exist - extractive body cue:** In summary, our contributions are as follows. • We introduce OpenGS-Fusion, an innovative openvocabulary dense mapping framework that leverages a hybrid scene representation to concurrently ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Compared to 3DGS-featurefield-based methods [12]-[15], our approach enables online modeling of scene appearance, geometry, and semantics while supporting 3D objectlevel queries.
- **p. 4 / III. OPENGS-FUSION - extractive body cue:** This approach allows our method to obtain a relatively accurate geometric representation at the initialization stage, reducing the optimization cost.
- **p. 3 / III. OPENGS-FUSION - extractive body cue:** Additionally, the proposed open-vocabulary query strategy enables precise localization of 3D objects without the need for explicit scene segmentation.
- **p. 4 / III. OPENGS-FUSION - extractive body cue:** We first input Q into the CLIP model to extract text features, which are then compared with semantic features F of all global voxels V ...
- **p. 1 / 1) Rigid Offline Pipeline. These methods rely on essen - extractive body cue:** tial preprocessing steps, such as pretraining 3D Gaussian representation or offline compression of high-dimensional semantic features.
- **p. 1 / 1) Rigid Offline Pipeline. These methods rely on essen - extractive body cue:** However, in real-world applications, for example, robotic exploration and embodied interaction, models must support online perception.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Therefore, we propose an adaptive threshold adjustment strategy assisted by MLLM, where MLLM refers to large vision language models that support both image and text inputs. | camera/depth stream, pose, map와 language goal | p. 4 (III. OPENGS-FUSION), p. 1 (1) Rigid Offline Pipeline. These methods rely on essen) |
| State/latent | Therefore, adaptive, threshold, adjustment, strategy, assisted, MLLM, where, refers, large, vision, language | robot pose, free-space/semantic map와 local goal | p. 4 (III. OPENGS-FUSION), p. 1 (1) Rigid Offline Pipeline. These methods rely on essen), p. 1 (Abstract) |
| Output/action | However, in real-world applications, for example, robotic exploration and embodied interaction, models must support online perception. | collision-free trajectory 또는 velocity command | p. 1 (1) Rigid Offline Pipeline. These methods rely on essen), p. 1 (Abstract), p. 2 (III. OPENGS-FUSION) |
| Objective/outcome | 3) Scene Optimization Strategy: To supervise the learning of our Gaussian representation, we apply the same loss function as described in [24]. | goal reach, safety, localization error와 replanning latency | p. 4 (III. OPENGS-FUSION), p. 4 (III. OPENGS-FUSION), p. 1 (2) Limited 3D Object-Level Understanding. Most exist) |

## Main Claims and Actual Contribution

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our method enables versatile task-oriented interactions, such as 3D object extraction and editing in an interactive manner.
- **p. 2 / 2) Limited 3D Object-Level Understanding. Most exist - extractive body cue:** In summary, our contributions are as follows. • We introduce OpenGS-Fusion, an innovative openvocabulary dense mapping framework that leverages a hybrid scene representation to concurrently ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Compared to 3DGS-featurefield-based methods [12]-[15], our approach enables online modeling of scene appearance, geometry, and semantics while supporting 3D objectlevel queries.
- **p. 4 / III. OPENGS-FUSION - extractive body cue:** This approach allows our method to obtain a relatively accurate geometric representation at the initialization stage, reducing the optimization cost.
- **p. 3 / III. OPENGS-FUSION - extractive body cue:** Additionally, the proposed open-vocabulary query strategy enables precise localization of 3D objects without the need for explicit scene segmentation.
- **p. 5 / IV. EXPERIMENT - extractive body cue:** Specifically, our method outperforms the state-of-the-art 3DGS-based approach, OpenGaussian, with improvements of 9.5% (Replica) and 12.2% (ScanNet) in terms of mIoU performance, while operating in ...
- **p. 5 / IV. EXPERIMENT - extractive body cue:** Our method achieves the best performance in both open-vocabulary 3D object segmentation accuracy and training efficiency.
- **p. 6 / IV. EXPERIMENT - extractive body cue:** Our method achieves state-of-the-art performance in PSNR, SSIM, LPIPS, and Depth L1.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT) |
| Embodiment/environment | Replica ScanNet Methods mAcc↑ mIoU↑ FPS↑ mAcc↑ mIoU↑ FPS↑ ConceptFusion* 28.02 11.49 0.49 21.22 10.64 0.52 ConceptGraphs 38.21 18.16 - 44.28 23.94 - LangSplat 10.32 4.17 - 8.18 2.93 - OpenGaussian 44.28 ... | hardware/simulator version and reset protocol | p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT) |
| Dataset/benchmark | Real-World Experiments In this section, we describe the practical implementation of OpenGS-Fusion for the reconstruction and understanding of indoor scenes using a mobile robotic device. | role, split, size and leakage | p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT) |
| Metric | We aggregate these measurements into dataset-level evaluation metrics, specifically mean IoU (mIoU) and mean accuracy (mAcc). | definition, denominator, direction and uncertainty | p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT) |
| Baseline/ablation | Specifically, our method outperforms the state-of-the-art 3DGS-based approach, OpenGaussian, with improvements of 9.5% (Replica) and 12.2% (ScanNet) in terms of mIoU performance, while operating in an online setting without the need for ... | fair input/data/compute/action matching | p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 1 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 7 / V. CONCLUSIONS - extractive body cue:** However, our method currently relies on accurate pose estimation and faces limitations in query efficiency.
- **p. 7 / V. CONCLUSIONS - extractive body cue:** Future work will explore how to leverage hybrid scene representation for pose estimation and investigate lightweight MLLMs specifically designed for image retrieval tasks to further ...
- **p. 5 / IV. EXPERIMENT - extractive body cue:** OpenGaussian fails to locate both instances as they are segmented into separate entities, and the model by default only retrieves the instance that best matches ...
- **p. 6 / IV. EXPERIMENT - extractive body cue:** 5 presents qualitative rendering results in four real-world scenes, highlighting the robustness of our method against motion blur and depth noise.
- **p. 6 / IV. EXPERIMENT - extractive body cue:** We attribute this to the incorporation of our extra GS initialization and pruning mechanism, which leverages the TSDF to improve robustness when handling real-world scene ...

## Why Read It

Robotics-enabling 3D perception의 navigation 문제를 이해하기 위해 읽는다. 본문은 However, they lack the ability to synthesize novel views and struggle with high-fidelity reconstruction.를 문제로 두고, Our method enables versatile task-oriented interactions, such as 3D object extraction and editing in an interactive manner.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (2) Limited 3D Object-Level Understanding. Most exist), p. 4 (III. OPENGS-FUSION), p. 1 (1) Rigid Offline Pipeline. These methods rely on essen), p. 1 (1) Rigid Offline Pipeline. These methods rely on essen) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
