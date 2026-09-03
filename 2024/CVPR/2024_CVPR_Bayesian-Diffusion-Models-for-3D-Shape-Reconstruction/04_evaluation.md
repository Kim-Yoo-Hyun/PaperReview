# Evaluation - Bayesian Diffusion Models for 3D Shape Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Xu_Bayesian_Diffusion_Models_for_3D_Shape_Reconstruction_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Xu_Bayesian_Diffusion_Models_for_3D_Shape_Reconstruction_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.1. Quantitative Results), p. 6 (4.1. Quantitative Results), p. 7 (4.4. Ablation Study), p. 8 (4.4. Ablation Study), p. 8 (4.6. Human Evaluation), p. 7 (4.2. Qualitative Results)): It can be seen that our method effectively improves the performance and achieves state-ofthe-art.

## Evaluation Body Digest

- **p. 7 / 4.2. Qualitative Results - extractive body cue:** Qualitative comparisons on the real-world Pix3D dataset.
- **p. 5 / 4. Experiment - extractive body cue:** For both the ShapeNet-R2N2 and Pix3D datasets, we sample 4,096 points per 3D object and set the rendering resolution to 224×224.
- **p. 5 / 4. Experiment - extractive body cue:** Pix3D comprises diverse real-world image-shape pairs with meticulously annotated 2D-3D alignments.
- **p. 6 / 4. Experiment - extractive body cue:** Qualitative comparisons on the synthetic ShapeNet-R2N2 dataset.
- **p. 6 / 4.1. Quantitative Results - extractive body cue:** Following CCD-3DR, we also evaluate on the Pix3D dataset in Tab.
- **p. 7 / 4.2. Qualitative Results - extractive body cue:** 6, it can be seen clearly that our method surpasses baselines with respect to the reconstruction quality on the Pix3D dataset.
- **p. 8 / 4.6. Human Evaluation - extractive body cue:** We randomly selected 20 comparison groups from the Chair, Airplane, and Car classes in the ShapeNet dataset, totaling 60 groups.
- **p. 6 / 4.1. Quantitative Results - extractive body cue:** In this metric, a reconstructed point is deemed accurately predicted if its nearest distance to the points in the ground truth point cloud is within ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4. Experiment (p. 5); 4.1. Quantitative Results (p. 6); 4.2. Qualitative Results (p. 6); 4.6. Human Evaluation (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.1. Quantitative Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | It can be seen that our method effectively improves the performance and achieves state-ofthe-art. | p. 6 (4.1. Quantitative Results) |
| 4.1. Quantitative Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results indicate improvement in both CD and F1 across all three categories. | p. 6 (4.1. Quantitative Results) |
| 4.4. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | 4 reveals that integrating priors in the late stage alone yields significant improvement on model performance, reducing CD to 80.22 and increasing F1 to ... | p. 7 (4.4. Ablation Study) |
| 4.4. Ablation Study | EMPIRICAL / REAL-ROBOT OR HARDWARE | First, the performance will greatly improve once the prior duration is greater than 1, thereby strongly validating the effectiveness of our BDM. | p. 8 (4.4. Ablation Study) |
| 4.6. Human Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results show that our two methods, BDM-M and BDM-B, still outperforms CCD-3DR, which is aligned with the quantitative result presented in the main ... | p. 8 (4.6. Human Evaluation) |

## Dataset / Benchmark Role

- **p. 7 / 4.2. Qualitative Results - extractive body cue:** Qualitative comparisons on the real-world Pix3D dataset.
- **p. 5 / 4. Experiment - extractive body cue:** For both the ShapeNet-R2N2 and Pix3D datasets, we sample 4,096 points per 3D object and set the rendering resolution to 224×224.
- **p. 5 / 4. Experiment - extractive body cue:** Pix3D comprises diverse real-world image-shape pairs with meticulously annotated 2D-3D alignments.
- **p. 6 / 4. Experiment - extractive body cue:** Qualitative comparisons on the synthetic ShapeNet-R2N2 dataset.
- **p. 6 / 4.1. Quantitative Results - extractive body cue:** Following CCD-3DR, we also evaluate on the Pix3D dataset in Tab.
- **p. 7 / 4.2. Qualitative Results - extractive body cue:** 6, it can be seen clearly that our method surpasses baselines with respect to the reconstruction quality on the Pix3D dataset.
- **p. 8 / 4.6. Human Evaluation - extractive body cue:** We randomly selected 20 comparison groups from the Chair, Airplane, and Car classes in the ShapeNet dataset, totaling 60 groups.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Baseline vs Bayesian Diffusion Models. Our BDM brings rich prior knowledge into the shape reconstruction process, fixing the incorrect predictions by the baseline ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of the generative process in our Bayesian Diffusion Model. In each Bayesian denoising dtep, the prior diffusion model fuses with the reconstruction ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. Initially, a concise overview of denoising diffu- sion models, particularly focusing on point cloud diffusion models, is presented. This is followed by an ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Illustration for the Bayesian Diffusion Models compared with the standard Bayesian formulation. We present the standard Bayesian formulation and the one using stochastic ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 4. Illustration of our proposed fusion methods: BDM-M and BDM-B. The left part is the BDM-M, while the right side shows the BDM-B. 3.4.1 ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 5. Qualitative comparisons on the synthetic ShapeNet-R2N2 dataset. We use PC2 [51] and CCD-3DR [15] as baselines of 3D shape reconstruction. Rows 1-3 show ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 6. Qualitative comparisons on the real-world Pix3D dataset. We examine three distinct categories, each represented in a separate row. Columns 3,4 and 8,9 feature ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1. Performance on Chair, Airplane and Car of ShapeNet-R2N2. We evaluate our BDM, comparing with two baselines: PC2 and CCD-3DR. These experiments span three ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Qualitative comparisons on the real-world Pix3D dataset. | embodiment, simulator version and control stack | p. 7 (4.2. Qualitative Results), p. 5 (4. Experiment) |
| Task/environment | For both the ShapeNet-R2N2 and Pix3D datasets, we sample 4,096 points per 3D object and set the rendering resolution to 224×224. | reset, timeout, object/scene variation | p. 5 (4. Experiment), p. 5 (4. Experiment) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 3 (3.1. Bayesian Inference with Stochastic Gradient), p. 4 (3.4. Point Cloud Prior Integration) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 4 (3.4. Point Cloud Prior Integration), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In this metric, a reconstructed point is deemed accurately predicted if its nearest distance to the points in the ground truth point cloud is ... | definition/direction/unit from same section | p. 6 (4.1. Quantitative Results) |
| To address the issue of CD's susceptibility to outliers, we additionally present F-Score at a threshold of 0.01. | definition/direction/unit from same section | p. 6 (4.1. Quantitative Results) |
| Sixteen evaluators then ranked each group on a scale of 1 to 3, and the average scores are shown in Tab. | definition/direction/unit from same section | p. 8 (4.6. Human Evaluation) |
| 4 reveals that integrating priors in the late stage alone yields significant improvement on model performance, reducing CD to 80.22 and increasing F1 to ... | definition/direction/unit from same section | p. 7 (4.4. Ablation Study) |
| contrasts with the middle stage integration, which even degrades the performance of the baseline on F1. | definition/direction/unit from same section | p. 8 (4.4. Ablation Study) |
| In our BDM inference framework, Bayesian integration is strategically applied at specific intervals during the denoising process. | definition/direction/unit from same section | p. 5 (4. Experiment) |
| To demonstrate the efficacy of our Bayesian Diffusion Model, we conducted our experiments on two datasets: the synthetic dataset ShapeNet [12] and the realworld ... | definition/direction/unit from same section | p. 5 (4. Experiment) |
| Performance on Chair, Sofa and Table of Pix3D. | definition/direction/unit from same section | p. 7 (4.2. Qualitative Results) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| For the training of the reconstruction diffusion model, we select PC2 and CCD-3DR as two baselines and follow the recipe of CCD-3DR. | comparison identity and matched condition | p. 5 (4. Experiment) |
| We use PC2 [51] and CCD-3DR [15] as baselines of 3D shape reconstruction. | comparison identity and matched condition | p. 6 (4. Experiment) |
| Input Image Baseline (10%) BDM-M (ours) BDM-B (ours) Baseline (50%) BDM-M (ours) BDM-B (ours) Ground Truth Figure 5. | comparison identity and matched condition | p. 6 (4. Experiment) |
| We evaluate our BDM on the two baselines: PC2 and CCD-3DR. | comparison identity and matched condition | p. 7 (4.2. Qualitative Results) |
| 6, it can be seen clearly that our method surpasses baselines with respect to the reconstruction quality on the Pix3D dataset. | comparison identity and matched condition | p. 7 (4.2. Qualitative Results) |
| This is a remarkable improvement over the baseline (0 step). | comparison identity and matched condition | p. 8 (4.4. Ablation Study) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To validate the effectiveness and rationality of our BDM, we conduct several ablation studies to explore the impact of the timing, duration and intensity ... | component/input/data sensitivity | p. 7 (4.4. Ablation Study) |
| Table 6. Ablation on the ratio of prior integration. This table com- pares the effects of different prior integration ratios on CD and F1. | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Table 4. Ablation on the timing of prior integration. This table presents the impact of applying prior integration during the early, middle, and late ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| Fig. 2. Initially, a concise overview of denoising diffu- sion models, particularly focusing on point cloud diffusion models, is presented. This is followed by ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The contribution of our paper is summarized as follows: • We present Bayesian Diffusion Models (BDM), a new statistical inference algorithm that couples diffusionbased ... | It can be seen that our method effectively improves the performance and achieves state-ofthe-art. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.1. Quantitative Results), p. 6 (4.1. Quantitative Results), p. 7 (4.4. Ablation Study), p. 8 (4.4. Ablation Study), p. 8 (4.6. Human Evaluation), p. 7 (4.2. Qualitative Results) |
| Primary metric/result | The results indicate improvement in both CD and F1 across all three categories. | numeric claim only at cited anchor | p. 6 (4.1. Quantitative Results) |

