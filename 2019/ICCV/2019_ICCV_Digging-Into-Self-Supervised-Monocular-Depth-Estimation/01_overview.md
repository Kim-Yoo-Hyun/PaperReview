# Digging Into Self-Supervised Monocular Depth Estimation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1806.01260.
> PDF retrieval source: https://arxiv.org/pdf/1806.01260. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2019 / ICCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: 3D Vision, monocular depth, self-supervised, geometry
- Official paper: https://arxiv.org/abs/1806.01260
- Full-text retrieval: https://arxiv.org/pdf/1806.01260
- Code/Project: https://github.com/nianticlabs/monodepth2
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, collecting large and varied training datasets with accurate ground truth depth for supervised learning [55, 9] is itself a formidable challenge.를 문제로 두고, Our method succeeds here where others, and our baseline with our contributions turned off, fail. motion is observed in monocular training.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Per-pixel ground-truth depth data is challenging to acquire at scale.
- **p. 1 / Abstract - extractive body cue:** To overcome this limitation, self-supervised learning has emerged as a promising alternative for training models to perform monocular depth estimation.
- **p. 1 / Abstract - extractive body cue:** In this paper, we propose a set of improvements, which together result in both quantitatively and qualitatively improved depth maps compared to competing self-supervised methods.
- **p. 1 / Abstract - extractive body cue:** Research on self-supervised monocular training usually explores increasingly complex architectures, loss functions, and image formation models, all of which have recently helped to close the ...
- **p. 1 / Abstract - extractive body cue:** We show that a surprisingly simple model, and associated design choices, lead to superior predictions.
- **p. 1 / 1. Introduction - extractive body cue:** However, collecting large and varied training datasets with accurate ground truth depth for supervised learning [55, 9] is itself a formidable challenge.
- **p. 1 / 1. Introduction - extractive body cue:** Among the two self-supervised approaches, monocular video is an attractive alternative to stereo-based supervision, but it introduces its own set of challenges.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Our method succeeds here where others, and our baseline with our contributions turned off, fail. motion is observed in monocular training.
- **p. 1 / 1. Introduction - extractive body cue:** We propose three architectural and loss innovations that combined, lead to large improvements in monocular depth estimation when training with monocular video, stereo pairs, or ...
- **p. 4 / 3.2. Improved Self-Supervised Depth Estimation - extractive body cue:** We propose an improvement that deals with both issues Figure 5.
- **p. 4 / 3.2. Improved Self-Supervised Depth Estimation - extractive body cue:** To close this gap, we propose several improvements that significantly increase predicted depth quality, without adding additional model components that also require training (see Fig.
- **p. 5 / 3.2. Improved Self-Supervised Depth Estimation - extractive body cue:** Inspired by techniques in stereo reconstruction [56], we propose an improvement to this multi-scale formulation, where we decouple the resolutions of the disparity images and ...
- **p. 3 / 3. Method - extractive body cue:** We first review the key ideas behind self-supervised training for monocular depth estimation, and then describe our depth estimation network and joint training loss.
- **p. 5 / 3.3. Additional Considerations - extractive body cue:** Our depth estimation network is based on the general U-Net architecture [53], i.e. an encoder-decoder network, with skip connections, enabling us to represent both deep ...
- **p. 3 / 3.1. Self-Supervised Training - extractive body cue:** By constraining the network to perform image synthesis using an intermediary variable, in our case depth or disparity, we can then extract this interpretable depth ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | This typically involves training a pose estimation network that takes a finite sequence of frames as input, and outputs the corresponding camera transformations. | RGB-D, image set, point cloud, depth와 camera pose | p. 1 (1. Introduction), p. 5 (3.3. Additional Considerations) |
| State/latent | typically, involves, training, pose, estimation, network, takes, finite, sequence, frames, input, outputs | geometry, map, object/relationship state | p. 1 (1. Introduction), p. 5 (3.3. Additional Considerations), p. 1 (1. Introduction) |
| Output/action | Our models are implemented in PyTorch [46], trained for 20 epochs using Adam [26], with a batch size of 12 and an input/output resolution of 640 × 192 unless otherwise specified. | point map, pose, scene graph, affordance 또는 query result | p. 5 (3.3. Additional Considerations), p. 1 (1. Introduction), p. 3 (3. Method) |
| Objective/outcome | Multi-scale Estimation Due to the gradient locality of the bilinear sampler [21], and to prevent the training objective getting stuck in local minima, existing models use multi-scale depth prediction and image reconstruction. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.2. Improved Self-Supervised Depth Estimation), p. 3 (3.1. Self-Supervised Training), p. 3 (3.1. Self-Supervised Training) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Our method succeeds here where others, and our baseline with our contributions turned off, fail. motion is observed in monocular training.
- **p. 1 / 1. Introduction - extractive body cue:** We propose three architectural and loss innovations that combined, lead to large improvements in monocular depth estimation when training with monocular video, stereo pairs, or ...
- **p. 4 / 3.2. Improved Self-Supervised Depth Estimation - extractive body cue:** We propose an improvement that deals with both issues Figure 5.
- **p. 4 / 3.2. Improved Self-Supervised Depth Estimation - extractive body cue:** To close this gap, we propose several improvements that significantly increase predicted depth quality, without adding additional model components that also require training (see Fig.
- **p. 5 / 3.2. Improved Self-Supervised Depth Estimation - extractive body cue:** Inspired by techniques in stereo reconstruction [56], we propose an improvement to this multi-scale formulation, where we decouple the resolutions of the disparity images and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Ablation. Results for different variants of our model (Monodepth2) with monocular training on KITTI 2015 [13] using the Eigen split. (a) The baseline ...
- **p. 5 / 4. Experiments - extractive body cue:** Here, we validate that (1) our reprojection loss helps with occluded pixels compared to existing pixel-averaging, (2) our auto-masking improves results, especially when training on ...
- **p. 14 / Figure/Table caption - extractive body cue:** Table 7. We present results for all other methods for which we have obtained predictions from the authors. We use the same error metrics from ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 7 (Figure/Table caption), p. 5 (4. Experiments) |
| Embodiment/environment | KITTI Depth Prediction Benchmark We also perform experiments on the recently introduced KITTI Depth Prediction Evaluation dataset [59], which features more accurate ground truth depth, addressing quality issues with the stanType Abs ... | hardware/simulator version and reset protocol | p. 7 (4.2. Additional Datasets), p. 7 (4.2. Additional Datasets) |
| Dataset/benchmark | We evaluate our models, named Monodepth2, on the KITTI 2015 stereo dataset [13], to allow comparison with previously published monocular methods. | role, split, size and leakage | p. 7 (4.2. Additional Datasets), p. 7 (4.2. Additional Datasets), p. 5 (4. Experiments), p. 5 (4. Experiments) |
| Metric | Here, we validate that (1) our reprojection loss helps with occluded pixels compared to existing pixel-averaging, (2) our auto-masking improves results, especially when training on scenes with static cameras, and (3) our ... | definition, denominator, direction and uncertainty | p. 5 (4. Experiments), p. 12 (Figure/Table caption), p. 4 (Figure/Table caption) |
| Baseline/ablation | Figure 12. Additional Wander results. We observe that our model (Ours M) results in fewer visual artifacts when compared to the the baseline (i.e. the same model including VGG loss, but without ... | fair input/data/compute/action matching | p. 17 (Figure/Table caption), p. 7 (Figure/Table caption), p. 13 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 8. Failure cases. Top: Our self-supervised loss fails to learn good depths for distorted, reflective and color-saturated re- gions. Bottom: We can fail to ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 10. Additional Make3D results. Our model (MD2 M) trained on KITTI results in plausible depths, predicting more detail than existing monocular methods. The last ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 11. Effect of varying resolutions on the KITTI Eigen split. All predicted disparity maps have been resized to the same size for visualization. Our ...
- **p. 15 / Figure/Table caption - extractive body cue:** Table 9. KITTI depth prediction benchmark. Comparison of our monocular plus stereo approaches to fully supervised methods on the KITTI depth prediction benchmark [27]. D ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Moving objects. Monocular methods can fail to predict depth for objects that were often observed to be in motion dur- ing training e.g. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. Overview. (a) Depth network: We use a standard, fully convolutional, U-Net to predict depth. (b) Pose network: Pose between a pair of frames ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, collecting large and varied training datasets with accurate ground truth depth for supervised learning [55, 9] is itself a formidable challenge.를 문제로 두고, Our method succeeds here where others, and our baseline with our contributions turned off, fail. motion is observed in monocular training.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 3 (3. Method), p. 5 (3.3. Additional Considerations), p. 3 (3.1. Self-Supervised Training) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
