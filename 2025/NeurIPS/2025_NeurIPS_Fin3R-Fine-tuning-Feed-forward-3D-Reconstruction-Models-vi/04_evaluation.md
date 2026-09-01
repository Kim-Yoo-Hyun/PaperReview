# Evaluation - Fin3R: Fine-tuning Feed-forward 3D Reconstruction Models via Monocular Knowledge Distillation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (34 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=pZIeK0Xvph; PDF retrieval source: https://openreview.net/pdf/7543305cf2956c454b415330b7bf04eda9e451f9.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4 Experiment), p. 9 (4 Experiment), p. 10 (4.7 Discussion), p. 6 (4 Experiment), p. 7 (4 Experiment), p. 9 (4 Experiment)): The results indicate that models enhanced with our distillation method consistently achieve lower Acc and Comp as well as improved NC scores across most baselines.

## Evaluation Body Digest

- **p. 8 / 4 Experiment - extractive PDF cue:** Method ETH3D [49] T&T [27] KITTI [58] Sintel [6] Bonn [40] rel ↓ δ1 ↑ rel ↓ δ1 ↑ rel ↓ δ1 ↑ rel ↓ ...
- **p. 7 / 4 Experiment - extractive PDF cue:** 4.2 Relative Pose Estimation Table 2 summarizes our evaluation of relative pose estimation on the ScanNet dataset [10].
- **p. 7 / 4 Experiment - extractive PDF cue:** The fine-tuned versions of CUT3R and VGGT consistently outperform their respective baselines across datasets spanning diverse domains.
- **p. 9 / 4 Experiment - extractive PDF cue:** 7-Scenes [52] NRGBD [2] Acc↓ Comp↓ NC↑ Acc↓ Comp↓ NC↑ Method Mean Med.
- **p. 9 / 4 Experiment - extractive PDF cue:** The first two columns report mean monocular depth metrics (see Table 1), while the final column details the 7-Scenes [52] accuracy.
- **p. 10 / 4.7 Discussion - extractive PDF cue:** This underscores the necessity of including in-the-wild data alongside highquality datasets during training to achieve optimal results.
- **p. 10 / 4.7 Discussion - extractive PDF cue:** We attribute this improvement primarily to the incorporation of unlabeled datasets, which enhance the model's robustness and overall performance.
- **p. 6 / 4 Experiment - extractive PDF cue:** The table shows that our integrated models consistently achieve lower relative depth error and higher δ1 scores.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiment (p. 6); A Experiment Details (p. 23); A.2 Evaluation Details (p. 23); B Additional Experiments (p. 24).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiment | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results indicate that models enhanced with our distillation method consistently achieve lower Acc and Comp as well as improved NC scores across most ... | p. 8 (4 Experiment) |
| 4 Experiment | EMPIRICAL / SOURCE-REPORTED EVALUATION | Together, these results highlight that monocular finetuning with high-quality pseudo-labels from the diverse dataset improves both single-view and multi-view accuracy. | p. 9 (4 Experiment) |
| 4.7 Discussion | EMPIRICAL / SOURCE-REPORTED EVALUATION | This underscores the necessity of including in-the-wild data alongside highquality datasets during training to achieve optimal results. | p. 10 (4.7 Discussion) |
| 4 Experiment | EMPIRICAL / SOURCE-REPORTED EVALUATION | The table shows that our integrated models consistently achieve lower relative depth error and higher δ1 scores. | p. 6 (4 Experiment) |
| 4 Experiment | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results indicate that our fine-tuning method consistently improves the baseline model correspondence by improving the geometry. | p. 7 (4 Experiment) |

## Dataset / Benchmark Role

