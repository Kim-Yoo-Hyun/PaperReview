# Evaluation - Map Space Belief Prediction for Manipulation-Enhanced Mapping

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p039.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p039.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 14 (B. CNABU Implementation Details), p. 8 (B. Simulation Experiments), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 8 (B. Simulation Experiments), p. 7 (V. EXPERIMENTS)): The mfoU serves as a measure of the correctness of the predicitons, while the mECE measures the confidence calibration of these predictions, i.e., how well the predicted confidences align with ...

## Evaluation Body Digest

- **p. 14 / B. CNABU Implementation Details - extractive body cue:** The dataset for training o,, consists of 30,000 randomly sampled scenes, while the dataset for training a, consists of 11.700 pushes.
- **p. 14 / B. CNABU Implementation Details - extractive body cue:** Both datasets were split into train, validation and test splits at a ratio of 0.8:0.1:0.1, Dataset generation details are discussed in Sec.
- **p. 7 / A. Experimental Setup - extractive body cue:** The real-world setup is similar, but with a few notable differences.
- **p. 7 / B. Simulation Experiments - extractive body cue:** 10 and 11 in the Appendix. ‘The robot begins with a naive uniform map prior.
- **p. 13 / B. CNABU Implementation Details - extractive body cue:** For the manipulation CNABU, the robot trajectory ay is projected into an aligned map space that approximates the robot's swept volume, To calculate the robot's ...
- **p. 15 / B. CNABU Implementation Details - extractive body cue:** 14 shows the objects which were used to create the test scenes during our real world experiments.
- **p. 13 / B. CNABU Implementation Details - extractive body cue:** Ultimately, we learn om = om (A, RobotOccupancy (04 (t.)), RobotOccupancy (a (te))) ‘We use network architectures Similar to Georgakis et al.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** We perform four core experiments to evaluate our approach, First, we test in simulation to highlight our pipeline's improvements in map completeness and accuracy compared ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** mapped 3D environment과 mobile robot.
- **Input boundary:** camera/depth stream, pose, map와 language goal.
- **Output/decision under evaluation:** collision-free trajectory 또는 velocity command.
- **Primary target:** goal reach, safety, localization error와 replanning latency.
- **Detected evaluation headings:** V. EXPERIMENTS (p. 6); A. Experimental Setup (p. 7); B. Simulation Experiments (p. 7); A. Dataset Generation Details (p. 13); B. CNABU Implementation Details (p. 13).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| B. CNABU Implementation Details | EMPIRICAL / REAL-ROBOT OR HARDWARE | The mfoU serves as a measure of the correctness of the predicitons, while the mECE measures the confidence calibration of these predictions, i.e., how ... | p. 14 (B. CNABU Implementation Details) |
| B. Simulation Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Our method uses pushing to achieve significantly higher mloUs. | p. 8 (B. Simulation Experiments) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | We perform four core experiments to evaluate our approach, First, we test in simulation to highlight our pipeline's improvements in map completeness and accuracy ... | p. 6 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | anced Mapping agains tho, Our method outperforms all bese | p. 7 (V. EXPERIMENTS) |
| B. Simulation Experiments | EMPIRICAL / REAL-ROBOT OR HARDWARE | Note how our method aot only achieves better mloUs than any of the other methods it does | p. 8 (B. Simulation Experiments) |

## Dataset / Benchmark Role

