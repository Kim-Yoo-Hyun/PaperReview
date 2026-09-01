# Evaluation - Learned Perceptive Forward Dynamics Model for Safe and Platform-aware Robotic Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p001.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p001.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (C. Platform-aware Predictions), p. 10 (C. Platform-aware Predictions), p. 6 (B. Model Architecture), p. 8 (C. Platform-aware Predictions), p. 8 (B. Baseline Comparison), p. 9 (C. Platform-aware Predictions)): Il, our approach achieves the highest success rate across both environments.

## Evaluation Body Digest

- **p. 10 / C. Platform-aware Predictions - extractive body cue:** Second, the failure states observed in simulation environments do not perfectly translate to real-world failures, and real-world data lacks demonstrations. of collisions due to the ...
- **p. 10 / C. Platform-aware Predictions - extractive body cue:** Trained with a mix of simulated and real-world data, the 'DM captures the complex dynamics of a quadrupedal robot and enables zero-shot adjustments of the ...
- **p. 8 / B. Baseline Comparison - extractive body cue:** In the planar environment, robot failures are rare (0.042%), likely caused by simulation instabilities that the model cannot predict, leading to low recall and precision ...
- **p. 6 / B. Model Architecture - extractive body cue:** Large-scale simulations are performed on the legged robot ANYmal [41], Barry [42], and the wheeled-legged robot ANYmal-On-Wheels (AoW) [43].
- **p. 6 / B. Model Architecture - extractive body cue:** Experimental Setup: ‘The effectiveness and perceptive capabilities of the developed FDM are evaluated in both simulated and real-world environments.
- **p. 7 / B. Model Architecture - extractive body cue:** Across 15 rounds, each collecting 80k samples from 10k parallel environments, updates consist of 8 episodes with a batch sizeof 2048, optimized using the AdamW ...
- **p. 8 / C. Platform-aware Predictions - extractive body cue:** 8, new datasets in similar environments have been used.
- **p. 9 / C. Platform-aware Predictions - extractive body cue:** Despite real-world, challenges such as sensor noise, terrain inconsistencies, and imperfect state estimation, our FDM successfully interprets the environment's traversability.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** legged robot, terrain과 contact dynamics.
- **Input boundary:** proprioception, terrain/perception observation과 velocity command.
- **Output/decision under evaluation:** joint target, torque, footstep 또는 locomotion action.
- **Primary target:** velocity/progress, stability, energy와 terrain generalization.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| C. Platform-aware Predictions | EMPIRICAL / REAL-ROBOT OR HARDWARE | Il, our approach achieves the highest success rate across both environments. | p. 9 (C. Platform-aware Predictions) |
| C. Platform-aware Predictions | EMPIRICAL / REAL-ROBOT OR HARDWARE | Moreover, our FDM integrated into an MPPI planner with simplified rewards achieves on average 81% goal success rate in complex environments. | p. 10 (C. Platform-aware Predictions) |
| B. Model Architecture | EMPIRICAL / REAL-ROBOT OR HARDWARE | The simulation results are achieved by building upon the NVIDIA IsaacLab framework [44] with terain details and data augmentations provided in Appendix E. | p. 6 (B. Model Architecture) |
| C. Platform-aware Predictions | EMPIRICAL / REAL-ROBOT OR HARDWARE | The perceptive baseline is more conservative and achieves higher recall scores. | p. 8 (C. Platform-aware Predictions) |
| B. Baseline Comparison | EMPIRICAL / REAL-ROBOT OR HARDWARE | The baseline achieves a higher recall score, which we hypothesize is due to its limited perception. | p. 8 (B. Baseline Comparison) |

## Dataset / Benchmark Role

