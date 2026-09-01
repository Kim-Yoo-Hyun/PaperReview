# Evaluation - Egocentric Action-aware Inertial Localization in Point Clouds with Vision-Language Guidance

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-01 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_Egocentric_Action-aware_Inertial_Localization_in_Point_Clouds_with_Vision-Language_Guidance_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_Egocentric_Action-aware_Inertial_Localization_in_Point_Clouds_with_Vision-Language_Guidance_ICCV_2025_paper.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (Figure/Table caption), p. 8 (5.4. Ablation Studies), p. 8 (5.4. Ablation Studies), p. 5 (5.1. Experimental Setup), p. 6 (5.2. Inertial Localization Results), p. 7 (5.4. Ablation Studies)): Table 1. Inertial Localization Results. We evaluate the accuracy using two metrics: the localization success rate (%) at various error distance thresholds and the Relative Score (RS) metric for localization ...

## Evaluation Body Digest

- **p. 5 / 5.1. Experimental Setup - extractive PDF cue:** These scores are assessed under two setups: "seen rooms" where the localization is performed in the environments present in the training dataset and "unseen rooms" ...
- **p. 5 / 5.1. Experimental Setup - extractive PDF cue:** The dataset is labeled with 35 distinct action classes for classification tasks.
- **p. 7 / 5.4. Ablation Studies - extractive PDF cue:** This demonstrates the broad applicability and flexibility of our approach in real-world environments.
- **p. 6 / 5.2. Inertial Localization Results - extractive PDF cue:** This is because each recording in the dataset is relatively long, with an average duration of 525 seconds and a maximum of 2,526 seconds.
- **p. 8 / 5.4. Ablation Studies - extractive PDF cue:** This holistic reasoning capability ensures the model generates a more precise and coherent trajectory prediction of the user's movements within their environment.
- **p. 7 / 5.4. Ablation Studies - extractive PDF cue:** Furthermore, even in scenarios where action caption annotations are unavailable in the training set, our method does not fail, ensuring reasonable accuracy without relying on ...
- **p. 6 / 5.2. Inertial Localization Results - extractive PDF cue:** In their original work, they trained three separate models, each for a different scene.
- **p. 8 / 5.4. Ablation Studies - extractive PDF cue:** It shows that when these two modules work in tandem, they align sequential motion data with the environmental settings.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 5. Experiments (p. 5); 5.1. Experimental Setup (p. 5); 5.2. Inertial Localization Results (p. 5); 5.3. Inertial Action Recognition Results (p. 6); 5.5. Qualitative evaluations (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Table 1. Inertial Localization Results. We evaluate the accuracy using two metrics: the localization success rate (%) at various error distance thresholds and the ... | p. 6 (Figure/Table caption) |
| 5.4. Ablation Studies | EMPIRICAL / REAL-ROBOT OR HARDWARE | 4, using only IMU signals, we achieve results comparable to IMU2CLIP [41]. | p. 8 (5.4. Ablation Studies) |
| 5.4. Ablation Studies | EMPIRICAL / REAL-ROBOT OR HARDWARE | In contrast, integrating point cloud features with predicted location attention with IMU features provides a clear performance improvement. | p. 8 (5.4. Ablation Studies) |
| 5.1. Experimental Setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | Evaluation Metrics For the localization task, we report the success rate (%) at error distance thresholds of 0.2 m, 0.4 m, and 0.6 m ... | p. 5 (5.1. Experimental Setup) |
| 5.2. Inertial Localization Results | EMPIRICAL / REAL-ROBOT OR HARDWARE | 1, direct location prediction methods outperform velocity accumulation methods. | p. 6 (5.2. Inertial Localization Results) |

## Dataset / Benchmark Role

- **p. 5 / 5.1. Experimental Setup - extractive PDF cue:** These scores are assessed under two setups: "seen rooms" where the localization is performed in the environments present in the training dataset and "unseen rooms" ...
- **p. 5 / 5.1. Experimental Setup - extractive PDF cue:** The dataset is labeled with 35 distinct action classes for classification tasks.
- **p. 7 / 5.4. Ablation Studies - extractive PDF cue:** This demonstrates the broad applicability and flexibility of our approach in real-world environments.
- **p. 6 / 5.2. Inertial Localization Results - extractive PDF cue:** This is because each recording in the dataset is relatively long, with an average duration of 525 seconds and a maximum of 2,526 seconds.
- **p. 8 / 5.4. Ablation Studies - extractive PDF cue:** This holistic reasoning capability ensures the model generates a more precise and coherent trajectory prediction of the user's movements within their environment.
- **p. 7 / 5.4. Ablation Studies - extractive PDF cue:** Furthermore, even in scenarios where action caption annotations are unavailable in the training set, our method does not fail, ensuring reasonable accuracy without relying on ...
- **p. 6 / 5.2. Inertial Localization Results - extractive PDF cue:** In their original work, they trained three separate models, each for a different scene.
- **p. 8 / 5.4. Ablation Studies - extractive PDF cue:** It shows that when these two modules work in tandem, they align sequential motion data with the environmental settings.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive PDF cue:** Figure 1. Egocentric Action-aware Inertial Localization (EAIL). Our framework leverages egocentric action cues obtained from the head-mounted IMU to perform inertial localization in the environ- ...
- **p. 3 / Figure/Table caption - extractive PDF cue:** Figure 2. Short-Term Action-Location Alignment. In this first stage, our objective is to train a point cloud encoder and an IMU encoder using contrastive learning. ...
- **p. 4 / Figure/Table caption - extractive PDF cue:** Figure 3. Sequential Motion Localization. In this second stage, we generate a sequence of the user's locations and actions over T seconds using a series ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 1. Inertial Localization Results. We evaluate the accuracy using two metrics: the localization success rate (%) at various error distance thresholds and the Relative ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Figure 4. Inertial Localization Error Over Time Elapsed. While velocity accumulation-based methods experience signifi- cant trajectory drift, our approach remains accurate over time. Velocity Cumulation ...
- **p. 6 / Figure/Table caption - extractive PDF cue:** Table 2. Inertial Action Recognition Results. We evaluate per- formance using top1 and top5 accuracy metrics. Higher values indicate better performance.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Table 3. Ablation Studies. We report the inertial localization accuracy and the inertial action recognition (A) accuracy simultaneously.
- **p. 7 / Figure/Table caption - extractive PDF cue:** Figure 5. Visualization of Heatmaps in Each Stage. Quantitative Evaluation As shown in Tab. 2, DeepCon- vLSTM performs relatively poorly due to its architecture's difficulty ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | These scores are assessed under two setups: "seen rooms" where the localization is performed in the environments present in the training dataset and "unseen ... | embodiment, simulator version and control stack | p. 5 (5.1. Experimental Setup), p. 5 (5.1. Experimental Setup) |
| Task/environment | The dataset is labeled with 35 distinct action classes for classification tasks. | reset, timeout, object/scene variation | p. 5 (5.1. Experimental Setup), p. 7 (5.4. Ablation Studies) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 2 (1. Introduction), p. 2 (1. Introduction) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 1 (1. Introduction), p. 1 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We evaluate the accuracy using two metrics: the localization success rate (%) at various error distance thresholds and the Relative Score (RS) metric for ... | definition/direction/unit from same section | p. 6 (5.2. Inertial Localization Results) |
| Evaluation Metrics For the localization task, we report the success rate (%) at error distance thresholds of 0.2 m, 0.4 m, and 0.6 m ... | definition/direction/unit from same section | p. 5 (5.1. Experimental Setup) |
| For action classification, we evaluate performance using top-1 and top-5 accuracy metrics. | definition/direction/unit from same section | p. 5 (5.1. Experimental Setup) |
| We evaluate performance using top1 and top5 accuracy metrics. | definition/direction/unit from same section | p. 6 (5.2. Inertial Localization Results) |
| We report the inertial localization accuracy and the inertial action recognition (A) accuracy simultaneously. | definition/direction/unit from same section | p. 7 (5.3. Inertial Action Recognition Results) |
| By doing so, our model is able to learn and align features across multiple modalities, significantly enhancing both localization and action recognition accuracy. | definition/direction/unit from same section | p. 7 (5.4. Ablation Studies) |
| From the visualization results, we observe that RoNIN suffers from cumulative errors, causing its predicted location to drift outside the point cloud boundary after ... | definition/direction/unit from same section | p. 8 (5.5. Qualitative evaluations) |
| These include analyses on different vision-language encoders in Stage 1, the preliminary location retrieval accuracy in Stage 1, different architecture designs in Stage 2, ... | definition/direction/unit from same section | p. 8 (5.4. Ablation Studies) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Baselines RoNIN [22] learns to predict velocity from IMU signals. | comparison identity and matched condition | p. 5 (5.2. Inertial Localization Results) |
| 1, direct location prediction methods outperform velocity accumulation methods. | comparison identity and matched condition | p. 6 (5.2. Inertial Localization Results) |
| Baselines DeepConvLSTM [44] uses convolutional networks and LSTMs to classify actions from IMU signals. | comparison identity and matched condition | p. 6 (5.3. Inertial Action Recognition Results) |
| Figure 1. Egocentric Action-aware Inertial Localization (EAIL). Our framework leverages egocentric action cues obtained from the head-mounted IMU to perform inertial localization in the ... | comparison identity and matched condition | p. 1 (Figure/Table caption) |
| Location-Aware Action Recognition Ablation Study. "PC" denotes point cloud features, and "LA" represents location attention. | comparison identity and matched condition | p. 7 (5.4. Ablation Studies) |
| Furthermore, even in scenarios where action caption annotations are unavailable in the training set, our method does not fail, ensuring reasonable accuracy without relying ... | comparison identity and matched condition | p. 7 (5.4. Ablation Studies) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Location-Aware Action Recognition Ablation Study. "PC" denotes point cloud features, and "LA" represents location attention. | component/input/data sensitivity | p. 7 (5.4. Ablation Studies) |
| Furthermore, even in scenarios where action caption annotations are unavailable in the training set, our method does not fail, ensuring reasonable accuracy without relying ... | component/input/data sensitivity | p. 7 (5.4. Ablation Studies) |
| More Ablation Results in Supplementary Material Further ablation results can be found in Tab. | component/input/data sensitivity | p. 8 (5.4. Ablation Studies) |
| IMU2CLIP [41] uses a strategy similar to our Stage 1, employing a pretrained CLIP model [43, 50] to guide IMU feature extraction and fine-tuning ... | component/input/data sensitivity | p. 6 (5.3. Inertial Action Recognition Results) |
| Figure 2. Short-Term Action-Location Alignment. In this first stage, our objective is to train a point cloud encoder and an IMU encoder using contrastive ... | component/input/data sensitivity | p. 3 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In summary, our main contributions are as follows: • We introduce EAIL, a novel inertial localization framework that leverages egocentric action cues from headmounted ... | Table 1. Inertial Localization Results. We evaluate the accuracy using two metrics: the localization success rate (%) at various error distance thresholds and the ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (Figure/Table caption), p. 8 (5.4. Ablation Studies), p. 8 (5.4. Ablation Studies), p. 5 (5.1. Experimental Setup), p. 6 (5.2. Inertial Localization Results), p. 7 (5.4. Ablation Studies) |
| Primary metric/result | 4, using only IMU signals, we achieve results comparable to IMU2CLIP [41]. | numeric claim only at cited anchor | p. 8 (5.4. Ablation Studies) |

- Numeric sentences retained from the body:
- **p. 5 / 5.1. Experimental Setup - extractive PDF cue:** For this paper, we used the cooking activities subset, which includes 173 participants across 60 kitchens, totaling 564.13 hours of recordings.
- **p. 5 / 5.1. Experimental Setup - extractive PDF cue:** The activity area for these cooking activities averaged around 2.8 meters per side, with the largest spanning 6.15 meters.
- **p. 5 / 5.1. Experimental Setup - extractive PDF cue:** Each local 1 m2 point cloud is sub-sampled to contain 8192 points, and the IMU signals are recorded at an 800 Hz sample rate.
- **p. 5 / 5.1. Experimental Setup - extractive PDF cue:** The IMU signals are preprocessed following [22] and downsampled to 400 Hz.
- **p. 5 / 5.1. Experimental Setup - extractive PDF cue:** We trained Stage 1 for 250 epochs and Stage 2 for 100 epochs, using a batch size of 64, a learning rate of 10^{-3} , ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Furthermore, even in scenarios where action caption annotations are unavailable in the training set, our method does not fail, ensuring reasonable accuracy without relying ... | p. 7 (5.4. Ablation Studies) |
| body limitation/failure cue | While our method can robustly exploit head-mounted IMU signals for human localization within pre-built point clouds, it does hinge on several factors that present ... | p. 8 (6. Limitations and Future Directions) |
| body limitation/failure cue | Finally, our experiments are based on IMU data from head-mounted devices, and substantially different sensor placements (e.g., ankle or wrist) may necessitate model adaptations ... | p. 8 (6. Limitations and Future Directions) |
| body limitation/failure cue | Nevertheless, its lack of spatial awareness still leads to reduced accuracy, whereas our approach leverages point cloud structures to deliver robust inertial localization across ... | p. 6 (5.2. Inertial Localization Results) |
| body limitation/failure cue | To accomplish this, we leverage the power of robust pre-trained and prealigned vision-language models, such as [43, 50]. | p. 7 (5.4. Ablation Studies) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We trained Stage 1 for 250 epochs and Stage 2 for 100 epochs, using a batch size of 64, a learning rate of 10^{-3} ... | p. 5 (5.1. Experimental Setup) |
| Implementation Details In Stage 1, we employed an enhanced version of the CLIP model [43] as the visionlanguage encoder. | p. 5 (5.1. Experimental Setup) |
| Modalities Engagement for Action-aware Alignment In Stage 1 of our framework, we focus on effectively training the IMU and the point cloud encoders to ... | p. 7 (5.4. Ablation Studies) |
| The heatmap from Stage 1 reflects the direct similarity strength between the features generated by the IMU encoder and the point cloud encoder. | p. 8 (5.5. Qualitative evaluations) |
| These include analyses on different vision-language encoders in Stage 1, the preliminary location retrieval accuracy in Stage 1, different architecture designs in Stage 2, ... | p. 8 (5.4. Ablation Studies) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / 5.4. Ablation Studies - extractive PDF cue:** Furthermore, even in scenarios where action caption annotations are unavailable in the training set, our method does not fail, ensuring reasonable accuracy without relying on ...
- **p. 8 / 6. Limitations and Future Directions - extractive PDF cue:** While our method can robustly exploit head-mounted IMU signals for human localization within pre-built point clouds, it does hinge on several factors that present avenues ...
- **p. 8 / 6. Limitations and Future Directions - extractive PDF cue:** Finally, our experiments are based on IMU data from head-mounted devices, and substantially different sensor placements (e.g., ankle or wrist) may necessitate model adaptations for ...
- **p. 6 / 5.2. Inertial Localization Results - extractive PDF cue:** Nevertheless, its lack of spatial awareness still leads to reduced accuracy, whereas our approach leverages point cloud structures to deliver robust inertial localization across diverse ...
- **p. 7 / 5.4. Ablation Studies - extractive PDF cue:** To accomplish this, we leverage the power of robust pre-trained and prealigned vision-language models, such as [43, 50].

- **PDF anchors reviewed:** datasets p. 5 (5.1. Experimental Setup), p. 5 (5.1. Experimental Setup), p. 7 (5.4. Ablation Studies), p. 6 (5.2. Inertial Localization Results), p. 8 (5.4. Ablation Studies), p. 7 (5.4. Ablation Studies), metrics p. 6 (5.2. Inertial Localization Results), p. 5 (5.1. Experimental Setup), p. 5 (5.1. Experimental Setup), p. 6 (5.2. Inertial Localization Results), p. 7 (5.3. Inertial Action Recognition Results), p. 7 (5.4. Ablation Studies), baselines p. 5 (5.2. Inertial Localization Results), p. 6 (5.2. Inertial Localization Results), p. 6 (5.3. Inertial Action Recognition Results), p. 1 (Figure/Table caption), p. 7 (5.4. Ablation Studies), p. 7 (5.4. Ablation Studies), results p. 6 (Figure/Table caption), p. 8 (5.4. Ablation Studies), p. 8 (5.4. Ablation Studies), p. 5 (5.1. Experimental Setup), p. 6 (5.2. Inertial Localization Results), p. 7 (5.4. Ablation Studies).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
