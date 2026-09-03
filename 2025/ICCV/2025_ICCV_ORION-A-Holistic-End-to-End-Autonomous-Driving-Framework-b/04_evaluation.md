# Evaluation - ORION: A Holistic End-to-End Autonomous Driving Framework by Vision-Language Instructed Action Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/ICCV2025/html/Fu_ORION_A_Holistic_End-to-End_Autonomous_Driving_Framework_by_Vision-Language_Instructed_ICCV_2025_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/ICCV2025/papers/Fu_ORION_A_Holistic_End-to-End_Autonomous_Driving_Framework_by_Vision-Language_Instructed_ICCV_2025_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (4.5. Ablation Study), p. 6 (25.00 71.11 78.33 30.00 69.15 54.72(+16.12)), p. 6 (25.00 71.11 78.33 30.00 69.15 54.72(+16.12)), p. 8 (4.5. Ablation Study), p. 7 (Figure/Table caption), p. 5 (4.1. Dataset and Evaluation Metrics)): By leveraging explicit traffic state supervision (ID-2), ORION achieves 74.65 DS and 49.31% SR, which already outperforms DriveAdapter [22] and DriveTRansformer [25] by a large margin and makes an improvement ...

## Evaluation Body Digest

- **p. 5 / 4.1. Dataset and Evaluation Metrics - extractive body cue:** Additionally, we compare our method with other baselines on nuScenes [7] open-loop evaluation (details in Appendix).
- **p. 5 / 4.1. Dataset and Evaluation Metrics - extractive body cue:** We train and evaluate ORION on the Bench2drive dataset [24], a closed-loop evaluation protocol under CARLA V2 [12] for E2E autonomous driving.
- **p. 8 / 4.5. Ablation Study - extractive body cue:** The slight degradation on DS may be caused by the trade-off between DS and SR in the CARLA benchmark protocol [74].
- **p. 8 / 4.5. Ablation Study - extractive body cue:** Furthermore, the results also validate the high quality and validity of the Chat-B2D dataset produced by our auto-pipeline.
- **p. 7 / 4.5. Ablation Study - extractive body cue:** The brown, red, and green refer to the action decision, the objects that influence driving decisions, and the prediction trajectory, respectively.
- **p. 6 / 4.4. Qualitative Results - extractive body cue:** It shows both the driving action reasoning and trajectory prediction outputted by our model, as well as the corresponding ego-vehicle states.
- **p. 6 / 4.4. Qualitative Results - extractive body cue:** We observe that ORION can capture the correct causal relationship in the scenario and make correct driving decisions, then predict the planning trajectory following the ...
- **p. 7 / 4.5. Ablation Study - extractive body cue:** Note that VAE-based trajectory generTable 2.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** 3D scene/object와 robot coordinate frame.
- **Input boundary:** RGB-D, image set, point cloud, depth와 camera pose.
- **Output/decision under evaluation:** point map, pose, scene graph, affordance 또는 query result.
- **Primary target:** geometric accuracy, semantic consistency와 planning/manipulation utility.
- **Detected evaluation headings:** 4. Experiments (p. 5); 4.1. Dataset and Evaluation Metrics (p. 5); 4.2. Implementation Details (p. 5); 4.3. Main Results (p. 5); 4.4. Qualitative Results (p. 6).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4.5. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | By leveraging explicit traffic state supervision (ID-2), ORION achieves 74.65 DS and 49.31% SR, which already outperforms DriveAdapter [22] and DriveTRansformer [25] by a ... | p. 7 (4.5. Ablation Study) |
| 25.00 71.11 78.33 30.00 69.15 54.72(+16.12) | EMPIRICAL / SOURCE-REPORTED EVALUATION | ORION achieves +16.12% and +12.64% performance improvements compared with DriveTransformer [25] and DriveAdapter [22] in the average ability, respectively. | p. 6 (25.00 71.11 78.33 30.00 69.15 54.72(+16.12)) |
| 25.00 71.11 78.33 30.00 69.15 54.72(+16.12) | EMPIRICAL / SOURCE-REPORTED EVALUATION | achieves improvements of +13.52 DS and +21.54% SR over DriveAdapter [22], even if DriveAdapter distills the expert feature from Think2Drive [30] and accepts two ... | p. 6 (25.00 71.11 78.33 30.00 69.15 54.72(+16.12)) |
| 4.5. Ablation Study | EMPIRICAL / SOURCE-REPORTED EVALUATION | Meanwhile, with the same QT-former designs, our ORION framework achieves further improvements of 35.51 Table 5. | p. 8 (4.5. Ablation Study) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 5. Advantages of the vision-language instructed action gen- eration. DS and SR denote Driving Score and Success Rate sepa- rately. VAD [26] is ... | p. 7 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / 4.1. Dataset and Evaluation Metrics - extractive body cue:** Additionally, we compare our method with other baselines on nuScenes [7] open-loop evaluation (details in Appendix).
- **p. 5 / 4.1. Dataset and Evaluation Metrics - extractive body cue:** We train and evaluate ORION on the Bench2drive dataset [24], a closed-loop evaluation protocol under CARLA V2 [12] for E2E autonomous driving.
- **p. 8 / 4.5. Ablation Study - extractive body cue:** The slight degradation on DS may be caused by the trade-off between DS and SR in the CARLA benchmark protocol [74].
- **p. 8 / 4.5. Ablation Study - extractive body cue:** Furthermore, the results also validate the high quality and validity of the Chat-B2D dataset produced by our auto-pipeline.
- **p. 7 / 4.5. Ablation Study - extractive body cue:** The brown, red, and green refer to the action decision, the objects that influence driving decisions, and the prediction trajectory, respectively.
- **p. 6 / 4.4. Qualitative Results - extractive body cue:** It shows both the driving action reasoning and trajectory prediction outputted by our model, as well as the corresponding ego-vehicle states.
- **p. 6 / 4.4. Qualitative Results - extractive body cue:** We observe that ORION can capture the correct causal relationship in the scenario and make correct driving decisions, then predict the planning trajectory following the ...
- **p. 7 / 4.5. Ablation Study - extractive body cue:** Note that VAE-based trajectory generTable 2.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1. The comparison of different E2E paradigms. Our ORION framework establishes the differentiable connection be- tween reasoning and action space via the generative planner. ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2. The pipeline of our ORION, a holistic E2E framework aligning vision-reasoning-action space. It consists of three key compo- nents: a QT-Former to extract ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3. The detailed architecture of QT-Former. It accepts di- verse queries and image features as inputs to detect traffic ele- ments, predict motion, and ...
- **p. 6 / Figure/Table caption - extractive body cue:** Table 1. Closed-loop, Open-loop and Multi-Ability Results of E2E-AD Methods in Bench2Drive under base set. C/L refers to cam- era/LiDAR. Avg.L2 is averaged over the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4. It shows both the driving action reasoning and tra- jectory prediction outputted by our model, as well as the corresponding ego-vehicle states. We ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 4. Qualitative results of ORION on the Bench2Drive closed-loop evaluation set. The brown, red, and green refer to the action decision, the objects that ...
- **p. 7 / Figure/Table caption - extractive body cue:** Figure 5. Advantages of the vision-language instructed action gen- eration. DS and SR denote Driving Score and Success Rate sepa- rately. VAD [26] is a ...
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2. Ablation on diverse generative planner. DS and SR denote Driving Score and Success Rate separately. Generative Planner Closed-loop Open-loop Ability DS↑

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Additionally, we compare our method with other baselines on nuScenes [7] open-loop evaluation (details in Appendix). | embodiment, simulator version and control stack | p. 5 (4.1. Dataset and Evaluation Metrics), p. 5 (4.1. Dataset and Evaluation Metrics) |
| Task/environment | We train and evaluate ORION on the Bench2drive dataset [24], a closed-loop evaluation protocol under CARLA V2 [12] for E2E autonomous driving. | reset, timeout, object/scene variation | p. 5 (4.1. Dataset and Evaluation Metrics), p. 8 (4.5. Ablation Study) |
| Observation/sensor | RGB-D, image set, point cloud, depth와 camera pose | calibration, preprocessing, privileged input | p. 4 (3.2. Large Language Model), p. 5 (3.3. Generative Planner) |
| Output/decision | point map, pose, scene graph, affordance 또는 query result | action frame, controller and termination | p. 2 (1. Introduction), p. 2 (1. Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Bench2drive includes five metrics for closed-loop evaluation: Driving Score (DS), Success Rate (SR), Efficiency, Comfortness, and Multi-Ability. | definition/direction/unit from same section | p. 5 (4.1. Dataset and Evaluation Metrics) |
| Ref: Reference, Con: Condition, Mod: modality, NC: navigation command, TP: target point, DS: Driving Score, SR: Success Rate, Eff: Efficiency, Com: Comfortness, M: Merging, ... | definition/direction/unit from same section | p. 6 (4.3. Main Results) |
| DS and SR denote Driving Score and Success Rate separately. | definition/direction/unit from same section | p. 7 (4.5. Ablation Study) |
| For open-loop evaluation, we use the L2 distance error and the collision rate. | definition/direction/unit from same section | p. 5 (4.1. Dataset and Evaluation Metrics) |
| Specifically, our model demonstrates outstanding performance in some scenarios, such as Overtaking (71.11%), Emergency Brake (78.33%), and Traffic Sign (69.15%), which shows that our ... | definition/direction/unit from same section | p. 6 (25.00 71.11 78.33 30.00 69.15 54.72(+16.12)) |
| Diffusion 71.97 46.54 0.73 0.96 46.68 VAE (Ours) 77.74 54.62 0.68 0.47 54.72 ation demonstrates a significant performance improvement over the diffusion-based. | definition/direction/unit from same section | p. 7 (4.5. Ablation Study) |
| Then, we combine the motion prediction module in the QT-Former's perception head, which gains a slight improvement of +0.4% SR and further reduces the ... | definition/direction/unit from same section | p. 8 (4.5. Ablation Study) |
| Specifically, the multi-task training leads to improvements of +3.64 DS and +9.66% SR in the planning task, as well as a performance gain of ... | definition/direction/unit from same section | p. 8 (4.5. Ablation Study) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| By leveraging explicit traffic state supervision (ID-2), ORION achieves 74.65 DS and 49.31% SR, which already outperforms DriveAdapter [22] and DriveTRansformer [25] by a ... | comparison identity and matched condition | p. 7 (4.5. Ablation Study) |
| It provides an official training set where we use the base set (1000 clips) for fair comparison with all the other baselines, which is ... | comparison identity and matched condition | p. 5 (4.1. Dataset and Evaluation Metrics) |
| Additionally, we compare our method with other baselines on nuScenes [7] open-loop evaluation (details in Appendix). | comparison identity and matched condition | p. 5 (4.1. Dataset and Evaluation Metrics) |
| Compared with the plain text paradigm, the dual-system paradigm only obtains a slight performance improvement. | comparison identity and matched condition | p. 6 (4.5. Ablation Study) |
| ORION achieves +16.12% and +12.64% performance improvements compared with DriveTransformer [25] and DriveAdapter [22] in the average ability, respectively. | comparison identity and matched condition | p. 6 (25.00 71.11 78.33 30.00 69.15 54.72(+16.12)) |
| We argue the main reasons are as follows: 1) Compared with the conditional denoising process of diffusion, the latent space of VAE more directly ... | comparison identity and matched condition | p. 7 (4.5. Ablation Study) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We then investigate the effect of employing different generative planners to bridge the reasoning-action space. | component/input/data sensitivity | p. 7 (4.5. Ablation Study) |
| To ensure the fairness of the ablations, experiments of different paradigms use the same sensor inputs, vision encoder, QT-former, and VLM as our ORION ... | component/input/data sensitivity | p. 6 (4.5. Ablation Study) |
| Ablation on diverse generative planner. | component/input/data sensitivity | p. 7 (4.5. Ablation Study) |
| Ablation of history queries number. | component/input/data sensitivity | p. 8 (4.5. Ablation Study) |
| Ablation on QT-Former designs in different frameworks. | component/input/data sensitivity | p. 8 (4.5. Ablation Study) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To tackle this problem, we propose a hOlistic E2E autonomous dRiving framework by vIsion-language instructed actiON generation, termed ORION. | By leveraging explicit traffic state supervision (ID-2), ORION achieves 74.65 DS and 49.31% SR, which already outperforms DriveAdapter [22] and DriveTRansformer [25] by a ... | PDF body cue; verify exact table/figure and matched conditions | p. 7 (4.5. Ablation Study), p. 6 (25.00 71.11 78.33 30.00 69.15 54.72(+16.12)), p. 6 (25.00 71.11 78.33 30.00 69.15 54.72(+16.12)), p. 8 (4.5. Ablation Study), p. 7 (Figure/Table caption), p. 5 (4.1. Dataset and Evaluation Metrics) |
| Primary metric/result | ORION achieves +16.12% and +12.64% performance improvements compared with DriveTransformer [25] and DriveAdapter [22] in the average ability, respectively. | numeric claim only at cited anchor | p. 6 (25.00 71.11 78.33 30.00 69.15 54.72(+16.12)) |

