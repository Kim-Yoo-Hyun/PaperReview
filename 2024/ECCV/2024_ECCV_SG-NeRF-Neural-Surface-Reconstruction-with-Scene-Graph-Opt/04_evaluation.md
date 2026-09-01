# Evaluation - SG-NeRF: Neural Surface Reconstruction with Scene Graph Optimization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/8870_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/08870.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 13 (7.71 3.77†), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 13 (7.71 3.77†), p. 14 (7.71 3.77†), p. 14 (7.71 3.77†)): While BARF* achieves the best results in scene 37, it is more likely to impose negative impact on camera poses, thereby has worse performance in most scenes.

## Evaluation Body Digest

- **p. 10 / 4 Experiments - extractive PDF cue:** We then report the comparisons with state-of-the-art methods on both the proposed dataset and a widely used benchmark, DTU dataset [21] (Sec.
- **p. 13 / 7.71 3.77† - extractive PDF cue:** We select three representative scenes from the proposed dataset and conduct ablation studies to evaluate the effectiveness of each component.
- **p. 10 / 4 Experiments - extractive PDF cue:** After SfM, to prune the scene graph, we set the angular threshold to τ = 70 degrees for our dataset.
- **p. 11 / 4 Experiments - extractive PDF cue:** 4.3 Comparisons We compare our method with existing approaches on the proposed dataset and the DTU dataset.
- **p. 11 / 4 Experiments - extractive PDF cue:** Our method runs in average 11 hours for 150k iterations on the proposed dataset, and 18 hours for 300k iterations on the DTU dataset.
- **p. 12 / 4 Experiments - extractive PDF cue:** 6: Qualitative comparison on the DTU dataset (top five).
- **p. 12 / 4 Experiments - extractive PDF cue:** We also compare with recent work PoRF [2] on our dataset.
- **p. 13 / 7.71 3.77† - extractive PDF cue:** SG-NeRF (Ours) 0.87 2.39 0.88 0.38 1.13 1.13 Results on the DTU dataset.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4 Experiments (p. 10).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 7.71 3.77† | EMPIRICAL / SOURCE-REPORTED EVALUATION | While BARF* achieves the best results in scene 37, it is more likely to impose negative impact on camera poses, thereby has worse performance ... | p. 13 (7.71 3.77†) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Overall, our method achieves the best reconstruction results. | p. 11 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | In contrast, our method shows robustness to pose errors and outperforms NeuS by 61% in Chamfer distance and by 15% in F-score. | p. 12 (4 Experiments) |
| 7.71 3.77† | EMPIRICAL / SOURCE-REPORTED EVALUATION | Compared to the competitors, our method achieves the best overall performance among all the methods. | p. 13 (7.71 3.77†) |
| 7.71 3.77† | EMPIRICAL / SOURCE-REPORTED EVALUATION | Notably, images with larger pose errors exhibit lower scores, and this gap increases as the refinement progresses, during which, the inlier poses are sampled ... | p. 14 (7.71 3.77†) |

## Dataset / Benchmark Role

- **p. 10 / 4 Experiments - extractive PDF cue:** We then report the comparisons with state-of-the-art methods on both the proposed dataset and a widely used benchmark, DTU dataset [21] (Sec.
- **p. 13 / 7.71 3.77† - extractive PDF cue:** We select three representative scenes from the proposed dataset and conduct ablation studies to evaluate the effectiveness of each component.
- **p. 10 / 4 Experiments - extractive PDF cue:** After SfM, to prune the scene graph, we set the angular threshold to τ = 70 degrees for our dataset.
- **p. 11 / 4 Experiments - extractive PDF cue:** 4.3 Comparisons We compare our method with existing approaches on the proposed dataset and the DTU dataset.
- **p. 11 / 4 Experiments - extractive PDF cue:** Our method runs in average 11 hours for 150k iterations on the proposed dataset, and 18 hours for 300k iterations on the DTU dataset.
- **p. 12 / 4 Experiments - extractive PDF cue:** 6: Qualitative comparison on the DTU dataset (top five).
- **p. 12 / 4 Experiments - extractive PDF cue:** We also compare with recent work PoRF [2] on our dataset.
- **p. 13 / 7.71 3.77† - extractive PDF cue:** SG-NeRF (Ours) 0.87 2.39 0.88 0.38 1.13 1.13 Results on the DTU dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1: 3D surface reconstruction (meshes) from images with camera poses that present significant noise. Directly training radiance fields with noisy poses can lead to ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 2: An overview of the proposed joint learning pipeline. Given a set of images, we first apply a Structure-from-Motion (SfM) algorithm to construct an ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 3: Visualization of matches that are falsely established as correspondences from non-overlapping regions. The results are obtained using COLMAP [40] with Super- Point [12] ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Fig. 4: Illustration of the two-view intersection-over-union (IoU) loss in 2D that can be easily extended into 3D. Given a pair of matched keypoints from ...
- **p. 11 / Figure/Table caption - extractive PDF cue:** Table 1: Quantitative results on our dataset. The red and blue numbers indicate the first and second performer for each scene. † denotes that only ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Fig. 5: Qualitative comparisons on the proposed dataset. As shown, our method is more robust to outlier poses, producing less distortion and better geometric detail. ...
- **p. 12 / Figure/Table caption - extractive PDF cue:** Fig. 6: Qualitative comparison on the DTU dataset (top five). Neuralangelo shows detailed windows but struggles with the gap area between buildings. In contrast, our ...
- **p. 13 / Figure/Table caption - extractive PDF cue:** Table 2: Quantitative results on the DTU dataset with noisy camera poses as input. Chamfer distance ↓ 24 37 40 55 63

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We then report the comparisons with state-of-the-art methods on both the proposed dataset and a widely used benchmark, DTU dataset [21] (Sec. | embodiment, simulator version and control stack | p. 10 (4 Experiments), p. 13 (7.71 3.77†) |
| Task/environment | We select three representative scenes from the proposed dataset and conduct ablation studies to evaluate the effectiveness of each component. | reset, timeout, object/scene variation | p. 13 (7.71 3.77†), p. 10 (4 Experiments) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 5 (3 Method), p. 7 (3 Method) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 5 (3 Method), p. 9 (3 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 3: Quantitative results of our ablation studies. We individually remove the use of sparsification by thresholding (w/o τ), confidence estimation (w/o CS), Intersection- ... | definition/direction/unit from same section | p. 14 (Figure/Table caption) |
| In contrast, our method shows robustness to pose errors and outperforms NeuS by 61% in Chamfer distance and by 15% in F-score. | definition/direction/unit from same section | p. 12 (4 Experiments) |
| 7: The correlation between confidence scores and actual camera pose errors. | definition/direction/unit from same section | p. 14 (7.71 3.77†) |
| We follow the hierarchical sampling strategy in NeuS and set the batch size to 512, among which, we select 16 matched keypoints and use ... | definition/direction/unit from same section | p. 10 (4 Experiments) |
| By disabling the use of the confidence score (w/o CS), an even larger performance drop is observed. | definition/direction/unit from same section | p. 13 (7.71 3.77†) |
| Similar performance drop is also observed when we remove the IoU term from the loss function (w/o IoU). | definition/direction/unit from same section | p. 13 (7.71 3.77†) |
| 6) as 1.0 to balance the initial and updated confidence scores. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| We follow the evaluation protocol in the literature [24,49] and report Chamfer distance and F-score for evaluating the mesh quality. | definition/direction/unit from same section | p. 11 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We then report the comparisons with state-of-the-art methods on both the proposed dataset and a widely used benchmark, DTU dataset [21] (Sec. | comparison identity and matched condition | p. 10 (4 Experiments) |
| We compare our method with our backbone model NeuS [49] and the state-of-the-art Neuralangelo [24]. | comparison identity and matched condition | p. 11 (4 Experiments) |
| Specifically, we select BARF [25], SCNeRF [22], GARF [8], L2G-NeRF [6], and Joint-TensoRF [7] as the baselines. | comparison identity and matched condition | p. 11 (4 Experiments) |
| In contrast, our method shows robustness to pose errors and outperforms NeuS by 61% in Chamfer distance and by 15% in F-score. | comparison identity and matched condition | p. 12 (4 Experiments) |
| Compared to the competitors, our method achieves the best overall performance among all the methods. | comparison identity and matched condition | p. 13 (7.71 3.77†) |
| A noticeable performance drop is observed when compared to our full method (as indicated by w/o τ in the table). | comparison identity and matched condition | p. 13 (7.71 3.77†) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Furthermore, we perform a series of ablation studies and analyses to verify the effectiveness of each proposed component (Sec. | component/input/data sensitivity | p. 10 (4 Experiments) |
| We select three representative scenes from the proposed dataset and conduct ablation studies to evaluate the effectiveness of each component. | component/input/data sensitivity | p. 13 (7.71 3.77†) |
| To evaluate the effectiveness of the joint optimization, we directly train our method using the original scene graph obtained from SfM without further refinement. | component/input/data sensitivity | p. 13 (7.71 3.77†) |
| Table 3: Quantitative results of our ablation studies. We individually remove the use of sparsification by thresholding (w/o τ), confidence estimation (w/o CS), Intersection- ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| Fig. 3: Visualization of matches that are falsely established as correspondences from non-overlapping regions. The results are obtained using COLMAP [40] with Super- Point ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Following hloc [37], we replace the keypoints and the matching module with SuperPoint [12] and SuperGlue [38], respectively. | component/input/data sensitivity | p. 10 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we propose a novel framework that jointly optimizes the neural radiance field with a scene graph to alleviate the influence of ... | While BARF* achieves the best results in scene 37, it is more likely to impose negative impact on camera poses, thereby has worse performance ... | PDF body cue; verify exact table/figure and matched conditions | p. 13 (7.71 3.77†), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 13 (7.71 3.77†), p. 14 (7.71 3.77†), p. 14 (7.71 3.77†) |
| Primary metric/result | Overall, our method achieves the best reconstruction results. | numeric claim only at cited anchor | p. 11 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 10 / 4 Experiments - extractive PDF cue:** After SfM, to prune the scene graph, we set the angular threshold to τ = 70 degrees for our dataset.
- **p. 10 / 4 Experiments - extractive PDF cue:** For the DTU dataset, we set τ = 45 degrees because the viewpoints are more densely sampled.
- **p. 10 / 4 Experiments - extractive PDF cue:** The MoG of each ray is calculated using 8 points with the highest densities.
- **p. 11 / 4 Experiments - extractive PDF cue:** All of the experiments are conducted on NVIDIA RTX 3090 GPUs.
- **p. 11 / 4 Experiments - extractive PDF cue:** Our method runs in average 11 hours for 150k iterations on the proposed dataset, and 18 hours for 300k iterations on the DTU dataset.
- **p. 5 / 3 Method - extractive PDF cue:** 3.1 Scene Graph A scene graph G = (V, E) in SfM consists of a set of nodes V and edges E.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 1: 3D surface reconstruction (meshes) from images with camera poses that present significant noise. Directly training radiance fields with noisy poses can lead ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Even though our method can greatly refine the inlier poses, the improvement on outlier poses is moderate (whose effect is still largely alleviated with ... | p. 14 (5 Conclusion) |
| body limitation/failure cue | Please also note that there are several failure cases from the competitors indicating completely incorrect reconstruction. | p. 13 (4 Experiments) |
| body limitation/failure cue | Most of these poses tend to come with a large angular deviation and cannot be rectified through local optimization. | p. 10 (4 Experiments) |
| body limitation/failure cue | The subpar performance of the competitors is due to their pose optimization processes, namely, local optimizations, which cannot rectify the poses with significant errors. | p. 12 (4 Experiments) |
| body limitation/failure cue | As shown, our method is more robust to outlier poses, producing less distortion and better geometric detail. | p. 12 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We follow the hierarchical sampling strategy in NeuS and set the batch size to 512, among which, we select 16 matched keypoints and use ... | p. 10 (4 Experiments) |
| Next, we describe the implementation details of the proposed (Sec. | p. 10 (4 Experiments) |
| For each of them, we adopt the official implementation to optimize camera poses, and then apply the optimized poses to train NeuS. | p. 11 (4 Experiments) |
| The scene graph is initially constructed with the employed SfM module [40], which contains two major steps: a) correspondence search, and b) incremental registration ... | p. 6 (3 Method) |
| The confidence score for a node vi is computed as: CS(v _ i ) = \fr ac {\s um _ {M_{i,j} \in \mathbf {M}_i} ... | p. 7 (3 Method) |
| It consists of several training epochs. | p. 8 (3 Method) |
| As illustrated in Figure 4, it is computed on top of keypoint matches. | p. 8 (3 Method) |
| SG-NeRF 9 Optimized Source Ray & MoG Compute IoU Source Ray & MoG Reference (Fixed) Ray & MoG ⨁ = Fig. | p. 9 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1: 3D surface reconstruction (meshes) from images with camera poses that present significant noise. Directly training radiance fields with noisy poses can lead to ...
- **p. 14 / 5 Conclusion - extractive PDF cue:** Even though our method can greatly refine the inlier poses, the improvement on outlier poses is moderate (whose effect is still largely alleviated with the ...
- **p. 13 / 4 Experiments - extractive PDF cue:** Please also note that there are several failure cases from the competitors indicating completely incorrect reconstruction.
- **p. 10 / 4 Experiments - extractive PDF cue:** Most of these poses tend to come with a large angular deviation and cannot be rectified through local optimization.
- **p. 12 / 4 Experiments - extractive PDF cue:** The subpar performance of the competitors is due to their pose optimization processes, namely, local optimizations, which cannot rectify the poses with significant errors.
- **p. 12 / 4 Experiments - extractive PDF cue:** As shown, our method is more robust to outlier poses, producing less distortion and better geometric detail.

- **PDF anchors reviewed:** datasets p. 10 (4 Experiments), p. 13 (7.71 3.77†), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), metrics p. 14 (Figure/Table caption), p. 12 (4 Experiments), p. 14 (7.71 3.77†), p. 10 (4 Experiments), p. 13 (7.71 3.77†), p. 13 (7.71 3.77†), baselines p. 10 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 13 (7.71 3.77†), p. 13 (7.71 3.77†), results p. 13 (7.71 3.77†), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 13 (7.71 3.77†), p. 14 (7.71 3.77†), p. 14 (7.71 3.77†).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
