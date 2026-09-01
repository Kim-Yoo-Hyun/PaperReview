# Evaluation - RoboPack: Learning Tactile-Informed Dynamics Models for Dense Packing

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p130.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p130.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 7 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS), p. 10 (V. EXPERIMENTS), p. 6 (IV. EXPERIMENTAL SETUP), p. 8 (V. EXPERIMENTS)): Does integrating tactile sensing information from prior interactions improve future prediction accuracy? ii.

## Evaluation Body Digest

- **p. 9 / V. EXPERIMENTS - extractive body cue:** Benchmarking Real-World Planning Performance Next, we evaluate the performance of our approach in solving real-world robotic planning tasks.
- **p. 6 / IV. EXPERIMENTAL SETUP - extractive body cue:** The robot needs to avoid inserting into infeasible regions to prevent hardware and object damage.
- **p. 6 / IV. EXPERIMENTAL SETUP - extractive body cue:** The robot has access to tactile feedback at all steps but only visual observations in between pushes, which corresponds to the real-world feedback loop frequency.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Does our tactile-informed model-predictive control framework enable robots to solve tasks involving objects of unknown physical properties?
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Each method either learns the full environment dynamics, or in the case of Physicsbased simulator, performs system identification from a static dataset.
- **p. 8 / V. EXPERIMENTS - extractive body cue:** As it gives more direct control of object properties, we use our dataset collected for the Non-Prehensile Box Pushing task for the analysis.
- **p. 8 / V. EXPERIMENTS - extractive body cue:** 2.65 ± 0.18 4.11 ± 0.17 4.57 ± 0.16 Dense RoboPack 0.070 ± 0.005 1.12 ± 0.036 2.01 ± 0.050 Packing RoboPack (no tactile) 0.088 ...
- **p. 10 / V. EXPERIMENTS - extractive body cue:** 9: Real-world planning performance on the box pushing task.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** contact-rich manipulation scene.
- **Input boundary:** tactile image/force, vision과 proprioceptive history.
- **Output/decision under evaluation:** grasp/contact action, force command 또는 object motion.
- **Primary target:** slip/contact success, force/pose error와 robustness.
- **Detected evaluation headings:** IV. EXPERIMENTAL SETUP (p. 6); V. EXPERIMENTS (p. 7).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Does integrating tactile sensing information from prior interactions improve future prediction accuracy? ii. | p. 7 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | A trial is labeled as a success if it achieves an error lower than 0.02 for point-wise MSE within 10 pushes. histories than a ... | p. 9 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | While the physics-based simulator achieves the strongest performance of the baselines, it is not able to achieve as precise control as our method, taking ... | p. 9 (V. EXPERIMENTS) |
| V. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Method Seen Objects Unseen Objects RoboPack 12/15 10/15 RoboPack (no tactile) 6/15 5/15 TABLE III: Success rates on the dense packing task. | p. 10 (V. EXPERIMENTS) |
| IV. EXPERIMENTAL SETUP | EMPIRICAL / REAL-ROBOT OR HARDWARE | To achieve effective planning, the robot needs to identify the box's properties from the tactile interaction history and adjust its predictions of the rod ... | p. 6 (IV. EXPERIMENTAL SETUP) |

## Dataset / Benchmark Role

