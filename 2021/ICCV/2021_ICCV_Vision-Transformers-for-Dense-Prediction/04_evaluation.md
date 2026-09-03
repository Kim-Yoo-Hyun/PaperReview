# Evaluation - Vision Transformers for Dense Prediction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2103.13413; PDF retrieval source: https://arxiv.org/pdf/2103.13413. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (Figure/Table caption), p. 4 (4. Experiments), p. 8 (4.3. Ablations), p. 6 (4.1. Monocular Depth Estimation), p. 7 (4.3. Ablations), p. 8 (4.3. Ablations)): Table 3. Evaluation on KITTI (Eigen split). Zero-shot cross-dataset transfer. Table 1 shows the re- sults of zero-shot transfer to different datasets that were not seen during training. We refer ...

## Evaluation Body Digest

- **p. 7 / 4.3. Ablations - extractive body cue:** We split each dataset into a training set and a small validation set of about 1,000 images total.
- **p. 5 / 4.1. Monocular Depth Estimation - extractive body cue:** To ensure that the observed improvements are not only due to the enlarged training set, we retrain the fullyconvolutional network used by MiDaS on our ...
- **p. 4 / 4. Experiments - extractive body cue:** For both tasks, we show that DPT can significantly improve accuracy when compared to convolutional networks with a similar capacity, especially if a large training ...
- **p. 4 / 4.1. Monocular Depth Estimation - extractive body cue:** We construct a meta-dataset that includes the original datasets that were used in [30] (referred to as MIX 5 in that work) and extend it ...
- **p. 5 / 4.1. Monocular Depth Estimation - extractive body cue:** We refer to this meta-dataset as MIX 6.
- **p. 6 / 4.2. Semantic Segmentation - extractive body cue:** We fine-tune DPTHybrid on the Pascal Context dataset [26] for 50 epochs.
- **p. 6 / 4.1. Monocular Depth Estimation - extractive body cue:** This indicates that DPT can also be usefully applied to smaller datasets.
- **p. 7 / 4.3. Ablations - extractive body cue:** We choose these datasets since they provide high-quality ground truth.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 4).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 3. Evaluation on KITTI (Eigen split). Zero-shot cross-dataset transfer. Table 1 shows the re- sults of zero-shot transfer to different datasets that were ... | p. 5 (Figure/Table caption) |
| 4. Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | For both tasks, we show that DPT can significantly improve accuracy when compared to convolutional networks with a similar capacity, especially if a large ... | p. 4 (4. Experiments) |
| 4.3. Ablations | EMPIRICAL / SOURCE-REPORTED EVALUATION | ViT-Base has comparable performance to ResNext101WSL, while ViT-Hybrid and ViT-Large improve performance even though they have been pretrained on significantly less data. | p. 8 (4.3. Ablations) |
| 4.1. Monocular Depth Estimation | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our architecture matches or improves state-of-the-art performance on both datasets in all metrics. | p. 6 (4.1. Monocular Depth Estimation) |
| 4.3. Ablations | EMPIRICAL / SOURCE-REPORTED EVALUATION | Best results are achieved with a combination of skip connections from shallow and deep layers. | p. 7 (4.3. Ablations) |

## Dataset / Benchmark Role

