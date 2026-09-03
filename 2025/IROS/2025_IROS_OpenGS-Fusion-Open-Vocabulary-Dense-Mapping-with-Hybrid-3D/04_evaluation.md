# Evaluation - OpenGS-Fusion: Open-Vocabulary Dense Mapping with Hybrid 3D Gaussian Splatting for Refined Object-Level Understanding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2508.01150; PDF retrieval source: https://arxiv.org/pdf/2508.01150. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT)): Specifically, our method outperforms the state-of-the-art 3DGS-based approach, OpenGaussian, with improvements of 9.5% (Replica) and 12.2% (ScanNet) in terms of mIoU performance, while operating in an online setting without the ...

## Evaluation Body Digest

- **p. 5 / IV. EXPERIMENT - extractive body cue:** Replica ScanNet Methods mAcc↑ mIoU↑ FPS↑ mAcc↑ mIoU↑ FPS↑ ConceptFusion* 28.02 11.49 0.49 21.22 10.64 0.52 ConceptGraphs 38.21 18.16 - 44.28 23.94 - LangSplat 10.32 ...
- **p. 6 / IV. EXPERIMENT - extractive body cue:** 3) Datasets: The experiments are carried out on 8 synthetic scenes from the Replica dataset and 6 real-world scenes from the ScanNet dataset, following the ...
- **p. 7 / IV. EXPERIMENT - extractive body cue:** Real-World Experiments In this section, we describe the practical implementation of OpenGS-Fusion for the reconstruction and understanding of indoor scenes using a mobile robotic device.
- **p. 5 / IV. EXPERIMENT - extractive body cue:** Finally, we implement and validate the proposed algorithm in real-world scenarios using our robotic mobile platform (Sec.
- **p. 6 / IV. EXPERIMENT - extractive body cue:** 5 presents qualitative rendering results in four real-world scenes, highlighting the robustness of our method against motion blur and depth noise.
- **p. 7 / IV. EXPERIMENT - extractive body cue:** Reconstruction and scene understanding results on our self-captured dataset, demonstrated across three representative spatial locations.
- **p. 5 / IV. EXPERIMENT - extractive body cue:** We aggregate these measurements into dataset-level evaluation metrics, specifically mean IoU (mIoU) and mean accuracy (mAcc).
- **p. 6 / IV. EXPERIMENT - extractive body cue:** We also evaluated geometric reconstruction accuracy with depth L1 loss and system efficiency with mapping frame rate (FPS).

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** IV. EXPERIMENT (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| IV. EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | Specifically, our method outperforms the state-of-the-art 3DGS-based approach, OpenGaussian, with improvements of 9.5% (Replica) and 12.2% (ScanNet) in terms of mIoU performance, while operating ... | p. 5 (IV. EXPERIMENT) |
| IV. EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method achieves the best performance in both open-vocabulary 3D object segmentation accuracy and training efficiency. | p. 5 (IV. EXPERIMENT) |
| IV. EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method achieves state-of-the-art performance in PSNR, SSIM, LPIPS, and Depth L1. | p. 6 (IV. EXPERIMENT) |
| IV. EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | In particular, the scene understanding module of our method is disabled in this evaluation, which explains the significant speed improvement compared to Table I. | p. 6 (IV. EXPERIMENT) |
| IV. EXPERIMENT | EMPIRICAL / REAL-ROBOT OR HARDWARE | Parallel processing on the server achieved an overall operational efficiency of 4 fps. | p. 7 (IV. EXPERIMENT) |

## Dataset / Benchmark Role

- **p. 5 / IV. EXPERIMENT - extractive body cue:** Replica ScanNet Methods mAcc↑ mIoU↑ FPS↑ mAcc↑ mIoU↑ FPS↑ ConceptFusion* 28.02 11.49 0.49 21.22 10.64 0.52 ConceptGraphs 38.21 18.16 - 44.28 23.94 - LangSplat 10.32 ...
- **p. 6 / IV. EXPERIMENT - extractive body cue:** 3) Datasets: The experiments are carried out on 8 synthetic scenes from the Replica dataset and 6 real-world scenes from the ScanNet dataset, following the ...
- **p. 7 / IV. EXPERIMENT - extractive body cue:** Real-World Experiments In this section, we describe the practical implementation of OpenGS-Fusion for the reconstruction and understanding of indoor scenes using a mobile robotic device.
- **p. 5 / IV. EXPERIMENT - extractive body cue:** Finally, we implement and validate the proposed algorithm in real-world scenarios using our robotic mobile platform (Sec.
- **p. 6 / IV. EXPERIMENT - extractive body cue:** 5 presents qualitative rendering results in four real-world scenes, highlighting the robustness of our method against motion blur and depth noise.
- **p. 7 / IV. EXPERIMENT - extractive body cue:** Reconstruction and scene understanding results on our self-captured dataset, demonstrated across three representative spatial locations.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Comparison of Model Architectures. Compared to 3DGS-feature- field-based methods [12]-[15], our approach enables online modeling of scene appearance, geometry, and semantics while supporting ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2. Overview of OpenGS-Fusion. Receiving RGB-D input with 2D language embeddings extracted from 2D foundation models, we simultaneously update the appearance, geometry and semantic ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. A visual demonstration of our proposed AT-MLLM. This strategy enables the precise localization of multiple objects in 3D space through multi-stage threshold adjustment ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 4. Qualitative comparison of open-vocabulary 3D understanding on ScanNet (top two rows) and Replica (last two rows), benchmarking 3DGS- based methods (OpenGaussian [4] and ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5. Qualitative rendering results from training views on the ScanNet dataset. Zoom in for a clearer view. * denotes that the method employs a ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6. An Example of Language-Guided Scene Editing. OpenGS-Fusion accurately localizes objects in 3D space and efficiently executes language- guided scene modifications. The spatial position ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 7. Reconstruction and scene understanding results on our self-captured dataset, demonstrated across three representative spatial locations. RGB-D camera system and an NVIDIA Jetson AGX ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Replica ScanNet Methods mAcc↑ mIoU↑ FPS↑ mAcc↑ mIoU↑ FPS↑ ConceptFusion* 28.02 11.49 0.49 21.22 10.64 0.52 ConceptGraphs 38.21 18.16 - 44.28 23.94 - LangSplat ... | embodiment, simulator version and control stack | p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT) |
| Task/environment | 3) Datasets: The experiments are carried out on 8 synthetic scenes from the Replica dataset and 6 real-world scenes from the ScanNet dataset, following ... | reset, timeout, object/scene variation | p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 4 (III. OPENGS-FUSION), p. 1 (1) Rigid Offline Pipeline. These methods rely on essen) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 1 (Abstract), p. 2 (III. OPENGS-FUSION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We aggregate these measurements into dataset-level evaluation metrics, specifically mean IoU (mIoU) and mean accuracy (mAcc). | definition/direction/unit from same section | p. 5 (IV. EXPERIMENT) |
| We also evaluated geometric reconstruction accuracy with depth L1 loss and system efficiency with mapping frame rate (FPS). | definition/direction/unit from same section | p. 6 (IV. EXPERIMENT) |
| Our method achieves the best performance in both open-vocabulary 3D object segmentation accuracy and training efficiency. | definition/direction/unit from same section | p. 5 (IV. EXPERIMENT) |
| Language-guided scene editing By integrating with large language models (LLMs) on the front end, OpenGS-Fusion empowers users to execute a diverse range of scene ... | definition/direction/unit from same section | p. 6 (IV. EXPERIMENT) |
| OpenGS-Fusion accurately localizes objects in 3D space and efficiently executes languageguided scene modifications. | definition/direction/unit from same section | p. 7 (IV. EXPERIMENT) |
| Reconstruction and scene understanding results on our self-captured dataset, demonstrated across three representative spatial locations. | definition/direction/unit from same section | p. 7 (IV. EXPERIMENT) |
| Fig. 2. Overview of OpenGS-Fusion. Receiving RGB-D input with 2D language embeddings extracted from 2D foundation models, we simultaneously update the appearance, geometry and ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Fig. 3. A visual demonstration of our proposed AT-MLLM. This strategy enables the precise localization of multiple objects in 3D space through multi-stage threshold ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Specifically, our method outperforms the state-of-the-art 3DGS-based approach, OpenGaussian, with improvements of 9.5% (Replica) and 12.2% (ScanNet) in terms of mIoU performance, while operating ... | comparison identity and matched condition | p. 5 (IV. EXPERIMENT) |
| 2) Baselines: We select state-of-the-art dense mapping methods based on Gaussian splatting as comparative baselines, including SplaTAM [17], MonoGS [29], RTG-SLAM [48] and GSICP-SLAM ... | comparison identity and matched condition | p. 6 (IV. EXPERIMENT) |
| Fig. 1. Comparison of Model Architectures. Compared to 3DGS-feature- field-based methods [12]-[15], our approach enables online modeling of scene appearance, geometry, and semantics while ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Based on similarity scores, we select the most relevant 3D primitives and quantitatively compare them with the ground-truth 3D object segmentation 2) Baselines: We ... | comparison identity and matched condition | p. 5 (IV. EXPERIMENT) |
| Our method achieves state-of-the-art performance in PSNR, SSIM, LPIPS, and Depth L1. | comparison identity and matched condition | p. 6 (IV. EXPERIMENT) |
| Compared to a fixed threshold strategy (set at 0.6), our AT-MLLM module enhances the final scene understanding of mIoU by 17% (at 5 cm ... | comparison identity and matched condition | p. 7 (IV. EXPERIMENT) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| To ensure fairness, we adhere to [4] for training LangSplat, OpenGaussian, and our method, without optimizing the positional attributes of Gaussian primitives. | component/input/data sensitivity | p. 5 (IV. EXPERIMENT) |
| Specifically, our method outperforms the state-of-the-art 3DGS-based approach, OpenGaussian, with improvements of 9.5% (Replica) and 12.2% (ScanNet) in terms of mIoU performance, while operating ... | component/input/data sensitivity | p. 5 (IV. EXPERIMENT) |
| Ablation Experiments To further validate our method, we conducted ablation studies focusing on the core parameters of our hybrid representation, specifically the voxel size ... | component/input/data sensitivity | p. 6 (IV. EXPERIMENT) |
| Fig. 2. Overview of OpenGS-Fusion. Receiving RGB-D input with 2D language embeddings extracted from 2D foundation models, we simultaneously update the appearance, geometry and ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our method enables versatile task-oriented interactions, such as 3D object extraction and editing in an interactive manner. | Specifically, our method outperforms the state-of-the-art 3DGS-based approach, OpenGaussian, with improvements of 9.5% (Replica) and 12.2% (ScanNet) in terms of mIoU performance, while operating ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT) |
| Primary metric/result | Our method achieves the best performance in both open-vocabulary 3D object segmentation accuracy and training efficiency. | numeric claim only at cited anchor | p. 5 (IV. EXPERIMENT) |