- **p. 9 / V. EXPERIMENTS - extractive body cue:** Benchmarking Real-World Planning Performance Next, we evaluate the performance of our approach in solving real-world robotic planning tasks.
- **p. 6 / IV. EXPERIMENTAL SETUP - extractive body cue:** The robot needs to avoid inserting into infeasible regions to prevent hardware and object damage.
- **p. 6 / IV. EXPERIMENTAL SETUP - extractive body cue:** The robot has access to tactile feedback at all steps but only visual observations in between pushes, which corresponds to the real-world feedback loop frequency.
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Does our tactile-informed model-predictive control framework enable robots to solve tasks involving objects of unknown physical properties?
- **p. 7 / V. EXPERIMENTS - extractive body cue:** Each method either learns the full environment dynamics, or in the case of Physicsbased simulator, performs system identification from a static dataset.
- **p. 8 / V. EXPERIMENTS - extractive body cue:** As it gives more direct control of object properties, we use our dataset collected for the Non-Prehensile Box Pushing task for the analysis.
- **p. 8 / V. EXPERIMENTS - extractive body cue:** 2.65 ± 0.18 4.11 ± 0.17 4.57 ± 0.16 Dense RoboPack 0.070 ± 0.005 1.12 ± 0.036 2.01 ± 0.050 Packing RoboPack (no tactile) 0.088 ...
- **p. 10 / V. EXPERIMENTS - extractive body cue:** 9: Real-world planning performance on the box pushing task.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Tactile sensing for dense packing. Tactile feedback is critical in tasks with heavy occlusion and rich contact, such as dense packing. (a) Humans ...
- **p. 3 / Figure/Table caption - extractive body cue:** Fig. 2: RoboPack's perception module. (a) We construct a trajectory comprising particle representations of the scene, maintaining correspondence via 3D point tracking on the point ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: RoboPack's dynamics module. We perform state estimation and dynamics reasoning with a state estimator and a dynamics predictor respectively. (a) The state estimator ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Hardware overview. Our experimental platform con- sists of a Franka Panda arm, two Soft-Bubble sensors, four RealSense D415 RGB-D cameras, and a diverse ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5: Object sets for the packing task. The test objects are more complex than the training set visually, geometrically, and physically, to showcase the ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 6: Qualitative results on dynamics prediction. Pre- dictions made by our model compared to baseline methods in the Non-prehensile Box Pushing task. Red dots ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 7: Analysis of learned physics parameters. We assess our state estimator across 145-step trajectories and record the estimated physics parameters at each step. PCA ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 8: Non-prehensile box pushing and dense packing. In the Non-prehensile Box Pushing task, we demonstrate that our robot can push a box with unknown ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Benchmarking Real-World Planning Performance Next, we evaluate the performance of our approach in solving real-world robotic planning tasks. | embodiment, simulator version and control stack | p. 9 (V. EXPERIMENTS), p. 6 (IV. EXPERIMENTAL SETUP) |
| Task/environment | The robot needs to avoid inserting into infeasible regions to prevent hardware and object damage. | reset, timeout, object/scene variation | p. 6 (IV. EXPERIMENTAL SETUP), p. 6 (IV. EXPERIMENTAL SETUP) |
| Observation/sensor | tactile image/force, vision과 proprioceptive history | calibration, preprocessing, privileged input | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| Output/decision | grasp/contact action, force command 또는 object motion | action frame, controller and termination | p. 4 (III. METHOD), p. 5 (III. METHOD) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We report the minimum error to goal across 10 plan executions per trial, trial success rates, and number of execution steps to solve the ... | definition/direction/unit from same section | p. 9 (V. EXPERIMENTS) |
| Method Seen Objects Unseen Objects RoboPack 12/15 10/15 RoboPack (no tactile) 6/15 5/15 TABLE III: Success rates on the dense packing task. | definition/direction/unit from same section | p. 10 (V. EXPERIMENTS) |
| The classifier's improving accuracy across timesteps underscores the state estimator's proficiency in extracting and integrating box-specific information from the tactile observation history. | definition/direction/unit from same section | p. 9 (V. EXPERIMENTS) |
| We use a cost function that (i) penalizes the objects in the box from being pushed out of the boundary, (ii) encourages the robot ... | definition/direction/unit from same section | p. 7 (IV. EXPERIMENTAL SETUP) |
| Errors represent a 95% confidence interval. | definition/direction/unit from same section | p. 8 (V. EXPERIMENTS) |
| However, for the MSE loss, which measures prediction error for every point, RoboPack is significantly better than the baseline, indicating its ability to capture ... | definition/direction/unit from same section | p. 8 (V. EXPERIMENTS) |
| Our method has stable performance even for hard ones: its 75-percentile error is lower than the mean error of all other methods. | definition/direction/unit from same section | p. 10 (V. EXPERIMENTS) |
| Does integrating tactile sensing information from prior interactions improve future prediction accuracy? ii. | definition/direction/unit from same section | p. 7 (V. EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Fig. 6: Qualitative results on dynamics prediction. Pre- dictions made by our model compared to baseline methods in the Non-prehensile Box Pushing task. Red ... | comparison identity and matched condition | p. 8 (Figure/Table caption) |
| For the Dense Packing task, our model outperforms the best baseline on the pushing task, RoboPack (no tactile). | comparison identity and matched condition | p. 8 (V. EXPERIMENTS) |
| We first introduce our baselines and then present empirical results in the subsequent subsections. | comparison identity and matched condition | p. 7 (V. EXPERIMENTS) |
| All compared methods use the dynamics models to perform model-predictive control via sampling-based planning. | comparison identity and matched condition | p. 7 (V. EXPERIMENTS) |
| For the Dense Packing task, we would ideally compare our method against the baseline with the best results on nonprehensile box pushing: the physics-based ... | comparison identity and matched condition | p. 9 (V. EXPERIMENTS) |
| While the physics-based simulator achieves the strongest performance of the baselines, it is not able to achieve as precise control as our method, taking ... | comparison identity and matched condition | p. 9 (V. EXPERIMENTS) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| RoboPack (no tactile): To study the effects of using tactile sensing in state estimation and dynamics prediction, we evaluate this ablation of our method, ... | component/input/data sensitivity | p. 7 (V. EXPERIMENTS) |
| In contrast, when using tactile and visual observations directly as the state representation (RoboCook + tactile), the performance is even worse than RoboPack without ... | component/input/data sensitivity | p. 8 (V. EXPERIMENTS) |
| However, this is impractical for this task, because it is infeasible to obtain corresponding object models for the diverse and complex objects in this ... | component/input/data sensitivity | p. 9 (V. EXPERIMENTS) |
| This can be viewed as an adaptation of previous work [29, 48, 50, 49] to include an additional tactile observation component. | component/input/data sensitivity | p. 7 (V. EXPERIMENTS) |
| To qualitatively inspect the learned representations, we perform principal component analysis, reducing the learned latent vectors from R16 to R2. | component/input/data sensitivity | p. 8 (V. EXPERIMENTS) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To tackle these challenges, in this work, we propose to 1) learn dynamics directly from real physical interaction data using powerful deep function approximators, ... | Does integrating tactile sensing information from prior interactions improve future prediction accuracy? ii. | PDF body cue; verify exact table/figure and matched conditions | p. 7 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS), p. 10 (V. EXPERIMENTS), p. 6 (IV. EXPERIMENTAL SETUP), p. 8 (V. EXPERIMENTS) |
| Primary metric/result | A trial is labeled as a success if it achieves an error lower than 0.02 for point-wise MSE within 10 pushes. histories than a ... | numeric claim only at cited anchor | p. 9 (V. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 8 / V. EXPERIMENTS - extractive body cue:** Task Method MSE *1e-3 ↓ EMD *1e-2 ↓ CD *1e-2 ↓ RoboPack 1.48 ± 0.14 2.97 ± 0.14 3.46 ± 0.13 Box RoboPack (no tactile) ...
- **p. 8 / V. EXPERIMENTS - extractive body cue:** 2.65 ± 0.18 4.11 ± 0.17 4.57 ± 0.16 Dense RoboPack 0.070 ± 0.005 1.12 ± 0.036 2.01 ± 0.050 Packing RoboPack (no tactile) 0.088 ...
- **p. 8 / V. EXPERIMENTS - extractive body cue:** In particular, the state estimator can extract considerable information in the first 20 steps, which is approximately the average number of steps it takes to ...
- **p. 8 / V. EXPERIMENTS - extractive body cue:** Furthermore, note that the state estimator only observes a history of no more than 25 steps during training, but it can generalize to sequences four ...
- **p. 5 / III. METHOD - extractive body cue:** The loss is computed only on visual observations: L = 1 H H-1 X t=0 //ˆovis t -ovis t //2 2.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The test objects are more complex than the training set visually, geometrically, and physically, to showcase the generalizability of our model. yet the same ... | p. 6 (IV. EXPERIMENTAL SETUP) |
| body limitation/failure cue | Each episode includes various attempts at packing an object into the box and includes pushing and deforming objects, as well as in-hand slipping of ... | p. 7 (IV. EXPERIMENTAL SETUP) |
| body limitation/failure cue | Metrics such as EMD and CD that emphasize global shape and distribution but are insensitive to subtle positional changes cannot differentiate the two methods ... | p. 8 (V. EXPERIMENTS) |
| body limitation/failure cue | Due to heavy occlusions during task execution, the robot does not have access to meaningful visual feedback during robot execution other than the initial ... | p. 6 (IV. EXPERIMENTAL SETUP) |
| body limitation/failure cue | Mathematically, the loss function is J (ˆot, og, at) = X x∈ˆot min y∈og //x -y//2 - X y∈og min x∈ˆot //x -y//2 + ... | p. 7 (IV. EXPERIMENTAL SETUP) |
| body limitation/failure cue | Fig. 1: Tactile sensing for dense packing. Tactile feedback is critical in tasks with heavy occlusion and rich contact, such as dense packing. (a) ... | p. 1 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| We report the minimum error to goal across 10 plan executions per trial, trial success rates, and number of execution steps to solve the ... | p. 9 (V. EXPERIMENTS) |
| Our hardware setup is depicted in Figure 4. | p. 6 (IV. EXPERIMENTAL SETUP) |
| The robot needs to avoid inserting into infeasible regions to prevent hardware and object damage. | p. 6 (IV. EXPERIMENTAL SETUP) |
| Each episode includes various attempts at packing an object into the box and includes pushing and deforming objects, as well as in-hand slipping of ... | p. 7 (IV. EXPERIMENTAL SETUP) |
| We first identify the outer objects in the box and compute feasible starting positions of actions nudging each object, determined by the geometric center ... | p. 7 (IV. EXPERIMENTAL SETUP) |
| Furthermore, note that the state estimator only observes a history of no more than 25 steps during training, but it can generalize to sequences ... | p. 8 (V. EXPERIMENTS) |
| In particular, the state estimator can extract considerable information in the first 20 steps, which is approximately the average number of steps it takes ... | p. 8 (V. EXPERIMENTS) |
| PCA visualizations at four distinct timesteps show that the physics parameters gradually form clusters by box type. | p. 9 (V. EXPERIMENTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / IV. EXPERIMENTAL SETUP - extractive body cue:** The test objects are more complex than the training set visually, geometrically, and physically, to showcase the generalizability of our model. yet the same visual ...
- **p. 7 / IV. EXPERIMENTAL SETUP - extractive body cue:** Each episode includes various attempts at packing an object into the box and includes pushing and deforming objects, as well as in-hand slipping of the ...
- **p. 8 / V. EXPERIMENTS - extractive body cue:** Metrics such as EMD and CD that emphasize global shape and distribution but are insensitive to subtle positional changes cannot differentiate the two methods in ...
- **p. 6 / IV. EXPERIMENTAL SETUP - extractive body cue:** Due to heavy occlusions during task execution, the robot does not have access to meaningful visual feedback during robot execution other than the initial frame, ...
- **p. 7 / IV. EXPERIMENTAL SETUP - extractive body cue:** Mathematically, the loss function is J (ˆot, og, at) = X x∈ˆot min y∈og //x -y//2 - X y∈og min x∈ˆot //x -y//2 + r ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Tactile sensing for dense packing. Tactile feedback is critical in tasks with heavy occlusion and rich contact, such as dense packing. (a) Humans ...

- **PDF anchors reviewed:** datasets p. 9 (V. EXPERIMENTS), p. 6 (IV. EXPERIMENTAL SETUP), p. 6 (IV. EXPERIMENTAL SETUP), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), metrics p. 9 (V. EXPERIMENTS), p. 10 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS), p. 7 (IV. EXPERIMENTAL SETUP), p. 8 (V. EXPERIMENTS), p. 8 (V. EXPERIMENTS), baselines p. 8 (Figure/Table caption), p. 8 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 7 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS), results p. 7 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS), p. 9 (V. EXPERIMENTS), p. 10 (V. EXPERIMENTS), p. 6 (IV. EXPERIMENTAL SETUP), p. 8 (V. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
