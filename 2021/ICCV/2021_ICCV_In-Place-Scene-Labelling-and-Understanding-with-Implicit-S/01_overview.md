# In-Place Scene Labelling and Understanding with Implicit Scene Representation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2103.15875.
> PDF retrieval source: https://arxiv.org/pdf/2103.15875. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2021 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: NeRF, semantic, 3D Vision, alignment
- Official paper: https://arxiv.org/abs/2103.15875
- Full-text retrieval: https://arxiv.org/pdf/2103.15875
- Code/Project: https://shuaifengzhi.com/Semantic-NeRF/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Semantic scene understanding means attaching class laFusion via Learning Label Denoising Super-Resolution Label Propagation Label Synthesis Label Interpolation Figure 1: Neural radiance fields (NeRF) jointly encoding appearance and geom ...를 문제로 두고, In addition, multi-view consistency is inherent to the training process and enables the network to produce accurate semantic labels of the scene, including for views that are substantially different from any in ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Semantic labelling is highly correlated with geometry and radiance reconstruction, as scene entities with similar shape and appearance are more likely to come from similar ...
- **p. 1 / Abstract - extractive body cue:** Recent implicit neural reconstruction techniques are appealing as they do not require prior training data, but the same fully self-supervised approach is not possible for ...
- **p. 1 / Abstract - extractive body cue:** We extend neural radiance fields (NeRF) to jointly encode semantics with appearance and geometry, so that complete and accurate 2D semantic labels can be achieved ...
- **p. 1 / Abstract - extractive body cue:** The intrinsic multi-view consistency and smoothness of NeRF benefit semantics by enabling sparse labels to efficiently propagate.
- **p. 1 / Abstract - extractive body cue:** We show the benefit of this approach when labels are either sparse or very noisy in room-scale scenes.
- **p. 1 / 1. Introduction - extractive body cue:** Semantic scene understanding means attaching class laFusion via Learning Label Denoising Super-Resolution Label Propagation Label Synthesis Label Interpolation Figure 1: Neural radiance fields (NeRF) jointly ...

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** In addition, multi-view consistency is inherent to the training process and enables the network to produce accurate semantic labels of the scene, including for views ...
- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we show how to design a scene-specific network for joint geometric and semantic prediction and train it on images from a single ...
- **p. 1 / 1. Introduction - extractive body cue:** Unlike scene geometry, however, semantic classes are a human-defined concept and it is not possible to semantically label a novel scene in a purely self-supervised ...
- **p. 2 / 3.1. Preliminaries - extractive body cue:** Specifically, σ(x) is designed to be a function of only 3D position while the radiance c(x, d) is a function of both 3D position and ...
- **p. 3 / 3.4. Implementation - extractive body cue:** Specifically, we use hierarchical volume sampling to jointly optimise coarse and fine networks, where the former provides importance sampling bias so that the latter can ...
- **p. 3 / 3.4. Implementation - extractive body cue:** A scene-specific semantic representation is obtained by training the network from scratch for each scene individually.
- **p. 4 / 3.4. Implementation - extractive body cue:** We train the neural network using the Adam optimiser [7] with a learning rate of 5e-4 for 200,000 iterations.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Given multiple images of a static scene with known camera intrinsics and extrinsics, NeRF [16] uses MLPs to implicitly represent the continuous 3D scene density σ and colour c = (r, g, ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (3.1. Preliminaries), p. 2 (1. Introduction) |
| State/latent | Given, multiple, images, static, scene, known, camera, intrinsics, extrinsics, NeRF, uses, MLPs | geometry, map, object/relationship state | p. 2 (3.1. Preliminaries), p. 2 (1. Introduction), p. 3 (3.3. Network Training) |
| Output/action | Our system takes as input a set of RGB images with associated known camera poses. | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 3 (3.3. Network Training), p. 1 (1. Introduction) |
| Objective/outcome | Ls is chosen as a multi-class cross-entropy loss to encourage the rendered semantic labels to be consistent with the provided labels, whether these are ground-truth, noisy or partial observations. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 3 (3.3. Network Training), p. 3 (3.3. Network Training) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** In addition, multi-view consistency is inherent to the training process and enables the network to produce accurate semantic labels of the scene, including for views ...
- **p. 1 / 1. Introduction - extractive body cue:** In this paper, we show how to design a scene-specific network for joint geometric and semantic prediction and train it on images from a single ...
- **p. 1 / 1. Introduction - extractive body cue:** Unlike scene geometry, however, semantic classes are a human-defined concept and it is not possible to semantically label a novel scene in a purely self-supervised ...
- **p. 2 / 3.1. Preliminaries - extractive body cue:** Specifically, σ(x) is designed to be a function of only 3D position while the radiance c(x, d) is a function of both 3D position and ...
- **p. 8 / 4.4. Semantic Fusion - extractive body cue:** Our method achieves the highest improvement across all metrics, showing the effectiveness of our joint representation in label fusion.
- **p. 4 / 4.2. Semantic Neural Radiance Fields - extractive body cue:** Note that we might expect that significant high quality semantic labelling information could feasibly improve reconstruction quality, but in this paper we are focused on ...
- **p. 7 / 4.4. Semantic Fusion - extractive body cue:** Object boundaries are gradually refined when more supervision is available and the incremental improvements from more labels tend to saturate.
- **p. 8 / 4.4. Semantic Fusion - extractive body cue:** Accurate labels can be achieved even from single-clicks, which are zoomed-in 9 times for visualisation purposes.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4.4. Semantic Fusion), p. 4 (4.2. Semantic Neural Radiance Fields) |
| Embodiment/environment | ScanNet ScanNet [3] is a large-scale real-world indoor RGB-D video dataset of 2.5M views in 1513 scenes with rich annotations including semantic segmentation, camera poses and surface reconstructions. | hardware/simulator version and reset protocol | p. 4 (4.1. Indoor Scene Datasets and Data Preparation), p. 4 (4.1. Indoor Scene Datasets and Data Preparation) |
| Dataset/benchmark | To prepare training data in Replica dataset, we render two different sequences per Replica scene to cover various parts of scenes. | role, split, size and leakage | p. 4 (4.1. Indoor Scene Datasets and Data Preparation), p. 4 (4.1. Indoor Scene Datasets and Data Preparation), p. 8 (4.4. Semantic Fusion), p. 7 (4.4. Semantic Fusion) |
| Metric | 0 20 40 60 80 100 Sparsity Ratio (%) 75 80 85 90 95 100 Segmentation Metrics (%) Total Accuracy Class Average Accuracy mIoU 12 15 20 30 57 97145 Baseline Length ... | definition, denominator, direction and uncertainty | p. 5 (4.4. Semantic Fusion), p. 8 (4.4. Semantic Fusion), p. 4 (4.4. Semantic Fusion) |
| Baseline/ablation | Our approach relying on consistency of scene representations outperforms baselines aided with depth maps. posed images. | fair input/data/compute/action matching | p. 8 (4.4. Semantic Fusion), p. 5 (4.4. Semantic Fusion), p. 5 (4.4. Semantic Fusion) |

