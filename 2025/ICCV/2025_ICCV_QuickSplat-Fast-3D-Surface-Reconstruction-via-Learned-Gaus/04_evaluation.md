# Evaluation - QuickSplat: Fast 3D Surface Reconstruction via Learned Gaussian Initialization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Liu_QuickSplat_Fast_3D_Surface_Reconstruction_via_Learned_Gaussian_Initialization_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Liu_QuickSplat_Fast_3D_Surface_Reconstruction_via_Learned_Gaussian_Initialization_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (4. Experiments), p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 1 (Figure/Table caption), p. 3 (Figure/Table caption), p. 7 (Figure/Table caption)): PGSR renders unbiased depth maps from flattened 3D Gaussians and introduces both single-view and multi-view regularization losses to improve geometric reconstruction.

## Evaluation Body Digest

- **p. 5 / 4. Experiments - extractive PDF cue:** We evaluate our method on 20 unseen test scenes and report averaged metrics.
- **p. 5 / 4. Experiments - extractive PDF cue:** Dataset We train and evaluate our model on the ScanNet++ dataset [52].
- **p. 5 / 4. Experiments - extractive PDF cue:** We calculate the absolute error, as well as the accuracy within different thresholds (2cm, 5cm, 10cm).
- **p. 5 / 4. Experiments - extractive PDF cue:** Metrics To evaluate the quality of the reconstructed geometry, we measure the error between rendered depth and the ground-truth depth maps of ScanNet++ testing frames.
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 4. In general, our proposed QuickSplat achieves better performance: it reconstructs scenes with cleaner structures and flat surfaces that matches the ground truth compared ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitative comparison against baselines. We show top-down views of reconstructed mesh geometries (with and without vertex colors) in comparison to the ground-truth meshes ...
- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. QuickSplat performs surface reconstruction of large indoor scenes from multi-view images as input. We learn strong priors for initialization of gaussian splatting optimization ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Ablation study. We ablate the impact of our learned priors for initialization, densification, and optimization updates. Only using our optimizer network does not ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4. Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | PGSR renders unbiased depth maps from flattened 3D Gaussians and introduces both single-view and multi-view regularization losses to improve geometric reconstruction. | p. 5 (4. Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 4. In general, our proposed QuickSplat achieves better performance: it reconstructs scenes with cleaner structures and flat surfaces that matches the ground truth ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Table 2. Ablation study. We ablate the impact of our learned priors for initialization, densification, and optimization updates. Only using our optimizer network does ... | p. 6 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 1. QuickSplat performs surface reconstruction of large indoor scenes from multi-view images as input. We learn strong priors for initialization of gaussian splatting ... | p. 1 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 2. Method overview. From the SfM points of input multi-view images, our initializer network predicts an initial set of Gaussians G0. We then ... | p. 3 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / 4. Experiments - extractive PDF cue:** We evaluate our method on 20 unseen test scenes and report averaged metrics.
- **p. 5 / 4. Experiments - extractive PDF cue:** Dataset We train and evaluate our model on the ScanNet++ dataset [52].

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. QuickSplat performs surface reconstruction of large indoor scenes from multi-view images as input. We learn strong priors for initialization of gaussian splatting optimization ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Method overview. From the SfM points of input multi-view images, our initializer network predicts an initial set of Gaussians G0. We then learn ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Importance sampling of densified Gaussians. Top: the densifier network predicts a pool of additional voxel features in an encoder-decoder architecture from the current ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Quantitative comparison against baselines. We compare the quality and optimization runtime of our reconstructed surfaces against baseline methods, and show averaged results on ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Ablation study. We ablate the impact of our learned priors for initialization, densification, and optimization updates. Only using our optimizer network does not ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 4. In general, our proposed QuickSplat achieves better performance: it reconstructs scenes with cleaner structures and flat surfaces that matches the ground truth compared ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Qualitative comparison against baselines. We show top-down views of reconstructed mesh geometries (with and without vertex colors) in comparison to the ground-truth meshes ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 5. Qualitative comparison between MonoSDF [54] and ours. Our QuickSplat achieves faster reconstruction and retains more fine details. For example, MonoSDF fails to reconstruct ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate our method on 20 unseen test scenes and report averaged metrics. | embodiment, simulator version and control stack | p. 5 (4. Experiments), p. 5 (4. Experiments) |
| Task/environment | Dataset We train and evaluate our model on the ScanNet++ dataset [52]. | reset, timeout, object/scene variation | p. 5 (4. Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (3. Method), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3. Method), p. 5 (3.3. Iterative Gaussian Optimization) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We calculate the absolute error, as well as the accuracy within different thresholds (2cm, 5cm, 10cm). | definition/direction/unit from same section | p. 5 (4. Experiments) |
| Metrics To evaluate the quality of the reconstructed geometry, we measure the error between rendered depth and the ground-truth depth maps of ScanNet++ testing ... | definition/direction/unit from same section | p. 5 (4. Experiments) |
| Fig. 4. In general, our proposed QuickSplat achieves better performance: it reconstructs scenes with cleaner structures and flat surfaces that matches the ground truth ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Figure 4. Qualitative comparison against baselines. We show top-down views of reconstructed mesh geometries (with and without vertex colors) in comparison to the ground-truth ... | definition/direction/unit from same section | p. 7 (Figure/Table caption) |
| Figure 1. QuickSplat performs surface reconstruction of large indoor scenes from multi-view images as input. We learn strong priors for initialization of gaussian splatting ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Table 2. Ablation study. We ablate the impact of our learned priors for initialization, densification, and optimization updates. Only using our optimizer network does ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 4. In general, our proposed QuickSplat achieves better performance: it reconstructs scenes with cleaner structures and flat surfaces that matches the ground truth ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Table 1. Quantitative comparison against baselines. We compare the quality and optimization runtime of our reconstructed surfaces against baseline methods, and show averaged results ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Figure 4. Qualitative comparison against baselines. We show top-down views of reconstructed mesh geometries (with and without vertex colors) in comparison to the ground-truth ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Baselines We compare our method with several recent 3D surface reconstruction approaches: SuGaR [22], 2DGS [25], GS2Mesh [46], PGSR [9], and MonoSDF [54]. | comparison identity and matched condition | p. 5 (4. Experiments) |
| Figure 1. QuickSplat performs surface reconstruction of large indoor scenes from multi-view images as input. We learn strong priors for initialization of gaussian splatting ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| After running our iterative optimization for t=5 timesteps, we optionally refine the Gaussians for another 2000 steps of gradient descent (without adaptive density control). | comparison identity and matched condition | p. 5 (4. Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 6. Visualization of ablations. (a) Without our initializer and densification priors during optimization, surface reconstruc- tion of untextured regions such as walls is ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| After running our iterative optimization for t=5 timesteps, we optionally refine the Gaussians for another 2000 steps of gradient descent (without adaptive density control). | component/input/data sensitivity | p. 5 (4. Experiments) |
| Table 1. Quantitative comparison against baselines. We compare the quality and optimization runtime of our reconstructed surfaces against baseline methods, and show averaged results ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Table 2. Ablation study. We ablate the impact of our learned priors for initialization, densification, and optimization updates. Only using our optimizer network does ... | component/input/data sensitivity | p. 6 (Figure/Table caption) |
| Figure 4. Qualitative comparison against baselines. We show top-down views of reconstructed mesh geometries (with and without vertex colors) in comparison to the ground-truth ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Table 3. Initializer output ablation study. We evaluate the im- pact of predicting different Gaussian attributes from the SfM point cloud with our initializer ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To summarize, our contributions are: • We propose a learned, generalized initializer network, that leverages scene priors to create effective Gaussian initializations for more ... | PGSR renders unbiased depth maps from flattened 3D Gaussians and introduces both single-view and multi-view regularization losses to improve geometric reconstruction. | PDF body cue; verify exact table/figure and matched conditions | p. 5 (4. Experiments), p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 1 (Figure/Table caption), p. 3 (Figure/Table caption), p. 7 (Figure/Table caption) |
| Primary metric/result | Fig. 4. In general, our proposed QuickSplat achieves better performance: it reconstructs scenes with cleaner structures and flat surfaces that matches the ground truth ... | numeric claim only at cited anchor | p. 6 (Figure/Table caption) |

- Numeric sentences retained from the body:
- **p. 5 / 4. Experiments - extractive PDF cue:** After running our iterative optimization for t=5 timesteps, we optionally refine the Gaussians for another 2000 steps of gradient descent (without adaptive density control).
- **p. 6 / Method - extractive PDF cue:** Abs err↓ Acc (2cm)↑ Acc (5cm)↑ Acc (10cm)↑ Chamfer↓ Time↓ SuGaR [22] 0.2061 0.1157 0.2774 0.4794 0.2078 3130s 2DGS [25] 0.1127 0.4021 0.6027 0.7422 0.2420 ...
- **p. 8 / 4.3. Limitations - extractive PDF cue:** Our method accelerates optimization runtime by 8x and obtains more accurate surface reconstructions from posed images in comparison to baselines.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Second, we assume static environments and therefore cannot reconstruct dynamic scenes (e.g., people walking inside of a room). | p. 8 (4.3. Limitations) |
| body limitation/failure cue | Lastly, even though we significantly reduce optimization runtime, our method does not yet reconstruct in real-time, but could be integrated with recent SLAM-based approaches ... | p. 8 (4.3. Limitations) |
| body limitation/failure cue | Table 2. Ablation study. We ablate the impact of our learned priors for initialization, densification, and optimization updates. Only using our optimizer network does ... | p. 6 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We set the learning rate to 1e-4 and train the networks for 3 days on a single Nvidia RTX A6000. | p. 5 (4. Experiments) |
| Additionally, we report the optimization runtime in seconds. | p. 5 (4. Experiments) |
| We then decode them into vg Gaussian primitives with a small MLP. | p. 3 (3.1. Surface Representation) |
| Inspired by SGNN [14], this network comprises sparse 3D convolutions in an encoder-decoder architecture. | p. 3 (3.2. Initialization Prior) |
| Concretely, we render the training images and compute the gradients of the rendering loss Eq. | p. 4 (3.3. Iterative Gaussian Optimization) |
| This allows us to compute an occupancy loss Locc before every upsampling layer of the SGNN architecture. | p. 4 (3.2. Initialization Prior) |
| We compare the quality and optimization runtime of our reconstructed surfaces against baseline methods, and show averaged results on the test scenes in ScanNet++ ... | p. 6 (Method) |
| Both our method without post-training ("w/o opt") and with additional SGD iterations ("w/ opt") obtain better geometry while achieving orders of magnitude faster runtime. ... | p. 6 (Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 4.3. Limitations - extractive PDF cue:** Second, we assume static environments and therefore cannot reconstruct dynamic scenes (e.g., people walking inside of a room).
- **p. 8 / 4.3. Limitations - extractive PDF cue:** Lastly, even though we significantly reduce optimization runtime, our method does not yet reconstruct in real-time, but could be integrated with recent SLAM-based approaches [26, ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Ablation study. We ablate the impact of our learned priors for initialization, densification, and optimization updates. Only using our optimizer network does not ...

- **PDF anchors reviewed:** datasets p. 5 (4. Experiments), p. 5 (4. Experiments), metrics p. 5 (4. Experiments), p. 5 (4. Experiments), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 1 (Figure/Table caption), p. 6 (Figure/Table caption), baselines p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 5 (4. Experiments), p. 1 (Figure/Table caption), p. 5 (4. Experiments), results p. 5 (4. Experiments), p. 6 (Figure/Table caption), p. 6 (Figure/Table caption), p. 1 (Figure/Table caption), p. 3 (Figure/Table caption), p. 7 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
