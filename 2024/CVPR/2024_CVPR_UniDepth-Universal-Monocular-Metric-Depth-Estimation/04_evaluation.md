# Evaluation - UniDepth: Universal Monocular Metric Depth Estimation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2403.18913; PDF retrieval source: https://arxiv.org/pdf/2403.18913. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2. Comparison with the State of the Art), p. 6 (4.2. Comparison with the State of the Art), p. 8 (4.3. Ablation Study), p. 8 (4.3. Ablation Study), p. 7 (4.3. Ablation Study), p. 5 (4.1. Experimental Setup)): Importantly, the KITTI Depth Prediction Benchmark, which provides a perfectly fair evaluation, underscores the excellent zero-shot performance of our method and its robustness compared to the current MMDE SotA methods, ...

## Evaluation Body Digest

- **p. 5 / 4.1. Experimental Setup - extractive body cue:** The resulting dataset amounts roughly to 3M real-world images with different cameras and domains, compared to, e.g.
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** More precisely, each method is tested on validation splits from SUN-RGBD [48] without NYU split, Diode Indoor [50] , IBims-1 [26], VOID [54] HAMMER [25], ...
- **p. 6 / 4.2. Comparison with the State of the Art - extractive body cue:** Method δ0.5 δ1 FA A.Rel RMS RMSlog CD SIlog Higher is better Lower is better BTS [28] 86.9 96.2 82.0 5.63 2.43 0.089 0.42 8.18 ...
- **p. 8 / 4.3. Ablation Study - extractive body cue:** In particular, Full achieves 95.2% in δ1 in KITTI, while "- Camera" obtains 58.9% for the same test set, despite a mere 2% difference between ...
- **p. 6 / 4.2. Comparison with the State of the Art - extractive body cue:** Comparison on KITTI Eigen-split test set.
- **p. 7 / 4.3. Ablation Study - extractive body cue:** The In-Domain column reflects testing on validation splits of training domains, while Out-of-Domain corresponds to zero-shot testing, as detailed in Sec.
- **p. 7 / 4.2. Comparison with the State of the Art - extractive body cue:** (†): KITTI and NYU in the training set.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** This limitation is underscored by the marked variability observed for test sets strongly out-of-distribution, such as KITTI, when comparing the utilization or absence of camera ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Experimental Setup (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Comparison with the State of the Art | EMPIRICAL / REAL-ROBOT OR HARDWARE | Importantly, the KITTI Depth Prediction Benchmark, which provides a perfectly fair evaluation, underscores the excellent zero-shot performance of our method and its robustness compared ... | p. 6 (4.2. Comparison with the State of the Art) |
| 4.2. Comparison with the State of the Art | EMPIRICAL / REAL-ROBOT OR HARDWARE | Experiments show that not only is the performance preserved for most of the test sets, but UniDepth with the bootstrapped camera can also outperform ... | p. 6 (4.2. Comparison with the State of the Art) |
| 4.3. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | This approach hurts generalization, as evidenced by ARelC in the out-of-domain evaluation, despite the slight improvement in in-domain ARelC. | p. 8 (4.3. Ablation Study) |
| 4.3. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | In particular, Full achieves 95.2% in δ1 in KITTI, while "- Camera" obtains 58.9% for the same test set, despite a mere 2% difference ... | p. 8 (4.3. Ablation Study) |
| 4.3. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | Notably, In-Domain results exhibit a higher degree of homogeneity compared to Out-of-Domain, which is noisier yet more informative for gauging expected performances in downstream ... | p. 7 (4.3. Ablation Study) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Experimental Setup - extractive body cue:** The resulting dataset amounts roughly to 3M real-world images with different cameras and domains, compared to, e.g.
- **p. 5 / 4.1. Experimental Setup - extractive body cue:** More precisely, each method is tested on validation splits from SUN-RGBD [48] without NYU split, Diode Indoor [50] , IBims-1 [26], VOID [54] HAMMER [25], ...
- **p. 6 / 4.2. Comparison with the State of the Art - extractive body cue:** Method δ0.5 δ1 FA A.Rel RMS RMSlog CD SIlog Higher is better Lower is better BTS [28] 86.9 96.2 82.0 5.63 2.43 0.089 0.42 8.18 ...
- **p. 8 / 4.3. Ablation Study - extractive body cue:** In particular, Full achieves 95.2% in δ1 in KITTI, while "- Camera" obtains 58.9% for the same test set, despite a mere 2% difference between ...
- **p. 6 / 4.2. Comparison with the State of the Art - extractive body cue:** Comparison on KITTI Eigen-split test set.
- **p. 7 / 4.3. Ablation Study - extractive body cue:** The In-Domain column reflects testing on validation splits of training domains, while Out-of-Domain corresponds to zero-shot testing, as detailed in Sec.
- **p. 7 / 4.2. Comparison with the State of the Art - extractive body cue:** (†): KITTI and NYU in the training set.
- **p. 8 / 4.3. Ablation Study - extractive body cue:** This limitation is underscored by the marked variability observed for test sets strongly out-of-distribution, such as KITTI, when comparing the utilization or absence of camera ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. We introduce UniDepth, a novel approach that di- rectly predicts 3D points in a scene with only one image as input. UniDepth incorporates ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Model Architecture. UniDepth utilizes solely the input image to generate the 3D output (O). It bootstraps dense camera prediction (C) from the Camera ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Impact of noise in camera intrinsics. The amount of relative distortion (εCAM(%)) of the intrinsics is shown on the x- axis, while δ0.5 ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Comparison on zero-shot evaluation. All methods are tested in a zero-shot setting on eight different datasets without overlap with any of the sets ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 2. Comparison on NYU test set. The first five methods are trained on NYU and tested on it. The last four methods are tested ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 3. Comparison on KITTI Eigen-split test set. The first five methods are trained on KITTI and tested on it. The last four meth- ods ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Zero-shot qualitative results. Each pair of consecutive rows corresponds to one test sample. Each odd row shows the input RGB image and the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 4. Comparison with equivalent training setup. All meth- ods have the same backbone, ConvNext-L [33] and are tested in a zero-shot regime on KITTI ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The resulting dataset amounts roughly to 3M real-world images with different cameras and domains, compared to, e.g. | embodiment, simulator version and control stack | p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup) |
| Task/environment | More precisely, each method is tested on validation splits from SUN-RGBD [48] without NYU split, Diode Indoor [50] , IBims-1 [26], VOID [54] HAMMER ... | reset, timeout, object/scene variation | p. 5 (4.1. Experimental Setup), p. 6 (4.2. Comparison with the State of the Art) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 1 (1. Introduction), p. 1 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Importantly, the KITTI Depth Prediction Benchmark, which provides a perfectly fair evaluation, underscores the excellent zero-shot performance of our method and its robustness compared ... | definition/direction/unit from same section | p. 6 (4.2. Comparison with the State of the Art) |
| In addition, we report pointcloud-based metrics proposed in [37], namely Chamfer Distance (CD) and F-score (FA), with the latter aggregated as the area under ... | definition/direction/unit from same section | p. 5 (4.1. Experimental Setup) |
| Row 5 demonstrates the positive impact of the geometric invariance loss. | definition/direction/unit from same section | p. 8 (4.3. Ablation Study) |
| This loss contributes to enhanced in-domain and out-of-domain performance by promoting the invariance of depth features to appearance variations owing to different camera intrinsics. | definition/direction/unit from same section | p. 8 (4.3. Ablation Study) |
| Figure 1. We introduce UniDepth, a novel approach that di- rectly predicts 3D points in a scene with only one image as input. UniDepth ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| We utilize common depth estimation evaluation metrics: root mean square error (RMS) and its log variant (RMSlog), absolute mean relative error (A.Rel), the percentage ... | definition/direction/unit from same section | p. 5 (4.1. Experimental Setup) |
| The last column represents the specific colormap ranges for depth and error. | definition/direction/unit from same section | p. 7 (4.2. Comparison with the State of the Art) |
| Each odd row shows the input RGB image and the predicted pointcloud color-coded with coolwarm based on the absolute relative error. | definition/direction/unit from same section | p. 7 (4.2. Comparison with the State of the Art) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The Oracle model demonstrates more robust scale-dependent performance during zero-shot testing compared to the Full model, highlighting how the proposed task is inherently more ... | comparison identity and matched condition | p. 7 (4.3. Ablation Study) |
| Table 5. Ablations of UniDepth. In-Domain corresponds to the union of the training domain's validation sets, while Out-of-Domain involves the union of zero-shot testing ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Our method consistently outperforms previous SotA methods as shown in Table 1. | comparison identity and matched condition | p. 6 (4.2. Comparison with the State of the Art) |
| Importantly, the KITTI Depth Prediction Benchmark, which provides a perfectly fair evaluation, underscores the excellent zero-shot performance of our method and its robustness compared ... | comparison identity and matched condition | p. 6 (4.2. Comparison with the State of the Art) |
| The Baseline model illustrates an approach to the problem without utilizing external information and lacking a proper design for both internal and output space. | comparison identity and matched condition | p. 7 (4.3. Ablation Study) |
| We evaluate the generalizability of the compared models by testing them on ten datasets not seen during training. | comparison identity and matched condition | p. 5 (4.1. Experimental Setup) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In Table 5, row 3, the benefit of the Camera Module becomes apparent, revealing a substantial disparity in the effect of this module on ... | component/input/data sensitivity | p. 7 (4.3. Ablation Study) |
| Nonetheless, we present results both with and without GT intrinsics for UniDepth. | component/input/data sensitivity | p. 5 (4.1. Experimental Setup) |
| More precisely, each method is tested on validation splits from SUN-RGBD [48] without NYU split, Diode Indoor [50] , IBims-1 [26], VOID [54] HAMMER ... | component/input/data sensitivity | p. 5 (4.1. Experimental Setup) |
| FA drop is 11.8% and 31.4%, respectively, although having a clear scale-invariant improvement of 36.9% and 28.5%. | component/input/data sensitivity | p. 6 (4.2. Comparison with the State of the Art) |
| All methods are tested in a zero-shot setting on eight different datasets without overlap with any of the sets used for training. | component/input/data sensitivity | p. 6 (4.1. Experimental Setup) |
| All ablations exploit the predicted camera representation, if not stated otherwise. | component/input/data sensitivity | p. 7 (4.3. Ablation Study) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We introduce UniDepth, a novel approach that directly predicts 3D points in a scene with only one image as input. | Importantly, the KITTI Depth Prediction Benchmark, which provides a perfectly fair evaluation, underscores the excellent zero-shot performance of our method and its robustness compared ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2. Comparison with the State of the Art), p. 6 (4.2. Comparison with the State of the Art), p. 8 (4.3. Ablation Study), p. 8 (4.3. Ablation Study), p. 7 (4.3. Ablation Study), p. 5 (4.1. Experimental Setup) |
| Primary metric/result | Experiments show that not only is the performance preserved for most of the test sets, but UniDepth with the bootstrapped camera can also outperform ... | numeric claim only at cited anchor | p. 6 (4.2. Comparison with the State of the Art) |

