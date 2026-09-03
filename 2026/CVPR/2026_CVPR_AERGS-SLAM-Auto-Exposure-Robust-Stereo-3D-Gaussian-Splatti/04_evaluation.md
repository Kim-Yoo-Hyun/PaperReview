# Evaluation - AERGS-SLAM: Auto-Exposure-Robust Stereo 3D Gaussian Splatting SLAM

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_AERGS-SLAM_Auto-Exposure-Robust_Stereo_3D_Gaussian_Splatting_SLAM_CVPR_2026_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2026/papers/Zhou_AERGS-SLAM_Auto-Exposure-Robust_Stereo_3D_Gaussian_Splatting_SLAM_CVPR_2026_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.3. Results and Evaluation), p. 7 (4.3. Results and Evaluation), p. 8 (4.4. Ablation Studies), p. 8 (4.4. Ablation Studies), p. 4 (Figure/Table caption), p. 5 (4. Experiments)): Secondly, on the self-collected dataset, AERGS-SLAM achieves significantly higher localization accuracy than all baselines, confirming its generalization to real-world scenarios.

## Evaluation Body Digest

- **p. 7 / 4.3. Results and Evaluation - extractive body cue:** Secondly, on the self-collected dataset, AERGS-SLAM achieves significantly higher localization accuracy than all baselines, confirming its generalization to real-world scenarios.
- **p. 7 / 4.3. Results and Evaluation - extractive body cue:** These results further demonstrate the generalization capability of the CEN in real-world scenarios.
- **p. 8 / 4.4. Ablation Studies - extractive body cue:** Experiments are conducted on the processed EuRoC and self-collected datasets.
- **p. 8 / 4.4. Ablation Studies - extractive body cue:** Moreover, as shown in the rows (2) and (4) of Table 3, applying the CEN module increases the PSNR metric by more than 5 dB ...
- **p. 5 / 4.1. Implementation Details - extractive body cue:** These keyframes act as the training set, with remaining frames used as the testing set.
- **p. 7 / 4.3. Results and Evaluation - extractive body cue:** Additionally, compared with MonoGS [26], all decoupled pipelines achieve superior accuracy, highlighting the robustness of the decoupled framework.
- **p. 8 / 4.4. Ablation Studies - extractive body cue:** This is because higher localization accuracy can provide the mapping module with more accurate Gaussian ellipsoids and camera poses, thereby improving the accuracy of photorealistic ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Estimated CRF and exposure-controlled renderings. Top row: recovered CRF curves (i.e., ours and HDR-GS [2]) and ren- dered scene radiance map. Bottom row: ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Implementation Details (p. 5); 4.2. Experiment Setup (p. 5); 4.3. Results and Evaluation (p. 7); Datasets (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.3. Results and Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | Secondly, on the self-collected dataset, AERGS-SLAM achieves significantly higher localization accuracy than all baselines, confirming its generalization to real-world scenarios. | p. 7 (4.3. Results and Evaluation) |
| 4.3. Results and Evaluation | EMPIRICAL / REAL-ROBOT OR HARDWARE | On the processed EuRoC dataset [1], AERGS-SLAM achieves the best localization performance against 3DGS-based baselines. | p. 7 (4.3. Results and Evaluation) |
| 4.4. Ablation Studies | EMPIRICAL / REAL-ROBOT OR HARDWARE | Firstly, as shown in the rows (3) and (5) of Table 3, the employment of the CEN module significantly enhances the quality of photometric ... | p. 8 (4.4. Ablation Studies) |
| 4.4. Ablation Studies | EMPIRICAL / REAL-ROBOT OR HARDWARE | Moreover, with the improvement of localization accuracy, the PSNR metric is further enhanced. | p. 8 (4.4. Ablation Studies) |
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Figure 4. Exposure modeling in HDR-GS [2] and the proposed method. The differences between them are: 1) HDR-GS uses a network to map per-Gaussian ... | p. 4 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 7 / 4.3. Results and Evaluation - extractive body cue:** Secondly, on the self-collected dataset, AERGS-SLAM achieves significantly higher localization accuracy than all baselines, confirming its generalization to real-world scenarios.
- **p. 7 / 4.3. Results and Evaluation - extractive body cue:** These results further demonstrate the generalization capability of the CEN in real-world scenarios.
- **p. 8 / 4.4. Ablation Studies - extractive body cue:** Experiments are conducted on the processed EuRoC and self-collected datasets.
- **p. 8 / 4.4. Ablation Studies - extractive body cue:** Moreover, as shown in the rows (2) and (4) of Table 3, applying the CEN module increases the PSNR metric by more than 5 dB ...
- **p. 5 / 4.1. Implementation Details - extractive body cue:** These keyframes act as the training set, with remaining frames used as the testing set.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. Estimated CRF and exposure-controlled renderings. Top row: recovered CRF curves (i.e., ours and HDR-GS [2]) and ren- dered scene radiance map. Bottom row: ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of the proposed AERGS-SLAM. Firstly, the localization thread performs illumination-robust localization using stereo images, generating posed keyframes and sparse point clouds to ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Feature detection in illumination-varying scene. handcrafted features [3] lack sufficient robustness to such appearance variations, reducing the reliability of residual E(k, j). As ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 4. Exposure modeling in HDR-GS [2] and the proposed method. The differences between them are: 1) HDR-GS uses a network to map per-Gaussian radiance ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 5. Exposure-controlled RGB renderings of CEN and HDR- GS [2] under varying exposure times ∆t. where SSIM(Ic, Ic gt) denotes structural similarity between the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative results of localization (RMSE ↓). We color code eac column as best and second best. 'X' denotes running failure in our experiments. ...
- **p. 6 / Figure/Table caption - extractive body cue:** Figure 6. Qualitative comparison of diverse systems from EuRoC MAV and our self-collected dataset. CEN's effectiveness; 4) ORB-SLAM3 [3], a classic hand- crafted feature-based SLAM ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Quantitative results of Photorealistic mapping results. We color code each column as best and second best. 'X' denotes running failure in our experiments. ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Secondly, on the self-collected dataset, AERGS-SLAM achieves significantly higher localization accuracy than all baselines, confirming its generalization to real-world scenarios. | embodiment, simulator version and control stack | p. 7 (4.3. Results and Evaluation), p. 7 (4.3. Results and Evaluation) |
| Task/environment | These results further demonstrate the generalization capability of the CEN in real-world scenarios. | reset, timeout, object/scene variation | p. 7 (4.3. Results and Evaluation), p. 8 (4.4. Ablation Studies) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 6 (Method), p. 1 (1. Introduction) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 1 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Additionally, compared with MonoGS [26], all decoupled pipelines achieve superior accuracy, highlighting the robustness of the decoupled framework. | definition/direction/unit from same section | p. 7 (4.3. Results and Evaluation) |
| Secondly, on the self-collected dataset, AERGS-SLAM achieves significantly higher localization accuracy than all baselines, confirming its generalization to real-world scenarios. | definition/direction/unit from same section | p. 7 (4.3. Results and Evaluation) |
| This is because higher localization accuracy can provide the mapping module with more accurate Gaussian ellipsoids and camera poses, thereby improving the accuracy of ... | definition/direction/unit from same section | p. 8 (4.4. Ablation Studies) |
| Figure 1. Estimated CRF and exposure-controlled renderings. Top row: recovered CRF curves (i.e., ours and HDR-GS [2]) and ren- dered scene radiance map. Bottom ... | definition/direction/unit from same section | p. 1 (Figure/Table caption) |
| The localization module generates sparse point clouds and posed keyframes, which are fed to the mapping module to initialize Gaussian ellipsoids and train the ... | definition/direction/unit from same section | p. 5 (4.1. Implementation Details) |
| Figure 2. Overview of the proposed AERGS-SLAM. Firstly, the localization thread performs illumination-robust localization using stereo images, generating posed keyframes and sparse point clouds ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Moreover, with the improvement of localization accuracy, the PSNR metric is further enhanced. | definition/direction/unit from same section | p. 8 (4.4. Ablation Studies) |
| The learning rate for Gaussian parameters follows PhotoSLAM [14]. | definition/direction/unit from same section | p. 5 (4.1. Implementation Details) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We compare AERGS-SLAM with seven baselines: 1) MonoGS [26], a state-of-the-art (SOTA) coupled 3DGS-based SLAM method; 2) Photo-SLAM [14] and SEGS-SLAM [37], representative decoupled ... | comparison identity and matched condition | p. 5 (4.2. Experiment Setup) |
| For the EuRoC dataset [1], AERGS-SLAM outperforms Photo-SLAM [14] without using any exposure mechanism, SEGS-SLAM utilizing appearance embedding, and MonoGS utilizing learnable exposure parameters. | comparison identity and matched condition | p. 7 (4.3. Results and Evaluation) |
| Moreover, compared with HDR-GS [2], AERGS-SLAM performs better, as its esti40935 | comparison identity and matched condition | p. 7 (4.3. Results and Evaluation) |
| Figure 6. Qualitative comparison of diverse systems from EuRoC MAV and our self-collected dataset. CEN's effectiveness; 4) ORB-SLAM3 [3], a classic hand- crafted feature-based ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |
| We observe that, compared with HDR-GS, the proposed CEN can achieve higher-quality exposure-controlled renderings. | comparison identity and matched condition | p. 8 (Datasets) |
| Section 4.4 reports ablation studies. | comparison identity and matched condition | p. 5 (4. Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The ablation results are reported in Table 3 within Row (1) (i.e., without CTFO, CEN and IRL) corresponds to the original Photo-SLAM [14]. | component/input/data sensitivity | p. 8 (4.4. Ablation Studies) |
| These ablation results consistently demonstrate that the proposed time-aware coarse-to-fine optimization strategy can effectively improve the quality of photorealistic mapping. | component/input/data sensitivity | p. 8 (4.4. Ablation Studies) |
| We compare AERGS-SLAM with seven baselines: 1) MonoGS [26], a state-of-the-art (SOTA) coupled 3DGS-based SLAM method; 2) Photo-SLAM [14] and SEGS-SLAM [37], representative decoupled ... | component/input/data sensitivity | p. 5 (4.2. Experiment Setup) |
| Section 4.4 reports ablation studies. | component/input/data sensitivity | p. 5 (4. Experiments) |
| For the EuRoC dataset [1], AERGS-SLAM outperforms Photo-SLAM [14] without using any exposure mechanism, SEGS-SLAM utilizing appearance embedding, and MonoGS utilizing learnable exposure parameters. | component/input/data sensitivity | p. 7 (4.3. Results and Evaluation) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To summarize, the main contributions of this work are as follows: • We propose a camera exposure network that recovers the camera's CRF to ... | Secondly, on the self-collected dataset, AERGS-SLAM achieves significantly higher localization accuracy than all baselines, confirming its generalization to real-world scenarios. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.3. Results and Evaluation), p. 7 (4.3. Results and Evaluation), p. 8 (4.4. Ablation Studies), p. 8 (4.4. Ablation Studies), p. 4 (Figure/Table caption), p. 5 (4. Experiments) |
| Primary metric/result | On the processed EuRoC dataset [1], AERGS-SLAM achieves the best localization performance against 3DGS-based baselines. | numeric claim only at cited anchor | p. 7 (4.3. Results and Evaluation) |

