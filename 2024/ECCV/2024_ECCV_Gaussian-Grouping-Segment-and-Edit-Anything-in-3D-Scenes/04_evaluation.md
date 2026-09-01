# Evaluation - Gaussian Grouping: Segment and Edit Anything in 3D Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/4195_ECCV_2024_paper.php; PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/04195.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 11 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments)): 6 and Table 2, K = 5 achieves both the best balance between the scene reconstruction and 3D object removal accuracy.

## Evaluation Body Digest

- **p. 12 / 4 Experiments - extractive PDF cue:** Also, our approach is better at distinguishing objects with similar colors, such as the "Green apple" prompt case. compare fine-grained mask localization quality, we annotate ...
- **p. 9 / 4 Experiments - extractive PDF cue:** 4.1 Dataset and Experiment Setup Datasets To measure segmentation or fine-grained localization accuracy in open-world scene, we evolve the existing LERF-Localization [15] evaluation dataset and ...
- **p. 13 / 4 Experiments - extractive PDF cue:** Gaussian Grouping: Segment and Edit Anything in 3D Scenes 13 Table 3: Comparison of Open Vocabulary Segmentation on LERF-Mask dataset.
- **p. 13 / 4 Experiments - extractive PDF cue:** 9: 3D Object removal on the Tanks & Temples dataset [17].
- **p. 9 / 4 Experiments - extractive PDF cue:** All datasets are trained for 30K iterations on one A100 GPU.
- **p. 11 / 4 Experiments - extractive PDF cue:** Gaussian Grouping: Segment and Edit Anything in 3D Scenes 11 Rendered Image K=1 K=5 K=10 K=5 + Post process K=0 Fig.
- **p. 11 / 4 Experiments - extractive PDF cue:** Ablation of 3D Regularization Loss We perform ablation of K in our 3D Regularization Loss on the Kitchen dataset of Mip-NeRF 360 [1] to select ...
- **p. 12 / 4 Experiments - extractive PDF cue:** In Table 3, the advantage of our Gaussian Grouping is significant, doubling the performance of LERF and SA3D on both the "figurines" and "ramen" scenes.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4 Experiments (p. 9).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | 6 and Table 2, K = 5 achieves both the best balance between the scene reconstruction and 3D object removal accuracy. | p. 11 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | Gaussian Grouping outperforms Panoptic Lifting in both performance and speed. | p. 12 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | While the performance of DFFs is limited by the quality of its CLIP-distilled features, which results in the complete foreground removal (Train case) or ... | p. 12 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | We also provide 3D panoptic segmentation results on Replica [44] and ScanNet [8] dataset. | p. 9 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | We take the cost-based linear assignment strategy proposed in [43], and perform the visual comparison on rendering results in Figure 4. | p. 9 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 12 / 4 Experiments - extractive PDF cue:** Also, our approach is better at distinguishing objects with similar colors, such as the "Green apple" prompt case. compare fine-grained mask localization quality, we annotate ...
- **p. 9 / 4 Experiments - extractive PDF cue:** 4.1 Dataset and Experiment Setup Datasets To measure segmentation or fine-grained localization accuracy in open-world scene, we evolve the existing LERF-Localization [15] evaluation dataset and ...
- **p. 13 / 4 Experiments - extractive PDF cue:** Gaussian Grouping: Segment and Edit Anything in 3D Scenes 13 Table 3: Comparison of Open Vocabulary Segmentation on LERF-Mask dataset.
- **p. 13 / 4 Experiments - extractive PDF cue:** 9: 3D Object removal on the Tanks & Temples dataset [17].
- **p. 9 / 4 Experiments - extractive PDF cue:** All datasets are trained for 30K iterations on one A100 GPU.
- **p. 11 / 4 Experiments - extractive PDF cue:** Gaussian Grouping: Segment and Edit Anything in 3D Scenes 11 Rendered Image K=1 K=5 K=10 K=5 + Post process K=0 Fig.
- **p. 11 / 4 Experiments - extractive PDF cue:** Ablation of 3D Regularization Loss We perform ablation of K in our 3D Regularization Loss on the Kitchen dataset of Mip-NeRF 360 [1] to select ...
- **p. 12 / 4 Experiments - extractive PDF cue:** In Table 3, the advantage of our Gaussian Grouping is significant, doubling the performance of LERF and SA3D on both the "figurines" and "ramen" scenes.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Fig. 1: Our Gaussian Grouping jointly reconstructs (column a) and segments (column b) anything in full open-world 3D scenes, with fine-grained instance and stuff level ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Fig. 2: The method pipeline of our Gaussian Grouping contains three main steps: (a) We first prepare the input by deploying SAM to automatically generate ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Fig. 3: The grouped 3D Gaussians after training, where each group represents a specific instance / stuff of the 3D scene and can be fully ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Fig. 4: Ablation on the Identity Con- sistency across views, where we treat multi-view images as a video and as- sociate the mask labels to ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Fig. 5: Robustness to input masks errors on Mip-NeRF 360 [1]. In the 2nd and 3rd columns (middle two views), SAM + DEVA fails to ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 1: Influence of Identity Encoding on Mip-NeRF 360 [1] dataset with its 7 public scenes. The joint train- ing of the introduced Identity Encodings ...
- **p. 10 / Figure/Table caption - extractive PDF cue:** Table 2: Ablation of K of 3D Regularization Loss on the 3D object removal. RAcc: Object Removal Accuracy. Model Gaussian Splatting Gaussian Grouping K=0 K=1
- **p. 11 / Figure/Table caption - extractive PDF cue:** Fig. 6: Visual ablation of K in the 3D Regularization Loss on object removal editing of MipNeRF360. We remove Gaussians classified as lego with various ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Also, our approach is better at distinguishing objects with similar colors, such as the "Green apple" prompt case. compare fine-grained mask localization quality, we ... | embodiment, simulator version and control stack | p. 12 (4 Experiments), p. 9 (4 Experiments) |
| Task/environment | 4.1 Dataset and Experiment Setup Datasets To measure segmentation or fine-grained localization accuracy in open-world scene, we evolve the existing LERF-Localization [15] evaluation dataset ... | reset, timeout, object/scene variation | p. 9 (4 Experiments), p. 13 (4 Experiments) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 5 (3 Method), p. 5 (3 Method) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1 Introduction), p. 6 (3 Method) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| 4.1 Dataset and Experiment Setup Datasets To measure segmentation or fine-grained localization accuracy in open-world scene, we evolve the existing LERF-Localization [15] evaluation dataset ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| 5: Robustness to input masks errors on Mip-NeRF 360 [1]. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| Masks Association Errors Correction and Robustness Gaussian Grouping can also correct the 2D segmentation errors produced by DEVA, as shown in Figure 5. | definition/direction/unit from same section | p. 10 (4 Experiments) |
| The joint supervision of 2D and 3D losses addresses the "transparent bear issue", which shows better Gaussian Grouping accuracy. | definition/direction/unit from same section | p. 11 (4 Experiments) |
| 6 and Table 2, K = 5 achieves both the best balance between the scene reconstruction and 3D object removal accuracy. | definition/direction/unit from same section | p. 11 (4 Experiments) |
| While the performance of DFFs is limited by the quality of its CLIP-distilled features, which results in the complete foreground removal (Train case) or ... | definition/direction/unit from same section | p. 12 (4 Experiments) |
| For 3D regularization loss, we choose k = 5 and m = 1000. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| Gaussian Grouping outperforms Panoptic Lifting in both performance and speed. | definition/direction/unit from same section | p. 12 (4 Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Model Scene Seg Scene Edit PSNR↑SSIM↑LPIPS↓FPS Baseline: Gaussian Splatting [14] - - 28.69 0.870 0.182 ∼200 Gaussian Grouping ✓ ✓ 28.43 0.863 0.189 ∼170 ... | comparison identity and matched condition | p. 10 (4 Experiments) |
| 4.3 3D Multi-view Segmentation Open-vocabulary Segmentation Comparison We compare the segmentation quality of Gaussian Grouping in 3D scenes with the state-of-the-art openvocabulary 3D segmentation ... | comparison identity and matched condition | p. 11 (4 Experiments) |
| Doubling the dimension to 32 does not bring a better reconstruction quality compared to 16 but make training 1.3 times slower. | comparison identity and matched condition | p. 11 (4 Experiments) |
| Gaussian Grouping outperforms Panoptic Lifting in both performance and speed. | comparison identity and matched condition | p. 12 (4 Experiments) |
| In Figure 10, compared to SPIn-NeRF [33], the inpainting result of our Gaussian Grouping better preserves spatial detail and multi-view coherence. | comparison identity and matched condition | p. 13 (4 Experiments) |
| Compared to DFFs [18], our Gaussian Grouping can remove the large-scale objects, such as truck, from the 3D scene with greatly reduced artifacts w/o ... | comparison identity and matched condition | p. 13 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 4.2 Ablation Experiments Ablation on Mask Cross-view Association To study the effect of cross-view masks association [7] for input preparation, we replace the associated ... | component/input/data sensitivity | p. 9 (4 Experiments) |
| Visual Ablation on the Grouping Losses In Figure 7, we study the effect of our grouping loss components, where solely using 2D Identity Loss ... | component/input/data sensitivity | p. 11 (4 Experiments) |
| Fig. 6: Visual ablation of K in the 3D Regularization Loss on object removal editing of MipNeRF360. We remove Gaussians classified as lego with ... | component/input/data sensitivity | p. 11 (Figure/Table caption) |
| In Figure 9, we compare the removal effect of our Gaussian Grouping with the Distilled Feature Fields (DFFs) [18]. | component/input/data sensitivity | p. 12 (4 Experiments) |
| Fig. 1: Our Gaussian Grouping jointly reconstructs (column a) and segments (column b) anything in full open-world 3D scenes, with fine-grained instance and stuff ... | component/input/data sensitivity | p. 1 (Figure/Table caption) |
| 4: Ablation on the Identity Consistency across views, where we treat multi-view images as a video and associate the mask labels to generate coherent ... | component/input/data sensitivity | p. 10 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To our knowledge, we propose the first Gaussian-based method to tackle open-world 3D scene understanding, where we show the advantages compared to existing NeRF-based ... | 6 and Table 2, K = 5 achieves both the best balance between the scene reconstruction and 3D object removal accuracy. | PDF body cue; verify exact table/figure and matched conditions | p. 11 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments) |
| Primary metric/result | Gaussian Grouping outperforms Panoptic Lifting in both performance and speed. | numeric claim only at cited anchor | p. 12 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 10 / 4 Experiments - extractive PDF cue:** GT Image Rendered Image Rendered Mask Cost-based Linear Assignment (2K Iterations, training time: > 1 hour) Our Zero-shot Mask Association (2K Iterations, training time: 1 ...
- **p. 10 / 4 Experiments - extractive PDF cue:** For 2K training iteration, linear assignment requires 1 hour but our associated mask input only requires 1 minute.
- **p. 13 / 4 Experiments - extractive PDF cue:** 10: Comparison on 3D object inpainting cases, where SPIn-NeRF [33] requires 5h training while our method with better inpainting quality only needs 1 hour training ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Fig. 5: Robustness to input masks errors on Mip-NeRF 360 [1]. In the 2nd and 3rd columns (middle two views), SAM + DEVA fails ... | p. 10 (Figure/Table caption) |
| body limitation/failure cue | Model Gaussian Splatting Gaussian Grouping K=0 K=1 k=2 K=5 K=10 PSNR 30.32 30.51 30.62 30.61 30.72 30.62 RAcc N/A 41.2% 40.5% 67.5% 76.6% 77.8% ... | p. 10 (4 Experiments) |
| body limitation/failure cue | This is due to Gaussians inside the bear being occluded during training and cannot be supervised sufficiently. | p. 11 (4 Experiments) |
| body limitation/failure cue | Limitation Due to the lack of dynamic modeling and time-dependent updating, Gaussian Grouping is currently limited to the static 3D scene. | p. 14 (4 Experiments) |
| body limitation/failure cue | Doubling the dimension to 32 does not bring a better reconstruction quality compared to 16 but make training 1.3 times slower. | p. 11 (4 Experiments) |
| body limitation/failure cue | Since SAM does not support language prompts, both SA3D and our method adopt Grounding DINO [25] to identify the mask ID in a 2D ... | p. 12 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We use the Adam optimizer for both Gaussians and the linear layer, with a learning rate of 2.5e-3 for identity encoding and 5e-4 for ... | p. 9 (4 Experiments) |
| GT Image Rendered Image Rendered Mask Cost-based Linear Assignment (2K Iterations, training time: > 1 hour) Our Zero-shot Mask Association (2K Iterations, training time: ... | p. 10 (4 Experiments) |
| All datasets are trained for 30K iterations on one A100 GPU. | p. 9 (4 Experiments) |
| We compute the convex hull of the removed 3D Gaussian points as the post process. | p. 11 (4 Experiments) |
| We then detail the input data pre-processing steps and further describe the proposed Gaussian Grouping in Section 3.2. | p. 5 (3 Method) |
| 2: The method pipeline of our Gaussian Grouping contains three main steps: (a) We first prepare the input by deploying SAM to automatically generate ... | p. 6 (3 Method) |
| To optimize the introduced Identity Encoding of each Gaussian, in Figure 2(c), we render these encoded identity vectors into 2D images in a differentiable ... | p. 7 (3 Method) |
| Refer to [60], we compute α′ i by measuring a 2D Gaussian with covariance Σ2D multiplied with a learned per-point opacity αi, and \ ... | p. 7 (3 Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 10 / Figure/Table caption - extractive PDF cue:** Fig. 5: Robustness to input masks errors on Mip-NeRF 360 [1]. In the 2nd and 3rd columns (middle two views), SAM + DEVA fails to ...
- **p. 10 / 4 Experiments - extractive PDF cue:** Model Gaussian Splatting Gaussian Grouping K=0 K=1 k=2 K=5 K=10 PSNR 30.32 30.51 30.62 30.61 30.72 30.62 RAcc N/A 41.2% 40.5% 67.5% 76.6% 77.8% to ...
- **p. 11 / 4 Experiments - extractive PDF cue:** This is due to Gaussians inside the bear being occluded during training and cannot be supervised sufficiently.
- **p. 14 / 4 Experiments - extractive PDF cue:** Limitation Due to the lack of dynamic modeling and time-dependent updating, Gaussian Grouping is currently limited to the static 3D scene.
- **p. 11 / 4 Experiments - extractive PDF cue:** Doubling the dimension to 32 does not bring a better reconstruction quality compared to 16 but make training 1.3 times slower.
- **p. 12 / 4 Experiments - extractive PDF cue:** Since SAM does not support language prompts, both SA3D and our method adopt Grounding DINO [25] to identify the mask ID in a 2D image, ...

- **PDF anchors reviewed:** datasets p. 12 (4 Experiments), p. 9 (4 Experiments), p. 13 (4 Experiments), p. 13 (4 Experiments), p. 9 (4 Experiments), p. 11 (4 Experiments), metrics p. 9 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), baselines p. 10 (4 Experiments), p. 11 (4 Experiments), p. 11 (4 Experiments), p. 12 (4 Experiments), p. 13 (4 Experiments), p. 13 (4 Experiments), results p. 11 (4 Experiments), p. 12 (4 Experiments), p. 12 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 10 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