- **p. 7 / 4.3. Ablations - extractive body cue:** We split each dataset into a training set and a small validation set of about 1,000 images total.
- **p. 5 / 4.1. Monocular Depth Estimation - extractive body cue:** To ensure that the observed improvements are not only due to the enlarged training set, we retrain the fullyconvolutional network used by MiDaS on our ...
- **p. 4 / 4. Experiments - extractive body cue:** For both tasks, we show that DPT can significantly improve accuracy when compared to convolutional networks with a similar capacity, especially if a large training ...
- **p. 4 / 4.1. Monocular Depth Estimation - extractive body cue:** We construct a meta-dataset that includes the original datasets that were used in [30] (referred to as MIX 5 in that work) and extend it ...
- **p. 5 / 4.1. Monocular Depth Estimation - extractive body cue:** We refer to this meta-dataset as MIX 6.
- **p. 6 / 4.2. Semantic Segmentation - extractive body cue:** We fine-tune DPTHybrid on the Pascal Context dataset [26] for 50 epochs.
- **p. 6 / 4.1. Monocular Depth Estimation - extractive body cue:** This indicates that DPT can also be usefully applied to smaller datasets.
- **p. 7 / 4.3. Ablations - extractive body cue:** We choose these datasets since they provide high-quality ground truth.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive body cue:** Figure 1. Left: Architecture overview. The input image is transformed into tokens (orange) either by extracting non-overlapping patches followed by a linear projection of their ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. Comparison to the state of the art on monocular depth estimation. We evaluate zero-shot cross-dataset transfer according to the protocol defined in [30]. ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2. Evaluation on NYUv2 depth. δ>1.25 δ>1.252 δ>1.253 AbsRel RMSE RMSE log DORN [13]
- **p. 5 / Figure/Table caption - extractive body cue:** Table 3. Evaluation on KITTI (Eigen split). Zero-shot cross-dataset transfer. Table 1 shows the re- sults of zero-shot transfer to different datasets that were not ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2. Sample results for monocular depth estimation. Compared to the fully-convolutional network used by MiDaS, DPT shows better global coherence (e.g., sky, second row) ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Sample results for semantic segmentation on ADE20K (first and second column) and Pascal Context (third and fourth column). Predictions are frequently better aligned ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Semantic segmentation results on the ADE20K validation set. Backbone pixAcc [%] mIoU [%] OCNet HRNet-W48 [42, 50]
- **p. 7 / Figure/Table caption - extractive body cue:** Table 5. Finetuning results on the Pascal Context validation set. representation. Since the transformer backbone maintains a constant feature resolution, it is not clear at ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We split each dataset into a training set and a small validation set of about 1,000 images total. | embodiment, simulator version and control stack | p. 7 (4.3. Ablations), p. 5 (4.1. Monocular Depth Estimation) |
| Task/environment | To ensure that the observed improvements are not only due to the enlarged training set, we retrain the fullyconvolutional network used by MiDaS on ... | reset, timeout, object/scene variation | p. 5 (4.1. Monocular Depth Estimation), p. 4 (4. Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3. Architecture), p. 3 (3. Architecture) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1. Introduction), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For both tasks, we show that DPT can significantly improve accuracy when compared to convolutional networks with a similar capacity, especially if a large ... | definition/direction/unit from same section | p. 4 (4. Experiments) |
| [30] for details of the evaluation procedure and error metrics. | definition/direction/unit from same section | p. 5 (4.1. Monocular Depth Estimation) |
| We use multi-scale inference at test time and report both pixel accuracy (pixAcc) as well as mean Intersectionover-Union (mIoU). | definition/direction/unit from same section | p. 6 (4.2. Semantic Segmentation) |
| As such it provides a good trade-off between accuracy and capacity. | definition/direction/unit from same section | p. 8 (4.3. Ablations) |
| We learn a monocular depth prediction network using a scale- and shift-invariant trimmed loss that operates on an inverse depth representation, together with the ... | definition/direction/unit from same section | p. 4 (4.1. Monocular Depth Estimation) |
| Relative loss in performance for different inference resolutions (lower is better). in every layer. | definition/direction/unit from same section | p. 8 (4.3. Ablations) |
| Relative performance is computed with respect to the original MiDaS model [30]. | definition/direction/unit from same section | p. 5 (4.1. Monocular Depth Estimation) |
| We set the weight of the auxiliary loss to 0.2. | definition/direction/unit from same section | p. 6 (4.2. Semantic Segmentation) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The hybrid and large backbones consistently outperform the convolutional baselines. | comparison identity and matched condition | p. 8 (4.3. Ablations) |
| The base architecture can outperform the convolutional baseline with better pretraining (DeIT-Base-Dist). | comparison identity and matched condition | p. 8 (4.3. Ablations) |
| Figure 2. Sample results for monocular depth estimation. Compared to the fully-convolutional network used by MiDaS, DPT shows better global coherence (e.g., sky, second ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| For both tasks, we show that DPT can significantly improve accuracy when compared to convolutional networks with a similar capacity, especially if a large ... | comparison identity and matched condition | p. 4 (4. Experiments) |
| Both DPT variants significantly outperform the state of the art. | comparison identity and matched condition | p. 5 (4.1. Monocular Depth Estimation) |
| While the fully-convolutional network indeed benefits from the larger training set, we observe that both DPT variants still strongly outperform this network. | comparison identity and matched condition | p. 5 (4.1. Monocular Depth Estimation) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We first present our main results using the default configuration and show comprehensive ablations of different DPT configurations at the end of this section. | component/input/data sensitivity | p. 4 (4. Experiments) |
| We learn a monocular depth prediction network using a scale- and shift-invariant trimmed loss that operates on an inverse depth representation, together with the ... | component/input/data sensitivity | p. 4 (4.1. Monocular Depth Estimation) |
| Both DPT variants significantly outperform the state of the art. | component/input/data sensitivity | p. 5 (4.1. Monocular Depth Estimation) |
| Since the network was trained with an affine-invariant loss, its predictions are arbitrarily scaled and shifted and can have large magnitudes. | component/input/data sensitivity | p. 5 (4.1. Monocular Depth Estimation) |
| We examine a number of aspects and technical choices in DPT via ablation studies. | component/input/data sensitivity | p. 7 (4.3. Ablations) |
| We choose monocular depth estimation as the task for our ablations and follow the same protocol and hyper-parameter settings as previously described. | component/input/data sensitivity | p. 7 (4.3. Ablations) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this work, we introduce the dense prediction transformer (DPT). | Table 3. Evaluation on KITTI (Eigen split). Zero-shot cross-dataset transfer. Table 1 shows the re- sults of zero-shot transfer to different datasets that were ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (Figure/Table caption), p. 4 (4. Experiments), p. 8 (4.3. Ablations), p. 6 (4.1. Monocular Depth Estimation), p. 7 (4.3. Ablations), p. 8 (4.3. Ablations) |
| Primary metric/result | For both tasks, we show that DPT can significantly improve accuracy when compared to convolutional networks with a similar capacity, especially if a large ... | numeric claim only at cited anchor | p. 4 (4. Experiments) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Monocular Depth Estimation - extractive body cue:** We train for 60 epochs, where one epoch consists of 72,000 steps with a batch size of 16.
- **p. 5 / 4.1. Monocular Depth Estimation - extractive body cue:** Similar to [30], we first pretrain on a well-curated subset of the data [45, 46, 47] for 60 epochs before training on the full dataset. ...
- **p. 6 / 4.2. Semantic Segmentation - extractive body cue:** We train the DPT on the ADE20K semantic segmentation dataset [54] for 240 epochs.
- **p. 6 / 4.2. Semantic Segmentation - extractive body cue:** We fine-tune DPTHybrid on the Pascal Context dataset [26] for 50 epochs.
- **p. 8 / 4.3. Ablations - extractive body cue:** To test this hypothesis, we plot the loss in performance of different architectures when performing inference at resolutions higher than the training resolution of 384×384 ...
- **p. 3 / 3. Architecture - extractive body cue:** Tokens are assembled into feature maps with 1 s the spatial resolution of the input image.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We thus first align predictions of the initial network to each training sample using the robust alignment procedure described in [30]. | p. 5 (4.1. Monocular Depth Estimation) |
| body limitation/failure cue | We observe that the performance of DPT variants indeed degrades more gracefully as inference resolution increases. | p. 8 (4.3. Ablations) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We train for 60 epochs, where one epoch consists of 72,000 steps with a batch size of 16. | p. 5 (4.1. Monocular Depth Estimation) |
| We use multi-objective optimization [32] together with Adam [19] and set a learning rate of 1e-5 for the backbone and 1e-4 for the decoder ... | p. 5 (4.1. Monocular Depth Estimation) |
| We use batch normalization in the fusion layers and train with batch size 48. | p. 6 (4.2. Semantic Segmentation) |
| We use SGD with momentum 0.9 and a polynomial learning rate scheduler with decay factor 0.9. | p. 6 (4.2. Semantic Segmentation) |
| Performance of attaching skip connections to different encoder layers. | p. 7 (4.3. Ablations) |
| Convolutional architectures offer natural points of interest for passing features from the encoder to the decoder, namely before or after downsampling of the Backbone ... | p. 7 (4.3. Ablations) |
| Transformer encoders, on the other hand, have a global receptive field HRWSI BlendedMVS ReDWeb Mean ResNet50 0.0890 0.0887 0.1029 0.0935 ResNext101-WSL 0.0780 0.0751 0.0886 ... | p. 8 (4.3. Ablations) |
| We maintain the overall encoder-decoder structure that has been successful for dense prediction in the past. | p. 2 (3. Architecture) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / 4.1. Monocular Depth Estimation - extractive body cue:** We thus first align predictions of the initial network to each training sample using the robust alignment procedure described in [30].
- **p. 8 / 4.3. Ablations - extractive body cue:** We observe that the performance of DPT variants indeed degrades more gracefully as inference resolution increases.

- **Evidence anchors reviewed:** datasets p. 7 (4.3. Ablations), p. 5 (4.1. Monocular Depth Estimation), p. 4 (4. Experiments), p. 4 (4.1. Monocular Depth Estimation), p. 5 (4.1. Monocular Depth Estimation), p. 6 (4.2. Semantic Segmentation), metrics p. 4 (4. Experiments), p. 5 (4.1. Monocular Depth Estimation), p. 6 (4.2. Semantic Segmentation), p. 8 (4.3. Ablations), p. 4 (4.1. Monocular Depth Estimation), p. 8 (4.3. Ablations), baselines p. 8 (4.3. Ablations), p. 8 (4.3. Ablations), p. 6 (Figure/Table caption), p. 4 (4. Experiments), p. 5 (4.1. Monocular Depth Estimation), p. 5 (4.1. Monocular Depth Estimation), results p. 5 (Figure/Table caption), p. 4 (4. Experiments), p. 8 (4.3. Ablations), p. 6 (4.1. Monocular Depth Estimation), p. 7 (4.3. Ablations), p. 8 (4.3. Ablations).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
