# Evaluation - TokenSplat: Token-aligned 3D Gaussian Splatting for Feed-forward Pose-free Reconstruction

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Li_TokenSplat_Token-aligned_3D_Gaussian_Splatting_for_Feed-forward_Pose-free_Reconstruction_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Li_TokenSplat_Token-aligned_3D_Gaussian_Splatting_for_Feed-forward_Pose-free_Reconstruction_CVPR_2026_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2. Experimental Results), p. 5 (4.2. Experimental Results), p. 5 (4.2. Experimental Results), p. 6 (4.2. Experimental Results), p. 8 (4.3. Ablation Analysis), p. 7 (4.2. Experimental Results)): Moreover, as the number of input images increases, our model achieves a higher SSIM of 0.061 over FreeSplat, while also showing improved novel view synthesis quality.

## Evaluation Body Digest

- **p. 5 / 4. Experiment - extractive PDF cue:** We evaluate our method on novel view synthesis (NVS) and camera pose estimation across sparse and long-sequence real-world datasets.
- **p. 6 / 4.2. Experimental Results - extractive PDF cue:** Notably, fine details such as furniture boundaries are better preserved than in competing methods, demonstrating the effectiveness of our method across unseen scenes.
- **p. 5 / 4.1. Experimental Settings - extractive PDF cue:** Following [23], we train and evaluate on RE10K under both 4-view and 8-view reference settings, and further perform cross-dataset generalization tests on ScanNet.
- **p. 6 / 4.2. Experimental Results - extractive PDF cue:** Quantitative results of NVS on RE10K with varying reference views (left) and cross-dataset generalization to ScanNet (right).
- **p. 8 / 4.2. Experimental Results - extractive PDF cue:** Scene-level visualizations and multiple novel viewpoints renderings.
- **p. 5 / 4.1. Experimental Settings - extractive PDF cue:** For camera pose estimation, we report Absolute Translation Error (ATE), Relative Translation Error (RPE-t), and Relative Rotation Error (RPE-r).
- **p. 6 / 4.2. Experimental Results - extractive PDF cue:** On ScanNet, the model maintains accurate pose estimation under the 28-view setting, reducing ATE by 0.018 over AnySplat, confirming both robustness and scalability of TokenSplat ...
- **p. 5 / 4.1. Experimental Settings - extractive PDF cue:** We evaluate NVS performance using PSNR, SSIM [39], and LPIPS [48].

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiment (p. 5); 4.1. Experimental Settings (p. 5); 4.2. Experimental Results (p. 5).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Experimental Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Moreover, as the number of input images increases, our model achieves a higher SSIM of 0.061 over FreeSplat, while also showing improved novel view ... | p. 6 (4.2. Experimental Results) |
| 4.2. Experimental Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Here, AnySplat refers to zero-shot results trained on other datasets, while AnySplat∗ denotes the results we achieved after fine-tuning on the corresponding dataset. | p. 5 (4.2. Experimental Results) |
| 4.2. Experimental Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | As can be seen, TokenSplat consistently outperforms state-of-the-art pose-free methods, including those specifically designed for multi-view input such as VicaSplat and AnySplat, which leverage ... | p. 5 (4.2. Experimental Results) |
| 4.2. Experimental Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | Compared to FreeSplat, TokenSplat achieves up to 0.92/0.51 dB higher PSNR, and reduces ATE by 0.013/0.033 over SPFSplat. | p. 6 (4.2. Experimental Results) |
| 4.3. Ablation Analysis | EMPIRICAL / REAL-ROBOT OR HARDWARE | Compared to our full model (a), (b) replacing the Token-aligned Gaussian Prediction with a pixelaligned Gaussian head degrades both reconstruction and pose estimation, with ... | p. 8 (4.3. Ablation Analysis) |

## Dataset / Benchmark Role

