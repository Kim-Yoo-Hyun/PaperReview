# Evaluation - Control-Limited Differential Dynamic Programming

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/ICRA.2014.6907001; PDF retrieval source: https://roboti.us/lab/papers/TassaICRA14.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (IV. RESULTS), p. 5 (IV. RESULTS)): However, despite some recent work in this direction [34], direct feed-forward current control is not yet a functional option, while the lack of joint torque sensor on most of hu0 ...

## Evaluation Body Digest

- **p. 4 / IV. RESULTS - extractive body cue:** Finally, we demonstrate box-DDP on a complex platform, the humanoid robot HRP-2.
- **p. 5 / IV. RESULTS - extractive body cue:** Car Parking For the car-like robot, one of the control variables, the angle of the front wheels, is a kinematic, rather than a dynamic variable.
- **p. 6 / IV. RESULTS - extractive body cue:** Two solutions are possible to apply the DDP on a robot such as HRP-2.
- **p. 6 / IV. RESULTS - extractive body cue:** Optimal control allows for very simple specification of the robot movement.
- **p. 4 / IV. RESULTS - extractive body cue:** All the experiments are performed in simulation, which is enough to demonstrate the relationship with respect to unconstrained classical DDP.
- **p. 5 / IV. RESULTS - extractive body cue:** Middle: the control trajectory U ≡{u0 . . . u199}.
- **p. 4 / IV. RESULTS - extractive body cue:** We generated random LQ problems as follows.
- **p. 4 / IV. RESULTS - extractive body cue:** The squashing demonstrates a sub-linear convergence.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** robot mechanism의 state와 task-space dynamics.
- **Input boundary:** joint/task state, reference와 sensor feedback.
- **Output/decision under evaluation:** torque, force, velocity 또는 position command.
- **Primary target:** tracking, stability, constraint satisfaction과 contact behavior.
- **Detected evaluation headings:** IV. RESULTS (p. 4).

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| IV. RESULTS | EMPIRICAL / SIMULATION | However, despite some recent work in this direction [34], direct feed-forward current control is not yet a functional option, while the lack of joint ... | p. 6 (IV. RESULTS) |
| IV. RESULTS | EMPIRICAL / SIMULATION | 3 compares the results obtained with the two solvers. | p. 5 (IV. RESULTS) |

## Dataset / Benchmark Role

