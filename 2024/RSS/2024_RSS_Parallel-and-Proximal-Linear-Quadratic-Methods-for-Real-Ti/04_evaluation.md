# Evaluation - Parallel and Proximal Linear-Quadratic Methods for Real-Time Constrained Model-Predictive Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (17 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss20/p002.html; PDF retrieval source: https://www.roboticsproceedings.org/rss20/p002.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 9 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS)): It is the authors' aim to improve its efficiency in the future.

## Evaluation Body Digest

- **p. 9 / VIII. EXPERIMENTS - extractive body cue:** 1) TALOS locomotion benchmarks: We consider a wholebody trajectory optimization problem on a TALOS [47] humanoid robot with constrained 6D contacts.
- **p. 10 / VIII. EXPERIMENTS - extractive body cue:** C++ benchmarks of a trajectory optimization problem involving two forward steps with the whole-body model of the TALOS robot, with single support time Tss set ...
- **p. 10 / VIII. EXPERIMENTS - extractive body cue:** 2) Constrained NMPC on TALOS: In this subsection, we leverage our proximal solver to perform whole-body nonlinear MPC on the humanoid robot TALOS in simulation, ...
- **p. 9 / VIII. EXPERIMENTS - extractive body cue:** Nonlinear trajectory optimization Computation of robot dynamical quantities (joint acceleration, frame jacobians. . . ) is provided by the Pinocchio [10, 11] rigid-body dynamics library.
- **p. 8 / VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY - extractive body cue:** OPTIMIZER We now consider a nonlinear discrete-time trajectory optimization problem with implicit system dynamics: min x,u J(x,u) = N-1 ∑ t=0 ℓt(xt,ut)+ℓN(xN) (48a) s.t. x0 ...
- **p. 10 / VIII. EXPERIMENTS - extractive body cue:** Each instance is run 40 times on every solver to produce a mean and standard deviation.
- **p. 10 / VIII. EXPERIMENTS - extractive body cue:** Comparison of the performances of parallel and serial proximal algorithms on the TALOS walking MPC.
- **p. 9 / VIII. EXPERIMENTS - extractive body cue:** It is the authors' aim to improve its efficiency in the future.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY (p. 8); VIII. EXPERIMENTS (p. 9).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| VIII. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | It is the authors' aim to improve its efficiency in the future. | p. 9 (VIII. EXPERIMENTS) |
| VIII. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | Synthetic benchmark To assess the speedups our implementation of the parallel algorithm could achieve, we implemented a synthetic benchmark of problems with different horizons ... | p. 9 (VIII. EXPERIMENTS) |
| VIII. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | 2) Constrained NMPC on TALOS: In this subsection, we leverage our proximal solver to perform whole-body nonlinear MPC on the humanoid robot TALOS in ... | p. 10 (VIII. EXPERIMENTS) |
| VIII. EXPERIMENTS | EMPIRICAL / REAL-ROBOT OR HARDWARE | The timing results of this experiment are shown in fig. | p. 10 (VIII. EXPERIMENTS) |

## Dataset / Benchmark Role

