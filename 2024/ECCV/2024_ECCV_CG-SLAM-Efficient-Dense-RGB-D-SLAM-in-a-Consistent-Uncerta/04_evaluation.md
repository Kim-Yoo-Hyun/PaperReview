# Evaluation - CG-SLAM: Efficient Dense RGB-D SLAM in a Consistent Uncertainty-aware 3D Gaussian Field

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3580_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/03580.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (4 Experiments), p. 11 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments)): In this section, we describe our experimental setup and validate that the proposed system can achieve improvement in both accuracy (Sec.

## Evaluation Body Digest

- **p. 10 / 4 Experiments - extractive body cue:** We examined the generalization of our method on real-world TUM [44] and ScanNet [10] datasets, which contain 5 and 6 challenging scenes respectively.
- **p. 10 / 4 Experiments - extractive body cue:** 2, despite noisy and sparse depth information in the real-world TUM-RGBD dataset [44], our method still achieves better or competitive performance in 5 selected scenarios.
- **p. 11 / 4 Experiments - extractive body cue:** Our system consistently achieved the best performance in this dataset, both for 8 individual scenes and for the average.
- **p. 11 / 4 Experiments - extractive body cue:** CG-SLAM 11 Table 1: Tracking Results on the Replica Dataset [43] (ATE RMSE [cm] ↓).
- **p. 13 / 4 Experiments - extractive body cue:** 4: Reconstruction Performance on Replica [43] Dataset.
- **p. 12 / 4 Experiments - extractive body cue:** However, as a non-MLP scene representation, the 3D Gaussian field inevitably requires much memory consumption to store different properties.
- **p. 13 / 56.50 MB - extractive body cue:** Alignment and variance losses push primitives closer to object surfaces, facilitating novel view syn
- **p. 14 / 56.50 MB - extractive body cue:** This plot illustrates that the uncertainty model helps improve tracking accuracy while avoiding some extreme errors.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4 Experiments (p. 9).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | In this section, we describe our experimental setup and validate that the proposed system can achieve improvement in both accuracy (Sec. | p. 9 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our system achieves better tracking accuracy and lower variance in different scenarios. "-" indicates unavailable results because the related work is not open source. | p. 11 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 2, despite noisy and sparse depth information in the real-world TUM-RGBD dataset [44], our method still achieves better or competitive performance in 5 selected ... | p. 10 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | It can be observed that our method outperforms all baselines on mapping accuracy. | p. 11 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | In terms of mapping accuracy, our method can outperform all existing methods. | p. 12 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 10 / 4 Experiments - extractive body cue:** We examined the generalization of our method on real-world TUM [44] and ScanNet [10] datasets, which contain 5 and 6 challenging scenes respectively.
- **p. 10 / 4 Experiments - extractive body cue:** 2, despite noisy and sparse depth information in the real-world TUM-RGBD dataset [44], our method still achieves better or competitive performance in 5 selected scenarios.
- **p. 11 / 4 Experiments - extractive body cue:** Our system consistently achieved the best performance in this dataset, both for 8 individual scenes and for the average.
- **p. 11 / 4 Experiments - extractive body cue:** CG-SLAM 11 Table 1: Tracking Results on the Replica Dataset [43] (ATE RMSE [cm] ↓).
- **p. 13 / 4 Experiments - extractive body cue:** 4: Reconstruction Performance on Replica [43] Dataset.
- **p. 12 / 4 Experiments - extractive body cue:** However, as a non-MLP scene representation, the 3D Gaussian field inevitably requires much memory consumption to store different properties.
- **p. 13 / 56.50 MB - extractive body cue:** Alignment and variance losses push primitives closer to object surfaces, facilitating novel view syn

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: CG-SLAM, which adopts a well-designed 3D Gaussian field, can simultaneously achieve state-of-the-art performance in localization, reconstruction and rendering. Ben- efiting from 3D Gaussian ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: System Overview. In a 3D Gaussian field constructed from an RGB-D se- quence, we can render color, depth, opacity, and uncertainty maps through ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 3: Uncertainty of the Gaussian Primitives. Uncertainty of a Gaussian prim- itive is derived from its dominated pixels and corresponding depth biases, reflecting the ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 1: Tracking Results on the Replica Dataset [43] (ATE RMSE [cm] ↓). Our system consistently achieved the best performance in this dataset, both for ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 2: Tracking Results on the TUM-RGBD Dataset [44] (ATE RMSE [cm] ↓). Our system achieves better tracking accuracy and lower variance in different scenarios. ...
- **p. 11 / Figure/Table caption - extractive body cue:** Table 3: Tracking Results on the ScanNet Dataset [10] (ATE RMSE [cm] ↓). Our method achieves state-of-the-art tracking results in 6 scenes and exceeds other ...
- **p. 12 / Figure/Table caption - extractive body cue:** Table 4: Reconstruction Results on the Replica [43] Dataset. In terms of map- ping accuracy, our method can outperform all existing methods. Due to the ...
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 4: Reconstruction Performance on Replica [43] Dataset. We qualitatively compared the mesh reconstruction results from CG-SLAM and other baselines, where CG-SLAM can produce more ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We examined the generalization of our method on real-world TUM [44] and ScanNet [10] datasets, which contain 5 and 6 challenging scenes respectively. | embodiment, simulator version and control stack | p. 10 (4 Experiments), p. 10 (4 Experiments) |
| Task/environment | 2, despite noisy and sparse depth information in the real-world TUM-RGBD dataset [44], our method still achieves better or competitive performance in 5 selected ... | reset, timeout, object/scene variation | p. 10 (4 Experiments), p. 11 (4 Experiments) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 7 (3 Method), p. 7 (3 Method) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 8 (3 Method), p. 8 (3 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| This plot illustrates that the uncertainty model helps improve tracking accuracy while avoiding some extreme errors. | definition/direction/unit from same section | p. 14 (56.50 MB) |
| This is the reason why we have lower variances and higher accuracy. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| Given 3D triangle meshes, we compute mapping Accuracy [cm], Completion [cm], and Completion Ratio [<5cm %]. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| Our system achieves better tracking accuracy and lower variance in different scenarios. "-" indicates unavailable results because the related work is not open source. | definition/direction/unit from same section | p. 11 (4 Experiments) |
| Table 4: Reconstruction Results on the Replica [43] Dataset. In terms of map- ping accuracy, our method can outperform all existing methods. Due to ... | definition/direction/unit from same section | p. 12 (Figure/Table caption) |
| In this section, we describe our experimental setup and validate that the proposed system can achieve improvement in both accuracy (Sec. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| It can be observed that our method outperforms all baselines on mapping accuracy. | definition/direction/unit from same section | p. 11 (4 Experiments) |
| For tracking, this lightweight version can work twice as fast as the original one, at the cost of a slight decrease in accuracy, as ... | definition/direction/unit from same section | p. 12 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We primarily consider state-of-the-art NeRF-SLAM works, including NICE-SLAM [61], Co-SLAM [50], Point-SLAM [37], and Vox-Fusion [56], as baselines. | comparison identity and matched condition | p. 10 (4 Experiments) |
| It can be observed that our method outperforms all baselines on mapping accuracy. | comparison identity and matched condition | p. 11 (4 Experiments) |
| We qualitatively compared the mesh reconstruction results from CG-SLAM and other baselines, where CG-SLAM can produce more detailed geometry at a lower computation cost. | comparison identity and matched condition | p. 13 (4 Experiments) |
| For a fair comparison, we reproduced all results from these baselines and reported their reconstruction performance with the same evaluation mechanism. | comparison identity and matched condition | p. 10 (4 Experiments) |
| We achieve state-of-the-art reconstruction in observed areas. | comparison identity and matched condition | p. 11 (4 Experiments) |
| In terms of mapping accuracy, our method can outperform all existing methods. | comparison identity and matched condition | p. 12 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 4.4 Ablation Study To verify the rationality of our designs, we investigate the effectiveness of the anisotropy regularization, alignment and variance losses, and uncertainty ... | component/input/data sensitivity | p. 13 (56.50 MB) |
| Table 6: Isotropy Loss Ablation Results(ATE RMSE [cm] ↓). The experimental results demonstrate the effectiveness of our anisotropy regularization term. "-" indicates a failure ... | component/input/data sensitivity | p. 14 (Figure/Table caption) |
| To more intuitively illustrate this phenomenon, we display opacity maps with and without anisotropy regularization in Fig. | component/input/data sensitivity | p. 13 (56.50 MB) |
| For further quantitative ablation results, refer to the supplementary material. | component/input/data sensitivity | p. 14 (56.50 MB) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Overall, our contributions can be summarized as follows: - We present a new GPU-accelerated framework for real-time dense RGB-D SLAM based on a thorough ... | In this section, we describe our experimental setup and validate that the proposed system can achieve improvement in both accuracy (Sec. | PDF body cue; verify exact table/figure and matched conditions | p. 9 (4 Experiments), p. 11 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments) |
| Primary metric/result | Our system achieves better tracking accuracy and lower variance in different scenarios. "-" indicates unavailable results because the related work is not open source. | numeric claim only at cited anchor | p. 11 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 10 / 4 Experiments - extractive body cue:** We run our system on a desktop equipped with an Intel i9-14900K and an NVIDIA RTX 4090 GPU.
- **p. 11 / 4 Experiments - extractive body cue:** NICE-SLAM 0.97 1.31 1.07 0.88 1.00 1.06 1.10 1.13 1.06 Co-SLAM 0.77 1.04 1.09 0.58 0.53 2.05 1.49 0.84 0.99 Point-SLAM 0.56 0.47 0.30 0.35 ...
- **p. 11 / 4 Experiments - extractive body cue:** NICE-SLAM 4.26 4.99 34.49 31.73 3.87 15.87 Co-SLAM 2.7 4.57 30.16 1.9 2.6 8.38 Point-SLAM 4.34 4.54 30.92 1.31 3.48 8.92 Vox-Fusion 3.52 6.00 19.53 ...
- **p. 11 / 4 Experiments - extractive body cue:** Our method achieves state-of-the-art tracking results in 6 scenes and exceeds other methods on average. "-" indicates failure results in Vox-Fusion [56].
- **p. 11 / 4 Experiments - extractive body cue:** NICE-SLAM 12.00 14.00 7.90 10.90 13.40 6.20 10.70 Co-SLAM 7.18 12.29 10.9 6.62 13.43 7.13 9.37 Point-SLAM 10.24 8.29 11.86 22.16 14.77 9.54 12.19 Vox-Fusion ...
- **p. 12 / 4 Experiments - extractive body cue:** With the support of the GPU-accelerated rasterizer, our system can operate at around 8.5Hz.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Considerable memory usage is one limitation of the Gaussianbased system. | p. 14 (5 Conclusion) |
| body limitation/failure cue | Our method achieves state-of-the-art tracking results in 6 scenes and exceeds other methods on average. "-" indicates failure results in Vox-Fusion [56]. | p. 11 (4 Experiments) |
| body limitation/failure cue | The experimental results demonstrate the effectiveness of our anisotropy regularization term. "-" indicates a failure situation. | p. 14 (56.50 MB) |
| body limitation/failure cue | Due to the inherent limitation of 3D Gaussian representation, our method is slightly worse in completion. | p. 12 (4 Experiments) |
| body limitation/failure cue | This reason results in a considerable memory footprint in the Gaussian-based SLAM system, which is a common limitation in other Gaussian-based research topics. | p. 12 (4 Experiments) |
| body limitation/failure cue | Fig. 3: Uncertainty of the Gaussian Primitives. Uncertainty of a Gaussian prim- itive is derived from its dominated pixels and corresponding depth biases, reflecting ... | p. 7 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We run our system on a desktop equipped with an Intel i9-14900K and an NVIDIA RTX 4090 GPU. | p. 10 (4 Experiments) |
| We set the learning rate of {so(3)/T} to {0.0015, 0.00215} in sequential tracking in all experiments. | p. 10 (4 Experiments) |
| With the support of the GPU-accelerated rasterizer, our system can operate at around 8.5Hz. | p. 12 (4 Experiments) |
| 4.3 Runtime and Memory Analysis We evaluate the runtime and memory footprint of our system compared to other works in Tab. | p. 12 (4 Experiments) |
| We comprehensively compared the runtime and memory usage on Replica [43] Office 0. | p. 13 (4 Experiments) |
| Method Tracking Mapping Mapping System Decoder Scene [ms× it]↓[ms× it]↓Interval FPS↑ Param↓ Embeeding↓ Vox-Fusion 23.61 × 30 86.55 × 10 10 1.25 | p. 13 (4 Experiments) |
| Fast Gaussian splatting rasterizer enables efficient pixel-by-pixel parallel rendering, and is fully differentiable, which provides a useful GPU-accelerated framework. | p. 6 (3 Method) |
| In terms of color rendering, the Gaussian splatting rasterizer adopts an α-blending solution, which accumulates radiance c and opacity values σ on a given ... | p. 6 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 14 / 5 Conclusion - extractive body cue:** Considerable memory usage is one limitation of the Gaussianbased system.
- **p. 11 / 4 Experiments - extractive body cue:** Our method achieves state-of-the-art tracking results in 6 scenes and exceeds other methods on average. "-" indicates failure results in Vox-Fusion [56].
- **p. 14 / 56.50 MB - extractive body cue:** The experimental results demonstrate the effectiveness of our anisotropy regularization term. "-" indicates a failure situation.
- **p. 12 / 4 Experiments - extractive body cue:** Due to the inherent limitation of 3D Gaussian representation, our method is slightly worse in completion.
- **p. 12 / 4 Experiments - extractive body cue:** This reason results in a considerable memory footprint in the Gaussian-based SLAM system, which is a common limitation in other Gaussian-based research topics.
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 3: Uncertainty of the Gaussian Primitives. Uncertainty of a Gaussian prim- itive is derived from its dominated pixels and corresponding depth biases, reflecting the ...

- **Evidence anchors reviewed:** datasets p. 10 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments), p. 13 (4 Experiments), p. 12 (4 Experiments), metrics p. 14 (56.50 MB), p. 10 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 12 (Figure/Table caption), p. 9 (4 Experiments), baselines p. 10 (4 Experiments), p. 11 (4 Experiments), p. 13 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), results p. 9 (4 Experiments), p. 11 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