- **p. 10 / C. Platform-aware Predictions - extractive body cue:** Second, the failure states observed in simulation environments do not perfectly translate to real-world failures, and real-world data lacks demonstrations. of collisions due to the ...
- **p. 10 / C. Platform-aware Predictions - extractive body cue:** Trained with a mix of simulated and real-world data, the 'DM captures the complex dynamics of a quadrupedal robot and enables zero-shot adjustments of the ...
- **p. 8 / B. Baseline Comparison - extractive body cue:** In the planar environment, robot failures are rare (0.042%), likely caused by simulation instabilities that the model cannot predict, leading to low recall and precision ...
- **p. 6 / B. Model Architecture - extractive body cue:** Large-scale simulations are performed on the legged robot ANYmal [41], Barry [42], and the wheeled-legged robot ANYmal-On-Wheels (AoW) [43].
- **p. 6 / B. Model Architecture - extractive body cue:** Experimental Setup: ‘The effectiveness and perceptive capabilities of the developed FDM are evaluated in both simulated and real-world environments.
- **p. 7 / B. Model Architecture - extractive body cue:** Across 15 rounds, each collecting 80k samples from 10k parallel environments, updates consist of 8 episodes with a batch sizeof 2048, optimized using the AdamW ...
- **p. 8 / C. Platform-aware Predictions - extractive body cue:** 8, new datasets in similar environments have been used.
- **p. 9 / C. Platform-aware Predictions - extractive body cue:** Despite real-world, challenges such as sensor noise, terrain inconsistencies, and imperfect state estimation, our FDM successfully interprets the environment's traversability.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Demonstration of the proposed perceptive Forward Dynamics Model for robust navigation in complex environments. The model, trained with real-world and simulation data, predicts ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3: Overview of the MPPI-based planning approach. A population Of action trajectories is generated by perturbating an inital solution ‘with Gaussian noise, The presented ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Demonstration of environment- and platform-aware state predictions using the presented FDM. Collision-free predictions of our method are displayed in Min collision ones in ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 6: Comparison of the position error over the prediction steps between the presented method, the perceptive FDM by Kim etal. [5] and the constant ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 8: Comparison of the position error at two predict
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 9: Demonstration of the pose and failure rewards across various simulation scenarios. The proposed FDM accurately predicts failures due to collisions and ealy path ...
- **p. 15 / Figure/Table caption - extractive body cue:** Fig. 10: The simulation training environment consists of four distinct segments. The frst segment features a randomized mix of stairs. ramps, walls, and rough surfaces. ...
- **p. 16 / Figure/Table caption - extractive body cue:** Fig. 11: Combined visualization of the height scan and traversability estimates generated by the heurstics-based method of (26) for four

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Second, the failure states observed in simulation environments do not perfectly translate to real-world failures, and real-world data lacks demonstrations. of collisions due to ... | embodiment, simulator version and control stack | p. 10 (C. Platform-aware Predictions), p. 10 (C. Platform-aware Predictions) |
| Task/environment | Trained with a mix of simulated and real-world data, the 'DM captures the complex dynamics of a quadrupedal robot and enables zero-shot adjustments of ... | reset, timeout, object/scene variation | p. 10 (C. Platform-aware Predictions), p. 8 (B. Baseline Comparison) |
| Observation/sensor | proprioception, terrain/perception observation과 velocity command | calibration, preprocessing, privileged input | p. 3 (A. Dynamics Modeling), p. 2 (A. Dynamics Modeling) |
| Output/decision | joint target, torque, footstep 또는 locomotion action | action frame, controller and termination | p. 3 (A. Dynamics Modeling), p. 5 (B. Model Architecture) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Moreover, our FDM integrated into an MPPI planner with simplified rewards achieves on average 81% goal success rate in complex environments. | definition/direction/unit from same section | p. 10 (C. Platform-aware Predictions) |
| Our FDM demonstrates the highest accuracy with the lowest errors and smallest standard deviation, | definition/direction/unit from same section | p. 7 (A. FDM Percepriveness) |
| Regarding the collision estimation, the developed FDM demonstrates an accuracy of at least 89% over all ‘environments, Our method predicts collision in environments with ... | definition/direction/unit from same section | p. 8 (B. Baseline Comparison) |
| The presented method demonstrates the lowest final position error and highest failure prediction accuracy over all test environments. | definition/direction/unit from same section | p. 8 (C. Platform-aware Predictions) |
| Fig. 12: Comparison of the position error over the prediction steps between the presented method I, the perceptive FDM by Kim et a. [5] ... | definition/direction/unit from same section | p. 16 (Figure/Table caption) |
| Il, our approach achieves the highest success rate across both environments. | definition/direction/unit from same section | p. 9 (C. Platform-aware Predictions) |
| We assess the planner's effectiveness in both 2D and 3.D environments based on success rate, mean path length (MPL), and mean path time (MPT). | definition/direction/unit from same section | p. 9 (C. Platform-aware Predictions) |
| Trained with a mix of simulated and real-world data, the 'DM captures the complex dynamics of a quadrupedal robot and enables zero-shot adjustments of ... | definition/direction/unit from same section | p. 10 (C. Platform-aware Predictions) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Further, the better accuracy compared to the baselines becomes clearly | comparison identity and matched condition | p. 7 (B. Baseline Comparison) |
| 6, we demonstrate that the position error averaged overall environments remains the smallest for the developed FDM with a decrease of 41.28% compared to ... | comparison identity and matched condition | p. 7 (B. Baseline Comparison) |
| Moreover, demonstrates the most precise failure estimation, although it is less likely to detect all collisions compared to the more conservative baseline. | comparison identity and matched condition | p. 8 (B. Baseline Comparison) |
| Our approach <demonstrates superior performance compared to the baseline method of Kim et al. | comparison identity and matched condition | p. 9 (C. Platform-aware Predictions) |
| Trained with a mix of simulated and real-world data, the 'DM captures the complex dynamics of a quadrupedal robot and enables zero-shot adjustments of ... | comparison identity and matched condition | p. 10 (C. Platform-aware Predictions) |
| The baseline achieves a higher recall score, which we hypothesize is due to its limited perception. | comparison identity and matched condition | p. 8 (B. Baseline Comparison) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Fig, 5: Comparison of the postion error atthe final prediction step in different environments for the presented FDM I, the perceptive FDM by Kim ... | component/input/data sensitivity | p. 7 (B. Model Architecture) |
| These obstacles cannot be differentiated from walls using only a horizontal 2D sensor without actively changing the observation angle. | component/input/data sensitivity | p. 6 (B. Model Architecture) |
| Using a zero-shot MPPI planner allows for adjustments of the planning behavior without retraining, Leveraging the pose and failure risk of the perceptive FDM, ... | component/input/data sensitivity | p. 6 (B. Model Architecture) |
| More details on the sensitivity of learning and planning parameters, alongside discussion of the adaptation required for a new robot platform, ‘can be found ... | component/input/data sensitivity | p. 7 (B. Model Architecture) |
| The more conservative baseline instead circled around the obstacles, leading to increased path time and length, often without reaching the goal | component/input/data sensitivity | p. 9 (C. Platform-aware Predictions) |
| The experiments show that even before the fine-tuning, our FDM performs better than the constant velocity model. | component/input/data sensitivity | p. 8 (C. Platform-aware Predictions) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| To overcome these issues, we propose a novel learned perceptive | Il, our approach achieves the highest success rate across both environments. | PDF body cue; verify exact table/figure and matched conditions | p. 9 (C. Platform-aware Predictions), p. 10 (C. Platform-aware Predictions), p. 6 (B. Model Architecture), p. 8 (C. Platform-aware Predictions), p. 8 (B. Baseline Comparison), p. 9 (C. Platform-aware Predictions) |
| Primary metric/result | Moreover, our FDM integrated into an MPPI planner with simplified rewards achieves on average 81% goal success rate in complex environments. | numeric claim only at cited anchor | p. 10 (C. Platform-aware Predictions) |

