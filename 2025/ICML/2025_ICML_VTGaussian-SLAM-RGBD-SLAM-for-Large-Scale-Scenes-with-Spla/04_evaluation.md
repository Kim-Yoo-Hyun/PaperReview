# Evaluation - VTGaussian-SLAM: RGBD SLAM for Large Scale Scenes with Splatting View-Tied 3D Gaussians

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=vkmi3jZtYG; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/168040. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.1. Comparisons), p. 8 (4.2. Ablation Studies and Analysis), p. 9 (4.2. Ablation Studies and Analysis), p. 7 (4.1. Comparisons), p. 6 (4. Experiments and Analysis), p. 5 (4. Experiments and Analysis)): Based on the camera poses, our method also significantly improves the rendering quality on ScanNet, as shown in Fig.

## Evaluation Body Digest

- **p. 5 / 4. Experiments and Analysis - extractive body cue:** TUM-RGBD, ScanNet, and ScanNet++ are real-world datasets.
- **p. 5 / 4. Experiments and Analysis - extractive body cue:** Here Replica is a synthetic dataset with high-fidelity 3D reconstruction of indoor scenes.
- **p. 6 / 4.1. Comparisons - extractive body cue:** 1, mapping scenes with rendered images in Tab.
- **p. 6 / 4.1. Comparisons - extractive body cue:** We first report our results on 8 scenes in Replica.
- **p. 7 / 4.1. Comparisons - extractive body cue:** We report our results on the TUMRGBD dataset in camera tracking in Tab.
- **p. 7 / 4.1. Comparisons - extractive body cue:** Our evaluations in camera tracking and mapping scenes with rendering views are reported in Tab.
- **p. 8 / 4.1. Comparisons - extractive body cue:** We report tracking results on the widely used 5 scenes in ScanNet++ in Tab.
- **p. 8 / 4.2. Ablation Studies and Analysis - extractive body cue:** We justify the effectiveness of each design on synthetic and real scenes in Replica (Straub et al., 2019) and TUMRGBD (Sturm et al., 2012).

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4. Experiments and Analysis (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Comparisons | EMPIRICAL / REAL-ROBOT OR HARDWARE | Based on the camera poses, our method also significantly improves the rendering quality on ScanNet, as shown in Fig. | p. 7 (4.1. Comparisons) |
| 4.2. Ablation Studies and Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | The comparisons show that our viewtied Gaussians not only significantly reduce the size of each Gaussian (number of parameters) but also achieve good rendering ... | p. 8 (4.2. Ablation Studies and Analysis) |
| 4.2. Ablation Studies and Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | 8 show that our selection strategy achieves the best performance. | p. 9 (4.2. Ablation Studies and Analysis) |
| 4.1. Comparisons | EMPIRICAL / REAL-ROBOT OR HARDWARE | 8 highlight our improvement over the other methods. | p. 7 (4.1. Comparisons) |
| 4. Experiments and Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | Then we measure the reconstruction performance with F1-score, the harmonic mean of the Precision (P) and Recall (R), using a distance threshold of 1 ... | p. 6 (4. Experiments and Analysis) |

## Dataset / Benchmark Role

- **p. 5 / 4. Experiments and Analysis - extractive body cue:** TUM-RGBD, ScanNet, and ScanNet++ are real-world datasets.
- **p. 5 / 4. Experiments and Analysis - extractive body cue:** Here Replica is a synthetic dataset with high-fidelity 3D reconstruction of indoor scenes.
- **p. 6 / 4.1. Comparisons - extractive body cue:** 1, mapping scenes with rendered images in Tab.
- **p. 6 / 4.1. Comparisons - extractive body cue:** We first report our results on 8 scenes in Replica.
- **p. 7 / 4.1. Comparisons - extractive body cue:** We report our results on the TUMRGBD dataset in camera tracking in Tab.
- **p. 7 / 4.1. Comparisons - extractive body cue:** Our evaluations in camera tracking and mapping scenes with rendering views are reported in Tab.
- **p. 8 / 4.1. Comparisons - extractive body cue:** We report tracking results on the widely used 5 scenes in ScanNet++ in Tab.
- **p. 8 / 4.2. Ablation Studies and Analysis - extractive body cue:** We justify the effectiveness of each design on synthetic and real scenes in Replica (Straub et al., 2019) and TUMRGBD (Sturm et al., 2012).

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1. Overview. (a) and (c) are tracking strategies, while (b) and (d) are mapping strategies. Please refer to Sec. 3.1 for more details. geometry ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Illustration of selecting overlapping section. We show Gaussian centers and colors in each section.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Initialization of view-tied Gaussians in a section. If the latest frame {Vi, Di} is a head starting a new section Sk, we select ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. Issue of pose error cumulation. This design aims to find a balance between the rendering quality and the spatial consistency
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5. Illustration of optimizing view-tied Gaussians initialized on a head frame. Error maps are shown at different iterations. Implementation Details. For neighboring views in ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6. Visual comparisons in reconstruction on Replica.
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Tracking comparisons in ATE RMSE ↓[cm] on Replica. ∗denotes use of pre-trained data-driven priors. Neural Implicit Fields 3D Gaussian Splatting Methods NICE-SLAM DF-Prior ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 7. Error map comparisons in rendering on Replica. ing quality, we measure PSNR, SSIM (Wang et al., 2004), and LPIPS (Zhang et al., 2018). ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | TUM-RGBD, ScanNet, and ScanNet++ are real-world datasets. | embodiment, simulator version and control stack | p. 5 (4. Experiments and Analysis), p. 5 (4. Experiments and Analysis) |
| Task/environment | Here Replica is a synthetic dataset with high-fidelity 3D reconstruction of indoor scenes. | reset, timeout, object/scene variation | p. 5 (4. Experiments and Analysis), p. 6 (4.1. Comparisons) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 5 (3.4. Mapping Scenes), p. 4 (3.3. Tracking Cameras) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 3 (3.2. View-tied Gaussians), p. 3 (3.2. View-tied Gaussians) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Then we measure the reconstruction performance with F1-score, the harmonic mean of the Precision (P) and Recall (R), using a distance threshold of 1 ... | definition/direction/unit from same section | p. 6 (4. Experiments and Analysis) |
| For tracking accuracy, we use the root mean square absolute trajectory error (ATE RMSE) (Sturm et al., 2012) as a metric. | definition/direction/unit from same section | p. 5 (4. Experiments and Analysis) |
| Error map comparisons in rendering on Replica. ing quality, we measure PSNR, SSIM (Wang et al., 2004), and LPIPS (Zhang et al., 2018). | definition/direction/unit from same section | p. 6 (4. Experiments and Analysis) |
| However, relying on data-driven priors, LoopSplat (Zhu et al., 2024) reported more accurate camera tracking in terms of average accuracy, while our method does ... | definition/direction/unit from same section | p. 7 (4.1. Comparisons) |
| Using no visibility in the loss function will degenerate the performance, as shown in Tab. | definition/direction/unit from same section | p. 9 (4.2. Ablation Studies and Analysis) |
| Error maps are shown at different iterations. | definition/direction/unit from same section | p. 5 (4. Experiments and Analysis) |
| Although the input RGBD observations are not in high resolution and with good quality, our method still produces the best tracking accuracy. | definition/direction/unit from same section | p. 7 (4.1. Comparisons) |
| Too few frames will increase the possibility of cumulating camera pose errors while changing into the next section. | definition/direction/unit from same section | p. 8 (4.2. Ablation Studies and Analysis) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to previous GS-based SLAM methods, our method can use many more Gaussians tied at each pixel on depth images to fit sudden color ... | comparison identity and matched condition | p. 7 (4.1. Comparisons) |
| We compare with the state-of-the-art NeRFbased and GS-based SLAM methods in camera tracking in Tab. | comparison identity and matched condition | p. 6 (4.1. Comparisons) |
| Note that Point-SLAM (Sandstr¨om et al., 2023a) requires ground truth depth images as an input to guide sampling when rendering, which is an unfair ... | comparison identity and matched condition | p. 6 (4. Experiments and Analysis) |
| Compared to GS-based methods, our methods can estimate more accurate camera poses thanks to the more accurate renderings. | comparison identity and matched condition | p. 8 (4.1. Comparisons) |
| Comparisons in camera tracking in Tab. | comparison identity and matched condition | p. 7 (4.1. Comparisons) |
| The Gaussian centers nearby are shown without color. | comparison identity and matched condition | p. 8 (4.1. Comparisons) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We conduct experiments to highlight the effect of view-tied Gaussians in Tab. | component/input/data sensitivity | p. 8 (4.2. Ablation Studies and Analysis) |
| We also show the effect of learnable locations with our simplified Gaussians ("iso + w/o VT"). | component/input/data sensitivity | p. 8 (4.2. Ablation Studies and Analysis) |
| Compared to previous GS-based SLAM methods, our method can use many more Gaussians tied at each pixel on depth images to fit sudden color ... | component/input/data sensitivity | p. 7 (4.1. Comparisons) |
| Ablation study on the length of section S, overlap selecting strategy, and visible mask. | component/input/data sensitivity | p. 9 (4.2. Ablation Studies and Analysis) |
| Ablation study on attributes of 3D Gaussians (aniso: anisotropic Gaussians, iso: isotropic Gaussians, VT: view-tied Gaussians). | component/input/data sensitivity | p. 9 (4.2. Ablation Studies and Analysis) |
| Figure 1. Overview. (a) and (c) are tracking strategies, while (b) and (d) are mapping strategies. Please refer to Sec. 3.1 for more details. ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions are listed below. • We propose view-tied Gaussian splatting that significantly reduces storage but improves rendering quality with 3DGS in SLAM. ... | Based on the camera poses, our method also significantly improves the rendering quality on ScanNet, as shown in Fig. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.1. Comparisons), p. 8 (4.2. Ablation Studies and Analysis), p. 9 (4.2. Ablation Studies and Analysis), p. 7 (4.1. Comparisons), p. 6 (4. Experiments and Analysis), p. 5 (4. Experiments and Analysis) |
| Primary metric/result | The comparisons show that our viewtied Gaussians not only significantly reduce the size of each Gaussian (number of parameters) but also achieve good rendering ... | numeric claim only at cited anchor | p. 8 (4.2. Ablation Studies and Analysis) |

