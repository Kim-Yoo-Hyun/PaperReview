# Evaluation - Flying Hand: End-Effector-Centric Framework for Versatile Aerial Manipulation Teleoperation and Policy Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p130.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p130.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (B. Implementation Details), p. 10 (B. Implementation Details), p. 10 (B. Implementation Details), p. 2 (4) Rich real-world experiments demonstrated the versatility), p. 8 (B. Implementation Details), p. 8 (B. Implementation Details)): improvements can be achieved through more accurate system modeling and higher-precision hardware to enhance tracking accuracy.

## Evaluation Body Digest

- **p. 2 / 4) Rich real-world experiments demonstrated the versatility - extractive body cue:** Some work also showed amazing results, achieving high-speed grasping, or grasping moving objects [50], but sacrificed payload capacity or precision due to specialized hardware designs.
- **p. 2 / 4) Rich real-world experiments demonstrated the versatility - extractive body cue:** In general, although different works have shown success on different specific tasks, the specific system design and algorithm development make the same hardware and algorithm ...
- **p. 10 / B. Implementation Details - extractive body cue:** 2) Real-world Experiments: We adopt the aerial peg-inhole task to demonstrate our capability to derive an autonomous policy from human demonstrations for aerial manipulation in ...
- **p. 10 / B. Implementation Details - extractive body cue:** ‘To show the advantage of leaming from an ee-centric demonstration compared to a joint space demonstration, we use the same demonstration trajectory but change the ...
- **p. 9 / B. Implementation Details - extractive body cue:** Ina subsequent experiment, we evaluate the benefits of directly controlling the end-effector's pose using our framework against controlling each degree of freedom (DoF) for UAVs ...
- **p. 11 / B. Implementation Details - extractive body cue:** We tested ‘with random unseen horizontal hole positions and the learned policy successfully completed 4 out of 5 real-world peg-inhole tests, ie, 80% successful rate.
- **p. 7 / A. Experimental Setup - extractive body cue:** 1) Trajectory Tracking Task Setup: To show the effectiveness of our proposed method in end-effector trajectory tracking tasks, we perform a comparison between our control ...
- **p. 8 / A. Experimental Setup - extractive body cue:** + Aerial Writing: Drawing a target shape (the digit 2025") on a vertical wall, with an overall size of approxirately 3m%0.Sm, This task required precise ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** 4) Rich real-world experiments demonstrated the versatility (p. 2); A. Experimental Setup (p. 7); B. Implementation Details (p. 8).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| B. Implementation Details | EMPIRICAL / REAL-ROBOT OR HARDWARE | improvements can be achieved through more accurate system modeling and higher-precision hardware to enhance tracking accuracy. | p. 9 (B. Implementation Details) |
| B. Implementation Details | EMPIRICAL / REAL-ROBOT OR HARDWARE | + Multi-Skill Composition: In the open and retrieve task, our ee-centric policy achieves 2 higher success rate than the joint space policy, which demonstrates ... | p. 10 (B. Implementation Details) |
| B. Implementation Details | EMPIRICAL / REAL-ROBOT OR HARDWARE | + Geometric Precision Advantage: Our ee-centric policy achieves 2.5% higher success rate in geometrically sensitive peg in hole task, directly benefiting from task-space supervision ... | p. 10 (B. Implementation Details) |
| 4) Rich real-world experiments demonstrated the versatility | EMPIRICAL / REAL-ROBOT OR HARDWARE | Typical work includes [42] where they proposed a specific hole searching policy for bolt screwing tasks, and [52] where they achieved mm-level peg-in-hole task; ... | p. 2 (4) Rich real-world experiments demonstrated the versatility) |
| B. Implementation Details | EMPIRICAL / REAL-ROBOT OR HARDWARE | The results show that our proposed method achieves the lowest tracking error, with approximately / em in hover and 4 em during motion. | p. 8 (B. Implementation Details) |

## Dataset / Benchmark Role

