# Evaluation - PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1612.00593; PDF retrieval source: https://arxiv.org/pdf/1612.00593. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5.1. Applications), p. 5 (5.1. Applications), p. 6 (5.1. Applications), p. 7 (5.2. Architecture Design Analysis), p. 8 (5.4. Time and Space Complexity Analysis), p. 6 (5.1. Applications)): Results are shown in Table 3, where our PointNet method significantly outperforms the baseline method.

## Evaluation Body Digest

- **p. 5 / 5.1. Applications - extractive body cue:** Even though we are working on a brand new data representation (point sets), we are able to achieve comparable or even better performance on benchmarks ...
- **p. 6 / 5.1. Applications - extractive body cue:** Results on 3D object detection in scenes.
- **p. 6 / 5.1. Applications - extractive body cue:** Semantic Segmentation in Scenes Our network on part segmentation can be easily extended to semantic scene segmentation, where point labels become semantic object classes instead ...
- **p. 5 / 5.1. Applications - extractive body cue:** We evaluate our model on the ModelNet40 [28] shape classification benchmark.
- **p. 7 / 5.2. Architecture Design Analysis - extractive body cue:** Metric is overall classification accuracy on ModelNet40 test set.
- **p. 7 / 5.2. Architecture Design Analysis - extractive body cue:** We use the ModelNet40 shape classification problem as a test bed for comparisons of those options, the following two control experiment will also use this ...
- **p. 8 / 5.4. Time and Space Complexity Analysis - extractive body cue:** Empirically, PointNet is able to process more than one million points per second for point cloud classification (around 1K objects/second) or semantic segmentation (around 2 ...
- **p. 6 / 5.1. Applications - extractive body cue:** In Table 2, we report per-category and mean IoU(%) scores.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiment (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.1. Applications | SYSTEM / EVALUATION SCOPE UNRESOLVED | Results are shown in Table 3, where our PointNet method significantly outperforms the baseline method. | p. 7 (5.1. Applications) |
| 5.1. Applications | SYSTEM / EVALUATION SCOPE UNRESOLVED | Even though we are working on a brand new data representation (point sets), we are able to achieve comparable or even better performance on ... | p. 5 (5.1. Applications) |
| 5.1. Applications | SYSTEM / EVALUATION SCOPE UNRESOLVED | Our model achieved state-of-the-art performance among methods based on 3D input (volumetric and point cloud). | p. 6 (5.1. Applications) |
| 5.2. Architecture Design Analysis | SYSTEM / EVALUATION SCOPE UNRESOLVED | By combining both transformations and the regularization term, we achieve the best performance. | p. 7 (5.2. Architecture Design Analysis) |
| 5.4. Time and Space Complexity Analysis | SYSTEM / EVALUATION SCOPE UNRESOLVED | While MVCNN [23] and Subvolume (3D CNN) [18] achieve high performance, PointNet is orders more efficient in computational cost (measured in FLOPs/sample: 141x and ... | p. 8 (5.4. Time and Space Complexity Analysis) |

## Dataset / Benchmark Role

- **p. 5 / 5.1. Applications - extractive body cue:** Even though we are working on a brand new data representation (point sets), we are able to achieve comparable or even better performance on benchmarks ...
- **p. 6 / 5.1. Applications - extractive body cue:** Results on 3D object detection in scenes.
- **p. 6 / 5.1. Applications - extractive body cue:** Semantic Segmentation in Scenes Our network on part segmentation can be easily extended to semantic scene segmentation, where point labels become semantic object classes instead ...
- **p. 5 / 5.1. Applications - extractive body cue:** We evaluate our model on the ModelNet40 [28] shape classification benchmark.
- **p. 7 / 5.2. Architecture Design Analysis - extractive body cue:** Metric is overall classification accuracy on ModelNet40 test set.
- **p. 7 / 5.2. Architecture Design Analysis - extractive body cue:** We use the ModelNet40 shape classification problem as a test bed for comparisons of those options, the following two control experiment will also use this ...
- **p. 8 / 5.4. Time and Space Complexity Analysis - extractive body cue:** Empirically, PointNet is able to process more than one million points per second for point cloud classification (around 1K objects/second) or semantic segmentation (around 2 ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Applications of PointNet. We propose a novel deep net architecture that consumes raw point cloud (set of points) without voxelization or rendering. It ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. PointNet Architecture. The classification network takes n points as input, applies input and feature transformations, and then aggregates point features by max pooling. ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 3. Qualitative results for part segmentation. We visualize the CAD part segmentation results across all 16 object categories. We show both results for partial ...
- **p. 5 / Figure/Table caption - extractive body cue:** Table 1. Classification results on ModelNet40. Our net achieves state-of-the-art among deep nets on 3D input. We explain the implications of the theorem. (a) says ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Segmentation results on ShapeNet part dataset. Metric is mIoU(%) on points. We compare with two traditional methods [27] and [29] and a 3D ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Results on semantic segmentation in scenes. Metric is average IoU over 13 classes (structural and furniture elements plus clutter) and classification accuracy calculated ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 4. Results on 3D object detection in scenes. Metric is average precision with threshold IoU 0.5 computed in 3D volumes.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative results for semantic segmentation. Top row is input point cloud with color. Bottom row is output semantic segmentation result (on points) displayed ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Even though we are working on a brand new data representation (point sets), we are able to achieve comparable or even better performance on ... | embodiment, simulator version and control stack | p. 5 (5.1. Applications), p. 6 (5.1. Applications) |
| Task/environment | Results on 3D object detection in scenes. | reset, timeout, object/scene variation | p. 6 (5.1. Applications), p. 6 (5.1. Applications) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 1 (1. Introduction), p. 3 (3. Problem Statement) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (3. Problem Statement), p. 3 (4.2. PointNet Architecture) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In Table 2, we report per-category and mean IoU(%) scores. | definition/direction/unit from same section | p. 6 (5.1. Applications) |
| We train our segmentation version of PointNet to predict mean IoU overall accuracy Ours baseline 20.12 53.19 Ours PointNet 47.71 78.62 Table 3. | definition/direction/unit from same section | p. 6 (5.1. Applications) |
| Figure 11. Precision-recall curves for object detection in 3D point cloud. We evaluated on all six areas for four categories: table, chair, sofa and ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| Metric is overall classification accuracy on ModelNet40 test set. | definition/direction/unit from same section | p. 7 (5.2. Architecture Design Analysis) |
| The weighted sum is then computed on the normalized scores and the point features. | definition/direction/unit from same section | p. 7 (5.2. Architecture Design Analysis) |
| The net has more than 80% accuracy even when 20% of the points are outliers. | definition/direction/unit from same section | p. 8 (5.2. Architecture Design Analysis) |
| 30 40 50 60 70 80 90 0 0.05 0.1 Accuracy (%) Perturbation noise std 30 40 50 60 70 80 90 100 0 ... | definition/direction/unit from same section | p. 8 (5.2. Architecture Design Analysis) |
| Figure 23. PointNet segmentation failure cases. In this figure, we summarize six types of common errors in our segmentation application. The prediction and the ... | definition/direction/unit from same section | p. 18 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Results are shown in Table 3, where our PointNet method significantly outperforms the baseline method. | comparison identity and matched condition | p. 7 (5.1. Applications) |
| The baselines (illustrated in Fig 5) we compared with include multi-layer perceptron on unsorted and sorted (1,2,3) (2,3,4) (1,3,1) rnn cell rnn cell rnn ... | comparison identity and matched condition | p. 7 (5.2. Architecture Design Analysis) |
| Table 2. Segmentation results on ShapeNet part dataset. Metric is mIoU(%) on points. We compare with two traditional methods [27] and [29] and a ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| We observe a 2.3% mean IoU improvement and our net beats the baseline methods in most categories. | comparison identity and matched condition | p. 6 (5.1. Applications) |
| Our net achieves state-of-the-art among deep nets on 3D input. | comparison identity and matched condition | p. 5 (4.3. Theoretical Analysis) |
| Then, (a) ∀S, ∃CS, NS ⊆X, f(T) = f(S) if CS ⊆T ⊆NS; (b) /CS/ ≤K input #views accuracy accuracy avg. class overall SPH ... | comparison identity and matched condition | p. 5 (4.3. Theoretical Analysis) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 1. Applications of PointNet. We propose a novel deep net architecture that consumes raw point cloud (set of points) without voxelization or rendering. ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Comparison with Alternative Order-invariant Methods As mentioned in Sec 4.2, there are at least three options for consuming unordered set inputs. | component/input/data sensitivity | p. 7 (5.2. Architecture Design Analysis) |
| PointNet (vanilla) is the classification PointNet without input and feature transformations. | component/input/data sensitivity | p. 8 (5.4. Time and Space Complexity Analysis) |
| Subvolume and MVCNN used pooling on input data from multiple rotations or views, without which they have much inferior performance. | component/input/data sensitivity | p. 8 (5.4. Time and Space Complexity Analysis) |
| Based on the semantic segmentation output from our network, we further build a 3D object detection system using connected component for object proposal (see ... | component/input/data sensitivity | p. 7 (5.1. Applications) |
| Figure 24. Examples of semantic segmentation and object detection. First row is input point cloud, where walls and ceiling are hided for clarity. Second ... | component/input/data sensitivity | p. 19 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The key contributions of our work are as follows: • We design a novel deep net architecture suitable for consuming unordered point sets in ... | Results are shown in Table 3, where our PointNet method significantly outperforms the baseline method. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5.1. Applications), p. 5 (5.1. Applications), p. 6 (5.1. Applications), p. 7 (5.2. Architecture Design Analysis), p. 8 (5.4. Time and Space Complexity Analysis), p. 6 (5.1. Applications) |
| Primary metric/result | Even though we are working on a brand new data representation (point sets), we are able to achieve comparable or even better performance on ... | numeric claim only at cited anchor | p. 5 (5.1. Applications) |

- Numeric sentences retained from the body:
- **p. 5 / 4.3. Theoretical Analysis - extractive body cue:** We visualize the CAD part segmentation results across all 16 object categories.
- **p. 6 / 5.1. Applications - extractive body cue:** We uniformly sample 1024 points on mesh faces according to face area and normalize them into a unit sphere.
- **p. 7 / 5.1. Applications - extractive body cue:** At training time, we randomly sample 4096 points in each block on-the-fly.
- **p. 8 / 5.2. Architecture Design Analysis - extractive body cue:** Furthest means the original 1024 points are sampled with furthest sampling.
- **p. 8 / 5.4. Time and Space Complexity Analysis - extractive body cue:** While MVCNN [23] and Subvolume (3D CNN) [18] achieve high performance, PointNet is orders more efficient in computational cost (measured in FLOPs/sample: 141x and 8x ...
- **p. 8 / 5.4. Time and Space Complexity Analysis - extractive body cue:** Besides, PointNet is much more space efficient than MVCNN in terms of #param in the network (17x less parameters).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 23. PointNet segmentation failure cases. In this figure, we summarize six types of common errors in our segmentation application. The prediction and the ... | p. 18 (Figure/Table caption) |
| body limitation/failure cue | While critical points jointly determine the global shape feature for a given shape, any point cloud that falls between the critical points set and ... | p. 8 (5.3. Visualizing PointNet) |
| body limitation/failure cue | CS and NS reflect the robustness of PointNet, meaning that losing some non-critical points does not change the global shape signature f(S) at all. | p. 8 (5.3. Visualizing PointNet) |
| body limitation/failure cue | Combined with the continuity of h, this explains the robustness of our model w.r.t point perturbation, corruption and extra noise points. | p. 5 (4.3. Theoretical Analysis) |
| body limitation/failure cue | Our network is able to output smooth predictions and is robust to missing points and occlusions. | p. 7 (5.1. Applications) |
| body limitation/failure cue | The robustness is gained in analogy to the sparsity principle in machine learning models. | p. 5 (4.3. Theoretical Analysis) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| At training time, we randomly sample 4096 points in each block on-the-fly. | p. 7 (5.1. Applications) |
| Metric is average precision with threshold IoU 0.5 computed in 3D volumes. | p. 6 (5.1. Applications) |
| With only fully connected layers and max pooling, our net gains a strong lead in inference speed and can be easily parallelized in CPU ... | p. 6 (5.1. Applications) |
| We also show the effects of our network's hyperparameters. | p. 7 (5.2. Architecture Design Analysis) |
| We color-code all figures to show the depth information. | p. 8 (5.3. Visualizing PointNet) |
| Empirically, PointNet is able to process more than one million points per second for point cloud classification (around 1K objects/second) or semantic segmentation (around ... | p. 8 (5.4. Time and Space Complexity Analysis) |
| [9] introduces the idea of spatial transformer to align 2D images through sampling and interpolation, achieved by a specifically tailored layer implemented on GPU. | p. 4 (4.2. PointNet Architecture) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 18 / Figure/Table caption - extractive body cue:** Figure 23. PointNet segmentation failure cases. In this figure, we summarize six types of common errors in our segmentation application. The prediction and the ground-truth ...
- **p. 8 / 5.3. Visualizing PointNet - extractive body cue:** While critical points jointly determine the global shape feature for a given shape, any point cloud that falls between the critical points set and the ...
- **p. 8 / 5.3. Visualizing PointNet - extractive body cue:** CS and NS reflect the robustness of PointNet, meaning that losing some non-critical points does not change the global shape signature f(S) at all.
- **p. 5 / 4.3. Theoretical Analysis - extractive body cue:** Combined with the continuity of h, this explains the robustness of our model w.r.t point perturbation, corruption and extra noise points.
- **p. 7 / 5.1. Applications - extractive body cue:** Our network is able to output smooth predictions and is robust to missing points and occlusions.
- **p. 5 / 4.3. Theoretical Analysis - extractive body cue:** The robustness is gained in analogy to the sparsity principle in machine learning models.

- **Evidence anchors reviewed:** datasets p. 5 (5.1. Applications), p. 6 (5.1. Applications), p. 6 (5.1. Applications), p. 5 (5.1. Applications), p. 7 (5.2. Architecture Design Analysis), p. 7 (5.2. Architecture Design Analysis), metrics p. 6 (5.1. Applications), p. 6 (5.1. Applications), p. 12 (Figure/Table caption), p. 7 (5.2. Architecture Design Analysis), p. 7 (5.2. Architecture Design Analysis), p. 8 (5.2. Architecture Design Analysis), baselines p. 7 (5.1. Applications), p. 7 (5.2. Architecture Design Analysis), p. 6 (Figure/Table caption), p. 6 (5.1. Applications), p. 5 (4.3. Theoretical Analysis), p. 5 (4.3. Theoretical Analysis), results p. 7 (5.1. Applications), p. 5 (5.1. Applications), p. 6 (5.1. Applications), p. 7 (5.2. Architecture Design Analysis), p. 8 (5.4. Time and Space Complexity Analysis), p. 6 (5.1. Applications).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (19 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Results are shown in Table 3, where our PointNet method significantly outperforms the baseline method. (p. 7, 5.1. Applications).
- **Metric evidence:** In Table 2, we report per-category and mean IoU(%) scores. (p. 6, 5.1. Applications).
- **Baseline/ablation evidence:** Results are shown in Table 3, where our PointNet method significantly outperforms the baseline method. (p. 7, 5.1. Applications).
- **Failure/negative evidence:** During training we augment the point cloud on-the-fly by randomly rotating the object along the up-axis and jitter the position of each points by a Gaussian noise with zero mean ... (p. 6, 5.1. Applications).
