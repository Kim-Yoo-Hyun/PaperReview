# Evaluation - Depth Map Prediction from a Single Image using a Multi-Scale Deep Network

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (9 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/1406.2283; PDF retrieval source: https://arxiv.org/pdf/1406.2283. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (Figure/Table caption), p. 6 (5 Results), p. 6 (5 Results), p. 7 (5 Results)): Figure 3: Qualitative comparison of Make3D, our method trained with l2 loss (λ = 0), and our method trained with both l2 and scale-invariant loss (λ = 0.5). 5.2 KITTI ...

## Evaluation Body Digest

- **p. 5 / 4 Experiments - extractive PDF cue:** We use the official train/test split, using 249 scenes for training and 215 for testing, and construct our training set using the raw data for ...
- **p. 5 / 4 Experiments - extractive PDF cue:** 4.1 NYU Depth The NYU Depth dataset [18] is composed of 464 indoor scenes, taken as video sequences using a Microsoft Kinect camera.
- **p. 6 / 4 Experiments - extractive PDF cue:** The depth for this dataset is sampled at irregularly spaced points, captured at different times using a rotating LIDAR scanner.
- **p. 6 / 4 Experiments - extractive PDF cue:** 4.3 Baselines and Comparisons We compare our method against Make3D trained on the same datasets, as well as the published results of other current methods ...
- **p. 7 / 5 Results - extractive PDF cue:** 5.2 KITTI We next examine results on the KITTI driving dataset.
- **p. 7 / 5 Results - extractive PDF cue:** Here, the Make3D baseline is well-suited to the dataset, being composed of horizontally aligned images, and achieves relatively good results.
- **p. 5 / 4 Experiments - extractive PDF cue:** These ratios were found by trial-and-error on a validation set (folded back into the training set for our final evaluations), and the global scale of ...
- **p. 7 / 5 Results - extractive PDF cue:** 3 shows Make3D performing much better on this data, as expected, while using the scale-invariant error as a loss seems to have little effect in ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 5); 5 Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 3: Qualitative comparison of Make3D, our method trained with l2 loss (λ = 0), and our method trained with both l2 and scale-invariant ... | p. 7 (Figure/Table caption) |
| 5 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our system achieves the best performance on all metrics, obtaining an average 35% relative gain compared to the runner-up. | p. 6 (5 Results) |
| 5 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | While we did not observe numeric gains using λ = 0.5 over λ = 0, it did produce slight qualitative improvements in the more ... | p. 6 (5 Results) |
| 5 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Again, the fine-scale network does not improve much over the coarse one in the error metrics, but differences between the two can be seen ... | p. 7 (5 Results) |

## Dataset / Benchmark Role

