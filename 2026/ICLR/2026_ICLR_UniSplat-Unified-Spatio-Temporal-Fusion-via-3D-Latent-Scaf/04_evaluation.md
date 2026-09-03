# Evaluation - UniSplat: Unified Spatio-Temporal Fusion via 3D Latent Scaffolds for Dynamic Driving Scene Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=Ng2VDbKD4r; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/247830. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS)): As shown in 1st and 2nd rows, the incorporation of spatial scaffold fusion, which aggregates spatial information in 3D space, improves performance by +0.36dB in PSNR and +0.02 in SSIM ...

## Evaluation Body Digest

- **p. 6 / 4 EXPERIMENTS - extractive body cue:** We conduct experiments on two large-scale autonomous driving benchmarks: Waymo Open (Sun et al., 2020) and nuScenes (Caesar et al., 2020) datasets.
- **p. 16 / A.2 EFFICIENCY ANALYSIS - extractive body cue:** We benchmark the efficiency of our method against Omni-Scene, a state-of-the-art open-source driving-specific reconstruction model, on the nuScenes dataset (Caesar et al., 2020).
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We adopt image resolutions of 350 × 518 for the Waymo dataset and 224 × 406 for the nuScenes dataset.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** Method Views Reconstruction Novel View Synthesis PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ EvolSplat (Miao et al., 2025) Front 23.35 0.70 0.29 - - - UniSplat ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** (2025), we evaluate UniSplat on the nuScenes benchmark under the same protocol.
- **p. 16 / A.3 MORE QUALITATIVE RESULTS - extractive body cue:** Qualitative Comparisons on the nuScenes dataset.
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** 4.1 EXPERIMENTAL SETTINGS Datasets and Metrics.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** 4.3 ABLATION STUDY In this section, we conduct ablation studies on the Waymo Open Dataset (Sun et al., 2020) to investigate the individual components of ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 6); A.1 IMPLEMENTATION DETAILS (p. 15); A.3 MORE QUALITATIVE RESULTS (p. 16).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | As shown in 1st and 2nd rows, the incorporation of spatial scaffold fusion, which aggregates spatial information in 3D space, improves performance by +0.36dB ... | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | UniSplat consistently outperforms all baselines across every metric for both input view reconstruction and novel view synthesis. | p. 7 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | We also report an variant (denoted by †), in which per-camera scales are set to optimal values derived from LiDAR pointmap, leading to additional ... | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | This approach achieves a lower PSNR of 24.72dB, likely due to its limited ability to model dynamic elements and restricted temporal context. | p. 9 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | The best results are marked in bold and underlined entries indicate second-place performance. ∗: Evaluation conducted on front 3 views only. †: Results obtained ... | p. 7 (4 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 6 / 4 EXPERIMENTS - extractive body cue:** We conduct experiments on two large-scale autonomous driving benchmarks: Waymo Open (Sun et al., 2020) and nuScenes (Caesar et al., 2020) datasets.
- **p. 16 / A.2 EFFICIENCY ANALYSIS - extractive body cue:** We benchmark the efficiency of our method against Omni-Scene, a state-of-the-art open-source driving-specific reconstruction model, on the nuScenes dataset (Caesar et al., 2020).
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We adopt image resolutions of 350 × 518 for the Waymo dataset and 224 × 406 for the nuScenes dataset.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** Method Views Reconstruction Novel View Synthesis PSNR↑ SSIM↑ LPIPS↓ PSNR↑ SSIM↑ LPIPS↓ EvolSplat (Miao et al., 2025) Front 23.35 0.70 0.29 - - - UniSplat ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** (2025), we evaluate UniSplat on the nuScenes benchmark under the same protocol.
- **p. 16 / A.3 MORE QUALITATIVE RESULTS - extractive body cue:** Qualitative Comparisons on the nuScenes dataset.
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** 4.1 EXPERIMENTAL SETTINGS Datasets and Metrics.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** 4.3 ABLATION STUDY In this section, we conduct ablation studies on the Waymo Open Dataset (Sun et al., 2020) to investigate the individual components of ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1: Overview of UniSplat. Given multi-camera images from vehicle-mounted cameras, UniSplat leverages foundation models to construct geometry-semantic aware 3D latent scaffolds, where unified spatio-temporal ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Quantitative results on the Waymo Dataset. The best results are marked in bold and underlined entries indicate second-place performance. ∗: Evaluation conducted on ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Quantitative results on the nuScenes Dataset. We highlight best results in bold and second- place results with underlines. ∗: reported by Wei et ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 2: Qualitative comparisons on the Waymo dataset. Our method yields more detailed and consistent geometry than existing works. Red boxes indicate artifacts. Best viewed ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 3: Qualitative results of scene completion on the Waymo dataset. Top: Aggregated scene without dynamic filtering, where red boxes indicate ghosting artifacts caused by ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Impact of feature composition of Ft. "Geo" and "Sem" denote geometric and semantic features, respectively. Geo Sem PSNR↑ SSIM↑ LPIPS↓
- **p. 9 / Figure/Table caption - extractive body cue:** Table 4: Analysis of spatio-temporal fusion. "Spa" and "Tem" denote spatial and temporal fu- sion, respectively. Spa Tem PSNR↑ SSIM↑
- **p. 10 / Figure/Table caption - extractive body cue:** Table 5: Ablation study on the two branches of our Gaussian decoder. Point Voxel PSNR↑SSIM↑LPIPS↓ ✓ 24.62 0.72 0.38

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We conduct experiments on two large-scale autonomous driving benchmarks: Waymo Open (Sun et al., 2020) and nuScenes (Caesar et al., 2020) datasets. | embodiment, simulator version and control stack | p. 6 (4 EXPERIMENTS), p. 16 (A.2 EFFICIENCY ANALYSIS) |
| Task/environment | We benchmark the efficiency of our method against Omni-Scene, a state-of-the-art open-source driving-specific reconstruction model, on the nuScenes dataset (Caesar et al., 2020). | reset, timeout, object/scene variation | p. 16 (A.2 EFFICIENCY ANALYSIS), p. 7 (4 EXPERIMENTS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1 INTRODUCTION), p. 2 (1 INTRODUCTION) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1 INTRODUCTION), p. 16 (A.1 IMPLEMENTATION DETAILS) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Using only point-anchored Gaussians results in a performance degradation of 0.46 in PSNR, 0.02 in SSIM, and an increase of 0.08 in LPIPS error, ... | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| The absence of semantic features causes a severe decline in LPIPS, increasing the error by 0.05, which can be attributed to the fact that ... | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| In the Gaussian decoding stage, the second branch generates g = 4 primitives per voxel, and the dynamic attribute threshold for streaming scene completion ... | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| For efficiency, we subsample the first 20% of frames from each sequence and apply optimal scale alignment to the point map to accelerate model ... | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| For nuScenes, which provides six surround-view images per frame, we adopt the strategy of Wei et al. | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| In Table 6, We ablate the impact of the geometry foundation model on our framework's performance. | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| The third row illustrates a failure case in which a moving pedestrian is misclassified as static. | definition/direction/unit from same section | p. 16 (A.3 MORE QUALITATIVE RESULTS) |
| Our method demonstrates superior spatial coherence, as evidenced in challenging cases such as the thin pole (first row), and produces fewer artifacts like the ... | definition/direction/unit from same section | p. 16 (A.3 MORE QUALITATIVE RESULTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| UniSplat consistently outperforms all baselines across every metric for both input view reconstruction and novel view synthesis. | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| As shown in 1st and 2nd rows, the incorporation of spatial scaffold fusion, which aggregates spatial information in 3D space, improves performance by +0.36dB ... | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| As shown in Figure 3, the top section presents a baseline without dynamic filtering, where ghosting artifacts arise from accumulated dynamic objects. | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| We compare UniSplat against state-of-the-art sparse-view reconstruction methods, including MVSplat (Chen et al., 2024), DepthSplat (Xu et al., 2025), EvolSplat (Miao et al., 2025), ... | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| For a fair comparison, evaluation is performed by resizing our model's outputs to 224 × 400, aligning with the baseline's resolution before metric computation. | comparison identity and matched condition | p. 16 (A.1 IMPLEMENTATION DETAILS) |
| We benchmark the efficiency of our method against Omni-Scene, a state-of-the-art open-source driving-specific reconstruction model, on the nuScenes dataset (Caesar et al., 2020). | comparison identity and matched condition | p. 16 (A.2 EFFICIENCY ANALYSIS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We also compare against a variant that explicitly uses two consecutive frames without latent-space temporal propagation. | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| 4.3 ABLATION STUDY In this section, we conduct ablation studies on the Waymo Open Dataset (Sun et al., 2020) to investigate the individual components ... | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| Ablation on Geometric and Semantic Features in Scaffold. | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| Top: Aggregated scene without dynamic filtering, where red boxes indicate ghosting artifacts caused by accumulating the dynamic car. | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| Table 5: Ablation study on the two branches of our Gaussian decoder. Point Voxel PSNR↑SSIM↑LPIPS↓ ✓ 24.62 0.72 0.38 | component/input/data sensitivity | p. 10 (Figure/Table caption) |
| For DepthSplat, we initialize from its official weights pre-trained on dl3dV (Ling et al., 2024) and use the variant equipped with a ViT-B backbone ... | component/input/data sensitivity | p. 16 (A.1 IMPLEMENTATION DETAILS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our main contributions are as follows: • We introduce UniSplat, a novel feed-forward framework for dynamic scene reconstruction from multi-camera videos via ... | As shown in 1st and 2nd rows, the incorporation of spatial scaffold fusion, which aggregates spatial information in 3D space, improves performance by +0.36dB ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Primary metric/result | UniSplat consistently outperforms all baselines across every metric for both input view reconstruction and novel view synthesis. | numeric claim only at cited anchor | p. 7 (4 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** Method PSNR↑ SSIM↑ LPIPS↓ PixelSplat∗(Charatan et al., 2024) 21.51 0.616 0.372 MVSplat∗(Chen et al., 2024) 21.61 0.658 0.295 Omin-Scene (Wei et al., 2025) 24.27 0.736 ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** All models are trained for 20 epochs with a batch size of 32 on 16 GPUs.
- **p. 15 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** The model is trained in a streaming manner using clips of 20 frames for 20 epochs, with an initial learning rate of 1.5 × 10-4 ...
- **p. 16 / A.2 EFFICIENCY ANALYSIS - extractive body cue:** UniSplat attains higher runtime efficiency (4.0 FPS vs.
- **p. 16 / A.2 EFFICIENCY ANALYSIS - extractive body cue:** 2.5 FPS) while surpassing Omni-Scene by a large margin in reconstruction quality.
- **p. 16 / A.2 EFFICIENCY ANALYSIS - extractive body cue:** The reported inference time represents the end-to-end reconstruction and rendering of all 18 target frames per sample, averaged over 2,048 samples, with data loading time ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The third row illustrates a failure case in which a moving pedestrian is misclassified as static. | p. 16 (A.3 MORE QUALITATIVE RESULTS) |
| body limitation/failure cue | The voxel-only variant is excluded from comparison as it fails catastrophically at long-range rendering (Wei et al., 2025), yielding consistently poor performance across all ... | p. 9 (4 EXPERIMENTS) |
| body limitation/failure cue | Specifically, replacing the default model with MoGe-2 (Wang et al., 2025e), a recently introduced open-domain geometry estimation method, yields consistent performance, which indicates that ... | p. 9 (4 EXPERIMENTS) |
| body limitation/failure cue | Training is conducted with a batch size of 16 on 8 H20 GPUs for 40,000 iterations, as further training empirically degrades performance. | p. 16 (A.1 IMPLEMENTATION DETAILS) |
| body limitation/failure cue | The final dual-branch decoder effectively combines these complementary strengths, recovering sharp details while maintaining robust structural integrity in novel views. | p. 17 (A.3 MORE QUALITATIVE RESULTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All models are trained for 20 epochs with a batch size of 32 on 16 GPUs. | p. 8 (4 EXPERIMENTS) |
| The model is trained in a streaming manner using clips of 20 frames for 20 epochs, with an initial learning rate of 1.5 × ... | p. 15 (A.1 IMPLEMENTATION DETAILS) |
| For the semantic backbone within the 3D scaffold reconstruction, we uses a learning rate scaled by a factor of 0.1. | p. 15 (A.1 IMPLEMENTATION DETAILS) |
| Training is conducted with a batch size of 16 on 8 H20 GPUs for 40,000 iterations, as further training empirically degrades performance. | p. 16 (A.1 IMPLEMENTATION DETAILS) |
| Additional implementation details are provided in Appendix A.1. | p. 7 (4 EXPERIMENTS) |
| For the general methods MVSplat and DepthSplat, we retrain them on the Waymo Open Dataset using their official codebases. | p. 7 (4 EXPERIMENTS) |
| We validate our dual-branch decoder design in Table 5. | p. 9 (4 EXPERIMENTS) |
| Implementation details of UniSplat counterparts. | p. 16 (A.1 IMPLEMENTATION DETAILS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 16 / A.3 MORE QUALITATIVE RESULTS - extractive body cue:** The third row illustrates a failure case in which a moving pedestrian is misclassified as static.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** The voxel-only variant is excluded from comparison as it fails catastrophically at long-range rendering (Wei et al., 2025), yielding consistently poor performance across all metrics.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Specifically, replacing the default model with MoGe-2 (Wang et al., 2025e), a recently introduced open-domain geometry estimation method, yields consistent performance, which indicates that our ...
- **p. 16 / A.1 IMPLEMENTATION DETAILS - extractive body cue:** Training is conducted with a batch size of 16 on 8 H20 GPUs for 40,000 iterations, as further training empirically degrades performance.
- **p. 17 / A.3 MORE QUALITATIVE RESULTS - extractive body cue:** The final dual-branch decoder effectively combines these complementary strengths, recovering sharp details while maintaining robust structural integrity in novel views.

- **Evidence anchors reviewed:** datasets p. 6 (4 EXPERIMENTS), p. 16 (A.2 EFFICIENCY ANALYSIS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 16 (A.3 MORE QUALITATIVE RESULTS), metrics p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), baselines p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 16 (A.1 IMPLEMENTATION DETAILS), p. 16 (A.2 EFFICIENCY ANALYSIS), results p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
