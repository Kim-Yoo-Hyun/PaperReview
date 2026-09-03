# Evaluation - No Pose, No Problem: Surprisingly Simple 3D Gaussian Splats from Sparse Unposed Images

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=P4o9akekdf; public full-text mirror used for retrieval (canonical paper source retained): https://chatpaper.com/api/v1/articles/download/111453. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 21 (Figure/Table caption)): On the other hand, we achieve competitive performance over SOTA pose-required methods (Charatan et al., 2024; Chen et al., 2024), and even outperform them when the overlap between input images ...

## Evaluation Body Digest

- **p. 7 / 4 EXPERIMENTS - extractive body cue:** Small Medium Large Average Method PSNR↑SSIM↑LPIPS↓PSNR↑SSIM↑LPIPS↓PSNR↑SSIM↑LPIPS↓PSNR↑SSIM↑LPIPS↓ PoseRequired pixelNeRF 19.376 0.535 0.564 20.339 0.561 0.537 20.826 0.576 0.509 20.323 0.561 0.533 AttnRend 20.942 0.616 0.398 24.004 ...
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** RE10K primarily contains indoor real estate videos, while ACID features nature scenes captured by aerial drones.
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** To further scale up our model (denoted as Ours*), we also combine RE10K with DL3DV (Ling et al., 2024), which is an outdoor dataset containing ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** The proposed method can be applied to pose estimation between input views on three diverse datasets.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Our method achieves the best results across all datasets.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** We also evaluate the zero-shot performance of the model, where we train exclusively on RealEstate10k and directly apply it to ScanNet++ (Yeshwanth et al., 2023) ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** This advantage arises primarily from our minimal geometric priors in the network structure, allowing it to adapt effectively to various types of scenes.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Ref. pixelSplat MVSplat Ours GT (a) Cross-Dataset Generalize: RE10K →DTU Ref. pixelSplat MVSplat Ours GT (b) Cross-Dataset Generalize: RE10K →ScanNet++ Figure 6: Cross-dataset generalization.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 6); A MORE IMPLEMENTATION DETAILS (p. 15); C MORE EXPERIMENTAL ANALYSIS (p. 17).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | On the other hand, we achieve competitive performance over SOTA pose-required methods (Charatan et al., 2024; Chen et al., 2024), and even outperform them ... | p. 7 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | 13, the performance significantly improves with the inclusion of the additional view. | p. 10 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | 4, NoPoSplat significantly outperforms all SOTA pose-free approaches. | p. 7 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | Our method achieves the best results across all datasets. | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / SOURCE-REPORTED EVALUATION | See the video supplementary for more results. tion method outperforms such pose-required strategy. | p. 10 (4 EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 7 / 4 EXPERIMENTS - extractive body cue:** Small Medium Large Average Method PSNR↑SSIM↑LPIPS↓PSNR↑SSIM↑LPIPS↓PSNR↑SSIM↑LPIPS↓PSNR↑SSIM↑LPIPS↓ PoseRequired pixelNeRF 19.376 0.535 0.564 20.339 0.561 0.537 20.826 0.576 0.509 20.323 0.561 0.533 AttnRend 20.942 0.616 0.398 24.004 ...
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** RE10K primarily contains indoor real estate videos, while ACID features nature scenes captured by aerial drones.
- **p. 6 / 4 EXPERIMENTS - extractive body cue:** To further scale up our model (denoted as Ours*), we also combine RE10K with DL3DV (Ling et al., 2024), which is an outdoor dataset containing ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** The proposed method can be applied to pose estimation between input views on three diverse datasets.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Our method achieves the best results across all datasets.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** We also evaluate the zero-shot performance of the model, where we train exclusively on RealEstate10k and directly apply it to ScanNet++ (Yeshwanth et al., 2023) ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** This advantage arises primarily from our minimal geometric priors in the network structure, allowing it to adapt effectively to various types of scenes.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** Ref. pixelSplat MVSplat Ours GT (a) Cross-Dataset Generalize: RE10K →DTU Ref. pixelSplat MVSplat Ours GT (b) Cross-Dataset Generalize: RE10K →ScanNet++ Figure 6: Cross-dataset generalization.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: NoPoSplat. Given sparse unposed images, our method reconstructs 3D Gaussians of different views in a canonical space using a feed-forward network. The resulting ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: Comparison with pose-required sparse-view 3D Gaussian splatting pipeline. Previ- ous methods first generate Gaussians in each local camera coordinate system and then transform ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3: Overview of NoPoSplat. We directly predict Gaussians in a canonical space from a feed-forward network to represent the underlying 3D scene from the ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 1: Novel view synthesis performance comparison on the RealEstate10k (Zhou et al., 2018) dataset. Our method largely outperforms previous pose-free methods on all overlap ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: Novel view synthesis performance comparison on the ACID (Liu et al., 2021) dataset. Small Medium Large Average
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 4: Qualitative comparison on RE10K (top three rows) and ACID (bottom row). Com- pared to baselines, we obtain: 1) more coherent fusion from input ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: Pose estimation performance in AUC with various thresholds on RE10k, ACID, and ScanNet-1500 (Dai et al., 2017; Sarlin et al., 2020). Our method ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 4: Out-of-distribution performance comparison. Our method shows superior performance when zero-shot evaluation on DTU and ScanNet++ using the model solely trained on RE10k. Training ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Small Medium Large Average Method PSNR↑SSIM↑LPIPS↓PSNR↑SSIM↑LPIPS↓PSNR↑SSIM↑LPIPS↓PSNR↑SSIM↑LPIPS↓ PoseRequired pixelNeRF 19.376 0.535 0.564 20.339 0.561 0.537 20.826 0.576 0.509 20.323 0.561 0.533 AttnRend 20.942 0.616 0.398 ... | embodiment, simulator version and control stack | p. 7 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Task/environment | RE10K primarily contains indoor real estate videos, while ACID features nature scenes captured by aerial drones. | reset, timeout, object/scene variation | p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (3 METHOD), p. 6 (3 METHOD) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 15 (A MORE IMPLEMENTATION DETAILS), p. 5 (3 METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For pose estimation, we report the area under the cumulative pose error curve (AUC) with thresholds of 5◦, 10◦, 20◦(Sarlin et al., 2020; Edstedt ... | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| Our model can better zero-shot transfer to out-ofdistribution data than SOTA pose-required methods. strates superior performance on out-of-distribution data compared to SOTA pose-required methods. | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| To evaluate novel view synthesis, we follow the setting in (Charatan et al., 2024; Chen et al., 2024) and train and evaluate our method ... | definition/direction/unit from same section | p. 6 (4 EXPERIMENTS) |
| To assess the method's capability in handling input images with varying camera overlaps, we generate input pairs for evaluation that are categorized based on ... | definition/direction/unit from same section | p. 6 (4 EXPERIMENTS) |
| 3 shows that the performance consistently improves when scaling up training with DL3DV involved. | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| Our method shows superior performance when zero-shot evaluation on DTU and ScanNet++ using the model solely trained on RE10k. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| Furthermore, our method does not require an explicit matching loss during training, meaning no ground truth depth is necessary. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| To demonstrate the effectiveness of our canonical Gaussian prediction, we compare it with the transform-then-fuse pipeline commonly used by pose-required methods (Charatan et al., ... | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to baselines, we obtain: 1) more coherent fusion from input views, 2) superior reconstruction from limited image overlap, 3) enhanced geometry reconstruction in ... | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| Figure 6: Cross-dataset generalization. Our model can better zero-shot transfer to out-of- distribution data than SOTA pose-required methods. strates superior performance on out-of-distribution data ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| Figure 9: Object-level comparison on Objaverse dataset. Compared with the pose-free baseline method, LEAP, our method shows significantly better novel view synthesis results on ... | comparison identity and matched condition | p. 16 (Figure/Table caption) |
| 4, NoPoSplat significantly outperforms all SOTA pose-free approaches. | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| For a fair comparison with baseline models, we report all quantitative results and baseline comparisons under 256×256. | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| The results show that even without camera poses as input, our method produces higher-quality 3D Gaussians resulting in better color/depth rendering over baselines. | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Figure 8: Ablations. No intrinsic results in blurriness due to scale misalignment. Without the RGB image shortcut, the ren- dered images are blurry in ... | component/input/data sensitivity | p. 10 (Figure/Table caption) |
| Table 7: Ablation on different weight initialization. The results show that our method effectively learns pose-free inference capabilities during training, with appropriate weight initialization ... | component/input/data sensitivity | p. 17 (Figure/Table caption) |
| 7, our method can also be trained with only RGB supervision-without pre-trained weight from MASt3R-and still achieve similar performance. | component/input/data sensitivity | p. 7 (4 EXPERIMENTS) |
| Looking closely, MVSplat not only suffers from the misalignment in the intersection regions of two input images (indicated by blue arrows), but also distortions ... | component/input/data sensitivity | p. 8 (4 EXPERIMENTS) |
| 4.2 ABLATION STUDIES Ablation on Output Gaussian Space. | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| This further shows the benefits of using a standard ViT without incorporating additional geometric operations. | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The main contributions of this work are: • We propose NoPoSplat, a feed-forward network that reconstructs 3D scenes parameterized by 3D Gaussians from unposed ... | On the other hand, we achieve competitive performance over SOTA pose-required methods (Charatan et al., 2024; Chen et al., 2024), and even outperform them ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 21 (Figure/Table caption) |
| Primary metric/result | 13, the performance significantly improves with the inclusion of the additional view. | numeric claim only at cited anchor | p. 10 (4 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** For a fair comparison with baseline models, we report all quantitative results and baseline comparisons under 256×256.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** As shown on the right, our method can predict 3D Gaussians from two 256 × 256 input images in 0.015 seconds (66 fps), which is ...
- **p. 15 / A MORE IMPLEMENTATION DETAILS - extractive body cue:** For the 256 × 256 version of the model, training was conducted on 8 NVIDIA GH200 GPUs (each with >80 GB memory) for approximately 6 ...
- **p. 15 / A MORE IMPLEMENTATION DETAILS - extractive body cue:** While this setup required more time (approximately 90 hours), it achieved comparable performance (PSNR on RE10K: 25.018 with A6000 vs.
- **p. 15 / A MORE IMPLEMENTATION DETAILS - extractive body cue:** For the 256 × 256 version of the model, training was conducted on 8 NVIDIA GH200 GPUs (each with >80 GB memory) for approximately 6 ...
- **p. 15 / A MORE IMPLEMENTATION DETAILS - extractive body cue:** While this setup required more time (approximately 90 hours), it achieved comparable performance (PSNR on RE10K: 25.018 with A6000 vs.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 11: RealEstate10k performance with different number of input views. Addtional Comparison with Splatt3R. In Tab.1 of the main paper, we compare our method ... | p. 19 (Figure/Table caption) |
| body limitation/failure cue | While our method currently applies only to static scenes, extending our pipeline to dynamic scenarios presents an interesting direction for future work. | p. 10 (5 CONCLUSION) |
| body limitation/failure cue | Note that DUSt3R (and MASt3R) struggle to fuse input views coherently due to their reliance on per-pixel depth loss, a limitation Splatt3R also inherits ... | p. 7 (4 EXPERIMENTS) |
| body limitation/failure cue | Figure 2: Comparison with pose-required sparse-view 3D Gaussian splatting pipeline. Previ- ous methods first generate Gaussians in each local camera coordinate system and then ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Furthermore, our method does not require an explicit matching loss during training, meaning no ground truth depth is necessary. | p. 8 (4 EXPERIMENTS) |
| body limitation/failure cue | These issues are largely due to the noises introduced in their transform-then-fuse pipeline. | p. 8 (4 EXPERIMENTS) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We employ the AdamW optimizer (Loshchilov & Hutter, 2018), setting the initial learning rate for the backbone to 2 × 10-5 and other parameters ... | p. 15 (A MORE IMPLEMENTATION DETAILS) |
| We use PyTorch, and the encoder is a vanilla ViT-large model with a patch size of 16, and the decoder is ViT-base. | p. 7 (4 EXPERIMENTS) |
| We initialize the encoder/decoder and Gaussian center head with the weights from MASt3R, while the remaining layers are initialized randomly. | p. 7 (4 EXPERIMENTS) |
| As shown on the right, our method can predict 3D Gaussians from two 256 × 256 input images in 0.015 seconds (66 fps), which ... | p. 9 (4 EXPERIMENTS) |
| We also experimented with training our model on a single A6000 GPU (48 GB memory). | p. 15 (A MORE IMPLEMENTATION DETAILS) |
| 3, comprises three main components: an encoder, a decoder, and Gaussian parameter prediction heads. | p. 4 (3 METHOD) |
| Both encoder and decoder utilize pure Vision Transformer (ViT) structures, without injecting any geometric priors (e.g. epipolar constraints employed in pixelSplat (Charatan et al., ... | p. 4 (3 METHOD) |
| The encoder shares the same weights for different views. | p. 5 (3 METHOD) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 19 / Figure/Table caption - extractive body cue:** Figure 11: RealEstate10k performance with different number of input views. Addtional Comparison with Splatt3R. In Tab.1 of the main paper, we compare our method with ...
- **p. 10 / 5 CONCLUSION - extractive body cue:** While our method currently applies only to static scenes, extending our pipeline to dynamic scenarios presents an interesting direction for future work.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** Note that DUSt3R (and MASt3R) struggle to fuse input views coherently due to their reliance on per-pixel depth loss, a limitation Splatt3R also inherits from ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: Comparison with pose-required sparse-view 3D Gaussian splatting pipeline. Previ- ous methods first generate Gaussians in each local camera coordinate system and then transform ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Furthermore, our method does not require an explicit matching loss during training, meaning no ground truth depth is necessary.
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** These issues are largely due to the noises introduced in their transform-then-fuse pipeline.

- **Evidence anchors reviewed:** datasets p. 7 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), metrics p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 6 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), baselines p. 8 (4 EXPERIMENTS), p. 9 (Figure/Table caption), p. 16 (Figure/Table caption), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), results p. 7 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 10 (4 EXPERIMENTS), p. 21 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