- **p. 2 / 4) Rich real-world experiments demonstrated the versatility - extractive body cue:** Some work also showed amazing results, achieving high-speed grasping, or grasping moving objects [50], but sacrificed payload capacity or precision due to specialized hardware designs.
- **p. 2 / 4) Rich real-world experiments demonstrated the versatility - extractive body cue:** In general, although different works have shown success on different specific tasks, the specific system design and algorithm development make the same hardware and algorithm ...
- **p. 10 / B. Implementation Details - extractive body cue:** 2) Real-world Experiments: We adopt the aerial peg-inhole task to demonstrate our capability to derive an autonomous policy from human demonstrations for aerial manipulation in ...
- **p. 10 / B. Implementation Details - extractive body cue:** ‘To show the advantage of leaming from an ee-centric demonstration compared to a joint space demonstration, we use the same demonstration trajectory but change the ...
- **p. 9 / B. Implementation Details - extractive body cue:** Ina subsequent experiment, we evaluate the benefits of directly controlling the end-effector's pose using our framework against controlling each degree of freedom (DoF) for UAVs ...
- **p. 11 / B. Implementation Details - extractive body cue:** We tested ‘with random unseen horizontal hole positions and the learned policy successfully completed 4 out of 5 real-world peg-inhole tests, ie, 80% successful rate.
- **p. 7 / A. Experimental Setup - extractive body cue:** 1) Trajectory Tracking Task Setup: To show the effectiveness of our proposed method in end-effector trajectory tracking tasks, we perform a comparison between our control ...
- **p. 8 / A. Experimental Setup - extractive body cue:** + Aerial Writing: Drawing a target shape (the digit 2025") on a vertical wall, with an overall size of approxirately 3m%0.Sm, This task required precise ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 3. UAM hardware system design, ilustaing the key components: () faly-scusted hexaroor as the base sructre, (2) 4 Dof manialator, (3) Intel RealSease cameras ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 4. Endeffector wacking performance of aerial manipulator in Ellipse teaectory, Tracking resis ndicale thatthe wo, MPC. baseline exhiis Significant racking lag, while the wo. ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 5. End-effector tacking eror distribution for de types of tajectores using our methods and two baselines.
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 7. Comparison of Figue-8 aad Ellipse tnjecory tracking performance across three methods. Our approach achieves the lowest tacking error in <ynamic trajectory tacking tasks
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 9. (a. End-effector command trajectory using the ce-centicteleapers- tion interface and fll-DOF teleoperation interface, in simulated peg-ihole task, (), Endetfector command trajectory ofthe leamed ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 10. Aerial Teleoperation Manipulation Tasks. We target 1) Acril Writing: UAM ith 2 marker pen wits °2028" on & whiteboan. 2) Rotate Valve: UAM ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 12. Task setup in Mujoco simulation, inching (a) Peg-in-Hole; () Rotate the Valve c) Pick and Place; and () long horizon Open and Retrieve ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Some work also showed amazing results, achieving high-speed grasping, or grasping moving objects [50], but sacrificed payload capacity or precision due to specialized hardware ... | embodiment, simulator version and control stack | p. 2 (4) Rich real-world experiments demonstrated the versatility), p. 2 (4) Rich real-world experiments demonstrated the versatility) |
| Task/environment | In general, although different works have shown success on different specific tasks, the specific system design and algorithm development make the same hardware and ... | reset, timeout, object/scene variation | p. 2 (4) Rich real-world experiments demonstrated the versatility), p. 10 (B. Implementation Details) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 10 (B. Implementation Details), p. 4 (C. Teleportation and Imitation Learning) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 2 (B. Mobile Manipulation Framework and EE-Centric Interface), p. 7 (B. EE-Centrie Policy Learning) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| + Geometric Precision Advantage: Our ee-centric policy achieves 2.5% higher success rate in geometrically sensitive peg in hole task, directly benefiting from task-space supervision ... | definition/direction/unit from same section | p. 10 (B. Implementation Details) |
| The precise end-effector control framework demonstrated superior end-effector tracking accuracy with minimal error. | definition/direction/unit from same section | p. 11 (B. Implementation Details) |
| ‘TABLE V IMITATION LEARNING SIMULATION SUCCESS RATE | definition/direction/unit from same section | p. 10 (B. Implementation Details) |
| Root Mean Square Error (RMSE) is used as the tracking performance evaluation criterion. | definition/direction/unit from same section | p. 8 (A. Experimental Setup) |
| improvements can be achieved through more accurate system modeling and higher-precision hardware to enhance tracking accuracy. | definition/direction/unit from same section | p. 9 (B. Implementation Details) |
| + Aerial Writing: Drawing a target shape (the digit 2025") on a vertical wall, with an overall size of approxirately 3m%0.Sm, This task required ... | definition/direction/unit from same section | p. 8 (A. Experimental Setup) |
| Fig. 7. Comparison of Figue-8 aad Ellipse tnjecory tracking performance across three methods. Our approach achieves the lowest tacking error in <ynamic trajectory tacking ... | definition/direction/unit from same section | p. 9 (Figure/Table caption) |
| Researchers mostly developed a point-contact arm, such as a rigid rod, and proposed the hybrid motion-force control framework, although achieving high-precision tracking performance, struggled ... | definition/direction/unit from same section | p. 2 (4) Rich real-world experiments demonstrated the versatility) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 4, compared with our method (blue), the baseline wo. | comparison identity and matched condition | p. 8 (B. Implementation Details) |
| 1) Trajectory Tracking Task Setup: To show the effectiveness of our proposed method in end-effector trajectory tracking tasks, we perform a comparison between our ... | comparison identity and matched condition | p. 7 (A. Experimental Setup) |
| LI: This baseline excludes the L1 adaptive component, leaving disturbances from UAV and manipulator interactions and modeling uncertainties uncompensated during control execution. | comparison identity and matched condition | p. 7 (A. Experimental Setup) |
| 6¢) compared to the MPC with flexible arm (Fig. | comparison identity and matched condition | p. 8 (B. Implementation Details) |
| End-effector tacking eror distribution for de types of tajectores using our methods and two baselines. | comparison identity and matched condition | p. 9 (B. Implementation Details) |
| Endeffector wacking performance of aerial manipulator in Ellipse teaectory, Tracking resis ndicale thatthe wo, MPC. baseline exhiis Significant racking lag, while the wo. | comparison identity and matched condition | p. 9 (B. Implementation Details) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| MPC: This baseline replaces the ee-centric MPC with the Direct Force Feedback Control(DEFC) method from [38]. which directly controls the end-effector acceleration based on ... | component/input/data sensitivity | p. 7 (A. Experimental Setup) |
| Fig. 3. UAM hardware system design, ilustaing the key components: () faly-scusted hexaroor as the base sructre, (2) 4 Dof manialator, (3) Intel RealSease ... | component/input/data sensitivity | p. 4 (Figure/Table caption) |
| 6 Arm flexibility ablation study for MPC contol. | component/input/data sensitivity | p. 9 (B. Implementation Details) |
| with our ee-centric interface, we do not consider any joint configuration when collecting demonstrations, which allows us to efficiently collect smooth demonstrations without tediously ... | component/input/data sensitivity | p. 10 (B. Implementation Details) |
| After that, we train a joint space ACT policy with the same training setting as the ee-centric ACT policy, except that the end-effector pose ... | component/input/data sensitivity | p. 10 (B. Implementation Details) |
| LI: This baseline excludes the L1 adaptive component, leaving disturbances from UAV and manipulator interactions and modeling uncertainties uncompensated during control execution. | component/input/data sensitivity | p. 7 (A. Experimental Setup) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Our framework consists of a fully-actuated hexarotor with a 4:DoF robotic arm, an end-effector-centrie whole-body: model predictive controller, and a high-level po is end-effector ... | improvements can be achieved through more accurate system modeling and higher-precision hardware to enhance tracking accuracy. | PDF body cue; verify exact table/figure and matched conditions | p. 9 (B. Implementation Details), p. 10 (B. Implementation Details), p. 10 (B. Implementation Details), p. 2 (4) Rich real-world experiments demonstrated the versatility), p. 8 (B. Implementation Details), p. 8 (B. Implementation Details) |
| Primary metric/result | + Multi-Skill Composition: In the open and retrieve task, our ee-centric policy achieves 2 higher success rate than the joint space policy, which demonstrates ... | numeric claim only at cited anchor | p. 10 (B. Implementation Details) |

