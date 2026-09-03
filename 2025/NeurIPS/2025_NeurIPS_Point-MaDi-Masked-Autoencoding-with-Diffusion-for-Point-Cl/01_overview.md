# Point-MaDi: Masked Autoencoding with Diffusion for Point Cloud Pre-training

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (29 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=sYeE1obXGG.
> PDF retrieval source: https://papers.nips.cc/paper_files/paper/2025/file/4809dd4b628b6253d0aad0154014f7a3-Paper-Conference.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Diffusion, Generation, point cloud, 3D Vision
- Official paper: https://openreview.net/forum?id=sYeE1obXGG
- Full-text retrieval: https://papers.nips.cc/paper_files/paper/2025/file/4809dd4b628b6253d0aad0154014f7a3-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (29 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 However, unlike 2D images arranged in regular grids, point clouds lack a consistent topology, making the annotation process both expensive and labor-intensive.를 문제로 두고, Considering this, we propose Point-MaDi, a novel Point cloud Masked autoencoding Diffusion framework.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Self-supervised pre-training is essential for 3D point cloud representation learning, as annotating their irregular, topology-free structures is costly and labor-intensive.
- **p. 1 / Abstract - extractive body cue:** Masked autoencoders (MAEs) offer a promising framework but rely on explicit positional embeddings, such as patch center coordinates, which leak geometric information and limit data-driven ...
- **p. 1 / Abstract - extractive body cue:** In this work, we propose Point-MaDi, a novel Point cloud Masked autoencoding Diffusion framework for pre-training that integrates a dual-diffusion pretext task into an MAE ...
- **p. 1 / Abstract - extractive body cue:** Specifically, we introduce a center diffusion mechanism in the encoder, noising and predicting the coordinates of both visible and masked patch centers without ground-truth positional ...
- **p. 1 / Abstract - extractive body cue:** These predicted centers are processed using a transformer with self-attention and cross-attention to capture intra- and inter-patch relationships.
- **p. 1 / 1 Introduction - extractive body cue:** However, unlike 2D images arranged in regular grids, point clouds lack a consistent topology, making the annotation process both expensive and labor-intensive.
- **p. 2 / 1 Introduction - extractive body cue:** Recent studies [70, 19] have begun to address these challenges by integrating diffusion frameworks into MAEs; this structure naturally complements diffusion models: the encoder can ...

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Considering this, we propose Point-MaDi, a novel Point cloud Masked autoencoding Diffusion framework.
- **p. 1 / Abstract - extractive body cue:** Specifically, we introduce a center diffusion mechanism in the encoder, noising and predicting the coordinates of both visible and masked patch centers without ground-truth positional ...
- **p. 2 / 1 Introduction - extractive body cue:** Recent studies [70, 19] have begun to address these challenges by integrating diffusion frameworks into MAEs; this structure naturally complements diffusion models: the encoder can ...
- **p. 1 / Abstract - extractive body cue:** In the decoder, we design a conditional patch diffusion process, guided by the encoder's latent features and predicted centers to reconstruct masked patches directly from ...
- **p. 2 / 1 Introduction - extractive body cue:** This process, implemented via iterative sampling, forces the encoder to model global spatial relationships by inferring center positions from partial observations.
- **p. 3 / 1 Introduction - extractive body cue:** By integrating center diffusion for global modeling and patch diffusion for local reconstruction, Point-MaDi encourages the encoder to learn robust, context-aware representations while enabling the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | (c) Our Point-MaDi denoises noisy masked patches and reconstruct their centers. alternative, enabling the extraction of generalizable representations from unlabeled point clouds through the design of various pretext tasks, including gen ... | conditioning observation와 noisy/intermediate sample | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| State/latent | Point-MaDi, denoises, noisy, masked, patches, reconstruct, centers, alternative, enabling, extraction, generalizable, representations | latent/noise variable와 conditional distribution | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction) |
| Output/action | This process, implemented via iterative sampling, forces the encoder to model global spatial relationships by inferring center positions from partial observations. | generated sample, action chunk 또는 trajectory | p. 2 (1 Introduction), p. 1 (1 Introduction), p. 1 (Abstract) |
| Objective/outcome | Recent studies [70, 19] have begun to address these challenges by integrating diffusion frameworks into MAEs; this structure naturally complements diffusion models: the encoder can operate on partially observed data, while the ... | distribution fit, multimodality, sample quality와 latency | p. 2 (1 Introduction), p. 1 (Abstract), p. 2 (1 Introduction) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** Considering this, we propose Point-MaDi, a novel Point cloud Masked autoencoding Diffusion framework.
- **p. 1 / Abstract - extractive body cue:** Specifically, we introduce a center diffusion mechanism in the encoder, noising and predicting the coordinates of both visible and masked patch centers without ground-truth positional ...
- **p. 8 / Figure/Table caption - extractive body cue:** Tab. 2. Our Point-MaDi achieves state-of-the-art performance, with a category mIoU of 84.8% and an instance mIoU of 86.3%, improving over Point-MAE by 0.6% and ...
- **p. 7 / 4 Experiments - extractive body cue:** Our Point-MaDi achieves superior performance on all subsets, reaching 95.52%, 93.46%, and 89.52% accuracies, respectively.
- **p. 7 / 4 Experiments - extractive body cue:** While diffusion-based methods like PointDif may not consistently dominate on the relatively clean and less diverse ModelNet40 dataset, our Point-MaDi still achieves 93.8% accuracy, demonstrating ...
- **p. 9 / 4 Experiments - extractive body cue:** 4, the joint decoder achieves the best overall performance.
- **p. 9 / 4 Experiments - extractive body cue:** 5, the Rand & Block strategy achieves the best performance under the same masking ratio.
- **p. 8 / 4 Experiments - extractive body cue:** Cls. mIoU Inst. mIoU mAcc mIoU Supervised Learning Only PointNet [34] CVPR 2017 80.4 83.7 49.0 41.1 DGCNN [51] TOG 2019 82.3 85.2 - - ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 7 (4 Experiments) |
| Embodiment/environment | 4.1 Downstream tasks Linear evaluation for real-world classification. | hardware/simulator version and reset protocol | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Dataset/benchmark | To further demonstrate the scene understanding ability of the proposed method, we fine-tune our Point-MaDi on the more challenging indoor dataset ScanNetV2 [6]. | role, split, size and leakage | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments) |
| Metric | Table 9: Few-shot classification results on ModelNet40. We perform ten separate trials for each experimental setting and the mean accuracy (%) and standard deviation are reported. | definition, denominator, direction and uncertainty | p. 23 (Figure/Table caption), p. 7 (4 Experiments), p. 9 (4 Experiments) |
| Baseline/ablation | Compared to the previous Point-MAE [31], our diffusion-based Point-MaDi yields consistent improvements of 5.50%, 5.17%, and 4.34% on OBJ-BG, OBJ-ONLY, and PB-T50-RS, respectively. | fair input/data/compute/action matching | p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Comparison between different pretext tasks. (a) Masked autoencoders reconstruct masked point patches. (b) PointDif uses a conditional point generator to guide the point-to-point ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: The pipeline of our Point-MaDi framework. The encoder adopts a center diffusion process, where noise is added to the centers of both visible ...
- **p. 6 / 2 Related Work - extractive body cue:** The stop-gradient further ensures that decoder gradients do not disrupt the encoder's center diffusion task, preserving the encoder's robust feature representations.
- **p. 7 / 2 Related Work - extractive body cue:** This hybrid approach enhances the robustness and generalization of patch reconstruction, complementing the encoder's sparse center denoising objective.
- **p. 9 / 4 Experiments - extractive body cue:** It introduces more spatial diversity in corrupted regions, which encourages the model to learn more robust and generalized representations.
- **p. 9 / 4 Experiments - extractive body cue:** The Cross decoder takes T v as queries and Xm as keys and values in cross-attention, mapping noise tokens to reconstructed patches within visible context.
- **p. 27 / Figure/Table caption - extractive body cue:** Figure 3: Visualization of point cloud denoising by Point-MaDi. (a) GT Points: original point cloud on ShapeNet test split. (b) GT Centers: FPS-sampled centers. (c) ...

## Why Read It

Robotics-enabling 3D perception의 generative 문제를 이해하기 위해 읽는다. 본문은 However, unlike 2D images arranged in regular grids, point clouds lack a consistent topology, making the annotation process both expensive and labor-intensive.를 문제로 두고, Considering this, we propose Point-MaDi, a novel Point cloud Masked autoencoding Diffusion framework.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 1 (Abstract), p. 1 (Abstract) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