- Numeric sentences retained from the body:
- **p. 5 / 4. Experiments and Analysis - extractive body cue:** For neighboring views in a section Sk, we choose N = 40 on Replica (Straub et al., 2019), N = 30 on TUM-RGBD (Sturm et ...
- **p. 5 / 4. Experiments and Analysis - extractive body cue:** During tracking, we use every 5 frames as a candidate view for overlapping section selection, i.e.
- **p. 5 / 4. Experiments and Analysis - extractive body cue:** Note that ScanNet++ is not a dataset designed for SLAM tasks, some sudden large motions are occurring in the DSLR-captured sequences, we follow previous methods ...
- **p. 6 / 4. Experiments and Analysis - extractive body cue:** Similar to (Sandstr¨om et al., 2023a; Liso et al., 2024; Zhu et al., 2024; Yugay et al., 2023), all the rendering metrics are computed by ...
- **p. 6 / 4.1. Comparisons - extractive body cue:** We first report our results on 8 scenes in Replica.
- **p. 8 / 4.1. Comparisons - extractive body cue:** We report tracking results on the widely used 5 scenes in ScanNet++ in Tab.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | We cannot use a large number of Gaussians 8 | p. 8 (4.2. Ablation Studies and Analysis) |
| body limitation/failure cue | However, relying on data-driven priors, LoopSplat (Zhu et al., 2024) reported more accurate camera tracking in terms of average accuracy, while our method does ... | p. 7 (4.1. Comparisons) |
| body limitation/failure cue | Table 22. Impact of depth noise and movability of Gaussians on the rendering performance in PSNR ↑, SSIM ↑, and LPIPS ↓on Replica (Straub ... | p. 23 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Meanwhile, around each frame, we still have good control of the number of Gaussians so that we can maximize the usage of the limited ... | p. 9 (4.2. Ablation Studies and Analysis) |
| More details of hyperparameters are provided in the supplementary materials. | p. 5 (4. Experiments and Analysis) |
| Similar to (Sandstr¨om et al., 2023a; Liso et al., 2024; Zhu et al., 2024; Yugay et al., 2023), all the rendering metrics are computed ... | p. 6 (4. Experiments and Analysis) |
| Runtime and Memory Usage on Replica. | p. 9 (4.2. Ablation Studies and Analysis) |
| With view-tied Gaussians, we manage to keep learnable Gaussians that are the most relevant to the latest frame in the GPU memory. | p. 3 (3.1. Overview) |
| We organize view-tied 3D Gaussians from several consecutive frames as a section so that we can keep as many Gaussians as the GPU memory ... | p. 3 (3.1. Overview) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4.2. Ablation Studies and Analysis - extractive body cue:** We cannot use a large number of Gaussians 8
- **p. 7 / 4.1. Comparisons - extractive body cue:** However, relying on data-driven priors, LoopSplat (Zhu et al., 2024) reported more accurate camera tracking in terms of average accuracy, while our method does not ...
- **p. 23 / Figure/Table caption - extractive body cue:** Table 22. Impact of depth noise and movability of Gaussians on the rendering performance in PSNR ↑, SSIM ↑, and LPIPS ↓on Replica (Straub et ...

- **Evidence anchors reviewed:** datasets p. 5 (4. Experiments and Analysis), p. 5 (4. Experiments and Analysis), p. 6 (4.1. Comparisons), p. 6 (4.1. Comparisons), p. 7 (4.1. Comparisons), p. 7 (4.1. Comparisons), metrics p. 6 (4. Experiments and Analysis), p. 5 (4. Experiments and Analysis), p. 6 (4. Experiments and Analysis), p. 7 (4.1. Comparisons), p. 9 (4.2. Ablation Studies and Analysis), p. 5 (4. Experiments and Analysis), baselines p. 7 (4.1. Comparisons), p. 6 (4.1. Comparisons), p. 6 (4. Experiments and Analysis), p. 8 (4.1. Comparisons), p. 7 (4.1. Comparisons), p. 8 (4.1. Comparisons), results p. 7 (4.1. Comparisons), p. 8 (4.2. Ablation Studies and Analysis), p. 9 (4.2. Ablation Studies and Analysis), p. 7 (4.1. Comparisons), p. 6 (4. Experiments and Analysis), p. 5 (4. Experiments and Analysis).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
