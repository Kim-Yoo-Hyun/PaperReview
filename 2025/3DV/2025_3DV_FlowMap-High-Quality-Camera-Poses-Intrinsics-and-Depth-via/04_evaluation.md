# Evaluation - FlowMap: High-Quality Camera Poses, Intrinsics, and Depth via Gradient Descent

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (28 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=QI6HrBseVF&name=pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 11 (6 Results), p. 13 (6 Results), p. 14 (Figure/Table caption), p. 13 (6 Results), p. 14 (6 Results), p. 10 (Figure/Table caption)): Quantitatively, FlowMap performs slightly better than COLMAP SfM and significantly outperforms DROID-SLAM and NoPE-NeRF.

## Evaluation Body Digest

- **p. 10 / 6 Results - extractive PDF cue:** We benchmark FlowMap via the downstream task of 3D Gaussian reconstruction [29].
- **p. 14 / 6 Results - extractive PDF cue:** Qualitatively, we find that point tracks reduce drift for longer sequences, such as object-centric 360◦scenes.
- **p. 10 / 6 Results - extractive PDF cue:** We benchmark FlowMap against several baselines.
- **p. 11 / 6 Results - extractive PDF cue:** We then optimize 3D Gaussian scenes for all methods except NoPE-NeRF, since it provides its own NeRF renderings.
- **p. 11 / 6 Results - extractive PDF cue:** Because FlowMap runs on video sequences, we restrict these datasets to just the videolike sequences they provide.
- **p. 12 / 6 Results - extractive PDF cue:** 6.3 Large-Scale Robustness Study We study FlowMap's robustness by using it to estimate camera poses for 420 CO3D scenes from 10 categories.
- **p. 12 / 6 Results - extractive PDF cue:** We run FlowMap and DROID-SLAM on 420 CO3D scenes across 10 categories and plot mean ATEs with respect to CO3D's COLMAP-generated pose metadata.
- **p. 13 / 6 Results - extractive PDF cue:** 9 shows qualitative results and quantitative results averaged across 33 scenes.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 6 Results (p. 10).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 6 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Quantitatively, FlowMap performs slightly better than COLMAP SfM and significantly outperforms DROID-SLAM and NoPE-NeRF. | p. 11 (6 Results) |
| 6 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | 7 Ablations and Analysis We perform ablations to answer the following questions: - Question 1: Are FlowMap's reparameterizations of depth, pose, and intrinsics necessary, ... | p. 13 (6 Results) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Fig. 10: Effects of pretraining. While a randomly initialized FlowMap network often provides accurate poses after optimization, pre-training leads to faster convergence and slightly ... | p. 14 (Figure/Table caption) |
| 6 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | We find that free-variable variants of FlowMap produce significantly worse reconstruction results and converge much more slowly, confirming that FlowMap's reparameterizations are crucial. | p. 13 (6 Results) |
| 6 Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | This suggests that FlowMap will benefit from further improvements in point tracking methods. | p. 14 (6 Results) |

## Dataset / Benchmark Role