- Numeric sentences retained from the body:
- **p. 4 / 3.3. Geometric Invariance Loss - extractive body cue:** For each image, we perform N distinct geometrical augmentations, denoted as {Ti}N i=1, with N = 2 in our experiments.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This limitation is underscored by the marked variability observed for test sets strongly out-of-distribution, such as KITTI, when comparing the utilization or absence of ... | p. 8 (4.3. Ablation Study) |
| body limitation/failure cue | The designed self-prompting camera allows camera-free test time application and renders the model more robust against camera noise. | p. 8 (5. Conclusion) |
| body limitation/failure cue | This pitfall is demonstrated by the drop in scale-dependent metrics, e.g. | p. 6 (4.2. Comparison with the State of the Art) |
| body limitation/failure cue | Moreover, ZoeDepth, which has a capacity similar to our ViT-based approach and is pre-trained on the diverse MiDaS dataset [42], shows limitations in general ... | p. 6 (4.2. Comparison with the State of the Art) |
| body limitation/failure cue | Figure 3. Impact of noise in camera intrinsics. The amount of relative distortion (εCAM(%)) of the intrinsics is shown on the x- axis, while ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | The Oracle model demonstrates more robust scale-dependent performance during zero-shot testing compared to the Full model, highlighting how the proposed task is inherently more ... | p. 7 (4.3. Ablation Study) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We run 1M optimization iterations with a batch size of 128, each training dataset is uniformly represented in each batch. | p. 5 (4.1. Experimental Setup) |
| On the other hand, Baseline is a straightforward encoder-decoder implementation with a (x,y,z) output, as outlined at the beginning of Sec. | p. 7 (4.3. Ablation Study) |
| As the learning rate scheduler, we exploit Cosine Annealing to one-tenth starting from 30% of the training. | p. 5 (4.1. Experimental Setup) |
| The required training time amounts to roughly 12 days on 8 NVIDIA A100. | p. 6 (4.1. Experimental Setup) |
| Ablations are conducted with three different seeds and for 100k training iterations, using a randomly sampled subset with a size equal to 20% of ... | p. 6 (4.1. Experimental Setup) |
| Each odd row shows the input RGB image and the predicted pointcloud color-coded with coolwarm based on the absolute relative error. | p. 7 (4.2. Comparison with the State of the Art) |
| Furthermore, stopping the gradient from propagating from the Camera Module to the Encoder (row 7), as described in Sec. | p. 8 (4.3. Ablation Study) |
| More specifically, the decoder of Baseline is not conditioned on inaccurate prior camera and scale information as in row 4. | p. 8 (4.3. Ablation Study) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4.3. Ablation Study - extractive body cue:** This limitation is underscored by the marked variability observed for test sets strongly out-of-distribution, such as KITTI, when comparing the utilization or absence of camera ...
- **p. 8 / 5. Conclusion - extractive body cue:** The designed self-prompting camera allows camera-free test time application and renders the model more robust against camera noise.
- **p. 6 / 4.2. Comparison with the State of the Art - extractive body cue:** This pitfall is demonstrated by the drop in scale-dependent metrics, e.g.
- **p. 6 / 4.2. Comparison with the State of the Art - extractive body cue:** Moreover, ZoeDepth, which has a capacity similar to our ViT-based approach and is pre-trained on the diverse MiDaS dataset [42], shows limitations in general zero-shot ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Impact of noise in camera intrinsics. The amount of relative distortion (εCAM(%)) of the intrinsics is shown on the x- axis, while δ0.5 ...
- **p. 7 / 4.3. Ablation Study - extractive body cue:** The Oracle model demonstrates more robust scale-dependent performance during zero-shot testing compared to the Full model, highlighting how the proposed task is inherently more demanding.

- **Evidence anchors reviewed:** datasets p. 5 (4.1. Experimental Setup), p. 5 (4.1. Experimental Setup), p. 6 (4.2. Comparison with the State of the Art), p. 8 (4.3. Ablation Study), p. 6 (4.2. Comparison with the State of the Art), p. 7 (4.3. Ablation Study), metrics p. 6 (4.2. Comparison with the State of the Art), p. 5 (4.1. Experimental Setup), p. 8 (4.3. Ablation Study), p. 8 (4.3. Ablation Study), p. 1 (Figure/Table caption), p. 5 (4.1. Experimental Setup), baselines p. 7 (4.3. Ablation Study), p. 8 (Figure/Table caption), p. 6 (4.2. Comparison with the State of the Art), p. 6 (4.2. Comparison with the State of the Art), p. 7 (4.3. Ablation Study), p. 5 (4.1. Experimental Setup), results p. 6 (4.2. Comparison with the State of the Art), p. 6 (4.2. Comparison with the State of the Art), p. 8 (4.3. Ablation Study), p. 8 (4.3. Ablation Study), p. 7 (4.3. Ablation Study), p. 5 (4.1. Experimental Setup).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
