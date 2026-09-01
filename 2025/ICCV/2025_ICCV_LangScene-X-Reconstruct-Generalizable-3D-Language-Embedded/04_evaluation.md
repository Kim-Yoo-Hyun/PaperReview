# Evaluation - LangScene-X: Reconstruct Generalizable 3D Language-Embedded Scenes with TriMap Video Diffusion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Liu_LangScene-X_Reconstruct_Generalizable_3D_Language-Embedded_Scenes_with_TriMap_Video_Diffusion_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Liu_LangScene-X_Reconstruct_Generalizable_3D_Language-Embedded_Scenes_with_TriMap_Video_Diffusion_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4.2. Main Results), p. 6 (4.1. Experiment Setup), p. 8 (4.3. Ablations), p. 8 (4.2. Main Results), p. 7 (4.2. Main Results), p. 7 (4.2. Main Results)): By comparing with existing state-of-the-art 3D language field techniques (e.g., LangSplat, LangSurf), unified 3D representation method (i.e., LSM), and open-vocabulary methods like LSeg, our method achieves superior performance in segme ...

## Evaluation Body Digest

- **p. 6 / 4.1. Experiment Setup - extractive PDF cue:** The LERF dataset is an in-the-wild dataset captured by a handheld device, while ScanNet is a large scene dataset captured by RGB-D devices in complex ...
- **p. 6 / 4.1. Experiment Setup - extractive PDF cue:** Then, we train our model on large-scale open-world dataset COCO [23] with a batch size of 16 and 500,000 steps.
- **p. 7 / 4.2. Main Results - extractive PDF cue:** 2D Segmentation Results on Scannet [7] Dataset.
- **p. 8 / 4.2. Main Results - extractive PDF cue:** On the ScanNet dataset, the improvement upon the best existing method comes to 14.92% in terms of mIoU.
- **p. 8 / 4.2. Main Results - extractive PDF cue:** Training Curve comparison between our LQC and regular autoencoder technique. curacy in both mIoU and mAcc metrics with a large margin, i.e., a 10.58\ % ...
- **p. 8 / 4.3. Ablations - extractive PDF cue:** 7, it is evident that our quantized technique demonstrates superior performance in both loss convergence rate and accuracy in terms of L2 loss (from 1e^{-3} ...
- **p. 6 / 4.1. Experiment Setup - extractive PDF cue:** For quantitative results, we report the standard metrics in semantic understanding, including open-vocabulary localization accuracy (mAcc) and semantic segmentation (mIoU scores).
- **p. 8 / 4.3. Ablations - extractive PDF cue:** 8, where our method enable to perform sharper boundaries and more accurate activation scores within the query objects.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiment (p. 6); 4.1. Experiment Setup (p. 6); 4.2. Main Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4.2. Main Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | By comparing with existing state-of-the-art 3D language field techniques (e.g., LangSplat, LangSurf), unified 3D representation method (i.e., LSM), and open-vocabulary methods like LSeg, our ... | p. 6 (4.2. Main Results) |
| 4.1. Experiment Setup | EMPIRICAL / SOURCE-REPORTED EVALUATION | For quantitative results, we report the standard metrics in semantic understanding, including open-vocabulary localization accuracy (mAcc) and semantic segmentation (mIoU scores). | p. 6 (4.1. Experiment Setup) |
| 4.3. Ablations | EMPIRICAL / SOURCE-REPORTED EVALUATION | 51.68 45.07 gressive training in TriMap video diffusion, which achieves more matched points. | p. 8 (4.3. Ablations) |
| 4.2. Main Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | On the ScanNet dataset, the improvement upon the best existing method comes to 14.92% in terms of mIoU. | p. 8 (4.2. Main Results) |
| 4.2. Main Results | EMPIRICAL / SOURCE-REPORTED EVALUATION | 2D Segmentation Results on Scannet [7] Dataset. | p. 7 (4.2. Main Results) |

## Dataset / Benchmark Role

- **p. 6 / 4.1. Experiment Setup - extractive PDF cue:** The LERF dataset is an in-the-wild dataset captured by a handheld device, while ScanNet is a large scene dataset captured by RGB-D devices in complex ...
- **p. 6 / 4.1. Experiment Setup - extractive PDF cue:** Then, we train our model on large-scale open-world dataset COCO [23] with a batch size of 16 and 500,000 steps.
- **p. 7 / 4.2. Main Results - extractive PDF cue:** 2D Segmentation Results on Scannet [7] Dataset.
- **p. 8 / 4.2. Main Results - extractive PDF cue:** On the ScanNet dataset, the improvement upon the best existing method comes to 14.92% in terms of mIoU.
- **p. 8 / 4.2. Main Results - extractive PDF cue:** Training Curve comparison between our LQC and regular autoencoder technique. curacy in both mIoU and mAcc metrics with a large margin, i.e., a 10.58\ % ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. LangScene-X: Given sparse views as input (e.g., as few as two images), we design a generative paradigm to build the 3D generalizable language-embedded ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2. Pipeline of LangScene-X. Given two sparse-view images as input, we first generate a sequence of 3D consistent RGB images, normal maps, and segmentation ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. The illustration of Language Quantized Compressor (LQC). By leveraging learnable embedding and vector quantisa- tion strategy, it compresses high-dimensional language features into discrete ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. 2D Quantitative Results on LERF-OVS Dataset. We report the open-vocabulary localization accuracy (%) and 2D semantic segmentation (IoU scores). LSeg [19] is a ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. 2D Quantitative Results on ScanNet Dataset. We report the open-vocabulary localization accuracy (%) and 2D semantic segmentation (IoU scores). The bold denotes the ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 4. 2D Segmentation Results on LERF-OVS [17] Dataset. Here, we showcase two cases (i.e., Teatime, Kitchen) with multiple segmentation masks with text query. On ...
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5. 2D Segmentation Results on Scannet [7] Dataset. Here, we showcase two cases (i.e., 0085 00, 0114 00) with multiple segmentation masks with text ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Figure 6. Feature Matching comparison between our method and vanilla video diffusion mdoel . L2 Loss (log) Step

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The LERF dataset is an in-the-wild dataset captured by a handheld device, while ScanNet is a large scene dataset captured by RGB-D devices in ... | embodiment, simulator version and control stack | p. 6 (4.1. Experiment Setup), p. 6 (4.1. Experiment Setup) |
| Task/environment | Then, we train our model on large-scale open-world dataset COCO [23] with a batch size of 16 and 500,000 steps. | reset, timeout, object/scene variation | p. 6 (4.1. Experiment Setup), p. 7 (4.2. Main Results) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 3 (3.1. Overview of LangScene-X), p. 3 (3.1. Overview of LangScene-X) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 4 (3.2. Building the TriMap Video Diffusion), p. 4 (3.2. Building the TriMap Video Diffusion) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 2. 2D Quantitative Results on ScanNet Dataset. We report the open-vocabulary localization accuracy (%) and 2D semantic segmentation (IoU scores). The bold denotes ... | definition/direction/unit from same section | p. 6 (Figure/Table caption) |
| 7, it is evident that our quantized technique demonstrates superior performance in both loss convergence rate and accuracy in terms of L2 loss (from ... | definition/direction/unit from same section | p. 8 (4.3. Ablations) |
| For quantitative results, we report the standard metrics in semantic understanding, including open-vocabulary localization accuracy (mAcc) and semantic segmentation (mIoU scores). | definition/direction/unit from same section | p. 6 (4.1. Experiment Setup) |
| 8, where our method enable to perform sharper boundaries and more accurate activation scores within the query objects. | definition/direction/unit from same section | p. 8 (4.3. Ablations) |
| Figure 1. LangScene-X: Given sparse views as input (e.g., as few as two images), we design a generative paradigm to build the 3D generalizable ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| Figure 3. The illustration of Language Quantized Compressor (LQC). By leveraging learnable embedding and vector quantisa- tion strategy, it compresses high-dimensional language features into ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 2. Pipeline of LangScene-X. Given two sparse-view images as input, we first generate a sequence of 3D consistent RGB images, normal maps, and ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| To demonstrate our strong capability in building 3D language-embedded scenes from only sparse views, we compare our LangScene-X against four competitive baselines: LSeg [19], ... | comparison identity and matched condition | p. 6 (4.1. Experiment Setup) |
| By comparing with existing state-of-the-art 3D language field techniques (e.g., LangSplat, LangSurf), unified 3D representation method (i.e., LSM), and open-vocabulary methods like LSeg, our ... | comparison identity and matched condition | p. 6 (4.2. Main Results) |
| Qualitative Comparison on LERF-OVS [17]. | comparison identity and matched condition | p. 8 (4.3. Ablations) |
| Ablations of proposed module and losses. | comparison identity and matched condition | p. 8 (4.3. Ablations) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Ablations of proposed module and losses. | component/input/data sensitivity | p. 8 (4.3. Ablations) |
| We conduct ablation experiments with our TriMap Video Diffusion and Language Quantized Compressor techniques. | component/input/data sensitivity | p. 8 (4.3. Ablations) |
| Finally, we apply SAM2 to annotate 300 clips of semantic video clips to fine-tune with RGB and normal videos with 1000 steps. | component/input/data sensitivity | p. 6 (4.1. Experiment Setup) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To address this, we propose LangScene-X, a novel generative paradigm to build generalizable 3D languageembedded scenes from very sparse views (i.e., as few as ... | By comparing with existing state-of-the-art 3D language field techniques (e.g., LangSplat, LangSurf), unified 3D representation method (i.e., LSM), and open-vocabulary methods like LSeg, our ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4.2. Main Results), p. 6 (4.1. Experiment Setup), p. 8 (4.3. Ablations), p. 8 (4.2. Main Results), p. 7 (4.2. Main Results), p. 7 (4.2. Main Results) |
| Primary metric/result | For quantitative results, we report the standard metrics in semantic understanding, including open-vocabulary localization accuracy (mAcc) and semantic segmentation (mIoU scores). | numeric claim only at cited anchor | p. 6 (4.1. Experiment Setup) |

- Numeric sentences retained from the body:
- **p. 6 / 4.1. Experiment Setup - extractive PDF cue:** Then we finetune it on 3D-consistent real data (i.e., RealEstate-10K [55] and ACID [24]) with 2000 steps on the learning rate 1 × 10-5.
- **p. 6 / 4.1. Experiment Setup - extractive PDF cue:** Next, we apply StableNormal to annotate 200 normal video clips of 3D scene data from RealEstate-10k and finetune TriMap video diffusion along with RGB videos ...
- **p. 6 / 4.1. Experiment Setup - extractive PDF cue:** Finally, we apply SAM2 to annotate 300 clips of semantic video clips to fine-tune with RGB and normal videos with 1000 steps.
- **p. 6 / 4.1. Experiment Setup - extractive PDF cue:** All videos are center-cropped and resized to 720 × 480 resolution with 49 frames.
- **p. 6 / 4.1. Experiment Setup - extractive PDF cue:** Then, we train our model on large-scale open-world dataset COCO [23] with a batch size of 16 and 500,000 steps.
- **p. 6 / 4.1. Experiment Setup - extractive PDF cue:** For Language Surface Fields training, we first train the Gaussian model with only RGB and normal loss \protect \mathcal {L}_{normal} for 5,000 steps, and then ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| no explicit failure cue selected | unreported; domain stress test remains open | verify Discussion/Conclusion |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Then, we train our model on large-scale open-world dataset COCO [23] with a batch size of 16 and 500,000 steps. | p. 6 (4.1. Experiment Setup) |
| Then we finetune it on 3D-consistent real data (i.e., RealEstate-10K [55] and ACID [24]) with 2000 steps on the learning rate 1 × 10-5. | p. 6 (4.1. Experiment Setup) |
| We visualize the training curve of our method and traditional autoencoder. | p. 8 (4.3. Ablations) |
| Training Curve comparison between our LQC and regular autoencoder technique. curacy in both mIoU and mAcc metrics with a large margin, i.e., a 10.58\ ... | p. 8 (4.2. Main Results) |
| hierarchy masks {Mh/h = s, m, l} at inference time from only two input views segmented by DS, where s, m, l represents small, ... | p. 5 (3.2. Building the TriMap Video Diffusion) |
| Finally, we iteratively denoise the noise latent and apply the VAE decoder to obtain key-frame interpolation results. | p. 4 (3.2. Building the TriMap Video Diffusion) |
| Then, we encode the condition video with a causal VAE [49] encoder to get a latent vector concatenated with a Gaussian noise of the ... | p. 4 (3.2. Building the TriMap Video Diffusion) |
| After that, z_q(x ) passes through the decoder and obtains the reconstructed feature \protect \hat {x}. | p. 5 (3.3. Language Quantized Compressor) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- explicit limitation/failure sentence not recovered

- **PDF anchors reviewed:** datasets p. 6 (4.1. Experiment Setup), p. 6 (4.1. Experiment Setup), p. 7 (4.2. Main Results), p. 8 (4.2. Main Results), p. 8 (4.2. Main Results), metrics p. 6 (Figure/Table caption), p. 8 (4.3. Ablations), p. 6 (4.1. Experiment Setup), p. 8 (4.3. Ablations), p. 1 (Figure/Table caption), p. 4 (Figure/Table caption), baselines p. 6 (4.1. Experiment Setup), p. 6 (4.2. Main Results), p. 8 (4.3. Ablations), p. 8 (4.3. Ablations), results p. 6 (4.2. Main Results), p. 6 (4.1. Experiment Setup), p. 8 (4.3. Ablations), p. 8 (4.2. Main Results), p. 7 (4.2. Main Results), p. 7 (4.2. Main Results).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