- Numeric sentences retained from the body:
- **p. 6 / IV. EXPERIMENT - extractive body cue:** (AVERAGE PERFORMANCE ON 6 SCENES) Method PSNR ↑ SSIM ↑ LPIPS ↓ Depth L1 ↓ FPS ↑ MonoGS 17.31 0.636 0.583 21.30 14.02 RTG-SLAM 18.22 ...
- **p. 6 / IV. EXPERIMENT - extractive body cue:** (AVERAGE PERFORMANCE ON 8 SCENES) Method PSNR ↑ SSIM ↑ LPIPS ↓ Depth L1 ↓ FPS ↑ MonoGS 36.50 0.960 0.070 0.77 4.691 RTG-SLAM 35.43 ...
- **p. 7 / IV. EXPERIMENT - extractive body cue:** Our algorithm was deployed on a computing setup with an NVIDIA RTX 4090 GPU and an Intel Core i9-14900K CPU.
- **p. 7 / IV. EXPERIMENT - extractive body cue:** To improve efficiency, MobileSAMv2 [42] was used as the 2D segmentation model in our 2D Embedding Extractor model, enabling real-time image segmentation at more than ...
- **p. 7 / IV. EXPERIMENT - extractive body cue:** Parallel processing on the server achieved an overall operational efficiency of 4 fps.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | However, our method currently relies on accurate pose estimation and faces limitations in query efficiency. | p. 7 (V. CONCLUSIONS) |
| body limitation/failure cue | Future work will explore how to leverage hybrid scene representation for pose estimation and investigate lightweight MLLMs specifically designed for image retrieval tasks to ... | p. 7 (V. CONCLUSIONS) |
| body limitation/failure cue | OpenGaussian fails to locate both instances as they are segmented into separate entities, and the model by default only retrieves the instance that best ... | p. 5 (IV. EXPERIMENT) |
| body limitation/failure cue | 5 presents qualitative rendering results in four real-world scenes, highlighting the robustness of our method against motion blur and depth noise. | p. 6 (IV. EXPERIMENT) |
| body limitation/failure cue | We attribute this to the incorporation of our extra GS initialization and pruning mechanism, which leverages the TSDF to improve robustness when handling real-world ... | p. 6 (IV. EXPERIMENT) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Our algorithm was deployed on a computing setup with an NVIDIA RTX 4090 GPU and an Intel Core i9-14900K CPU. | p. 7 (IV. EXPERIMENT) |
| 1) Task: Given an open-ended object-level textual query, we compute the cosine similarity between the query features and the 3D primitive features. | p. 5 (IV. EXPERIMENT) |
| 4) Evaluation Metrics: We consider all foreground objects in each scene as potential text queries and compute the 3D Intersection-over-Union (IoU) for individual class. | p. 5 (IV. EXPERIMENT) |
| Additionally, compared to our code-based approach GSICPTABLE III QUANTITATIVE TRAIN VIEW RENDERING PERFORMANCE ON REPLICA. | p. 6 (IV. EXPERIMENT) |
| Real-World Experiments In this section, we describe the practical implementation of OpenGS-Fusion for the reconstruction and understanding of indoor scenes using a mobile robotic ... | p. 7 (IV. EXPERIMENT) |
| tial preprocessing steps, such as pretraining 3D Gaussian representation or offline compression of high-dimensional semantic features. | p. 1 (1) Rigid Offline Pipeline. These methods rely on essen) |
| 2) Refined 3D Object Understanding: To achieve precise 3D object localization, we compute semantic similarity across all spatial regions within the semantic space. | p. 2 (2) Limited 3D Object-Level Understanding. Most exist) |
| OpenVDB [25] is a data structure designed to manipulate unbounded volumetric data, enabling efficient CPU-based operations. | p. 3 (III. OPENGS-FUSION) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / V. CONCLUSIONS - extractive body cue:** However, our method currently relies on accurate pose estimation and faces limitations in query efficiency.
- **p. 7 / V. CONCLUSIONS - extractive body cue:** Future work will explore how to leverage hybrid scene representation for pose estimation and investigate lightweight MLLMs specifically designed for image retrieval tasks to further ...
- **p. 5 / IV. EXPERIMENT - extractive body cue:** OpenGaussian fails to locate both instances as they are segmented into separate entities, and the model by default only retrieves the instance that best matches ...
- **p. 6 / IV. EXPERIMENT - extractive body cue:** 5 presents qualitative rendering results in four real-world scenes, highlighting the robustness of our method against motion blur and depth noise.
- **p. 6 / IV. EXPERIMENT - extractive body cue:** We attribute this to the incorporation of our extra GS initialization and pruning mechanism, which leverages the TSDF to improve robustness when handling real-world scene ...

- **Evidence anchors reviewed:** datasets p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), metrics p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), baselines p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 1 (Figure/Table caption), p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), results p. 5 (IV. EXPERIMENT), p. 5 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 6 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT), p. 7 (IV. EXPERIMENT).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