- **p. 14 / B. CNABU Implementation Details - extractive body cue:** The dataset for training o,, consists of 30,000 randomly sampled scenes, while the dataset for training a, consists of 11.700 pushes.
- **p. 14 / B. CNABU Implementation Details - extractive body cue:** Both datasets were split into train, validation and test splits at a ratio of 0.8:0.1:0.1, Dataset generation details are discussed in Sec.
- **p. 7 / A. Experimental Setup - extractive body cue:** The real-world setup is similar, but with a few notable differences.
- **p. 7 / B. Simulation Experiments - extractive body cue:** 10 and 11 in the Appendix. ‘The robot begins with a naive uniform map prior.
- **p. 13 / B. CNABU Implementation Details - extractive body cue:** For the manipulation CNABU, the robot trajectory ay is projected into an aligned map space that approximates the robot's swept volume, To calculate the robot's ...
- **p. 15 / B. CNABU Implementation Details - extractive body cue:** 14 shows the objects which were used to create the test scenes during our real world experiments.
- **p. 13 / B. CNABU Implementation Details - extractive body cue:** Ultimately, we learn om = om (A, RobotOccupancy (04 (t.)), RobotOccupancy (a (te))) ‘We use network architectures Similar to Georgakis et al.
- **p. 6 / V. EXPERIMENTS - extractive body cue:** We perform four core experiments to evaluate our approach, First, we test in simulation to highlight our pipeline's improvements in map completeness and accuracy compared ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: From a prior map belie ou pipeline predicts « map belie resuling from a se of candidate pushes. I then weighs the information ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Real-world environment showing & shelf senerio. The URS is sipped with an Robetiq parallel jw gripper and a Realsense LS15 RGB-D camera to ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: Simulation tests of push selection altematives. Note how our method aot only achieves better mloUs than any of the other methods it does
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 7: Qualitative real-world experi
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 9: Simulation envionment configuration example of different YCB ‘objects in 4 confined shell scenario. The URS is equipped with sn Rabotig pealle-aw gripper
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 11: Frontal and (privileged) top-down views of a scene from the Slighly Oschad set (ht).
- **p. 15 / Figure/Table caption - extractive body cue:** Fig. 14: The set of objects used during the rel world experiments

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | The dataset for training o,, consists of 30,000 randomly sampled scenes, while the dataset for training a, consists of 11.700 pushes. | embodiment, simulator version and control stack | p. 14 (B. CNABU Implementation Details), p. 14 (B. CNABU Implementation Details) |
| Task/environment | Both datasets were split into train, validation and test splits at a ratio of 0.8:0.1:0.1, Dataset generation details are discussed in Sec. | reset, timeout, object/scene variation | p. 14 (B. CNABU Implementation Details), p. 7 (A. Experimental Setup) |
| Observation/sensor | camera/depth stream, pose, map와 language goal | calibration, preprocessing, privileged input | p. 3 (A. Overview), p. 3 (B. Mechanical Search in Shelves and Piles) |
| Output/decision | collision-free trajectory 또는 velocity command | action frame, controller and termination | p. 4 (B. Neural Map Belief Dynamics), p. 13 (B. CNABU Implementation Details) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We perform four core experiments to evaluate our approach, First, we test in simulation to highlight our pipeline's improvements in map completeness and accuracy ... | definition/direction/unit from same section | p. 6 (V. EXPERIMENTS) |
| Further evaluations, which validate the individual CNABU's performance and the use of VIG as a reward proxy, are provided in Appendices C and D. | definition/direction/unit from same section | p. 7 (V. EXPERIMENTS) |
| [11's pipeline does not update its belief after a push, it requires multiple subsequent observations to reconcile inconsistencies between the actual scene and the ... | definition/direction/unit from same section | p. 7 (B. Simulation Experiments) |
| The mfoU serves as a measure of the correctness of the predicitons, while the mECE measures the confidence calibration of these predictions, i.e., how ... | definition/direction/unit from same section | p. 14 (B. CNABU Implementation Details) |
| Standard deviation of performance of random haslies is epreseated 3s shading | definition/direction/unit from same section | p. 8 (B. Simulation Experiments) |
| For each network, we report their mean Intersection over Union and their mean Expected Calibration Error (mECE) [28] for both the semantic and occuancy ... | definition/direction/unit from same section | p. 14 (B. CNABU Implementation Details) |
| Fig. 2: From a prior map belie ou pipeline predicts « map belie resuling from a se of candidate pushes. I then weighs the ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Each CNABU implements a preprocessing step to encode actions and observations in a representation aligned to the ‘map grid. | definition/direction/unit from same section | p. 13 (B. CNABU Implementation Details) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| We perform four core experiments to evaluate our approach, First, we test in simulation to highlight our pipeline's improvements in map completeness and accuracy ... | comparison identity and matched condition | p. 6 (V. EXPERIMENTS) |
| Next, we present a series of ablations of our method and evaluate several interactive baselines. | comparison identity and matched condition | p. 6 (V. EXPERIMENTS) |
| anced Mapping agains tho, Our method outperforms all bese | comparison identity and matched condition | p. 7 (V. EXPERIMENTS) |
| Metric and semantic mloU compared to the ground truth imap at time ¢ are plotted in Fig. | comparison identity and matched condition | p. 7 (B. Simulation Experiments) |
| Baseline Name / Use os VPP: Use cin Push Action Selection ‘Ours ar yes yes See IVC | comparison identity and matched condition | p. 14 (B. CNABU Implementation Details) |
| Consider now a greedy clairvoyant oracle policy, which, at every time step, has access to all possible observations that could be taken and selects ... | comparison identity and matched condition | p. 14 (B. CNABU Implementation Details) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Next, we present a series of ablations of our method and evaluate several interactive baselines. | component/input/data sensitivity | p. 6 (V. EXPERIMENTS) |
| We also compare an ablation of our pipeline that does not use manipulation, Ours ‘wo pushing. | component/input/data sensitivity | p. 7 (B. Simulation Experiments) |
| "Moreover, we observe that belief prediction is a powerful approach, leading to excellent scene coverage in low occlusion scenes even without pushing, In highly ... | component/input/data sensitivity | p. 7 (B. Simulation Experiments) |
| Consider the pure ‘Viewpoint Planning task, i, we must survey the environment without manipulating it, which is a submodular optimization. | component/input/data sensitivity | p. 14 (B. CNABU Implementation Details) |
| We compare our agent without pushing to this privileged information agent in the high-occlusion set of scenes and report the resulting ‘mean map occupancy ... | component/input/data sensitivity | p. 14 (B. CNABU Implementation Details) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Therefore, we propose Calibrated Neural-Accelerated Belief Updates (CNABUs) to learn a belief propagation model that generalizes to novel scenarios and provides confidence: calibrated predictions ... | The mfoU serves as a measure of the correctness of the predicitons, while the mECE measures the confidence calibration of these predictions, i.e., how ... | PDF body cue; verify exact table/figure and matched conditions | p. 14 (B. CNABU Implementation Details), p. 8 (B. Simulation Experiments), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 8 (B. Simulation Experiments), p. 7 (V. EXPERIMENTS) |
| Primary metric/result | Our method uses pushing to achieve significantly higher mloUs. | numeric claim only at cited anchor | p. 8 (B. Simulation Experiments) |

- Numeric sentences retained from the body:
- **p. 8 / B. Simulation Experiments - extractive body cue:** Standard deviation of performance of random haslies is epreseated 3s shading
- **p. 14 / B. CNABU Implementation Details - extractive body cue:** Random Pash Every 5!" vs ys yes yes Random every 5 steps
- **p. 14 / B. CNABU Implementation Details - extractive body cue:** Random Push Every 5", No Push CNABU / yes yes 0 yes Random every 5 Steps
- **p. 14 / B. CNABU Implementation Details - extractive body cue:** Random View Random Push Every 5!" yes 20 yes Random every 5 steps
- **p. 14 / B. CNABU Implementation Details - extractive body cue:** Random Pash Every 5!" vs ys yes yes Random every 5 steps
- **p. 14 / B. CNABU Implementation Details - extractive body cue:** Random Push Every 5", No Push CNABU / yes yes 0 yes Random every 5 Steps

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Limitations of our method include the need for represen: tative simulation training data or ground truth segmented maps, It also relies on high-quality semantic ... | p. 9 (VI. LIMITATIONS) |
| body limitation/failure cue | We generate 100 low occlusion scenarios via rejection sampling, using our sampling method described in Appendix A, but keeping only scenarios for which at ... | p. 7 (B. Simulation Experiments) |
| body limitation/failure cue | In this case, both "shelf" and "black" were used as syn- ‘onymous of the background class, capturing different failure cases of SAM2 segmentation. | p. 15 (B. CNABU Implementation Details) |
| body limitation/failure cue | ‘TABLE IE: Summary of features ofall considered base | p. 14 (B. CNABU Implementation Details) |
| body limitation/failure cue | [11's pipeline does not update its belief after a push, it requires multiple subsequent observations to reconcile inconsistencies between the actual scene and the ... | p. 7 (B. Simulation Experiments) |
| body limitation/failure cue | For added robustness in real-world scenarios, we augment the simulation <data with sat-and-pepper noise, random rotations and translations and add Gaussian noise to the ... | p. 14 (B. CNABU Implementation Details) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| ‘The networks are trained using backpropagation in PyTorch [32], with grid search-optimized learning rates and ADAM ‘optimizer, as well as early stopping based on ... | p. 14 (B. CNABU Implementation Details) |
| and fine-tuned the network weights provided by the authors for only 5,000 action steps. | p. 7 (B. Simulation Experiments) |
| Standard devistion of performance of random tasclines over random seeds is represented ss shading eund each plot, | p. 7 (V. EXPERIMENTS) |
| ‘consistently across all he steps, avoiding uninformative or overly aggressive manipulation | p. 8 (B. Simulation Experiments) |
| Additionally, the trajectory start and end points are encoded in 2D binary masks (Start Point and End Point maps in Fig. | p. 13 (B. CNABU Implementation Details) |
| Each CNABU implements a preprocessing step to encode actions and observations in a representation aligned to the ‘map grid. | p. 13 (B. CNABU Implementation Details) |
| Random Pash Every 5!" vs ys yes yes Random every 5 steps | p. 14 (B. CNABU Implementation Details) |
| For the evaluation, most approaches compute an estimated information gain 10 determine the utility of a view. | p. 2 (A. Next Best Viewpoint Planning) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / VI. LIMITATIONS - extractive body cue:** Limitations of our method include the need for represen: tative simulation training data or ground truth segmented maps, It also relies on high-quality semantic segmentation, ...
- **p. 7 / B. Simulation Experiments - extractive body cue:** We generate 100 low occlusion scenarios via rejection sampling, using our sampling method described in Appendix A, but keeping only scenarios for which at least ...
- **p. 15 / B. CNABU Implementation Details - extractive body cue:** In this case, both "shelf" and "black" were used as syn- ‘onymous of the background class, capturing different failure cases of SAM2 segmentation.
- **p. 14 / B. CNABU Implementation Details - extractive body cue:** ‘TABLE IE: Summary of features ofall considered base
- **p. 7 / B. Simulation Experiments - extractive body cue:** [11's pipeline does not update its belief after a push, it requires multiple subsequent observations to reconcile inconsistencies between the actual scene and the previously ...
- **p. 14 / B. CNABU Implementation Details - extractive body cue:** For added robustness in real-world scenarios, we augment the simulation <data with sat-and-pepper noise, random rotations and translations and add Gaussian noise to the depth ...

- **Evidence anchors reviewed:** datasets p. 14 (B. CNABU Implementation Details), p. 14 (B. CNABU Implementation Details), p. 7 (A. Experimental Setup), p. 7 (B. Simulation Experiments), p. 13 (B. CNABU Implementation Details), p. 15 (B. CNABU Implementation Details), metrics p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (B. Simulation Experiments), p. 14 (B. CNABU Implementation Details), p. 8 (B. Simulation Experiments), p. 14 (B. CNABU Implementation Details), baselines p. 6 (V. EXPERIMENTS), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (B. Simulation Experiments), p. 14 (B. CNABU Implementation Details), p. 14 (B. CNABU Implementation Details), results p. 14 (B. CNABU Implementation Details), p. 8 (B. Simulation Experiments), p. 6 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 8 (B. Simulation Experiments), p. 7 (V. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (15 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** We perform four core experiments to evaluate our approach, First, we test in simulation to highlight our pipeline's improvements in map completeness and accuracy compared to state-of-the-art [Il]. (p. 6, V. EXPERIMENTS).
- **Metric evidence:** Further evaluations, which validate the individual CNABU's performance and the use of VIG as a reward proxy, are provided in Appendices C and D. (p. 7, V. EXPERIMENTS).
- **Baseline/ablation evidence:** Next, we present a series of ablations of our method and evaluate several interactive baselines. (p. 6, V. EXPERIMENTS).
- **Failure/negative evidence:** Limitations of our method include the need for represen: tative simulation training data or ground truth segmented maps, It also relies on high-quality semantic segmentation, and although the computer vision ... (p. 9, VI. LIMITATIONS).
