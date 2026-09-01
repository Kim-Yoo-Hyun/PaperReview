# Evaluation - Kinodynamic Trajectory Following with STELA: Simultaneous Trajectory Estimation & Local Adaptation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (15 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p008.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p008.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 11 (Figure/Table caption), p. 12 (A. Experimemal setup), p. 11 (A. Experimemal setup), p. 12 (A. Experimemal setup), p. 10 (A. Experimemal setup), p. 10 (A. Experimemal setup)): Fig. 11: STL results for MuSHR (sim). Three normalized metrics reported, Time to collision isthe rate of a trajectory traversed before a collision (no data if the success rate is ...

## Evaluation Body Digest

- **p. 5 / V. SIMULTANEOUS TRAIECTORY ESTIMATION - extractive body cue:** Given the identified robot model /, (1, us). an environment ‘map that identifies obstacle regions %, and a motion planning query specifying 9 and Xq. ...
- **p. 9 / A. Experimemal setup - extractive body cue:** (Right) Observations "2 ate camera estimates of the robot's pose with the highest level of ‘observation noise (05) chosen to match the real-world setup.
- **p. 12 / A. Experimemal setup - extractive body cue:** Real experiments are performed with a MuSHR [40] robot the scenes of Figures / and 8.
- **p. 8 / A. Experimemal setup - extractive body cue:** 7 and with a real MuSHR [40] robot in the environments. shown in Fig. / and 8, "The system is tested against four levels o ...
- **p. 5 / B. Trajectory Optimization as a Motion Planner - extractive body cue:** 3: An 6 for robot planning employs the robot's model dy = Folds.) on a dynamics factor to compute a trajectory of T states, Sarting ...
- **p. 6 / B. The STELA Factor Graph - extractive body cue:** While the SEMP trajectory initialization is collision-free, a robot may move dangerously close to obstacles due to the model gap and noise.
- **p. 6 / B. The STELA Factor Graph - extractive body cue:** ‘The observation factor incorporates observations 10 estimate the executed trajectory. ‘This work considers observations of the configuration g! that are generated asynchronously as the robot ...
- **p. 9 / A. Experimemal setup - extractive body cue:** (Bottom) The robot follows & desied trajectory planned without obstacles, During execution, the envionment has movable obstacles.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** robot mechanism의 state와 task-space dynamics.
- **Input boundary:** joint/task state, reference와 sensor feedback.
- **Output/decision under evaluation:** torque, force, velocity 또는 position command.
- **Primary target:** tracking, stability, constraint satisfaction과 contact behavior.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | EMPIRICAL / REAL-ROBOT OR HARDWARE | Fig. 11: STL results for MuSHR (sim). Three normalized metrics reported, Time to collision isthe rate of a trajectory traversed before a collision (no ... | p. 11 (Figure/Table caption) |
| A. Experimemal setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | The low= cost trajectories returned from the SBMP are likely, however, to be in close proximity to obstacles, which makes following them susceptible to ... | p. 12 (A. Experimemal setup) |
| A. Experimemal setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | Simulation Results , / eee ‘Tables Ill, and Ill show the success rate of each algoPed rithm per environment for the LTV-SDE system in ... | p. 11 (A. Experimemal setup) |
| A. Experimemal setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | It also significantly outperforms alternatives in simulated evaluations as noise increases, while achieving desirable high-frequency control update rates, | p. 12 (A. Experimemal setup) |
| A. Experimemal setup | EMPIRICAL / REAL-ROBOT OR HARDWARE | VSO aga Xnoie Xing Xrose --Xnoite Sea = es # to-{ro-foaet ore t0-[-t0-{ totam] $eee +t totam foe / oof to foe rome) Bal ... | p. 10 (A. Experimemal setup) |

## Dataset / Benchmark Role

- **p. 5 / V. SIMULTANEOUS TRAIECTORY ESTIMATION - extractive body cue:** Given the identified robot model /, (1, us). an environment ‘map that identifies obstacle regions %, and a motion planning query specifying 9 and Xq. ...
- **p. 9 / A. Experimemal setup - extractive body cue:** (Right) Observations "2 ate camera estimates of the robot's pose with the highest level of ‘observation noise (05) chosen to match the real-world setup.
- **p. 12 / A. Experimemal setup - extractive body cue:** Real experiments are performed with a MuSHR [40] robot the scenes of Figures / and 8.
- **p. 8 / A. Experimemal setup - extractive body cue:** 7 and with a real MuSHR [40] robot in the environments. shown in Fig. / and 8, "The system is tested against four levels o ...
- **p. 5 / B. Trajectory Optimization as a Motion Planner - extractive body cue:** 3: An 6 for robot planning employs the robot's model dy = Folds.) on a dynamics factor to compute a trajectory of T states, Sarting ...
- **p. 6 / B. The STELA Factor Graph - extractive body cue:** While the SEMP trajectory initialization is collision-free, a robot may move dangerously close to obstacles due to the model gap and noise.
- **p. 6 / B. The STELA Factor Graph - extractive body cue:** ‘The observation factor incorporates observations 10 estimate the executed trajectory. ‘This work considers observations of the configuration g! that are generated asynchronously as the robot ...
- **p. 9 / A. Experimemal setup - extractive body cue:** (Bottom) The robot follows & desied trajectory planned without obstacles, During execution, the envionment has movable obstacles.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 5. is general in nature and can be applied to any dynamical system given access to first or second-order state update equations. It does ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2: A wypical unjectory estimation £6 at time T uses state observations 2*(0 : 7) and the robot model s+ = fg(ar, ue) to ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: An 6 for robot planning employs the robot's model dy = Folds.) on a dynamics factor to compute a trajectory of T states, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4: Asynchronous system architecture: Offline, a system iden- tification process. generates a #-based dynamics model of the robot system. A motion planner receives the ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 5. The proposed FG includes six different factor types, Bach factor is defined as J (-) x exp(}///d ()/[2) for a factor- specific error ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: (Left) The dynamics factor graph corresponding to each edge of the desired trajectory with all associated factors. (Middle) For
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 7: Simulated environments used for experiments with the LTV. SDE and MuSHR models. Letters indicate candidate starts and goals ‘The Simple Obstacle environment is ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 8: Experiments on a real MaSHR. (Top) The rbot navigates between (A-B), (CA), and (D-B),avoing obstacles. rita poses in colo, ad fal poses in ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Given the identified robot model /, (1, us). an environment ‘map that identifies obstacle regions %, and a motion planning query specifying 9 and ... | embodiment, simulator version and control stack | p. 5 (V. SIMULTANEOUS TRAIECTORY ESTIMATION), p. 9 (A. Experimemal setup) |
| Task/environment | (Right) Observations "2 ate camera estimates of the robot's pose with the highest level of ‘observation noise (05) chosen to match the real-world setup. | reset, timeout, object/scene variation | p. 9 (A. Experimemal setup), p. 12 (A. Experimemal setup) |
| Observation/sensor | joint/task state, reference와 sensor feedback | calibration, preprocessing, privileged input | p. 2 (1. INTRODUCTION), p. 2 (1. INTRODUCTION) |
| Output/decision | torque, force, velocity 또는 position command | action frame, controller and termination | p. 4 (1. INTRODUCTION), p. 4 (1. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Fig. 11: STL results for MuSHR (sim). Three normalized metrics reported, Time to collision isthe rate of a trajectory traversed before a collision (no ... | definition/direction/unit from same section | p. 11 (Figure/Table caption) |
| 10 presents the Time to Collision, Normalized ‘Trajectory Gas Error, and Estimation Error for the LT'V-SDE Forest scenario. ee/ ** Experiments with zero success ... | definition/direction/unit from same section | p. 11 (A. Experimemal setup) |
| STELA gets a 100% success rate on the lowest noise levels while maintaining a high success rate on the most challenging levels across all ... | definition/direction/unit from same section | p. 12 (A. Experimemal setup) |
| VSO aga Xnoie Xing Xrose --Xnoite Sea = es # to-{ro-foaet ore t0-[-t0-{ totam] $eee +t totam foe / oof to foe rome) Bal ... | definition/direction/unit from same section | p. 10 (A. Experimemal setup) |
| TIVSDE> Fast ‘pea Lap BMP Replay SMEN a sax en i ey Das [1a 9s / 04s [or 04 [Pa 040 /-038 / 40 ... | definition/direction/unit from same section | p. 10 (A. Experimemal setup) |
| This paper presents STELA, a novel approach that seamlessly integrates the output of kinodynamic sampling-based motion planning with an integrated approach for trajectory estimation ... | definition/direction/unit from same section | p. 12 (A. Experimemal setup) |
| The mean error and the standard deviation of these pose estimation were measured given ground-truth. | definition/direction/unit from same section | p. 9 (A. Experimemal setup) |
| These observations are used by STELA to estimate the executed trajectory and generate ‘controls to be forwarded to the robot ata high frequency, The ... | definition/direction/unit from same section | p. 6 (V. SIMULTANEOUS TRAIECTORY ESTIMATION) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The baseline comparison point is open-loop execution of the desired trajectory. | comparison identity and matched condition | p. 10 (A. Experimemal setup) |
| No experiments were " " " performed for non-zero observation noise since no estimation LO) Forest was performed in the case of the OPEN-LOOP ... | comparison identity and matched condition | p. 11 (A. Experimemal setup) |
| It also significantly outperforms alternatives in simulated evaluations as noise increases, while achieving desirable high-frequency control update rates, | comparison identity and matched condition | p. 12 (A. Experimemal setup) |
| (Bottom) The robot follows & desied trajectory planned without obstacles, During execution, the envionment has movable obstacles. | comparison identity and matched condition | p. 9 (A. Experimemal setup) |
| Comparison Points: Table V shows the number of problems (start-goal queries) per scene selected to test STELA against the alternatives. | comparison identity and matched condition | p. 9 (A. Experimemal setup) |
| DE Forest - Comparison of the Time 10 | comparison identity and matched condition | p. 10 (A. Experimemal setup) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| The ablation evaluation of the effect of the sliding window size, the use of the duration AT' as a factor variable, the impact of ... | component/input/data sensitivity | p. 12 (A. Experimemal setup) |
| The low= cost trajectories returned from the SBMP are likely, however, to be in close proximity to obstacles, which makes following them susceptible to ... | component/input/data sensitivity | p. 12 (A. Experimemal setup) |
| (Bottom) The robot follows & desied trajectory planned without obstacles, During execution, the envionment has movable obstacles. | component/input/data sensitivity | p. 9 (A. Experimemal setup) |
| goal without collisions; the most critical metric for safety. | component/input/data sensitivity | p. 10 (A. Experimemal setup) |
| The second variant is initialized with the same desired plan from the SeMP as the proposed STELA approach. | component/input/data sensitivity | p. 10 (A. Experimemal setup) |
| 4le) ‘observation factors are fot used for the ‘local "adaptation ‘component of the optimization, | component/input/data sensitivity | p. 7 (C. Inference over a Sliding Window) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The sliding, window mechanism allows the factor graph to be dynamically updated at high frequency by operating over a limited past history and forward ... | Fig. 11: STL results for MuSHR (sim). Three normalized metrics reported, Time to collision isthe rate of a trajectory traversed before a collision (no ... | PDF body cue; verify exact table/figure and matched conditions | p. 11 (Figure/Table caption), p. 12 (A. Experimemal setup), p. 11 (A. Experimemal setup), p. 12 (A. Experimemal setup), p. 10 (A. Experimemal setup), p. 10 (A. Experimemal setup) |
| Primary metric/result | The low= cost trajectories returned from the SBMP are likely, however, to be in close proximity to obstacles, which makes following them susceptible to ... | numeric claim only at cited anchor | p. 12 (A. Experimemal setup) |

- Numeric sentences retained from the body:
- **p. 8 / A. Experimemal setup - extractive body cue:** 7 and with a real MuSHR [40] robot in the environments. shown in Fig. / and 8, "The system is tested against four levels o ...
- **p. 10 / A. Experimemal setup - extractive body cue:** SCATE-Naive: ‘SCATE-SBMP STELA a wea ler / os / lle / of / of [ot lle [al / of / oF 10 OO 10-10] 10] ...
- **p. 10 / A. Experimemal setup - extractive body cue:** TIVSDE> Fast ‘pea Lap BMP Replay SMEN a sax en i ey Das [1a 9s / 04s [or 04 [Pa 040 /-038 / 40 /} ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | The "multiple obstacles" environment is similar to the setups from simulated experiments, where collisions with obstacles are considered failures. | p. 12 (A. Experimemal setup) |
| body limitation/failure cue | The second environment considers a set of movable boxes that are not present during planning, and the robot ‘can collide online without considering a ... | p. 12 (A. Experimemal setup) |
| body limitation/failure cue | Fig. 11: STL results for MuSHR (sim). Three normalized metrics reported, Time to collision isthe rate of a trajectory traversed before a collision (no ... | p. 11 (Figure/Table caption) |
| body limitation/failure cue | While the SEMP trajectory initialization is collision-free, a robot may move dangerously close to obstacles due to the model gap and noise. | p. 6 (B. The STELA Factor Graph) |
| body limitation/failure cue | 13 for both STEZA and SCATE. e OPEN-LOOP showeases the effects of noise on the system's as/ 2? dynamics, resulting in collisions as soon ... | p. 11 (A. Experimemal setup) |
| body limitation/failure cue | Fig. 14: The effects of state-space noise in collision on the Forest environment for the Open-loop baseline (left) and the proposed STELA (middle). The ... | p. 13 (Figure/Table caption) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| 3: An 6 for robot planning employs the robot's model dy = Folds.) on a dynamics factor to compute a trajectory of T states, ... | p. 5 (B. Trajectory Optimization as a Motion Planner) |
| 2 presents a typical #6 for, past trajectory estimation, Te computes p(Orple) ox JTF = sires sertonation where f= [Tho ££" (0,) is the ... | p. 5 (A. Trajectory Estimation) |
| Lower limits can be computed similarly. | p. 6 (B. The STELA Factor Graph) |
| function j - f(u,)- The error function uses the predicted velocity term q?"¢" = g; + GAt to compute the error function: Euler integration ... | p. 6 (B. The STELA Factor Graph) |
| AEG associated with the entire desired trajectory returned by the SMP planner has at least 2/.V/ + 2/2] €G-variables and 6/N/+-5/// £G-factors, At runtime, ... | p. 7 (C. Inference over a Sliding Window) |
| Both algorithms are executed in a server with 72 cores, but each experiment is limited to 8 cores (the number of cores found in ... | p. 9 (A. Experimemal setup) |
| Both implementations of SCATE use the same obstacle factor as STELA and also include a factor to ensure that the controls are within the ... | p. 10 (A. Experimemal setup) |
| The low= cost trajectories returned from the SBMP are likely, however, to be in close proximity to obstacles, which makes following them susceptible to ... | p. 12 (A. Experimemal setup) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 12 / A. Experimemal setup - extractive body cue:** The "multiple obstacles" environment is similar to the setups from simulated experiments, where collisions with obstacles are considered failures.
- **p. 12 / A. Experimemal setup - extractive body cue:** The second environment considers a set of movable boxes that are not present during planning, and the robot ‘can collide online without considering a failure, ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 11: STL results for MuSHR (sim). Three normalized metrics reported, Time to collision isthe rate of a trajectory traversed before a collision (no data ...
- **p. 6 / B. The STELA Factor Graph - extractive body cue:** While the SEMP trajectory initialization is collision-free, a robot may move dangerously close to obstacles due to the model gap and noise.
- **p. 11 / A. Experimemal setup - extractive body cue:** 13 for both STEZA and SCATE. e OPEN-LOOP showeases the effects of noise on the system's as/ 2? dynamics, resulting in collisions as soon as ...
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 14: The effects of state-space noise in collision on the Forest environment for the Open-loop baseline (left) and the proposed STELA (middle). The top ...

- **PDF anchors reviewed:** datasets p. 5 (V. SIMULTANEOUS TRAIECTORY ESTIMATION), p. 9 (A. Experimemal setup), p. 12 (A. Experimemal setup), p. 8 (A. Experimemal setup), p. 5 (B. Trajectory Optimization as a Motion Planner), p. 6 (B. The STELA Factor Graph), metrics p. 11 (Figure/Table caption), p. 11 (A. Experimemal setup), p. 12 (A. Experimemal setup), p. 10 (A. Experimemal setup), p. 10 (A. Experimemal setup), p. 12 (A. Experimemal setup), baselines p. 10 (A. Experimemal setup), p. 11 (A. Experimemal setup), p. 12 (A. Experimemal setup), p. 9 (A. Experimemal setup), p. 9 (A. Experimemal setup), p. 10 (A. Experimemal setup), results p. 11 (Figure/Table caption), p. 12 (A. Experimemal setup), p. 11 (A. Experimemal setup), p. 12 (A. Experimemal setup), p. 10 (A. Experimemal setup), p. 10 (A. Experimemal setup).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
