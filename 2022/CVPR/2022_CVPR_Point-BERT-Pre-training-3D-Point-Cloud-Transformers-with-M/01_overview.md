# Point-BERT: Pre-training 3D Point Cloud Transformers with Masked Point Modeling

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2111.14819.
> PDF retrieval source: https://arxiv.org/pdf/2111.14819. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2022 / CVPR
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: point cloud, 3D Vision
- Official paper: https://arxiv.org/abs/2111.14819
- Full-text retrieval: https://arxiv.org/pdf/2111.14819
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (13 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, it is challenging to directly employ BERT on point clouds due to a lack of pre-existing vocabulary.를 문제로 두고, Driven by the above analysis, we present Point-BERT, a new scheme for learning point cloud Transformers.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present Point-BERT, a new paradigm for learning Transformers to generalize the concept of BERT [8] to 3D point cloud.
- **p. 1 / Abstract - extractive body cue:** Inspired by BERT, we devise a Masked Point Modeling (MPM) task to pre-train point cloud Transformers.
- **p. 1 / Abstract - extractive body cue:** Specifically, we first divide a point cloud into several local point patches, and a point cloud Tokenizer with a discrete Variational AutoEncoder (dVAE) is designed ...
- **p. 1 / Abstract - extractive body cue:** Then, we randomly mask out some patches of input point clouds and feed them into the backbone Transformers.
- **p. 1 / Abstract - extractive body cue:** The pre-training objective is to recover the original point tokens at the masked locations under the supervision of point tokens obtained by the Tokenizer.
- **p. 2 / 1. Introduction - extractive body cue:** However, it is challenging to directly employ BERT on point clouds due to a lack of pre-existing vocabulary.
- **p. 1 / 1. Introduction - extractive body cue:** The difficulty motivates a flux of research into learning from unlabelled 3D data.

## Core Idea

- **p. 2 / 1. Introduction - extractive body cue:** Driven by the above analysis, we present Point-BERT, a new scheme for learning point cloud Transformers.
- **p. 2 / 1. Introduction - extractive body cue:** We hope that our model enables reasoning the geometric relations among different patches of the point cloud, capturing meaningful geometric features for point cloud understanding.
- **p. 3 / 1. Introduction - extractive body cue:** We hope a neat and unified Transformer architecture across images and point clouds could facilitate both domains since it enables joint modeling of 2D and ...
- **p. 5 / 3.3. Masked Point Modeling - extractive body cue:** Coupling MPM objective and contrastive loss enables our Point-BERT to simultaneously capture the local geometric structures and high-level semantic patterns, which are crucial in point ...
- **p. 1 / 1. Introduction - extractive body cue:** Point-BERT is designed for pre-training of standard point cloud Transformers.
- **p. 5 / 3.3. Masked Point Modeling - extractive body cue:** With our point patch mixing technique, the optimization of contrastive loss encourages the model to pay attention to the high-level semantics of point clouds by ...
- **p. 4 / 3.3. Masked Point Modeling - extractive body cue:** Motivated by BERT [8] and BEiT [2], we extend the masked modeling strategy to point cloud learning and devise a masked point modeling (MPM) task ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Block Masking Input Masked Input Output Random Masking Input Masked Input Output Real Scans from ScanObjectNN Input Masked Input Output Input Masked Input Output Figure 2. | RGB-D, image set, point cloud, depth와 camera pose | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| State/latent | Block, Masking, Input, Masked, Output, Random, Real, Scans, ScanObjectNN, Figure, Point, Modeling | geometry, map, object/relationship state | p. 2 (1. Introduction), p. 2 (1. Introduction), p. 3 (1. Introduction) |
| Output/action | 2) Masked Point Modeling: A ‘masked point modeling' (MPM) task is performed to pre-train Transformers, which masks a portion of input point cloud and learns to reconstruct the missing point tokens at ... | point map, pose, scene graph, affordance 또는 query result | p. 2 (1. Introduction), p. 3 (1. Introduction), p. 1 (1. Introduction) |
| Objective/outcome | The pre-training objective can be formalized as maximizing the log-likelihood of the correct point tokens zi given the masked input embeddings XM: max X X∈D EM " X i∈M logP  zi/XM# ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 5 (3.3. Masked Point Modeling), p. 5 (3.3. Masked Point Modeling) |