- Numeric sentences retained from the body:
- **p. 8 / Datasets - extractive body cue:** (a) HDR-GS [2] with rendering speed of 416 FPS.
- **p. 8 / Datasets - extractive body cue:** (b) Ours with rendering speed of 3700 FPS.
- **p. 6 / Method - extractive body cue:** EuRoC MAV Self-collected MH01 MH03 V102 V103 V202 V203 S1 S2 S3 S4 S5 S6 ORB-SLAM3 [3] 0.044 X 0.088 X 0.125 1.522 0.359 0.523 ...
- **p. 7 / Method - extractive body cue:** 0 200 400 600 800 1000 1200 1400 Frame Index 0 25 50 75 100 125 Exposure Time (ms) Ground Truth Ours HDR-GS 0 200 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Table 1. Quantitative results of localization (RMSE ↓). We color code eac column as best and second best. 'X' denotes running failure in our ... | p. 6 (Figure/Table caption) |
| body limitation/failure cue | Extensive experiments show the IRL module significantly improves localization accuracy and robustness. | p. 8 (5. Conclusion) |
| body limitation/failure cue | It adopts a decoupled pipeline enabling illumination-robust localization and auto-exposurerobust photorealistic mapping. | p. 8 (5. Conclusion) |
| body limitation/failure cue | Figure 2. Overview of the proposed AERGS-SLAM. Firstly, the localization thread performs illumination-robust localization using stereo images, generating posed keyframes and sparse point clouds ... | p. 3 (Figure/Table caption) |
| body limitation/failure cue | Figure 3. Feature detection in illumination-varying scene. handcrafted features [3] lack sufficient robustness to such appearance variations, reducing the reliability of residual E(k, j). ... | p. 4 (Figure/Table caption) |
| body limitation/failure cue | Overall, these comprehensive evaluation results validate the effectiveness of our illumination-robust localization pipeline. | p. 7 (4.3. Results and Evaluation) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We run AERGS-SLAM and all baseline methods using their official implementations on a desktop computer equipped with an RTX 4090 24GB GPU, an Intel ... | p. 6 (Method) |
| The learning rate for Gaussian parameters follows PhotoSLAM [14]. | p. 5 (4.1. Implementation Details) |
| The learning rate for the MLP and exposure time are set to 0.001 and 0.02, respectively. | p. 5 (4.1. Implementation Details) |
| We color code eac column as best and second best. 'X' denotes running failure in our experiments. '-' denotes no results, as we use ... | p. 6 (Method) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Quantitative results of localization (RMSE ↓). We color code eac column as best and second best. 'X' denotes running failure in our experiments. ...
- **p. 8 / 5. Conclusion - extractive body cue:** Extensive experiments show the IRL module significantly improves localization accuracy and robustness.
- **p. 8 / 5. Conclusion - extractive body cue:** It adopts a decoupled pipeline enabling illumination-robust localization and auto-exposurerobust photorealistic mapping.
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. Overview of the proposed AERGS-SLAM. Firstly, the localization thread performs illumination-robust localization using stereo images, generating posed keyframes and sparse point clouds to ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 3. Feature detection in illumination-varying scene. handcrafted features [3] lack sufficient robustness to such appearance variations, reducing the reliability of residual E(k, j). As ...
- **p. 7 / 4.3. Results and Evaluation - extractive body cue:** Overall, these comprehensive evaluation results validate the effectiveness of our illumination-robust localization pipeline.

- **Evidence anchors reviewed:** datasets p. 7 (4.3. Results and Evaluation), p. 7 (4.3. Results and Evaluation), p. 8 (4.4. Ablation Studies), p. 8 (4.4. Ablation Studies), p. 5 (4.1. Implementation Details), metrics p. 7 (4.3. Results and Evaluation), p. 7 (4.3. Results and Evaluation), p. 8 (4.4. Ablation Studies), p. 1 (Figure/Table caption), p. 5 (4.1. Implementation Details), p. 3 (Figure/Table caption), baselines p. 5 (4.2. Experiment Setup), p. 7 (4.3. Results and Evaluation), p. 7 (4.3. Results and Evaluation), p. 6 (Figure/Table caption), p. 8 (Datasets), p. 5 (4. Experiments), results p. 7 (4.3. Results and Evaluation), p. 7 (4.3. Results and Evaluation), p. 8 (4.4. Ablation Studies), p. 8 (4.4. Ablation Studies), p. 4 (Figure/Table caption), p. 5 (4. Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