- Numeric sentences retained from the body:
- **p. 6 / B. Model Architecture - extractive body cue:** The FDM runs onboard using an NVIDIA Jetson Orin AGX, with the planner running at 7 Hz. using 2048 trajectories and a model inference time ...
- **p. 7 / B. Model Architecture - extractive body cue:** Across 15 rounds, each collecting 80k samples from 10k parallel environments, updates consist of 8 episodes with a batch sizeof 2048, optimized using the AdamW ...
- **p. 4 / B. Planning - extractive body cue:** ‘TABLE I: The observation space of the FDM combines proprioceptive information of the robot state m2" and the joint states m?""* with exteroceptive measurements h. ...
- **p. 6 / B. Model Architecture - extractive body cue:** The FDM runs onboard using an NVIDIA Jetson Orin AGX, with the planner running at 7 Hz. using 2048 trajectories and a model inference time ...
- **p. 7 / B. Model Architecture - extractive body cue:** Across 15 rounds, each collecting 80k samples from 10k parallel environments, updates consist of 8 episodes with a batch sizeof 2048, optimized using the AdamW ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Specifically, the FDM can estimate failure states (eg., collisions) and adjust future poses based on the velocity ‘command tracking performance in rough terrain, To ... | p. 7 (A. FDM Percepriveness) |
| body limitation/failure cue | Moreover, demonstrates the most precise failure estimation, although it is less likely to detect all collisions compared to the more conservative baseline. | p. 8 (B. Baseline Comparison) |
| body limitation/failure cue | In the planar environment, robot failures are rare (0.042%), likely caused by simulation instabilities that the model cannot predict, leading to low recall and ... | p. 8 (B. Baseline Comparison) |
| body limitation/failure cue | The proposed FDM accurately predicts failures due to collisions and ealy path terminations caused by unlzaversable stars and ramps. | p. 10 (C. Platform-aware Predictions) |
| body limitation/failure cue | As a resull, the simple combination of pose reward guiding the robot toward the goal and a failure reward preventing collisions proves sufficient for ... | p. 10 (C. Platform-aware Predictions) |
| body limitation/failure cue | Fig. 1: Demonstration of the proposed perceptive Forward Dynamics Model for robust navigation in complex environments. The model, trained with real-world and simulation data, ... | p. 1 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Across 15 rounds, each collecting 80k samples from 10k parallel environments, updates consist of 8 episodes with a batch sizeof 2048, optimized using the ... | p. 7 (B. Model Architecture) |
| The FDM runs onboard using an NVIDIA Jetson Orin AGX, with the planner running at 7 Hz. using 2048 trajectories and a model inference ... | p. 6 (B. Model Architecture) |
| In later stages, real-world data is integrated with synthetic data, and weights are refined using a small, constant learning rate to capture the full ... | p. 7 (B. Model Architecture) |
| Lately, world models have emerged, which encode system dynamics in a latent space, enabling policy optimization through imagined rollouts [19 20) Such models can ... | p. 2 (A. Dynamics Modeling) |
| Therefore, the action sequences must be forwardpropagated through the system's dynamics over a prediction horizon n to compute the future states. | p. 3 (B. Model Predictive Path Integral Control) |
| These weights are computed based on the reward 7, of each trajectory, ensuring higherreward trajectories contrite more significantly to the update: | p. 3 (B. Model Predictive Path Integral Control) |
| about the current and past state of the robotic system is encoded and given to a recurrent unit, which generates a latent of the ... | p. 4 (B. Planning) |
| The pose loss is computed using mean squared error (MSE) between predicted and true poses. | p. 5 (B. Model Architecture) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 7 / A. FDM Percepriveness - extractive body cue:** Specifically, the FDM can estimate failure states (eg., collisions) and adjust future poses based on the velocity ‘command tracking performance in rough terrain, To evaluate ...
- **p. 8 / B. Baseline Comparison - extractive body cue:** Moreover, demonstrates the most precise failure estimation, although it is less likely to detect all collisions compared to the more conservative baseline.
- **p. 8 / B. Baseline Comparison - extractive body cue:** In the planar environment, robot failures are rare (0.042%), likely caused by simulation instabilities that the model cannot predict, leading to low recall and precision ...
- **p. 10 / C. Platform-aware Predictions - extractive body cue:** The proposed FDM accurately predicts failures due to collisions and ealy path terminations caused by unlzaversable stars and ramps.
- **p. 10 / C. Platform-aware Predictions - extractive body cue:** As a resull, the simple combination of pose reward guiding the robot toward the goal and a failure reward preventing collisions proves sufficient for safe ...
- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Demonstration of the proposed perceptive Forward Dynamics Model for robust navigation in complex environments. The model, trained with real-world and simulation data, predicts ...

- **PDF anchors reviewed:** datasets p. 10 (C. Platform-aware Predictions), p. 10 (C. Platform-aware Predictions), p. 8 (B. Baseline Comparison), p. 6 (B. Model Architecture), p. 6 (B. Model Architecture), p. 7 (B. Model Architecture), metrics p. 10 (C. Platform-aware Predictions), p. 7 (A. FDM Percepriveness), p. 8 (B. Baseline Comparison), p. 8 (C. Platform-aware Predictions), p. 16 (Figure/Table caption), p. 9 (C. Platform-aware Predictions), baselines p. 7 (B. Baseline Comparison), p. 7 (B. Baseline Comparison), p. 8 (B. Baseline Comparison), p. 9 (C. Platform-aware Predictions), p. 10 (C. Platform-aware Predictions), p. 8 (B. Baseline Comparison), results p. 9 (C. Platform-aware Predictions), p. 10 (C. Platform-aware Predictions), p. 6 (B. Model Architecture), p. 8 (C. Platform-aware Predictions), p. 8 (B. Baseline Comparison), p. 9 (C. Platform-aware Predictions).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
