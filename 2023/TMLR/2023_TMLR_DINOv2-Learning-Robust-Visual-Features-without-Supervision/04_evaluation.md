# Evaluation - DINOv2: Learning Robust Visual Features without Supervision

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (32 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2304.07193; PDF retrieval source: https://arxiv.org/pdf/2304.07193. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (Figure/Table caption), p. 13 (7 Results), p. 14 (7 Results), p. 14 (7 Results), p. 8 (Figure/Table caption), p. 11 (7 Results)): Figure 6: Role of resolution. Performance of ViT-L/16 trained on ImageNet-1k at fixed resolution ("224" and "416") or trained at 224 then 416 for a short duration ("224→416"). We train ...

## Evaluation Body Digest

- **p. 13 / 7 Results - extractive body cue:** This benchmark covers scenes, objects (food, cars, planes), and textures.
- **p. 13 / 7 Results - extractive body cue:** The image benchmarks contain a large quantity of fine-grained examples about objects or scenes.
- **p. 14 / 7 Results - extractive body cue:** Accuracy on 12 benchmarks covering objects, scenes and textures following the evaluation protocol proposed in Chen et al.
- **p. 14 / 7 Results - extractive body cue:** Even though these benchmarks favor text-guided pretraining, our features are still competitive with OpenCLIP on most classification benchmarks, with the exception of a few datasets, ...
- **p. 30 / B.1 Unsupervised pre-training - extractive body cue:** We report the list of datasets and associated splits used to build the dataset, how they were included (as is without retrieval or via sample-based ...
- **p. 11 / 7 Results - extractive body cue:** We detail the list of benchmarks in Appendix C.
- **p. 11 / 7 Results - extractive body cue:** We question if the ability of our models to produce high quality frozen features impact their performance when finetuned with supervision on a specific dataset.
- **p. 12 / 7 Results - extractive body cue:** We use the best performing linear classifier as described above and simply run inference on those benchmarks.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 논문이 정의한 robot/embodied environment.
- **Input boundary:** 논문이 명시한 observation과 task input.
- **Output/decision under evaluation:** paper-specific output/action.
- **Primary target:** primary task objective와 closed-loop behavior.
- **Detected evaluation headings:** 7 Results (p. 11); B Implementation Details (p. 29); B.3 Linear probing evaluation (p. 31); C List of Datasets used (p. 31).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 6: Role of resolution. Performance of ViT-L/16 trained on ImageNet-1k at fixed resolution ("224" and "416") or trained at 224 then 416 for ... | p. 10 (Figure/Table caption) |
| 7 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Interestingly, our model significantly outperforms OpenCLIP ViT-G/14 on both variants of iNaturalist (+8.6% and +9.7% for 2018 and 2021 respectively), and lags slightly behind ... | p. 13 (7 Results) |
| 7 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | We see that our features significantly outperform both SSL (+41% mAP on Oxford-Hard), and weakly-supervised (+34% mAP on Oxford-Hard) ones. | p. 14 (7 Results) |
| 7 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our model significantly outperforms state-of-the-art SSL models, with most notable differences on Stanford Cars (+14.8% versus DINO ViT-B/8) and FGVC Aircraft (+14.8% versus iBOT ... | p. 14 (7 Results) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 2: Ablation of the source of pretraining data. We compare the INet-22k dataset that was used in iBOT to our dataset, LVD-142M. Each ... | p. 8 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 13 / 7 Results - extractive body cue:** This benchmark covers scenes, objects (food, cars, planes), and textures.
- **p. 13 / 7 Results - extractive body cue:** The image benchmarks contain a large quantity of fine-grained examples about objects or scenes.
- **p. 14 / 7 Results - extractive body cue:** Accuracy on 12 benchmarks covering objects, scenes and textures following the evaluation protocol proposed in Chen et al.
- **p. 14 / 7 Results - extractive body cue:** Even though these benchmarks favor text-guided pretraining, our features are still competitive with OpenCLIP on most classification benchmarks, with the exception of a few datasets, ...
- **p. 30 / B.1 Unsupervised pre-training - extractive body cue:** We report the list of datasets and associated splits used to build the dataset, how they were included (as is without retrieval or via sample-based ...
- **p. 11 / 7 Results - extractive body cue:** We detail the list of benchmarks in Appendix C.
- **p. 11 / 7 Results - extractive body cue:** We question if the ability of our models to produce high quality frozen features impact their performance when finetuned with supervision on a specific dataset.
- **p. 12 / 7 Results - extractive body cue:** We use the best performing linear classifier as described above and simply run inference on those benchmarks.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: Visualization of the first PCA components. We compute a PCA between the patches of the images from the same column (a, b, c ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: Evolution of performance when scaling in parameters. We show performance on eight types of vision tasks, as presented in Sec. 7, and average ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Overview of our data processing pipeline. Images from curated and uncurated data sources are first mapped to embeddings. Uncurated images are then deduplicated ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Ablation study of the training differences between iBOT and DINOv2. We optimize for k-NN performance, as in our experience, the linear probe performance ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2: Ablation of the source of pretraining data. We compare the INet-22k dataset that was used in iBOT to our dataset, LVD-142M. Each model ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4: Model scale versus data scale. Evolution of performance as a function of model size for two different pretraining datasets: ImageNet-22k (14M images) and ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: (a) Effect of the KoLeo loss term. (b) Effect of the iBOT Masked Image Modeling (MIM) loss term. Evaluation performed on ImageNet-{1k,A} (classification ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 5: Effectiveness of knowledge distillation. Comparison between a ViT-L trained from scratch or distilled from DINOv2 using ViT-g/14. For reference, we also report the ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | This benchmark covers scenes, objects (food, cars, planes), and textures. | embodiment, simulator version and control stack | p. 13 (7 Results), p. 13 (7 Results) |
| Task/environment | The image benchmarks contain a large quantity of fine-grained examples about objects or scenes. | reset, timeout, object/scene variation | p. 13 (7 Results), p. 14 (7 Results) |
| Observation/sensor | 논문이 명시한 observation과 task input | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Output/decision | paper-specific output/action | action frame, controller and termination | p. 31 (B.1 Unsupervised pre-training), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 3: (a) Effect of the KoLeo loss term. (b) Effect of the iBOT Masked Image Modeling (MIM) loss term. Evaluation performed on ImageNet-{1k,A} ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Because most SSL methods were developped using ImageNet-1k validation performance as a debugging signal, we also report the top-1 accuracy on ImageNet-ReaL and ImageNet-V2. | definition/direction/unit from same section | p. 11 (7 Results) |
| We train our linear layer with SGD for 12500 iterations, using random-resized-crop data augmentation, and perform the following grid search: • learning rate in ... | definition/direction/unit from same section | p. 31 (B.3 Linear probing evaluation) |
| Figure 9: More visualization of the first PCA components. We compute the PCA between the patches from all of the images and show their ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |
| In Table 5, we show that the Top-1 accuracy on the validation set of ImageNet-1k improves by more than +2% when the backbone is ... | definition/direction/unit from same section | p. 11 (7 Results) |
| We report Top-1 accuracy on the validation set for publicly available models trained on public or private data, and with or without text supervision ... | definition/direction/unit from same section | p. 12 (7 Results) |
| We compare with the accuracy obtained with linear probing and observe only modest improvements with fine-tuning: this suggests that DINOv2 features already perform well ... | definition/direction/unit from same section | p. 12 (7 Results) |
| 7.1 We report top-1 accuracy for those three datasets in Table 7. | definition/direction/unit from same section | p. 13 (7 Results) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| When comparing with state-of-the-art SSL methods, our models shows drastically better robustness (+29.6% on A (Hendrycks et al., 2021b), +22.1% on R (Hendrycks et ... | comparison identity and matched condition | p. 12 (7 Results) |
| Our model significantly outperforms state-of-the-art SSL models, with most notable differences on Stanford Cars (+14.8% versus DINO ViT-B/8) and FGVC Aircraft (+14.8% versus iBOT ... | comparison identity and matched condition | p. 14 (7 Results) |
| In our comparisons, we use two kinds of models as baselines. | comparison identity and matched condition | p. 11 (7 Results) |
| First, we show that our self-supervised features outperform the current state of the art by a very large margin. | comparison identity and matched condition | p. 11 (7 Results) |
| Moreover, our model matches the accuracy of the OpenCLIP features on UCF and Kinetics (+0.1% and +0.5% respectively) and clearly outperforms them on SSv2 ... | comparison identity and matched condition | p. 13 (7 Results) |
| Interestingly, our model significantly outperforms OpenCLIP ViT-G/14 on both variants of iNaturalist (+8.6% and +9.7% for 2018 and 2021 respectively), and lags slightly behind ... | comparison identity and matched condition | p. 13 (7 Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 2: Ablation of the source of pretraining data. We compare the INet-22k dataset that was used in iBOT to our dataset, LVD-142M. Each ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 3: (a) Effect of the KoLeo loss term. (b) Effect of the iBOT Masked Image Modeling (MIM) loss term. Evaluation performed on ImageNet-{1k,A} ... | component/input/data sensitivity | p. 9 (Figure/Table caption) |
| Figure 1: Visualization of the first PCA components. We compute a PCA between the patches of the images from the same column (a, b, ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |
| Background is removed by removing patches with a negative score of the first PCA component. | component/input/data sensitivity | p. 18 (7 Results) |
| Table 4: Linear evaluation on ImageNet-1k of frozen pretrained features. We report Top-1 accuracy on the validation set for publicly available models trained on ... | component/input/data sensitivity | p. 12 (Figure/Table caption) |
| Table 15: Composition of our LVD-142M dataset. We report the list of datasets and associated splits used to build the dataset, how they were ... | component/input/data sensitivity | p. 30 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Most of our technical contributions are tailored toward stabilizing and accelerating discriminative self-supervised learning when scaling in model and data sizes. | Figure 6: Role of resolution. Performance of ViT-L/16 trained on ImageNet-1k at fixed resolution ("224" and "416") or trained at 224 then 416 for ... | PDF body cue; verify exact table/figure and matched conditions | p. 10 (Figure/Table caption), p. 13 (7 Results), p. 14 (7 Results), p. 14 (7 Results), p. 8 (Figure/Table caption), p. 11 (7 Results) |
| Primary metric/result | Interestingly, our model significantly outperforms OpenCLIP ViT-G/14 on both variants of iNaturalist (+8.6% and +9.7% for 2018 and 2021 respectively), and lags slightly behind ... | numeric claim only at cited anchor | p. 13 (7 Results) |

- Numeric sentences retained from the body:
- **p. 15 / 7 Results - extractive body cue:** 5, the segmentation training in this experiment took 28 hours on 16 V100 GPUs.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This procedure is extremely simple but cannot easily produce high-resolution segmentations. +ms: a boosted version of the linear setup. | p. 15 (7 Results) |
| body limitation/failure cue | This observation supports the intuition that caption-based feature learning fails to learn subtle patterns like this one. | p. 16 (7 Results) |
| body limitation/failure cue | When comparing with state-of-the-art SSL methods, our models shows drastically better robustness (+29.6% on A (Hendrycks et al., 2021b), +22.1% on R (Hendrycks et ... | p. 12 (7 Results) |
| body limitation/failure cue | Table 5: Supervised finetuning on ImageNet-1k. We use the pipeline of Touvron et al. (2022) to finetune our encoders on ImageNet-1k at resolutions 224 ... | p. 12 (Figure/Table caption) |
| body limitation/failure cue | Out-of-distribution generalization. | p. 16 (7 Results) |
| body limitation/failure cue | Figure 8: Examples of out-of-distribution examples with frozen DINOv2-g features and a linear probe. PCA of patch features. We show the results of the ... | p. 17 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All the hyperparameters are kept the same as in the first pretraining, except the base learning rate which is reduced. | p. 31 (B.2 High-Resolution adaptation) |
| Drop-rate LR Batch size DINOv2-S (distilled) ViT-S/14 0 1e-3 2048 DINOv2-B (distilled) ViT-B/14 0 1e-3 2048 DINOv2-L (distilled) ViT-L/14 0 1e-3 2048 DINOv2-L (from ... | p. 31 (B.1 Unsupervised pre-training) |
| For unsupervised pre-training we build on the DINO and iBOT codebases. | p. 29 (B.1 Unsupervised pre-training) |
| We use hyperparameters shown in Table 16, ViT architectures described in Table 17. | p. 29 (B.1 Unsupervised pre-training) |
| In order to report this additional validation performance, for all models, we run the evaluation with our code. | p. 11 (7 Results) |
| For all models, we run the linear evaluation using our code, after making sure that our numbers match those reported in technical reports and ... | p. 11 (7 Results) |
| (2022) to finetune our encoders on ImageNet-1k at resolutions 224 × 224 or 448 × 448. | p. 12 (7 Results) |
| We use the best performing linear classifier as described above and simply run inference on those benchmarks. | p. 12 (7 Results) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 15 / 7 Results - extractive body cue:** This procedure is extremely simple but cannot easily produce high-resolution segmentations. +ms: a boosted version of the linear setup.
- **p. 16 / 7 Results - extractive body cue:** This observation supports the intuition that caption-based feature learning fails to learn subtle patterns like this one.
- **p. 12 / 7 Results - extractive body cue:** When comparing with state-of-the-art SSL methods, our models shows drastically better robustness (+29.6% on A (Hendrycks et al., 2021b), +22.1% on R (Hendrycks et al., ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 5: Supervised finetuning on ImageNet-1k. We use the pipeline of Touvron et al. (2022) to finetune our encoders on ImageNet-1k at resolutions 224 × ...
- **p. 16 / 7 Results - extractive body cue:** Out-of-distribution generalization.
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 8: Examples of out-of-distribution examples with frozen DINOv2-g features and a linear probe. PCA of patch features. We show the results of the principal ...

- **Evidence anchors reviewed:** datasets p. 13 (7 Results), p. 13 (7 Results), p. 14 (7 Results), p. 14 (7 Results), p. 30 (B.1 Unsupervised pre-training), p. 11 (7 Results), metrics p. 9 (Figure/Table caption), p. 11 (7 Results), p. 31 (B.3 Linear probing evaluation), p. 18 (Figure/Table caption), p. 11 (7 Results), p. 12 (7 Results), baselines p. 12 (7 Results), p. 14 (7 Results), p. 11 (7 Results), p. 11 (7 Results), p. 13 (7 Results), p. 13 (7 Results), results p. 10 (Figure/Table caption), p. 13 (7 Results), p. 14 (7 Results), p. 14 (7 Results), p. 8 (Figure/Table caption), p. 11 (7 Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