- Numeric sentences retained from the body:
- **p. 5 / 4.1. Dataset and Evaluation Metrics - extractive body cue:** Each clip captures approximately 150 meters of continuous driving within a specific traffic scene.
- **p. 6 / 4.3. Main Results - extractive body cue:** Avg.L2 is averaged over the predictions in 2 seconds under 2Hz, similar to UniAD. * denote expert feature distillation.
- **p. 7 / 4.5. Ablation Study - extractive body cue:** T=0.00s, V=5.02m/s T=0.25s, V=4.19m/s T=1.00s, V=0.05m/s T=2.00s, V=2.67m/s T=3.00s, V=5.04m/s T=0.00s, V=0.00m/s T=4.50s, V=4.92m/s T=6.50s, V=4.85m/s T=7.50s, V=0.26m/s T=9.50s, V=5.12m/s You should keep and lanefollow. ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | For open-loop evaluation, we use the L2 distance error and the collision rate. | p. 5 (4.1. Dataset and Evaluation Metrics) |
| body limitation/failure cue | On the other hand, our model falls behind DriveAdapter in Merging and Give Way, which shows that ORION is not good at making lane-changing ... | p. 6 (25.00 71.11 78.33 30.00 69.15 54.72(+16.12)) |
| body limitation/failure cue | The plain text paradigm performs the worst (42.23 DS, 13.14% SR, and 15.39% mean ability), indicating the limitations of plain text output in closed-loop ... | p. 6 (4.5. Ablation Study) |
| body limitation/failure cue | The model cannot obtain both reasoning and planning capabilities with single-task training. | p. 8 (4.5. Ablation Study) |
| body limitation/failure cue | Then, we combine the motion prediction module in the QT-Former's perception head, which gains a slight improvement of +0.4% SR and further reduces the ... | p. 8 (4.5. Ablation Study) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Following Omnidrive [61], we adopt EVA-02-L [13] as the vision encoder. | p. 5 (4.2. Implementation Details) |
| Although the effectiveness of the MLP decoder paradigm has 24828 | p. 6 (4.5. Ablation Study) |
| VAD [26]) outputs guided by elaborated design VLM interface (e.g. meta-action) [27], and (c) special token decode outputs by MLP [47], as shown in ... | p. 6 (4.5. Ablation Study) |
| Additionally, the MLP-decoder struggles with handling multi-modal trajectory [9, 21], making it still significantly lag behind ORION in closed-loop evaluation. | p. 7 (4.5. Ablation Study) |
| 2, ORION first encodes the image tokens with a vision encoder. | p. 3 (3. Method) |
| To compress and extract multi-view image features Fm derived from the vision encoder while achieving long-term information modeling, we introduce QT-Former, a querybased temporal ... | p. 3 (3.1. QT-Former) |
| To construct p(a / s), there are many excellent methods in the generation field (e.g., variational autoencoders (VAE) [29] and diffusion model [49]). | p. 4 (3.3. Generative Planner) |
| 2, the user instruction Xq, including scene description, history information review, scene analysis, and action reasoning, is first encoded into language tokens xq ∈RL×C ... | p. 4 (3.2. Large Language Model) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / 4.1. Dataset and Evaluation Metrics - extractive body cue:** For open-loop evaluation, we use the L2 distance error and the collision rate.
- **p. 6 / 25.00 71.11 78.33 30.00 69.15 54.72(+16.12) - extractive body cue:** On the other hand, our model falls behind DriveAdapter in Merging and Give Way, which shows that ORION is not good at making lane-changing decisions.
- **p. 6 / 4.5. Ablation Study - extractive body cue:** The plain text paradigm performs the worst (42.23 DS, 13.14% SR, and 15.39% mean ability), indicating the limitations of plain text output in closed-loop driving ...
- **p. 8 / 4.5. Ablation Study - extractive body cue:** The model cannot obtain both reasoning and planning capabilities with single-task training.
- **p. 8 / 4.5. Ablation Study - extractive body cue:** Then, we combine the motion prediction module in the QT-Former's perception head, which gains a slight improvement of +0.4% SR and further reduces the collision ...

