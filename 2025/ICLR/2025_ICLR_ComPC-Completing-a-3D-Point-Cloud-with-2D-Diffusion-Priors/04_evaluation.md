# Evaluation - ComPC: Completing a 3D Point Cloud with 2D Diffusion Priors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=SoUwcVplq4; PDF retrieval source: https://openreview.net/pdf/07e0e163b5ab2a3918ebbccd045080a0decea42e.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 10 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 16 (A.7 EVALUATION ON MULTI-MODAL METRICS), p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS)): The results demonstrate that the Preservation Constraint improves performance compared to standard view-dependent diffusion guidance.

## Evaluation Body Digest

- **p. 19 / A.10 EVALUATION ON LIDAR POINTS - extractive PDF cue:** Published as a conference paper at ICLR 2025 Table 12: Quantitative comparison on ShapeNet dataset. "Known category" and "Unknown category" denote categories included and not ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** By introducing abundant priors from 2D diffusion model (Liu et al., 2023), our method can achieve robust completion for objects across different datasets.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Existing fully-supervised methods may perform inferior even on the in-domain objects as illustrated in Table 2, which reveals their limitation on datasets differing from the ...
- **p. 19 / A.10 EVALUATION ON LIDAR POINTS - extractive PDF cue:** AdaPoinTr SVDFormer PoinTr PointAttN Ours Input GT Figure 16: Qualitative comparison on objects from ShapeNet (Chang et al., 2015) dataset.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** As SDS-complete (Kasten et al., 2024) only provides codes for the processing of the Redwood dataset (Choi et al., 2016), we implement corresponding comparisons on ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Considering the impracticality of applying test-time completion methods (Kasten et al., 2024) to benchmarks such as Completion3D (Tchapmi et al., 2019) or ShapeNet (Chang et ...
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** We evaluated our method on both Redwood and synthetic datasets.
- **p. 16 / A.9 EVALUATION ON SHAPENET - extractive PDF cue:** In this section, we further compare our methods with network-based methods on 16 common models from 4 different categories of ShapeNet dataset.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 8); A.7 EVALUATION ON MULTI-MODAL METRICS (p. 16); A.9 EVALUATION ON SHAPENET (p. 16); A.10 EVALUATION ON LIDAR POINTS (p. 17).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results demonstrate that the Preservation Constraint improves performance compared to standard view-dependent diffusion guidance. | p. 10 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results show that the normal map consistently outperforms other methods. | p. 9 (4 EXPERIMENTS) |
| A.7 EVALUATION ON MULTI-MODAL METRICS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our method achieves superior performance on UHD and MMD metrics, further validating its effectiveness for 3D point cloud completion. | p. 16 (A.7 EVALUATION ON MULTI-MODAL METRICS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | 7, these alternative strategies are clearly outperformed by the normal map composed of normal vectors, particularly in the circled areas. | p. 9 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | The quantitative and qualitative results are presented in Table 1 and Fig. | p. 8 (4 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 19 / A.10 EVALUATION ON LIDAR POINTS - extractive PDF cue:** Published as a conference paper at ICLR 2025 Table 12: Quantitative comparison on ShapeNet dataset. "Known category" and "Unknown category" denote categories included and not ...
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** By introducing abundant priors from 2D diffusion model (Liu et al., 2023), our method can achieve robust completion for objects across different datasets.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Existing fully-supervised methods may perform inferior even on the in-domain objects as illustrated in Table 2, which reveals their limitation on datasets differing from the ...
- **p. 19 / A.10 EVALUATION ON LIDAR POINTS - extractive PDF cue:** AdaPoinTr SVDFormer PoinTr PointAttN Ours Input GT Figure 16: Qualitative comparison on objects from ShapeNet (Chang et al., 2015) dataset.
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** As SDS-complete (Kasten et al., 2024) only provides codes for the processing of the Redwood dataset (Choi et al., 2016), we implement corresponding comparisons on ...
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** Considering the impracticality of applying test-time completion methods (Kasten et al., 2024) to benchmarks such as Completion3D (Tchapmi et al., 2019) or ShapeNet (Chang et ...
- **p. 10 / 4 EXPERIMENTS - extractive PDF cue:** We evaluated our method on both Redwood and synthetic datasets.
- **p. 16 / A.9 EVALUATION ON SHAPENET - extractive PDF cue:** In this section, we further compare our methods with network-based methods on 16 common models from 4 different categories of ShapeNet dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Different point cloud completion methods. (a) Existing network-based completion methods; (b) Test-time SDS-complete (Kasten et al., 2024) with text prompts to guide Neural ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Illustration of our framework. ①In Partial Gaussian Initialization (PGI), Reference Viewpoint Estimation estimates a camera pose Vp where Pin can be most completely ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3: Differences between our binarized opacity and original continuous opacity. ≺denotes smaller but not approaching. Gaussian Attributes Setting. Upon estimating the reference camera pose ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4: Illustration of Grid Pulling module. g(·) is a MLP-based SDF learned from the completed point cloud Psurf. Merge denotes merge layer from (Huang ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5: Qualitative comparison on synthetic data.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: Quantitative comparison on synthetic data. Bold marks the best results. Object Horse MaxPlanck Armadillo Cow Homer Teapot Bunny
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 6: Qualitative comparison on Redwood dataset (Choi et al., 2016; Kasten et al., 2024).
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Quantitative comparison on Redwood dataset (Choi et al., 2016; Kasten et al., 2024). For the convenience, we re-optimize and normalize the results of ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Published as a conference paper at ICLR 2025 Table 12: Quantitative comparison on ShapeNet dataset. "Known category" and "Unknown category" denote categories included and ... | embodiment, simulator version and control stack | p. 19 (A.10 EVALUATION ON LIDAR POINTS), p. 9 (4 EXPERIMENTS) |
| Task/environment | By introducing abundant priors from 2D diffusion model (Liu et al., 2023), our method can achieve robust completion for objects across different datasets. | reset, timeout, object/scene variation | p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 2 (1 INTRODUCTION), p. 4 (3 METHODOLOGY) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 4 (3 METHODOLOGY), p. 5 (3 METHODOLOGY) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 4.3 ABLATION STUDY FOR COLORIZATION STRATEGIES IN PGI To confirm the necessity of using normal map for colorization in Partial Gaussian Initialization, we compare ... | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| In contrast, the final Grid Pulling (GP) module acquire more uniform surface points, leading to better EMD performance, although the CD metric experiences a ... | definition/direction/unit from same section | p. 10 (4 EXPERIMENTS) |
| 7, these alternative strategies are clearly outperformed by the normal map composed of normal vectors, particularly in the circled areas. | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| The results demonstrate that the Preservation Constraint improves performance compared to standard view-dependent diffusion guidance. | definition/direction/unit from same section | p. 10 (4 EXPERIMENTS) |
| Our method achieves superior performance on UHD and MMD metrics, further validating its effectiveness for 3D point cloud completion. | definition/direction/unit from same section | p. 16 (A.7 EVALUATION ON MULTI-MODAL METRICS) |
| Notably, our method demonstrates the ability for reasonable completion even with LiDAR-derived point clouds. | definition/direction/unit from same section | p. 17 (A.10 EVALUATION ON LIDAR POINTS) |
| Std denotes the Standard deviation of added noises. | definition/direction/unit from same section | p. 17 (A.9 EVALUATION ON SHAPENET) |
| Figure 1: Different point cloud completion methods. (a) Existing network-based completion methods; (b) Test-time SDS-complete (Kasten et al., 2024) with text prompts to guide ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We compare our approach with state-of-the-art supervised methods including PointAttN(Wang et al., 2024), PoinTr (Yu et al., 2021), SVDFormer (Zhu et al., 2023), AdaPoinTr ... | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| The results show that the normal map consistently outperforms other methods. | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| 7, these alternative strategies are clearly outperformed by the normal map composed of normal vectors, particularly in the circled areas. | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| The results demonstrate that the Preservation Constraint improves performance compared to standard view-dependent diffusion guidance. | comparison identity and matched condition | p. 10 (4 EXPERIMENTS) |
| All metrics are multiplied by 102 in subsequent comparisons. | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| More detailed ablation study can be found in the appendix A. | comparison identity and matched condition | p. 10 (4 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We also provide quantitative ablation study for our proposed components in Table 4. | component/input/data sensitivity | p. 10 (4 EXPERIMENTS) |
| 5 without any prompts and related geometries. | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| Depth Coordinates Normal(Ours) CD 2.25 2.01 1.96 EMD 2.88 2.64 2.60 Table 4: Ablation for ZFC and PCE. | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| More detailed ablation study can be found in the appendix A. | component/input/data sensitivity | p. 10 (4 EXPERIMENTS) |
| Figure 9: Ablation study for Grid Pulling module. Far, Near, and Merge denote the Lfar, Lnear, and merge layer gm(·), respectively. Vanilla Gaussian + ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| Table 5: The setting of mentioned hyper-parameters in Sec. 3. Hyper-parameters w0 ∼w3 1e-3, 1e3, 1e2, 0.1 δ, σ0, σn 0.01, 0.005, 0.05 Iterations ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our main contributions can be summarized as below: • We propose the Partial Gaussian Initialization to generate a reference image for partial points, which ... | The results demonstrate that the Preservation Constraint improves performance compared to standard view-dependent diffusion guidance. | PDF body cue; verify exact table/figure and matched conditions | p. 10 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 16 (A.7 EVALUATION ON MULTI-MODAL METRICS), p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS) |
| Primary metric/result | The results show that the normal map consistently outperforms other methods. | numeric claim only at cited anchor | p. 9 (4 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 8 / 4 EXPERIMENTS - extractive PDF cue:** We standardize point clouds and perform comparisons at a resolution of 16,384 points following PCN (Yuan et al., 2018).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | LIMITATION Our method shares similar limitations as claimed by SDS-complete (Kasten et al., 2024). | p. 10 (5 CONCLUSION) |
| body limitation/failure cue | Figure 12: Some failure cases. AdaPoinTr SVDFormer Ours Input GT 0.0 0.001 | p. 17 (Figure/Table caption) |
| body limitation/failure cue | Published as a conference paper at ICLR 2025 Output Ground Truth Partial Reference Image Figure 12: Some failure cases. | p. 17 (A.9 EVALUATION ON SHAPENET) |
| body limitation/failure cue | As a test-time completion method, although our method does not require any training, the optimization on the test data would take relatively long time ... | p. 10 (5 CONCLUSION) |
| body limitation/failure cue | We will explore it in our future work. | p. 15 (A.4 FAILURE CASES) |
| body limitation/failure cue | Existing fully-supervised methods may perform inferior even on the in-domain objects as illustrated in Table 2, which reveals their limitation on datasets differing from ... | p. 9 (4 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| As SDS-complete (Kasten et al., 2024) only provides codes for the processing of the Redwood dataset (Choi et al., 2016), we implement corresponding comparisons ... | p. 8 (4 EXPERIMENTS) |
| We compare our approach with state-of-the-art supervised methods including PointAttN(Wang et al., 2024), PoinTr (Yu et al., 2021), SVDFormer (Zhu et al., 2023), AdaPoinTr ... | p. 8 (4 EXPERIMENTS) |
| PoinTr Seedformer PointAttN SVDFormer ShapeFormer AdaPoinTr Ours Level CD/EMD CD/EMD CD/EMD CD/EMD CD/EMD CD/EMD CD/EMD 1 3.77/5.13 4.16/6.02 5.52/6.29 4.63/5.08 3.30/4.07 5.33/5.82 1.86/2.01 3 ... | p. 18 (A.10 EVALUATION ON LIDAR POINTS) |
| Known category Unknown category Categories Chair Table Pistol Tower Metrics CD/EMD CD/EMD CD/EMD CD/EMD PoinTr 1.31/2.64 0.74/2.86 1.84/3.84 2.38/3.05 SeedFormer 1.39/2.77 0.80/2.17 1.79/3.91 1.95/3.24 ... | p. 19 (A.10 EVALUATION ON LIDAR POINTS) |
| Additionally, it incorporates a Preservation Constraint computed with respect to Vp. | p. 4 (3 METHODOLOGY) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 5 CONCLUSION - extractive PDF cue:** LIMITATION Our method shares similar limitations as claimed by SDS-complete (Kasten et al., 2024).
- **p. 17 / Figure/Table caption - extractive PDF cue:** Figure 12: Some failure cases. AdaPoinTr SVDFormer Ours Input GT 0.0 0.001
- **p. 17 / A.9 EVALUATION ON SHAPENET - extractive PDF cue:** Published as a conference paper at ICLR 2025 Output Ground Truth Partial Reference Image Figure 12: Some failure cases.
- **p. 10 / 5 CONCLUSION - extractive PDF cue:** As a test-time completion method, although our method does not require any training, the optimization on the test data would take relatively long time cost.
- **p. 15 / A.4 FAILURE CASES - extractive PDF cue:** We will explore it in our future work.
- **p. 9 / 4 EXPERIMENTS - extractive PDF cue:** Existing fully-supervised methods may perform inferior even on the in-domain objects as illustrated in Table 2, which reveals their limitation on datasets differing from the ...

- **PDF anchors reviewed:** datasets p. 19 (A.10 EVALUATION ON LIDAR POINTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 19 (A.10 EVALUATION ON LIDAR POINTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), metrics p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 16 (A.7 EVALUATION ON MULTI-MODAL METRICS), p. 17 (A.10 EVALUATION ON LIDAR POINTS), baselines p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), results p. 10 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 16 (A.7 EVALUATION ON MULTI-MODAL METRICS), p. 9 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
