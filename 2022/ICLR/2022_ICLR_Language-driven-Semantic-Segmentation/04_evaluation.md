# Evaluation - Language-driven Semantic Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (13 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2201.03546; PDF retrieval source: https://arxiv.org/pdf/2201.03546. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS)): We notice that a consistent improvement can be achieved by adding a few regularization blocks.

## Evaluation Body Digest

- **p. 5 / 4 EXPERIMENTS - extractive PDF cue:** However, due to a lack of a standardized protocol and sufficient datasets and baselines for the zero-shot setting, we compare LSeg to zero- and few-shot ...
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** 4.3 FSS-1000 FSS-1000 (Li et al., 2020c) is a recent benchmark dataset for few-shot segmentation.
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** It contains a significant number of unseen or unannotated objects in comparison to previous datasets such as PASCAL and COCO.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** Input Image LSeg Ouput others, snowman Input Image LSeg Ouput others, magpie_bird Input Image LSeg Ouput others, wooden_spoon others, pizza others, potato_chips others, minicooper Figure ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** To test this, we train LSeg on ADE20K using the standard protocol on this dataset, where the training and test labels are fixed (that is, ...
- **p. 5 / 4 EXPERIMENTS - extractive PDF cue:** For datasets that provide a background or unknown class, we set the corresponding background label to "other".
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** We conduct experiments on the ADE20K dataset (Zhou et al., 2019), which is a standard semantic segmentation dataset that includes a diversity of images and ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Note that we train our model on the original label sets that are provided by these datasets without any preprocessing or relabeling.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | We notice that a consistent improvement can be achieved by adding a few regularization blocks. | p. 7 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | The strongest improvement is achieved by stacking two BottleneckBlocks, an addition to the architecture that incurs little overhead. | p. 7 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | We observe that using RN50×16 achieves the best performance among all text encoders and surpasses the weakest ViT-B/32 text encoder by 2.5%. | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | While LSeg in general achieves very promising results, we also observe some failure cases, as illustrated in Figure 6. | p. 9 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our model (with the same ResNet101 backbone) outperforms the zero-shot baseline by a considerable margin across folds and datasets and is even competitive with ... | p. 6 (4 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 5 / 4 EXPERIMENTS - extractive PDF cue:** However, due to a lack of a standardized protocol and sufficient datasets and baselines for the zero-shot setting, we compare LSeg to zero- and few-shot ...
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** 4.3 FSS-1000 FSS-1000 (Li et al., 2020c) is a recent benchmark dataset for few-shot segmentation.
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** It contains a significant number of unseen or unannotated objects in comparison to previous datasets such as PASCAL and COCO.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** Input Image LSeg Ouput others, snowman Input Image LSeg Ouput others, magpie_bird Input Image LSeg Ouput others, wooden_spoon others, pizza others, potato_chips others, minicooper Figure ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** To test this, we train LSeg on ADE20K using the standard protocol on this dataset, where the training and test labels are fixed (that is, ...
- **p. 5 / 4 EXPERIMENTS - extractive PDF cue:** For datasets that provide a background or unknown class, we set the corresponding background label to "other".
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** We conduct experiments on the ADE20K dataset (Zhou et al., 2019), which is a standard semantic segmentation dataset that includes a diversity of images and ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Note that we train our model on the original label sets that are provided by these datasets without any preprocessing or relabeling.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Example results. LSeg is able to handle unseen labels as well as label sets of arbitrary length and order. This enables flexible synthesis ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Overview. A text encoder embeds labels into a vector space. An image encoder extracts per-pixel embeddings from the image and correlates the feature ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Illustration of BottleneckBlock and DepthwiseBlock.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1: Comparison of mIoU and FB-IoU (higher is better) on PASCAL-5i.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2: Comparison of mIoU and FB-IoU (higher is better) on COCO-20i. to the competitive zero-shot baseline ZS3Net (Bucher et al., 2019), which adopts the ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3: Comparison of mIoU on FSS-1000. Table 3 compares our approach to state-of-the- art few-shot models. Notably, under the same ResNet101, LSeg could achieve ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4: LSeg zero-shot semantic segmentation results on unseen categories of FSS-1000 dataset. 5 EXPLORATION AND DISCUSSION 5.1
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 4: Ablation study on the depth of BottleneckBlock and DepthwiseBlock before the last layer. For both Pixel Accuracy (pixAcc) and mIoU, higher is better. ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | However, due to a lack of a standardized protocol and sufficient datasets and baselines for the zero-shot setting, we compare LSeg to zero- and ... | embodiment, simulator version and control stack | p. 5 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Task/environment | 4.3 FSS-1000 FSS-1000 (Li et al., 2020c) is a recent benchmark dataset for few-shot segmentation. | reset, timeout, object/scene variation | p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 4 (C Input Label Set), p. 1 (ABSTRACT) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Note that few-shot methods have access to more information and are thus expected to yield higher accuracy. | definition/direction/unit from same section | p. 5 (4 EXPERIMENTS) |
| The mIoU calculates the average IoU over all classes, FB-IoU computes mean value of foreground and background IoUs in fold i and ignores the ... | definition/direction/unit from same section | p. 5 (4 EXPERIMENTS) |
| Model Backbone Method 200 201 202 203 mean FB-IoU PPNet ResNet50 1-shot 28.1 30.8 29.5 27.7 29.0 - PMM 1-shot 29.3 34.8 27.1 27.3 ... | definition/direction/unit from same section | p. 6 (4 EXPERIMENTS) |
| Published as a conference paper at ICLR 2022 Model Backbone Method 50 51 52 53 mean FB-IoU OSLSM 1-shot 33.6 55.2 40.9 33.5 40.8 ... | definition/direction/unit from same section | p. 6 (4 EXPERIMENTS) |
| For both Pixel Accuracy (pixAcc) and mIoU, higher is better. | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| We find that LSeg performs competitively when using the RN50 × 16 text encoder and incurs only a negligible loss in performance when compared ... | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| We set the base learning rate to 0.004 and train the model for 240 iterations. | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| Language assistance helps boost the recognition performance on unannotated or unseen classes. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our model (with the same ResNet101 backbone) outperforms the zero-shot baseline by a considerable margin across folds and datasets and is even competitive with ... | comparison identity and matched condition | p. 6 (4 EXPERIMENTS) |
| Also, LSeg even outperforms a state-of-the-art one-shot method: 87.8 mIoU (ours) vs. | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| Model Backbone Method 200 201 202 203 mean FB-IoU PPNet ResNet50 1-shot 28.1 30.8 29.5 27.7 29.0 - PMM 1-shot 29.3 34.8 27.1 27.3 ... | comparison identity and matched condition | p. 6 (4 EXPERIMENTS) |
| However, the need for labeled samples severely restricts their flexibility compared to our approach. | comparison identity and matched condition | p. 5 (4 EXPERIMENTS) |
| However, due to a lack of a standardized protocol and sufficient datasets and baselines for the zero-shot setting, we compare LSeg to zero- and ... | comparison identity and matched condition | p. 5 (4 EXPERIMENTS) |
| Notably, under the same ResNet101, LSeg could achieve comparative results of the state-of-the-art one-shot method. | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We first conduct an ablation study on the two variants of the spatial regularization blocks for cleaning up the output. | component/input/data sensitivity | p. 7 (4 EXPERIMENTS) |
| A similar effect is shown in the second row, where LSeg successfully Method Backbone Text Encoder (fixed) embedding dimension pixAcc [%] mIoU [%] LSeg ... | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| Table 4: Ablation study on the depth of BottleneckBlock and DepthwiseBlock before the last layer. For both Pixel Accuracy (pixAcc) and mIoU, higher is ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Note that we train our model on the original label sets that are provided by these datasets without any preprocessing or relabeling. | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| Going from left to right, labels that are removed between runs are underlined, whereas labels that are added are marked in bold red. segments ... | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| Figure 1: Example results. LSeg is able to handle unseen labels as well as label sets of arbitrary length and order. This enables flexible ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our approach enables the synthesis of zero-shot semantic segmentation models on the fly. | We notice that a consistent improvement can be achieved by adding a few regularization blocks. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS) |
| Primary metric/result | The strongest improvement is achieved by stacking two BottleneckBlocks, an addition to the architecture that incurs little overhead. | numeric claim only at cited anchor | p. 7 (4 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 5 / 4 EXPERIMENTS - extractive PDF cue:** PASCAL5i is composed of 20 object classes with corresponding mask annotations and has been evenly divided into 4 folds of 5 classes each.
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** It consists of 1000 object classes with pixelwise annotated segmentation masks.
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** We use a base learning rate of 0.05 and train the model for 60 epochs.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** We follow the same training protocol as on ADE20K and train LSeg with a ViT-L/16 backbone and a ViT-B/32 text encoder for 200 epochs with ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We hope that these failure cases can inform future work, which could involve augmenting training with negative samples or building fine-grained language-driven semantic segmentation ... | p. 9 (4 EXPERIMENTS) |
| body limitation/failure cue | While LSeg in general achieves very promising results, we also observe some failure cases, as illustrated in Figure 6. | p. 9 (4 EXPERIMENTS) |
| body limitation/failure cue | Figure 1: Example results. LSeg is able to handle unseen labels as well as label sets of arbitrary length and order. This enables flexible ... | p. 2 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We follow the same training protocol as on ADE20K and train LSeg with a ViT-L/16 backbone and a ViT-B/32 text encoder for 200 epochs ... | p. 8 (4 EXPERIMENTS) |
| In addition, we also compare 2We also evaluated on a model initialized with the CLIP image encoder with the same setup and hyperparameters, but ... | p. 5 (4 EXPERIMENTS) |
| We follow their official code, training setting and training steps on the basis of their provided model pretrained on ImageNet (Deng et al., 2009). | p. 6 (4 EXPERIMENTS) |
| We train with a batch size of 6 on six Quadro RTX 6000. | p. 5 (4 EXPERIMENTS) |
| We set the base learning rate to 0.004 and train the model for 240 iterations. | p. 7 (4 EXPERIMENTS) |
| We use SGD with momentum 0.9 and a polynomial learning rate scheduler with decay rate 0.9. | p. 7 (4 EXPERIMENTS) |
| LSeg uses a text encoder to compute embeddings of descriptive input labels (e.g., "grass" or "building") together with a transformer-based image encoder that computes ... | p. 1 (ABSTRACT) |
| We conjecture that this is because of the larger size of the embedding that is provided by this encoder. | p. 8 (4 EXPERIMENTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** We hope that these failure cases can inform future work, which could involve augmenting training with negative samples or building fine-grained language-driven semantic segmentation models ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** While LSeg in general achieves very promising results, we also observe some failure cases, as illustrated in Figure 6.
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Example results. LSeg is able to handle unseen labels as well as label sets of arbitrary length and order. This enables flexible synthesis ...

- **PDF anchors reviewed:** datasets p. 5 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS), metrics p. 5 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), baselines p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), results p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
