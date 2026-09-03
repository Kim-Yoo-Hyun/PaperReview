# Evaluation - RayI2P: Learning Rays for Image-to-Point Cloud Registration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=arfeGsDWoq; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/247078. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 15 (Figure/Table caption)): As a result, our method achieves much faster inference time, making it more efficient without compromising performance.

## Evaluation Body Digest

- **p. 7 / 4 EXPERIMENTS - extractive body cue:** 4.2 DATASETS We conduct experiments on two mostly used benchmarks: KITTI and nuScenes.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** On the nuScenes dataset, our approach also shows strong generalization, surpassing ICL by 0.24m in RTE and 0.65◦in RRE.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** While classical pose solver (Row 4) achieves reasonable results, it is less stable than learning-based formulation, with notably larger mean and variance in rotation errors ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We follow the official train/test split, using 850 scenes for training and 150 scenes for testing.
- **p. 16 / A.6 MORE IMPLEMENTATION DETAILS - extractive body cue:** The point clouds are voxelized with an initial voxel size of 15cm for both the KITTI dataset and nuScenes dataset.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** On the KITTI dataset, our method consistently outperforms all baselines across all evaluation metrics, including GraphI2P, which benefits from an auxiliary high-quality depth estimator.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Here ✗indicates method that doesn't use Lfoc. σ KITTI nuScenes RTE(m)↓ RRE(◦)↓ Acc(%)↑ RTE(m)↓ RRE(◦)↓ Acc(%)↑ ✗ 0.10±0.09 1.02±1.00 99.18 0.42±0.31 1.94±6.22 94.44 8 0.11±0.09 ...
- **p. 16 / A.6 MORE IMPLEMENTATION DETAILS - extractive body cue:** The output feature map is downsampled by a factor of 8 relative to the input image, yielding a resolution of 20 × 64 for KITTI ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 6); A.1 EVALUATION METRICS (p. 14); A.6 MORE IMPLEMENTATION DETAILS (p. 16).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | As a result, our method achieves much faster inference time, making it more efficient without compromising performance. | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Specifically, our method achieves the highest registration accuracy (Acc), while reducing RTE by 0.11m and RRE by 0.61◦compared to ICL. | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | While classical pose solver (Row 4) achieves reasonable results, it is less stable than learning-based formulation, with notably larger mean and variance in rotation ... | p. 9 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | The full model (Row 6) further achieves the best overall performance, highlighting both the necessity of a learnable regression module and the contribution of ... | p. 9 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Following VP2P-match (Zhou et al., 2023), we define Acc as the proportion of samples where the estimated transformation achieves RTE < 2m and RRE ... | p. 7 (4 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 7 / 4 EXPERIMENTS - extractive body cue:** 4.2 DATASETS We conduct experiments on two mostly used benchmarks: KITTI and nuScenes.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** On the nuScenes dataset, our approach also shows strong generalization, surpassing ICL by 0.24m in RTE and 0.65◦in RRE.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** While classical pose solver (Row 4) achieves reasonable results, it is less stable than learning-based formulation, with notably larger mean and variance in rotation errors ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We follow the official train/test split, using 850 scenes for training and 150 scenes for testing.
- **p. 16 / A.6 MORE IMPLEMENTATION DETAILS - extractive body cue:** The point clouds are voxelized with an initial voxel size of 15cm for both the KITTI dataset and nuScenes dataset.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** On the KITTI dataset, our method consistently outperforms all baselines across all evaluation metrics, including GraphI2P, which benefits from an auxiliary high-quality depth estimator.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Here ✗indicates method that doesn't use Lfoc. σ KITTI nuScenes RTE(m)↓ RRE(◦)↓ Acc(%)↑ RTE(m)↓ RRE(◦)↓ Acc(%)↑ ✗ 0.10±0.09 1.02±1.00 99.18 0.42±0.31 1.94±6.22 94.44 8 0.11±0.09 ...
- **p. 16 / A.6 MORE IMPLEMENTATION DETAILS - extractive body cue:** The output feature map is downsampled by a factor of 8 relative to the input image, yielding a resolution of 20 × 64 for KITTI ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: (a) Illustration of the iterative pose optimization process in matching-free methods such as DeepI2P. Green points indicate 3D points predicted to lie within ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: Overview of our proposed image-to-point cloud registration framework. Given a pair of image I and point cloud P, we first extract downsampled patch ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Registration accuracy on the KITTI and nuScenes datasets. Here † represents method that adopts external powerful depth estimation model (Bhat et al., 2023) ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3: Qualitative comparison of Image-to-Point Cloud registration results on KITTI dataset. backbone network, where the output channel dimension is 512. For the 3D backbone, ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Visualization of predicted and ground truth camera poses, rays, and attention maps. Left: Predicted camera poses (red) and GT poses (green), with red ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 3: Ablation studies on Ray-guided Pose Regression Module. FPF: Fused Patch Features Ff; PR: Patch Rays r; RR: Renference Rays r′; CPS: classical pose ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 4: Ablation studies on focus radius σ. Here ✗indicates method that doesn't use Lfoc. σ KITTI nuScenes RTE(m)↓ RRE(◦)↓ Acc(%)↑ RTE(m)↓
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 5: Visual comparison between classical pose solver and our proposed ray-guided pose re- gression module. Classical pose solver suffers from unstable predictions under noisy ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 4.2 DATASETS We conduct experiments on two mostly used benchmarks: KITTI and nuScenes. | embodiment, simulator version and control stack | p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Task/environment | On the nuScenes dataset, our approach also shows strong generalization, surpassing ICL by 0.24m in RTE and 0.65◦in RRE. | reset, timeout, object/scene variation | p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 16 (A.6 MORE IMPLEMENTATION DETAILS), p. 5 (3 METHOD) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3 METHOD), p. 1 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 4.3 EVALUATION METRICS To assess registration performance, we follow the protocol from VP2P-match (Zhou et al., 2023), reporting three key metrics: average Relative Translation ... | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| To quantitatively evaluate the performance of image-to-point cloud registration, we adopt two widely used metrics that measure the accuracy of estimated 6-DoF (Degrees of ... | definition/direction/unit from same section | p. 14 (A.1 EVALUATION METRICS) |
| Unlike CorrI2P (Ren et al., 2022), which filters out high-error samples before computing averages, we retain all test pairs during evaluation to better reflect ... | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| While classical pose solver (Row 4) achieves reasonable results, it is less stable than learning-based formulation, with notably larger mean and variance in rotation ... | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| Specifically, our method achieves the highest registration accuracy (Acc), while reducing RTE by 0.11m and RRE by 0.61◦compared to ICL. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| Across diverse road scenes, our method achieves superior registration accuracy compared to VP2P-match (Zhou et al., 2023) and ICL (Li et al., 2025), demonstrating ... | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| However, further increasing σ beyond 32, along with the removal of the focus loss, leads to performance degradation. | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| Figure 5: Visual comparison between classical pose solver and our proposed ray-guided pose re- gression module. Classical pose solver suffers from unstable predictions under ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 4.4 COMPARISON WITH STATE-OF-THE-ART METHODS Baselines. | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| On the KITTI dataset, our method consistently outperforms all baselines across all evaluation metrics, including GraphI2P, which benefits from an auxiliary high-quality depth estimator. | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| More detailed ablation results are provided in Appendix 6. | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| 4.5 ABLATION STUDY Ablation on Ray-guided Pose Regression Module. | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| Figure 3: Qualitative comparison of Image-to-Point Cloud registration results on KITTI dataset. backbone network, where the output channel dimension is 512. For the 3D ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 5: Ablation studies on patch size associated with each ray. Each ray corresponds to a p × p local image patch. p KITTI ... | comparison identity and matched condition | p. 15 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To better understand the contribution of each component in our Ray-guided Pose Regression Module, we conduct ablation studies by selectively removing or replacing fused ... | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| We investigate the effect of focus radius σ, which governs the spatial constraints in cross-attention between patch and point features. | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| As a result, our method achieves much faster inference time, making it more efficient without compromising performance. | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| Table 5: Ablation studies on patch size associated with each ray. Each ray corresponds to a p × p local image patch. p KITTI ... | component/input/data sensitivity | p. 15 (Figure/Table caption) |
| Table 6: Ablation studies on focus radius σ. Here ✗indicates method that doesn't use Lfoc. σ KITTI nuScenes RTE(m)↓ RRE(◦)↓ Acc(%)↑ RTE(m)↓ | component/input/data sensitivity | p. 16 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The main contributions are summarized as follows: (1) We propose a novel ray-based paradigm for image-to-point cloud registration, which effectively addresses the core limitations ... | As a result, our method achieves much faster inference time, making it more efficient without compromising performance. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 15 (Figure/Table caption) |
| Primary metric/result | Specifically, our method achieves the highest registration accuracy (Acc), while reducing RTE by 0.11m and RRE by 0.61◦compared to ICL. | numeric claim only at cited anchor | p. 8 (4 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** 4.1 IMPLEMENTATION DETAILS In this work, we implement the proposed model in Pytorch (Paszke et al., 2019) and adopt a single NVIDIA RTX 3090 GPU ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We train the whole network with the total loss Ltotal for 20 epochs.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** All input images are resized to a resolution of 160 × 512, and point clouds are uniformly downsampled to 40,960 points for both training and ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We follow the official train/test split, using 850 scenes for training and 150 scenes for testing.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** For consistency, we downsample the image resolution to 160 × 320 and retain 40,960 points per point cloud.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** In Table 2, we provide a comparison of model size and inference time across different methods, with results obtained on the same machine using a ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | This failure mode, although observed only in rare extreme cases, reveals a fundamental limitation of the current framework: when the predicted overlap region is ... | p. 16 (A.5.2 FAILURE CASES UNDER COMPLETELY INCORRECT OVERLAP PREDICTION) |
| body limitation/failure cue | Figure 5: Visual comparison between classical pose solver and our proposed ray-guided pose re- gression module. Classical pose solver suffers from unstable predictions under ... | p. 15 (Figure/Table caption) |
| body limitation/failure cue | In this paper, we present a novel ray-based framework for image-to-point cloud registration that overcomes key limitations of both matching-based and matching-free approaches. | p. 9 (5 CONCLUSION) |
| body limitation/failure cue | While our method achieves competitive performance on challenging outdoor datasets, it still exhibits certain limitation primarily associated with the reliance on overlap prediction, which ... | p. 15 (A.5 LIMITATIONS AND FUTURE WORK) |
| body limitation/failure cue | Figure 7: Failure Cases Under Completely Incorrect Overlap Prediction. Visualization of a rare but critical failure mode where the predicted overlapping region contains no ... | p. 18 (Figure/Table caption) |
| body limitation/failure cue | Under this condition, the cross attention mechanism is misled and lacks access to any informative cues, resulting in failed ray-level reasoning across the modalities. | p. 16 (A.5.2 FAILURE CASES UNDER COMPLETELY INCORRECT OVERLAP PREDICTION) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In Table 2, we provide a comparison of model size and inference time across different methods, with results obtained on the same machine using ... | p. 8 (4 EXPERIMENTS) |
| 4.1 IMPLEMENTATION DETAILS In this work, we implement the proposed model in Pytorch (Paszke et al., 2019) and adopt a single NVIDIA RTX 3090 ... | p. 6 (4 EXPERIMENTS) |
| The learning rate is set to 10-4, and the weight decay is set to be 10-6. | p. 7 (4 EXPERIMENTS) |
| As a result, our method achieves much faster inference time, making it more efficient without compromising performance. | p. 8 (4 EXPERIMENTS) |
| We train the whole network with the total loss Ltotal for 20 epochs. | p. 7 (4 EXPERIMENTS) |
| All experiments are conducted on a single RTX 3090 GPU. | p. 16 (A.6 MORE IMPLEMENTATION DETAILS) |
| We implement our code using PyTorch 1.13.1 and CUDA 11.7. | p. 16 (A.6 MORE IMPLEMENTATION DETAILS) |
| To address this difficulty, we instead adopt a more expressive formulation by representing the camera as a bundle of rays associated with image patches, ... | p. 4 (3 METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 16 / A.5.2 FAILURE CASES UNDER COMPLETELY INCORRECT OVERLAP PREDICTION - extractive body cue:** This failure mode, although observed only in rare extreme cases, reveals a fundamental limitation of the current framework: when the predicted overlap region is entirely ...
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 5: Visual comparison between classical pose solver and our proposed ray-guided pose re- gression module. Classical pose solver suffers from unstable predictions under noisy ...
- **p. 9 / 5 CONCLUSION - extractive body cue:** In this paper, we present a novel ray-based framework for image-to-point cloud registration that overcomes key limitations of both matching-based and matching-free approaches.
- **p. 15 / A.5 LIMITATIONS AND FUTURE WORK - extractive body cue:** While our method achieves competitive performance on challenging outdoor datasets, it still exhibits certain limitation primarily associated with the reliance on overlap prediction, which is ...
- **p. 18 / Figure/Table caption - extractive body cue:** Figure 7: Failure Cases Under Completely Incorrect Overlap Prediction. Visualization of a rare but critical failure mode where the predicted overlapping region contains no part ...
- **p. 16 / A.5.2 FAILURE CASES UNDER COMPLETELY INCORRECT OVERLAP PREDICTION - extractive body cue:** Under this condition, the cross attention mechanism is misled and lacks access to any informative cues, resulting in failed ray-level reasoning across the modalities.

- **Evidence anchors reviewed:** datasets p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 16 (A.6 MORE IMPLEMENTATION DETAILS), p. 8 (4 EXPERIMENTS), metrics p. 7 (4 EXPERIMENTS), p. 14 (A.1 EVALUATION METRICS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), baselines p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 7 (Figure/Table caption), p. 15 (Figure/Table caption), results p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 15 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