- Numeric sentences retained from the body:
- **p. 5 / 4. Experiment - extractive body cue:** For both the ShapeNet-R2N2 and Pix3D datasets, we sample 4,096 points per 3D object and set the rendering resolution to 224×224.
- **p. 5 / 4. Experiment - extractive body cue:** This integration occurs every 32 steps, both in the early stage and in the late stage of denoising.
- **p. 5 / 4. Experiment - extractive body cue:** The fusion process initiated by this integration extends throughout 16 steps, ensuring a balanced and effective incorporation of Bayesian principles throughout the denoising procedure.
- **p. 7 / 4.3. Efficiency and Fairness Analysis - extractive body cue:** PC2/CCD-3DR BDM-B BDM-M #Parameters (M) 47.41 73.78 74.82 Runtime (s) 46.89 48.84 49.24 GPU memory (GB) 1.73 1.93 2.01 Table 3.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** Notably, the prior integration duration of 16 steps demonstrates the most substantial improvement.
- **p. 8 / 4.4. Ablation Study - extractive body cue:** This is a remarkable improvement over the baseline (0 step).

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | BDM overcomes the limitations in the traditional MCMC-based Bayesian inference that requires having the explicit distributions in performing stochastic gradient Langevin dynamics by tightly ... | p. 8 (5. Conclusion and Limitations) |
| body limitation/failure cue | contrasts with the middle stage integration, which even degrades the performance of the baseline on F1. | p. 8 (4.4. Ablation Study) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 3, we present BDM's parameters, runtime and GPU memory when doing inference with batch size of 1. | p. 7 (4.3. Efficiency and Fairness Analysis) |
| This integration occurs every 32 steps, both in the early stage and in the late stage of denoising. | p. 5 (4. Experiment) |
| Training of generative models was conducted on 4 NVIDIA A5000 GPUs, while we trained reconstruction models utilizing a single NVIDIA A5000 GPU. | p. 5 (4. Experiment) |
| While parameters increase due to the incorporation of prior model P, memory usage and runtime of BDM only increase slightly. | p. 7 (4.3. Efficiency and Fairness Analysis) |
| Notably, the prior integration duration of 16 steps demonstrates the most substantial improvement. | p. 8 (4.4. Ablation Study) |
| This table presents how different durations of prior integration affect CD and F1, ranging from 0 to 32 steps. | p. 8 (4.4. Ablation Study) |
| In particular, we feed the intermediate point cloud from our reconstruction model into the prior model, forward it through a certain number of timesteps ... | p. 4 (3.4. Point Cloud Prior Integration) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion and Limitations - extractive body cue:** BDM overcomes the limitations in the traditional MCMC-based Bayesian inference that requires having the explicit distributions in performing stochastic gradient Langevin dynamics by tightly coupling ...
- **p. 8 / 4.4. Ablation Study - extractive body cue:** contrasts with the middle stage integration, which even degrades the performance of the baseline on F1.

- **Evidence anchors reviewed:** datasets p. 7 (4.2. Qualitative Results), p. 5 (4. Experiment), p. 5 (4. Experiment), p. 6 (4. Experiment), p. 6 (4.1. Quantitative Results), p. 7 (4.2. Qualitative Results), metrics p. 6 (4.1. Quantitative Results), p. 6 (4.1. Quantitative Results), p. 8 (4.6. Human Evaluation), p. 7 (4.4. Ablation Study), p. 8 (4.4. Ablation Study), p. 5 (4. Experiment), baselines p. 5 (4. Experiment), p. 6 (4. Experiment), p. 6 (4. Experiment), p. 7 (4.2. Qualitative Results), p. 7 (4.2. Qualitative Results), p. 8 (4.4. Ablation Study), results p. 6 (4.1. Quantitative Results), p. 6 (4.1. Quantitative Results), p. 7 (4.4. Ablation Study), p. 8 (4.4. Ablation Study), p. 8 (4.6. Human Evaluation), p. 7 (4.2. Qualitative Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