## Explicit Limitations and Failure Boundary

- **p. 4 / 3.4. Implementation - extractive body cue:** batch size of rays is set to 1024 due to memory limitations.
- **p. 4 / 4.4. Semantic Fusion - extractive body cue:** Given multiple noisy or partial semantic labels, the network can fuse them into a joint implicit 3D space so that we can extract a denoised ...
- **p. 5 / 4.4. Semantic Fusion - extractive body cue:** Quantitative results shown in Table 1 also confirm that accurate denoised labels are obtained after training-as-fusion.
- **p. 5 / 4.4. Semantic Fusion - extractive body cue:** After training using only these noisy labels, we obtain denoised semantic labels by rendering back to the same training poses.
- **p. 6 / 4.4. Semantic Fusion - extractive body cue:** Even when 90% of all training labels are randomly corrupted, we can recover an accurate denoised semantic map.
- **p. 6 / 4.4. Semantic Fusion - extractive body cue:** From left to right are noisy training labels, denoised labels rendered from the same poses after training, and information entropy.
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 11: Pixel-wise denoising of semantic labels with 90% noise ratio.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Semantic scene understanding means attaching class laFusion via Learning Label Denoising Super-Resolution Label Propagation Label Synthesis Label Interpolation Figure 1: Neural radiance fields (NeRF) jointly encoding appearance and geom ...를 문제로 두고, In addition, multi-view consistency is inherent to the training process and enables the network to produce accurate semantic labels of the scene, including for views that are substantially different from any in ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 3 (3.4. Implementation), p. 3 (3.4. Implementation), p. 4 (3.4. Implementation), p. 8 (4.4. Semantic Fusion), p. 4 (4.2. Semantic Neural Radiance Fields) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
