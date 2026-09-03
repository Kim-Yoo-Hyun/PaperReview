# Evaluation - Surface Reconstruction for 3D Gaussian Splatting via Local Structural Hints

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/274_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/00274.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 13 (4 Experiments), p. 13 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments)): While keeping the MLS term with the gradient term in the joint loss (w/o eikonal term), the F-score can be significantly improved thanks to the zero-order approximation of the MLS ...

## Evaluation Body Digest

- **p. 10 / 4 Experiments - extractive body cue:** 2) ScanNet [10] is a real-world dataset captured with challenging image quality.
- **p. 10 / 4 Experiments - extractive body cue:** We conduct our experiments on 1) Replica [44] is a synthesized dataset with accurate camera poses and ground truth mesh for evaluation. we use 8 ...
- **p. 14 / 4 Experiments - extractive body cue:** Chamfer-L1↓F-score ↑ COLMAP [41] 0.141 0.537 UNISURF [33] 0.359 0.267 NeuS [51] 0.194 0.291 VolSDF [58] 0.267 0.346 Manhattan-SDF [16] 0.070 0.602 MonoSDF (Grid) [62] ...
- **p. 11 / 4 Experiments - extractive body cue:** GSrec 11 Table 1: The quantitative results of the scene reconstruction on 8 Replica scenes.
- **p. 12 / 4 Experiments - extractive body cue:** Notably, the average training time of our approach on this dataset is about 40 minutes, which is similar to SuGaR.
- **p. 14 / 4 Experiments - extractive body cue:** This shows the potential ability of 3DGS to achieve high-quality surface reconstruction for real-world capture.
- **p. 12 / 4 Experiments - extractive body cue:** In terms of storage, thanks to the Scaffold-GS baseline, our framework only takes about 45MB for each scene while the size of the SuGaR model ...
- **p. 10 / 4 Experiments - extractive body cue:** For quantitative evaluation of surface quality, we measure Chamfer Distance, Normal Consistency Score and Fscore with a threshold of 5cm on Replica.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 10).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | While keeping the MLS term with the gradient term in the joint loss (w/o eikonal term), the F-score can be significantly improved thanks to ... | p. 13 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 3 (b), although L = 1 has achieved good results, the F-score keeps improving as L gets increased. | p. 13 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | It provides very important hints about the Gaussian orientation, which also significantly improves the quality of Poisson reconstruction. | p. 12 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our approach significantly improves the quality of the final mesh. single Gaussian assumption, which potentially makes the output mesh rough. | p. 12 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 1 where our method outperforms both of SuGaR's variants with a clear margin. | p. 11 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 10 / 4 Experiments - extractive body cue:** 2) ScanNet [10] is a real-world dataset captured with challenging image quality.
- **p. 10 / 4 Experiments - extractive body cue:** We conduct our experiments on 1) Replica [44] is a synthesized dataset with accurate camera poses and ground truth mesh for evaluation. we use 8 ...
- **p. 14 / 4 Experiments - extractive body cue:** Chamfer-L1↓F-score ↑ COLMAP [41] 0.141 0.537 UNISURF [33] 0.359 0.267 NeuS [51] 0.194 0.291 VolSDF [58] 0.267 0.346 Manhattan-SDF [16] 0.070 0.602 MonoSDF (Grid) [62] ...
- **p. 11 / 4 Experiments - extractive body cue:** GSrec 11 Table 1: The quantitative results of the scene reconstruction on 8 Replica scenes.
- **p. 12 / 4 Experiments - extractive body cue:** Notably, the average training time of our approach on this dataset is about 40 minutes, which is similar to SuGaR.
- **p. 14 / 4 Experiments - extractive body cue:** This shows the potential ability of 3DGS to achieve high-quality surface reconstruction for real-world capture.
- **p. 12 / 4 Experiments - extractive body cue:** In terms of storage, thanks to the Scaffold-GS baseline, our framework only takes about 45MB for each scene while the size of the SuGaR model ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 1: Overview of GSrec. GSrec first leverages the monocular geometry cue as supervision to adjust the position and orientation of each 3D Gaussian primitive. ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 2: Joint optimization of 3DGS and neural implicit representation. We propose a novel strategy to further align the Gaussians with the surface. We jointly ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 3: Qualitative results on Replica [44]. The surface produced by our approach achieves better quality compared with SuGaR [15] owing to the structural hints. ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 1: The quantitative results of the scene reconstruction on 8 Replica scenes. We compare our method against the SoTA surface reconstruction method for 3D ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 2: Ablation study on Replica. We compared the key components with the variants of [25] including the guidance and the joint optimization.
- **p. 12 / Figure/Table caption - extractive body cue:** Fig. 4: Reconstructed surface by ablating proposed components on
- **p. 13 / Figure/Table caption - extractive body cue:** Table 3: Ablation study about the joint MLS optimization and the MLS computation. We provide an in-depth analysis by verifying the effectiveness of the joint ...
- **p. 14 / Figure/Table caption - extractive body cue:** Table 4: Scene-level 3D Reconstruction on ScanNet. (a) The quantitative re- sults of several neural implicit surface reconstruction methods and the 3DGS-based approaches [15] (b) ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 2) ScanNet [10] is a real-world dataset captured with challenging image quality. | embodiment, simulator version and control stack | p. 10 (4 Experiments), p. 10 (4 Experiments) |
| Task/environment | We conduct our experiments on 1) Replica [44] is a synthesized dataset with accurate camera poses and ground truth mesh for evaluation. we use ... | reset, timeout, object/scene variation | p. 10 (4 Experiments), p. 14 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 9 (3 Method), p. 1 (1 Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (3 Method), p. 5 (3 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For quantitative evaluation of surface quality, we measure Chamfer Distance, Normal Consistency Score and Fscore with a threshold of 5cm on Replica. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| We compare our method against the SoTA surface reconstruction method for 3D Gaussian Splatting [15] in terms of Chamfer distance and F-score. | definition/direction/unit from same section | p. 11 (4 Experiments) |
| Chamfer distance↓ room0 room1 room2 office0 office1 office2 office3 office4 average SuGaR (density) [15] 8.84 9.79 12.59 7.89 14.31 11.24 9.54 12.06 10.78 SuGaR ... | definition/direction/unit from same section | p. 11 (4 Experiments) |
| We discover the naive incorporation of depth guidance will slightly impair the F-score, which might be due to the inaccurate depth calculation in Eqn.(5). | definition/direction/unit from same section | p. 12 (4 Experiments) |
| While keeping the MLS term with the gradient term in the joint loss (w/o eikonal term), the F-score can be significantly improved thanks to ... | definition/direction/unit from same section | p. 13 (4 Experiments) |
| Normal-C↑F-score↑ w/o MLS term 84.15 64.55 w/o gradient term 81.38 63.56 w/o eikonal term 84.64 66.62 Full joint loss 85.23 67.22 Normal-C↑F-score↑ L=1 84.49 ... | definition/direction/unit from same section | p. 13 (4 Experiments) |
| Chamfer-L1↓F-score ↑ COLMAP [41] 0.141 0.537 UNISURF [33] 0.359 0.267 NeuS [51] 0.194 0.291 VolSDF [58] 0.267 0.346 Manhattan-SDF [16] 0.070 0.602 MonoSDF (Grid) ... | definition/direction/unit from same section | p. 14 (4 Experiments) |
| Method Geometry Guidance MLS design Reconstruction metric Normal Depth IMLS RIMLS Normal-C ↑ F-score ↑ (a) Scaffold-GS [25]+D ✗ ✓ ✗ ✗ 66.53±2.56 55.33±6.29 ... | definition/direction/unit from same section | p. 12 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We compare with previous strong baselines of neural implicit surface [16,33,51,58,62] and the 3DGS-based approach SuGaR [15]. | comparison identity and matched condition | p. 14 (4 Experiments) |
| Following the setting [16,62], 4 scenes are selected from ScanNet for experiments and compared ours with both the | comparison identity and matched condition | p. 10 (4 Experiments) |
| We compared the final refinement mesh from SuGaR with our output. | comparison identity and matched condition | p. 11 (4 Experiments) |
| 1 where our method outperforms both of SuGaR's variants with a clear margin. | comparison identity and matched condition | p. 11 (4 Experiments) |
| We compared the key components with the variants of [25] including the guidance and the joint optimization. | comparison identity and matched condition | p. 12 (4 Experiments) |
| 2, the inaccurate normal estimated by the density gradient will lead to a degraded iso-surface estimation compared with Scaffold-GS+D and ScaffoldGS+N. | comparison identity and matched condition | p. 12 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 2: Ablation study on Replica. We compared the key components with the variants of [25] including the guidance and the joint optimization. | component/input/data sensitivity | p. 12 (Figure/Table caption) |
| Table 3: Ablation study about the joint MLS optimization and the MLS computation. We provide an in-depth analysis by verifying the effectiveness of the ... | component/input/data sensitivity | p. 13 (Figure/Table caption) |
| We term these two variants as SuGaR (SDF)/(density). | component/input/data sensitivity | p. 11 (4 Experiments) |
| 1 where our method outperforms both of SuGaR's variants with a clear margin. | component/input/data sensitivity | p. 11 (4 Experiments) |
| To delve into its functionality, we show the results by ablation study over the MLS-based joint optimization. | component/input/data sensitivity | p. 13 (4 Experiments) |
| Although the MonoSDF (MLP) adopts pure MLP structure which shows robustness to the camera noise, the training time of such a variant gets much ... | component/input/data sensitivity | p. 14 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To address this, we propose a novel regularizer that leverages a neural implicit network to approximate the signed distance values of the MLS function ... | While keeping the MLS term with the gradient term in the joint loss (w/o eikonal term), the F-score can be significantly improved thanks to ... | PDF body cue; verify exact table/figure and matched conditions | p. 13 (4 Experiments), p. 13 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments) |
| Primary metric/result | 3 (b), although L = 1 has achieved good results, the F-score keeps improving as L gets increased. | numeric claim only at cited anchor | p. 13 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 10 / 4 Experiments - extractive body cue:** Our experiments were run on a 24GB NVIDIA RTX 3090 GPU.
- **p. 10 / 4 Experiments - extractive body cue:** We conduct our experiments on 1) Replica [44] is a synthesized dataset with accurate camera poses and ground truth mesh for evaluation. we use 8 ...
- **p. 10 / 4 Experiments - extractive body cue:** Following the setting [16,62], 4 scenes are selected from ScanNet for experiments and compared ours with both the
- **p. 12 / 4 Experiments - extractive body cue:** Method Geometry Guidance MLS design Reconstruction metric Normal Depth IMLS RIMLS Normal-C ↑ F-score ↑ (a) Scaffold-GS [25]+D ✗ ✓ ✗ ✗ 66.53±2.56 55.33±6.29 (b) ...
- **p. 14 / 4 Experiments - extractive body cue:** 4 (a), we find that our approach is comparable with ManhattanSDF [16] and the MonoSDF [62] in which multi-resolution grid embedding [32] is utilized, while ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 2: Joint optimization of 3DGS and neural implicit representation. We propose a novel strategy to further align the Gaussians with the surface. We ... | p. 8 (Figure/Table caption) |
| body limitation/failure cue | Although the MonoSDF (MLP) adopts pure MLP structure which shows robustness to the camera noise, the training time of such a variant gets much ... | p. 14 (4 Experiments) |
| body limitation/failure cue | 2, the inaccurate normal estimated by the density gradient will lead to a degraded iso-surface estimation compared with Scaffold-GS+D and ScaffoldGS+N. | p. 12 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Our experiments were run on a 24GB NVIDIA RTX 3090 GPU. | p. 10 (4 Experiments) |
| Notably, the average training time of our approach on this dataset is about 40 minutes, which is similar to SuGaR. | p. 12 (4 Experiments) |
| Although the MonoSDF (MLP) adopts pure MLP structure which shows robustness to the camera noise, the training time of such a variant gets much ... | p. 14 (4 Experiments) |
| 4 (a), we find that our approach is comparable with ManhattanSDF [16] and the MonoSDF [62] in which multi-resolution grid embedding [32] is utilized, ... | p. 14 (4 Experiments) |
| Scaffold-GS proposes to use learnable anchor points as seeds and generate new Gaussians from these anchors along with their attributes (including color, opacity, and ... | p. 6 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 2: Joint optimization of 3DGS and neural implicit representation. We propose a novel strategy to further align the Gaussians with the surface. We jointly ...
- **p. 14 / 4 Experiments - extractive body cue:** Although the MonoSDF (MLP) adopts pure MLP structure which shows robustness to the camera noise, the training time of such a variant gets much longer ...
- **p. 12 / 4 Experiments - extractive body cue:** 2, the inaccurate normal estimated by the density gradient will lead to a degraded iso-surface estimation compared with Scaffold-GS+D and ScaffoldGS+N.

- **Evidence anchors reviewed:** datasets p. 10 (4 Experiments), p. 10 (4 Experiments), p. 14 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 14 (4 Experiments), metrics p. 10 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), p. 13 (4 Experiments), baselines p. 14 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments), results p. 13 (4 Experiments), p. 13 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