- **p. 5 / 4 Experiments - extractive PDF cue:** We use the official train/test split, using 249 scenes for training and 215 for testing, and construct our training set using the raw data for ...
- **p. 5 / 4 Experiments - extractive PDF cue:** 4.1 NYU Depth The NYU Depth dataset [18] is composed of 464 indoor scenes, taken as video sequences using a Microsoft Kinect camera.
- **p. 6 / 4 Experiments - extractive PDF cue:** The depth for this dataset is sampled at irregularly spaced points, captured at different times using a rotating LIDAR scanner.
- **p. 6 / 4 Experiments - extractive PDF cue:** 4.3 Baselines and Comparisons We compare our method against Make3D trained on the same datasets, as well as the published results of other current methods ...
- **p. 7 / 5 Results - extractive PDF cue:** 5.2 KITTI We next examine results on the KITTI driving dataset.
- **p. 7 / 5 Results - extractive PDF cue:** Here, the Make3D baseline is well-suited to the dataset, being composed of horizontally aligned images, and achieves relatively good results.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 1: Model architecture. as vanishing points, object locations, and room alignment. A local view (as is commonly used for stereo matching) is insufficient to ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Weight vectors from layer Coarse 7 (coarse output), for (a) KITTI and (b) NYUDepth. Red is positive (farther) and blue is negative (closer); ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: Comparison on the NYUDepth dataset input m3d coarse L2 L2 scale-inv ground truth input
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3: Qualitative comparison of Make3D, our method trained with l2 loss (λ = 0), and our method trained with both l2 and scale-invariant loss ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2: Comparison on the KITTI dataset. 6
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4: Example predictions from our algorithm. NYUDepth on left, KITTI on right. For each image, we show (a) input, (b) output of coarse network, ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We use the official train/test split, using 249 scenes for training and 215 for testing, and construct our training set using the raw data ... | embodiment, simulator version and control stack | p. 5 (4 Experiments), p. 5 (4 Experiments) |
| Task/environment | 4.1 NYU Depth The NYU Depth dataset [18] is composed of 464 indoor scenes, taken as video sequences using a Microsoft Kinect camera. | reset, timeout, object/scene variation | p. 5 (4 Experiments), p. 6 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (3 Approach), p. 3 (3 Approach) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3 Approach), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| These ratios were found by trial-and-error on a validation set (folded back into the training set for our final evaluations), and the global scale ... | definition/direction/unit from same section | p. 5 (4 Experiments) |
| 3 shows Make3D performing much better on this data, as expected, while using the scale-invariant error as a loss seems to have little effect ... | definition/direction/unit from same section | p. 7 (5 Results) |
| Although the fine-scale network does not improve in the error measurements, its effect is clearly visible in the depth maps - surface boundaries have ... | definition/direction/unit from same section | p. 6 (5 Results) |
| We evaluate each method using several errors from prior works, as well as our scale-invariant metric: Threshold: % of yi s.t. max( yi y∗ ... | definition/direction/unit from same section | p. 6 (4 Experiments) |
| 4 shows examples of predictions, again sorted by error. | definition/direction/unit from same section | p. 7 (5 Results) |
| Learning rates are: 0.001 for coarse convolutional layers 1-5, 0.1 for coarse full layers 6 and 7, 0.001 for fine layers 1 and 3, ... | definition/direction/unit from same section | p. 5 (4 Experiments) |
| Figure 1: Model architecture. as vanishing points, object locations, and room alignment. A local view (as is commonly used for stereo matching) is insufficient ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 4.3 Baselines and Comparisons We compare our method against Make3D trained on the same datasets, as well as the published results of other current ... | comparison identity and matched condition | p. 6 (4 Experiments) |
| As explained in Section 4.3, we compare against the data mean and Make3D as baselines, as well as Karsch et al. | comparison identity and matched condition | p. 6 (5 Results) |
| Here, the Make3D baseline is well-suited to the dataset, being composed of horizontally aligned images, and achieves relatively good results. | comparison identity and matched condition | p. 7 (5 Results) |
| Figure 1: Model architecture. as vanishing points, object locations, and room alignment. A local view (as is commonly used for stereo matching) is insufficient ... | comparison identity and matched condition | p. 3 (Figure/Table caption) |
| Mean Make3D Coarse Coarse + Fine threshold δ < 1.25 0.556 0.601 0.679 0.692 higher threshold δ < 1.252 0.752 0.820 0.897 0.899 is ... | comparison identity and matched condition | p. 7 (5 Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 3 shows Make3D performing much better on this data, as expected, while using the scale-invariant error as a loss seems to have little effect ... | component/input/data sensitivity | p. 7 (5 Results) |
| To remove many invalid regions caused by windows, open doorways and specular surfaces we also mask out depths equal to the minimum or maximum ... | component/input/data sensitivity | p. 5 (4 Experiments) |
| We evaluate each method using several errors from prior works, as well as our scale-invariant metric: Threshold: % of yi s.t. max( yi y∗ ... | component/input/data sensitivity | p. 6 (4 Experiments) |
| 4, sorted top-to-bottom by scale-invariant MSE. | component/input/data sensitivity | p. 6 (5 Results) |
| Just as importantly, there is a 25% gain in both the scale-dependent and scale-invariant RMSE errors, showing there is substantial improvement in the predicted ... | component/input/data sensitivity | p. 7 (5 Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper we present a new approach for estimating depth from a single image. | Figure 3: Qualitative comparison of Make3D, our method trained with l2 loss (λ = 0), and our method trained with both l2 and scale-invariant ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (Figure/Table caption), p. 6 (5 Results), p. 6 (5 Results), p. 7 (5 Results) |
| Primary metric/result | Our system achieves the best performance on all metrics, obtaining an average 35% relative gain compared to the runner-up. | numeric claim only at cited anchor | p. 6 (5 Results) |

- Numeric sentences retained from the body:
- **p. 5 / 4 Experiments - extractive PDF cue:** We use the official train/test split, using 249 scenes for training and 215 for testing, and construct our training set using the raw data for ...
- **p. 5 / 4 Experiments - extractive PDF cue:** We use 56 scenes from the "city," "residential," and "road" 2For KITTI, s ∈[1, 1.2], and rotations are not performed (images are horizontal from the ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In future work, we plan to extend our method to incorporate further 3D geometry information, such as surface normals. | p. 7 (6 Discussion) |
| body limitation/failure cue | Although the fine-scale network does not improve in the error measurements, its effect is clearly visible in the depth maps - surface boundaries have ... | p. 6 (5 Results) |
| body limitation/failure cue | Again, the fine-scale network does not improve much over the coarse one in the error metrics, but differences between the two can be seen ... | p. 7 (5 Results) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Learning rates are: 0.001 for coarse convolutional layers 1-5, 0.1 for coarse full layers 6 and 7, 0.001 for fine layers 1 and 3, ... | p. 5 (4 Experiments) |
| Learning rates are the same as for NYU Depth. | p. 6 (4 Experiments) |
| These ratios were found by trial-and-error on a validation set (folded back into the training set for our final evaluations), and the global scale ... | p. 5 (4 Experiments) |
| As an additional reference, we also compare to the mean depth image computed across the training set. | p. 6 (4 Experiments) |
| Rather than limiting the output to the feature map size and relying on hardcoded upsampling before passing the prediction to the fine network, we ... | p. 3 (3 Approach) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 6 Discussion - extractive PDF cue:** In future work, we plan to extend our method to incorporate further 3D geometry information, such as surface normals.
- **p. 6 / 5 Results - extractive PDF cue:** Although the fine-scale network does not improve in the error measurements, its effect is clearly visible in the depth maps - surface boundaries have sharper ...
- **p. 7 / 5 Results - extractive PDF cue:** Again, the fine-scale network does not improve much over the coarse one in the error metrics, but differences between the two can be seen in ...

- **PDF anchors reviewed:** datasets p. 5 (4 Experiments), p. 5 (4 Experiments), p. 6 (4 Experiments), p. 6 (4 Experiments), p. 7 (5 Results), p. 7 (5 Results), metrics p. 5 (4 Experiments), p. 7 (5 Results), p. 6 (5 Results), p. 6 (4 Experiments), p. 7 (5 Results), p. 5 (4 Experiments), baselines p. 6 (4 Experiments), p. 6 (5 Results), p. 7 (5 Results), p. 3 (Figure/Table caption), p. 7 (5 Results), results p. 7 (Figure/Table caption), p. 6 (5 Results), p. 6 (5 Results), p. 7 (5 Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