- **p. 4 / IV. RESULTS - extractive body cue:** Finally, we demonstrate box-DDP on a complex platform, the humanoid robot HRP-2.
- **p. 5 / IV. RESULTS - extractive body cue:** Car Parking For the car-like robot, one of the control variables, the angle of the front wheels, is a kinematic, rather than a dynamic variable.
- **p. 6 / IV. RESULTS - extractive body cue:** Two solutions are possible to apply the DDP on a robot such as HRP-2.
- **p. 6 / IV. RESULTS - extractive body cue:** Optimal control allows for very simple specification of the robot movement.
- **p. 4 / IV. RESULTS - extractive body cue:** All the experiments are performed in simulation, which is enough to demonstrate the relationship with respect to unconstrained classical DDP.
- **p. 5 / IV. RESULTS - extractive body cue:** Middle: the control trajectory U ≡{u0 . . . u199}.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Left: The humanoid robot HRP-2. Right: Real-time reaching and balancing behaviors are described in Section IV and in the attached movie. methods are ...
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 2. Control-bounded random linear systems. Here h = 0.01, n = 20, m = 7 and N = 200. Top: A typical state trajectory ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3. Comparison between squashing-functions and BOX-DDP. Left column: Bird's eye view of the parking trajectories obtained after convergence of both DDP, starting from (1, ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 4. Cost decrease ∆J of the two algorithms for the car-parking problem. Box-DDP converges quadratically after 64 iterations, while the squashing-function solution has barely ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5. Reaching a moving target, stepping when necessary. A sequence of frames of full body motion synthesized in real-time for the HRP2 robot. The ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | Finally, we demonstrate box-DDP on a complex platform, the humanoid robot HRP-2. | embodiment, simulator version and control stack | p. 4 (IV. RESULTS), p. 5 (IV. RESULTS) |
| Task/environment | Car Parking For the car-like robot, one of the control variables, the angle of the front wheels, is a kinematic, rather than a dynamic ... | reset, timeout, object/scene variation | p. 5 (IV. RESULTS), p. 6 (IV. RESULTS) |
| Observation/sensor | joint/task state, reference와 sensor feedback | calibration, preprocessing, privileged input | p. 2 (II. DIFFERENTIAL DYNAMIC PROGRAMMING), p. 1 (Abstract) |
| Output/decision | torque, force, velocity 또는 position command | action frame, controller and termination | p. 1 (I. INTRODUCTION), p. 3 (C. Line Search) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We generated random LQ problems as follows. | definition/direction/unit from same section | p. 4 (IV. RESULTS) |
| The squashing demonstrates a sub-linear convergence. | definition/direction/unit from same section | p. 4 (IV. RESULTS) |
| 4 gives the convergence rate comparison. | definition/direction/unit from same section | p. 5 (IV. RESULTS) |
| Distance was measured using the Hubertype function z(x,p) = √ x2 + p2-p. | definition/direction/unit from same section | p. 5 (IV. RESULTS) |
| In the demonstrated example, the robot has to reach a moving target with its right gripper, while standing and if necessary stepping to maintain ... | definition/direction/unit from same section | p. 6 (IV. RESULTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The bottom row of Figure 2 shows a comparison between the clamping and squashing heuristics and the proposed algorithm. | comparison identity and matched condition | p. 4 (IV. RESULTS) |
| We begin with an initial comparison of the three solution types on a set of simple linear systems randomly selected in Sec. | comparison identity and matched condition | p. 4 (IV. RESULTS) |
| 4 gives the convergence rate comparison. | comparison identity and matched condition | p. 5 (IV. RESULTS) |
| Fig. 3. Comparison between squashing-functions and BOX-DDP. Left column: Bird's eye view of the parking trajectories obtained after convergence of both DDP, starting from ... | comparison identity and matched condition | p. 6 (Figure/Table caption) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| no ablation sentence selected | not reported; proposed stress test only | verify ablation section |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| Finally, Section IV describes the results, illustrating the usefulness of our approach. | However, despite some recent work in this direction [34], direct feed-forward current control is not yet a functional option, while the lack of joint ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (IV. RESULTS), p. 5 (IV. RESULTS) |
| Primary metric/result | 3 compares the results obtained with the two solvers. | numeric claim only at cited anchor | p. 5 (IV. RESULTS) |

- Numeric sentences retained from the body:
- **p. 1 / Abstract - extractive body cue:** We apply our algorithm to three simulated problems, including the 36-DoF HRP-2 robot.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| no explicit failure cue selected | unreported; domain stress test remains open | verify Discussion/Conclusion |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Differential Dynamic Programming (DDP) is an indirect method which optimizes only over the unconstrained control-space and is therefore fast enough to allow real-time control ... | p. 1 (Abstract) |
| Quadratic Approximation DDP involves iterating a forward pass (or rollout) which integrates (1) for a given U, followed by a backward pass which compute ... | p. 2 (II. DIFFERENTIAL DYNAMIC PROGRAMMING) |
| This decomposition is used to compute the optimal feedback gain Kf = -Quu,fQux. | p. 4 (III. CONTROL LIMITS) |
| Since δx is not known during the backward pass, the QP needs to compute both the feedfoward and feedback gains k and K. | p. 4 (III. CONTROL LIMITS) |
| (13f) The "parking" task is encoded as a final-cost on the distance of the last state from (0,0,0,0), i.e. at the plane origin, facing ... | p. 5 (IV. RESULTS) |
| 0 500 -4 -2 0 2 4 6 states 0 500 -2 -1.5 -1 -0.5 0 0.5 1 1.5 2 squashing function controls 0 ... | p. 6 (IV. RESULTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- explicit limitation/failure sentence not recovered

- **PDF anchors reviewed:** datasets p. 4 (IV. RESULTS), p. 5 (IV. RESULTS), p. 6 (IV. RESULTS), p. 6 (IV. RESULTS), p. 4 (IV. RESULTS), p. 5 (IV. RESULTS), metrics p. 4 (IV. RESULTS), p. 4 (IV. RESULTS), p. 5 (IV. RESULTS), p. 5 (IV. RESULTS), p. 6 (IV. RESULTS), baselines p. 4 (IV. RESULTS), p. 4 (IV. RESULTS), p. 5 (IV. RESULTS), p. 6 (Figure/Table caption), results p. 6 (IV. RESULTS), p. 5 (IV. RESULTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