- **p. 10 / 6 Results - extractive PDF cue:** We benchmark FlowMap via the downstream task of 3D Gaussian reconstruction [29].
- **p. 14 / 6 Results - extractive PDF cue:** Qualitatively, we find that point tracks reduce drift for longer sequences, such as object-centric 360◦scenes.
- **p. 10 / 6 Results - extractive PDF cue:** We benchmark FlowMap against several baselines.
- **p. 11 / 6 Results - extractive PDF cue:** We then optimize 3D Gaussian scenes for all methods except NoPE-NeRF, since it provides its own NeRF renderings.
- **p. 11 / 6 Results - extractive PDF cue:** Because FlowMap runs on video sequences, we restrict these datasets to just the videolike sequences they provide.
- **p. 12 / 6 Results - extractive PDF cue:** 6.3 Large-Scale Robustness Study We study FlowMap's robustness by using it to estimate camera poses for 420 CO3D scenes from 10 categories.
- **p. 12 / 6 Results - extractive PDF cue:** We run FlowMap and DROID-SLAM on 420 CO3D scenes across 10 categories and plot mean ATEs with respect to CO3D's COLMAP-generated pose metadata.
- **p. 13 / 6 Results - extractive PDF cue:** 9 shows qualitative results and quantitative results averaged across 33 scenes.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 1: We present FlowMap, an end-to-end differentiable method that recovers poses, intrinsics, and depth maps of an input video. FlowMap is supervised only with ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Fig. 2: A FlowMap Forward Pass. Given RGB frames (red), optical flow (blue) and point tracks (green), FlowMap computes dense depth D, camera poses P, ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 3: Camera-Induced Flow Loss. To use a known correspondence uij to compute a loss L, we unproject ui using the corresponding depth map Di ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Fig. 4: We solve for the relative poses between consecutive frames using their depth maps, camera intrinsics, and optical flow. To do so, we first ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Fig. 5: View Synthesis Results. FlowMap's camera parameters and geometry pro- duce near-photorealistic 3D Gaussian Splatting results on par with COLMAP's. Sequence Length and Drift. ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 1: Camera parameter and geometry intializations from FlowMap produce 3D Gaussian reconstruction results that far outperform prior gradient-based baselines and are generally on par ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Fig. 6: Qualitative Pose Estimation Comparison. FlowMap (solid red) recovers camera poses that are very close to those of COLMAP (dotted black). 6
- **p. 11 / Figure/Table caption - extractive PDF cue:** Fig. 7: Point Clouds Reconstructed by FlowMap. Unprojecting FlowMap depths using FlowMap's intrinsics and poses yields dense and consistent point clouds. posed video trajectories. Finally, ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We benchmark FlowMap via the downstream task of 3D Gaussian reconstruction [29]. | embodiment, simulator version and control stack | p. 10 (6 Results), p. 14 (6 Results) |
| Task/environment | Qualitatively, we find that point tracks reduce drift for longer sequences, such as object-centric 360◦scenes. | reset, timeout, object/scene variation | p. 14 (6 Results), p. 10 (6 Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1 Introduction), p. 3 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 10: Effects of pretraining. While a randomly initialized FlowMap network often provides accurate poses after optimization, pre-training leads to faster convergence and slightly ... | definition/direction/unit from same section | p. 14 (Figure/Table caption) |
| 1 reports the average trajectory error (ATE) of FlowMap, DROID-SLAM, and NoPe-NeRF with respect to COLMAP. | definition/direction/unit from same section | p. 12 (6 Results) |
| Since the quality of CO3D's ground-truth trajectories varies between categories, we focus on categories that have been used to train novel view synthesis models ... | definition/direction/unit from same section | p. 12 (6 Results) |
| Fig. 2: A FlowMap Forward Pass. Given RGB frames (red), optical flow (blue) and point tracks (green), FlowMap computes dense depth D, camera poses ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| For FlowMap, we combine the output depth maps, poses, and intrinsics to yield one point per depth map pixel. | definition/direction/unit from same section | p. 11 (6 Results) |
| Point Tracking (Q2) While optical flow is only computed between adjacent frames, point track estimators can accurately track points across many frames. | definition/direction/unit from same section | p. 13 (6 Results) |
| It is worth noting that often, explicitly optimizing a focal length produces high-quality results, as indicated by the relatively high performance of the "Expl. | definition/direction/unit from same section | p. 13 (6 Results) |
| We note that FlowMap's loss formulation is compatible with conventional correspondence methods (e.g. | definition/direction/unit from same section | p. 14 (6 Results) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Table 1: Camera parameter and geometry intializations from FlowMap produce 3D Gaussian reconstruction results that far outperform prior gradient-based baselines and are generally on ... | comparison identity and matched condition | p. 10 (Figure/Table caption) |
| We benchmark FlowMap against several baselines. | comparison identity and matched condition | p. 10 (6 Results) |
| We run FlowMap and the baselines using images that have been rescaled to a resolution of about 700,000 pixels. | comparison identity and matched condition | p. 11 (6 Results) |
| Quantitatively, FlowMap performs slightly better than COLMAP SfM and significantly outperforms DROID-SLAM and NoPE-NeRF. | comparison identity and matched condition | p. 11 (6 Results) |
| Compared to DROID-SLAM, which requires ground-truth intrinsics, FlowMap produces notably lower ATEs. | comparison identity and matched condition | p. 12 (6 Results) |
| Since COLMAP's poses are not perfect [51], this comparison is not to be understood as a benchmark, but rather as an indication of how ... | comparison identity and matched condition | p. 12 (6 Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| This allows us to measure the quality of the camera parameters and geometry (depth maps) it outputs without having access to ground-truth scene geometry ... | component/input/data sensitivity | p. 10 (6 Results) |
| See the supplemental document for more ablations. | component/input/data sensitivity | p. 13 (6 Results) |
| We find that free-variable variants of FlowMap produce significantly worse reconstruction results and converge much more slowly, confirming that FlowMap's reparameterizations are crucial. | component/input/data sensitivity | p. 13 (6 Results) |
| Fig. 10: Effects of pretraining. While a randomly initialized FlowMap network often provides accurate poses after optimization, pre-training leads to faster convergence and slightly ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| During 3D Gaussian fitting, we follow the common [63] practice of fine-tuning the initial camera poses and intrinsics. | component/input/data sensitivity | p. 11 (6 Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this paper, we present FlowMap, a differentiable and surprisingly simple camera and geometry estimation method whose outputs enable photorealistic novel view synthesis. | Quantitatively, FlowMap performs slightly better than COLMAP SfM and significantly outperforms DROID-SLAM and NoPE-NeRF. | PDF body cue; verify exact table/figure and matched conditions | p. 11 (6 Results), p. 13 (6 Results), p. 14 (Figure/Table caption), p. 13 (6 Results), p. 14 (6 Results), p. 10 (Figure/Table caption) |
| Primary metric/result | 7 Ablations and Analysis We perform ablations to answer the following questions: - Question 1: Are FlowMap's reparameterizations of depth, pose, and intrinsics necessary, ... | numeric claim only at cited anchor | p. 13 (6 Results) |

- Numeric sentences retained from the body:
- **p. 12 / 6 Results - extractive PDF cue:** We note that COLMAP failed to estimate poses for 36 scenes, possibly because we ran it at a sparser frame rate to be consistent with ...
- **p. 13 / 6 Results - extractive PDF cue:** 9 shows qualitative results and quantitative results averaged across 33 scenes.
- **p. 14 / 6 Results - extractive PDF cue:** Randomly initialized FlowMap networks often require more than 20,000 steps to match the accuracy of a pre-trained initialization at 2,000 steps.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | FlowMap has several limitations that suggest exciting directions for future work. | p. 14 (8 Discussion) |
| body limitation/failure cue | However, on about 20 percent of scenes, this approach falls into a local minimum and reconstruction fails catastrophically. | p. 13 (6 Results) |
| body limitation/failure cue | DROID-SLAM* COLMAP Ours ATE Failure Fig. | p. 12 (6 Results) |
| body limitation/failure cue | We note that COLMAP failed to estimate poses for 36 scenes, possibly because we ran it at a sparser frame rate to be consistent ... | p. 12 (6 Results) |
| body limitation/failure cue | Table 1: Camera parameter and geometry intializations from FlowMap produce 3D Gaussian reconstruction results that far outperform prior gradient-based baselines and are generally on ... | p. 10 (Figure/Table caption) |
| body limitation/failure cue | Second, we mainly analyze FlowMap in the setting of per-scene optimization, where our results demonstrate that the gradients provided by FlowMap's formulation are robustly ... | p. 14 (8 Discussion) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In other words, FlowMap solves SfM by learning the depth network's parameters; camera poses and intrinsics are computed via analytical feed-forward modules without free ... | p. 2 (1 Introduction) |
| FlowMap directly minimizes the difference between optical flow that is induced by a camera moving through a static 3D scene and precomputed correspondences in ... | p. 2 (1 Introduction) |
| However, note that COLMAP MVS is rarely used in practice because it can be prohibitively time-consuming to run. | p. 10 (6 Results) |
| We run FlowMap and the baselines using images that have been rescaled to a resolution of about 700,000 pixels. | p. 11 (6 Results) |
| As noted previously, COLMAP MVS is rarely used for 3D Gaussian Splatting, since it is very time-consuming to run on high-resolution images. | p. 11 (6 Results) |
| We also re-run COLMAP on the same data. | p. 12 (6 Results) |
| We compare these trajectories to CO3D's pose annotations, which were computed using COLMAP. | p. 12 (6 Results) |
| Point Tracking (Q2) While optical flow is only computed between adjacent frames, point track estimators can accurately track points across many frames. | p. 13 (6 Results) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 14 / 8 Discussion - extractive PDF cue:** FlowMap has several limitations that suggest exciting directions for future work.
- **p. 13 / 6 Results - extractive PDF cue:** However, on about 20 percent of scenes, this approach falls into a local minimum and reconstruction fails catastrophically.
- **p. 12 / 6 Results - extractive PDF cue:** DROID-SLAM* COLMAP Ours ATE Failure Fig.
- **p. 12 / 6 Results - extractive PDF cue:** We note that COLMAP failed to estimate poses for 36 scenes, possibly because we ran it at a sparser frame rate to be consistent with ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 1: Camera parameter and geometry intializations from FlowMap produce 3D Gaussian reconstruction results that far outperform prior gradient-based baselines and are generally on par ...
- **p. 14 / 8 Discussion - extractive PDF cue:** Second, we mainly analyze FlowMap in the setting of per-scene optimization, where our results demonstrate that the gradients provided by FlowMap's formulation are robustly lead ...

- **PDF anchors reviewed:** datasets p. 10 (6 Results), p. 14 (6 Results), p. 10 (6 Results), p. 11 (6 Results), p. 11 (6 Results), p. 12 (6 Results), metrics p. 14 (Figure/Table caption), p. 12 (6 Results), p. 12 (6 Results), p. 5 (Figure/Table caption), p. 11 (6 Results), p. 13 (6 Results), baselines p. 10 (Figure/Table caption), p. 10 (6 Results), p. 11 (6 Results), p. 11 (6 Results), p. 12 (6 Results), p. 12 (6 Results), results p. 11 (6 Results), p. 13 (6 Results), p. 14 (Figure/Table caption), p. 13 (6 Results), p. 14 (6 Results), p. 10 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