## Main Claims and Actual Contribution

- **p. 2 / 1. Introduction - extractive body cue:** Driven by the above analysis, we present Point-BERT, a new scheme for learning point cloud Transformers.
- **p. 2 / 1. Introduction - extractive body cue:** We hope that our model enables reasoning the geometric relations among different patches of the point cloud, capturing meaningful geometric features for point cloud understanding.
- **p. 3 / 1. Introduction - extractive body cue:** We hope a neat and unified Transformer architecture across images and point clouds could facilitate both domains since it enables joint modeling of 2D and ...
- **p. 5 / 3.3. Masked Point Modeling - extractive body cue:** Coupling MPM objective and contrastive loss enables our Point-BERT to simultaneously capture the local geometric structures and high-level semantic patterns, which are crucial in point ...
- **p. 1 / 1. Introduction - extractive body cue:** Point-BERT is designed for pre-training of standard point cloud Transformers.
- **p. 8 / 4.4. Visualization - extractive body cue:** As can be seen, pre-training with our Point-BERT significantly improves the performance of baseline Transformers both in accuracy and speed on both synthetic and real-world ...
- **p. 6 / 4.2. Downstream Tasks - extractive body cue:** When we increase the density of inputs (4096), our Point-BERT achieves significantly better performance (93.4%) than that with the baseline (91.2%) and OcCo (92.2%).
- **p. 6 / 4.2. Downstream Tasks - extractive body cue:** We also observe that adding more points will not significantly improve the Transformer model without pre-training while Point-BERT models can be consistently improved by increasing ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (4.4. Visualization), p. 6 (4.2. Downstream Tasks) |
| Embodiment/environment | We compare the performance of Transformers training from scratch (blue) and pre-training with PointBERT (red) in terms of training loss and validation accuracy on synthetic and real-world object classification datasets. | hardware/simulator version and reset protocol | p. 8 (4.4. Visualization), p. 7 (4.2. Downstream Tasks) |
| Dataset/benchmark | As can be seen, pre-training with our Point-BERT significantly improves the performance of baseline Transformers both in accuracy and speed on both synthetic and real-world datasets. | role, split, size and leakage | p. 8 (4.4. Visualization), p. 7 (4.2. Downstream Tasks), p. 8 (4.4. Visualization), p. 5 (4.1. Pre-training Setups) |
| Metric | We compare the performance of Transformers training from scratch (blue) and pre-training with PointBERT (red) in terms of training loss and validation accuracy on synthetic and real-world object classification datasets. | definition, denominator, direction and uncertainty | p. 8 (4.4. Visualization), p. 6 (4.2. Downstream Tasks), p. 8 (4.4. Visualization) |
| Baseline/ablation | Additionally, we compare with a recent pre-training strategy OcCo [52] as a strong baseline of our pre-training method. | fair input/data/compute/action matching | p. 6 (4.2. Downstream Tasks), p. 6 (4.1. Pre-training Setups), p. 7 (4.2. Downstream Tasks) |

## Explicit Limitations and Failure Boundary

- **p. 5 / 4.1. Pre-training Setups - extractive body cue:** It is worth noting that the performance of dVAE is susceptible to hyper-parameters, which makes that the configurations of image-based dVAE [37] cannot be directly ...
- **p. 7 / 4.2. Downstream Tasks - extractive body cue:** Moreover, Point-BERT improves 0.69% and 0.5% mIoU over vanilla Transformers, while OcCo fails to improve baseline performance in part segmentation task.
- **p. 7 / 4.2. Downstream Tasks - extractive body cue:** While the superiority is degraded on the real-world dataset ScanObjectNN.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** Thus, randmask makes the task easier than block-mask, and further degrades the reconstruction performance.

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 However, it is challenging to directly employ BERT on point clouds due to a lack of pre-existing vocabulary.를 문제로 두고, Driven by the above analysis, we present Point-BERT, a new scheme for learning point cloud Transformers.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1. Introduction), p. 1 (1. Introduction), p. 2 (1. Introduction), p. 1 (1. Introduction), p. 3 (1. Introduction), p. 5 (3.3. Masked Point Modeling) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
