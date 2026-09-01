# Evaluation - Point-MaDi: Masked Autoencoding with Diffusion for Point Cloud Pre-training

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (29 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=sYeE1obXGG; PDF retrieval source: https://openreview.net/pdf/62bf13ac3402b1f0fcc04ba494b5fba2e1214fa0.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (Figure/Table caption), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments)): Tab. 2. Our Point-MaDi achieves state-of-the-art performance, with a category mIoU of 84.8% and an instance mIoU of 86.3%, improving over Point-MAE by 0.6% and 0.2%, respectively. 3D scene segmentation. ...

## Evaluation Body Digest

- **p. 7 / 4 Experiments - extractive PDF cue:** 4.1 Downstream tasks Linear evaluation for real-world classification.
- **p. 7 / 4 Experiments - extractive PDF cue:** We first fine-tune the proposed method on realworld scenes for 3D object classification.
- **p. 9 / 4 Experiments - extractive PDF cue:** To further demonstrate the scene understanding ability of the proposed method, we fine-tune our Point-MaDi on the more challenging indoor dataset ScanNetV2 [6].
- **p. 9 / 4 Experiments - extractive PDF cue:** Method Reference [P] Pre Dataset AP50 VoteNet [33] ICCV 2019 × - 33.5 STRL [16] ICCV 2021 ✓ ScanNet 38.4 PointContrast [57] ECCV 2020 ✓ ...
- **p. 8 / 4 Experiments - extractive PDF cue:** We validate our model on the indoor S3DIS [2] dataset to demonstrate the ability of the models to comprehend contextual semantics and intricate local geometric ...
- **p. 8 / 4 Experiments - extractive PDF cue:** We report ScanObjectNN results without voting.
- **p. 23 / Figure/Table caption - extractive PDF cue:** Table 9: Few-shot classification results on ModelNet40. We perform ten separate trials for each experimental setting and the mean accuracy (%) and standard deviation are ...
- **p. 7 / 4 Experiments - extractive PDF cue:** While diffusion-based methods like PointDif may not consistently dominate on the relatively clean and less diverse ModelNet40 dataset, our Point-MaDi still achieves 93.8% accuracy, demonstrating ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-dimensional data 또는 robot action-trajectory distribution.
- **Input boundary:** conditioning observation와 noisy/intermediate sample.
- **Output/decision under evaluation:** generated sample, action chunk 또는 trajectory.
- **Primary target:** distribution fit, multimodality, sample quality와 latency.
- **Detected evaluation headings:** 4 Experiments (p. 7); A Experimental Settings Details (p. 22); C Additional Experimental Results (p. 23).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Tab. 2. Our Point-MaDi achieves state-of-the-art performance, with a category mIoU of 84.8% and an instance mIoU of 86.3%, improving over Point-MAE by 0.6% ... | p. 8 (Figure/Table caption) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our Point-MaDi achieves superior performance on all subsets, reaching 95.52%, 93.46%, and 89.52% accuracies, respectively. | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | While diffusion-based methods like PointDif may not consistently dominate on the relatively clean and less diverse ModelNet40 dataset, our Point-MaDi still achieves 93.8% accuracy, ... | p. 7 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 4, the joint decoder achieves the best overall performance. | p. 9 (4 Experiments) |
| 4 Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | 5, the Rand & Block strategy achieves the best performance under the same masking ratio. | p. 9 (4 Experiments) |

## Dataset / Benchmark Role

- **p. 7 / 4 Experiments - extractive PDF cue:** 4.1 Downstream tasks Linear evaluation for real-world classification.
- **p. 7 / 4 Experiments - extractive PDF cue:** We first fine-tune the proposed method on realworld scenes for 3D object classification.
- **p. 9 / 4 Experiments - extractive PDF cue:** To further demonstrate the scene understanding ability of the proposed method, we fine-tune our Point-MaDi on the more challenging indoor dataset ScanNetV2 [6].
- **p. 9 / 4 Experiments - extractive PDF cue:** Method Reference [P] Pre Dataset AP50 VoteNet [33] ICCV 2019 × - 33.5 STRL [16] ICCV 2021 ✓ ScanNet 38.4 PointContrast [57] ECCV 2020 ✓ ...
- **p. 8 / 4 Experiments - extractive PDF cue:** We validate our model on the indoor S3DIS [2] dataset to demonstrate the ability of the models to comprehend contextual semantics and intricate local geometric ...
- **p. 8 / 4 Experiments - extractive PDF cue:** We report ScanObjectNN results without voting.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Comparison between different pretext tasks. (a) Masked autoencoders reconstruct masked point patches. (b) PointDif uses a conditional point generator to guide the point-to-point ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: The pipeline of our Point-MaDi framework. The encoder adopts a center diffusion process, where noise is added to the centers of both visible ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 1: Classification accuracy (%) on three variants of ScanObjectNN and ModelNet40. Parameters of inference models #P (M) are listed. We report ScanObjectNN results without ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Table 2: Part segmentation on ShapeNetPart and semantic segmentation on S3DIS Area 5. The mean intersection over union (mIoU) for all classes (Cls.) and for ...
- **p. 8 / Figure/Table caption - extractive PDF cue:** Tab. 2. Our Point-MaDi achieves state-of-the-art performance, with a category mIoU of 84.8% and an instance mIoU of 86.3%, improving over Point-MAE by 0.6% and ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 3: Object detection results on ScanNet. We report average precision (%). "Pre Dataset" refers to the pre-training dataset. ScanNet-Medium is a subset of ScanNet.
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 4: Classification accuracy (%) of decoder architectures on ScanObjectNN variants. The configurations differ in how attention is applied between visible and masked tokens. Decoder ...
- **p. 9 / Figure/Table caption - extractive PDF cue:** Table 5: Classification accuracy (%) of masking strategies on ScanObjectNN variants. "Random" is random masking, "Block" is block masking, "Rand & Block" combines both. Masking ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 4.1 Downstream tasks Linear evaluation for real-world classification. | embodiment, simulator version and control stack | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Task/environment | We first fine-tune the proposed method on realworld scenes for 3D object classification. | reset, timeout, object/scene variation | p. 7 (4 Experiments), p. 9 (4 Experiments) |
| Observation/sensor | conditioning observation와 noisy/intermediate sample | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Output/decision | generated sample, action chunk 또는 trajectory | action frame, controller and termination | p. 1 (1 Introduction), p. 1 (Abstract) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Table 9: Few-shot classification results on ModelNet40. We perform ten separate trials for each experimental setting and the mean accuracy (%) and standard deviation ... | definition/direction/unit from same section | p. 23 (Figure/Table caption) |
| While diffusion-based methods like PointDif may not consistently dominate on the relatively clean and less diverse ModelNet40 dataset, our Point-MaDi still achieves 93.8% accuracy, ... | definition/direction/unit from same section | p. 7 (4 Experiments) |
| For evaluation purposes, we measure the Average Precision (AP) of 3D bounding boxes with 0.5 thresholds for IoU. | definition/direction/unit from same section | p. 9 (4 Experiments) |
| Decoder Configuration OBJ-BG OBJ-ONLY PB-T50-RS Joint decoder 95.52 93.46 89.52 Cross decoder 94.66 92.60 88.69 Cross-self decoder 93.63 92.43 87.93 Table 5: Classification accuracy ... | definition/direction/unit from same section | p. 9 (4 Experiments) |
| Tab. 2. Our Point-MaDi achieves state-of-the-art performance, with a category mIoU of 84.8% and an instance mIoU of 86.3%, improving over Point-MAE by 0.6% ... | definition/direction/unit from same section | p. 8 (Figure/Table caption) |
| We take the overall accuracy (OA) on ScanObjectNN [47] subsets as the evaluation metric and summarize experiment results as in Tab. | definition/direction/unit from same section | p. 7 (4 Experiments) |
| Mean accuracy (mAcc) and mIoU are reported for Semantic Segmentation. | definition/direction/unit from same section | p. 8 (4 Experiments) |
| Table 6: Classification accuracy (%) of different component configurations on three variants of ScanObjectNN. Center (Vis) Center (Mask) Patch Time Embedding OBJ-BG OBJ-ONLY | definition/direction/unit from same section | p. 10 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Compared to the previous Point-MAE [31], our diffusion-based Point-MaDi yields consistent improvements of 5.50%, 5.17%, and 4.34% on OBJ-BG, OBJ-ONLY, and PB-T50-RS, respectively. | comparison identity and matched condition | p. 7 (4 Experiments) |
| Our Point-MaDi achieves state-of-the-art performance, with a category mIoU of 84.8% and an instance mIoU of 86.3%, improving over Point-MAE by 0.6% and 0.2%, ... | comparison identity and matched condition | p. 8 (4 Experiments) |
| The baseline uses clean patch centers for both visible and masked patches in 9 | comparison identity and matched condition | p. 9 (4 Experiments) |
| Following MaskPoint, we utilize 3DETR [26] as the baseline and replace the encoder with our Point-MaDi backbone. | comparison identity and matched condition | p. 9 (4 Experiments) |
| Furthermore, the performance is competitive with recent cross-modal methods (e.g., ReCon [36], I2P-MAE [67]), without requiring additional modalities or complex pre-training pipelines. | comparison identity and matched condition | p. 7 (4 Experiments) |
| We report ScanObjectNN results without voting. | comparison identity and matched condition | p. 8 (4 Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Table 11: Effect of different loss functions for Lcenter and Lpatch. The accuracies (%) are reported on three variants of ScanObjectNN. | component/input/data sensitivity | p. 24 (Figure/Table caption) |
| Table 16: The effect of time embedding in the encoder. The accuracies (%) are reported on three variants of ScanObjectNN. Time Embedding OBJ-BG OBJ-ONLY ... | component/input/data sensitivity | p. 26 (Figure/Table caption) |
| Table 1: Classification accuracy (%) on three variants of ScanObjectNN and ModelNet40. Parameters of inference models #P (M) are listed. We report ScanObjectNN results ... | component/input/data sensitivity | p. 8 (Figure/Table caption) |
| We conduct a comprehensive ablation study focusing on the components of our dual-diffusion framework in Tab. | component/input/data sensitivity | p. 9 (4 Experiments) |
| We discuss the effect of different decoder designs, exploring three configurations that vary in how attention modules are applied to visible latent tokens T ... | component/input/data sensitivity | p. 9 (4 Experiments) |
| Furthermore, the performance is competitive with recent cross-modal methods (e.g., ReCon [36], I2P-MAE [67]), without requiring additional modalities or complex pre-training pipelines. | component/input/data sensitivity | p. 7 (4 Experiments) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Considering this, we propose Point-MaDi, a novel Point cloud Masked autoencoding Diffusion framework. | Tab. 2. Our Point-MaDi achieves state-of-the-art performance, with a category mIoU of 84.8% and an instance mIoU of 86.3%, improving over Point-MAE by 0.6% ... | PDF body cue; verify exact table/figure and matched conditions | p. 8 (Figure/Table caption), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments) |
| Primary metric/result | Our Point-MaDi achieves superior performance on all subsets, reaching 95.52%, 93.46%, and 89.52% accuracies, respectively. | numeric claim only at cited anchor | p. 7 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 7 / 4 Experiments - extractive PDF cue:** Following previous research, we randomly sample 2,048 points from each input instance and adopt the same segmentation head for the fair comparison, which concatenates the ...
- **p. 8 / 4 Experiments - extractive PDF cue:** Cls. mIoU Inst. mIoU mAcc mIoU Supervised Learning Only PointNet [34] CVPR 2017 80.4 83.7 49.0 41.1 DGCNN [51] TOG 2019 82.3 85.2 - - ...
- **p. 9 / 4 Experiments - extractive PDF cue:** Method Reference [P] Pre Dataset AP50 VoteNet [33] ICCV 2019 × - 33.5 STRL [16] ICCV 2021 ✓ ScanNet 38.4 PointContrast [57] ECCV 2020 ✓ ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 1: Comparison between different pretext tasks. (a) Masked autoencoders reconstruct masked point patches. (b) PointDif uses a conditional point generator to guide the ... | p. 2 (Figure/Table caption) |
| body limitation/failure cue | Figure 2: The pipeline of our Point-MaDi framework. The encoder adopts a center diffusion process, where noise is added to the centers of both ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | The stop-gradient further ensures that decoder gradients do not disrupt the encoder's center diffusion task, preserving the encoder's robust feature representations. | p. 6 (2 Related Work) |
| body limitation/failure cue | This hybrid approach enhances the robustness and generalization of patch reconstruction, complementing the encoder's sparse center denoising objective. | p. 7 (2 Related Work) |
| body limitation/failure cue | It introduces more spatial diversity in corrupted regions, which encourages the model to learn more robust and generalized representations. | p. 9 (4 Experiments) |
| body limitation/failure cue | The Cross decoder takes T v as queries and Xm as keys and values in cross-attention, mapping noise tokens to reconstructed patches within visible ... | p. 9 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Both category mIoU and instance mIoU are computed and presented in 7 | p. 7 (4 Experiments) |
| 4.2 Ablation studies Decoder architecture. | p. 9 (4 Experiments) |
| 4, the joint decoder achieves the best overall performance. | p. 9 (4 Experiments) |
| In the decoder, we design a conditional patch diffusion process, guided by the encoder's latent features and predicted centers to reconstruct masked patches directly ... | p. 1 (Abstract) |
| Specifically, we introduce a center diffusion mechanism in the encoder, noising and predicting the coordinates of both visible and masked patch centers without ground-truth ... | p. 1 (Abstract) |
| (a) Masked autoencoders reconstruct masked point patches. | p. 2 (1 Introduction) |
| This process, implemented via iterative sampling, forces the encoder to model global spatial relationships by inferring center positions from partial observations. | p. 2 (1 Introduction) |
| By integrating center diffusion for global modeling and patch diffusion for local reconstruction, Point-MaDi encourages the encoder to learn robust, context-aware representations while enabling ... | p. 3 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 2 / Figure/Table caption - extractive PDF cue:** Figure 1: Comparison between different pretext tasks. (a) Masked autoencoders reconstruct masked point patches. (b) PointDif uses a conditional point generator to guide the point-to-point ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 2: The pipeline of our Point-MaDi framework. The encoder adopts a center diffusion process, where noise is added to the centers of both visible ...
- **p. 6 / 2 Related Work - extractive PDF cue:** The stop-gradient further ensures that decoder gradients do not disrupt the encoder's center diffusion task, preserving the encoder's robust feature representations.
- **p. 7 / 2 Related Work - extractive PDF cue:** This hybrid approach enhances the robustness and generalization of patch reconstruction, complementing the encoder's sparse center denoising objective.
- **p. 9 / 4 Experiments - extractive PDF cue:** It introduces more spatial diversity in corrupted regions, which encourages the model to learn more robust and generalized representations.
- **p. 9 / 4 Experiments - extractive PDF cue:** The Cross decoder takes T v as queries and Xm as keys and values in cross-attention, mapping noise tokens to reconstructed patches within visible context.

- **PDF anchors reviewed:** datasets p. 7 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments), p. 8 (4 Experiments), metrics p. 23 (Figure/Table caption), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 8 (Figure/Table caption), p. 7 (4 Experiments), baselines p. 7 (4 Experiments), p. 8 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments), results p. 8 (Figure/Table caption), p. 7 (4 Experiments), p. 7 (4 Experiments), p. 9 (4 Experiments), p. 9 (4 Experiments), p. 8 (4 Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
