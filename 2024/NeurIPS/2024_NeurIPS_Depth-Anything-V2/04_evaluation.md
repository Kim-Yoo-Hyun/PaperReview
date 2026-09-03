# Evaluation - Depth Anything V2

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (30 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2406.09414; PDF retrieval source: https://arxiv.org/pdf/2406.09414. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 12 (Dataset), p. 1 (Figure/Table caption), p. 9 (Figure/Table caption), p. 13 (Figure/Table caption), p. 8 (7 Experiment), p. 4 (Figure/Table caption)): We achieve the results without Mapillary [1] or COCO [40] pre-training. our models of various scales consistently achieve the best performance, outperforming other methods remarkably.

## Evaluation Body Digest

- **p. 8 / 7 Experiment - extractive body cue:** As shown in Table 3, on our proposed benchmark with diverse scenes, even our smallest model is significantly better than other heavy SD-based 8
- **p. 8 / 7 Experiment - extractive body cue:** This version aims to produce fine-grained predictions for thin structures and robust predictions for complex scenes, transparent objects, etc..
- **p. 16 / C.1 Per-scenario accuracy - extractive body cue:** Encoder Dl Lu Indoor Outdoor Non-real Transparent Adverse style Aerial Underwater Object Mean ViT-S ✓ 88.1 87.8 90.8 86.9 90.6 93.8 94.9 89.9 89.8 ✓ ...
- **p. 22 / C.4 Visualization - extractive body cue:** From top to bottom, the highly diverse images are sampled from BDD100K [97], Google Landmarks [81], ImageNet-21K [60], LSUN [98], Objects365 [65], Open Images V7 ...
- **p. 11 / B.9 Harm of real labeled images to fine-grained predictions - extractive body cue:** 16 B.15 Qualitative results on test benchmarks . . . . . . . . . . . . . . . . . . ...
- **p. 12 / B.2 Transferring performance of each labeled dataset - extractive body cue:** We totally use five synthetic datasets to train our teacher model for pseudo labeling.
- **p. 12 / B.2 Transferring performance of each labeled dataset - extractive body cue:** Overall, each dataset has its own good properties to benefit the combined performance.
- **p. 13 / B.4 Are such large-scale unlabeled images really necessary? - extractive body cue:** To validate this, we solely use the SA-1B [33] dataset as our unlabeled source and train a model on it for the same iterations we ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 7 Experiment (p. 8); B Experiments (p. 11); B.2 Transferring performance of each labeled dataset (p. 11); B.3 Transferring performance of each unlabeled dataset (p. 11); C DA-2K Evaluation Benchmark (p. 11); C.2 Comparison with the DIW dataset (p. 11); Dataset (p. 12); B.2 Transferring performance of each labeled dataset (p. 12); B.3 Transferring performance of each unlabeled dataset (p. 13); B.14 Qualitative results of produced pseudo labels (p. 16); B.15 Qualitative results on test benchmarks (p. 16); C DA-2K Evaluation Benchmark (p. 16).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Dataset | EMPIRICAL / SOURCE-REPORTED EVALUATION | We achieve the results without Mapillary [1] or COCO [40] pre-training. our models of various scales consistently achieve the best performance, outperforming other methods ... | p. 12 (Dataset) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 1: Depth Anything V2 significantly outperforms V1 [89] in robustness and fine-grained details. Compared with SD-based models [31, 25], it enjoys faster inference ... | p. 1 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 5: Importance of pseudo-labeled (unlabeled) real images (Du). Dl: precisely labeled synthetic images. models, e.g., Marigold [31] and Geowizard [20]. Our most capable ... | p. 9 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 11: Training the model solely on SA-1B for the same iterations as all sets (thus more cycles) with ViT-S. B.5 Performance on transparent ... | p. 13 (Figure/Table caption) |
| 7 Experiment | EMPIRICAL / SOURCE-REPORTED EVALUATION | Improvement in these dimensions cannot be correctly reflected in current benchmarks. | p. 8 (7 Experiment) |

## Dataset / Benchmark Role

- **p. 8 / 7 Experiment - extractive body cue:** As shown in Table 3, on our proposed benchmark with diverse scenes, even our smallest model is significantly better than other heavy SD-based 8
- **p. 8 / 7 Experiment - extractive body cue:** This version aims to produce fine-grained predictions for thin structures and robust predictions for complex scenes, transparent objects, etc..
- **p. 16 / C.1 Per-scenario accuracy - extractive body cue:** Encoder Dl Lu Indoor Outdoor Non-real Transparent Adverse style Aerial Underwater Object Mean ViT-S ✓ 88.1 87.8 90.8 86.9 90.6 93.8 94.9 89.9 89.8 ✓ ...
- **p. 22 / C.4 Visualization - extractive body cue:** From top to bottom, the highly diverse images are sampled from BDD100K [97], Google Landmarks [81], ImageNet-21K [60], LSUN [98], Objects365 [65], Open Images V7 ...
- **p. 11 / B.9 Harm of real labeled images to fine-grained predictions - extractive body cue:** 16 B.15 Qualitative results on test benchmarks . . . . . . . . . . . . . . . . . . ...
- **p. 12 / B.2 Transferring performance of each labeled dataset - extractive body cue:** We totally use five synthetic datasets to train our teacher model for pseudo labeling.
- **p. 12 / B.2 Transferring performance of each labeled dataset - extractive body cue:** Overall, each dataset has its own good properties to benefit the combined performance.
- **p. 13 / B.4 Are such large-scale unlabeled images really necessary? - extractive body cue:** To validate this, we solely use the SA-1B [33] dataset as our unlabeled source and train a model on it for the same iterations we ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Depth Anything V2 significantly outperforms V1 [89] in robustness and fine-grained details. Compared with SD-based models [31, 25], it enjoys faster inference speed, ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: Robustness (1st row, the misleading room layout) of Depth Anything V1 and Fine-grained detail (2nd row, the thin basketball net) of Marigold. Preferable ...
- **p. 2 / Figure/Table caption - extractive body cue:** Table 1: Preferable properties of a powerful monocular depth estimation model. 1
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3: Various noise in "GT" depth labels (a: NYU-D [70], b: HRWSI [83], c: MegaDepth [37]) and prediction errors in correspondingly trained models (d). ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4: Depth labels of real images (a) and synthetic images (b), and the corresponding model predictions (c). The labels of synthetic images are highly ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5: Qualitative comparison of different vision encoders on synthetic-to-real transfer. Only DINOv2-G produces a satisfying prediction. For quantitative comparisons, please refer to Section B.6. ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 6: Failure cases of the most capable DINOv2-G model when purely trained on synthetic images. Left: the sky should be ultra far. Right: the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 7: Depth Anything V2. We first train the most capable teacher on precise synthetic images. Then, to mitigate the distribution shift and limited diversity ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | As shown in Table 3, on our proposed benchmark with diverse scenes, even our smallest model is significantly better than other heavy SD-based 8 | embodiment, simulator version and control stack | p. 8 (7 Experiment), p. 8 (7 Experiment) |
| Task/environment | This version aims to produce fine-grained predictions for thin structures and robust predictions for complex scenes, transparent objects, etc.. | reset, timeout, object/scene variation | p. 8 (7 Experiment), p. 16 (C.1 Per-scenario accuracy) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 9 (Method), p. 2 (1 Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 8 (Method), p. 9 (Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Figure 1: Depth Anything V2 significantly outperforms V1 [89] in robustness and fine-grained details. Compared with SD-based models [31, 25], it enjoys faster inference ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| We report the per-scenario accuracy on our DA-2K evaluation benchmark. | definition/direction/unit from same section | p. 16 (C.1 Per-scenario accuracy) |
| Encoder Dl Lu Indoor Outdoor Non-real Transparent Adverse style Aerial Underwater Object Mean ViT-S ✓ 88.1 87.8 90.8 86.9 90.6 93.8 94.9 89.9 89.8 ... | definition/direction/unit from same section | p. 16 (C.1 Per-scenario accuracy) |
| Figure 8: Visualization of widely adopted but indeed noisy test benchmark [70]. As highlighted, the depth of the mirror and thin structures are incorrect ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Table 5: Importance of pseudo-labeled (unlabeled) real images (Du). Dl: precisely labeled synthetic images. models, e.g., Marigold [31] and Geowizard [20]. Our most capable ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Figure 3: Various noise in "GT" depth labels (a: NYU-D [70], b: HRWSI [83], c: MegaDepth [37]) and prediction errors in correspondingly trained models ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 4: Depth labels of real images (a) and synthetic images (b), and the corresponding model predictions (c). The labels of synthetic images are ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Table 2: Zero-shot relative depth estimation. Better: AbsRel ↓, δ1 ↑. Solely from the metrics, Depth Anything V2 is better than MiDaS, but merely ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Figure 1: Depth Anything V2 significantly outperforms V1 [89] in robustness and fine-grained details. Compared with SD-based models [31, 25], it enjoys faster inference ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| We achieve the results without Mapillary [1] or COCO [40] pre-training. our models of various scales consistently achieve the best performance, outperforming other methods ... | comparison identity and matched condition | p. 12 (Dataset) |
| In comparison, our DA-2K is precise, because we exclude many hard-to-decide or controversial pairs. • (better organized) DIW randomly downloads images from Flickr, without ... | comparison identity and matched condition | p. 16 (C.2 Comparison with the DIW dataset) |
| Table 4: Fine-tuning our Depth Anything V2 pre-trained encoder to in-domain metric depth estimation, i.e., training and test images share the same domain. All ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| Compared with the DINOv2 [50] encoder, our pre-trained model acts as a much stronger initialization (0.758 vs. | comparison identity and matched condition | p. 13 (B.5 Performance on transparent or reflective surfaces) |
| 15 B.11 Qualitative comparison between Marigold and Depth Anything V2 . . . . . . . . . | comparison identity and matched condition | p. 11 (B.9 Harm of real labeled images to fine-grained predictions) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Since our model predicts affine-invariant inverse depth, for fairness, we compare with Depth Anything V1 [89] and MiDaS V3.1 [7] on five unseen test ... | component/input/data sensitivity | p. 8 (7 Experiment) |
| In comparison, our DA-2K is precise, because we exclude many hard-to-decide or controversial pairs. • (better organized) DIW randomly downloads images from Flickr, without ... | component/input/data sensitivity | p. 16 (C.2 Comparison with the DIW dataset) |
| Image Loss weight 0.5 Loss weight 2.0 Loss weight 4.0 Figure 10: Effect of the gradient matching loss Lgm in terms of fine-grained details. | component/input/data sensitivity | p. 14 (B.7 Benefit of gradient matching loss to fine-grained predictions) |
| Figure 7: Depth Anything V2. We first train the most capable teacher on precise synthetic images. Then, to mitigate the distribution shift and limited ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| We achieve the results without Mapillary [1] or COCO [40] pre-training. our models of various scales consistently achieve the best performance, outperforming other methods ... | component/input/data sensitivity | p. 12 (Dataset) |
| The success of DINOv2 further reflects the promising future of the data-driven roadmap, since it carefully collects 142M pre-training data without designing fancy algorithms ... | component/input/data sensitivity | p. 14 (B.6 Comparison among various pre-trained encoders) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| It consists of three steps: • train a reliable teacher model based on DINOv2-G purely on high-quality synthetic images. • produce precise pseudo depth ... | We achieve the results without Mapillary [1] or COCO [40] pre-training. our models of various scales consistently achieve the best performance, outperforming other methods ... | PDF body cue; verify exact table/figure and matched conditions | p. 12 (Dataset), p. 1 (Figure/Table caption), p. 9 (Figure/Table caption), p. 13 (Figure/Table caption), p. 8 (7 Experiment), p. 4 (Figure/Table caption) |
| Primary metric/result | Figure 1: Depth Anything V2 significantly outperforms V1 [89] in robustness and fine-grained details. Compared with SD-based models [31, 25], it enjoys faster inference ... | numeric claim only at cited anchor | p. 1 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 8 / 7 Experiment - extractive body cue:** All images are trained at the resolution of 518×518 by resizing the shorter size to 518 followed by a random crop.
- **p. 15 / B.8 Test-time resolution scaling up - extractive body cue:** Image 1x resolution 2x resolution 4x resolution Figure 11: Test-time resolution scaling up can further improve the prediction sharpness.
- **p. 17 / C.2 Comparison with the DIW dataset - extractive body cue:** However, considering the widespread application of MDE models in AIGC [101, 39], we provide additional non-real images, such as AI-generated images, cartoon images, etc.. • ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Table 13: Comparison among various pre-trained encoders when purely trained on synthetic images. B.7 Benefit of gradient matching loss to fine-grained predictions MiDaS [56] ... | p. 14 (Figure/Table caption) |
| body limitation/failure cue | Figure 6: Failure cases of the most capable DINOv2-G model when purely trained on synthetic images. Left: the sky should be ultra far. Right: ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | Table 2: Zero-shot relative depth estimation. Better: AbsRel ↓, δ1 ↑. Solely from the metrics, Depth Anything V2 is better than MiDaS, but merely ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Figure 9: Our proposed evaluation benchmark DA-2K. (a) The annotation pipeline for relative depth between two points. Points are sampled based on SAM [33] ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Improvement in these dimensions cannot be correctly reflected in current benchmarks. | p. 8 (7 Experiment) |
| body limitation/failure cue | As shown in Table 11, data diversity (i.e., more datasets) is still highly important, which cannot be bridged by simply iterating a single dataset ... | p. 13 (B.4 Are such large-scale unlabeled images really necessary?) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We use the Adam optimizer and set the learning rate of the encoder and the decoder as 5e-6 and 5e-5, respectively. | p. 8 (7 Experiment) |
| 7.1 Implementation details Follow Depth Anything V1 [89], we use DPT [55] as our depth decoder, built on DINOv2 encoders. | p. 8 (7 Experiment) |
| Similar to the practice in metric MDE, we further fine-tune our pre-trained encoder to downstream semantic segmentation task to especially examine its semantic awareness. | p. 11 (B.1 Fine-tuned to semantic segmentation) |
| Encoder Dl Lu Indoor Outdoor Non-real Transparent Adverse style Aerial Underwater Object Mean ViT-S ✓ 88.1 87.8 90.8 86.9 90.6 93.8 94.9 89.9 89.8 ... | p. 16 (C.1 Per-scenario accuracy) |
| All compared methods use the encoder size close to ViT-L. | p. 9 (Method) |
| First, same as V1 [89], we follow the ZoeDepth [6] pipeline, but replace its MiDaS [7] encoder with our pre-trained encoder. | p. 9 (Method) |
| Method Encoder mIoU DDP [30] Swin-S [45] 82.4 Depth Anything V2 Small 82.9 DDP [30] Swin-B [45] 82.5 Depth Anything V2 Base 83.9 Segmenter ... | p. 12 (Dataset) |
| What if we only use part of unlabeled sets and iterate the model for more epochs on it? | p. 13 (B.4 Are such large-scale unlabeled images really necessary?) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 14 / Figure/Table caption - extractive body cue:** Table 13: Comparison among various pre-trained encoders when purely trained on synthetic images. B.7 Benefit of gradient matching loss to fine-grained predictions MiDaS [56] proposes ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 6: Failure cases of the most capable DINOv2-G model when purely trained on synthetic images. Left: the sky should be ultra far. Right: the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Zero-shot relative depth estimation. Better: AbsRel ↓, δ1 ↑. Solely from the metrics, Depth Anything V2 is better than MiDaS, but merely comparable ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 9: Our proposed evaluation benchmark DA-2K. (a) The annotation pipeline for relative depth between two points. Points are sampled based on SAM [33] mask ...
- **p. 8 / 7 Experiment - extractive body cue:** Improvement in these dimensions cannot be correctly reflected in current benchmarks.
- **p. 13 / B.4 Are such large-scale unlabeled images really necessary? - extractive body cue:** As shown in Table 11, data diversity (i.e., more datasets) is still highly important, which cannot be bridged by simply iterating a single dataset for ...

- **Evidence anchors reviewed:** datasets p. 8 (7 Experiment), p. 8 (7 Experiment), p. 16 (C.1 Per-scenario accuracy), p. 22 (C.4 Visualization), p. 11 (B.9 Harm of real labeled images to fine-grained predictions), p. 12 (B.2 Transferring performance of each labeled dataset), metrics p. 1 (Figure/Table caption), p. 16 (C.1 Per-scenario accuracy), p. 16 (C.1 Per-scenario accuracy), p. 7 (Figure/Table caption), p. 9 (Figure/Table caption), p. 3 (Figure/Table caption), baselines p. 1 (Figure/Table caption), p. 12 (Dataset), p. 16 (C.2 Comparison with the DIW dataset), p. 9 (Figure/Table caption), p. 13 (B.5 Performance on transparent or reflective surfaces), p. 11 (B.9 Harm of real labeled images to fine-grained predictions), results p. 12 (Dataset), p. 1 (Figure/Table caption), p. 9 (Figure/Table caption), p. 13 (Figure/Table caption), p. 8 (7 Experiment), p. 4 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
