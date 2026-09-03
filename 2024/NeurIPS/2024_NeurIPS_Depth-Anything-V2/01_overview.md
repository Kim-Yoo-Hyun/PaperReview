# Depth Anything V2

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (30 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2406.09414.
> PDF retrieval source: https://arxiv.org/pdf/2406.09414. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / NeurIPS
- Authors: not duplicated here when not verified in the registry source
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: depth, 3D Vision
- Official paper: https://arxiv.org/abs/2406.09414
- Full-text retrieval: https://arxiv.org/pdf/2406.09414
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (30 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Consequently, despite the astonishing precision of Hypersim [58] or Virtual KITTI [9] (Figure 4b), we cannot expect models trained on them to generalize well in real-world scenes like "crowded people".를 문제로 두고, It consists of three steps: • train a reliable teacher model based on DINOv2-G purely on high-quality synthetic images. • produce precise pseudo depth on large-scale unlabeled real images. • train final ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** This work presents Depth Anything V2.
- **p. 1 / Abstract - extractive body cue:** Without pursuing fancy techniques, we aim to reveal crucial findings to pave the way towards building a powerful monocular depth estimation model.
- **p. 1 / Abstract - extractive body cue:** Notably, compared with V1 [89], this version produces much finer and more robust depth predictions through three key practices: 1) replacing all labeled real images ...
- **p. 1 / Abstract - extractive body cue:** Compared with the latest models [31] built on Stable Diffusion, our models are significantly more efficient (more than 10× faster) and more accurate.
- **p. 1 / Abstract - extractive body cue:** We offer models of different scales (ranging from 25M to 1.3B params) to support extensive scenarios.
- **p. 4 / 1 Introduction - extractive body cue:** Consequently, despite the astonishing precision of Hypersim [58] or Virtual KITTI [9] (Figure 4b), we cannot expect models trained on them to generalize well in ...
- **p. 7 / 1 Introduction - extractive body cue:** 6 A New Evaluation Benchmark: DA-2K 6.1 Limitations in Existing Benchmarks In Section 2, we demonstrated that commonly used real training sets have noisy depth ...

## Core Idea

- **p. 6 / 1 Introduction - extractive body cue:** It consists of three steps: • train a reliable teacher model based on DINOv2-G purely on high-quality synthetic images. • produce precise pseudo depth on ...
- **p. 7 / 1 Introduction - extractive body cue:** To address this, we introduce a second pipeline, where we carefully analyze images and manually identify challenging pairs.
- **p. 4 / 1 Introduction - extractive body cue:** In the right side of Figure 4c, we show the fine-grained prediction of a MDE model trained on synthetic images.
- **p. 3 / 1 Introduction - extractive body cue:** Black regions are ignored during training. such a challenging goal, no fancy or sophisticated techniques need to be developed.
- **p. 9 / Method - extractive body cue:** First, same as V1 [89], we follow the ZoeDepth [6] pipeline, but replace its MiDaS [7] encoder with our pre-trained encoder.
- **p. 9 / Method - extractive body cue:** Different from Depth Anything V1 [89], we further attempt to remove the synthetic images during training student models.
- **p. 8 / Method - extractive body cue:** Even our most lightweight model is superior to all other community models.
- **p. 8 / Method - extractive body cue:** Similar results (i.e., better model but worse score) are also observed in [7, 28].

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | This observation is indeed similar to SAM [33] that only releases its pseudo-labeled masks. | RGB-D, image set, point cloud, depth와 camera pose | p. 9 (Method), p. 2 (1 Introduction) |
| State/latent | observation, indeed, similar, SAM, only, releases, pseudo-labeled, masks, Precise, depth, information, favorable | geometry, map, object/relationship state | p. 9 (Method), p. 2 (1 Introduction), p. 8 (Method) |
| Output/action | Precise depth information is not only favorable in classical applications, such as 3D reconstruction [47, 32, 93], navigation [82], and autonomous driving [80], but is also preferable in modern scenarios, e.g., AI-generated ... | point map, pose, scene graph, affordance 또는 query result | p. 2 (1 Introduction), p. 8 (Method), p. 9 (Method) |
| Objective/outcome | MiDaS [56] proposes a gradient matching loss Lgm to enhance the depth sharpness. | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 14 (B.7 Benefit of gradient matching loss to fine-grained predictions), p. 14 (B.7 Benefit of gradient matching loss to fine-grained predictions), p. 8 (Method) |

## Main Claims and Actual Contribution

- **p. 6 / 1 Introduction - extractive body cue:** It consists of three steps: • train a reliable teacher model based on DINOv2-G purely on high-quality synthetic images. • produce precise pseudo depth on ...
- **p. 7 / 1 Introduction - extractive body cue:** To address this, we introduce a second pipeline, where we carefully analyze images and manually identify challenging pairs.
- **p. 4 / 1 Introduction - extractive body cue:** In the right side of Figure 4c, we show the fine-grained prediction of a MDE model trained on synthetic images.
- **p. 3 / 1 Introduction - extractive body cue:** Black regions are ignored during training. such a challenging goal, no fancy or sophisticated techniques need to be developed.
- **p. 12 / Dataset - extractive body cue:** We achieve the results without Mapillary [1] or COCO [40] pre-training. our models of various scales consistently achieve the best performance, outperforming other methods remarkably.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Depth Anything V2 significantly outperforms V1 [89] in robustness and fine-grained details. Compared with SD-based models [31, 25], it enjoys faster inference speed, ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 5: Importance of pseudo-labeled (unlabeled) real images (Du). Dl: precisely labeled synthetic images. models, e.g., Marigold [31] and Geowizard [20]. Our most capable model ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 11: Training the model solely on SA-1B for the same iterations as all sets (thus more cycles) with ViT-S. B.5 Performance on transparent or ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 12 (Dataset), p. 1 (Figure/Table caption) |
| Embodiment/environment | As shown in Table 3, on our proposed benchmark with diverse scenes, even our smallest model is significantly better than other heavy SD-based 8 | hardware/simulator version and reset protocol | p. 8 (7 Experiment), p. 8 (7 Experiment) |
| Dataset/benchmark | Encoder Dl Lu Indoor Outdoor Non-real Transparent Adverse style Aerial Underwater Object Mean ViT-S ✓ 88.1 87.8 90.8 86.9 90.6 93.8 94.9 89.9 89.8 ✓ 92.9 93.0 98.4 94.4 95.7 96.4 99.2 ... | role, split, size and leakage | p. 8 (7 Experiment), p. 8 (7 Experiment), p. 16 (C.1 Per-scenario accuracy), p. 22 (C.4 Visualization) |
| Metric | Figure 1: Depth Anything V2 significantly outperforms V1 [89] in robustness and fine-grained details. Compared with SD-based models [31, 25], it enjoys faster inference speed, fewer parameters, and higher depth accuracy. | definition, denominator, direction and uncertainty | p. 1 (Figure/Table caption), p. 16 (C.1 Per-scenario accuracy), p. 16 (C.1 Per-scenario accuracy) |
| Baseline/ablation | Figure 1: Depth Anything V2 significantly outperforms V1 [89] in robustness and fine-grained details. Compared with SD-based models [31, 25], it enjoys faster inference speed, fewer parameters, and higher depth accuracy. | fair input/data/compute/action matching | p. 1 (Figure/Table caption), p. 12 (Dataset), p. 16 (C.2 Comparison with the DIW dataset) |

## Explicit Limitations and Failure Boundary

- **p. 14 / Figure/Table caption - extractive body cue:** Table 13: Comparison among various pre-trained encoders when purely trained on synthetic images. B.7 Benefit of gradient matching loss to fine-grained predictions MiDaS [56] proposes ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 6: Failure cases of the most capable DINOv2-G model when purely trained on synthetic images. Left: the sky should be ultra far. Right: the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Zero-shot relative depth estimation. Better: AbsRel ↓, δ1 ↑. Solely from the metrics, Depth Anything V2 is better than MiDaS, but merely comparable ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 9: Our proposed evaluation benchmark DA-2K. (a) The annotation pipeline for relative depth between two points. Points are sampled based on SAM [33] mask ...
- **p. 8 / 7 Experiment - extractive body cue:** Improvement in these dimensions cannot be correctly reflected in current benchmarks.
- **p. 13 / B.4 Are such large-scale unlabeled images really necessary? - extractive body cue:** As shown in Table 11, data diversity (i.e., more datasets) is still highly important, which cannot be bridged by simply iterating a single dataset for ...
- **p. 13 / Figure/Table caption - extractive body cue:** Table 10: Transferring performance by incorporating each unlabeled dataset with ViT-S. Best, second best. B.4 Are such large-scale unlabeled images really necessary? We have proved ...

## Why Read It

Robotics-enabling 3D perception의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 Consequently, despite the astonishing precision of Hypersim [58] or Virtual KITTI [9] (Figure 4b), we cannot expect models trained on them to generalize well in real-world scenes like "crowded people".를 문제로 두고, It consists of three steps: • train a reliable teacher model based on DINOv2-G purely on high-quality synthetic images. • produce precise pseudo depth on large-scale unlabeled real images. • train final ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 4 (1 Introduction), p. 7 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction), p. 9 (Method) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
