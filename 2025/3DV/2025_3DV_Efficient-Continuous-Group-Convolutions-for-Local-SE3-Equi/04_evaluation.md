# Evaluation - Efficient Continuous Group Convolutions for Local SE(3) Equivariance in 3D Point Clouds

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=c6RR0bqNVI&name=pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2. Shape classification), p. 7 (Figure/Table caption), p. 6 (4.2. Shape classification), p. 7 (4.3. Semantic segmentation), p. 14 (Figure/Table caption), p. 15 (Figure/Table caption)): When we look at the SO(3) / SO(3) setup, all three methods achieve good performance; MC and Ours are able to outperform STD, while Ours achieves the best accuracy.

## Evaluation Body Digest

- **p. 7 / 4.3. Semantic segmentation - extractive PDF cue:** We test our method on ScanNet [14], a dataset composed of several indoor 3D scene scans, to show its applicability to real-world scenarios.
- **p. 5 / 4.2. Shape classification - extractive PDF cue:** We use the ModelNet40 dataset [40] since this is a standard benchmark for rotation equivariant networks [15].
- **p. 7 / 4.3. Semantic segmentation - extractive PDF cue:** 4.3.2 Scene understanding Scenes consist of multiple parts or objects with arbitrary orientations, making local equivariance essential for generalizing to unseen configurations.
- **p. 6 / 4.3. Semantic segmentation - extractive PDF cue:** The PosePrior dataset consists of challenging poses significantly divergent from those executed in DFAUST, which we use to test our model for generalization to unseen, ...
- **p. 5 / 4. Experiments - extractive PDF cue:** Due to space constraints, additional experiments, ablation studies, detailed dataset description and implementation are provided in the supplementary materials.
- **p. 6 / 4.3. Semantic segmentation - extractive PDF cue:** 3 depicts predictions for different models tested on the dataset.
- **p. 8 / 4.3. Semantic segmentation - extractive PDF cue:** Comparison to equivariant models on the classification task of ModelNet40 for different setups.
- **p. 8 / 4.3. Semantic segmentation - extractive PDF cue:** Comparison of our method to other rotation equivariant models on the segmentation task for out-of-distribution poses.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Shape classification | EMPIRICAL / REAL-ROBOT OR HARDWARE | When we look at the SO(3) / SO(3) setup, all three methods achieve good performance; MC and Ours are able to outperform STD, while ... | p. 6 (4.2. Shape classification) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 3. Qualitative results. Global equivariant methods such as VN, or FA struggle with out-of-distribution models. Our method, on the other hand, achieves almost ... | p. 7 (Figure/Table caption) |
| 4.2. Shape classification | EMPIRICAL / REAL-ROBOT OR HARDWARE | MC, although it can also achieve competitive performance, for most of the cases, the drop in performance is significant compared to the I / ... | p. 6 (4.2. Shape classification) |
| 4.3. Semantic segmentation | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results show that using our sampling approach increases the performance significantly, leading to better results with fewer samples. | p. 7 (4.3. Semantic segmentation) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4. Additional Qualitative results. Global equivariant methods such as VN, or FA struggle with out-of-distribution models, especially up-side down models. Our method, on ... | p. 14 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 4.3. Semantic segmentation - extractive PDF cue:** We test our method on ScanNet [14], a dataset composed of several indoor 3D scene scans, to show its applicability to real-world scenarios.
- **p. 5 / 4.2. Shape classification - extractive PDF cue:** We use the ModelNet40 dataset [40] since this is a standard benchmark for rotation equivariant networks [15].
- **p. 7 / 4.3. Semantic segmentation - extractive PDF cue:** 4.3.2 Scene understanding Scenes consist of multiple parts or objects with arbitrary orientations, making local equivariance essential for generalizing to unseen configurations.
- **p. 6 / 4.3. Semantic segmentation - extractive PDF cue:** The PosePrior dataset consists of challenging poses significantly divergent from those executed in DFAUST, which we use to test our model for generalization to unseen, ...
- **p. 5 / 4. Experiments - extractive PDF cue:** Due to space constraints, additional experiments, ablation studies, detailed dataset description and implementation are provided in the supplementary materials.
- **p. 6 / 4.3. Semantic segmentation - extractive PDF cue:** 3 depicts predictions for different models tested on the dataset.
- **p. 8 / 4.3. Semantic segmentation - extractive PDF cue:** Comparison to equivariant models on the classification task of ModelNet40 for different setups.
- **p. 8 / 4.3. Semantic segmentation - extractive PDF cue:** Comparison of our method to other rotation equivariant models on the segmentation task for out-of-distribution poses.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. While global equivariant designs ensure robustness to whole-scene rotations, they fail with randomly rotated scene parts or elements. In contrast, local equivariant operations ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 2. Overview of our convolution operation. Given a central point with an orientation, first, we sample neighboring points. For each point, we use PCA ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1. Results for different configurations for the classification task on the ModelNet40 dataset. The results show that using our sampling approach increases the performance ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3. Qualitative results. Global equivariant methods such as VN, or FA struggle with out-of-distribution models. Our method, on the other hand, achieves almost perfect ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2. Comparison to equivariant models on the classification task of ModelNet40 for different setups. Equiv.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3. Semantic segmentation results for different models trained on DFAUST and tested on PosePrior. By using our sam- pling approach, mAcc, and mIoU increase ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Comparison of our method to other rotation equivariant models on the segmentation task for out-of-distribution poses. Equiv.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 5. Computational and memory resources of a single convo- lution layer for our approach and state-of-the-art methods.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We test our method on ScanNet [14], a dataset composed of several indoor 3D scene scans, to show its applicability to real-world scenarios. | embodiment, simulator version and control stack | p. 7 (4.3. Semantic segmentation), p. 5 (4.2. Shape classification) |
| Task/environment | We use the ModelNet40 dataset [40] since this is a standard benchmark for rotation equivariant networks [15]. | reset, timeout, object/scene variation | p. 5 (4.2. Shape classification), p. 7 (4.3. Semantic segmentation) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3.1. Group equivariant convolution), p. 3 (3.1. Group equivariant convolution) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (3.2. Efficient group convolution), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Our model only takes as input point coordinates, and performance is measured with overall accuracy. | definition/direction/unit from same section | p. 5 (4.2. Shape classification) |
| When we look at the SO(3) / SO(3) setup, all three methods achieve good performance; MC and Ours are able to outperform STD, while ... | definition/direction/unit from same section | p. 6 (4.2. Shape classification) |
| We hypothesize that training with random 1 or 2 samples, rather than using the full frame, introduces stochasticity that acts as a regularizer, enhancing ... | definition/direction/unit from same section | p. 6 (4.2. Shape classification) |
| Table 7. Error in degrees of different methods on the task of pose estimation on ModelNet40. Metrics # samp. Mean(◦) Median(◦) Max(◦) EPN [9] | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| Figure 1. While global equivariant designs ensure robustness to whole-scene rotations, they fail with randomly rotated scene parts or elements. In contrast, local equivariant ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| The results show that using our sampling approach increases the performance significantly, leading to better results with fewer samples. | definition/direction/unit from same section | p. 7 (4.3. Semantic segmentation) |
| 4.3.2 Scene understanding Scenes consist of multiple parts or objects with arbitrary orientations, making local equivariance essential for generalizing to unseen configurations. | definition/direction/unit from same section | p. 7 (4.3. Semantic segmentation) |
| Results for the semantic segmentation task on ScanNet20 show that using our sampling approach increases the performance. | definition/direction/unit from same section | p. 8 (4.3. Semantic segmentation) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| When comparing to current state-of-the-art local equivariant methods, we can see that while they also outperform global equivariant methods by a large margin, our ... | comparison identity and matched condition | p. 7 (4.3. Semantic segmentation) |
| Additionally, to compare to other state-of-the-art methods, we take the commonly used setup where random rotations are applied along the up vector during training ... | comparison identity and matched condition | p. 5 (4.2. Shape classification) |
| Also, in the z / SO(3) and SO(3) / SO(3) settings, we outperform all local rotation equivariant networks. | comparison identity and matched condition | p. 6 (4.2. Shape classification) |
| MC, although it can also achieve competitive performance, for most of the cases, the drop in performance is significant compared to the I / ... | comparison identity and matched condition | p. 6 (4.2. Shape classification) |
| Compared to other state-ofthe-art local rotation equivariant methods, E2PN [48] and EPN [9], the computational resources needed for our approach are significantly lower even ... | comparison identity and matched condition | p. 7 (4.3. Semantic segmentation) |
| Compared to MC, we can see that our approach obtains better predictions in all but one configuration. | comparison identity and matched condition | p. 8 (4.3. Semantic segmentation) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| This shows that with our method, we can introduce the equivariant property without extra costs, demonstrating the efficiency of our proposed model. | component/input/data sensitivity | p. 7 (4.3. Semantic segmentation) |
| Analyzing the effect of different samples used to compute the integral over SO(3) for training and testing, we can see that Ours, even with ... | component/input/data sensitivity | p. 6 (4.2. Shape classification) |
| All models are evaluated when trained and tested without any rotation, I / I. | component/input/data sensitivity | p. 5 (4.2. Shape classification) |
| For this task, predictions must be invariant of the rotation applied to the model. | component/input/data sensitivity | p. 5 (4.2. Shape classification) |
| The same is true for our non-equivariant version, STD. | component/input/data sensitivity | p. 6 (4.3. Semantic segmentation) |
| Global equivariant methods such as VN, or FA struggle with out-of-distribution models. | component/input/data sensitivity | p. 7 (4.3. Semantic segmentation) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we propose using a finite subset F(x) ⊂ SE(3), referred to as a frame, to solve the group equivariant integral, which ... | When we look at the SO(3) / SO(3) setup, all three methods achieve good performance; MC and Ours are able to outperform STD, while ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2. Shape classification), p. 7 (Figure/Table caption), p. 6 (4.2. Shape classification), p. 7 (4.3. Semantic segmentation), p. 14 (Figure/Table caption), p. 15 (Figure/Table caption) |
| Primary metric/result | Figure 3. Qualitative results. Global equivariant methods such as VN, or FA struggle with out-of-distribution models. Our method, on the other hand, achieves almost ... | numeric claim only at cited anchor | p. 7 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 6 / 4.2. Shape classification - extractive PDF cue:** Analyzing the effect of different samples used to compute the integral over SO(3) for training and testing, we can see that Ours, even with 1 ...
- **p. 6 / 4.2. Shape classification - extractive PDF cue:** With only 2 samples, our method is able to match or even surpass the accuracy of using the full frame, 4 samples.
- **p. 6 / 4.2. Shape classification - extractive PDF cue:** Moreover, using only 1 or 2 samples appears to be more robust than using the full frame, 4 samples, when tested with different numbers of ...
- **p. 6 / 4.2. Shape classification - extractive PDF cue:** We hypothesize that training with random 1 or 2 samples, rather than using the full frame, introduces stochasticity that acts as a regularizer, enhancing robustness ...
- **p. 6 / 4.2. Shape classification - extractive PDF cue:** In contrast, MC is more sensitive to the number of samples, exhibiting significant performance degradation with 1 or 2 samples.
- **p. 6 / 4.3. Semantic segmentation - extractive PDF cue:** When evaluating the model robustness to the number of samples in the SO(3) integral, Ours outperforms MC in all cases except when trained on 4 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 3. Qualitative results. Global equivariant methods such as VN, or FA struggle with out-of-distribution models. Our method, on the other hand, achieves almost ... | p. 7 (Figure/Table caption) |
| body limitation/failure cue | Figure 4. Additional Qualitative results. Global equivariant methods such as VN, or FA struggle with out-of-distribution models, especially up-side down models. Our method, on ... | p. 14 (Figure/Table caption) |
| body limitation/failure cue | Figure 5. Additional Qualitative results. Global equivariant methods such as VN, or FA struggle with out-of-distribution models. Our method, on the other hand, achieves ... | p. 15 (Figure/Table caption) |
| body limitation/failure cue | When compared to global equivariant networks, our method falls behind in the I / SO(3) setup and achieves similar performance on the z / ... | p. 6 (4.2. Shape classification) |
| body limitation/failure cue | Figure 1. While global equivariant designs ensure robustness to whole-scene rotations, they fail with randomly rotated scene parts or elements. In contrast, local equivariant ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | Moreover, by restricting the receptive field of our convolution, our operation becomes local equivariant, allowing us to be robust to local transformations. | p. 8 (5. Conclusions) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| (4)) at the end of our encoder to transform the equivariant features into invariant ones. | p. 5 (4.2. Shape classification) |
| Due to space constraints, additional experiments, ablation studies, detailed dataset description and implementation are provided in the supplementary materials. | p. 5 (4. Experiments) |
| Analyzing the effect of different samples used to compute the integral over SO(3) for training and testing, we can see that Ours, even with ... | p. 6 (4.2. Shape classification) |
| This is a crucial property for processing such large point clouds, making it intractable for the other methods to run | p. 7 (4.3. Semantic segmentation) |
| Since group convolution layers map between higher dimensional feature maps and must compute the integral over the entire group, they can introduce a computational ... | p. 4 (3.2. Efficient group convolution) |
| In addition to the computational burden of a 6D convolution, another difficulty lies in how to define a grid on SE(3) or, more specifically, ... | p. 4 (3.2. Efficient group convolution) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3. Qualitative results. Global equivariant methods such as VN, or FA struggle with out-of-distribution models. Our method, on the other hand, achieves almost perfect ...
- **p. 14 / Figure/Table caption - extractive PDF cue:** Figure 4. Additional Qualitative results. Global equivariant methods such as VN, or FA struggle with out-of-distribution models, especially up-side down models. Our method, on the ...
- **p. 15 / Figure/Table caption - extractive PDF cue:** Figure 5. Additional Qualitative results. Global equivariant methods such as VN, or FA struggle with out-of-distribution models. Our method, on the other hand, achieves almost ...
- **p. 6 / 4.2. Shape classification - extractive PDF cue:** When compared to global equivariant networks, our method falls behind in the I / SO(3) setup and achieves similar performance on the z / SO(3) ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. While global equivariant designs ensure robustness to whole-scene rotations, they fail with randomly rotated scene parts or elements. In contrast, local equivariant operations ...
- **p. 8 / 5. Conclusions - extractive PDF cue:** Moreover, by restricting the receptive field of our convolution, our operation becomes local equivariant, allowing us to be robust to local transformations.

- **PDF anchors reviewed:** datasets p. 7 (4.3. Semantic segmentation), p. 5 (4.2. Shape classification), p. 7 (4.3. Semantic segmentation), p. 6 (4.3. Semantic segmentation), p. 5 (4. Experiments), p. 6 (4.3. Semantic segmentation), metrics p. 5 (4.2. Shape classification), p. 6 (4.2. Shape classification), p. 6 (4.2. Shape classification), p. 12 (Figure/Table caption), p. 1 (Figure/Table caption), p. 7 (4.3. Semantic segmentation), baselines p. 7 (4.3. Semantic segmentation), p. 5 (4.2. Shape classification), p. 6 (4.2. Shape classification), p. 6 (4.2. Shape classification), p. 7 (4.3. Semantic segmentation), p. 8 (4.3. Semantic segmentation), results p. 6 (4.2. Shape classification), p. 7 (Figure/Table caption), p. 6 (4.2. Shape classification), p. 7 (4.3. Semantic segmentation), p. 14 (Figure/Table caption), p. 15 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
