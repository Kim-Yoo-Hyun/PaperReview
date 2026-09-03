# Evaluation - HAD: Hallucination-Aware Diffusion Priors for 3D Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Liu_HAD_Hallucination-Aware_Diffusion_Priors_for_3D_Reconstruction_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_HAD_Hallucination-Aware_Diffusion_Priors_for_3D_Reconstruction_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (5.4. Ablation studies), p. 8 (5.4. Ablation studies), p. 7 (5.3. Cross-domain evaluation), p. 7 (5.4. Ablation studies), p. 1 (Figure/Table caption), p. 6 (5.2. In-domain evaluation)): We select 3 views to achieve a trade-off between marginal improvement and computational overhead.

## Evaluation Body Digest

- **p. 6 / 5.1. Experimental Setup - extractive body cue:** We first curate training dataset of randomly selected 116 scenes from benchmark dataset for hallucination score network training.
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** This design ensures that no leaked information from the target subset is used for model adaptation, maintaining fair and unbiased comparisons across methods. • MipNeRF360 ...
- **p. 8 / 5.4. Ablation studies - extractive body cue:** Method (GSplat-MCMC) PSNR ↑ SSIM ↑ LPIPS ↓ Gsplat-MCMC 26.280 0.869 0.101 Difix3D 26.770 0.874 0.0926 Ours 26.969 0.876 0.0921 estimation on our curated dataset ...
- **p. 7 / 5.3. Cross-domain evaluation - extractive body cue:** We also examine whether our HAD can generalize to a different dataset - MipNeRF360 [3].
- **p. 8 / 5.4. Ablation studies - extractive body cue:** We calculate the Mean Absolute Error (MAE) of the predicted hallucination score maps on the test scenes.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 6. Different hallucination score estimators. We use Mean Absolute Error (MAE) of the predicted hallucination score maps as our evaluation metric. We demonstrate that ...
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** The poses for these augmented views are sampled from views excluded from the 3DGS training set, providing ground-truth images that enable computation of the ground-truth ...
- **p. 7 / 5.2. In-domain evaluation - extractive body cue:** Notably, LVSM [20], despite producing blurry images, achieves better fidelity, validating our approach of leveraging LVSM's feature backbone as multi-view encoder for hallucination score prediction.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 5. Experiments (p. 6); 5.1. Experimental Setup (p. 6); 5.2. In-domain evaluation (p. 6); 5.3. Cross-domain evaluation (p. 7).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.4. Ablation studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | We select 3 views to achieve a trade-off between marginal improvement and computational overhead. | p. 8 (5.4. Ablation studies) |
| 5.4. Ablation studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | We demonstrate that our hallucination score network, with the pretrained multiview encoder, achieves the best performance. | p. 8 (5.4. Ablation studies) |
| 5.3. Cross-domain evaluation | EMPIRICAL / SOURCE-REPORTED EVALUATION | 2, similar to the in-domain evaluation, our method achieves state-of-the-art performance. | p. 7 (5.3. Cross-domain evaluation) |
| 5.4. Ablation studies | EMPIRICAL / SOURCE-REPORTED EVALUATION | 3, HAD notably improves performance over Difix3D, confirming the importance of hallucination awareness. | p. 7 (5.4. Ablation studies) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 1. While diffusion priors [41] enhance the quality of 3D reconstruction, they introduce detrimental aliens - the hallucinated elements that do not exist ... | p. 1 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 6 / 5.1. Experimental Setup - extractive body cue:** We first curate training dataset of randomly selected 116 scenes from benchmark dataset for hallucination score network training.
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** This design ensures that no leaked information from the target subset is used for model adaptation, maintaining fair and unbiased comparisons across methods. • MipNeRF360 ...
- **p. 8 / 5.4. Ablation studies - extractive body cue:** Method (GSplat-MCMC) PSNR ↑ SSIM ↑ LPIPS ↓ Gsplat-MCMC 26.280 0.869 0.101 Difix3D 26.770 0.874 0.0926 Ours 26.969 0.876 0.0921 estimation on our curated dataset ...
- **p. 7 / 5.3. Cross-domain evaluation - extractive body cue:** We also examine whether our HAD can generalize to a different dataset - MipNeRF360 [3].
- **p. 8 / 5.4. Ablation studies - extractive body cue:** We calculate the Mean Absolute Error (MAE) of the predicted hallucination score maps on the test scenes.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. While diffusion priors [41] enhance the quality of 3D reconstruction, they introduce detrimental aliens - the hallucinated elements that do not exist in ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overview of framework - We train 3DGS with input images and HAD-augmented novel views. HAD combines a pretrained diffusion prior (which generates images ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative comparison of different methods on DL3DV [25]. Best, second, and third results are highlighted in 1st , 2nd , and 3rd , ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 3. Examples on DL3DV [25] - We show novel-view rendering obtained by ours, Gspat-mcmc [22], LVSM [20] and Difix3D [41]. Our approach achieves the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Quantitative comparison of different methods on Mip- Nerf360 [3]. Note the results of Genfusion and FSGS are from Genfusion [43].
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Impact of different components.
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4. Number of versions in multi-sampling strategy. Num. of versions PSNR ↑ SSIM ↑ LPIPS ↓ 1 (No M.S.) 21.779 0.749
- **p. 8 / Figure/Table caption - extractive body cue:** Table 5. Fusion methods in multi-sampling strategy. We com- pare two approaches: (1) ArgMin: selecting pixels with the low- est hallucination score; (2) Weighted Average: ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We first curate training dataset of randomly selected 116 scenes from benchmark dataset for hallucination score network training. | embodiment, simulator version and control stack | p. 6 (5.1. Experimental Setup), p. 6 (5.1. Experimental Setup) |
| Task/environment | This design ensures that no leaked information from the target subset is used for model adaptation, maintaining fair and unbiased comparisons across methods. • ... | reset, timeout, object/scene variation | p. 6 (5.1. Experimental Setup), p. 8 (5.4. Ablation studies) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 3 (3. Preliminary), p. 5 (4.2.2. Hallucination Score Estimation) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 5 (4.2.2. Hallucination Score Estimation), p. 4 (4. Methodology) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 6. Different hallucination score estimators. We use Mean Absolute Error (MAE) of the predicted hallucination score maps as our evaluation metric. We demonstrate ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| We calculate the Mean Absolute Error (MAE) of the predicted hallucination score maps on the test scenes. | definition/direction/unit from same section | p. 8 (5.4. Ablation studies) |
| We first curate training dataset of randomly selected 116 scenes from benchmark dataset for hallucination score network training. | definition/direction/unit from same section | p. 6 (5.1. Experimental Setup) |
| The poses for these augmented views are sampled from views excluded from the 3DGS training set, providing ground-truth images that enable computation of the ... | definition/direction/unit from same section | p. 6 (5.1. Experimental Setup) |
| Notably, LVSM [20], despite producing blurry images, achieves better fidelity, validating our approach of leveraging LVSM's feature backbone as multi-view encoder for hallucination score ... | definition/direction/unit from same section | p. 7 (5.2. In-domain evaluation) |
| Figure 2. Overview of framework - We train 3DGS with input images and HAD-augmented novel views. HAD combines a pretrained diffusion prior (which generates ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| We conduct ablation studies on different components, the number of versions and fusion strategy in the multisampling strategy (M.S.), the pretrained multiview encoder, and ... | definition/direction/unit from same section | p. 7 (5.4. Ablation studies) |
| Figure 1. While diffusion priors [41] enhance the quality of 3D reconstruction, they introduce detrimental aliens - the hallucinated elements that do not exist ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Our method outperforms the baselines by a large margin across all metrics. | comparison identity and matched condition | p. 6 (5.2. In-domain evaluation) |
| Note that GenFusion [43] leverages video diffusion priors that exhibit better multi-view consistency, thereby outperforming baselines using image diffusion priors such as Difix3D. | comparison identity and matched condition | p. 7 (5.3. Cross-domain evaluation) |
| We compare against feedforward NVS networks (DepthSplat [44], LVSM [20]), two variants of 3DGS, and state-of-the-art diffusion prior-assisted 3DGS pipelines (Difix3D [41] and Difix3D+ ... | comparison identity and matched condition | p. 6 (5.2. In-domain evaluation) |
| We compare against baselines including FSGS [52], GenFusion [43] and Difix3D [41]. | comparison identity and matched condition | p. 7 (5.3. Cross-domain evaluation) |
| Similarly, our method without the pretrained multi-view encoder performs worse. | comparison identity and matched condition | p. 8 (5.4. Ablation studies) |
| This comparison demonstrates the importance of leveraging multi-view reasoning ability of a pretrained NVS network. | comparison identity and matched condition | p. 8 (5.4. Ablation studies) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Note that ours* denotes a variant following the twophase 3DGS optimization strategy of Difix3D, enabling a fair comparison between diffusion priors with and without ... | component/input/data sensitivity | p. 6 (5.1. Experimental Setup) |
| We conduct ablation studies on different components, the number of versions and fusion strategy in the multisampling strategy (M.S.), the pretrained multiview encoder, and ... | component/input/data sensitivity | p. 7 (5.4. Ablation studies) |
| Similarly, our method without the pretrained multi-view encoder performs worse. | component/input/data sensitivity | p. 8 (5.4. Ablation studies) |
| We study the performance of three hallucination score estimators: retrained Difix3D, ours without the pretrained multiview encoder, and our full method. | component/input/data sensitivity | p. 8 (5.4. Ablation studies) |
| We compare against feedforward NVS networks (DepthSplat [44], LVSM [20]), two variants of 3DGS, and state-of-the-art diffusion prior-assisted 3DGS pipelines (Difix3D [41] and Difix3D+ ... | component/input/data sensitivity | p. 6 (5.2. In-domain evaluation) |
| Except for the dense view setting where we use 24 views, all ablation studies employ the 9-views setting. | component/input/data sensitivity | p. 7 (5.4. Ablation studies) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To the best of our knowledge, this is the first work to study hallucination score modeling in this context. • We introduce a multi-sampling ... | We select 3 views to achieve a trade-off between marginal improvement and computational overhead. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (5.4. Ablation studies), p. 8 (5.4. Ablation studies), p. 7 (5.3. Cross-domain evaluation), p. 7 (5.4. Ablation studies), p. 1 (Figure/Table caption), p. 6 (5.2. In-domain evaluation) |
| Primary metric/result | We demonstrate that our hallucination score network, with the pretrained multiview encoder, achieves the best performance. | numeric claim only at cited anchor | p. 8 (5.4. Ablation studies) |

- Numeric sentences retained from the body:
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** We first curate training dataset of randomly selected 116 scenes from benchmark dataset for hallucination score network training.
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** To validate the performance of HAD on novel view synthesis, we follow Difix3D [41] to select other 24 scenes for testing.
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** This design ensures that no leaked information from the target subset is used for model adaptation, maintaining fair and unbiased comparisons across methods. • MipNeRF360 ...
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** For each scene, we first train a 3DGS model using 9 input training views, then generate 100 augmented novel views via diffusion priors [41] at ...
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** We fine-tune the network for 10k iterations with a batch size of 2 per GPU, requiring approximately 28 hours on eight NVIDIA V100 32GB GPUs.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In this work, we identify and address a critical limitation in diffusion-assisted 3D reconstruction: while diffusion priors effectively alleviate data sparsity, they introduce hallucinated ... | p. 8 (6. Conclusion and Future Work) |
| body limitation/failure cue | An interesting direction for future work is to scale up the training of our model by removing the need for complex data requirementsfor instance, ... | p. 8 (6. Conclusion and Future Work) |
| body limitation/failure cue | Figure 2. Overview of framework - We train 3DGS with input images and HAD-augmented novel views. HAD combines a pretrained diffusion prior (which generates ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | We primarily use Peak Signal-toNoise Ratio (PSNR), structural (SSIM [39]) and perceptual (LPIPS [50]) similarities as metrics to quantify the performance of novel view ... | p. 6 (5.1. Experimental Setup) |
| body limitation/failure cue | Notably, while the post-rendering improves the photorealism metric (LPIPS), it degrades fidelity metrics (PSNR and SSIM) for both Difix3D and our method. | p. 7 (5.2. In-domain evaluation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We fine-tune the network for 10k iterations with a batch size of 2 per GPU, requiring approximately 28 hours on eight NVIDIA V100 32GB ... | p. 6 (5.1. Experimental Setup) |
| Specifically, unlike Difix3D [41], which employs a two-phase training strategy that first fully trains a 3DGS model and then progressively updates it with diffusion ... | p. 5 (4.1. 3DGS training) |
| For 3DGS training, we set the learning rates to 8e-5 for Gaussian means, 5e-2 for opacity, 1e-3 for rotation, 5e-4 for the 0-th order ... | p. 6 (5.1. Experimental Setup) |
| We follow 3DGS [21] to compute the rendering loss as in at input views by combining L1 and LD-SSIM: Linput = 0.8L1 (RΦ (c) ... | p. 4 (4.1. 3DGS training) |
| Nevertheless, we follow Difix3D [41] in alternating between view augmentation and training steps. | p. 5 (4.1. 3DGS training) |
| Notably, LVSM [20], despite producing blurry images, achieves better fidelity, validating our approach of leveraging LVSM's feature backbone as multi-view encoder for hallucination score ... | p. 7 (5.2. In-domain evaluation) |
| We conduct ablation studies on different components, the number of versions and fusion strategy in the multisampling strategy (M.S.), the pretrained multiview encoder, and ... | p. 7 (5.4. Ablation studies) |
| Similarly, our method without the pretrained multi-view encoder performs worse. | p. 8 (5.4. Ablation studies) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6. Conclusion and Future Work - extractive body cue:** In this work, we identify and address a critical limitation in diffusion-assisted 3D reconstruction: while diffusion priors effectively alleviate data sparsity, they introduce hallucinated content ...
- **p. 8 / 6. Conclusion and Future Work - extractive body cue:** An interesting direction for future work is to scale up the training of our model by removing the need for complex data requirementsfor instance, using ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overview of framework - We train 3DGS with input images and HAD-augmented novel views. HAD combines a pretrained diffusion prior (which generates images ...
- **p. 6 / 5.1. Experimental Setup - extractive body cue:** We primarily use Peak Signal-toNoise Ratio (PSNR), structural (SSIM [39]) and perceptual (LPIPS [50]) similarities as metrics to quantify the performance of novel view synthesis.
- **p. 7 / 5.2. In-domain evaluation - extractive body cue:** Notably, while the post-rendering improves the photorealism metric (LPIPS), it degrades fidelity metrics (PSNR and SSIM) for both Difix3D and our method.

- **Evidence anchors reviewed:** datasets p. 6 (5.1. Experimental Setup), p. 6 (5.1. Experimental Setup), p. 8 (5.4. Ablation studies), p. 7 (5.3. Cross-domain evaluation), p. 8 (5.4. Ablation studies), metrics p. 8 (Figure/Table caption), p. 8 (5.4. Ablation studies), p. 6 (5.1. Experimental Setup), p. 6 (5.1. Experimental Setup), p. 7 (5.2. In-domain evaluation), p. 4 (Figure/Table caption), baselines p. 6 (5.2. In-domain evaluation), p. 7 (5.3. Cross-domain evaluation), p. 6 (5.2. In-domain evaluation), p. 7 (5.3. Cross-domain evaluation), p. 8 (5.4. Ablation studies), p. 8 (5.4. Ablation studies), results p. 8 (5.4. Ablation studies), p. 8 (5.4. Ablation studies), p. 7 (5.3. Cross-domain evaluation), p. 7 (5.4. Ablation studies), p. 1 (Figure/Table caption), p. 6 (5.2. In-domain evaluation).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
