# Evaluation - An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (22 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2010.11929; PDF retrieval source: https://arxiv.org/pdf/2010.11929. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 5 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 15 (Figure/Table caption), p. 16 (Figure/Table caption)): Figure 5: Performance versus pre-training compute for different architectures: Vision Transformers, ResNets, and hybrids. Vision Transformers generally outperform ResNets with the same compu- tational budget. Hybrids improve upon pure T ...

## Evaluation Body Digest

- **p. 4 / 4 EXPERIMENTS - extractive PDF cue:** We transfer the models trained on these dataset to several benchmark tasks: ImageNet on the original validation labels and the cleaned-up ReaL labels (Beyer et ...
- **p. 4 / 4 EXPERIMENTS - extractive PDF cue:** To understand the data requirements of each model, we pre-train on datasets of varying size and evaluate many benchmark tasks.
- **p. 5 / 4 EXPERIMENTS - extractive PDF cue:** The smaller ViT-L/16 model pre-trained on JFT-300M outperforms BiT-L (which is pre-trained on the same dataset) on all tasks, while requiring substantially less computational resources ...
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2021 Ours-JFT Ours-JFT Ours-I21k BiT-L Noisy Student (ViT-H/14) (ViT-L/16) (ViT-L/16) (ResNet152x4) (EfficientNet-L2) ImageNet 88.55 ± 0.04 87.76 ± ...
- **p. 5 / 4 EXPERIMENTS - extractive PDF cue:** We report results on downstream datasets either through few-shot or fine-tuning accuracy.
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** With fewer inductive biases for vision than ResNets, how crucial is the dataset size?
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** Similarly, larger ViT variants overtake smaller ones as the dataset grows.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** While large ViT models perform worse than BiT ResNets (shaded area) when pre-trained on small datasets, they shine when pre-trained on larger datasets.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 논문이 정의한 robot/embodied environment.
- **Input boundary:** 논문이 명시한 observation과 task input.
- **Output/decision under evaluation:** paper-specific output/action.
- **Primary target:** primary task objective와 closed-loop behavior.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 4); B EXPERIMENT DETAILS (p. 13); C ADDITIONAL RESULTS (p. 14).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 5: Performance versus pre-training compute for different architectures: Vision Transformers, ResNets, and hybrids. Vision Transformers generally outperform ResNets with the same compu- tational ... | p. 7 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 2: Comparison with state of the art on popular image classification benchmarks. We re- port mean and standard deviation of the accuracies, averaged ... | p. 6 (Figure/Table caption) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | The larger model, ViT-H/14, further improves the performance, especially on the more challenging datasets - ImageNet, CIFAR-100, and the VTAB suite. | p. 5 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | This is because the resolution increase during fine-tuning improves the performance. | p. 6 (4 EXPERIMENTS) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 5: Top1 accuracy (in %) of Vision Transformer on various datasets when pre-trained on Im- ageNet, ImageNet-21k or JFT300M. These values correspond to ... | p. 15 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 4 / 4 EXPERIMENTS - extractive PDF cue:** We transfer the models trained on these dataset to several benchmark tasks: ImageNet on the original validation labels and the cleaned-up ReaL labels (Beyer et ...
- **p. 4 / 4 EXPERIMENTS - extractive PDF cue:** To understand the data requirements of each model, we pre-train on datasets of varying size and evaluate many benchmark tasks.
- **p. 5 / 4 EXPERIMENTS - extractive PDF cue:** The smaller ViT-L/16 model pre-trained on JFT-300M outperforms BiT-L (which is pre-trained on the same dataset) on all tasks, while requiring substantially less computational resources ...
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2021 Ours-JFT Ours-JFT Ours-I21k BiT-L Noisy Student (ViT-H/14) (ViT-L/16) (ViT-L/16) (ResNet152x4) (EfficientNet-L2) ImageNet 88.55 ± 0.04 87.76 ± ...
- **p. 5 / 4 EXPERIMENTS - extractive PDF cue:** We report results on downstream datasets either through few-shot or fine-tuning accuracy.
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** With fewer inductive biases for vision than ResNets, how crucial is the dataset size?
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** Similarly, larger ViT variants overtake smaller ones as the dataset grows.
- **p. 7 / 4 EXPERIMENTS - extractive PDF cue:** While large ViT models perform worse than BiT ResNets (shaded area) when pre-trained on small datasets, they shine when pre-trained on larger datasets.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 1: Model overview. We split an image into fixed-size patches, linearly embed each of them, add position embeddings, and feed the resulting sequence of ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Table 1: Details of Vision Transformer model variants. We also evaluate on the 19-task VTAB classification suite (Zhai et al., 2019b). VTAB evaluates low-data transfer ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2: Comparison with state of the art on popular image classification benchmarks. We re- port mean and standard deviation of the accuracies, averaged over ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 2: Breakdown of VTAB performance in Natural, Specialized, and Structured task groups. model still took substantially less compute to pre-train than prior state of ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3: Transfer to ImageNet. While large ViT models perform worse than BiT ResNets (shaded area) when pre-trained on small datasets, they shine when pre-trained ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4: Linear few-shot evaluation on Ima- geNet versus pre-training size. ResNets per- form better with smaller pre-training datasets but plateau sooner than ViT, which ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5: Performance versus pre-training compute for different architectures: Vision Transformers, ResNets, and hybrids. Vision Transformers generally outperform ResNets with the same compu- tational budget. ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 6: Representative ex- amples of attention from the output token to the input space. See Appendix D.7 for details. To begin to understand how ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We transfer the models trained on these dataset to several benchmark tasks: ImageNet on the original validation labels and the cleaned-up ReaL labels (Beyer ... | embodiment, simulator version and control stack | p. 4 (4 EXPERIMENTS), p. 4 (4 EXPERIMENTS) |
| Task/environment | To understand the data requirements of each model, we pre-train on datasets of varying size and evaluate many benchmark tasks. | reset, timeout, object/scene variation | p. 4 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS) |
| Observation/sensor | 논문이 명시한 observation과 task input | calibration, preprocessing, privileged input | p. 3 (3 METHOD), p. 3 (3 METHOD) |
| Output/decision | paper-specific output/action | action frame, controller and termination | p. 4 (3 METHOD), p. 4 (3 METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| VTAB (19 tasks) 65 70 75 80 Accuracy [%] Natural (7 tasks) 70 80 90 Specialized (4 tasks) 80 82 85 88 90 Structured ... | definition/direction/unit from same section | p. 6 (4 EXPERIMENTS) |
| Figure 13: Performance of Axial-Attention based models, in terms of top-1 accuracy on ImageNet 5-shot linear, versus their speed in terms of number of ... | definition/direction/unit from same section | p. 20 (Figure/Table caption) |
| We report results on downstream datasets either through few-shot or fine-tuning accuracy. | definition/direction/unit from same section | p. 5 (4 EXPERIMENTS) |
| Published as a conference paper at ICLR 2021 ImageNet ImageNet-21k JFT-300M Pre-training dataset 70 75 80 85 90 ImageNet Top1 Accuracy [%] BiT ViT-B/32 ... | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| Figure 7: Left: Filters of the initial linear embedding of RGB values of ViT-L/32. Center: Sim- ilarity of position embeddings of ViT-L/32. Tiles show ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Table 6: Detailed results of model scaling experiments. These correspond to Figure 5 in the main paper. We show transfer accuracy on several datasets, ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| We report mean and standard deviation of the accuracies, averaged over three fine-tuning runs. | definition/direction/unit from same section | p. 6 (4 EXPERIMENTS) |
| Table 5: Top1 accuracy (in %) of Vision Transformer on various datasets when pre-trained on Im- ageNet, ImageNet-21k or JFT300M. These values correspond to ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Vision Transformer models pre-trained on the JFT-300M dataset outperform ResNet-based baselines on all datasets, while taking substantially less computational resources to pre-train. | comparison identity and matched condition | p. 6 (4 EXPERIMENTS) |
| 4.2 COMPARISON TO STATE OF THE ART We first compare our largest models - ViT-H/14 and ViT-L/16 - to state-of-the-art CNNs from the literature. | comparison identity and matched condition | p. 5 (4 EXPERIMENTS) |
| The smaller ViT-L/16 model pre-trained on JFT-300M outperforms BiT-L (which is pre-trained on the same dataset) on all tasks, while requiring substantially less computational ... | comparison identity and matched condition | p. 5 (4 EXPERIMENTS) |
| ViT-H/14 outperforms BiT-R152x4, and other methods, on the Natural and Structured tasks. | comparison identity and matched condition | p. 6 (4 EXPERIMENTS) |
| Figure 5: Performance versus pre-training compute for different architectures: Vision Transformers, ResNets, and hybrids. Vision Transformers generally outperform ResNets with the same compu- tational ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Figure 8: Scaling different model dimensions of the Vision Transformer. performance of two ResNets - 50x1 and 152x2 - pre-trained on JFT with SGD ... | comparison identity and matched condition | p. 16 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The second is Noisy Student (Xie et al., 2020), which is a large EfficientNet trained using semi-supervised learning on ImageNet and JFT300M with the ... | component/input/data sensitivity | p. 5 (4 EXPERIMENTS) |
| In what follows we use brief notation to indicate the model size and the input patch size: for instance, ViT-L/16 means the "Large" variant ... | component/input/data sensitivity | p. 5 (4 EXPERIMENTS) |
| Similarly, larger ViT variants overtake smaller ones as the dataset grows. | component/input/data sensitivity | p. 7 (4 EXPERIMENTS) |
| Table 4: Hyperparameters for fine-tuning. All models are fine-tuned with cosine learning rate decay, a batch size of 512, no weight decay, and grad ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| Table 5: Top1 accuracy (in %) of Vision Transformer on various datasets when pre-trained on Im- ageNet, ImageNet-21k or JFT300M. These values correspond to ... | component/input/data sensitivity | p. 15 (Figure/Table caption) |
| Table 8: Results of the ablation study on positional embeddings with ViT-B/16 model evaluated on ImageNet 5-shot linear. the difference in performance is fully ... | component/input/data sensitivity | p. 17 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The Transformer encoder (Vaswani et al., 2017) consists of alternating layers of multiheaded selfattention (MSA, see Appendix A) and MLP blocks (Eq. | Figure 5: Performance versus pre-training compute for different architectures: Vision Transformers, ResNets, and hybrids. Vision Transformers generally outperform ResNets with the same compu- tational ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 5 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 15 (Figure/Table caption), p. 16 (Figure/Table caption) |
| Primary metric/result | Table 2: Comparison with state of the art on popular image classification benchmarks. We re- port mean and standard deviation of the accuracies, averaged ... | numeric claim only at cited anchor | p. 6 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 4 EXPERIMENTS - extractive PDF cue:** In what follows we use brief notation to indicate the model size and the input patch size: for instance, ViT-L/16 means the "Large" variant with ...
- **p. 5 / 4 EXPERIMENTS - extractive PDF cue:** Option (ii) results in a 4x longer sequence length, and a more expensive ViT model.
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** Published as a conference paper at ICLR 2021 Ours-JFT Ours-JFT Ours-I21k BiT-L Noisy Student (ViT-H/14) (ViT-L/16) (ViT-L/16) (ResNet152x4) (EfficientNet-L2) ImageNet 88.55 ± 0.04 87.76 ± ...
- **p. 6 / 4 EXPERIMENTS - extractive PDF cue:** VTAB (19 tasks) 65 70 75 80 Accuracy [%] Natural (7 tasks) 70 80 90 Specialized (4 tasks) 80 82 85 88 90 Structured (8 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Further analysis of few-shot properties of ViT is an exciting direction of future work. | p. 7 (300 M) |
| body limitation/failure cue | In this setting data size does not bottleneck the models' performances, and we assess performance versus pre-training cost of each model. | p. 8 (300 M) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All models were trained on TPUv3 hardware, and we report the number of TPUv3-core-days taken to pre-train each of them, that is, the number ... | p. 5 (4 EXPERIMENTS) |
| We use a linear learning rate warmup and decay, see Appendix B.1 for details. | p. 5 (4 EXPERIMENTS) |
| We provide a controlled study of performance vs. compute for different architectures in Section 4.4. | p. 6 (4 EXPERIMENTS) |
| VTAB (19 tasks) 65 70 75 80 Accuracy [%] Natural (7 tasks) 70 80 90 Specialized (4 tasks) 80 82 85 88 90 Structured ... | p. 6 (4 EXPERIMENTS) |
| The classification head is implemented by a MLP with one hidden layer at pre-training time and by a single linear layer at fine-tuning time. | p. 3 (3 METHOD) |
| The resulting sequence of embedding vectors serves as input to the encoder. | p. 3 (3 METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 300 M - extractive PDF cue:** Further analysis of few-shot properties of ViT is an exciting direction of future work.
- **p. 8 / 300 M - extractive PDF cue:** In this setting data size does not bottleneck the models' performances, and we assess performance versus pre-training cost of each model.

- **PDF anchors reviewed:** datasets p. 4 (4 EXPERIMENTS), p. 4 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), metrics p. 6 (4 EXPERIMENTS), p. 20 (Figure/Table caption), p. 5 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (Figure/Table caption), p. 15 (Figure/Table caption), baselines p. 6 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS), p. 5 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 7 (Figure/Table caption), p. 16 (Figure/Table caption), results p. 7 (Figure/Table caption), p. 6 (Figure/Table caption), p. 5 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 15 (Figure/Table caption), p. 16 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