- Numeric sentences retained from the body:
- **p. 8 / A. Experimental Setup - extractive body cue:** The maximum velocity in the reference trajectory is about 0.2 ms.
- **p. 8 / B. Implementation Details - extractive body cue:** ‘The optimal control problem in the ee-centric MPC is implemented using ACADOS [51] with a 25ms discretisation step and a 2.5s constant prediction horizon, running ...
- **p. 10 / B. Implementation Details - extractive body cue:** We collect 50 episodes for each task.
- **p. 10 / B. Implementation Details - extractive body cue:** Our ACT policy for each task in the simulation is trained with the action chunk size of 100 and limited 5000 epochs.
- **p. 10 / B. Implementation Details - extractive body cue:** We collected 25 episodes of demonstration data via human teleoperation, varying the hole's horizontal position, with each episode taking approximately 2 minutes, culminating in a ...
- **p. 10 / B. Implementation Details - extractive body cue:** The data is downsampled to 10 Hz, and the action chunk size is empirically set to 100 during the

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Although we have demonstrated the proposed framework through various real-world experiments, there are still several limitations due to time constraints and methodological limitations. | p. 11 (IX. LIMITATIONS) |
| body limitation/failure cue | Incorporating onboard perception to detect obstacles and generate safety constraints in real-time will be our next step, as various studies have demonstrated the feasibility ... | p. 11 (IX. LIMITATIONS) |
| body limitation/failure cue | MPC (orange) suffers from significant motion lag, as DFFC fails to account for trajectory feedforward. | p. 8 (B. Implementation Details) |
| body limitation/failure cue | LI: This baseline excludes the L1 adaptive component, leaving disturbances from UAV and manipulator interactions and modeling uncertainties uncompensated during control execution. | p. 7 (A. Experimental Setup) |
| body limitation/failure cue | 8 shows disturbances along the base x (red), = (blue) and Open (green), respectively. ‘The disturbances and model uncertainties primarily arise from arm motions, ... | p. 8 (B. Implementation Details) |
| body limitation/failure cue | 7 reveals that tracking error increases at lower altitudes (around Im), likely due to unmodeled ground and wall effect disturbances. | p. 9 (B. Implementation Details) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Some work also showed amazing results, achieving high-speed grasping, or grasping moving objects [50], but sacrificed payload capacity or precision due to specialized hardware ... | p. 2 (4) Rich real-world experiments demonstrated the versatility) |
| In general, although different works have shown success on different specific tasks, the specific system design and algorithm development make the same hardware and ... | p. 2 (4) Rich real-world experiments demonstrated the versatility) |
| Horizon Length Horizoa Steps NV State Cost Qy Rotation Cost Qe. | p. 8 (A. Experimental Setup) |
| Each trajectory is repeated three times to compute the mean and standard deviation, | p. 8 (A. Experimental Setup) |
| improvements can be achieved through more accurate system modeling and higher-precision hardware to enhance tracking accuracy. | p. 9 (B. Implementation Details) |
| More details on implementation are included in Appendix A. | p. 10 (B. Implementation Details) |
| After training, wwe choose the policy with the least validation loss to perform 50 evaluation trials. | p. 10 (B. Implementation Details) |
| After training through 100,000 epochs, the policy with the least validation loss is selected. | p. 11 (B. Implementation Details) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 11 / IX. LIMITATIONS - extractive body cue:** Although we have demonstrated the proposed framework through various real-world experiments, there are still several limitations due to time constraints and methodological limitations.
- **p. 11 / IX. LIMITATIONS - extractive body cue:** Incorporating onboard perception to detect obstacles and generate safety constraints in real-time will be our next step, as various studies have demonstrated the feasibility of ...
- **p. 8 / B. Implementation Details - extractive body cue:** MPC (orange) suffers from significant motion lag, as DFFC fails to account for trajectory feedforward.
- **p. 7 / A. Experimental Setup - extractive body cue:** LI: This baseline excludes the L1 adaptive component, leaving disturbances from UAV and manipulator interactions and modeling uncertainties uncompensated during control execution.
- **p. 8 / B. Implementation Details - extractive body cue:** 8 shows disturbances along the base x (red), = (blue) and Open (green), respectively. ‘The disturbances and model uncertainties primarily arise from arm motions, inaccurate ...
- **p. 9 / B. Implementation Details - extractive body cue:** 7 reveals that tracking error increases at lower altitudes (around Im), likely due to unmodeled ground and wall effect disturbances.

- **PDF anchors reviewed:** datasets p. 2 (4) Rich real-world experiments demonstrated the versatility), p. 2 (4) Rich real-world experiments demonstrated the versatility), p. 10 (B. Implementation Details), p. 10 (B. Implementation Details), p. 9 (B. Implementation Details), p. 11 (B. Implementation Details), metrics p. 10 (B. Implementation Details), p. 11 (B. Implementation Details), p. 10 (B. Implementation Details), p. 8 (A. Experimental Setup), p. 9 (B. Implementation Details), p. 8 (A. Experimental Setup), baselines p. 8 (B. Implementation Details), p. 7 (A. Experimental Setup), p. 7 (A. Experimental Setup), p. 8 (B. Implementation Details), p. 9 (B. Implementation Details), p. 9 (B. Implementation Details), results p. 9 (B. Implementation Details), p. 10 (B. Implementation Details), p. 10 (B. Implementation Details), p. 2 (4) Rich real-world experiments demonstrated the versatility), p. 8 (B. Implementation Details), p. 8 (B. Implementation Details).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