- **Evidence anchors reviewed:** datasets p. 5 (4.1. Dataset and Evaluation Metrics), p. 5 (4.1. Dataset and Evaluation Metrics), p. 8 (4.5. Ablation Study), p. 8 (4.5. Ablation Study), p. 7 (4.5. Ablation Study), p. 6 (4.4. Qualitative Results), metrics p. 5 (4.1. Dataset and Evaluation Metrics), p. 6 (4.3. Main Results), p. 7 (4.5. Ablation Study), p. 5 (4.1. Dataset and Evaluation Metrics), p. 6 (25.00 71.11 78.33 30.00 69.15 54.72(+16.12)), p. 7 (4.5. Ablation Study), baselines p. 7 (4.5. Ablation Study), p. 5 (4.1. Dataset and Evaluation Metrics), p. 5 (4.1. Dataset and Evaluation Metrics), p. 6 (4.5. Ablation Study), p. 6 (25.00 71.11 78.33 30.00 69.15 54.72(+16.12)), p. 7 (4.5. Ablation Study), results p. 7 (4.5. Ablation Study), p. 6 (25.00 71.11 78.33 30.00 69.15 54.72(+16.12)), p. 6 (25.00 71.11 78.33 30.00 69.15 54.72(+16.12)), p. 8 (4.5. Ablation Study), p. 7 (Figure/Table caption), p. 5 (4.1. Dataset and Evaluation Metrics).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
