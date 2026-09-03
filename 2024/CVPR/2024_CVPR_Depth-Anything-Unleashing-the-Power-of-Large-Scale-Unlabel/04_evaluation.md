# Evaluation - Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2401.10891; PDF retrieval source: https://arxiv.org/pdf/2401.10891. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (4.2. Zero-Shot Relative Depth Estimation), p. 5 (4.2. Zero-Shot Relative Depth Estimation), p. 8 (Figure/Table caption), p. 8 (4.6. Qualitative Results), p. 9 (9. More Qualitative Results), p. 9 (9. More Qualitative Results)): Moreover, our ViT-S model, whose scale is less than 1/10 of the MiDaS model, even outperforms MiDaS on several unseen datasets, including Sintel, DDAD, and ETH3D.

## Evaluation Body Digest

- **p. 5 / 4.2. Zero-Shot Relative Depth Estimation - extractive body cue:** Moreover, our ViT-S model, whose scale is less than 1/10 of the MiDaS model, even outperforms MiDaS on several unseen datasets, including Sintel, DDAD, and ...
- **p. 5 / 4.2. Zero-Shot Relative Depth Estimation - extractive body cue:** Therefore, we comprehensively validate the zero-shot depth estimation capability of our Depth Anything model on six representative unseen datasets: KITTI [18], NYUv2 [55], Sintel [7], ...
- **p. 8 / 4.6. Qualitative Results - extractive body cue:** We visualize our model predictions on the six unseen datasets in Figure 3.
- **p. 9 / 9. More Qualitative Results - extractive body cue:** Please refer to the following pages for comprehensive qualitative results on six unseen test sets (Figure 5 for KITTI [18], Figure 6 for NYUv2 [55], ...
- **p. 9 / 9. More Qualitative Results - extractive body cue:** Our model exhibits higher depth estimation accuracy and stronger robustness.
- **p. 5 / 4.2. Zero-Shot Relative Depth Estimation - extractive body cue:** As shown in Table 2, both with a ViT-L encoder, our Depth Anything surpasses the strongest MiDaS model tremendously across extensive scenes in terms of ...
- **p. 5 / 4.2. Zero-Shot Relative Depth Estimation - extractive body cue:** The performance advantage of these small-scale models demonstrates their great potential in computationally-constrained scenarios.
- **p. 8 / 4.6. Qualitative Results - extractive body cue:** Our model produces more accurate depth estimation than MiDaS, as well as better synthesis results.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiment (p. 5); 4.1. Implementation Details (p. 5); 4.6. Qualitative Results (p. 8); 6. More Implementation Details (p. 9); 9. More Qualitative Results (p. 9).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Zero-Shot Relative Depth Estimation | EMPIRICAL / SOURCE-REPORTED EVALUATION | Moreover, our ViT-S model, whose scale is less than 1/10 of the MiDaS model, even outperforms MiDaS on several unseen datasets, including Sintel, DDAD, ... | p. 5 (4.2. Zero-Shot Relative Depth Estimation) |
| 4.2. Zero-Shot Relative Depth Estimation | EMPIRICAL / SOURCE-REPORTED EVALUATION | For example, when tested on the well-known autonomous driving dataset DDAD [20], we improve the AbsRel (↓) from 0.251 →0.230 and improve the δ1 ... | p. 5 (4.2. Zero-Shot Relative Depth Estimation) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 10. Comparison between our trained encoder and MiDaS [5] trained encoder in terms of downstream fine-tuning performance. Better performance: AbsRel ↓, δ1 ↑, ... | p. 8 (Figure/Table caption) |
| 4.6. Qualitative Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our model produces more accurate depth estimation than MiDaS, as well as better synthesis results. | p. 8 (4.6. Qualitative Results) |
| 9. More Qualitative Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our model exhibits higher depth estimation accuracy and stronger robustness. | p. 9 (9. More Qualitative Results) |

## Dataset / Benchmark Role

- **p. 5 / 4.2. Zero-Shot Relative Depth Estimation - extractive body cue:** Moreover, our ViT-S model, whose scale is less than 1/10 of the MiDaS model, even outperforms MiDaS on several unseen datasets, including Sintel, DDAD, and ...
- **p. 5 / 4.2. Zero-Shot Relative Depth Estimation - extractive body cue:** Therefore, we comprehensively validate the zero-shot depth estimation capability of our Depth Anything model on six representative unseen datasets: KITTI [18], NYUv2 [55], Sintel [7], ...
- **p. 8 / 4.6. Qualitative Results - extractive body cue:** We visualize our model predictions on the six unseen datasets in Figure 3.
- **p. 9 / 9. More Qualitative Results - extractive body cue:** Please refer to the following pages for comprehensive qualitative results on six unseen test sets (Figure 5 for KITTI [18], Figure 6 for NYUv2 [55], ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Our model exhibits impressive generalization ability across extensive unseen scenes. Left two columns: COCO [36]. Middle two: SA-1B [27] (a hold-out unseen set). ...
- **p. 3 / Figure/Table caption - extractive body cue:** Table 1. In total, our Depth Anything is trained on 1.5M labeled images and 62M unlabeled images jointly. our easy-to-acquire and diverse unlabeled images will ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Our pipeline. Solid line: flow of labeled images, dotted line: unlabeled images. We especially highlight the value of large-scale unlabeled images. The S ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2. Zero-shot relative depth estimation. Better: AbsRel ↓, δ1 ↑. We compare with the best model from MiDaS v3.1. Note that MiDaS does not ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Fine-tuning and evaluating on NYUv2 [55] with our pre-trained MDE encoder. We highlight best, second best results, as well as most discriminative metrics. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 4. Fine-tuning and evaluating on KITTI [18] with our pre-trained MDE encoder. ∗: Reproduced by us. coder with metric depth information from NYUv2 [55] ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 5. Zero-shot metric depth estimation. The first three test sets in the header are indoor scenes, while the last two are outdoor scenes. Following ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 6. Examine the zero-shot transferring performance of each labeled training set (left) to six unseen datasets (top). Better performance: AbsRel ↓, δ1 ↑. We ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Moreover, our ViT-S model, whose scale is less than 1/10 of the MiDaS model, even outperforms MiDaS on several unseen datasets, including Sintel, DDAD, ... | embodiment, simulator version and control stack | p. 5 (4.2. Zero-Shot Relative Depth Estimation), p. 5 (4.2. Zero-Shot Relative Depth Estimation) |
| Task/environment | Therefore, we comprehensively validate the zero-shot depth estimation capability of our Depth Anything model on six representative unseen datasets: KITTI [18], NYUv2 [55], Sintel ... | reset, timeout, object/scene variation | p. 5 (4.2. Zero-Shot Relative Depth Estimation), p. 8 (4.6. Qualitative Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 8 (Method), p. 6 (4.4. Fine-tuned to Semantic Segmentation) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Our model exhibits higher depth estimation accuracy and stronger robustness. | definition/direction/unit from same section | p. 9 (9. More Qualitative Results) |
| As shown in Table 2, both with a ViT-L encoder, our Depth Anything surpasses the strongest MiDaS model tremendously across extensive scenes in terms ... | definition/direction/unit from same section | p. 5 (4.2. Zero-Shot Relative Depth Estimation) |
| The performance advantage of these small-scale models demonstrates their great potential in computationally-constrained scenarios. | definition/direction/unit from same section | p. 5 (4.2. Zero-Shot Relative Depth Estimation) |
| Our model produces more accurate depth estimation than MiDaS, as well as better synthesis results. | definition/direction/unit from same section | p. 8 (4.6. Qualitative Results) |
| For more accurate synthesis, we re-trained a better depth-conditioned ControlNet based on our Depth Anything, aiming to provide better control signals for image synthesis ... | definition/direction/unit from same section | p. 8 (4.6. Qualitative Results) |
| The brighter color denotes the closer distance. | definition/direction/unit from same section | p. 10 (9. More Qualitative Results) |
| Figure 1. Our model exhibits impressive generalization ability across extensive unseen scenes. Left two columns: COCO [36]. Middle two: SA-1B [27] (a hold-out unseen ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Table 1. In total, our Depth Anything is trained on 1.5M labeled images and 62M unlabeled images jointly. our easy-to-acquire and diverse unlabeled images ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Moreover, our ViT-S model, whose scale is less than 1/10 of the MiDaS model, even outperforms MiDaS on several unseen datasets, including Sintel, DDAD, ... | comparison identity and matched condition | p. 5 (4.2. Zero-Shot Relative Depth Estimation) |
| Table 10. Comparison between our trained encoder and MiDaS [5] trained encoder in terms of downstream fine-tuning performance. Better performance: AbsRel ↓, δ1 ↑, ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| All labeled datasets are simply combined together without re-sampling. | comparison identity and matched condition | p. 5 (4.1. Implementation Details) |
| Figure 2. Our pipeline. Solid line: flow of labeled images, dotted line: unlabeled images. We especially highlight the value of large-scale unlabeled images. The ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |
| Table 3. Fine-tuning and evaluating on NYUv2 [55] with our pre-trained MDE encoder. We highlight best, second best results, as well as most discriminative ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Table 5. Zero-shot metric depth estimation. The first three test sets in the header are indoor scenes, while the last two are outdoor scenes. ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| All labeled datasets are simply combined together without re-sampling. | component/input/data sensitivity | p. 5 (4.1. Implementation Details) |
| Table 3. Fine-tuning and evaluating on NYUv2 [55] with our pre-trained MDE encoder. We highlight best, second best results, as well as most discriminative ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Table 4. Fine-tuning and evaluating on KITTI [18] with our pre-trained MDE encoder. ∗: Reproduced by us. coder with metric depth information from NYUv2 ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Table 9. Ablation studies of: 1) challenging the student with strong perturbations (S) when learning unlabeled images, and 2) semantic constraint (Lfeat). Limited by ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| The model is trained for 160K iterations on ADE20K and 80K iterations on Cityscapes both with batch size 16, without any COCO [36] or ... | component/input/data sensitivity | p. 9 (6. More Implementation Details) |
| Table 12. Ablation studies on different values of the tolerance margin α for the feature alignment loss Lfeat. Limited by space, we only report ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| This allows our method to enjoy both the semantic-aware representation from DINOv2 and the part-level discriminative representation from depth supervision. | Moreover, our ViT-S model, whose scale is less than 1/10 of the MiDaS model, even outperforms MiDaS on several unseen datasets, including Sintel, DDAD, ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (4.2. Zero-Shot Relative Depth Estimation), p. 5 (4.2. Zero-Shot Relative Depth Estimation), p. 8 (Figure/Table caption), p. 8 (4.6. Qualitative Results), p. 9 (9. More Qualitative Results), p. 9 (9. More Qualitative Results) |
| Primary metric/result | For example, when tested on the well-known autonomous driving dataset DDAD [20], we improve the AbsRel (↓) from 0.251 →0.230 and improve the δ1 ... | numeric claim only at cited anchor | p. 5 (4.2. Zero-Shot Relative Depth Estimation) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Implementation Details - extractive body cue:** In the first stage, we train a teacher model on labeled images for 20 epochs.
- **p. 9 / 6. More Implementation Details - extractive body cue:** All images are cropped to 518×518 during training.
- **p. 9 / 6. More Implementation Details - extractive body cue:** Concretely, the training resolution is 392×518 on NYUv2 [55] and 384×768 on KITTI [18] to match the patch size of our encoder.
- **p. 9 / 6. More Implementation Details - extractive body cue:** The batch size is 16 and the model is trained for 5 epochs.
- **p. 9 / 6. More Implementation Details - extractive body cue:** The training resolution is set as 896×896 on both ADE20K [89] and Cityscapes [15].
- **p. 9 / 6. More Implementation Details - extractive body cue:** All images are cropped to 518×518 during training.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In this work, we present Depth Anything, a highly practical solution to robust monocular depth estimation. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Table 2. Zero-shot relative depth estimation. Better: AbsRel ↓, δ1 ↑. We compare with the best model from MiDaS v3.1. Note that MiDaS does ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | Figure 1. Our model exhibits impressive generalization ability across extensive unseen scenes. Left two columns: COCO [36]. Middle two: SA-1B [27] (a hold-out unseen ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Table 1. In total, our Depth Anything is trained on 1.5M labeled images and 62M unlabeled images jointly. our easy-to-acquire and diverse unlabeled images ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | Figure 2. Our pipeline. Solid line: flow of labeled images, dotted line: unlabeled images. We especially highlight the value of large-scale unlabeled images. The ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Table 8. Transferring our MDE encoder to ADE20K for semantic segmentation. We use Mask2Former as our segmentation model. since the labeled images are already ... | p. 7 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In both stages, the base learning rate of the pre-trained encoder is set as 5e-6, while the randomly initialized decoder uses a 10× larger ... | p. 5 (4.1. Implementation Details) |
| The batch size is 16 and the model is trained for 5 epochs. | p. 9 (6. More Implementation Details) |
| The encoder learning rate is set as 1/50 of the learning rate of the randomly initialized decoder, which is much smaller than the 1/10 ... | p. 9 (6. More Implementation Details) |
| We use the AdamW optimizer and decay the learning rate with a linear schedule. | p. 5 (4.1. Implementation Details) |
| In this part, we use our ViT-L encoder for fine-tuning. | p. 6 (4.3. Fine-tuned to Metric Depth Estimation) |
| Here, we examine the semantic capability of our MDE encoder. | p. 6 (4.4. Fine-tuned to Semantic Segmentation) |
| Comparison with MiDaS trained encoder in downstream tasks. | p. 7 (Method) |
| Transferring our MDE encoder to ADE20K for semantic segmentation. | p. 7 (Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive body cue:** In this work, we present Depth Anything, a highly practical solution to robust monocular depth estimation.
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2. Zero-shot relative depth estimation. Better: AbsRel ↓, δ1 ↑. We compare with the best model from MiDaS v3.1. Note that MiDaS does not ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Our model exhibits impressive generalization ability across extensive unseen scenes. Left two columns: COCO [36]. Middle two: SA-1B [27] (a hold-out unseen set). ...
- **p. 3 / Figure/Table caption - extractive body cue:** Table 1. In total, our Depth Anything is trained on 1.5M labeled images and 62M unlabeled images jointly. our easy-to-acquire and diverse unlabeled images will ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Our pipeline. Solid line: flow of labeled images, dotted line: unlabeled images. We especially highlight the value of large-scale unlabeled images. The S ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 8. Transferring our MDE encoder to ADE20K for semantic segmentation. We use Mask2Former as our segmentation model. since the labeled images are already sufficient. ...

- **Evidence anchors reviewed:** datasets p. 5 (4.2. Zero-Shot Relative Depth Estimation), p. 5 (4.2. Zero-Shot Relative Depth Estimation), p. 8 (4.6. Qualitative Results), p. 9 (9. More Qualitative Results), metrics p. 9 (9. More Qualitative Results), p. 5 (4.2. Zero-Shot Relative Depth Estimation), p. 5 (4.2. Zero-Shot Relative Depth Estimation), p. 8 (4.6. Qualitative Results), p. 8 (4.6. Qualitative Results), p. 10 (9. More Qualitative Results), baselines p. 5 (4.2. Zero-Shot Relative Depth Estimation), p. 8 (Figure/Table caption), p. 5 (4.1. Implementation Details), p. 4 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), results p. 5 (4.2. Zero-Shot Relative Depth Estimation), p. 5 (4.2. Zero-Shot Relative Depth Estimation), p. 8 (Figure/Table caption), p. 8 (4.6. Qualitative Results), p. 9 (9. More Qualitative Results), p. 9 (9. More Qualitative Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
