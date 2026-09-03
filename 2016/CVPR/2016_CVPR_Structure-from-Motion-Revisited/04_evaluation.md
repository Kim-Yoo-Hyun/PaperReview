# Evaluation - Structure-from-Motion Revisited

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content_cvpr_2016/html/Schonberger_Structure-From-Motion_Revisited_CVPR_2016_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content_cvpr_2016/papers/Schonberger_Structure-From-Motion_Revisited_CVPR_2016_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (7.82 M), p. 8 (7.82 M), p. 4 (Figure/Table caption), p. 7 (5. Experiments), p. 7 (5. Experiments)): For all datasets, we significantly outperform any other method in terms of completeness, especially for the larger models.

## Evaluation Body Digest

- **p. 7 / 5. Experiments - extractive body cue:** An experiment on the Dubrovnik dataset (Fig.
- **p. 7 / 5. Experiments - extractive body cue:** Triangulation statistics for Dubrovnik dataset.
- **p. 8 / 7.82 M - extractive body cue:** For each dataset, we report the largest reconstructed component.
- **p. 8 / 7.82 M - extractive body cue:** For all datasets, we significantly outperform any other method in terms of completeness, especially for the larger models.
- **p. 7 / 5. Experiments - extractive body cue:** After each image registration, we measure the number of registered images shared between the strategies (intersection over union) and the reconstruction error as the median ...
- **p. 7 / 5. Experiments - extractive body cue:** 5) compares our method (Pyramid) to existing strategies in terms of the reconstruction error.
- **p. 8 / 7.82 M - extractive body cue:** We encourage readers to view the supplementary material for additional visual comparisons of the results, demonstrating the superior robustness, completeness, and accuracy of our method.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Scores for different number of points (left and right) with different distributions (top and bottom) in the image for L = 3. late ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 5. Experiments (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 7.82 M | EMPIRICAL / SOURCE-REPORTED EVALUATION | For all datasets, we significantly outperform any other method in terms of completeness, especially for the larger models. | p. 8 (7.82 M) |
| 7.82 M | EMPIRICAL / SOURCE-REPORTED EVALUATION | In addition, we achieve the best pose accuracy for the Quad dataset: DISCO 1.16m, Bundler 1.01m, VisualSFM 0.89m, and Ours 0.85m. | p. 8 (7.82 M) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 3. Scores for different number of points (left and right) with different distributions (top and bottom) in the image for L = 3. ... | p. 4 (Figure/Table caption) |
| 5. Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 1Results for Theia kindly provided by the authors [55]. | p. 7 (5. Experiments) |
| 5. Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 4) evaluates how well the score S reflects the number and distribution of points. | p. 7 (5. Experiments) |

## Dataset / Benchmark Role

