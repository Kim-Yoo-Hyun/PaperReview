# Evaluation - Group Equivariant Convolutional Networks

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1602.07576; PDF retrieval source: https://arxiv.org/pdf/1602.07576. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (8.1. Rotated MNIST), p. 8 (8.1. Rotated MNIST), p. 7 (8.1. Rotated MNIST), p. 8 (8.1. Rotated MNIST)): This network (P4CNNRotationPooling) outperforms the baseline and the previous state of the art, but performs significantly worse than the P4CNN which does not pool over rotations in intermediate layers.

## Evaluation Body Digest

- **p. 7 / 8.1. Rotated MNIST - extractive body cue:** The dataset is split into a training, validation and test sets of size 10000, 2000 and 50000, respectively.
- **p. 7 / 8.1. Rotated MNIST - extractive body cue:** The dataset is split into 40k training, 10k validation and 10k testing splits.
- **p. 8 / 8.1. Rotated MNIST - extractive body cue:** Test set error rates and number of parameters are reported.
- **p. 7 / 8.1. Rotated MNIST - extractive body cue:** Error rates on rotated MNIST (with standard deviation under variation of the random seed).
- **p. 7 / 8.1. Rotated MNIST - extractive body cue:** The P4CNN almost halves the error rate of the previous state of the art (2.28% vs 3.98% error).
- **p. 8 / 8.1. Rotated MNIST - extractive body cue:** When trained with moderate data augmentation, this network achieves an error rate of 5.27% using planar convolutions, and 4.19% with p4m convolutions.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. A p4m feature map and its rotation by r. This rich transformation structure arises from the group op- eration of p4 or p4m, ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1. A p4 feature map and its rotation by r. When we apply the 90 degree rotation r to a function on p4, each ...

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 7. Efficient Implementation (p. 6); 8. Experiments (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 8.1. Rotated MNIST | SYSTEM / EVALUATION SCOPE UNRESOLVED | This network (P4CNNRotationPooling) outperforms the baseline and the previous state of the art, but performs significantly worse than the P4CNN which does not pool ... | p. 7 (8.1. Rotated MNIST) |
| 8.1. Rotated MNIST | SYSTEM / EVALUATION SCOPE UNRESOLVED | To the best of our knowledge, the p4m-CNN outperforms all published results on plain CIFAR10 (Wan et al., 2013; Goodfellow et al., 2013; Lin ... | p. 8 (8.1. Rotated MNIST) |
| 8.1. Rotated MNIST | SYSTEM / EVALUATION SCOPE UNRESOLVED | This baseline architecture outperforms the models tested by Larochelle et al. | p. 7 (8.1. Rotated MNIST) |
| 8.1. Rotated MNIST | SYSTEM / EVALUATION SCOPE UNRESOLVED | Extreme data augmentation and model ensembles can also further improve the numbers (Graham, 2014). | p. 8 (8.1. Rotated MNIST) |

## Dataset / Benchmark Role

- **p. 7 / 8.1. Rotated MNIST - extractive body cue:** The dataset is split into a training, validation and test sets of size 10000, 2000 and 50000, respectively.
- **p. 7 / 8.1. Rotated MNIST - extractive body cue:** The dataset is split into 40k training, 10k validation and 10k testing splits.
- **p. 8 / 8.1. Rotated MNIST - extractive body cue:** Test set error rates and number of parameters are reported.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1. A p4 feature map and its rotation by r. When we apply the 90 degree rotation r to a function on p4, each ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. A p4m feature map and its rotation by r. This rich transformation structure arises from the group op- eration of p4 or p4m, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Error rates on rotated MNIST (with standard deviation under variation of the random seed). 8.2. CIFAR-10 The CIFAR-10 dataset consists of 60k images ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. Comparison of conventional (i.e. Z2), p4 and p4m CNNs on CIFAR10 and augmented CIFAR10+. Test set error rates and number of parameters are ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The dataset is split into a training, validation and test sets of size 10000, 2000 and 50000, respectively. | embodiment, simulator version and control stack | p. 7 (8.1. Rotated MNIST), p. 7 (8.1. Rotated MNIST) |
| Task/environment | The dataset is split into 40k training, 10k validation and 10k testing splits. | reset, timeout, object/scene variation | p. 7 (8.1. Rotated MNIST), p. 8 (8.1. Rotated MNIST) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 7 (7.2. Planar convolution), p. 7 (7.1. Filter transformation) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1. Introduction), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Error rates on rotated MNIST (with standard deviation under variation of the random seed). | definition/direction/unit from same section | p. 7 (8.1. Rotated MNIST) |
| The P4CNN almost halves the error rate of the previous state of the art (2.28% vs 3.98% error). | definition/direction/unit from same section | p. 7 (8.1. Rotated MNIST) |
| Test set error rates and number of parameters are reported. | definition/direction/unit from same section | p. 8 (8.1. Rotated MNIST) |
| When trained with moderate data augmentation, this network achieves an error rate of 5.27% using planar convolutions, and 4.19% with p4m convolutions. | definition/direction/unit from same section | p. 8 (8.1. Rotated MNIST) |
| Figure 2. A p4m feature map and its rotation by r. This rich transformation structure arises from the group op- eration of p4 or ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 1. A p4 feature map and its rotation by r. When we apply the 90 degree rotation r to a function on p4, ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| This baseline architecture outperforms the models tested by Larochelle et al. | comparison identity and matched condition | p. 7 (8.1. Rotated MNIST) |
| We compared the p4-, p4m- and standard planar Z2 convolutions on two kinds of baseline architectures. | comparison identity and matched condition | p. 7 (8.1. Rotated MNIST) |
| Group Equivariant Convolutional Networks the baseline architectures by p4 or p4m convolutions. | comparison identity and matched condition | p. 8 (8.1. Rotated MNIST) |
| To the best of our knowledge, the p4m-CNN outperforms all published results on plain CIFAR10 (Wan et al., 2013; Goodfellow et al., 2013; Lin ... | comparison identity and matched condition | p. 8 (8.1. Rotated MNIST) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| This architecture (P4CNN) was found to perform better without dropout, so we removed it. | component/input/data sensitivity | p. 7 (8.1. Rotated MNIST) |
| The resulting feature maps consist of rotationinvariant features, and have the same transformation law as the input image. | component/input/data sensitivity | p. 7 (8.1. Rotated MNIST) |
| Group Equivariant Convolutional Networks the baseline architectures by p4 or p4m convolutions. | component/input/data sensitivity | p. 8 (8.1. Rotated MNIST) |
| This way, the number of parameters is left approximately invariant, while the size of the internal representation is increased. | component/input/data sensitivity | p. 8 (8.1. Rotated MNIST) |
| A plane symmetry group G is called split if any transformation g ∈G can be decomposed into a translation t ∈Z2 and a transformation ... | component/input/data sensitivity | p. 6 (7. Efficient Implementation) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Here we present the details for a G-convolution implementation that can leverage recent advances in fast computation of planar convolutions (Mathieu et al., 2014; ... | This network (P4CNNRotationPooling) outperforms the baseline and the previous state of the art, but performs significantly worse than the P4CNN which does not pool ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (8.1. Rotated MNIST), p. 8 (8.1. Rotated MNIST), p. 7 (8.1. Rotated MNIST), p. 8 (8.1. Rotated MNIST) |
| Primary metric/result | To the best of our knowledge, the p4m-CNN outperforms all published results on plain CIFAR10 (Wan et al., 2013; Goodfellow et al., 2013; Lin ... | numeric claim only at cited anchor | p. 8 (8.1. Rotated MNIST) |

- Numeric sentences retained from the body:
- **p. 7 / 7.2. Planar convolution - extractive body cue:** This sum can be folded into the sum over feature channels performed by the planar convolution routine by reshaping F + from Kl × Sl ...
- **p. 7 / 8.1. Rotated MNIST - extractive body cue:** We performed model selection using the validation set, yielding a CNN architecture (Z2CNN) with 7 layers of 3 × 3 convolutions (4 × 4 in ...
- **p. 7 / 8.1. Rotated MNIST - extractive body cue:** (2007) 10.38 ± 0.27 Sohn & Lee (2012) 4.2 Schmidt & Roth (2012) 3.98 Z2CNN 5.03 ± 0.0020 P4CNNRotationPooling 3.21 ± 0.0012 P4CNN 2.28 ± ...
- **p. 7 / 8.1. Rotated MNIST - extractive body cue:** Our second baseline is a residual network (He et al., 2016), which consists of an initial convolution layer, followed by three stages of 2n convolution ...
- **p. 7 / 8.1. Rotated MNIST - extractive body cue:** We use n = 7, ki = 32, 64, 128 yielding a wide 44-layer network called ResNet44.
- **p. 8 / 8.1. Rotated MNIST - extractive body cue:** The learning rate was divided by 10 at epoch 50, 100 and 150, and training was continued for 300 epochs.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | One limitation of the method as presented here is that it only works for discrete groups. | p. 8 (9. Discussion & Future work) |
| body limitation/failure cue | In future work, we want to implement G-CNNs that work on hexagonal lattices which have an increased number of symmetries relative to square grids, ... | p. 8 (9. Discussion & Future work) |
| body limitation/failure cue | (2007) (when trained on 12k and evaluated on 50k), but does not match the previous state of the art, which uses prior knowledge about ... | p. 7 (8.1. Rotated MNIST) |
| body limitation/failure cue | This network (P4CNNRotationPooling) outperforms the baseline and the previous state of the art, but performs significantly worse than the P4CNN which does not pool ... | p. 7 (8.1. Rotated MNIST) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The learning rate was divided by 10 at epoch 50, 100 and 150, and training was continued for 300 epochs. | p. 8 (8.1. Rotated MNIST) |
| The permutation can be implemented efficiently by a GPU kernel that does a lookup into F for each output cell of F +, using ... | p. 7 (7.1. Filter transformation) |
| For the ResNets, we used stochastic gradient descent with initial learning rate of 0.05 and momentum 0.9. | p. 8 (8.1. Rotated MNIST) |
| Here we present the details for a G-convolution implementation that can leverage recent advances in fast computation of planar convolutions (Mathieu et al., 2014; ... | p. 6 (7. Efficient Implementation) |
| Thus, to compute the p4 (or p4m) correlation f ⋆ψ we can first compute Lsψ ("filter transformation") for all four rotations (or all eight ... | p. 6 (7. Efficient Implementation) |
| Error rates on rotated MNIST (with standard deviation under variation of the random seed). | p. 7 (8.1. Rotated MNIST) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 9. Discussion & Future work - extractive body cue:** One limitation of the method as presented here is that it only works for discrete groups.
- **p. 8 / 9. Discussion & Future work - extractive body cue:** In future work, we want to implement G-CNNs that work on hexagonal lattices which have an increased number of symmetries relative to square grids, as ...
- **p. 7 / 8.1. Rotated MNIST - extractive body cue:** (2007) (when trained on 12k and evaluated on 50k), but does not match the previous state of the art, which uses prior knowledge about rotations ...
- **p. 7 / 8.1. Rotated MNIST - extractive body cue:** This network (P4CNNRotationPooling) outperforms the baseline and the previous state of the art, but performs significantly worse than the P4CNN which does not pool over ...

- **Evidence anchors reviewed:** datasets p. 7 (8.1. Rotated MNIST), p. 7 (8.1. Rotated MNIST), p. 8 (8.1. Rotated MNIST), metrics p. 7 (8.1. Rotated MNIST), p. 7 (8.1. Rotated MNIST), p. 8 (8.1. Rotated MNIST), p. 8 (8.1. Rotated MNIST), p. 4 (Figure/Table caption), p. 4 (Figure/Table caption), baselines p. 7 (8.1. Rotated MNIST), p. 7 (8.1. Rotated MNIST), p. 8 (8.1. Rotated MNIST), p. 8 (8.1. Rotated MNIST), results p. 7 (8.1. Rotated MNIST), p. 8 (8.1. Rotated MNIST), p. 7 (8.1. Rotated MNIST), p. 8 (8.1. Rotated MNIST).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