- **p. 8 / 4 Experiment - extractive PDF cue:** Method ETH3D [49] T&T [27] KITTI [58] Sintel [6] Bonn [40] rel ↓ δ1 ↑ rel ↓ δ1 ↑ rel ↓ δ1 ↑ rel ↓ ...
- **p. 7 / 4 Experiment - extractive PDF cue:** 4.2 Relative Pose Estimation Table 2 summarizes our evaluation of relative pose estimation on the ScanNet dataset [10].
- **p. 7 / 4 Experiment - extractive PDF cue:** The fine-tuned versions of CUT3R and VGGT consistently outperform their respective baselines across datasets spanning diverse domains.
- **p. 9 / 4 Experiment - extractive PDF cue:** 7-Scenes [52] NRGBD [2] Acc↓ Comp↓ NC↑ Acc↓ Comp↓ NC↑ Method Mean Med.
- **p. 9 / 4 Experiment - extractive PDF cue:** The first two columns report mean monocular depth metrics (see Table 1), while the final column details the 7-Scenes [52] accuracy.
- **p. 10 / 4.7 Discussion - extractive PDF cue:** This underscores the necessity of including in-the-wild data alongside highquality datasets during training to achieve optimal results.
- **p. 10 / 4.7 Discussion - extractive PDF cue:** We attribute this improvement primarily to the incorporation of unlabeled datasets, which enhance the model's robustness and overall performance.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1: Fin3R consistently improves the reconstructed geometry quality in DUSt3R, MASt3R, CUT3R, and VGGT, recovering finer details and producing sharper boundaries. ∗Corresponding author. 39th ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Analysis of scale uncertainty and error metrics. (a) Two views of a red cube are connected by a blue epipolar line. Gaussian distributions ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Heatmaps show spatial variations in L2 norms of encoder patch tokens across configurations. "Avg" is the average norm of the feature map, and ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4: Pipeline of our method. Green dashed lines denote pointmap supervision; pur- ple dashed lines indicate distillation supervision. Based on these observations, we introduce ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1: Quantitative results for monocular depth estimation. "+Ours" denotes the integration of our fine-tuning, and MoGe is the teacher model. Best results in each ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5: Depth prediction across baseline models. ⋆indicates integration with our method. discussed in Section 3.1. We also present the fine-tuned MASt3R model with metric ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Relative Camera Pose Evaluation on the ScanNet1500 [10, 47] datasets. "Ours" in- dicates the integration of our distillation method. Better results are highlighted ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3: Quantitative Results for Multi- view Pose Estimation on RealEstate10k [88]. "Ours" is the fine-tuned model using our method. Better results are highlighted in ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Method ETH3D [49] T&T [27] KITTI [58] Sintel [6] Bonn [40] rel ↓ δ1 ↑ rel ↓ δ1 ↑ rel ↓ δ1 ↑ rel ... | embodiment, simulator version and control stack | p. 8 (4 Experiment), p. 7 (4 Experiment) |
| Task/environment | 4.2 Relative Pose Estimation Table 2 summarizes our evaluation of relative pose estimation on the ScanNet dataset [10]. | reset, timeout, object/scene variation | p. 7 (4 Experiment), p. 7 (4 Experiment) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (3 Method), p. 4 (3 Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (3 Method), p. 2 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| The table shows that our integrated models consistently achieve lower relative depth error and higher δ1 scores. | definition/direction/unit from same section | p. 6 (4 Experiment) |
| Figure 2: Analysis of scale uncertainty and error metrics. (a) Two views of a red cube are connected by a blue epipolar line. Gaussian ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Combining all our strategies yields the highest accuracy. | definition/direction/unit from same section | p. 9 (4 Experiment) |
| Confidence and Fine Details: During our experiments, we observed that models like VGGT often produce blurry geometry accompanied by low confidence scores, as shown ... | definition/direction/unit from same section | p. 10 (4.7 Discussion) |
| We report mean and median values for three metrics: accuracy (Acc), completeness (Comp), and normal consistency (NC). | definition/direction/unit from same section | p. 8 (4 Experiment) |
| The results indicate that models enhanced with our distillation method consistently achieve lower Acc and Comp as well as improved NC scores across most ... | definition/direction/unit from same section | p. 8 (4 Experiment) |
| The first two columns report mean monocular depth metrics (see Table 1), while the final column details the 7-Scenes [52] accuracy. | definition/direction/unit from same section | p. 9 (4 Experiment) |
| This underscores the necessity of including in-the-wild data alongside highquality datasets during training to achieve optimal results. | definition/direction/unit from same section | p. 10 (4.7 Discussion) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Interestingly, we observe that although DUSt3R's depth estimates rank last among the evaluated models, they exhibit the sharpest boundaries compared with the other two ... | comparison identity and matched condition | p. 6 (4 Experiment) |
| The fine-tuned versions of CUT3R and VGGT consistently outperform their respective baselines across datasets spanning diverse domains. | comparison identity and matched condition | p. 7 (4 Experiment) |
| Fine-tuned VGGT performs almost as well as the state-of-the-art expert model, MoGe. | comparison identity and matched condition | p. 6 (4 Experiment) |
| The results indicate that our fine-tuning method consistently improves the baseline model correspondence by improving the geometry. | comparison identity and matched condition | p. 7 (4 Experiment) |
| The results indicate that models enhanced with our distillation method consistently achieve lower Acc and Comp as well as improved NC scores across most ... | comparison identity and matched condition | p. 8 (4 Experiment) |
| 4.5 Multi-view Pose Estimation Table 3 summarizes the performance of baseline models and our fine-tuned methods on the RealEstate10k [88] dataset. | comparison identity and matched condition | p. 9 (4 Experiment) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Since the depth predicted by MoGe is affine-invariant, we subtract the shift in the z-component and then apply the normalization used in DUSt3R. | component/input/data sensitivity | p. 6 (4 Experiment) |
| Teacher SA-1B Rel (↓) δ1 (↑) Acc (↓) ✗ ✗ ✗ 5.68 94.1 0.017 ✓ ✗ ✗ 5.21 95.0 0.014 ✗ ✓ ✗ 5.00 ... | component/input/data sensitivity | p. 9 (4 Experiment) |
| The top row represents VGGT model without fine-tuning, which can benefit from single-view distillation (second row) on a subset of training datasets (see appendix) ... | component/input/data sensitivity | p. 9 (4 Experiment) |
| Since CUT3R [65] is designed for long sequences and unsuitable for pairwise correspondences, we remove it in the two-view evaluation. | component/input/data sensitivity | p. 6 (4 Experiment) |
| Because both DUSt3R and VGGT produce scale-invariant point maps, we apply Umeyama alignment [59] to align scale. | component/input/data sensitivity | p. 8 (4 Experiment) |
| This demonstrates that a robustly trained encoder benefits downstream heads even without direct supervision. | component/input/data sensitivity | p. 10 (4.7 Discussion) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To directly address this challenge, we propose a refined integration of LoRA with a re-normalization strategy specifically designed to constrain feature norm drift. | The results indicate that models enhanced with our distillation method consistently achieve lower Acc and Comp as well as improved NC scores across most ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4 Experiment), p. 9 (4 Experiment), p. 10 (4.7 Discussion), p. 6 (4 Experiment), p. 7 (4 Experiment), p. 9 (4 Experiment) |
| Primary metric/result | Together, these results highlight that monocular finetuning with high-quality pseudo-labels from the diverse dataset improves both single-view and multi-view accuracy. | numeric claim only at cited anchor | p. 9 (4 Experiment) |

