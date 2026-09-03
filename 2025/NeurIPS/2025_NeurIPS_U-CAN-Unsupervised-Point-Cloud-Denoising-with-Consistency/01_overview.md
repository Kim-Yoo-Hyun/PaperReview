# U-CAN: Unsupervised Point Cloud Denoising with Consistency-Aware Noise2Noise Matching

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=hVFtXE19Me.
> PDF retrieval source: https://arxiv.org/pdf/2510.25210. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: ARCHIVE
- Tags: point cloud, 3D Vision
- Official paper: https://openreview.net/forum?id=hVFtXE19Me
- Full-text retrieval: https://arxiv.org/pdf/2510.25210
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (14 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, the current unsupervised approaches still struggle to predict를 문제로 두고, Our main contributions can be summarized as follows. • We introduce U-CAN, a novel framework for unsupervised point cloud denoising by leveraging a neural network to infer a multi-step denoising path for ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Point clouds captured by scanning sensors are often perturbed by noise, which have a highly negative impact on downstream tasks (e.g. surface reconstruction and shape ...
- **p. 1 / Abstract - extractive body cue:** Previous works mostly focus on training neural networks with noisy-clean point cloud pairs for learning denoising priors, which requires extensively manual efforts.
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce U-CAN, an Unsupervised framework for point cloud denoising with Consistency-Aware Noise2Noise matching.
- **p. 1 / Abstract - extractive body cue:** Specifically, we leverage a neural network to infer a multi-step denoising path for each point of a shape or scene with a noise to noise ...
- **p. 1 / Abstract - extractive body cue:** We achieve this by a novel loss which enables statistical reasoning on multiple noisy point cloud observations.
- **p. 1 / 1 Introduction - extractive body cue:** However, the current unsupervised approaches still struggle to predict
- **p. 2 / 1 Introduction - extractive body cue:** precise clean point cloud while keeping high-fidelity local geometries due to the lack of sufficient constraints at local-level.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Our main contributions can be summarized as follows. • We introduce U-CAN, a novel framework for unsupervised point cloud denoising by leveraging a neural network ...
- **p. 2 / 1 Introduction - extractive body cue:** In response to this challenge, we introduce a novel consistency-aware constraint that specifically targets the denoising geometric consistency.
- **p. 1 / Abstract - extractive body cue:** We achieve this by a novel loss which enables statistical reasoning on multiple noisy point cloud observations.
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce U-CAN, an Unsupervised framework for point cloud denoising with Consistency-Aware Noise2Noise matching.
- **p. 1 / Abstract - extractive body cue:** Previous works mostly focus on training neural networks with noisy-clean point cloud pairs for learning denoising priors, which requires extensively manual efforts.
- **p. 2 / 1 Introduction - extractive body cue:** This ambiguity can lead to unstable convergence due to inconsistencies in denoising results across different noisy observations.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our main contributions can be summarized as follows. • We introduce U-CAN, a novel framework for unsupervised point cloud denoising by leveraging a neural network to infer a multi-step denoising path for ... | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| State/latent | main, contributions, summarized, follows, introduce, U-CAN, novel, framework, unsupervised, point, cloud, denoising | geometry, map, object/relationship state | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract) |
| Output/action | Extensive experiments demonstrate that the proposed U-CAN outperforms state-of-the-art methods in unsupervised point cloud denoising, upsampling and image denoising, where U-CAN even achieves comparable performances with the supervised ... | point map, pose, scene graph, affordance 또는 query result | p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract) |
| Objective/outcome | Our main contributions can be summarized as follows. • We introduce U-CAN, a novel framework for unsupervised point cloud denoising by leveraging a neural network to infer a multi-step denoising path for ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** Our main contributions can be summarized as follows. • We introduce U-CAN, a novel framework for unsupervised point cloud denoising by leveraging a neural network ...
- **p. 2 / 1 Introduction - extractive body cue:** In response to this challenge, we introduce a novel consistency-aware constraint that specifically targets the denoising geometric consistency.
- **p. 1 / Abstract - extractive body cue:** We achieve this by a novel loss which enables statistical reasoning on multiple noisy point cloud observations.
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce U-CAN, an Unsupervised framework for point cloud denoising with Consistency-Aware Noise2Noise matching.
- **p. 9 / 4 Experiments - extractive body cue:** 3, where our method significantly outperforms DMR-TTD and ScoreDenoise-TTD, and also achieve better performance than the supervised method PU-Net designed for the upsampling task.
- **p. 7 / 4 Experiments - extractive body cue:** As presented, our model significantly outperforms previous unsupervised denoising methods, especially for noises with large variances, and can even rival the results of supervised methods ...
- **p. 8 / 4 Experiments - extractive body cue:** Specifically, by introducing the proposed denoising consistency constraint into ZS-N2N, we achieve significant improvements of nearly 1 dB over the baseline ZS-N2N.
- **p. 7 / 4 Experiments - extractive body cue:** In particular, at the 10K resolution and under noise levels of 2% and 3%, our method outperforms all other supervised and unsupervised methods in the ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (4 Experiments), p. 7 (4 Experiments) |
| Embodiment/environment | 4.2 Point Cloud Denoising on Scanned Data For demonstrating the capability of U-CAN to handle real-world point cloud noises, we conduct evaluations under the Paris-rue-Madame dataset [45] which is obtained from real ... | hardware/simulator version and reset protocol | p. 8 (4 Experiments), p. 6 (4 Experiments) |
| Dataset/benchmark | For evaluating in the image denoising task, we follow ZS-N2N [32] to conduct experiments under the McMaster18 dataset [22]. | role, split, size and leakage | p. 8 (4 Experiments), p. 6 (4 Experiments), p. 8 (4 Experiments), p. 6 (4 Experiments) |
| Metric | The unsupervised versions of DMR [28] and ScoreDenoise [29] which leverage the same constraint as TTD, share same limitations of TTD and presents sub-optimal performance at both low and high resolutions due ... | definition, denominator, direction and uncertainty | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments) |
| Baseline/ablation | We provide the visual comparison among the state-of-the-art supervised and unsupervised point cloud denoising methods in Fig. | fair input/data/compute/action matching | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 7 / 4 Experiments - extractive body cue:** The unsupervised versions of DMR [28] and ScoreDenoise [29] which leverage the same constraint as TTD, share same limitations of TTD and presents sub-optimal performance ...
- **p. 7 / 4 Experiments - extractive body cue:** For unsupervised denoising, the TTD [14] fails to produce high-fidelity local geometries with only the global constraints.
- **p. 9 / 4 Experiments - extractive body cue:** Note that U-CAN does not require (1) sparse-to-dense point cloud pairs and (2) clean point clouds, where the only required data is the noise point ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1: Overview of our method. (a) We design a multi-step denoising framework to gradually filter the noisy point cloud. (b) We introduce a novel ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 2: Illustrations on the effect of proposed constraint on denoising consistency. The noise errors indicate the Chamfer distance between the denoised and the clean ...
- **p. 6 / 4 Experiments - extractive body cue:** We split the dataset into training and testing sets with the same setting as ScoreDenoise [29].
- **p. 6 / 4 Experiments - extractive body cue:** For the experiments on synthetic shapes, we follow ScoreDenoise [29] to train our network on the PUNet [56] dataset.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, the current unsupervised approaches still struggle to predict를 문제로 두고, Our main contributions can be summarized as follows. • We introduce U-CAN, a novel framework for unsupervised point cloud denoising by leveraging a neural network to infer a multi-step denoising path for ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