- **p. 5 / 4. Experiment - extractive PDF cue:** We evaluate our method on novel view synthesis (NVS) and camera pose estimation across sparse and long-sequence real-world datasets.
- **p. 6 / 4.2. Experimental Results - extractive PDF cue:** Notably, fine details such as furniture boundaries are better preserved than in competing methods, demonstrating the effectiveness of our method across unseen scenes.
- **p. 5 / 4.1. Experimental Settings - extractive PDF cue:** Following [23], we train and evaluate on RE10K under both 4-view and 8-view reference settings, and further perform cross-dataset generalization tests on ScanNet.
- **p. 6 / 4.2. Experimental Results - extractive PDF cue:** Quantitative results of NVS on RE10K with varying reference views (left) and cross-dataset generalization to ScanNet (right).
- **p. 8 / 4.2. Experimental Results - extractive PDF cue:** Scene-level visualizations and multiple novel viewpoints renderings.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 1. Overview of TokenSplat. TokenSplat performs feed-forward 3D Gaussian reconstruction and camera pose estimation from unposed images. A shared ViT encoder extracts image tokens, ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Quantitative results of NVS on RE10K with varying reference views (left) and cross-dataset generalization to ScanNet (right). The best and second-best values are ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Quantitative results of NVS on ScanNet under varying numbers of views. The best and second-best values are highlighted.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 2. Qualitative comparison on RE10K and ScanNet under varying numbers of reference views.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 3. Cross-dataset generalization from RE10K to ScanNet.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Quantitative results of pose prediction on RE10K with diverse views (left) and cross-dataset generalization to ScanNet (right).
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 4. Quantitative results of pose prediction on ScanNet with diverse views. The best and second-best values are highlighted.
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 4. Scene-level visualizations and multiple novel viewpoints renderings.

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | We evaluate our method on novel view synthesis (NVS) and camera pose estimation across sparse and long-sequence real-world datasets. | embodiment, simulator version and control stack | p. 5 (4. Experiment), p. 6 (4.2. Experimental Results) |
| Task/environment | Notably, fine details such as furniture boundaries are better preserved than in competing methods, demonstrating the effectiveness of our method across unseen scenes. | reset, timeout, object/scene variation | p. 6 (4.2. Experimental Results), p. 5 (4.1. Experimental Settings) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3.1. Problem Formulation), p. 1 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 3 (3.2. Architecture), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For camera pose estimation, we report Absolute Translation Error (ATE), Relative Translation Error (RPE-t), and Relative Rotation Error (RPE-r). | definition/direction/unit from same section | p. 5 (4.1. Experimental Settings) |
| On ScanNet, the model maintains accurate pose estimation under the 28-view setting, reducing ATE by 0.018 over AnySplat, confirming both robustness and scalability of ... | definition/direction/unit from same section | p. 6 (4.2. Experimental Results) |
| We evaluate NVS performance using PSNR, SSIM [39], and LPIPS [48]. | definition/direction/unit from same section | p. 5 (4.1. Experimental Settings) |
| To further illustrate the reconstruction quality, Fig. | definition/direction/unit from same section | p. 6 (4.2. Experimental Results) |
| Overall, these results demonstrate the effectiveness of our model designs for accurate multi-view reconstruction and camera pose estimation. | definition/direction/unit from same section | p. 8 (4.3. Ablation Analysis) |
| Figure 1. Overview of TokenSplat. TokenSplat performs feed-forward 3D Gaussian reconstruction and camera pose estimation from unposed images. A shared ViT encoder extracts image ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As can be seen, TokenSplat consistently outperforms state-of-the-art pose-free methods, including those specifically designed for multi-view input such as VicaSplat and AnySplat, which leverage ... | comparison identity and matched condition | p. 5 (4.2. Experimental Results) |
| TokenSplat consistently surpasses pose-free baselines on RE10K, reducing RPE-r (lower is better) by 0.335 and 0.147 compared to VicaSplat and AnySplat under the 8-view ... | comparison identity and matched condition | p. 6 (4.2. Experimental Results) |
| Compared to our full model (a), (b) replacing the Token-aligned Gaussian Prediction with a pixelaligned Gaussian head degrades both reconstruction and pose estimation, with ... | comparison identity and matched condition | p. 8 (4.3. Ablation Analysis) |
| Compared to FreeSplat, TokenSplat achieves up to 0.92/0.51 dB higher PSNR, and reduces ATE by 0.013/0.033 over SPFSplat. | comparison identity and matched condition | p. 6 (4.2. Experimental Results) |
| Both settings ensure a direct and consistent comparison with prior work. | comparison identity and matched condition | p. 5 (4.1. Experimental Settings) |
| Qualitative comparison on RE10K and ScanNet under varying numbers of reference views. | comparison identity and matched condition | p. 7 (4.2. Experimental Results) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Component ablations on RE10K (8 view). | component/input/data sensitivity | p. 8 (4.2. Experimental Results) |
| We perform ablation studies on RE10K (8 views), summarized in Tab. | component/input/data sensitivity | p. 8 (4.3. Ablation Analysis) |
| Here, AnySplat refers to zero-shot results trained on other datasets, while AnySplat∗ denotes the results we achieved after fine-tuning on the corresponding dataset. | component/input/data sensitivity | p. 5 (4.2. Experimental Results) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our main contributions are as follows: • We propose TokenSplat, a feed-forward pose-free reconstruction framework that jointly estimates camera poses and 3D ... | Moreover, as the number of input images increases, our model achieves a higher SSIM of 0.061 over FreeSplat, while also showing improved novel view ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2. Experimental Results), p. 5 (4.2. Experimental Results), p. 5 (4.2. Experimental Results), p. 6 (4.2. Experimental Results), p. 8 (4.3. Ablation Analysis), p. 7 (4.2. Experimental Results) |
| Primary metric/result | Here, AnySplat refers to zero-shot results trained on other datasets, while AnySplat∗ denotes the results we achieved after fine-tuning on the corresponding dataset. | numeric claim only at cited anchor | p. 5 (4.2. Experimental Results) |

