# Evaluation - Hybrid Position/Force Control of Manipulators

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1115/1.3139652; PDF retrieval source: https://doi.org/10.1115/1.3139652. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 4 (Front matter), p. 5 (Front matter), p. 6 (Front matter), p. 7 (Front matter), p. 4 (Front matter), p. 6 (Front matter)): To improve thermal immunity, gauges mounted on opposite faces are operated as voltage divider pairs [9J.

## Evaluation Body Digest

- **p. 5 / Front matter - extractive body cue:** 5 Model used for simulation of hybrid control task 1 1 l-Kwwt -Acosfa,)] w2 = TT \-~K^w7. +Asin(<?i)l M3 Reaction surface model: fx=K,.(Cx CXf) Cx ...
- **p. 7 / Front matter - extractive body cue:** 11 The hybrid controller Is used for peg·ln·hole task ¥;:;;6 u ~ ~ 3 u 9 ----- 30 E "'-z 0 20 E 2 >- ...
- **p. 2 / Front matter - extractive body cue:** It is an N degree of freedom Cartesian system defined with respect to the task geometry.
- **p. 2 / Front matter - extractive body cue:** 1 Examples of force control tasks showing the constraint frame /C/, natural constraints, and artificial constraints.
- **p. 3 / Front matter - extractive body cue:** Eventually the natural constraints that correspond to a particular task may be determined automatically by an algorithm that makes use of knowledge about the task ...
- **p. 3 / Front matter - extractive body cue:** Though selection of the constraint frame's position and orientation is a matter of discretion, a suitable choice can make the task of determining the natural ...
- **p. 4 / Front matter - extractive body cue:** Also acting on the hand is reaction force fx produced through contact with an environmental surface.
- **p. 4 / Front matter - extractive body cue:** 3 was used to test the hybrid controller with simulations and the physical experiments reported in Figs.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Front matter | EMPIRICAL / SIMULATION | To improve thermal immunity, gauges mounted on opposite faces are operated as voltage divider pairs [9J. | p. 4 (Front matter) |
| Front matter | EMPIRICAL / SIMULATION | Force control was achieved by combining proportional-integral (PI) control with a saturation-type feedback limiter and a simple feed forward term. | p. 5 (Front matter) |
| Front matter | EMPIRICAL / SIMULATION | Therefore, stability is more easily achieved. | p. 6 (Front matter) |
| Front matter | EMPIRICAL / SIMULATION | These changes resulted in improved force response -less overshoot and better stability - but did not affect the position servo perceptibly. | p. 7 (Front matter) |
| Front matter | EMPIRICAL / SIMULATION | Our goals were to examine the feasibility of the hybrid method with regard to accuracy, interactions between force and position control and stability. | p. 4 (Front matter) |

## Dataset / Benchmark Role

- **p. 5 / Front matter - extractive body cue:** 5 Model used for simulation of hybrid control task 1 1 l-Kwwt -Acosfa,)] w2 = TT \-~K^w7. +Asin(<?i)l M3 Reaction surface model: fx=K,.(Cx CXf) Cx ...
- **p. 7 / Front matter - extractive body cue:** 11 The hybrid controller Is used for peg·ln·hole task ¥;:;;6 u ~ ~ 3 u 9 ----- 30 E "'-z 0 20 E 2 >- ...
- **p. 2 / Front matter - extractive body cue:** It is an N degree of freedom Cartesian system defined with respect to the task geometry.
- **p. 2 / Front matter - extractive body cue:** 1 Examples of force control tasks showing the constraint frame /C/, natural constraints, and artificial constraints.
- **p. 3 / Front matter - extractive body cue:** Eventually the natural constraints that correspond to a particular task may be determined automatically by an algorithm that makes use of knowledge about the task ...
- **p. 3 / Front matter - extractive body cue:** Though selection of the constraint frame's position and orientation is a matter of discretion, a suitable choice can make the task of determining the natural ...
- **p. 4 / Front matter - extractive body cue:** Also acting on the hand is reaction force fx produced through contact with an environmental surface.
- **p. 4 / Front matter - extractive body cue:** 3 was used to test the hybrid controller with simulations and the physical experiments reported in Figs.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- figure/table caption cue 없음

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 5 Model used for simulation of hybrid control task 1 1 l-Kwwt -Acosfa,)] w2 = TT \-~K^w7. +Asin(<?i)l M3 Reaction surface model: fx=K,.(Cx CXf) ... | embodiment, simulator version and control stack | p. 5 (Front matter), p. 7 (Front matter) |
| Task/environment | 11 The hybrid controller Is used for peg·ln·hole task ¥;:;;6 u ~ ~ 3 u 9 ----- 30 E "'-z 0 20 E 2 ... | reset, timeout, object/scene variation | p. 7 (Front matter), p. 2 (Front matter) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 3 (Front matter), p. 1 (Front matter) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 1 (Front matter), p. 3 (Front matter) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| As the manipulator moves, irregularities in the reaction surface and small errors in the accuracy of the position servo will look like surface motion ... | definition/direction/unit from same section | p. 7 (Front matter) |
| N [Vx] rotation matrix from [H] to {C) 0 -V, o -v[ v, o V = vector from the origin of (C) to the ... | definition/direction/unit from same section | p. 4 (Front matter) |
| Notice that sensory signals must be transformed from the coordinate system of the transducer, [q] for position and [H] for force, into (C) before ... | definition/direction/unit from same section | p. 3 (Front matter) |
| The actuator control signal for the /'th joint has N components - one for each force controlled degree of freedom in [C], and one ... | definition/direction/unit from same section | p. 3 (Front matter) |
| These errors are corrected on subsequent cycles by adjusting the position setpoints differentially. | definition/direction/unit from same section | p. 4 (Front matter) |
| Using equations (3) and (4) to find position and force errors in(CJ: A X ( 0 = c X r f ( 0 - ... | definition/direction/unit from same section | p. 5 (Front matter) |
| Force errors do not exceed 1.75 Nt except at the ends of the ramp where there are accelerations. | definition/direction/unit from same section | p. 6 (Front matter) |
| To compensate for this effect a saturation type non-linearity was included which reduced the effective integral gain for large values of force error. | definition/direction/unit from same section | p. 6 (Front matter) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Without this term the system was stable only when heavily overdamped. | comparison identity and matched condition | p. 6 (Front matter) |
| Comparison with previous results [1 and unpublished] shows that use of force feed-forward gives faithful trajectory control with relatively low force feedback gains. | comparison identity and matched condition | p. 6 (Front matter) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Without this term the system was stable only when heavily overdamped. | component/input/data sensitivity | p. 6 (Front matter) |
| Every manipulation task can be broken down into elemental components that are defined by a particular set of contacting surfaces. | component/input/data sensitivity | p. 2 (Front matter) |
| In these examples [vx,Vy,vz, u xu y, u z] T is the hand's velocity vector, 3 translational and 3 angular components, given in [C\. | component/input/data sensitivity | p. 2 (Front matter) |
| The actuator control signal for the /'th joint has N components - one for each force controlled degree of freedom in [C], and one ... | component/input/data sensitivity | p. 3 (Front matter) |
| The primary frictional component in the JPL Scheinman arm is due to Coulomb sliding force. | component/input/data sensitivity | p. 5 (Front matter) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Note that the method we propose here does not prescribe particular feedback control laws for the regulation of errors. | To improve thermal immunity, gauges mounted on opposite faces are operated as voltage divider pairs [9J. | PDF body cue; verify exact table/figure and matched conditions | p. 4 (Front matter), p. 5 (Front matter), p. 6 (Front matter), p. 7 (Front matter), p. 4 (Front matter), p. 6 (Front matter) |
| Primary metric/result | Force control was achieved by combining proportional-integral (PI) control with a saturation-type feedback limiter and a simple feed forward term. | numeric claim only at cited anchor | p. 5 (Front matter) |

- Numeric sentences retained from the body:
- **p. 2 / Front matter - extractive body cue:** 0 L = 0 x ' » x - o Tro Ux = o a; = 0 y ARTIFICIAL CONSTRAINTS v = 0 y " ...
- **p. 4 / Front matter - extractive body cue:** The gauges are operated as 8 voltage-divider pairs to measure distortions, and therefore forces, in 6 degrees of freedom in the hand coordinate system [H].
- **p. 5 / Front matter - extractive body cue:** The force sensor is also represented as a spring, K„ = 8 x 105 Nt/m, between the hand and the arm.
- **p. 5 / Front matter - extractive body cue:** The model includes a simplified static friction term plus the Coulomb force: r-sgn(<7,.)[min(Ti];,lT,-l)] L-sgn(<7i)[Tc,i] where: TS = static friction constant TC = Coulomb friction constant ...
- **p. 6 / Front matter - extractive body cue:** Except where noted, all data shown below were obtained with a sampling rate and servo rate of 16.7 ms (60 Hz).
- **p. 6 / Front matter - extractive body cue:** Force trajectories were filtered with a 12 Hz cutoff before plotting.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | A rigid X-Y table under precise numeric control was used to provide reaction forces and disturbance motions to the manipulator hand during testing. | p. 4 (Front matter) |
| body limitation/failure cue | As motion begins force control degrades somewhat, although contact with the reaction surface is never lost. | p. 6 (Front matter) |
| body limitation/failure cue | The upper two curves show response to the artificial constraints while the lower curve shows the position disturbance. error in the steady state was ... | p. 6 (Front matter) |
| body limitation/failure cue | Our ramp disturbance data suggest adequate force control is possible under such circumstances. | p. 7 (Front matter) |
| body limitation/failure cue | Although some error in position occurs along the position trajectory, the force step produces no noticeable disturbance in position. | p. 7 (Front matter) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Though recent advances in robotics technology have led to the application of computer controlled manipulators to industrial handling and simple assembly operations, advances in ... | p. 1 (Front matter) |
| A General Automation SPC-16/85 minicomputer was used to perform all control and simulation computations. | p. 4 (Front matter) |
| Experiments In order to examine the behavior of the proposed hybrid control method we conducted simple experiments involving simulation and physical implementation. | p. 4 (Front matter) |
| The hybrid controller implementation that was used for experimentation is now given. | p. 5 (Front matter) |
| The model includes a simplified static friction term plus the Coulomb force: r-sgn(<7,.)[min(Ti];,lT,-l)] L-sgn(<7i)[Tc,i] where: TS = static friction constant TC = Coulomb friction ... | p. 5 (Front matter) |
| 7 Response of physical system to 1, 5, and 10 Nt force steps. | p. 6 (Front matter) |
| 6 Hybrid controller implementation Since force rate information was not used in the force loop, all damping was provided mechanically. | p. 6 (Front matter) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 4 / Front matter - extractive body cue:** A rigid X-Y table under precise numeric control was used to provide reaction forces and disturbance motions to the manipulator hand during testing.
- **p. 6 / Front matter - extractive body cue:** As motion begins force control degrades somewhat, although contact with the reaction surface is never lost.
- **p. 6 / Front matter - extractive body cue:** The upper two curves show response to the artificial constraints while the lower curve shows the position disturbance. error in the steady state was < ...
- **p. 7 / Front matter - extractive body cue:** Our ramp disturbance data suggest adequate force control is possible under such circumstances.
- **p. 7 / Front matter - extractive body cue:** Although some error in position occurs along the position trajectory, the force step produces no noticeable disturbance in position.

- **PDF anchors reviewed:** datasets p. 5 (Front matter), p. 7 (Front matter), p. 2 (Front matter), p. 2 (Front matter), p. 3 (Front matter), p. 3 (Front matter), metrics p. 7 (Front matter), p. 4 (Front matter), p. 3 (Front matter), p. 3 (Front matter), p. 4 (Front matter), p. 5 (Front matter), baselines p. 6 (Front matter), p. 6 (Front matter), results p. 4 (Front matter), p. 5 (Front matter), p. 6 (Front matter), p. 7 (Front matter), p. 4 (Front matter), p. 6 (Front matter).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