- **p. 9 / VIII. EXPERIMENTS - extractive body cue:** 1) TALOS locomotion benchmarks: We consider a wholebody trajectory optimization problem on a TALOS [47] humanoid robot with constrained 6D contacts.
- **p. 10 / VIII. EXPERIMENTS - extractive body cue:** C++ benchmarks of a trajectory optimization problem involving two forward steps with the whole-body model of the TALOS robot, with single support time Tss set ...
- **p. 10 / VIII. EXPERIMENTS - extractive body cue:** 2) Constrained NMPC on TALOS: In this subsection, we leverage our proximal solver to perform whole-body nonlinear MPC on the humanoid robot TALOS in simulation, ...
- **p. 9 / VIII. EXPERIMENTS - extractive body cue:** Nonlinear trajectory optimization Computation of robot dynamical quantities (joint acceleration, frame jacobians. . . ) is provided by the Pinocchio [10, 11] rigid-body dynamics library.
- **p. 8 / VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY - extractive body cue:** OPTIMIZER We now consider a nonlinear discrete-time trajectory optimization problem with implicit system dynamics: min x,u J(x,u) = N-1 ∑ t=0 ℓt(xt,ut)+ℓN(xN) (48a) s.t. x0 ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 1. LQ problem with cyclical constraint x0 = x30 ,in one dimension. No other initial condition was provided for x0. 4https://github.com/Simple-Robotics/aligator/ 1.5 1.0 0.5 ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 3. Timings for a backward-forward sweep of the solver on a synthetic benchmark. 165 220 275 Horizon size of the problem 0
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 4. C++ benchmarks of a trajectory optimization problem involving two forward steps with the whole-body model of the TALOS robot, with single support time ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 5. Snapshot of a PyBullet [14] simulation featuring TALOS walking with pre-defined feet trajectories (blue rectangles). The Bullet simulation timestep is set to 1 ...
- **p. 10 / Figure/Table caption - extractive body cue:** Fig. 6. Comparison of the performances of parallel and serial proximal algorithms on the TALOS walking MPC. The histogram shows the distribution of time per ...
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 7. SOLO-12 walking on flat ground. • a high-level OCP solver runs on a powerful desktop, • a lower-level, high-frequency controller on a laptop ...
- **p. 17 / Figure/Table caption - extractive body cue:** Fig. 8. Theoretical speedup derived from the bounds, with varying problem horizon N and number of parallel legs/processors J. The problem dimensions correspond to the ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | 1) TALOS locomotion benchmarks: We consider a wholebody trajectory optimization problem on a TALOS [47] humanoid robot with constrained 6D contacts. | embodiment, simulator version and control stack | p. 9 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS) |
| Task/environment | C++ benchmarks of a trajectory optimization problem involving two forward steps with the whole-body model of the TALOS robot, with single support time Tss ... | reset, timeout, object/scene variation | p. 10 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 4 (III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM), p. 3 (III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 3 (III. RICCATI EQUATIONS FOR THE PROXIMAL LQ PROBLEM), p. 1 (I. INTRODUCTION) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Each instance is run 40 times on every solver to produce a mean and standard deviation. | definition/direction/unit from same section | p. 10 (VIII. EXPERIMENTS) |
| Comparison of the performances of parallel and serial proximal algorithms on the TALOS walking MPC. | definition/direction/unit from same section | p. 10 (VIII. EXPERIMENTS) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| 4, our proximal solver with various parallelization settings is compared against the feasibility-prone DDP from the CROCODDYL library [36]. | comparison identity and matched condition | p. 9 (VIII. EXPERIMENTS) |
| Comparison of the performances of parallel and serial proximal algorithms on the TALOS walking MPC. | comparison identity and matched condition | p. 10 (VIII. EXPERIMENTS) |

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
| We present this as a secondary contribution of this paper, which we have implemented and evaluated in the experimental section. | It is the authors' aim to improve its efficiency in the future. | PDF body cue; verify exact table/figure and matched conditions | p. 9 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS) |
| Primary metric/result | Synthetic benchmark To assess the speedups our implementation of the parallel algorithm could achieve, we implemented a synthetic benchmark of problems with different horizons ... | numeric claim only at cited anchor | p. 9 (VIII. EXPERIMENTS) |

- Numeric sentences retained from the body:
- **p. 9 / VIII. EXPERIMENTS - extractive body cue:** The problem is discretized using the semi-implicit Euler scheme with timestep ∆t = 10ms.
- **p. 10 / VIII. EXPERIMENTS - extractive body cue:** C++ benchmarks of a trajectory optimization problem involving two forward steps with the whole-body model of the TALOS robot, with single support time Tss set ...
- **p. 10 / VIII. EXPERIMENTS - extractive body cue:** The Bullet simulation timestep is set to 1 ms. we add equality constraints at the end of each flying phase to ensure that foot altitude ...
- **p. 10 / VIII. EXPERIMENTS - extractive body cue:** Horizon window is set to 0.5 s with a timestep of 10 ms for a total of N = 50 steps.
- **p. 10 / VIII. EXPERIMENTS - extractive body cue:** The horizon is set to 0.96 s, with a 12 ms timestep, resulting in a discrete-time horizon of N = 80.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | In our setting, the linear subproblem (47) does not have that same structure (such that our construction from section V cannot be iterated), however, ... | p. 9 (VII. DISCUSSION) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The TALOS benchmark and NMPC experiments were run on a Dell XPS laptop with an Intel i913900k CPU (8 P-cores and 16 E-cores). | p. 9 (VIII. EXPERIMENTS) |
| Our implementation will be open-sourced upon acceptance of the paper. | p. 8 (VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY) |
| It is then straightforward to adapt an implementation of [29] by replacing the proximal LQ solver by the parallel formulation. | p. 8 (VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY) |
| This implementation has been added to our optimal control framework ALIGATOR4. | p. 9 (VIII. EXPERIMENTS) |
| Horizon window is set to 0.5 s with a timestep of 10 ms for a total of N = 50 steps. | p. 10 (VIII. EXPERIMENTS) |
| Each instance is run 40 times on every solver to produce a mean and standard deviation. | p. 10 (VIII. EXPERIMENTS) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / VII. DISCUSSION - extractive body cue:** In our setting, the linear subproblem (47) does not have that same structure (such that our construction from section V cannot be iterated), however, it ...

- **Evidence anchors reviewed:** datasets p. 9 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 8 (VI. IMPLEMENTATION IN A NONLINEAR TRAJECTORY), metrics p. 10 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS), baselines p. 9 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS), results p. 9 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