- **p. 7 / 5. Experiments - extractive body cue:** An experiment on the Dubrovnik dataset (Fig.
- **p. 7 / 5. Experiments - extractive body cue:** Triangulation statistics for Dubrovnik dataset.
- **p. 8 / 7.82 M - extractive body cue:** For each dataset, we report the largest reconstructed component.
- **p. 8 / 7.82 M - extractive body cue:** For all datasets, we significantly outperform any other method in terms of completeness, especially for the larger models.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Result of Rome with 21K registered out of 75K images.
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2. Incremental Structure-from-Motion pipeline. Matching. Next, SfM discovers images that see the same scene part by leveraging the features Fi as an appearance description ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Scores for different number of points (left and right) with different distributions (top and bottom) in the image for L = 3. late ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Next best view scores for Gaussian distributed points xj ∈[0, 1]×[0, 1] with mean µ and std. dev. σ. Score S w.r.t. uni- ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Next best view results for Quad: Shared number of reg- istered images and reconstruction error during incremental SfM. 0 0.2 0.4 0.6 0.8 ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6. Triangulation statistics for Dubrovnik dataset. Left: Out- lier ratio distribution of feature tracks. Right: Average number of samples required to triangulate N-view point. ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 7. Average relative runtimes using standard global BA and exhaustive, rec. triangulation (1), and grouped BA and RANSAC, rec. triangulation (2). Runtime for Initialization ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1. Reconstruction results for state-of-the-art SfM systems on large-scale unordered Internet photo collections. #Points #Elements Avg. Track Length #Samples Bundler 713,824

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | An experiment on the Dubrovnik dataset (Fig. | embodiment, simulator version and control stack | p. 7 (5. Experiments), p. 7 (5. Experiments) |
| Task/environment | Triangulation statistics for Dubrovnik dataset. | reset, timeout, object/scene variation | p. 7 (5. Experiments), p. 8 (7.82 M) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 2 (2.2. Incremental Reconstruction), p. 1 (1. Introduction) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 2 (2.2. Incremental Reconstruction), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| After each image registration, we measure the number of registered images shared between the strategies (intersection over union) and the reconstruction error as the ... | definition/direction/unit from same section | p. 7 (5. Experiments) |
| 5) compares our method (Pyramid) to existing strategies in terms of the reconstruction error. | definition/direction/unit from same section | p. 7 (5. Experiments) |
| We encourage readers to view the supplementary material for additional visual comparisons of the results, demonstrating the superior robustness, completeness, and accuracy of our ... | definition/direction/unit from same section | p. 8 (7.82 M) |
| Figure 3. Scores for different number of points (left and right) with different distributions (top and bottom) in the image for L = 3. ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| In addition, we achieve the best pose accuracy for the Quad dataset: DISCO 1.16m, Bundler 1.01m, VisualSFM 0.89m, and Ours 0.85m. | definition/direction/unit from same section | p. 8 (7.82 M) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We run experiments on a large variety of datasets to evaluate both the proposed components and the overall system compared to state-of-the-art incremental (Bundler ... | comparison identity and matched condition | p. 7 (5. Experiments) |
| 9 shows a result of Bundler compared to our method. | comparison identity and matched condition | p. 8 (7.82 M) |
| For all datasets, we significantly outperform any other method in terms of completeness, especially for the larger models. | comparison identity and matched condition | p. 8 (7.82 M) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 4. Next best view scores for Gaussian distributed points xj ∈[0, 1]×[0, 1] with mean µ and std. dev. σ. Score S w.r.t. ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| We run experiments on a large variety of datasets to evaluate both the proposed components and the overall system compared to state-of-the-art incremental (Bundler ... | component/input/data sensitivity | p. 7 (5. Experiments) |
| For each dataset, we report the largest reconstructed component. | component/input/data sensitivity | p. 8 (7.82 M) |
| Reconstruction of Gendarmenmarkt [61] for Bundler (left) and our method (right). of the overall system and thereby also evaluate the performance of the individual ... | component/input/data sensitivity | p. 8 (7.82 M) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we propose a new SfM algorithm to approach this ultimate goal. | For all datasets, we significantly outperform any other method in terms of completeness, especially for the larger models. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (7.82 M), p. 8 (7.82 M), p. 4 (Figure/Table caption), p. 7 (5. Experiments), p. 7 (5. Experiments) |
| Primary metric/result | In addition, we achieve the best pose accuracy for the Quad dataset: DISCO 1.16m, Bundler 1.01m, VisualSFM 0.89m, and Ours 0.85m. | numeric claim only at cited anchor | p. 8 (7.82 M) |

- Numeric sentences retained from the body:
- **p. 8 / 7.82 M - extractive body cue:** The RANSAC-based approach yields just marginally inferior tracks but is much faster (10-40x).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The proposed components of the algorithm improve the state of the art in terms of completeness, robustness, accuracy, and efficiency. | p. 8 (6. Conclusion) |
| body limitation/failure cue | Figure 3. Scores for different number of points (left and right) with different distributions (top and bottom) in the image for L = 3. ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Robust and Efficient Triangulation. | p. 7 (5. Experiments) |
| body limitation/failure cue | The reconstruction quality is comparable for all choices of V > 0.3 and increasingly degrades for a smaller V . | p. 8 (7.82 M) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Runtime for Initialization and Next Best View Selection (all strategies) is smaller than 0.1%. | p. 7 (5. Experiments) |
| Average relative runtimes using standard global BA and exhaustive, rec. triangulation (1), and grouped BA and RANSAC, rec. triangulation (2). | p. 7 (5. Experiments) |
| Using V = 0.4, the runtime of the entire pipeline for Colosseum reduces by 36% yet results in an equivalent reconstruction. | p. 8 (7.82 M) |
| The effective speedup of the total runtime is 5% (V = 0.6), 14% (V = 0.3) and 32% (V = 0.1), while the average ... | p. 8 (7.82 M) |
| Moreover, the robustness, accuracy, and performance of the reconstruction depends on the seed location of the incremental process. | p. 2 (2.2. Incremental Reconstruction) |
| In contrast, initializing from a sparser location results in lower runtimes, since BAs deal with overall sparser problems accumulated over the reconstruction process. | p. 2 (2.2. Incremental Reconstruction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6. Conclusion - extractive body cue:** The proposed components of the algorithm improve the state of the art in terms of completeness, robustness, accuracy, and efficiency.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Scores for different number of points (left and right) with different distributions (top and bottom) in the image for L = 3. late ...
- **p. 7 / 5. Experiments - extractive body cue:** Robust and Efficient Triangulation.
- **p. 8 / 7.82 M - extractive body cue:** The reconstruction quality is comparable for all choices of V > 0.3 and increasingly degrades for a smaller V .

- **Evidence anchors reviewed:** datasets p. 7 (5. Experiments), p. 7 (5. Experiments), p. 8 (7.82 M), p. 8 (7.82 M), metrics p. 7 (5. Experiments), p. 7 (5. Experiments), p. 8 (7.82 M), p. 4 (Figure/Table caption), p. 8 (7.82 M), baselines p. 7 (5. Experiments), p. 8 (7.82 M), p. 8 (7.82 M), results p. 8 (7.82 M), p. 8 (7.82 M), p. 4 (Figure/Table caption), p. 7 (5. Experiments), p. 7 (5. Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
