# Evaluation - DexTrack: Towards Generalizable Neural Tracking Control for Dexterous Manipulation from Human References

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (25 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openreview.net/forum?id=ajSmXqgS24; PDF retrieval source: https://arxiv.org/pdf/2502.09614. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 17 (B.1 DEXTEROUS MANIPULATION TRACKING CONTROL), p. 17 (B.1 DEXTEROUS MANIPULATION TRACKING CONTROL), p. 18 (B.2 REAL-WORLD EVALUATIONS), p. 9 (4 EXPERIMENTS)): As shown in Table 1, we achieve significantly higher success rates, calculated under two different thresholds, compared to the best-performing baseline across both datasets.

## Evaluation Body Digest

- **p. 7 / 4 EXPERIMENTS - extractive body cue:** Tested on two HOI datasets featuring complex daily manipulation tasks, our method is assessed through both simulation and real-world evaluations (see Sec.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** For the TACO dataset, we follow the generalization evaluating setting suggested by the authors (Liu et al., 2024b) and split the dataset into a training ...
- **p. 21 / C ADDITIONAL EXPERIMENTAL DETAILS - extractive body cue:** Specifically, the whole dataset is split into 1) a training dataset, containing 1565 trajectories, 2) test set S0 where both the tool object geometries and ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** As demonstrated in Figures 4f and 4g, we enable the robot to track complex object movements and successfully lift a hard-to-grasp round apple in real-world ...
- **p. 21 / C ADDITIONAL EXPERIMENTAL DETAILS - extractive body cue:** Our dexterous robot hand-object manipulation dataset is created by retargeting two public human-object datasets, namely GRAB Taheri et al.
- **p. 24 / C ADDITIONAL EXPERIMENTAL DETAILS - extractive body cue:** To evaluate this, we construct a disturbed test set by adding random noise to the hand trajectory and the object position trajectory to test the ...
- **p. 18 / B.2 REAL-WORLD EVALUATIONS - extractive body cue:** As observed in the table, the tracking results achieved by our method can be well transferred to the real-world robot, helping us achieve obviously better ...
- **p. 19 / B.2 REAL-WORLD EVALUATIONS - extractive body cue:** Published as a conference paper at ICLR 2025 Table 8: Real-world quantitative comparisons (TACO dataset).

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** 4 EXPERIMENTS (p. 7); B ADDITIONAL EXPERIMENTS (p. 16); B.2 REAL-WORLD EVALUATIONS (p. 18); C ADDITIONAL EXPERIMENTAL DETAILS (p. 21).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | As shown in Table 1, we achieve significantly higher success rates, calculated under two different thresholds, compared to the best-performing baseline across both datasets. | p. 8 (4 EXPERIMENTS) |
| 4 EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | On average, our method improves the tracking success rate by over 10% compared to the best prior methods. | p. 7 (4 EXPERIMENTS) |
| B.1 DEXTEROUS MANIPULATION TRACKING CONTROL | EMPIRICAL / REAL-ROBOT OR HARDWARE | The final model trained in this way achieves 42.13% and 60.41% success rates under two thresholds. | p. 17 (B.1 DEXTEROUS MANIPULATION TRACKING CONTROL) |
| B.1 DEXTEROUS MANIPULATION TRACKING CONTROL | EMPIRICAL / REAL-ROBOT OR HARDWARE | Test set Rerr (rad, ↓) Terr (cm, ↓) Ewrist (↓) Efinger (rad, ↓) Success Rate (%, ↑) S1 0.5787 2.43 0.1481 0.4703 35.97/67.63 S2 ... | p. 17 (B.1 DEXTEROUS MANIPULATION TRACKING CONTROL) |
| B.2 REAL-WORLD EVALUATIONS | EMPIRICAL / REAL-ROBOT OR HARDWARE | For direct tracking results transferring setting, we present the quantitative success rates evaluated on our method and the best-performed baseline in Table 7 (for ... | p. 18 (B.2 REAL-WORLD EVALUATIONS) |

## Dataset / Benchmark Role

- **p. 7 / 4 EXPERIMENTS - extractive body cue:** Tested on two HOI datasets featuring complex daily manipulation tasks, our method is assessed through both simulation and real-world evaluations (see Sec.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** For the TACO dataset, we follow the generalization evaluating setting suggested by the authors (Liu et al., 2024b) and split the dataset into a training ...
- **p. 21 / C ADDITIONAL EXPERIMENTAL DETAILS - extractive body cue:** Specifically, the whole dataset is split into 1) a training dataset, containing 1565 trajectories, 2) test set S0 where both the tool object geometries and ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** As demonstrated in Figures 4f and 4g, we enable the robot to track complex object movements and successfully lift a hard-to-grasp round apple in real-world ...
- **p. 21 / C ADDITIONAL EXPERIMENTAL DETAILS - extractive body cue:** Our dexterous robot hand-object manipulation dataset is created by retargeting two public human-object datasets, namely GRAB Taheri et al.
- **p. 24 / C ADDITIONAL EXPERIMENTAL DETAILS - extractive body cue:** To evaluate this, we construct a disturbed test set by adding random noise to the hand trajectory and the object position trajectory to test the ...
- **p. 18 / B.2 REAL-WORLD EVALUATIONS - extractive body cue:** As observed in the table, the tracking results achieved by our method can be well transferred to the real-world robot, helping us achieve obviously better ...
- **p. 19 / B.2 REAL-WORLD EVALUATIONS - extractive body cue:** Published as a conference paper at ICLR 2025 Table 8: Real-world quantitative comparisons (TACO dataset).

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: DexTrack learns a generalizable neural tracking controller for dexterous manipulation from human references. It generates hand action commands from kinematic references, ensuring close ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 2: DexTrack learns a generalizable neural tracking controller for dexterous manipulation from human references. It alternates between training the tracking controller using abundant and ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 1: Quantitative evaluations. Bold red and italic blue values for best and the second best-performed ones respectively. "Ours (w/o) data" and "Ours (w/o data, ...
- **p. 8 / Figure/Table caption - extractive body cue:** Figure 3: Robustness w.r.t. unreasonable states. Please check our website and video for animated results. We demonstrate the generalization ability and robustness of our tracking ...
- **p. 9 / Figure/Table caption - extractive body cue:** Table 2: Real-world quantitative comparisons. Bold red numbers for best values.
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 5: Scaling the amount of demonstrations. Scaling the number of demonstrations. To in- vestigate the relationship between the tracking con- troller's performance and the ...
- **p. 10 / Figure/Table caption - extractive body cue:** Figure 4: Qualitative comparisons. Please check our website and the accompanying video for animated
- **p. 15 / Figure/Table caption - extractive body cue:** Figure 6: DexTrack learns a generalizable neural tracking controller for dexterous manipulation from human references. It alternates between training the tracking controller using abundant and ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Tested on two HOI datasets featuring complex daily manipulation tasks, our method is assessed through both simulation and real-world evaluations (see Sec. | embodiment, simulator version and control stack | p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS) |
| Task/environment | For the TACO dataset, we follow the generalization evaluating setting suggested by the authors (Liu et al., 2024b) and split the dataset into a ... | reset, timeout, object/scene variation | p. 7 (4 EXPERIMENTS), p. 21 (C ADDITIONAL EXPERIMENTAL DETAILS) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 2 (1 INTRODUCTION), p. 3 (3 METHOD) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 3 (3 METHOD), p. 2 (1 INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Test set Rerr (rad, ↓) Terr (cm, ↓) Ewrist (↓) Efinger (rad, ↓) Success Rate (%, ↑) S1 0.5787 2.43 0.1481 0.4703 35.97/67.63 S2 ... | definition/direction/unit from same section | p. 17 (B.1 DEXTEROUS MANIPULATION TRACKING CONTROL) |
| We introduce five metrics to evaluate the tracking accuracy and task success: 1) Per-frame average object rotation error: Rerr = 1 N+1 PN n=0 ... | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| (26) As the quality of the trajectory distribution gets worse and the tracking error decreases, the "robustness score" would increase. | definition/direction/unit from same section | p. 24 (C ADDITIONAL EXPERIMENTAL DETAILS) |
| On average, our method improves the tracking success rate by over 10% compared to the best prior methods. | definition/direction/unit from same section | p. 7 (4 EXPERIMENTS) |
| 5) Success rate: A tracking attempt is successful if Terr, Rerr, and 0.5Ewrist + 0.5Efinger are all below the thresholds. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| As shown in Table 1, we achieve significantly higher success rates, calculated under two different thresholds, compared to the best-performing baseline across both datasets. | definition/direction/unit from same section | p. 8 (4 EXPERIMENTS) |
| Success rates are measured under three thresholds and compared with the best baseline. | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |
| 0.0 0.2 0.4 0.6 0.8 1.0 Proportion of Total Demonstrations Used 60 65 70 75 Success Rate (%) 57.64 59.61 62.07 67.0 72.91 74.38 ... | definition/direction/unit from same section | p. 9 (4 EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| As shown in Table 1, we achieve significantly higher success rates, calculated under two different thresholds, compared to the best-performing baseline across both datasets. | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |
| Success rates are measured under three thresholds and compared with the best baseline. | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| These results demonstrate the robustness and generalization of our controller, outperforming the PPO baseline, which struggles with basic lifting. | comparison identity and matched condition | p. 9 (4 EXPERIMENTS) |
| We compare our approach to strong baselines, showing its superiority. | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| On average, our method improves the tracking success rate by over 10% compared to the best prior methods. | comparison identity and matched condition | p. 7 (4 EXPERIMENTS) |
| We show the real-world effectiveness of our method and the superiority over best-performing baselines (Figure 4,Table 2). | comparison identity and matched condition | p. 8 (4 EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| We ablate these strategies by creating two variants: "Ours (w/o data, w/o homotopy)", where the dataset is built by optimizing each trajectory without prior ... | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| 5 ABLATION STUDIES Diversity and quality of robot tracking demonstrations. | component/input/data sensitivity | p. 9 (4 EXPERIMENTS) |
| In Table 6, we present the full evaluation results on all five types of metrics of each model traiend in the ablation study regarding ... | component/input/data sensitivity | p. 17 (B.1 DEXTEROUS MANIPULATION TRACKING CONTROL) |
| All the models are trained in a single card without multi-gpu parallelization. | component/input/data sensitivity | p. 22 (C ADDITIONAL EXPERIMENTAL DETAILS) |
| Directly training PPO without any supervision is the most efficient approach while the performance lagged behind due to no proper guidance. | component/input/data sensitivity | p. 22 (C ADDITIONAL EXPERIMENTAL DETAILS) |
| Table 3: Weights of different reward components. wo,p wo,q wwrist · wtrans wwrist · wornt wfinger Weight 1.0 | component/input/data sensitivity | p. 15 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our contributions are threefold: • We present a generalizable neural tracking controller that progressively improves its performance through iterative mining and incorporating high-quality tracking ... | As shown in Table 1, we achieve significantly higher success rates, calculated under two different thresholds, compared to the best-performing baseline across both datasets. | PDF body cue; verify exact table/figure and matched conditions | p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 17 (B.1 DEXTEROUS MANIPULATION TRACKING CONTROL), p. 17 (B.1 DEXTEROUS MANIPULATION TRACKING CONTROL), p. 18 (B.2 REAL-WORLD EVALUATIONS), p. 9 (4 EXPERIMENTS) |
| Primary metric/result | On average, our method improves the tracking success rate by over 10% compared to the best prior methods. | numeric claim only at cited anchor | p. 7 (4 EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We fully retargeted the GRAB and TACO datasets, producing 1,269 and 2,316 robot hand manipulation sequences, respectively.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** For the TACO dataset, we follow the generalization evaluating setting suggested by the authors (Liu et al., 2024b) and split the dataset into a training ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** We introduce five metrics to evaluate the tracking accuracy and task success: 1) Per-frame average object rotation error: Rerr = 1 N+1 PN n=0 Diff ...
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** 2) Per-frame average object translation error: Terr = 1 N+1 PN n=0 ∥tnˆtn∥, where tn and ˆtn are the tracked and reference translations.
- **p. 7 / 4 EXPERIMENTS - extractive body cue:** 3) Per-frame average wrist position and rotation error: Ewrist = 1 N+1 PN n=0  0.5 Diff Angle(qwrist n , ˆqwrist n ) + 0.5∥twrist n ...
- **p. 8 / 4 EXPERIMENTS - extractive body cue:** Thus, we primarily compare our method with model-free approaches: 1) DGrasp (Christen et al., 2022): Adapted to track by dividing sequences into subsequences of 10 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Figure 10: Failure cases in real-world experiments. Please refer to our website for animated | p. 19 (Figure/Table caption) |
| body limitation/failure cue | Method soap shovel brush roller knife spoon PPO (w/o sup., tracking rew) 33.3/0/0 25.0/0.0/0.0 25.0/0/0 25.0/25.0/0.0 0/0/0 25.0/0/0 Ours 100.0/66.7/66.7 50.0/25.0/25.0 25.0/25.0/0.0 50.0/25.0/25.0 25.0/25.0/0.0 ... | p. 19 (B.2 REAL-WORLD EVALUATIONS) |
| body limitation/failure cue | A key limitation is the time-consuming process of acquiring high-quality demonstrations. | p. 9 (4 EXPERIMENTS) |
| body limitation/failure cue | 6 CONCLUSIONS AND LIMITATIONS We propose DexTrack to develop a generalizable tracking controller for dexterous manipulation. | p. 9 (4 EXPERIMENTS) |
| body limitation/failure cue | As shown in Figure 11b, the original per-trajectory tracker fails to find a proper way to grasp the small sphere and lift it up ... | p. 20 (B.3 ANALYSIS ON THE HOMOTOPY OPTIMIZATION SCHEME) |
| body limitation/failure cue | Figure 1: DexTrack learns a generalizable neural tracking controller for dexterous manipulation from human references. It generates hand action commands from kinematic references, ensuring ... | p. 1 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| In simulation, we use the Allegro hand, with URDF adapted from IsaacGymEnvs (Makoviychuk et al., 2021), and in real-world experiments, the LEAP hand (Shaw ... | p. 7 (4 EXPERIMENTS) |
| The third level of success is lifting the object up, followed by keeping tracking the object's trajectory for more than 100 timesteps. | p. 18 (B.2 REAL-WORLD EVALUATIONS) |
| For details, please refer to code in the supplementary material (refer "README.md" for instructions). | p. 21 (C ADDITIONAL EXPERIMENTAL DETAILS) |
| For instance, if the hand initially penetrates through the table, a large force would be applied to the hand at the beginning, which would ... | p. 21 (C ADDITIONAL EXPERIMENTAL DETAILS) |
| Both the simulation and the policy run at 60Hz. | p. 22 (C ADDITIONAL EXPERIMENTAL DETAILS) |
| Experiments are conducted on a Ubuntu 20.04 machine with eight A10 GPU cards. | p. 22 (C ADDITIONAL EXPERIMENTAL DETAILS) |
| Here we introduce three types of statistics: 1) object movement smoohtness so smooth: it quantifies the motion smoothness by calculating the per-frame average object ... | p. 25 (C ADDITIONAL EXPERIMENTAL DETAILS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 19 / Figure/Table caption - extractive body cue:** Figure 10: Failure cases in real-world experiments. Please refer to our website for animated
- **p. 19 / B.2 REAL-WORLD EVALUATIONS - extractive body cue:** Method soap shovel brush roller knife spoon PPO (w/o sup., tracking rew) 33.3/0/0 25.0/0.0/0.0 25.0/0/0 25.0/25.0/0.0 0/0/0 25.0/0/0 Ours 100.0/66.7/66.7 50.0/25.0/25.0 25.0/25.0/0.0 50.0/25.0/25.0 25.0/25.0/0.0 50.0/50.0/25.0 ...
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** A key limitation is the time-consuming process of acquiring high-quality demonstrations.
- **p. 9 / 4 EXPERIMENTS - extractive body cue:** 6 CONCLUSIONS AND LIMITATIONS We propose DexTrack to develop a generalizable tracking controller for dexterous manipulation.
- **p. 20 / B.3 ANALYSIS ON THE HOMOTOPY OPTIMIZATION SCHEME - extractive body cue:** As shown in Figure 11b, the original per-trajectory tracker fails to find a proper way to grasp the small sphere and lift it up from ...
- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: DexTrack learns a generalizable neural tracking controller for dexterous manipulation from human references. It generates hand action commands from kinematic references, ensuring close ...

- **PDF anchors reviewed:** datasets p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 21 (C ADDITIONAL EXPERIMENTAL DETAILS), p. 9 (4 EXPERIMENTS), p. 21 (C ADDITIONAL EXPERIMENTAL DETAILS), p. 24 (C ADDITIONAL EXPERIMENTAL DETAILS), metrics p. 17 (B.1 DEXTEROUS MANIPULATION TRACKING CONTROL), p. 7 (4 EXPERIMENTS), p. 24 (C ADDITIONAL EXPERIMENTAL DETAILS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), baselines p. 8 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 9 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 8 (4 EXPERIMENTS), results p. 8 (4 EXPERIMENTS), p. 7 (4 EXPERIMENTS), p. 17 (B.1 DEXTEROUS MANIPULATION TRACKING CONTROL), p. 17 (B.1 DEXTEROUS MANIPULATION TRACKING CONTROL), p. 18 (B.2 REAL-WORLD EVALUATIONS), p. 9 (4 EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
