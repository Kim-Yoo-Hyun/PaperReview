# Evaluation - Diffusion 3D Features (Diff3F): Decorating Untextured Shapes with Distilled Semantic Features

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Dutt_Diffusion_3D_Features_Diff3F_Decorating_Untextured_Shapes_with_Distilled_Semantic_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Dutt_Diffusion_3D_Features_Diff3F_Decorating_Untextured_Shapes_with_Distilled_Semantic_CVPR_2024_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.4. Evaluation on Human Shapes), p. 7 (4.4. Evaluation on Human Shapes), p. 6 (4.1. Datasets and Benchmarks), p. 1 (Figure/Table caption), p. 8 (4.6. Ablations), p. 5 (Figure/Table caption)): Our method achieves a state-of-theart correspondence accuracy of 26.41% at 1% error tolerance, an improvement of 5%.

## Evaluation Body Digest

- **p. 6 / 4.1. Datasets and Benchmarks - extractive PDF cue:** For DPC and SE-ORNet, we choose SURREAL and SMAL as the training sets for human and animal shapes, respectively - these larger datasets lead to ...
- **p. 6 / 4.1. Datasets and Benchmarks - extractive PDF cue:** We also evaluate our method on the FAUST benchmark [8].
- **p. 7 / 4.4. Evaluation on Human Shapes - extractive PDF cue:** We present results on the SHREC'19 dataset.
- **p. 7 / 4.4. Evaluation on Human Shapes - extractive PDF cue:** We choose baseline methods trained on SURREAL as it is a significantly larger dataset (consisting of human shapes) than SHREC'19, leading to improved performance.
- **p. 8 / 4.6. Ablations - extractive PDF cue:** Although our complete approach produces the second-best score in every category, incorporating all of our parts together (including fusion with DINO) resulted in the best ...
- **p. 6 / 4.2. Evaluation Metrics - extractive PDF cue:** The correspondence accuracy is measured as the fraction of correct correspondences within a threshold tolerance distance: acc( \ e p s ilon ) = \fr ...
- **p. 6 / 4.2. Evaluation Metrics - extractive PDF cue:** We use the average correspondence error and the correspondence accuracy as our evaluation criteria.
- **p. 7 / 4.4. Evaluation on Human Shapes - extractive PDF cue:** Our method achieves a state-of-theart correspondence accuracy of 26.41% at 1% error tolerance, an improvement of 5%.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4. Evaluation (p. 6); 4.1. Datasets and Benchmarks (p. 6); 4.2. Evaluation Metrics (p. 6); 4.4. Evaluation on Human Shapes (p. 7); 4.5. Evaluation on Animal Shapes (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.4. Evaluation on Human Shapes | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our method achieves a state-of-theart correspondence accuracy of 26.41% at 1% error tolerance, an improvement of 5%. | p. 7 (4.4. Evaluation on Human Shapes) |
| 4.4. Evaluation on Human Shapes | EMPIRICAL / SOURCE-REPORTED EVALUATION | We choose baseline methods trained on SURREAL as it is a significantly larger dataset (consisting of human shapes) than SHREC'19, leading to improved performance. | p. 7 (4.4. Evaluation on Human Shapes) |
| 4.1. Datasets and Benchmarks | EMPIRICAL / SOURCE-REPORTED EVALUATION | For DPC and SE-ORNet, we choose SURREAL and SMAL as the training sets for human and animal shapes, respectively - these larger datasets lead ... | p. 6 (4.1. Datasets and Benchmarks) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 1. Correspondence in-the-wild. We introduce DIFF3F, a novel feature distiller that harnesses the expressive power of in- painting diffusion features and distills them ... | p. 1 (Figure/Table caption) |
| 4.6. Ablations | EMPIRICAL / SOURCE-REPORTED EVALUATION | Although our complete approach produces the second-best score in every category, incorporating all of our parts together (including fusion with DINO) resulted in the ... | p. 8 (4.6. Ablations) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Datasets and Benchmarks - extractive PDF cue:** For DPC and SE-ORNet, we choose SURREAL and SMAL as the training sets for human and animal shapes, respectively - these larger datasets lead to ...
- **p. 6 / 4.1. Datasets and Benchmarks - extractive PDF cue:** We also evaluate our method on the FAUST benchmark [8].
- **p. 7 / 4.4. Evaluation on Human Shapes - extractive PDF cue:** We present results on the SHREC'19 dataset.
- **p. 7 / 4.4. Evaluation on Human Shapes - extractive PDF cue:** We choose baseline methods trained on SURREAL as it is a significantly larger dataset (consisting of human shapes) than SHREC'19, leading to improved performance.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Correspondence in-the-wild. We introduce DIFF3F, a novel feature distiller that harnesses the expressive power of in- painting diffusion features and distills them to ...
- **p. 2 / Figure/Table caption - extractive PDF cue:** Table 1. Comparison of DIFFUSION 3D FEATURES to related methods. Unlike traditional geometric feature detectors (e.g., WKS), modern learning-based approaches require training and can struggle ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Method overview. DIFF3F is a feature distiller to map semantic diffusion features to 3D surface points. We render the given shape without textures ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Results gallery. DIFF3F's performance on various point correspondence challenges. Corresponding points are similarly colored. Note that DIFF3F can successfully distinguish between symmetric parts ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Comparison. We report correspondence accuracy within 1% error tolerance, with our method against competing works. The Laplace Beltrami Operator (LBO) computation for Functional ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 3. Generalization. We compare generalization capabilities of DIFF3F vs others by training on one dataset and testing on a different set. For DPC and ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. Comparisons. We compare our DIFF3F (bottom) against SOTA methods (i.e., DPC [30] and SE-ORNet [14]) for the task of point-to-point shape correspondence. Corresponding ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Ablation. We ablate different components of our method and compare accuracy at 1% tolerance on SHREC'19 and SHREC'20, against our full method (last ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | For DPC and SE-ORNet, we choose SURREAL and SMAL as the training sets for human and animal shapes, respectively - these larger datasets lead ... | embodiment, simulator version and control stack | p. 6 (4.1. Datasets and Benchmarks), p. 6 (4.1. Datasets and Benchmarks) |
| Task/environment | We also evaluate our method on the FAUST benchmark [8]. | reset, timeout, object/scene variation | p. 6 (4.1. Datasets and Benchmarks), p. 7 (4.4. Evaluation on Human Shapes) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 4 (3.2. Semantics through Painting), p. 4 (3.1. Semantic Diffusion Features) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 5 (3.3. Distilling 2D Features to 3D), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Although our complete approach produces the second-best score in every category, incorporating all of our parts together (including fusion with DINO) resulted in the ... | definition/direction/unit from same section | p. 8 (4.6. Ablations) |
| The correspondence accuracy is measured as the fraction of correct correspondences within a threshold tolerance distance: acc( \ e p s ilon ) = ... | definition/direction/unit from same section | p. 6 (4.2. Evaluation Metrics) |
| We use the average correspondence error and the correspondence accuracy as our evaluation criteria. | definition/direction/unit from same section | p. 6 (4.2. Evaluation Metrics) |
| Our method achieves a state-of-theart correspondence accuracy of 26.41% at 1% error tolerance, an improvement of 5%. | definition/direction/unit from same section | p. 7 (4.4. Evaluation on Human Shapes) |
| We find that adding realistic texture, as opposed to only shading, results in a significant improvement in terms of accuracy and reducing errors. | definition/direction/unit from same section | p. 7 (4.6. Ablations) |
| We ablate different components of our method and compare accuracy at 1% tolerance on SHREC'19 and SHREC'20, against our full method (last row). | definition/direction/unit from same section | p. 8 (4.6. Ablations) |
| Figure 2. Method overview. DIFF3F is a feature distiller to map semantic diffusion features to 3D surface points. We render the given shape without ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 3. Results gallery. DIFF3F's performance on various point correspondence challenges. Corresponding points are similarly colored. Note that DIFF3F can successfully distinguish between symmetric ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We outperform baseline methods by a large margin for non-isometric shapes thanks to the semantic nature of DIFF3F. | comparison identity and matched condition | p. 7 (4.5. Evaluation on Animal Shapes) |
| Our method achieves the highest correspondence accuracy compared to existing works and the lowest average correspondence error compared to baseline methods, as seen in ... | comparison identity and matched condition | p. 7 (4.4. Evaluation on Human Shapes) |
| In comparison, our method requires no training, enabling zero-shot feature extraction. | comparison identity and matched condition | p. 6 (4.3. Baseline Methods) |
| To make a fair comparison with existing works, we follow a similar experiment setup described in DPC [30] and SE-ORNet [14]. | comparison identity and matched condition | p. 6 (4.1. Datasets and Benchmarks) |
| Ablation SHREC'19 SHREC'20 acc ↑ err ↓ acc ↑ err ↓ w/o ControlNet (untextured) 17.20 2.04 65.48 0.69 TEXTure[46]+DINO 17.20 2.04 65.48 0.69 w/o ... | comparison identity and matched condition | p. 8 (4.6. Ablations) |
| Figure 1. Correspondence in-the-wild. We introduce DIFF3F, a novel feature distiller that harnesses the expressive power of in- painting diffusion features and distills them ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 1. Correspondence in-the-wild. We introduce DIFF3F, a novel feature distiller that harnesses the expressive power of in- painting diffusion features and distills them ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| Ablation SHREC'19 SHREC'20 acc ↑ err ↓ acc ↑ err ↓ w/o ControlNet (untextured) 17.20 2.04 65.48 0.69 TEXTure[46]+DINO 17.20 2.04 65.48 0.69 w/o ... | component/input/data sensitivity | p. 8 (4.6. Ablations) |
| Table 4. Ablation. We ablate different components of our method and compare accuracy at 1% tolerance on SHREC'19 and SHREC'20, against our full method ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Figure 2. Method overview. DIFF3F is a feature distiller to map semantic diffusion features to 3D surface points. We render the given shape without ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| Note that we do not have access to pretrained 3D-CODED models for animal models. | component/input/data sensitivity | p. 6 (4.3. Baseline Methods) |
| Train Method TOSCA SHREC'19 SHREC'20 acc ↑ err ↓ acc ↑ err ↓ acc ↑ err ↓ SURREAL DPC [30] 29.30 5.25 17.40 6.26 ... | component/input/data sensitivity | p. 6 (4.1. Datasets and Benchmarks) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| We propose a simple and robust solution. | Our method achieves a state-of-theart correspondence accuracy of 26.41% at 1% error tolerance, an improvement of 5%. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.4. Evaluation on Human Shapes), p. 7 (4.4. Evaluation on Human Shapes), p. 6 (4.1. Datasets and Benchmarks), p. 1 (Figure/Table caption), p. 8 (4.6. Ablations), p. 5 (Figure/Table caption) |
| Primary metric/result | We choose baseline methods trained on SURREAL as it is a significantly larger dataset (consisting of human shapes) than SHREC'19, leading to improved performance. | numeric claim only at cited anchor | p. 7 (4.4. Evaluation on Human Shapes) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Datasets and Benchmarks - extractive PDF cue:** TOSCA comprises of 80 objects representing a mixture of animals and humans, formed by deforming template meshes.
- **p. 7 / 4.5. Evaluation on Animal Shapes - extractive PDF cue:** While the evaluation is on a subset of only about 50 points as the number of annotated points is very limited, we show dense correspondence ...
- **p. 5 / 3.3. Distilling 2D Features to 3D - extractive PDF cue:** Moreover, we render the 3D shape from several views (n = 100), which further stabilizes the aggregation, resulting in descriptors that mostly capture semantic meaning: ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Since our method relies on multi-view images, DIFF3F fails to produce features on parts of the shapes that are invisible from all the sampled ... | p. 8 (6. Conclusion) |
| body limitation/failure cue | Further, since we aggregate (diffusion) features from image diffusion models, we inherit their limitations in terms of suffering from bias in the dataset and/or ... | p. 8 (6. Conclusion) |
| body limitation/failure cue | Table 2. Comparison. We report correspondence accuracy within 1% error tolerance, with our method against competing works. The Laplace Beltrami Operator (LBO) computation for ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | Results using 3D-CODED are particularly poor on TOSCA mainly for two reasons: (i) It needs a much larger dataset with ground truth annotations, which ... | p. 7 (4.5. Evaluation on Animal Shapes) |
| body limitation/failure cue | Figure 3. Results gallery. DIFF3F's performance on various point correspondence challenges. Corresponding points are similarly colored. Note that DIFF3F can successfully distinguish between symmetric ... | p. 5 (Figure/Table caption) |
| body limitation/failure cue | Additionally, varied textured renderings enable a more robust feature aggregation due to the implicit denoising of unnecessary feature dimensions 4500 | p. 7 (4.6. Ablations) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Results using 3D-CODED are particularly poor on TOSCA mainly for two reasons: (i) It needs a much larger dataset with ground truth annotations, which ... | p. 7 (4.5. Evaluation on Animal Shapes) |
| Note that we do not have access to pretrained 3D-CODED models for animal models. | p. 6 (4.3. Baseline Methods) |
| We compute correspondence on the annotated correspondences per pair (approximately 50). | p. 6 (4.1. Datasets and Benchmarks) |
| Corresponding points, computed as described in Section 3.4, are similarly colored. | p. 7 (4.4. Evaluation on Human Shapes) |
| We use DDIM [51] to accelerate the sampling process for Stable Diffusion [47] and use 30 inference steps. | p. 4 (3.2. Semantics through Painting) |
| (4) During this texturing forward pass, we extract features Ft L from an intermediate layer L of Stable Diffusion's UNet decoder at diffusion time ... | p. 4 (3.2. Semantics through Painting) |
| Next, we describe how to use these descriptors to compute correspondences between pairs of shapes. | p. 5 (3.3. Distilling 2D Features to 3D) |
| Each pixel gets a 1280 dimensional feature from the diffusion UNet, aggregated over diffusion time steps. | p. 5 (3.2. Semantics through Painting) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6. Conclusion - extractive PDF cue:** Since our method relies on multi-view images, DIFF3F fails to produce features on parts of the shapes that are invisible from all the sampled views ...
- **p. 8 / 6. Conclusion - extractive PDF cue:** Further, since we aggregate (diffusion) features from image diffusion models, we inherit their limitations in terms of suffering from bias in the dataset and/or view ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Comparison. We report correspondence accuracy within 1% error tolerance, with our method against competing works. The Laplace Beltrami Operator (LBO) computation for Functional ...
- **p. 7 / 4.5. Evaluation on Animal Shapes - extractive PDF cue:** Results using 3D-CODED are particularly poor on TOSCA mainly for two reasons: (i) It needs a much larger dataset with ground truth annotations, which is ...
- **p. 5 / Figure/Table caption - extractive PDF cue:** Figure 3. Results gallery. DIFF3F's performance on various point correspondence challenges. Corresponding points are similarly colored. Note that DIFF3F can successfully distinguish between symmetric parts ...
- **p. 7 / 4.6. Ablations - extractive PDF cue:** Additionally, varied textured renderings enable a more robust feature aggregation due to the implicit denoising of unnecessary feature dimensions 4500

- **PDF anchors reviewed:** datasets p. 6 (4.1. Datasets and Benchmarks), p. 6 (4.1. Datasets and Benchmarks), p. 7 (4.4. Evaluation on Human Shapes), p. 7 (4.4. Evaluation on Human Shapes), metrics p. 8 (4.6. Ablations), p. 6 (4.2. Evaluation Metrics), p. 6 (4.2. Evaluation Metrics), p. 7 (4.4. Evaluation on Human Shapes), p. 7 (4.6. Ablations), p. 8 (4.6. Ablations), baselines p. 7 (4.5. Evaluation on Animal Shapes), p. 7 (4.4. Evaluation on Human Shapes), p. 6 (4.3. Baseline Methods), p. 6 (4.1. Datasets and Benchmarks), p. 8 (4.6. Ablations), p. 1 (Figure/Table caption), results p. 7 (4.4. Evaluation on Human Shapes), p. 7 (4.4. Evaluation on Human Shapes), p. 6 (4.1. Datasets and Benchmarks), p. 1 (Figure/Table caption), p. 8 (4.6. Ablations), p. 5 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
