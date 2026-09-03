# Evaluation - Distilling Unsigned Distance Function for Surface Reconstruction from 3D Gaussian Splatting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Li_Distilling_Unsigned_Distance_Function_for_Surface_Reconstruction_from_3D_Gaussian_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Distilling_Unsigned_Distance_Function_for_Surface_Reconstruction_from_3D_Gaussian_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.2. DF3D Dataset), p. 8 (4.2. DF3D Dataset), p. 8 (4.3. DTU Dataset), p. 6 (4.1. Experiment Settings)): Among UDF-based approaches, our model further achieves competitive runtime 4897

## Evaluation Body Digest

- **p. 8 / 4.3. DTU Dataset - extractive body cue:** We further evaluate our method on the DTU dataset [22], which contains 15 widely used multi-view scenes for surface reconstruction.
- **p. 5 / 4.1. Experiment Settings - extractive body cue:** We set the offset τ = 0.01 in DF3D dataset and τ = 0.02 in DTU dataset for the band B [29].
- **p. 6 / 4.1. Experiment Settings - extractive body cue:** Comparison of surface reconstruction accuracy across different methods on the DF3D [65] dataset, measured using Chamfer Distance (CD, ×10-3).
- **p. 7 / 4.2. DF3D Dataset - extractive body cue:** Each garment is captured from 72 high-resolution views at 1024 × 1024, making it a challenging benchmark for highfidelity surface reconstruction.
- **p. 7 / 4.2. DF3D Dataset - extractive body cue:** Following the standard evaluation protocol used in prior work (e.g., [21, 29, 61],etc), we evaluate our method on the DeepFashion3D (DF3D) dataset [65].
- **p. 8 / 4.3. DTU Dataset - extractive body cue:** Overall, the DTU results demonstrate that our render-aware UDF prior yields robust, stateof-the-art performance across diverse scenes, despite the inherent difficulty of unsigned distance learning.
- **p. 8 / 4.3. DTU Dataset - extractive body cue:** Compared to recent UDF-based competitors such as NeuralUDF [32], 2S-UDF [10], VRPrior [61], and GaussianUDF [29], our method also attains a lower mean error, indicating ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1. Overview. Given calibrated multi-view images, we jointly optimize a 3DGS and a student UDF us. For a local query point p and its ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiment (p. 5); 4.1. Experiment Settings (p. 5); 4.2. DF3D Dataset (p. 7); 4.3. DTU Dataset (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. DF3D Dataset | EMPIRICAL / SOURCE-REPORTED EVALUATION | Among UDF-based approaches, our model further achieves competitive runtime 4897 | p. 7 (4.2. DF3D Dataset) |
| 4.2. DF3D Dataset | EMPIRICAL / SOURCE-REPORTED EVALUATION | GaussianUDF [29], which couples a global UDF with 3D Gaussian Splatting, improves surface completeness over appearance-only methods but tends to oversmooth the geometry and ... | p. 8 (4.2. DF3D Dataset) |
| 4.3. DTU Dataset | EMPIRICAL / SOURCE-REPORTED EVALUATION | As shown in Table 2, our approach achieves the best average Chamfer Distance among all compared methods, including classical NeRF-style SDF baselines (NeuS [48]), ... | p. 8 (4.3. DTU Dataset) |
| 4.1. Experiment Settings | EMPIRICAL / SOURCE-REPORTED EVALUATION | Comparison of surface reconstruction accuracy across different methods on the DF3D [65] dataset, measured using Chamfer Distance (CD, ×10-3). | p. 6 (4.1. Experiment Settings) |

## Dataset / Benchmark Role

- **p. 8 / 4.3. DTU Dataset - extractive body cue:** We further evaluate our method on the DTU dataset [22], which contains 15 widely used multi-view scenes for surface reconstruction.
- **p. 5 / 4.1. Experiment Settings - extractive body cue:** We set the offset τ = 0.01 in DF3D dataset and τ = 0.02 in DTU dataset for the band B [29].
- **p. 6 / 4.1. Experiment Settings - extractive body cue:** Comparison of surface reconstruction accuracy across different methods on the DF3D [65] dataset, measured using Chamfer Distance (CD, ×10-3).
- **p. 7 / 4.2. DF3D Dataset - extractive body cue:** Each garment is captured from 72 high-resolution views at 1024 × 1024, making it a challenging benchmark for highfidelity surface reconstruction.
- **p. 7 / 4.2. DF3D Dataset - extractive body cue:** Following the standard evaluation protocol used in prior work (e.g., [21, 29, 61],etc), we evaluate our method on the DeepFashion3D (DF3D) dataset [65].
- **p. 8 / 4.3. DTU Dataset - extractive body cue:** Overall, the DTU results demonstrate that our render-aware UDF prior yields robust, stateof-the-art performance across diverse scenes, despite the inherent difficulty of unsigned distance learning.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1. Overview. Given calibrated multi-view images, we jointly optimize a 3DGS and a student UDF us. For a local query point p and its ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Comparison of surface reconstruction accuracy across different methods on the DF3D [65] dataset, measured using Chamfer Distance (CD, ×10-3). Lower values indicate better ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 2. Visual comparison with 2DGS [21], GaussianUDF [29], NeuralUDF [33], VRPrior [61] and ours on the DF3D [65] dataset. Baselines. We report the Chamfer ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Chamfer Distance (CD, ×10-3) comparison on the DTU dataset. Lower values indicate better reconstruction quality.
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Visual comparison with 2DGS [21], NeuralUDF [33], VRPrior [61] and ours on the DTU [51] dataset. Baseline +UDF distillation +Weighting Full Model Baseline ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Ablation study on the DTU [51]. report the numbers from the original papers [29, 32, 45, 61]. Our experiments follow [29] for surface ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Ablation studies on DTU dataset. Settings CD ↓ Baseline ✓ 0.99 + UDF distillation ✓

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We further evaluate our method on the DTU dataset [22], which contains 15 widely used multi-view scenes for surface reconstruction. | embodiment, simulator version and control stack | p. 8 (4.3. DTU Dataset), p. 5 (4.1. Experiment Settings) |
| Task/environment | We set the offset τ = 0.01 in DF3D dataset and τ = 0.02 in DTU dataset for the band B [29]. | reset, timeout, object/scene variation | p. 5 (4.1. Experiment Settings), p. 6 (4.1. Experiment Settings) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 3 (3. Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3. Method), p. 5 (3.5. Joint Optimization) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Comparison of surface reconstruction accuracy across different methods on the DF3D [65] dataset, measured using Chamfer Distance (CD, ×10-3). | definition/direction/unit from same section | p. 6 (4.1. Experiment Settings) |
| Compared to recent UDF-based competitors such as NeuralUDF [32], 2S-UDF [10], VRPrior [61], and GaussianUDF [29], our method also attains a lower mean error, ... | definition/direction/unit from same section | p. 8 (4.3. DTU Dataset) |
| Figure 1. Overview. Given calibrated multi-view images, we jointly optimize a 3DGS and a student UDF us. For a local query point p and ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Overall, the DTU results demonstrate that our render-aware UDF prior yields robust, stateof-the-art performance across diverse scenes, despite the inherent difficulty of unsigned distance ... | definition/direction/unit from same section | p. 8 (4.3. DTU Dataset) |
| The last layer uses an absolute value activation to enforce nonnegativity of the predicted unsigned distances. | definition/direction/unit from same section | p. 5 (4.1. Experiment Settings) |
| We train the UDF network with the Adam optimizer and an initial learning rate of 1 × 10-3, using a cosine learning rate decay ... | definition/direction/unit from same section | p. 5 (4.1. Experiment Settings) |
| Figure 2. Visual comparison with 2DGS [21], GaussianUDF [29], NeuralUDF [33], VRPrior [61] and ours on the DF3D [65] dataset. Baselines. We report the ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| Table 2. Chamfer Distance (CD, ×10-3) comparison on the DTU dataset. Lower values indicate better reconstruction quality. | definition/direction/unit from same section | p. 7 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As shown in Table 2, our approach achieves the best average Chamfer Distance among all compared methods, including classical NeRF-style SDF baselines (NeuS [48]), ... | comparison identity and matched condition | p. 8 (4.3. DTU Dataset) |
| As reported in Table 1, our method attains the best average Chamfer Distance across all garments when compared with baselines, including GOF [57], NeuralUDF ... | comparison identity and matched condition | p. 7 (4.2. DF3D Dataset) |
| Figure 2. Visual comparison with 2DGS [21], GaussianUDF [29], NeuralUDF [33], VRPrior [61] and ours on the DF3D [65] dataset. Baselines. We report the ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| Figure 3. Visual comparison with 2DGS [21], NeuralUDF [33], VRPrior [61] and ours on the DTU [51] dataset. Baseline +UDF distillation +Weighting Full Model ... | comparison identity and matched condition | p. 7 (Figure/Table caption) |
| Table 3. Ablation studies on DTU dataset. Settings CD ↓ Baseline ✓ 0.99 + UDF distillation ✓ | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| Comparison of surface reconstruction accuracy across different methods on the DF3D [65] dataset, measured using Chamfer Distance (CD, ×10-3). | comparison identity and matched condition | p. 6 (4.1. Experiment Settings) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 4. Ablation study on the DTU [51]. report the numbers from the original papers [29, 32, 45, 61]. Our experiments follow [29] for ... | component/input/data sensitivity | p. 7 (Figure/Table caption) |
| Table 3. Ablation studies on DTU dataset. Settings CD ↓ Baseline ✓ 0.99 + UDF distillation ✓ | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| As shown in Table 2, our approach achieves the best average Chamfer Distance among all compared methods, including classical NeRF-style SDF baselines (NeuS [48]), ... | component/input/data sensitivity | p. 8 (4.3. DTU Dataset) |
| Figure 1. Overview. Given calibrated multi-view images, we jointly optimize a 3DGS and a student UDF us. For a local query point p and ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The main contributions are as follows: • We propose a novel framework that learns UDF over Gaussian primitives by distilling a patch-based UDF predictor ... | Among UDF-based approaches, our model further achieves competitive runtime 4897 | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.2. DF3D Dataset), p. 8 (4.2. DF3D Dataset), p. 8 (4.3. DTU Dataset), p. 6 (4.1. Experiment Settings) |
| Primary metric/result | GaussianUDF [29], which couples a global UDF with 3D Gaussian Splatting, improves surface completeness over appearance-only methods but tends to oversmooth the geometry and ... | numeric claim only at cited anchor | p. 8 (4.2. DF3D Dataset) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Experiment Settings - extractive body cue:** All experiments are conducted on an NVIDIA RTX 3090 GPU.
- **p. 8 / 4.3. DTU Dataset - extractive body cue:** Compared to recent UDF-based competitors such as NeuralUDF [32], 2S-UDF [10], VRPrior [61], and GaussianUDF [29], our method also attains a lower mean error, indicating ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In future work, we plan to extend the framework to handle sparse setting and dynamic scenes and explore the integration of semantic priors to ... | p. 8 (5. Conclusion) |
| body limitation/failure cue | It is well known that learning unsigned distance functions (UDFs) is intrinsically more challenging than learning signed distance fields (SDFs), due to sign ambiguity ... | p. 8 (4.3. DTU Dataset) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We train the UDF network with the Adam optimizer and an initial learning rate of 1 × 10-3, using a cosine learning rate decay ... | p. 5 (4.1. Experiment Settings) |
| All experiments are conducted on an NVIDIA RTX 3090 GPU. | p. 5 (4.1. Experiment Settings) |
| The final pixel color C′(u, v) at location (u, v) is computed as: C′(u, v) = I X i=1 ciαipi(u, v) i-1 Y k=1 ... | p. 3 (3. Method) |
| Among UDF-based approaches, our model further achieves competitive runtime 4897 | p. 7 (4.2. DF3D Dataset) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive body cue:** In future work, we plan to extend the framework to handle sparse setting and dynamic scenes and explore the integration of semantic priors to further ...
- **p. 8 / 4.3. DTU Dataset - extractive body cue:** It is well known that learning unsigned distance functions (UDFs) is intrinsically more challenging than learning signed distance fields (SDFs), due to sign ambiguity and ...

- **Evidence anchors reviewed:** datasets p. 8 (4.3. DTU Dataset), p. 5 (4.1. Experiment Settings), p. 6 (4.1. Experiment Settings), p. 7 (4.2. DF3D Dataset), p. 7 (4.2. DF3D Dataset), p. 8 (4.3. DTU Dataset), metrics p. 6 (4.1. Experiment Settings), p. 8 (4.3. DTU Dataset), p. 4 (Figure/Table caption), p. 8 (4.3. DTU Dataset), p. 5 (4.1. Experiment Settings), p. 5 (4.1. Experiment Settings), baselines p. 8 (4.3. DTU Dataset), p. 7 (4.2. DF3D Dataset), p. 6 (Figure/Table caption), p. 7 (Figure/Table caption), p. 8 (Figure/Table caption), p. 6 (4.1. Experiment Settings), results p. 7 (4.2. DF3D Dataset), p. 8 (4.2. DF3D Dataset), p. 8 (4.3. DTU Dataset), p. 6 (4.1. Experiment Settings).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
