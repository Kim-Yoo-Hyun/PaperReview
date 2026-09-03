# Evaluation - Emerging Properties in Self-Supervised Vision Transformers

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2104.14294; PDF retrieval source: https://arxiv.org/pdf/2104.14294. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.1. Comparing with SSL frameworks on ImageNet), p. 7 (4.2. Properties of ViT trained with SSL), p. 14 (Figure/Table caption), p. 6 (4.2. Properties of ViT trained with SSL), p. 5 (3.2. Implementation and evaluation protocols), p. 5 (3.2. Implementation and evaluation protocols)): While training a larger ViT with DINO improves the performance, reducing the size of the patches ("/8" variants) has a bigger impact on the performance.

## Evaluation Body Digest

- **p. 7 / 4.2. Properties of ViT trained with SSL - extractive body cue:** 5 that even though our training objective nor our architecture are designed for dense tasks, the performance is competitive on this benchmark.
- **p. 5 / 3.2. Implementation and evaluation protocols - extractive body cue:** We pretrain the models on the ImageNet dataset [60] without labels.
- **p. 5 / 3.2. Implementation and evaluation protocols - extractive body cue:** This evaluation protocol does not require any other hyperparameter tuning, nor data augmentation and can be run with only one pass over the downstream dataset, ...
- **p. 7 / 4.2. Properties of ViT trained with SSL - extractive body cue:** [37] and segment scenes with a nearestneighbor between consecutive frames; we thus do not train any model on top of the features, nor finetune any ...
- **p. 6 / 4.1. Comparing with SSL frameworks on ImageNet - extractive body cue:** Pretraining with DINO on a landmark dataset performs particularly well.
- **p. 6 / 4.2. Properties of ViT trained with SSL - extractive body cue:** We consider the revisited [53] Oxford and Paris image retrieval datasets [50].
- **p. 15 / Figure/Table caption - extractive body cue:** Table 14: Relation to MoCo-v2 and BYOL. We ablate the com- ponents that differ between DINO, MoCo-v2 and BYOL: the loss function (cross-entropy, CE, versus ...
- **p. 5 / 3.2. Implementation and evaluation protocols - extractive body cue:** However, both evaluations are sensitive to hyperparameters, and we observe a large variance in accuracy between runs when varying the learning rate for example.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 논문이 정의한 robot/embodied environment.
- **Input boundary:** 논문이 명시한 observation과 task input.
- **Output/decision under evaluation:** paper-specific output/action.
- **Primary target:** primary task objective와 closed-loop behavior.
- **Detected evaluation headings:** 3.2. Implementation and evaluation protocols (p. 4); 4. Main Results (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Comparing with SSL frameworks on ImageNet | EMPIRICAL / SOURCE-REPORTED EVALUATION | While training a larger ViT with DINO improves the performance, reducing the size of the patches ("/8" variants) has a bigger impact on the ... | p. 6 (4.1. Comparing with SSL frameworks on ImageNet) |
| 4.2. Properties of ViT trained with SSL | EMPIRICAL / SOURCE-REPORTED EVALUATION | Finally, self-supervised pretraining greatly improves results on ImageNet (+1-2%). | p. 7 (4.2. Properties of ViT trained with SSL) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 13: Methodology comparison for DEIT-small and ResNet-50. We report ImageNet linear and k-NN evaluations validation accuracy after 300 epochs pre-training. All numbers are ... | p. 14 (Figure/Table caption) |
| 4.2. Properties of ViT trained with SSL | EMPIRICAL / SOURCE-REPORTED EVALUATION | We observe that DINO features outperform those trained on ImageNet with labels. | p. 6 (4.2. Properties of ViT trained with SSL) |
| 3.2. Implementation and evaluation protocols | EMPIRICAL / SOURCE-REPORTED EVALUATION | The code and models to reproduce our results is publicly available. | p. 5 (3.2. Implementation and evaluation protocols) |

## Dataset / Benchmark Role

- **p. 7 / 4.2. Properties of ViT trained with SSL - extractive body cue:** 5 that even though our training objective nor our architecture are designed for dense tasks, the performance is competitive on this benchmark.
- **p. 5 / 3.2. Implementation and evaluation protocols - extractive body cue:** We pretrain the models on the ImageNet dataset [60] without labels.
- **p. 5 / 3.2. Implementation and evaluation protocols - extractive body cue:** This evaluation protocol does not require any other hyperparameter tuning, nor data augmentation and can be run with only one pass over the downstream dataset, ...
- **p. 7 / 4.2. Properties of ViT trained with SSL - extractive body cue:** [37] and segment scenes with a nearestneighbor between consecutive frames; we thus do not train any model on top of the features, nor finetune any ...
- **p. 6 / 4.1. Comparing with SSL frameworks on ImageNet - extractive body cue:** Pretraining with DINO on a landmark dataset performs particularly well.
- **p. 6 / 4.2. Properties of ViT trained with SSL - extractive body cue:** We consider the revisited [53] Oxford and Paris image retrieval datasets [50].

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Self-attention from a Vision Transformer with 8 × 8 patches trained with no supervision. We look at the self-attention of the [CLS] token ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: Self-distillation with no labels. We illustrate DINO in the case of one single pair of views (x1, x2) for simplicity. The model passes ...
- **p. 4 / Figure/Table caption - extractive body cue:** Table 1: Networks configuration. "Blocks" is the number of Transformer blocks, "dim" is channel dimension and "heads" is the number of heads in multi-head attention. ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 2: Linear and k-NN classification on ImageNet. We report top-1 accuracy for linear and k-NN evaluations on the validation set of ImageNet for different ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3: Image retrieval. We compare the performance in retrieval of off-the-shelf features pretrained with supervision or with DINO on ImageNet and Google Landmarks v2 ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 4: Copy detection. We report the mAP performance in copy detection on Copydays "strong" subset [21]. For reference, we also report the performance of ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 5: DAVIS 2017 Video object segmentation. We evaluate the quality of frozen features on video instance tracking. We report mean region similarity Jm and ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Attention maps from multiple heads. We consider the heads from the last layer of a ViT-S/8 trained with DINO and display the self-attention ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 5 that even though our training objective nor our architecture are designed for dense tasks, the performance is competitive on this benchmark. | embodiment, simulator version and control stack | p. 7 (4.2. Properties of ViT trained with SSL), p. 5 (3.2. Implementation and evaluation protocols) |
| Task/environment | We pretrain the models on the ImageNet dataset [60] without labels. | reset, timeout, object/scene variation | p. 5 (3.2. Implementation and evaluation protocols), p. 5 (3.2. Implementation and evaluation protocols) |
| Observation/sensor | 논문이 명시한 observation과 task input | calibration, preprocessing, privileged input | p. 3 (3.1. SSL with Knowledge Distillation), p. 2 (1. Introduction) |
| Output/decision | paper-specific output/action | action frame, controller and termination | p. 3 (3.1. SSL with Knowledge Distillation), p. 4 (3.1. SSL with Knowledge Distillation) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 14: Relation to MoCo-v2 and BYOL. We ablate the com- ponents that differ between DINO, MoCo-v2 and BYOL: the loss function (cross-entropy, CE, ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| However, both evaluations are sensitive to hyperparameters, and we observe a large variance in accuracy between runs when varying the learning rate for example. | definition/direction/unit from same section | p. 5 (3.2. Implementation and evaluation protocols) |
| Figure 6: Top-1 accuracy on ImageNet validation with k-NN classi- fier. (left) Comparison between the performance of the momentum teacher and the student during ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| We report top-1 accuracy for linear and k-NN evaluations on the validation set of ImageNet for different self-supervised methods. | definition/direction/unit from same section | p. 5 (3.2. Implementation and evaluation protocols) |
| We report mean region similarity Jm and mean contour-based accuracy Fm. | definition/direction/unit from same section | p. 7 (4.2. Properties of ViT trained with SSL) |
| We report the mAP performance in copy detection on Copydays "strong" subset [21]. | definition/direction/unit from same section | p. 6 (4.2. Properties of ViT trained with SSL) |
| We report the Mean Average Precision (mAP) for the Medium (M) and Hard (H) splits. | definition/direction/unit from same section | p. 6 (4.2. Properties of ViT trained with SSL) |
| Table 6: Transfer learning by finetuning pretrained models on different datasets. We report top-1 accuracy. Self-supervised pretraining with DINO transfers better than supervised pretraining. ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We observe that DINO features outperform those trained on ImageNet with labels. | comparison identity and matched condition | p. 6 (4.2. Properties of ViT trained with SSL) |
| DINO ViT features trained on GLDv2 are remarkably good, outperforming previously published methods based on off-the-shelf descriptors [68, 57]. | comparison identity and matched condition | p. 6 (4.2. Properties of ViT trained with SSL) |
| Table 13: Methodology comparison for DEIT-small and ResNet-50. We report ImageNet linear and k-NN evaluations validation accuracy after 300 epochs pre-training. All numbers are ... | comparison identity and matched condition | p. 14 (Figure/Table caption) |
| We pretrain the models on the ImageNet dataset [60] without labels. | comparison identity and matched condition | p. 5 (3.2. Implementation and evaluation protocols) |
| We consider two different settings: comparison with the same architecture and across architectures. | comparison identity and matched condition | p. 5 (4.1. Comparing with SSL frameworks on ImageNet) |
| Table 1: Networks configuration. "Blocks" is the number of Transformer blocks, "dim" is channel dimension and "heads" is the number of heads in multi-head ... | comparison identity and matched condition | p. 4 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 9: Effect of batch sizes. Top-1 with k-NN for models trained for 100 epochs without multi-crop. In Tab. 9, we study the impact ... | component/input/data sensitivity | p. 10 (Figure/Table caption) |
| We pretrain the models on the ImageNet dataset [60] without labels. | component/input/data sensitivity | p. 5 (3.2. Implementation and evaluation protocols) |
| Table 7: Important component for self-supervised ViT pre- training. Models are trained for 300 epochs with ViT-S/16. We study the different components that matter ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| We freeze the pretrain model to compute and store the features of the training data of the downstream task. | component/input/data sensitivity | p. 5 (3.2. Implementation and evaluation protocols) |
| Figure 5: Effect of Patch Size. k-NN eval- uation as a function of the throughputs for dif- ferent input patch sizes with ViT-B and ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 1: Networks configuration. "Blocks" is the number of Transformer blocks, "dim" is channel dimension and "heads" is the number of heads in multi-head ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| However, our method shares also similarities with knowledge distillation [35] and we present it under this angle. | While training a larger ViT with DINO improves the performance, reducing the size of the patches ("/8" variants) has a bigger impact on the ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.1. Comparing with SSL frameworks on ImageNet), p. 7 (4.2. Properties of ViT trained with SSL), p. 14 (Figure/Table caption), p. 6 (4.2. Properties of ViT trained with SSL), p. 5 (3.2. Implementation and evaluation protocols), p. 5 (3.2. Implementation and evaluation protocols) |
| Primary metric/result | Finally, self-supervised pretraining greatly improves results on ImageNet (+1-2%). | numeric claim only at cited anchor | p. 7 (4.2. Properties of ViT trained with SSL) |

- Numeric sentences retained from the body:
- **p. 4 / 3.2. Implementation and evaluation protocols - extractive body cue:** In this paper we typically use N = 16 ("/16") or N = 8 ("/8").
- **p. 5 / 3.2. Implementation and evaluation protocols - extractive body cue:** We train with the adamw optimizer [44] and a batch size of 1024, distributed over 16 GPUs when using ViT-S/16.
- **p. 5 / 3.2. Implementation and evaluation protocols - extractive body cue:** The learning rate is linearly ramped up during the first 10 epochs to its base value determined with the following linear scaling rule [29]: lr ...
- **p. 5 / 3.2. Implementation and evaluation protocols - extractive body cue:** The temperature τs is set to 0.1 while we use a linear warm-up for τt from 0.04 to 0.07 during the first 30 epochs.
- **p. 5 / 3.2. Implementation and evaluation protocols - extractive body cue:** The throughput (im/s) is calculated on a NVIDIA V100 GPU with 128 samples per forward.
- **p. 7 / 4.2. Properties of ViT trained with SSL - extractive body cue:** Visualizations are obtained with 480p images, resulting in sequences of 3601 tokens for ViT-S/8.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | However, the performance gain from using smaller patches comes at the expense of throughput: when using 5×5 patches, the throughput falls to 44 im/s, ... | p. 8 (9 SwAV) |
| body limitation/failure cue | Figure 9: Projection head design w/ or w/o l2-norm bottleneck. linear layers is n + 1 (n from the MLP and 1 from the ... | p. 16 (Figure/Table caption) |
| body limitation/failure cue | This evaluation protocol does not require any other hyperparameter tuning, nor data augmentation and can be run with only one pass over the downstream ... | p. 5 (3.2. Implementation and evaluation protocols) |
| body limitation/failure cue | This property emerges only when using DINO with ViT architectures, and does not appear with other existing self-supervised methods nor with a ResNet-50. | p. 6 (4.1. Comparing with SSL frameworks on ImageNet) |
| body limitation/failure cue | 4, we show that a supervised ViT does not attend well to objects in presence of clutter both qualitatively and quantitatively. | p. 7 (4.2. Properties of ViT trained with SSL) |
| body limitation/failure cue | First, we observe that in the absence of momentum, our framework does not work (row 2) and more advanced operations, SK for example, are ... | p. 8 (5.1. Importance of the Different Components) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| However, both evaluations are sensitive to hyperparameters, and we observe a large variance in accuracy between runs when varying the learning rate for example. | p. 5 (3.2. Implementation and evaluation protocols) |
| The learning rate is linearly ramped up during the first 10 epochs to its base value determined with the following linear scaling rule [29]: ... | p. 5 (3.2. Implementation and evaluation protocols) |
| We follow the implementation used in DeiT [69]. | p. 4 (3.2. Implementation and evaluation protocols) |
| In this section, we provide the implementation details to train with DINO and present the evaluation protocols used in our experiments. | p. 4 (3.2. Implementation and evaluation protocols) |
| We illustrate DINO in Figure 2 and propose a pseudo-code implementation in Algorithm 1. | p. 3 (3.1. SSL with Knowledge Distillation) |
| Nonetheless, a base ViT with 8 × 8 patches trained with DINO achieves 80.1% top-1 in linear classification and 77.4% with a k-NN classifier ... | p. 6 (4.1. Comparing with SSL frameworks on ImageNet) |
| ViT-S/16 ImNet 33.5 8.9 63.0 37.2 DINO ResNet-50 ImNet 35.4 11.1 55.9 27.5 DINO ViT-S/16 ImNet 41.8 13.7 63.1 34.4 DINO ViT-S/16 GLDv2 51.5 ... | p. 6 (4.1. Comparing with SSL frameworks on ImageNet) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 9 SwAV - extractive body cue:** However, the performance gain from using smaller patches comes at the expense of throughput: when using 5×5 patches, the throughput falls to 44 im/s, vs ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 9: Projection head design w/ or w/o l2-norm bottleneck. linear layers is n + 1 (n from the MLP and 1 from the weight ...
- **p. 5 / 3.2. Implementation and evaluation protocols - extractive body cue:** This evaluation protocol does not require any other hyperparameter tuning, nor data augmentation and can be run with only one pass over the downstream dataset, ...
- **p. 6 / 4.1. Comparing with SSL frameworks on ImageNet - extractive body cue:** This property emerges only when using DINO with ViT architectures, and does not appear with other existing self-supervised methods nor with a ResNet-50.
- **p. 7 / 4.2. Properties of ViT trained with SSL - extractive body cue:** 4, we show that a supervised ViT does not attend well to objects in presence of clutter both qualitatively and quantitatively.
- **p. 8 / 5.1. Importance of the Different Components - extractive body cue:** First, we observe that in the absence of momentum, our framework does not work (row 2) and more advanced operations, SK for example, are required ...

- **Evidence anchors reviewed:** datasets p. 7 (4.2. Properties of ViT trained with SSL), p. 5 (3.2. Implementation and evaluation protocols), p. 5 (3.2. Implementation and evaluation protocols), p. 7 (4.2. Properties of ViT trained with SSL), p. 6 (4.1. Comparing with SSL frameworks on ImageNet), p. 6 (4.2. Properties of ViT trained with SSL), metrics p. 15 (Figure/Table caption), p. 5 (3.2. Implementation and evaluation protocols), p. 9 (Figure/Table caption), p. 5 (3.2. Implementation and evaluation protocols), p. 7 (4.2. Properties of ViT trained with SSL), p. 6 (4.2. Properties of ViT trained with SSL), baselines p. 6 (4.2. Properties of ViT trained with SSL), p. 6 (4.2. Properties of ViT trained with SSL), p. 14 (Figure/Table caption), p. 5 (3.2. Implementation and evaluation protocols), p. 5 (4.1. Comparing with SSL frameworks on ImageNet), p. 4 (Figure/Table caption), results p. 6 (4.1. Comparing with SSL frameworks on ImageNet), p. 7 (4.2. Properties of ViT trained with SSL), p. 14 (Figure/Table caption), p. 6 (4.2. Properties of ViT trained with SSL), p. 5 (3.2. Implementation and evaluation protocols), p. 5 (3.2. Implementation and evaluation protocols).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
