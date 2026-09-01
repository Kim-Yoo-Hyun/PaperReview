# Evaluation - GeGS-PCR: Fast and Robust Color 3D Point Cloud Registration with Two-Stage Geometric-3DGS Fusion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (31 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=UkBwyp3aXG; PDF retrieval source: https://openreview.net/pdf/b288be2e77239176daf3dd0989250da05bea4f5d.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 26 (A.5 Additional Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 26 (A.5 Additional Experiments), p. 25 (A.5 Additional Experiments), p. 25 (A.5 Additional Experiments)): The photometric optimization loss achieves the highest performance with 87.6% PIR, 98.2% FMR, 71.6% IR, and 91.9% RR on C3DM, and 56.1% PIR, 89.3% FMR, 44.2% IR, and 75.7% RR ...

## Evaluation Body Digest

- **p. 7 / 4 Experiments - extractive PDF cue:** To validate the performance of the GeGS-PCR model, we evaluate it on the indoor benchmarks Color3DMatch (C3DM) and Color3DLoMatch (C3DLM), as well as our colorized ...
- **p. 25 / A.5 Additional Experiments - extractive PDF cue:** C3DM consists of 62 scenes, with 46 scenes used for training, 8 for validation, and 8 for testing.
- **p. 7 / 4 Experiments - extractive PDF cue:** Each point cloud in these datasets includes an RGB color value.
- **p. 9 / 4 Experiments - extractive PDF cue:** 4.2 Outdoor Benchmarks: ColorKitti Registration results.
- **p. 9 / 4 Experiments - extractive PDF cue:** 4 shows the comparison of registration results using geometric attention and our 3DGS self-attention in low-overlap scenes.
- **p. 25 / A.5 Additional Experiments - extractive PDF cue:** During the entire training process, GeGS-PCR was trained for 40 epochs on the 3DMatch dataset and 80 epochs on the KITTI dataset.
- **p. 26 / A.5 Additional Experiments - extractive PDF cue:** 6 shows the training loss curves for both the standard model (without LoRA) and the model with LoRA applied on the Color3DMatch dataset.
- **p. 27 / A.7 Qualitative Results - extractive PDF cue:** In the ColorKitti dataset shown in Fig.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 7); A.5 Additional Experiments (p. 25); A.7 Qualitative Results (p. 27).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| A.5 Additional Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | The photometric optimization loss achieves the highest performance with 87.6% PIR, 98.2% FMR, 71.6% IR, and 91.9% RR on C3DM, and 56.1% PIR, 89.3% ... | p. 26 (A.5 Additional Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | In RR, GeGS-PCR achieves 97.9% on C3DM and 90.7% on C3DLM, outperforming ColorPCR by 0.4% on C3DM and 4.2% on C3DLM. | p. 8 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | In addition, removing LoRA optimization (row f) leads to a slight drop in registration performance, particularly in IR and RR, indicating that LoRA mainly ... | p. 9 (4 Experiments) |
| A.5 Additional Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | From the comparison of results, it is evident that our GeGS-PCR consistently achieves better performance. | p. 26 (A.5 Additional Experiments) |
| A.5 Additional Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Particularly on C3DM, GeGSPCR improves by 0.7% over YOHO and significantly surpasses methods like Predator and SpinNet. | p. 25 (A.5 Additional Experiments) |

## Dataset / Benchmark Role

- **p. 7 / 4 Experiments - extractive PDF cue:** To validate the performance of the GeGS-PCR model, we evaluate it on the indoor benchmarks Color3DMatch (C3DM) and Color3DLoMatch (C3DLM), as well as our colorized ...
- **p. 25 / A.5 Additional Experiments - extractive PDF cue:** C3DM consists of 62 scenes, with 46 scenes used for training, 8 for validation, and 8 for testing.
- **p. 7 / 4 Experiments - extractive PDF cue:** Each point cloud in these datasets includes an RGB color value.
- **p. 9 / 4 Experiments - extractive PDF cue:** 4.2 Outdoor Benchmarks: ColorKitti Registration results.
- **p. 9 / 4 Experiments - extractive PDF cue:** 4 shows the comparison of registration results using geometric attention and our 3DGS self-attention in low-overlap scenes.
- **p. 25 / A.5 Additional Experiments - extractive PDF cue:** During the entire training process, GeGS-PCR was trained for 40 epochs on the 3DMatch dataset and 80 epochs on the KITTI dataset.
- **p. 26 / A.5 Additional Experiments - extractive PDF cue:** 6 shows the training loss curves for both the standard model (without LoRA) and the model with LoRA applied on the Color3DMatch dataset.
- **p. 27 / A.7 Qualitative Results - extractive PDF cue:** In the ColorKitti dataset shown in Fig.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: In scenarios with minimal overlap, incomplete geomet- ric features, and subtle color variations, methods that simply add color features perform moderately, whereas GeGS-PCR ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: Pipeline. The entire network backbone is divided into coarse and fine scales. The feature extraction module extracts and integrates geometric and color information ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 1: Evaluation results on C3DM and C3DLM. #Samples in the table represents the number of correspondences selected by RANSAC. C3DM C3DLM #Samples 5000 2500 ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 2: Registration results w/o RANSAC on C3DM and C3DLM. The model is the time for feature extraction, while the pose time is for transformation ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 3: Performance of ablation experiments C3DM C3DLM Overlap PIR(%) FMR(%) IR(%) RR(%)
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 3: Registration performance with GeGS-PCR and Geometric self-attention.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4: Ablation results based on ColorPCR baseline C3DM C3DLM
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 5: Registration results w/o RANSAC on Kitti

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To validate the performance of the GeGS-PCR model, we evaluate it on the indoor benchmarks Color3DMatch (C3DM) and Color3DLoMatch (C3DLM), as well as our ... | embodiment, simulator version and control stack | p. 7 (4 Experiments), p. 25 (A.5 Additional Experiments) |
| Task/environment | C3DM consists of 62 scenes, with 46 scenes used for training, 8 for validation, and 8 for testing. | reset, timeout, object/scene variation | p. 25 (A.5 Additional Experiments), p. 7 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3 Method), p. 4 (3 Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 5 (3 Method), p. 5 (3 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In addition, removing LoRA optimization (row f) leads to a slight drop in registration performance, particularly in IR and RR, indicating that LoRA mainly ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| Additionally, in Table 8, we conduct a detailed analysis of the performance of recent techniques in terms of Relative Rotation Error (RRE) (the distance ... | definition/direction/unit from same section | p. 26 (A.5 Additional Experiments) |
| Removing LoRA (row g) slightly reduces performance, confirming its role in accelerating convergence and providing consistent accuracy gains while maintaining efficiency. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| The results demonstrate that in high overlap scenarios, GeGS-PCR exhibits superior registration accuracy compared to Geotransformer, particularly in terms of point correspondence and inlier ... | definition/direction/unit from same section | p. 27 (A.7 Qualitative Results) |
| In low-overlap or noisy point cloud data, GeGS-PCR dynamically adjusts local geometric distribution through covariance modeling, significantly improving registration accuracy. | definition/direction/unit from same section | p. 28 (A.7 Qualitative Results) |
| Overall, GeGS-PCR demonstrates higher stability and precision across various overlap conditions, proving its robustness in complex scenarios. | definition/direction/unit from same section | p. 27 (A.7 Qualitative Results) |
| Notably, in areas with similar geometric features such as floors and walls or appliances and furniture, GeGS-PCR maintains high accuracy. | definition/direction/unit from same section | p. 28 (A.7 Qualitative Results) |
| Compared to other methods, 3DGS Selfattention significantly improves PIR (Precision), IR (Inlier Ratio), and RR (Registration Recall). | definition/direction/unit from same section | p. 25 (A.5 Additional Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We compared GeGS-PCR with several SOTA methods (metrics in Appendix A.3). | comparison identity and matched condition | p. 7 (4 Experiments) |
| Baselines ablation experiments Table 4 reports the ablation results based on the ColorPCR baseline. | comparison identity and matched condition | p. 9 (4 Experiments) |
| Specifically, the losses for the LoRA-enhanced model decrease more steadily and reach a lower final value compared to the model without LoRA, suggesting that ... | comparison identity and matched condition | p. 27 (A.5 Additional Experiments) |
| Model Estimator C3DM C3DLM RRE(°) RTE(m) RRE(°) RTE(m) Predator [28] RANSAC-50k 2.029 0.064 3.048 0.093 CoFiNet [44] RANSAC-50k 2.002 0.064 3.271 0.090 GeoTransformer [15] ... | comparison identity and matched condition | p. 27 (A.5 Additional Experiments) |
| Figure 6: Comparison of Training Loss with and without LoRA Optimization (Color3DMatch Dataset). Additional baselines. Table 6 is a continuation of Table 1, present- ... | comparison identity and matched condition | p. 25 (Figure/Table caption) |
| As shown in Table 2, GeGS-PCR outperforms both RANSAC and RANSACfree methods. | comparison identity and matched condition | p. 8 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| More detailed ablation analysis is shown in Appendix A.5. | component/input/data sensitivity | p. 9 (4 Experiments) |
| Without the color encoder (row d), performance drops slightly, especially in FMR. | component/input/data sensitivity | p. 9 (4 Experiments) |
| 6 shows the training loss curves for both the standard model (without LoRA) and the model with LoRA applied on the Color3DMatch dataset. | component/input/data sensitivity | p. 26 (A.5 Additional Experiments) |
| Specifically, the losses for the LoRA-enhanced model decrease more steadily and reach a lower final value compared to the model without LoRA, suggesting that ... | component/input/data sensitivity | p. 27 (A.5 Additional Experiments) |
| Model Estimator C3DM C3DLM RRE(°) RTE(m) RRE(°) RTE(m) Predator [28] RANSAC-50k 2.029 0.064 3.048 0.093 CoFiNet [44] RANSAC-50k 2.002 0.064 3.271 0.090 GeoTransformer [15] ... | component/input/data sensitivity | p. 27 (A.5 Additional Experiments) |
| Table 4: Ablation results based on ColorPCR baseline C3DM C3DLM | component/input/data sensitivity | p. 8 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Additionally, we introduce a joint photometric loss to improve the utilization of color information during the registration process. | The photometric optimization loss achieves the highest performance with 87.6% PIR, 98.2% FMR, 71.6% IR, and 91.9% RR on C3DM, and 56.1% PIR, 89.3% ... | PDF body cue; verify exact table/figure and matched conditions | p. 26 (A.5 Additional Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 26 (A.5 Additional Experiments), p. 25 (A.5 Additional Experiments), p. 25 (A.5 Additional Experiments) |
| Primary metric/result | In RR, GeGS-PCR achieves 97.9% on C3DM and 90.7% on C3DLM, outperforming ColorPCR by 0.4% on C3DM and 4.2% on C3DLM. | numeric claim only at cited anchor | p. 8 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 8 / 4 Experiments - extractive PDF cue:** For RANSAC-based methods, GeGS-PCR achieves 97.9% RR on C3DM and 90.7% on C3DLM, surpassing ColorPCR, with a total processing time of 1.703s, second only to ...
- **p. 8 / 4 Experiments - extractive PDF cue:** GeGS-PCR also achieves the best pose estimation time of 0.072s.
- **p. 8 / 4 Experiments - extractive PDF cue:** For RANSAC-free methods, GeGS-PCR reaches 96.9% RR on C3DM and 89.1% on C3DLM, outperforming ColorPCR, with a total time of 0.124s, second only to GeoTransformer ...
- **p. 25 / A.5 Additional Experiments - extractive PDF cue:** C3DM consists of 62 scenes, with 46 scenes used for training, 8 for validation, and 8 for testing.
- **p. 25 / A.5 Additional Experiments - extractive PDF cue:** We implemented and evaluated our GeGS-PCR using PyTorch [15] on an AMD 610M CPU and an NVIDIA RTX 4070 GPU.
- **p. 25 / A.5 Additional Experiments - extractive PDF cue:** During the entire training process, GeGS-PCR was trained for 40 epochs on the 3DMatch dataset and 80 epochs on the KITTI dataset.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Through local Gaussian feature extraction, GeGS-PCR effectively suppresses noise interference and robustly fuses geometric and color features. | p. 10 (5 Conclusion) |
| body limitation/failure cue | In future work, we aim to explore scene-level registration of 3DGS for more realistic environmental registration. | p. 27 (A.6 Limitations) |
| body limitation/failure cue | Further limitations and a comprehensive performance analysis can be found in Appendix A.5 and Appendix A.6. | p. 10 (4 Experiments) |
| body limitation/failure cue | Removing color information (row e) causes the most significant degradation, with PIR, IR, and RR dropping notably on both C3DM and C3DLM, highlighting the ... | p. 9 (4 Experiments) |
| body limitation/failure cue | Specifically, compared to Vanilla Self-attention, 3DGS Self-attention shows stronger robustness across the entire overlap range, with its advantages becoming more pronounced in complex environments. | p. 25 (A.5 Additional Experiments) |
| body limitation/failure cue | As the overlap decreases, GeGS-PCR maintains strong performance even in the 0.5-0.6 overlap range, with a PIR of 0.938, an IR of 0.872, and ... | p. 25 (A.5 Additional Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The batch size was set to 1, with an initial learning rate of 10-4, decaying by 0.05 every epoch. | p. 25 (A.5 Additional Experiments) |
| We implemented and evaluated our GeGS-PCR using PyTorch [15] on an AMD 610M CPU and an NVIDIA RTX 4070 GPU. | p. 25 (A.5 Additional Experiments) |
| To validate the performance of the GeGS-PCR model, we evaluate it on the indoor benchmarks Color3DMatch (C3DM) and Color3DLoMatch (C3DLM), as well as our ... | p. 7 (4 Experiments) |
| Without the color encoder (row d), performance drops slightly, especially in FMR. | p. 9 (4 Experiments) |
| In contrast, removing the color encoder (row b) or geometric positional encoding (row f) only leads to minor fluctuations, suggesting these modules play supportive ... | p. 9 (4 Experiments) |
| The specific steps of the 3DGS encoder are as follows: We calculate the covariance matrix of each local neighborhood in the point cloud, which ... | p. 5 (3 Method) |
| The image gradient is: ∂∥f(G1) -f(G2)∥2 ∂∆I = 2 · (f(G1) -f(G2)), (15) We also calculate the rendering Jacobian and Lie Algebra Jacobian as: ... | p. 22 (A.1 Proof of photometric optimization) |
| The encoder first inputs the three-channel color vector Fc ∈R3 into a multi-layer perceptron (MLP). | p. 4 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / 5 Conclusion - extractive PDF cue:** Through local Gaussian feature extraction, GeGS-PCR effectively suppresses noise interference and robustly fuses geometric and color features.
- **p. 27 / A.6 Limitations - extractive PDF cue:** In future work, we aim to explore scene-level registration of 3DGS for more realistic environmental registration.
- **p. 10 / 4 Experiments - extractive PDF cue:** Further limitations and a comprehensive performance analysis can be found in Appendix A.5 and Appendix A.6.
- **p. 9 / 4 Experiments - extractive PDF cue:** Removing color information (row e) causes the most significant degradation, with PIR, IR, and RR dropping notably on both C3DM and C3DLM, highlighting the critical ...
- **p. 25 / A.5 Additional Experiments - extractive PDF cue:** Specifically, compared to Vanilla Self-attention, 3DGS Self-attention shows stronger robustness across the entire overlap range, with its advantages becoming more pronounced in complex environments.
- **p. 25 / A.5 Additional Experiments - extractive PDF cue:** As the overlap decreases, GeGS-PCR maintains strong performance even in the 0.5-0.6 overlap range, with a PIR of 0.938, an IR of 0.872, and an ...

- **PDF anchors reviewed:** datasets p. 7 (4 Experiments), p. 25 (A.5 Additional Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 25 (A.5 Additional Experiments), metrics p. 9 (4 Experiments), p. 26 (A.5 Additional Experiments), p. 9 (4 Experiments), p. 27 (A.7 Qualitative Results), p. 28 (A.7 Qualitative Results), p. 27 (A.7 Qualitative Results), baselines p. 7 (4 Experiments), p. 9 (4 Experiments), p. 27 (A.5 Additional Experiments), p. 27 (A.5 Additional Experiments), p. 25 (Figure/Table caption), p. 8 (4 Experiments), results p. 26 (A.5 Additional Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 26 (A.5 Additional Experiments), p. 25 (A.5 Additional Experiments), p. 25 (A.5 Additional Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