- Numeric sentences retained from the body:
- **p. 6 / 4 Experiment - extractive PDF cue:** Training runs for 10 epochs on four NVIDIA L20 GPUs over a single day.
- **p. 7 / 4 Experiment - extractive PDF cue:** Following [47], we assess performance using area-under-the-curve (AUC) metrics computed at thresholds of 5, 10, and 20 degrees.
- **p. 8 / 4 Experiment - extractive PDF cue:** Method ETH3D [49] T&T [27] KITTI [58] Sintel [6] Bonn [40] rel ↓ δ1 ↑ rel ↓ δ1 ↑ rel ↓ δ1 ↑ rel ↓ ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Note that VGGT is not trained on dynamic datasets, so its performance bottleneck may stem from dataset limitations rather than our fine-tuning method. | p. 7 (4 Experiment) |
| body limitation/failure cue | This demonstrates that a robustly trained encoder benefits downstream heads even without direct supervision. | p. 10 (4.7 Discussion) |
| body limitation/failure cue | We attribute this improvement primarily to the incorporation of unlabeled datasets, which enhance the model's robustness and overall performance. | p. 10 (4.7 Discussion) |
| body limitation/failure cue | This is likely because CUT3R and VGGT are trained on long sequences and are consequently more affected by the long-sequence degradation 6 | p. 6 (4 Experiment) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| By carefully fine-tuning the encoder, it avoids the resource-intensive decoder tuning, which typically requires long-sequence inputs from diverse datasets with large batch sizes. | p. 10 (4.7 Discussion) |
| Further implementation details are provided in the appendix. | p. 6 (4 Experiment) |
| Training runs for 10 epochs on four NVIDIA L20 GPUs over a single day. | p. 6 (4 Experiment) |
| Following [47], we assess performance using area-under-the-curve (AUC) metrics computed at thresholds of 5, 10, and 20 degrees. | p. 7 (4 Experiment) |
| We attribute this improvement to the decoder functioning as an implicit feature matcher, which allows it to leverage the enhanced feature details for more ... | p. 9 (4 Experiment) |
| This demonstrates that a robustly trained encoder benefits downstream heads even without direct supervision. | p. 10 (4.7 Discussion) |
| Pointmap Head Self-View Head LoRA🔥 Labeled Multi-View ~10% Data Decoder❄ | p. 5 (3 Method) |
| We contend that the limitations in detail recovery primarily originate from the encoder. | p. 5 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 4 Experiment - extractive PDF cue:** Note that VGGT is not trained on dynamic datasets, so its performance bottleneck may stem from dataset limitations rather than our fine-tuning method.
- **p. 10 / 4.7 Discussion - extractive PDF cue:** This demonstrates that a robustly trained encoder benefits downstream heads even without direct supervision.
- **p. 10 / 4.7 Discussion - extractive PDF cue:** We attribute this improvement primarily to the incorporation of unlabeled datasets, which enhance the model's robustness and overall performance.
- **p. 6 / 4 Experiment - extractive PDF cue:** This is likely because CUT3R and VGGT are trained on long sequences and are consequently more affected by the long-sequence degradation 6

- **PDF anchors reviewed:** datasets p. 8 (4 Experiment), p. 7 (4 Experiment), p. 7 (4 Experiment), p. 9 (4 Experiment), p. 9 (4 Experiment), p. 10 (4.7 Discussion), metrics p. 6 (4 Experiment), p. 4 (Figure/Table caption), p. 9 (4 Experiment), p. 10 (4.7 Discussion), p. 8 (4 Experiment), p. 8 (4 Experiment), baselines p. 6 (4 Experiment), p. 7 (4 Experiment), p. 6 (4 Experiment), p. 7 (4 Experiment), p. 8 (4 Experiment), p. 9 (4 Experiment), results p. 8 (4 Experiment), p. 9 (4 Experiment), p. 10 (4.7 Discussion), p. 6 (4 Experiment), p. 7 (4 Experiment), p. 9 (4 Experiment).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