- Numeric sentences retained from the body:
- no numeric body cue

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | It yields consistent accuracy improvements and robust zero-shot generalization across diverse datasets. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Despite the difference in view counts, TokenSplat maintains stable reconstruction quality, while competing methods, including AnySplat, which fuses pixel-aligned Gaussians by predicting fusion confidence, ... | p. 5 (4.2. Experimental Results) |
| body limitation/failure cue | FreeSplat generates numerous scattered Gaussians, while NoPoSplat and SPFSplat show poor scalability and fail to generalize to unseen distant viewpoints. | p. 6 (4.2. Experimental Results) |
| body limitation/failure cue | On ScanNet, the model maintains accurate pose estimation under the 28-view setting, reducing ATE by 0.018 over AnySplat, confirming both robustness and scalability of ... | p. 6 (4.2. Experimental Results) |
| body limitation/failure cue | Compared to our full model (a), (b) replacing the Token-aligned Gaussian Prediction with a pixelaligned Gaussian head degrades both reconstruction and pose estimation, with ... | p. 8 (4.3. Ablation Analysis) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The encoder follows [44] and adopts a ViTLarge backbone with a patch size of 16. | p. 5 (4.1. Experimental Settings) |
| We initialize the encoder-decoder and Gaussian center head with MASt3R [20] weights, while the ADF-Decoder and remaining heads are randomly initialized. | p. 5 (4.1. Experimental Settings) |
| This gain stems from our directionally constrained ADF-Decoder, which enforces disentangled interaction between camera and image tokens, leading to more stable pose learning. | p. 6 (4.2. Experimental Results) |
| Compared to our full model (a), (b) replacing the Token-aligned Gaussian Prediction with a pixelaligned Gaussian head degrades both reconstruction and pose estimation, with ... | p. 8 (4.3. Ablation Analysis) |
| Image tokens are generated by the shared ViT encoder. | p. 3 (3.3. Asymmetric Dual-Flow Decoder) |
| At each decoder layer, camera tokens interact with the cor40888 | p. 3 (3.3. Asymmetric Dual-Flow Decoder) |
| The ADF-Decoder consists of 12 decoder blocks. | p. 4 (3.3. Asymmetric Dual-Flow Decoder) |
| The updates are computed as: ˆtI i ←Softmax  QI iKI i ⊤/ √ d  | p. 4 (3.3. Asymmetric Dual-Flow Decoder) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 8 / 5. Conclusion - extractive PDF cue:** It yields consistent accuracy improvements and robust zero-shot generalization across diverse datasets.
- **p. 5 / 4.2. Experimental Results - extractive PDF cue:** Despite the difference in view counts, TokenSplat maintains stable reconstruction quality, while competing methods, including AnySplat, which fuses pixel-aligned Gaussians by predicting fusion confidence, and ...
- **p. 6 / 4.2. Experimental Results - extractive PDF cue:** FreeSplat generates numerous scattered Gaussians, while NoPoSplat and SPFSplat show poor scalability and fail to generalize to unseen distant viewpoints.
- **p. 6 / 4.2. Experimental Results - extractive PDF cue:** On ScanNet, the model maintains accurate pose estimation under the 28-view setting, reducing ATE by 0.018 over AnySplat, confirming both robustness and scalability of TokenSplat ...
- **p. 8 / 4.3. Ablation Analysis - extractive PDF cue:** Compared to our full model (a), (b) replacing the Token-aligned Gaussian Prediction with a pixelaligned Gaussian head degrades both reconstruction and pose estimation, with SSIM ...

- **PDF anchors reviewed:** datasets p. 5 (4. Experiment), p. 6 (4.2. Experimental Results), p. 5 (4.1. Experimental Settings), p. 6 (4.2. Experimental Results), p. 8 (4.2. Experimental Results), metrics p. 5 (4.1. Experimental Settings), p. 6 (4.2. Experimental Results), p. 5 (4.1. Experimental Settings), p. 6 (4.2. Experimental Results), p. 8 (4.3. Ablation Analysis), p. 3 (Figure/Table caption), baselines p. 5 (4.2. Experimental Results), p. 6 (4.2. Experimental Results), p. 8 (4.3. Ablation Analysis), p. 6 (4.2. Experimental Results), p. 5 (4.1. Experimental Settings), p. 7 (4.2. Experimental Results), results p. 6 (4.2. Experimental Results), p. 5 (4.2. Experimental Results), p. 5 (4.2. Experimental Results), p. 6 (4.2. Experimental Results), p. 8 (4.3. Ablation Analysis), p. 7 (4.2. Experimental Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
