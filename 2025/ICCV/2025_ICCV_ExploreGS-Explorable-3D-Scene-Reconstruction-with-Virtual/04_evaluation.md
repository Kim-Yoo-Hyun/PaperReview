# Evaluation - ExploreGS: Explorable 3D Scene Reconstruction with Virtual Camera Samplings and Diffusion Priors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Kim_ExploreGS_Explorable_3D_Scene_Reconstruction_with_Virtual_Camera_Samplings_and_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Kim_ExploreGS_Explorable_3D_Scene_Reconstruction_with_Virtual_Camera_Samplings_and_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (5.2. Results), p. 7 (5.2. Results), p. 7 (5.2. Results), p. 8 (5.3. Ablation study), p. 8 (5.3. Ablation study), p. 1 (Figure/Table caption)): Since our method effectively removes artifacts and fills missing regions, as observed in the qualitative analysis, our model outperforms across all metrics, particularly in PSNR and SSIM.

## Evaluation Body Digest

- **p. 6 / 4.1. WildExplore - extractive body cue:** To address the lack of an appropriate benchmark for scene exploration, we introduce WildExplore, a new dataset comprising four indoor and four outdoor scenes.
- **p. 6 / 4.2. Curated Nerfbusters - extractive body cue:** We curate the Nerfbusters dataset to better align with scene exploration objectives.
- **p. 7 / 5.2. Results - extractive body cue:** Qualitative comparison on the curated Nerfbusters dataset.
- **p. 8 / 5.3. Ablation study - extractive body cue:** We validate our finetuning approach by benchmarking it against the methods proposed by [21] , as shown in Table 4.
- **p. 8 / 5.3. Ablation study - extractive body cue:** The model without the imagelevel confidence produces worse results in terms of LPIPS, as generated images whose viewpoints closely match the training set negatively impact ...
- **p. 8 / 5.3. Ablation study - extractive body cue:** TopK vs BottomK Finetuning Curated Nerfbusters Image level Pixel level PSNR↑ SSIM↑ LPIPS↓ Distance [21] - 15.00 0.427 0.443 - Scale [21] 16.18 0.476 0.442 ...
- **p. 8 / 5.3. Ablation study - extractive body cue:** Although both our image-level confidence map and scale based one are effective, our method leads to slight better performance.
- **p. 6 / 4.2. Curated Nerfbusters - extractive body cue:** Our curated version includes seven scenes with swapped splits and two in their original form.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4. Evaluation dataset for scene exploration (p. 6); 5. Experiments (p. 6); 5.1. Experimental Setup (p. 6); 5.2. Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 5.2. Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Since our method effectively removes artifacts and fills missing regions, as observed in the qualitative analysis, our model outperforms across all metrics, particularly in ... | p. 6 (5.2. Results) |
| 5.2. Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | See the supplementary materials for additional results. | p. 7 (5.2. Results) |
| 5.2. Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | Although ViewExtrapolator [19] utilizes a video diffusion prior and thereby shows competitive performance compared to 3DGS variants, it underperforms in challenging scenarios. | p. 7 (5.2. Results) |
| 5.3. Ablation study | EMPIRICAL / SOURCE-REPORTED EVALUATION | As presented in the first and second rows, both show suboptimal results. | p. 8 (5.3. Ablation study) |
| 5.3. Ablation study | EMPIRICAL / SOURCE-REPORTED EVALUATION | Ignoring camera rotation further degrades performance, as observed in the second and fifth rows. | p. 8 (5.3. Ablation study) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. WildExplore - extractive body cue:** To address the lack of an appropriate benchmark for scene exploration, we introduce WildExplore, a new dataset comprising four indoor and four outdoor scenes.
- **p. 6 / 4.2. Curated Nerfbusters - extractive body cue:** We curate the Nerfbusters dataset to better align with scene exploration objectives.
- **p. 7 / 5.2. Results - extractive body cue:** Qualitative comparison on the curated Nerfbusters dataset.
- **p. 8 / 5.3. Ablation study - extractive body cue:** We validate our finetuning approach by benchmarking it against the methods proposed by [21] , as shown in Table 4.
- **p. 8 / 5.3. Ablation study - extractive body cue:** The model without the imagelevel confidence produces worse results in terms of LPIPS, as generated images whose viewpoints closely match the training set negatively impact ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. (a) Explorable 3D scene reconstruction results. Our method renders photorealistic images from any arbitrary viewpoints. (b) Virtual cameras are sampled in regions with ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2. Overview of the proposed framework for scene exploration. (a) The scene is initially optimized using 3DGS on the given training viewpoints. (b) Based ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. (a) Viewpoint candidates for virtual camera viewpoint generation. (b) Information gain of each viewpoint. Simplified 2D examples of both are presented for clarity. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 4. Viewpoint difference comparison with previous 3D re- construction dataset. Training and evaluation viewpoints are visu- alized. LVT = //IT -IV //1 + LD-SSIM(IT ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Qualitative comparison on the curated Nerfbusters dataset. Qualitative comparison. Fig. 5 and Fig. 6 show qualita- tive comparisons among our method and baseline ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 6. Qualitative comparison on the WildExplore dataset. Virtual View Sampling Curated Nerfbusters Info. Gain PSNR↑ SSIM↑ LPIPS↓ Grid view coverage [22]
- **p. 8 / Figure/Table caption - extractive body cue:** Table 2. Comparisons on information gain design. Method (K = 3) Garbage PSNR↑ SSIM↑ LPIPS↓ 3DGS 14.42
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3. Ablation study on information gain. TopK vs BottomK Finetuning Curated Nerfbusters Image level Pixel level PSNR↑ SSIM↑ LPIPS↓

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | To address the lack of an appropriate benchmark for scene exploration, we introduce WildExplore, a new dataset comprising four indoor and four outdoor scenes. | embodiment, simulator version and control stack | p. 6 (4.1. WildExplore), p. 6 (4.2. Curated Nerfbusters) |
| Task/environment | We curate the Nerfbusters dataset to better align with scene exploration objectives. | reset, timeout, object/scene variation | p. 6 (4.2. Curated Nerfbusters), p. 7 (5.2. Results) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 3 (3.1. Overview), p. 3 (3.2. Scene initialization) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 2 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| TopK vs BottomK Finetuning Curated Nerfbusters Image level Pixel level PSNR↑ SSIM↑ LPIPS↓ Distance [21] - 15.00 0.427 0.443 - Scale [21] 16.18 0.476 ... | definition/direction/unit from same section | p. 8 (5.3. Ablation study) |
| Although both our image-level confidence map and scale based one are effective, our method leads to slight better performance. | definition/direction/unit from same section | p. 8 (5.3. Ablation study) |
| We curate the Nerfbusters dataset to better align with scene exploration objectives. | definition/direction/unit from same section | p. 6 (4.2. Curated Nerfbusters) |
| Our curated version includes seven scenes with swapped splits and two in their original form. | definition/direction/unit from same section | p. 6 (4.2. Curated Nerfbusters) |
| Qualitative comparison on the curated Nerfbusters dataset. | definition/direction/unit from same section | p. 7 (5.2. Results) |
| We validate the effectiveness of our information gain design by comparing it with alternative strategies, as shown in Table 2. | definition/direction/unit from same section | p. 7 (5.3. Ablation study) |
| Figure 1. (a) Explorable 3D scene reconstruction results. Our method renders photorealistic images from any arbitrary viewpoints. (b) Virtual cameras are sampled in regions ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 3. (a) Viewpoint candidates for virtual camera viewpoint generation. (b) Information gain of each viewpoint. Simplified 2D examples of both are presented for ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 6 show qualitative comparisons among our method and baseline methods. | comparison identity and matched condition | p. 7 (5.2. Results) |
| Since our method effectively removes artifacts and fills missing regions, as observed in the qualitative analysis, our model outperforms across all metrics, particularly in ... | comparison identity and matched condition | p. 6 (5.2. Results) |
| Although ViewExtrapolator [19] utilizes a video diffusion prior and thereby shows competitive performance compared to 3DGS variants, it underperforms in challenging scenarios. | comparison identity and matched condition | p. 7 (5.2. Results) |
| We evaluate our method in comparison to 3DGS-based methods, including 3DGS [11], 3DGS + Depth, DNGaussians [15], and ViewExtrapolator [19]. | comparison identity and matched condition | p. 6 (5.1. Experimental Setup) |
| Ablation study on information gain. | comparison identity and matched condition | p. 8 (5.3. Ablation study) |
| Ablations study on finetuning methods. | comparison identity and matched condition | p. 8 (5.3. Ablation study) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Since our method effectively removes artifacts and fills missing regions, as observed in the qualitative analysis, our model outperforms across all metrics, particularly in ... | component/input/data sensitivity | p. 6 (5.2. Results) |
| In contrast, our method fills missing regions and removes artifacts more effectively, producing images that align closely with the ground truth. | component/input/data sensitivity | p. 7 (5.2. Results) |
| Figure 3. (a) Viewpoint candidates for virtual camera viewpoint generation. (b) Information gain of each viewpoint. Simplified 2D examples of both are presented for ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| 3DGS [11] suffers from artifacts, and its variants with depth regularization also meet the same problem, as they lack the capability to fill missing ... | component/input/data sensitivity | p. 7 (5.2. Results) |
| Ablation study on information gain. | component/input/data sensitivity | p. 8 (5.3. Ablation study) |
| Ablations study on finetuning methods. | component/input/data sensitivity | p. 8 (5.3. Ablation study) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our contributions can be organized as follows: • We propose a pipeline for explorable 3D scene reconstruction, which incorporates the real-time rendering ... | Since our method effectively removes artifacts and fills missing regions, as observed in the qualitative analysis, our model outperforms across all metrics, particularly in ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (5.2. Results), p. 7 (5.2. Results), p. 7 (5.2. Results), p. 8 (5.3. Ablation study), p. 8 (5.3. Ablation study), p. 1 (Figure/Table caption) |
| Primary metric/result | See the supplementary materials for additional results. | numeric claim only at cited anchor | p. 7 (5.2. Results) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In addition, extending the scene bounding box to cover a large scale scene would be an interesting avenue for the future work. | p. 8 (6. Conclusion) |
| body limitation/failure cue | Gridbased approach often fails to maximize information gain, as it includes the gain from free space, resulting in redundant viewpoint selections. | p. 8 (5.3. Ablation study) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| At each step, we select the top 3 candidate views based on computed information gain. | p. 6 (5.1. Experimental Setup) |
| 3DGS + Depth applies additional depth regularization using monocular depth estimation [44], following the implementation from the official 3DGS repository [11]. | p. 6 (5.1. Experimental Setup) |
| This bounding box is computed by using the mesh extracted from the initial 3D Gaussians and the given cameras. | p. 3 (3.2. Scene initialization) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 6. Conclusion - extractive body cue:** In addition, extending the scene bounding box to cover a large scale scene would be an interesting avenue for the future work.
- **p. 8 / 5.3. Ablation study - extractive body cue:** Gridbased approach often fails to maximize information gain, as it includes the gain from free space, resulting in redundant viewpoint selections.

- **Evidence anchors reviewed:** datasets p. 6 (4.1. WildExplore), p. 6 (4.2. Curated Nerfbusters), p. 7 (5.2. Results), p. 8 (5.3. Ablation study), p. 8 (5.3. Ablation study), metrics p. 8 (5.3. Ablation study), p. 8 (5.3. Ablation study), p. 6 (4.2. Curated Nerfbusters), p. 6 (4.2. Curated Nerfbusters), p. 7 (5.2. Results), p. 7 (5.3. Ablation study), baselines p. 7 (5.2. Results), p. 6 (5.2. Results), p. 7 (5.2. Results), p. 6 (5.1. Experimental Setup), p. 8 (5.3. Ablation study), p. 8 (5.3. Ablation study), results p. 6 (5.2. Results), p. 7 (5.2. Results), p. 7 (5.2. Results), p. 8 (5.3. Ablation study), p. 8 (5.3. Ablation study), p. 1 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
