# Evaluation - DualSplat: Robust 3D Gaussian Splatting via Pseudo-Mask Bootstrapping from Reconstruction Failures

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Wang_DualSplat_Robust_3D_Gaussian_Splatting_via_Pseudo-Mask_Bootstrapping_from_Reconstruction_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_DualSplat_Robust_3D_Gaussian_Splatting_via_Pseudo-Mask_Bootstrapping_from_Reconstruction_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2. Distractor-free 3D Reconstruction), p. 1 (Figure/Table caption), p. 7 (4.2. Distractor-free 3D Reconstruction), p. 2 (4. We conduct comprehensive experiments on Robust), p. 6 (4.1. Setups), p. 7 (4.2. Distractor-free 3D Reconstruction)): DualSplat achieves the best overall average performance.

## Evaluation Body Digest

- **p. 5 / 4.1. Setups - extractive PDF cue:** These datasets contain diverse outdoor scenes with varying transient densities, enabling a comprehensive assessment of robustness and reconstruction quality.
- **p. 7 / 4.2. Distractor-free 3D Reconstruction - extractive PDF cue:** Qualitative results on Statue and Android from the RobustNeRF dataset. or distractor-induced artifacts in the highlighted regions, whereas DualSplat reconstructs cleaner background structures and preserves ...
- **p. 2 / 4. We conduct comprehensive experiments on Robust - extractive PDF cue:** NeRF and NeRF On-the-go, showing superior performance and robustness in transient-heavy scenes.
- **p. 5 / 4.1. Setups - extractive PDF cue:** We evaluated DualSplat on two standard datasets for transient-free reconstruction: RobustNeRF [23] and NeRF On-the-go [21].
- **p. 6 / 4.1. Setups - extractive PDF cue:** Comparison on NeRF On-the-go Dataset.
- **p. 6 / 4.1. Setups - extractive PDF cue:** Qualitative results on Spot and Mountain from the NeRF On-the-go dataset.
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** Unless otherwise stated, all experiments are performed on the NeRF On-thego dataset.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 6. Comparison of different feature extraction models. Methods Accuracy Precision Recall IoU Ours* 0.988

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. We conduct comprehensive experiments on Robust (p. 2); 4. Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Distractor-free 3D Reconstruction | EMPIRICAL / SOURCE-REPORTED EVALUATION | DualSplat achieves the best overall average performance. | p. 6 (4.2. Distractor-free 3D Reconstruction) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 1. Transient objects in the training images introduce noticeable artifacts in the reconstruction results. Compared with other methods, our approach achieves higher fidelity ... | p. 1 (Figure/Table caption) |
| 4.2. Distractor-free 3D Reconstruction | EMPIRICAL / SOURCE-REPORTED EVALUATION | Although the margins are modest and some individual scenes are still led by competing methods, our method remains consistently competitive across all five scenes ... | p. 7 (4.2. Distractor-free 3D Reconstruction) |
| 4. We conduct comprehensive experiments on Robust | EMPIRICAL / SOURCE-REPORTED EVALUATION | NeRF and NeRF On-the-go, showing superior performance and robustness in transient-heavy scenes. | p. 2 (4. We conduct comprehensive experiments on Robust) |
| 4.1. Setups | EMPIRICAL / SOURCE-REPORTED EVALUATION | Qualitative results on Spot and Mountain from the NeRF On-the-go dataset. | p. 6 (4.1. Setups) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Setups - extractive PDF cue:** These datasets contain diverse outdoor scenes with varying transient densities, enabling a comprehensive assessment of robustness and reconstruction quality.
- **p. 7 / 4.2. Distractor-free 3D Reconstruction - extractive PDF cue:** Qualitative results on Statue and Android from the RobustNeRF dataset. or distractor-induced artifacts in the highlighted regions, whereas DualSplat reconstructs cleaner background structures and preserves ...
- **p. 2 / 4. We conduct comprehensive experiments on Robust - extractive PDF cue:** NeRF and NeRF On-the-go, showing superior performance and robustness in transient-heavy scenes.
- **p. 5 / 4.1. Setups - extractive PDF cue:** We evaluated DualSplat on two standard datasets for transient-free reconstruction: RobustNeRF [23] and NeRF On-the-go [21].
- **p. 6 / 4.1. Setups - extractive PDF cue:** Comparison on NeRF On-the-go Dataset.
- **p. 6 / 4.1. Setups - extractive PDF cue:** Qualitative results on Spot and Mountain from the NeRF On-the-go dataset.
- **p. 7 / 4.3. Ablation Study - extractive PDF cue:** Unless otherwise stated, all experiments are performed on the NeRF On-thego dataset.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Transient objects in the training images introduce noticeable artifacts in the reconstruction results. Compared with other methods, our approach achieves higher fidelity and ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 2. We select three scenes from the NeRF On-the-go dataset to showcase incomplete fragments, where "high", "medium", and "low" denote the proportion of dynamic ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 2. These failure patterns can be explicitly mined as cues for transient discovery. Specifically, we first perform a conservative 3DGS reconstruction to expose failure ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Table 1. Comparison of paradigms and mechanisms. Item Online suppression methods Ours(DualSplat) Paradigm Online Heuristic (Internal) Failure-to-Prior (External Guidance) Dependency
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. DualSplat performs two-stage 3D Gaussian Splatting to suppress transient distractions. The first stage reconstructs a coarse static scene. After the first training, Mask ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 4. Visualization results using different pretrained mod- els as feature extractors. FiT3D, when used as the feature extrac- tor, produces the most distinct feature ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Comparison on NeRF On-the-go Dataset. For better visualization, the 1st , 2nd and 3rd best results are highlighted. Our method not only effectively ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 5. Qualitative results on Spot and Mountain from the NeRF On-the-go dataset.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | These datasets contain diverse outdoor scenes with varying transient densities, enabling a comprehensive assessment of robustness and reconstruction quality. | embodiment, simulator version and control stack | p. 5 (4.1. Setups), p. 7 (4.2. Distractor-free 3D Reconstruction) |
| Task/environment | Qualitative results on Statue and Android from the RobustNeRF dataset. or distractor-induced artifacts in the highlighted regions, whereas DualSplat reconstructs cleaner background structures and ... | reset, timeout, object/scene variation | p. 7 (4.2. Distractor-free 3D Reconstruction), p. 2 (4. We conduct comprehensive experiments on Robust) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3.2. Overview), p. 5 (3.4. Reconstruction Failures to Object-Level Priors) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 4 (3.2. Overview) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 6. Comparison of different feature extraction models. Methods Accuracy Precision Recall IoU Ours* 0.988 | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| Figure 4. Visualization results using different pretrained mod- els as feature extractors. FiT3D, when used as the feature extrac- tor, produces the most distinct ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |
| NeRF and NeRF On-the-go, showing superior performance and robustness in transient-heavy scenes. | definition/direction/unit from same section | p. 2 (4. We conduct comprehensive experiments on Robust) |
| These datasets contain diverse outdoor scenes with varying transient densities, enabling a comprehensive assessment of robustness and reconstruction quality. | definition/direction/unit from same section | p. 5 (4.1. Setups) |
| DualSplat achieves the best overall average performance. | definition/direction/unit from same section | p. 6 (4.2. Distractor-free 3D Reconstruction) |
| We set λlocal = 1.5, λrobust = 0.5, λprior = 1, Tdensify = 10,000, βrobustness = 10,000, and βprior = 10,000. | definition/direction/unit from same section | p. 6 (4.1. Setups) |
| Method Mean PSNR SSIM LPIPS base (3DGS) 19.043 0.697 0.196 base+PM 22.604 0.810 0.089 DD 20.820 0.764 0.145 DD+PM 22.899 0.818 0.090 DD+MLP w/o ... | definition/direction/unit from same section | p. 7 (4.3. Ablation Study) |
| Figure 1. Transient objects in the training images introduce noticeable artifacts in the reconstruction results. Compared with other methods, our approach achieves higher fidelity ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 4.2, we compare our method against 3DGSbased baselines using both quantitative metrics and qualitative visualizations. | comparison identity and matched condition | p. 5 (4.1. Setups) |
| On the Mountain and Spot scenes, several baselines either suffer from noticeable background blurring 4917 | comparison identity and matched condition | p. 6 (4.2. Distractor-free 3D Reconstruction) |
| Compared with vanilla 3DGS, the gain is substantial, confirming that transient-aware masking is essential for in-thewild 3DGS reconstruction. | comparison identity and matched condition | p. 6 (4.2. Distractor-free 3D Reconstruction) |
| We report averaged metrics with relative gains over vanilla 3DGS baseline. | comparison identity and matched condition | p. 7 (4.3. Ablation Study) |
| In the upper example, DualSplat recovers the background texture as well as other baselines. | comparison identity and matched condition | p. 7 (4.2. Distractor-free 3D Reconstruction) |
| Figure 1. Transient objects in the training images introduce noticeable artifacts in the reconstruction results. Compared with other methods, our approach achieves higher fidelity ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We additionally include a 3DGS [8] variant that directly applies the pseudo-masks without any additional refinement. | component/input/data sensitivity | p. 6 (4.1. Setups) |
| 4.3 presents ablation studies to validate the contribution of each core component in handling occlusions and improving overall reconstruction quality. | component/input/data sensitivity | p. 5 (4.1. Setups) |
| We further decompose DualSplat into three main components and perform controlled ablations: (i) Delayed Densification (DD) for 3DGS; (ii) pseudo-mask application (PM), which directly ... | component/input/data sensitivity | p. 7 (4.3. Ablation Study) |
| All ablations are retrained from the same initialization and schedule to ensure fair comparison. | component/input/data sensitivity | p. 7 (4.3. Ablation Study) |
| Figure 4. Visualization results using different pretrained mod- els as feature extractors. FiT3D, when used as the feature extrac- tor, produces the most distinct ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our method is built on a Failure-to-Prior principle: reconstruction failures caused by view-inconsistent transients are not merely artifacts to suppress, but signals that can ... | DualSplat achieves the best overall average performance. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2. Distractor-free 3D Reconstruction), p. 1 (Figure/Table caption), p. 7 (4.2. Distractor-free 3D Reconstruction), p. 2 (4. We conduct comprehensive experiments on Robust), p. 6 (4.1. Setups), p. 7 (4.2. Distractor-free 3D Reconstruction) |
| Primary metric/result | Figure 1. Transient objects in the training images introduce noticeable artifacts in the reconstruction results. Compared with other methods, our approach achieves higher fidelity ... | numeric claim only at cited anchor | p. 1 (Figure/Table caption) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | robust 3DGS that breaks the circular dependency between transient detection and scene reconstruction by converting first-pass reconstruction failures into explicit priors. | p. 2 (1. We propose a Failure-to-Prior paradigm for transient) |
| body limitation/failure cue | The primary objective of this step is to translate these firstpass failures into reliable object-level priors for the second reconstruction stage, rather than directly ... | p. 4 (3.4. Reconstruction Failures to Object-Level Priors) |
| body limitation/failure cue | Fig. 2. These failure patterns can be explicitly mined as cues for transient discovery. Specifically, we first perform a conservative 3DGS reconstruction to expose ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Table 1. Comparison of paradigms and mechanisms. Item Online suppression methods Ours(DualSplat) Paradigm Online Heuristic (Internal) Failure-to-Prior (External Guidance) Dependency | p. 3 (Figure/Table caption) |
| body limitation/failure cue | (15) The final MLP objective is LMLP = λrobustLrobust + λpriorLprior + Lreg. | p. 5 (3.4. Reconstruction Failures to Object-Level Priors) |
| body limitation/failure cue | These loss functions are combined as: Lrobust = exp  -max(0, Tdensify -t) βrobustness  (Lcos + Lres) . | p. 5 (3.4. Reconstruction Failures to Object-Level Priors) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| All parameters, including gaussian primitive parameters, are optimized with Adam using the default learning rates, while the MLP uses a learning rate of 1 ... | p. 6 (4.1. Setups) |
| We inherit RobustSplat's progressive MLP training schedule and other hyperparameters in Stage II unless otherwise stated. | p. 6 (4.1. Setups) |
| For an instance mask m with pixel set Ωm, we compute µm = 1 /Ωm/ X p∈Ωm ˆS(p), ¯ℓm = 1 /Ωm/ X p∈Ωm ... | p. 4 (3.4. Reconstruction Failures to Object-Level Priors) |
| Given the feature maps Fgt and Frender, we compute a pixel-wise cosine-similarity map S = cos(Fgt, Frender). | p. 4 (3.4. Reconstruction Failures to Object-Level Priors) |
| (14) Concretely, fi is the cached feature of the ground-truth training view, and f ′ i is computed from the current rendering during optimization. | p. 5 (3.4. Reconstruction Failures to Object-Level Priors) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / 1. We propose a Failure-to-Prior paradigm for transient - extractive PDF cue:** robust 3DGS that breaks the circular dependency between transient detection and scene reconstruction by converting first-pass reconstruction failures into explicit priors.
- **p. 4 / 3.4. Reconstruction Failures to Object-Level Priors - extractive PDF cue:** The primary objective of this step is to translate these firstpass failures into reliable object-level priors for the second reconstruction stage, rather than directly outputting ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Fig. 2. These failure patterns can be explicitly mined as cues for transient discovery. Specifically, we first perform a conservative 3DGS reconstruction to expose failure ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Table 1. Comparison of paradigms and mechanisms. Item Online suppression methods Ours(DualSplat) Paradigm Online Heuristic (Internal) Failure-to-Prior (External Guidance) Dependency
- **p. 5 / 3.4. Reconstruction Failures to Object-Level Priors - extractive PDF cue:** (15) The final MLP objective is LMLP = λrobustLrobust + λpriorLprior + Lreg.
- **p. 5 / 3.4. Reconstruction Failures to Object-Level Priors - extractive PDF cue:** These loss functions are combined as: Lrobust = exp  -max(0, Tdensify -t) βrobustness  (Lcos + Lres) .

- **PDF anchors reviewed:** datasets p. 5 (4.1. Setups), p. 7 (4.2. Distractor-free 3D Reconstruction), p. 2 (4. We conduct comprehensive experiments on Robust), p. 5 (4.1. Setups), p. 6 (4.1. Setups), p. 6 (4.1. Setups), metrics p. 8 (Figure/Table caption), p. 5 (Figure/Table caption), p. 2 (4. We conduct comprehensive experiments on Robust), p. 5 (4.1. Setups), p. 6 (4.2. Distractor-free 3D Reconstruction), p. 6 (4.1. Setups), baselines p. 5 (4.1. Setups), p. 6 (4.2. Distractor-free 3D Reconstruction), p. 6 (4.2. Distractor-free 3D Reconstruction), p. 7 (4.3. Ablation Study), p. 7 (4.2. Distractor-free 3D Reconstruction), p. 1 (Figure/Table caption), results p. 6 (4.2. Distractor-free 3D Reconstruction), p. 1 (Figure/Table caption), p. 7 (4.2. Distractor-free 3D Reconstruction), p. 2 (4. We conduct comprehensive experiments on Robust), p. 6 (4.1. Setups), p. 7 (4.2. Distractor-free 3D Reconstruction).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
