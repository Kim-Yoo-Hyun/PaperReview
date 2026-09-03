# Evaluation - EnerGS: Energy-Based Gaussian Splatting under Partial Geometric Priors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ebt72acjt6; PDF retrieval source: https://openreview.net/pdf/bfce7f71c1e37001e68263ecce2837ec77904739.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (5.2. Quantitative Analysis), p. 6 (5.1. Experimental Setup), p. 8 (5.5. Training Generalization Comparison), p. 1 (Figure/Table caption), p. 7 (Figure/Table caption), p. 19 (Figure/Table caption)): On KITTI, it attains the highest PSNR and OccCov together with the lowest Leak score, indicating improved alignment with occupied regions and fewer free space violations.

## Evaluation Body Digest

- **p. 6 / 5.1. Experimental Setup - extractive body cue:** Our study focuses exclusively on static scenes, and consequently, the evaluation excludes all dynamic objects.
- **p. 6 / 5.3. Qualitative Results - extractive body cue:** 2 compares novel view synthesis results of state-ofthe-art baselines and our EnerGS across different scenes.
- **p. 7 / 5.3. Qualitative Results - extractive body cue:** Visual Comparison on KITTI and Waymo Open Dataset.
- **p. 7 / 5.3. Qualitative Results - extractive body cue:** Method KITTI Waymo Open Dataset Photometry Geometry #G (M)↓ Photometry Geometry #G (M)↓ PSNR↑SSIM↑Leak↓OccCov↑Margin↑Thick↓ PSNR↑SSIM↑Leak↓OccCov↑Margin↑Thick↓ 3DGS ToG 23 15.01 0.938 12.5 16.1 0.22 1.39 1.51 ...
- **p. 8 / 5.3. Qualitative Results - extractive body cue:** Ablation Study on KITTI and Waymo Open Dataset.
- **p. 8 / 5.3. Qualitative Results - extractive body cue:** Variant KITTI Waymo Open Dataset Photometry Geometry Photometry Geometry ∆PSNR↑∆SSIM↑∆Leak↓∆OccCov↑∆Margin↑∆Thick↓∆#G↓ ∆PSNR↑∆SSIM↑∆Leak↓∆OccCov↑∆Margin↑∆Thick↓∆#G↓ Full EnerGS 0.00 0.000 0.0 0.0 0.00 0.00 0.00 0.00 0.000 0.0 0.0 0.00 ...
- **p. 5 / 4.3. Optimization Stability - extractive body cue:** We analyze the smoothness of the optimization trajectory by examining the Lipschitz properties of the driving force.
- **p. 5 / 4.2. Exclusion of Degenerate Solutions - extractive body cue:** It must migrate along the trajectory defined by -∂dT ∂µ until exiting Ωfree, thereby ensuring Sdeg ∩Ωfree = ∅in the convergence limit.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 3.5. Complexity and Implementation Efficiency (p. 4); 5. Experiments (p. 6); 5.1. Experimental Setup (p. 6); 5.3. Qualitative Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.2. Quantitative Analysis | EMPIRICAL / SOURCE-REPORTED EVALUATION | On KITTI, it attains the highest PSNR and OccCov together with the lowest Leak score, indicating improved alignment with occupied regions and fewer free ... | p. 6 (5.2. Quantitative Analysis) |
| 5.1. Experimental Setup | EMPIRICAL / SOURCE-REPORTED EVALUATION | Beyond improvements in standard evaluation metrics, our primary objective is to validate that our proposed energy formulation successfully resolves the ill-posedness inherent in sparse ... | p. 6 (5.1. Experimental Setup) |
| 5.5. Training Generalization Comparison | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our EnerGS consistently maintains a smaller train-test gap throughout training, indicating that our method encourages the model to learn multi-view consistent geometry rather than ... | p. 8 (5.5. Training Generalization Comparison) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 1. Accurate geometric priors can significantly improve Gaussian initialization and optimization (e.g., via point clouds from LiDAR). However, in large-scale outdoor scenes, such ... | p. 1 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 2. Visual Comparison on KITTI and Waymo Open Dataset. Our EnerGS achieves superior novel view synthesis, particularly in geometrically unobserved regions (e.g., upper ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 5.1. Experimental Setup - extractive body cue:** Our study focuses exclusively on static scenes, and consequently, the evaluation excludes all dynamic objects.
- **p. 6 / 5.3. Qualitative Results - extractive body cue:** 2 compares novel view synthesis results of state-ofthe-art baselines and our EnerGS across different scenes.
- **p. 7 / 5.3. Qualitative Results - extractive body cue:** Visual Comparison on KITTI and Waymo Open Dataset.
- **p. 7 / 5.3. Qualitative Results - extractive body cue:** Method KITTI Waymo Open Dataset Photometry Geometry #G (M)↓ Photometry Geometry #G (M)↓ PSNR↑SSIM↑Leak↓OccCov↑Margin↑Thick↓ PSNR↑SSIM↑Leak↓OccCov↑Margin↑Thick↓ 3DGS ToG 23 15.01 0.938 12.5 16.1 0.22 1.39 1.51 ...
- **p. 8 / 5.3. Qualitative Results - extractive body cue:** Ablation Study on KITTI and Waymo Open Dataset.
- **p. 8 / 5.3. Qualitative Results - extractive body cue:** Variant KITTI Waymo Open Dataset Photometry Geometry Photometry Geometry ∆PSNR↑∆SSIM↑∆Leak↓∆OccCov↑∆Margin↑∆Thick↓∆#G↓ ∆PSNR↑∆SSIM↑∆Leak↓∆OccCov↑∆Margin↑∆Thick↓∆#G↓ Full EnerGS 0.00 0.000 0.0 0.0 0.00 0.00 0.00 0.00 0.000 0.0 0.0 0.00 ...
- **p. 5 / 4.3. Optimization Stability - extractive body cue:** We analyze the smoothness of the optimization trajectory by examining the Lipschitz properties of the driving force.
- **p. 5 / 4.2. Exclusion of Degenerate Solutions - extractive body cue:** It must migrate along the trajectory defined by -∂dT ∂µ until exiting Ωfree, thereby ensuring Sdeg ∩Ωfree = ∅in the convergence limit.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Accurate geometric priors can significantly improve Gaussian initialization and optimization (e.g., via point clouds from LiDAR). However, in large-scale outdoor scenes, such priors ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Quantitative Comparison on KITTI and Waymo Open Dataset. We report Photometry (PSNR, SSIM), Geometry (Leak, OccCov, Margin, Thick), and Efficiency (#Gauss). Bold, underlined, ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 2. Visual Comparison on KITTI and Waymo Open Dataset. Our EnerGS achieves superior novel view synthesis, particularly in geometrically unobserved regions (e.g., upper structures ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. Ablation Study on KITTI and Waymo Open Dataset. All values report differences (∆) relative to the full EnerGS model. Positive ∆indicates an increase ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3. The Gap between Train and Test PSNR with Training Iteration. Our EnerGS consistently maintains a smaller train-test gap throughout training, indicating that our ...
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 4. Random Initialization Experiment. We randomly initialize 50,000 Gaussian primitives (with 500 of them tracked and recorded) in free space and optimize them using ...
- **p. 12 / Figure/Table caption - extractive body cue:** Figure 5. Comparison of Gradient Norm between Vanilla 3DGS and EnerGS. 12
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 6. Comparison of rendering results in LiDAR blind-spot regions (unobservable geometry), highlighting the effect of enabling the UNK field. B. Derivation and Interpretation of ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Our study focuses exclusively on static scenes, and consequently, the evaluation excludes all dynamic objects. | embodiment, simulator version and control stack | p. 6 (5.1. Experimental Setup), p. 6 (5.3. Qualitative Results) |
| Task/environment | 2 compares novel view synthesis results of state-ofthe-art baselines and our EnerGS across different scenes. | reset, timeout, object/scene variation | p. 6 (5.3. Qualitative Results), p. 7 (5.3. Qualitative Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 3 (3.2. Probabilistic Geometric Field) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3.4. Discrete Pruning as Boundary Enforcement), p. 3 (3.2. Probabilistic Geometric Field) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| On KITTI, it attains the highest PSNR and OccCov together with the lowest Leak score, indicating improved alignment with occupied regions and fewer free ... | definition/direction/unit from same section | p. 6 (5.2. Quantitative Analysis) |
| On Waymo, the advantages become more pronounced under partial observability, where our method achieves the best Leak and Margin scores and the highest PSNR, ... | definition/direction/unit from same section | p. 6 (5.2. Quantitative Analysis) |
| This visual evidence supports Theorem 1, confirming that the decoupled update rule effectively precludes the existence of stable degenerate solutions in Ωfree. | definition/direction/unit from same section | p. 7 (5.3. Qualitative Results) |
| Without Eocc or decoupled optimization, Gaussians no longer concentrate near the Occ-Free interface and instead disperse within Ωunk. | definition/direction/unit from same section | p. 8 (5.4. Ablation Studies) |
| Several ablation variants show reduced leakage ratios and increased margins while occupied coverage and surface alignment deteriorate. | definition/direction/unit from same section | p. 8 (5.4. Ablation Studies) |
| Table 6. Comparison with SplatAD. EnerGS improves performance when integrated into a LiDAR-prior-based pipeline, particularly on sparser datasets like KITTI. Dataset Method PSNR↑ SSIM↑ ... | definition/direction/unit from same section | p. 19 (Figure/Table caption) |
| Figure 1. Accurate geometric priors can significantly improve Gaussian initialization and optimization (e.g., via point clouds from LiDAR). However, in large-scale outdoor scenes, such ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| During training, the geometric regularization operates with linear complexity relative to the number of primitives N. | definition/direction/unit from same section | p. 4 (3.5. Complexity and Implementation Efficiency) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our method renders significantly finer details in these areas compared to baselines, aligning with our theoretical expectation that the adaptive energy field facilitates robust ... | comparison identity and matched condition | p. 7 (5.3. Qualitative Results) |
| Positive ∆indicates an increase compared to the baseline. | comparison identity and matched condition | p. 8 (5.3. Qualitative Results) |
| 2 compares novel view synthesis results of state-ofthe-art baselines and our EnerGS across different scenes. | comparison identity and matched condition | p. 6 (5.3. Qualitative Results) |
| 3 shows the generalization gap between Train and Test PSNR across different baseline methods. | comparison identity and matched condition | p. 8 (5.5. Training Generalization Comparison) |
| For a fair comparison, we initialize all methods with identical point clouds whenever applicable. | comparison identity and matched condition | p. 6 (5.1. Experimental Setup) |
| Visual Comparison on KITTI and Waymo Open Dataset. | comparison identity and matched condition | p. 7 (5.3. Qualitative Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Several ablation variants show reduced leakage ratios and increased margins while occupied coverage and surface alignment deteriorate. | component/input/data sensitivity | p. 8 (5.4. Ablation Studies) |
| Table 2. Ablation Study on KITTI and Waymo Open Dataset. All values report differences (∆) relative to the full EnerGS model. Positive ∆indicates an ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Finally, we demonstrate that the "Unknown" region naturally permits reconstruction driven by photometry, without requiring explicit heuristic switching. | component/input/data sensitivity | p. 5 (4.4. Permissiveness via Asymptotic Variance Analysis) |
| Our method renders significantly finer details in these areas compared to baselines, aligning with our theoretical expectation that the adaptive energy field facilitates robust ... | component/input/data sensitivity | p. 7 (5.3. Qualitative Results) |
| Figure 6. Comparison of rendering results in LiDAR blind-spot regions (unobservable geometry), highlighting the effect of enabling the UNK field. B. Derivation and Interpretation ... | component/input/data sensitivity | p. 13 (Figure/Table caption) |
| Table 3. Correspondence between paper components and code implementation. Paper Component Equation Implementation Occupied attraction Eocc Eq. (5) Listing 1, Line 2 Free space ... | component/input/data sensitivity | p. 17 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are summarized as follows: • We introduce an energy field that unifies uncertainaware occupancy attraction (via a Welsch M-estimator) and free space ... | On KITTI, it attains the highest PSNR and OccCov together with the lowest Leak score, indicating improved alignment with occupied regions and fewer free ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (5.2. Quantitative Analysis), p. 6 (5.1. Experimental Setup), p. 8 (5.5. Training Generalization Comparison), p. 1 (Figure/Table caption), p. 7 (Figure/Table caption), p. 19 (Figure/Table caption) |
| Primary metric/result | Beyond improvements in standard evaluation metrics, our primary objective is to validate that our proposed energy formulation successfully resolves the ill-posedness inherent in sparse ... | numeric claim only at cited anchor | p. 6 (5.1. Experimental Setup) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | It shows that degenerate solutions in free space cannot form stable equilibria and that the geometric update field is well-conditioned. | p. 8 (6. Conclusion) |
| body limitation/failure cue | Figure 1. Accurate geometric priors can significantly improve Gaussian initialization and optimization (e.g., via point clouds from LiDAR). However, in large-scale outdoor scenes, such ... | p. 1 (Figure/Table caption) |
| body limitation/failure cue | We first prove that degenerate solutions (floaters) cannot persist in the trusted free space, regardless of their photometric consistency. | p. 5 (4.2. Exclusion of Degenerate Solutions) |
| body limitation/failure cue | If µ lies within the trusted free space Ωfree ⊂Ωtrust, it cannot be a stable stationary point of the decoupled update rule, even if ... | p. 5 (4.2. Exclusion of Degenerate Solutions) |
| body limitation/failure cue | We conduct our evaluation on the KITTI [37] and Waymo Open Dataset [35], selecting sequences characterized by complex occlusions and unbounded backgrounds. | p. 6 (5.1. Experimental Setup) |
| body limitation/failure cue | This mathematically justifies the system's ability to reconstruct geometry in blind spots (e.g., occlusion or far-field) solely through multi-view consistency. | p. 6 (4.4. Permissiveness via Asymptotic Variance Analysis) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| This O(V 3) operation is performed once, avoiding expensive runtime differentiation and ensuring that complex geometric constraints are reduced to simple lookups. | p. 4 (3.5. Complexity and Implementation Efficiency) |
| In the initialization step, we compute the Euclidean Distance Transform [11] for the LiDAR point cloud and derive the gradient field ∇Egeom via central ... | p. 4 (3.5. Complexity and Implementation Efficiency) |
| All geometric metrics are computed with identical filtering and evaluation criteria across methods, ensuring that observed differences stem from reconstruction quality rather than evaluation ... | p. 6 (5.1. Experimental Setup) |
| The pixel color C(u) for a pixel u ∈R2 is computed via α-blending of K ordered primitives overlapping the pixel: C(u) = K X ... | p. 3 (3. Methodology) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6. Conclusion - extractive body cue:** It shows that degenerate solutions in free space cannot form stable equilibria and that the geometric update field is well-conditioned.
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Accurate geometric priors can significantly improve Gaussian initialization and optimization (e.g., via point clouds from LiDAR). However, in large-scale outdoor scenes, such priors ...
- **p. 5 / 4.2. Exclusion of Degenerate Solutions - extractive body cue:** We first prove that degenerate solutions (floaters) cannot persist in the trusted free space, regardless of their photometric consistency.
- **p. 5 / 4.2. Exclusion of Degenerate Solutions - extractive body cue:** If µ lies within the trusted free space Ωfree ⊂Ωtrust, it cannot be a stable stationary point of the decoupled update rule, even if µ ...
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** We conduct our evaluation on the KITTI [37] and Waymo Open Dataset [35], selecting sequences characterized by complex occlusions and unbounded backgrounds.
- **p. 6 / 4.4. Permissiveness via Asymptotic Variance Analysis - extractive body cue:** This mathematically justifies the system's ability to reconstruct geometry in blind spots (e.g., occlusion or far-field) solely through multi-view consistency.

- **Evidence anchors reviewed:** datasets p. 6 (5.1. Experimental Setup), p. 6 (5.3. Qualitative Results), p. 7 (5.3. Qualitative Results), p. 7 (5.3. Qualitative Results), p. 8 (5.3. Qualitative Results), p. 8 (5.3. Qualitative Results), metrics p. 6 (5.2. Quantitative Analysis), p. 6 (5.2. Quantitative Analysis), p. 7 (5.3. Qualitative Results), p. 8 (5.4. Ablation Studies), p. 8 (5.4. Ablation Studies), p. 19 (Figure/Table caption), baselines p. 7 (5.3. Qualitative Results), p. 8 (5.3. Qualitative Results), p. 6 (5.3. Qualitative Results), p. 8 (5.5. Training Generalization Comparison), p. 6 (5.1. Experimental Setup), p. 7 (5.3. Qualitative Results), results p. 6 (5.2. Quantitative Analysis), p. 6 (5.1. Experimental Setup), p. 8 (5.5. Training Generalization Comparison), p. 1 (Figure/Table caption), p. 7 (Figure/Table caption), p. 19 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
