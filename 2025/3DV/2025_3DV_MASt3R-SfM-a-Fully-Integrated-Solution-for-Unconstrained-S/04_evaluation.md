# Evaluation - MASt3R-SfM: a Fully-Integrated Solution for Unconstrained Structure-from-Motion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://3dvconf.github.io/2025/accepted-papers/; PDF retrieval source: https://openreview.net/attachment?id=5uw1GRBFoT&name=pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (5.2. Comparison with the state of the art), p. 7 (5.2. Comparison with the state of the art), p. 8 (8.4 GB), p. 9 (8.4 GB), p. 8 (8.4 GB), p. 9 (Figure/Table caption)): MASt3R-SfM provides nearly constant performance for all ranges, significantly outperforming COLMAP, Ace-Zero, FlowMap and VGGSfM in all settings.

## Evaluation Body Digest

- **p. 7 / 5.2. Comparison with the state of the art - extractive PDF cue:** We point out that, not only these splits select a subset of scenes for each dataset (in details: 3 scenes from Mip-360, 7 from LLFF, ...
- **p. 6 / 5.1. Experimental setup - extractive PDF cue:** Namely, we employ Tanks&Temples [25] (T&T), a 3D reconstruction dataset comprising 21 scenes ranging from 151 to 1106 images; ETH3D [49], a multi-view stereo dataset ...
- **p. 6 / 5.1. Experimental setup - extractive PDF cue:** When reported at the dataset level, metrics are averaged over all scenes.
- **p. 7 / 5.2. Comparison with the state of the art - extractive PDF cue:** We thus experiment on the ETH3D dataset, a photograph dataset, composed of 13 scenes with up to to 76 images per scene.
- **p. 8 / 8.4 GB - extractive PDF cue:** We compare ASMK on MASt3R features to the off-the-shelf retrieval method FIRe [66], also based on ASMK, on the Aachen-Day-Night [45] and InLoc [53] datasets.
- **p. 8 / 8.4 GB - extractive PDF cue:** 14.3 min Table 4: Ablation of scene graph construction on Tanks&Temples (200 view subset).
- **p. 8 / 8.4 GB - extractive PDF cue:** We report standard visual localization accuracy metrics, i.e. the percentages of images successfully localized within error thresholds of (0.25m, 2°) / (0.5m, 5°) / (5m, ...
- **p. 15 / Figure/Table caption - extractive PDF cue:** Table 10: Detailed per-scene results on Tanks & Temples in terms of ATE, pose accuracy (RTA@5 and RRA@5) and registration rate (Reg.). For easier readability, ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experimental Results (p. 6); 5.1. Experimental setup (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 5.2. Comparison with the state of the art | EMPIRICAL / SOURCE-REPORTED EVALUATION | MASt3R-SfM provides nearly constant performance for all ranges, significantly outperforming COLMAP, Ace-Zero, FlowMap and VGGSfM in all settings. | p. 7 (5.2. Comparison with the state of the art) |
| 5.2. Comparison with the state of the art | EMPIRICAL / SOURCE-REPORTED EVALUATION | Results reported in table 3 shows that MASt3R-SfM outperforms all competing approaches by a large margin on average. | p. 7 (5.2. Comparison with the state of the art) |
| 8.4 GB | EMPIRICAL / SOURCE-REPORTED EVALUATION | Slightly better results are achieved with the complete graph, but it is about 10x slower than retrieval-based graph and no scalable in general. | p. 8 (8.4 GB) |
| 8.4 GB | EMPIRICAL / SOURCE-REPORTED EVALUATION | Good enough poses are typically obtained after 𝜈1 ≃250 iterations of coarse optimization, from which point refinement consistently improves. | p. 9 (8.4 GB) |
| 8.4 GB | EMPIRICAL / SOURCE-REPORTED EVALUATION | We report standard visual localization accuracy metrics, i.e. the percentages of images successfully localized within error thresholds of (0.25m, 2°) / (0.5m, 5°) / ... | p. 8 (8.4 GB) |

## Dataset / Benchmark Role

- **p. 7 / 5.2. Comparison with the state of the art - extractive PDF cue:** We point out that, not only these splits select a subset of scenes for each dataset (in details: 3 scenes from Mip-360, 7 from LLFF, ...
- **p. 6 / 5.1. Experimental setup - extractive PDF cue:** Namely, we employ Tanks&Temples [25] (T&T), a 3D reconstruction dataset comprising 21 scenes ranging from 151 to 1106 images; ETH3D [49], a multi-view stereo dataset ...
- **p. 6 / 5.1. Experimental setup - extractive PDF cue:** When reported at the dataset level, metrics are averaged over all scenes.
- **p. 7 / 5.2. Comparison with the state of the art - extractive PDF cue:** We thus experiment on the ETH3D dataset, a photograph dataset, composed of 13 scenes with up to to 76 images per scene.
- **p. 8 / 8.4 GB - extractive PDF cue:** We compare ASMK on MASt3R features to the off-the-shelf retrieval method FIRe [66], also based on ASMK, on the Aachen-Day-Night [45] and InLoc [53] datasets.
- **p. 8 / 8.4 GB - extractive PDF cue:** 14.3 min Table 4: Ablation of scene graph construction on Tanks&Temples (200 view subset).

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Top: Relative rotation (RRA) and translation (RTA) accuracies on the CO3Dv2 dataset when varying the number of input views with random subsampling (the ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Overview of the proposed MASt3R-SfM method. Given an unconstrained image collections, possibly small (1 image) or large (> 1000 images), we start by ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Factor graph for MASt3R-SfM. Free vari- ables on the top row serve to construct the constrained pointmap 𝜒, which follows the pinhole camera ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: Results on Tanks&Temples in terms of ATE and overall registration rate (Reg.). For easier readability, we color-code ATE results as a linear gradient ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2: Multi-view pose regression on CO3Dv2 [39] and RealEstate10K [70] with 10 random frames. Parenthesis () denote methods that do not report results on ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3: Detailed per-scene translation and rotation accuracies (↑) on ETH-3D. For clarity, we color-code results with a linear gradient between the worst and best ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4: Ablation of scene graph construction on Tanks&Temples (200 view subset). See text for details. Ablation ATE↓ RTA@5↑ RRA@5↑ #Pairs Retrieval
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 5: Ablations on Tanks&Temples (200 view sub- set). See text for details. Scene graph. We evaluate different construction strategies for the scene graph in ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We point out that, not only these splits select a subset of scenes for each dataset (in details: 3 scenes from Mip-360, 7 from ... | embodiment, simulator version and control stack | p. 7 (5.2. Comparison with the state of the art), p. 6 (5.1. Experimental setup) |
| Task/environment | Namely, we employ Tanks&Temples [25] (T&T), a 3D reconstruction dataset comprising 21 scenes ranging from 151 to 1106 images; ETH3D [49], a multi-view stereo ... | reset, timeout, object/scene variation | p. 6 (5.1. Experimental setup), p. 6 (5.1. Experimental setup) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3. Preliminaries), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3. Preliminaries), p. 4 (4.1. Scene graph) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We report standard visual localization accuracy metrics, i.e. the percentages of images successfully localized within error thresholds of (0.25m, 2°) / (0.5m, 5°) / ... | definition/direction/unit from same section | p. 8 (8.4 GB) |
| Table 10: Detailed per-scene results on Tanks & Temples in terms of ATE, pose accuracy (RTA@5 and RRA@5) and registration rate (Reg.). For easier ... | definition/direction/unit from same section | p. 15 (Figure/Table caption) |
| We evaluate the average translation error (ATE) as in FlowMap [50], i.e. we align estimated camera positions to ground-truth ones with Procrustes [32] and ... | definition/direction/unit from same section | p. 6 (5.1. Experimental setup) |
| Following [50], we report results in terms of Average Translation Error (ATE) against the COLMAP pseudo ground-truth in table 1 (left), computed from the ... | definition/direction/unit from same section | p. 7 (5.2. Comparison with the state of the art) |
| 4, we plot the pose accuracy as a function of the number of iterations during coarse optimization and refinement. | definition/direction/unit from same section | p. 9 (8.4 GB) |
| Figure 2: Overview of the proposed MASt3R-SfM method. Given an unconstrained image collections, possibly small (1 image) or large (> 1000 images), we start ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Finally, we report the successful registration rate as a percentage, denoted as Reg. | definition/direction/unit from same section | p. 6 (5.1. Experimental setup) |
| Table 7: Comparison of retrieval based on MASt3R features. We compare the visual localization accuracy using top-20 retrieved images with ASMK (top row), a ... | definition/direction/unit from same section | p. 10 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Overall, we find that combining short-range (𝑘-NN) and long-range (keyframes) connections is important for Method Aachen-Day-Night↑ InLoc↑ Day Night DUC1 DUC2 Kapture [21]+R2D2 [41] ... | comparison identity and matched condition | p. 8 (8.4 GB) |
| After presenting the datasets and metrics, we extensively compare our approach with state-of-the-art SfM methods in diverse conditions. | comparison identity and matched condition | p. 6 (5. Experimental Results) |
| We distinguish between (a) multi-view and (b) pairwise methods. ferent state-of-the-art methods. | comparison identity and matched condition | p. 7 (5.2. Comparison with the state of the art) |
| Results reported in table 3 shows that MASt3R-SfM outperforms all competing approaches by a large margin on average. | comparison identity and matched condition | p. 7 (5.2. Comparison with the state of the art) |
| Except for the ‘complete' case, we try to match the number of pairs used in the baseline retrieval strategy. | comparison identity and matched condition | p. 8 (8.4 GB) |
| We finally present several ablations. | comparison identity and matched condition | p. 6 (5. Experimental Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We finally present several ablations. | component/input/data sensitivity | p. 6 (5. Experimental Results) |
| 0.014) for 𝜈1 = 300 iterations and 𝜆1 = 1.5 (resp. 𝜈2 = 300 and 𝜆2 = 0.5) for the coarse (resp. refinement) optimization, ... | component/input/data sensitivity | p. 6 (5.1. Experimental setup) |
| The fact that COLMAP and VGGSfM also perform relatively poorly indicates a high sensitivity to not having highly overlapping images, meaning that in the ... | component/input/data sensitivity | p. 7 (5.2. Comparison with the state of the art) |
| 14.3 min Table 4: Ablation of scene graph construction on Tanks&Temples (200 view subset). | component/input/data sensitivity | p. 8 (8.4 GB) |
| We also try to perform the optimization without optimizing depth (i.e. using frozen canonical depthmaps, which proves useful for purely rotational cases, denoted as ... | component/input/data sensitivity | p. 9 (8.4 GB) |
| Figure 1: Top: Relative rotation (RRA) and translation (RTA) accuracies on the CO3Dv2 dataset when varying the number of input views with random subsampling ... | component/input/data sensitivity | p. 2 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We present a novel large-scale 3D reconstruction approach consisting of four steps outlined in fig. | MASt3R-SfM provides nearly constant performance for all ranges, significantly outperforming COLMAP, Ace-Zero, FlowMap and VGGSfM in all settings. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (5.2. Comparison with the state of the art), p. 7 (5.2. Comparison with the state of the art), p. 8 (8.4 GB), p. 9 (8.4 GB), p. 8 (8.4 GB), p. 9 (Figure/Table caption) |
| Primary metric/result | Results reported in table 3 shows that MASt3R-SfM outperforms all competing approaches by a large margin on average. | numeric claim only at cited anchor | p. 7 (5.2. Comparison with the state of the art) |

- Numeric sentences retained from the body:
- **p. 6 / 5.1. Experimental setup - extractive PDF cue:** Namely, we employ Tanks&Temples [25] (T&T), a 3D reconstruction dataset comprising 21 scenes ranging from 151 to 1106 images; ETH3D [49], a multi-view stereo dataset ...
- **p. 7 / 5.2. Comparison with the state of the art - extractive PDF cue:** We form new splits by regularly subsampling the original images for 25, 50, 100 and 200 frames.
- **p. 7 / 5.2. Comparison with the state of the art - extractive PDF cue:** We point out that, not only these splits select a subset of scenes for each dataset (in details: 3 scenes from Mip-360, 7 from LLFF, ...
- **p. 7 / 5.2. Comparison with the state of the art - extractive PDF cue:** We thus experiment on the ETH3D dataset, a photograph dataset, composed of 13 scenes with up to to 76 images per scene.
- **p. 8 / 8.4 GB - extractive PDF cue:** Slightly better results are achieved with the complete graph, but it is about 10x slower than retrieval-based graph and no scalable in general.
- **p. 5 / 4.2. Local reconstruction - extractive PDF cue:** Focals Quaternions Translations Anchor depths 𝑓∈ℝ𝑁 𝜚∈ℝ𝑁×4 t𝑛∈ℝ𝑁×3 ሶ𝑍𝑛∈ℝ𝑁×𝐻 𝑠×𝑊 𝑠 𝑃= 𝑅/𝑡∈ℝ𝑁×4×4 𝑍∈ℝ𝑁×𝐻×𝑊 𝜋-1 𝐾, 𝑃, 𝑍→𝜒∈ℝ𝑁×𝑊×𝐻×3 𝐾∈ℝ𝑁×3×3 Intrinsics Extrinsics Depthmaps Constrained pointmap Figure ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | After analyzing the results, we observe that failures are due to the presence of outlier (false) matches between similar-looking structures. | p. 10 (6. Conclusion) |
| body limitation/failure cue | MASt3R-SfM: a Fully-Integrated Solution for Unconstrained Structure-from-Motion 7154 false matches (30° azimut, 0° elevation) (240° azimut, 0° elevation) 6659 false matches (60° azimut, 30° ... | p. 12 (6. Conclusion) |
| body limitation/failure cue | In such cases, the triangulation step from traditional SfM pipeline becomes ill-defined and notoriously fails. | p. 10 (6. Conclusion) |
| body limitation/failure cue | Figure 6: In all failure cases that we have manually reviewed, the root cause of failure was the presence of wrong matches (outliers) between ... | p. 12 (Figure/Table caption) |
| body limitation/failure cue | Thanks to the strong priors encoded in the underlying MASt3R foundation model upon which our approach is based, it can even deal with cases ... | p. 9 (6. Conclusion) |
| body limitation/failure cue | The fact that COLMAP and VGGSfM also perform relatively poorly indicates a high sensitivity to not having highly overlapping images, meaning that in the ... | p. 7 (5.2. Comparison with the state of the art) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Since the encoder features {𝐹𝑛}𝑛=1..𝑁have already been extracted and cached during scene graph construction (section 4.1), we only need to run the ViT decoder ... | p. 5 (4.2. Local reconstruction) |
| For the two gradient descents, we use the Adam optimizer [24] with a learning rate of 0.07 (resp. | p. 6 (5.1. Experimental setup) |
| 0.014) for 𝜈1 = 300 iterations and 𝜆1 = 1.5 (resp. 𝜈2 = 300 and 𝜆2 = 0.5) for the coarse (resp. refinement) optimization, ... | p. 6 (5.1. Experimental setup) |
| For easier readability, we color-code ATE results as a linear gradient between worst and best ATE for a given dataset or split; and Reg ... | p. 7 (5.2. Comparison with the state of the art) |
| Following [50], we report results in terms of Average Translation Error (ATE) against the COLMAP pseudo ground-truth in table 1 (left), computed from the ... | p. 7 (5.2. Comparison with the state of the art) |
| We follow the protocol from [27] and retrieve the top-𝑘posed images in the database for each query, extract 2D-3D corresponds and run RANSAC to ... | p. 8 (8.4 GB) |
| We then compute local 3D reconstruction and matches for each edge using again a frozen MASt3R's decoder. | p. 4 (4. Proposed Method) |
| Note that this method is training-free, only requiring to compute the whitening matrix and the codebook once from a representative set of features. | p. 4 (4.1. Scene graph) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 6. Conclusion - extractive PDF cue:** After analyzing the results, we observe that failures are due to the presence of outlier (false) matches between similar-looking structures.
- **p. 12 / 6. Conclusion - extractive PDF cue:** MASt3R-SfM: a Fully-Integrated Solution for Unconstrained Structure-from-Motion 7154 false matches (30° azimut, 0° elevation) (240° azimut, 0° elevation) 6659 false matches (60° azimut, 30° elevation) ...
- **p. 10 / 6. Conclusion - extractive PDF cue:** In such cases, the triangulation step from traditional SfM pipeline becomes ill-defined and notoriously fails.
- **p. 12 / Figure/Table caption - extractive PDF cue:** Figure 6: In all failure cases that we have manually reviewed, the root cause of failure was the presence of wrong matches (outliers) between similar-looking ...
- **p. 9 / 6. Conclusion - extractive PDF cue:** Thanks to the strong priors encoded in the underlying MASt3R foundation model upon which our approach is based, it can even deal with cases without ...
- **p. 7 / 5.2. Comparison with the state of the art - extractive PDF cue:** The fact that COLMAP and VGGSfM also perform relatively poorly indicates a high sensitivity to not having highly overlapping images, meaning that in the end ...

- **PDF anchors reviewed:** datasets p. 7 (5.2. Comparison with the state of the art), p. 6 (5.1. Experimental setup), p. 6 (5.1. Experimental setup), p. 7 (5.2. Comparison with the state of the art), p. 8 (8.4 GB), p. 8 (8.4 GB), metrics p. 8 (8.4 GB), p. 15 (Figure/Table caption), p. 6 (5.1. Experimental setup), p. 7 (5.2. Comparison with the state of the art), p. 9 (8.4 GB), p. 4 (Figure/Table caption), baselines p. 8 (8.4 GB), p. 6 (5. Experimental Results), p. 7 (5.2. Comparison with the state of the art), p. 7 (5.2. Comparison with the state of the art), p. 8 (8.4 GB), p. 6 (5. Experimental Results), results p. 7 (5.2. Comparison with the state of the art), p. 7 (5.2. Comparison with the state of the art), p. 8 (8.4 GB), p. 9 (8.4 GB), p. 8 (8.4 GB), p. 9 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
