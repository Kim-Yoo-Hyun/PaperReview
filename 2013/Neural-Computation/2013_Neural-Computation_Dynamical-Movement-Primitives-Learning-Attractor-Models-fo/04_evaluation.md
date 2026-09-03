# Evaluation - Dynamical Movement Primitives: Learning Attractor Models for Motor Behaviors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (47 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://is.mpg.de/ics/publications/ijspeert_nc_2013; PDF retrieval source: https://www.pure.ed.ac.uk/ws/portalfiles/portal/7874487/NECO_a_00393.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 29 (3 Evaluations), p. 30 (3 Evaluations), p. 22 (3 Evaluations), p. 9 (Figure/Table caption), p. 33 (Figure/Table caption)): Within two beats (the time needed to extract the frequency from the acoustic signal), perfect synchronization and phase locking is achieved with a 0.15 Hz signal-very rapid synchronization.

## Evaluation Body Digest

- **p. 22 / 3 Evaluations - extractive body cue:** In the next sections, we present and review several experimental evaluations of applying our approach to learning attractor systems in the domain of motor control, ...
- **p. 22 / 3 Evaluations - extractive body cue:** In robotics, one of the most common classic methods to represent movement plans is by means of third-order or fifth-order splines, which could be equally ...
- **p. 24 / 3 Evaluations - extractive body cue:** A state-space mixture model for our humanoid robot above would require a 60-dimension state space and thus would create computational and numerical problems.
- **p. 26 / 3 Evaluations - extractive body cue:** In the second row, the (green) target is suddenly moved to the right while the robot has already begun moving.
- **p. 26 / 3 Evaluations - extractive body cue:** The third row of images demonstrates an avoidance behavior based on equation 3.2, when the blue ball comes too close to the robot's movement.
- **p. 27 / 3 Evaluations - extractive body cue:** Dynamical Movement Primitives 353 Obstacle Avoidance Movement Online Adaptation to changing target Orignal Figure 9: Sarcos slave robot placing a red cup on a green ...
- **p. 29 / 3 Evaluations - extractive body cue:** In the beginning, the robots started from immobility (ω = 0).
- **p. 29 / 3 Evaluations - extractive body cue:** Dynamical Movement Primitives 355 to which the slow drumbeat of the robot was to synchronize.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.
- **Target system/task:** robot mechanism의 state와 task-space dynamics.
- **Input boundary:** joint/task state, reference와 sensor feedback.
- **Output/decision under evaluation:** torque, force, velocity 또는 position command.
- **Primary target:** tracking, stability, constraint satisfaction과 contact behavior.
- **Detected evaluation headings:** 3 Evaluations (p. 22).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 3 Evaluations | EMPIRICAL / SIMULATION | Within two beats (the time needed to extract the frequency from the acoustic signal), perfect synchronization and phase locking is achieved with a 0.15 ... | p. 29 (3 Evaluations) |
| 3 Evaluations | EMPIRICAL / SIMULATION | It should be noted that many other coupling terms could be created to achieve similar behavior and that our realization is just a simple ... | p. 30 (3 Evaluations) |
| 3 Evaluations | EMPIRICAL / SIMULATION | For instance, Wada and Kawato (2004) presented an elegant algorithm that recursively fits a demonstrated trajectory with a growing number of spline nodes until ... | p. 22 (3 Evaluations) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Figure 2: Vector plot for a 2D trajectory where y1 (top left) fits the trajectory of Figure 1 and y2 (bottom left) fits a ... | p. 9 (Figure/Table caption) |
| Figure/Table caption | EMPIRICAL / SIMULATION | Figure 13: Correlation between the parameter vectors of different instantiations of the Graffiti characters (5 instances of each of the 26 alphabet characters). A ... | p. 33 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 22 / 3 Evaluations - extractive body cue:** In the next sections, we present and review several experimental evaluations of applying our approach to learning attractor systems in the domain of motor control, ...
- **p. 22 / 3 Evaluations - extractive body cue:** In robotics, one of the most common classic methods to represent movement plans is by means of third-order or fifth-order splines, which could be equally ...
- **p. 24 / 3 Evaluations - extractive body cue:** A state-space mixture model for our humanoid robot above would require a 60-dimension state space and thus would create computational and numerical problems.
- **p. 26 / 3 Evaluations - extractive body cue:** In the second row, the (green) target is suddenly moved to the right while the robot has already begun moving.
- **p. 26 / 3 Evaluations - extractive body cue:** The third row of images demonstrates an avoidance behavior based on equation 3.2, when the blue ball comes too close to the robot's movement.
- **p. 27 / 3 Evaluations - extractive body cue:** Dynamical Movement Primitives 353 Obstacle Avoidance Movement Online Adaptation to changing target Orignal Figure 9: Sarcos slave robot placing a red cup on a green ...
- **p. 29 / 3 Evaluations - extractive body cue:** In the beginning, the robots started from immobility (ω = 0).
- **p. 29 / 3 Evaluations - extractive body cue:** Dynamical Movement Primitives 355 to which the slow drumbeat of the robot was to synchronize.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 8 / Figure/Table caption - extractive body cue:** Figure 1: Exemplary time evolution of the discrete dynamical system. The pa- rameters wi have been adjusted to fit a fifth-order polynomial trajectory between start ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 2: Vector plot for a 2D trajectory where y1 (top left) fits the trajectory of Figure 1 and y2 (bottom left) fits a minimum ...
- **p. 11 / Figure/Table caption - extractive body cue:** Figure 3: Exemplary time evolution of the rhythmic dynamical system (limit cycle behavior). The parameters wi have been adjusted to fit a trajectory ydemo(t) = ...
- **p. 13 / Figure/Table caption - extractive body cue:** Figure 4: Illustration of invariance properties in the discrete dynamical systems, using the example from Figure 1. (a) The goal position is varied from -1 ...
- **p. 14 / Figure/Table caption - extractive body cue:** Figure 5: Illustration of the significance of the invariance properties, exempli- fied in a two-dimensional discrete dynamical system to draw a cursive letter a. In ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 6: Conceptual illustration of a multi-DOF dynamical system. The canon- ical system is shared, while each DOF has its own nonlinear function and trans- ...
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 7: Graphical sketch of the design principle of our approach to learnable dynamical systems. movement, it is easily possible to choose a second-order system ...
- **p. 23 / Figure/Table caption - extractive body cue:** Table 1: Summary of the Equations for Our Discrete and Rhythmic Model Equations. Discrete Rhythmic Transformation system: Transformation system: τ ˙z = αz(βz(g -y) -z) ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | In the next sections, we present and review several experimental evaluations of applying our approach to learning attractor systems in the domain of motor ... | embodiment, simulator version and control stack | p. 22 (3 Evaluations), p. 22 (3 Evaluations) |
| Task/environment | In robotics, one of the most common classic methods to represent movement plans is by means of third-order or fifth-order splines, which could be ... | reset, timeout, object/scene variation | p. 22 (3 Evaluations), p. 24 (3 Evaluations) |
| Observation/sensor | joint/task state, reference와 sensor feedback | calibration, preprocessing, privileged input | p. 6 (2 A Learnable Nonlinear Attractor Systems), p. 6 (2 A Learnable Nonlinear Attractor Systems) |
| Output/decision | torque, force, velocity 또는 position command | action frame, controller and termination | p. 8 (2 A Learnable Nonlinear Attractor Systems), p. 8 (2 A Learnable Nonlinear Attractor Systems) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| For instance, Wada and Kawato (2004) presented an elegant algorithm that recursively fits a demonstrated trajectory with a growing number of spline nodes until ... | definition/direction/unit from same section | p. 22 (3 Evaluations) |
| (3.11) The first equation is just a low-pass filter of the tracking error e = ya -y. | definition/direction/unit from same section | p. 29 (3 Evaluations) |
| This error is used as an additive coupling term in the transformation system, which hinders the state y to evolve too far away from ... | definition/direction/unit from same section | p. 29 (3 Evaluations) |
| This modification of the time constant slows the temporal evolution of the dynamics in case of a significant tracking error. | definition/direction/unit from same section | p. 30 (3 Evaluations) |
| Without the coupling terms, y would already have evolved all the way to the goal position, and the error between ya and y would ... | definition/direction/unit from same section | p. 30 (3 Evaluations) |
| Figure 13: Correlation between the parameter vectors of different instantiations of the Graffiti characters (5 instances of each of the 26 alphabet characters). A ... | definition/direction/unit from same section | p. 33 (Figure/Table caption) |
| The evaluations are intended to demonstrate the properties of our methodology, but also the domain-specific choices that need to be made. | definition/direction/unit from same section | p. 22 (3 Evaluations) |
| The parameters wi are fitted to a demonstrated trajectory using locally weighted learning. | definition/direction/unit from same section | p. 23 (3 Evaluations) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The design parameters of the rhythmic system are g, the baseline of the oscillation; τ, the period divided by 2π; and r, the amplitude ... | comparison identity and matched condition | p. 23 (3 Evaluations) |
| Figure 13: Correlation between the parameter vectors of different instantiations of the Graffiti characters (5 instances of each of the 26 alphabet characters). A ... | comparison identity and matched condition | p. 33 (Figure/Table caption) |
| Figure 2: Vector plot for a 2D trajectory where y1 (top left) fits the trajectory of Figure 1 and y2 (bottom left) fits a ... | comparison identity and matched condition | p. 9 (Figure/Table caption) |
| Those online modulations are among the most important properties offered by a dynamical systems approach, and these properties cannot easily be replicated without the ... | comparison identity and matched condition | p. 24 (3 Evaluations) |
| By modulating the canonical system, one can influence the temporal evolution of our dynamical systems without affecting | comparison identity and matched condition | p. 26 (3 Evaluations) |
| Without coupling terms, the dynamical system would just continue its time evolution, regardless of what happens to the point mass. | comparison identity and matched condition | p. 29 (3 Evaluations) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| Those online modulations are among the most important properties offered by a dynamical systems approach, and these properties cannot easily be replicated without the ... | component/input/data sensitivity | p. 24 (3 Evaluations) |
| By modulating the canonical system, one can influence the temporal evolution of our dynamical systems without affecting | component/input/data sensitivity | p. 26 (3 Evaluations) |
| Without coupling terms, the dynamical system would just continue its time evolution, regardless of what happens to the point mass. | component/input/data sensitivity | p. 29 (3 Evaluations) |
| Without the coupling terms, y would already have evolved all the way to the goal position, and the error between ya and y would ... | component/input/data sensitivity | p. 30 (3 Evaluations) |
| Essentially the perturbation simply delays the time evolution of the dynamical system without any large motor commands leading to possible harm. system, that is, ... | component/input/data sensitivity | p. 30 (3 Evaluations) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In this letter, we propose a generic modeling approach to generate multidimensional systems of weakly nonlinear differential equations to 1With low-dimensional, we refer to ... | Within two beats (the time needed to extract the frequency from the acoustic signal), perfect synchronization and phase locking is achieved with a 0.15 ... | PDF body cue; verify exact table/figure and matched conditions | p. 29 (3 Evaluations), p. 30 (3 Evaluations), p. 22 (3 Evaluations), p. 9 (Figure/Table caption), p. 33 (Figure/Table caption) |
| Primary metric/result | It should be noted that many other coupling terms could be created to achieve similar behavior and that our realization is just a simple ... | numeric claim only at cited anchor | p. 30 (3 Evaluations) |

- Numeric sentences retained from the body:
- **p. 22 / 3 Evaluations - extractive body cue:** (2003) and Ijspeert, Nakanishi, and Schaal (2002a) demonsrated imitation learning with a 30 degrees-of-freedom (DOFs) humanoid robot (Atkeson et al., 2000) for performing a tennis ...
- **p. 25 / 3 Evaluations - extractive body cue:** We start with a 3 degree-of-freedom (DOF) discrete movement system that models point-to-point reaching in a 3D Cartesian space.
- **p. 25 / 3 Evaluations - extractive body cue:** The vector r is the vector that is perpendicular to the plane spanned by ˙y and (o -y), and serves to define a rotation matrix ...
- **p. 29 / 3 Evaluations - extractive body cue:** Within two beats (the time needed to extract the frequency from the acoustic signal), perfect synchronization and phase locking is achieved with a 0.15 Hz ...
- **p. 29 / 3 Evaluations - extractive body cue:** Afterward, we had the external metronome pace increase frequency slowly to 0.5 Hz to demonstrate the continuous adaptation ability of the oscillator.
- **p. 29 / 3 Evaluations - extractive body cue:** At time t = 0.35 s, the point mass is suddenly blocked from any further motion and released again at t = 0.9 s.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Those online modulations are among the most important properties offered by a dynamical systems approach, and these properties cannot easily be replicated without the ... | p. 24 (3 Evaluations) |
| body limitation/failure cue | Trajectories starting at points where the direct line to the goal does not intersect with the obstacle are only minimally curved around the obstacle, ... | p. 26 (3 Evaluations) |
| body limitation/failure cue | Figure 8: Illustration of obstacle avoidance with a coupling term. The obstacle is the large (red) sphere in the center of the plot. Various ... | p. 26 (Figure/Table caption) |
| body limitation/failure cue | In this section, we illustrate how both temporal and spatial coupling can be used together to model disturbance rejection, a property that is inherent ... | p. 29 (3 Evaluations) |
| body limitation/failure cue | Thus, for instance, a variation at the end of a movement will not affect the parameter values at the beginning of a movement, which ... | p. 31 (3 Evaluations) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Using imitation learning, a placing behavior of a cup on a target was coded in a discrete dynamical system for a 3D end effector ... | p. 26 (3 Evaluations) |
| The 26 letters of the Graffiti alphabet used in hand-held computers were chosen. | p. 31 (3 Evaluations) |
| Thus, modeling is often left to the intuition and the trial-and-error patience of the researchers. | p. 3 (1 Introduction) |
| We evaluate our approach in the domain of motor control for robotics, where desired kinematic motor behaviors will be coded in attractor landscapes and ... | p. 4 (1 Introduction) |
| Matlab code is provided as supplemental material to allow readers to explore properties of the system.2 Early versions of the dynamical system presented in ... | p. 4 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 24 / 3 Evaluations - extractive body cue:** Those online modulations are among the most important properties offered by a dynamical systems approach, and these properties cannot easily be replicated without the attractor ...
- **p. 26 / 3 Evaluations - extractive body cue:** Trajectories starting at points where the direct line to the goal does not intersect with the obstacle are only minimally curved around the obstacle, while ...
- **p. 26 / Figure/Table caption - extractive body cue:** Figure 8: Illustration of obstacle avoidance with a coupling term. The obstacle is the large (red) sphere in the center of the plot. Various trajectories ...
- **p. 29 / 3 Evaluations - extractive body cue:** In this section, we illustrate how both temporal and spatial coupling can be used together to model disturbance rejection, a property that is inherent in ...
- **p. 31 / 3 Evaluations - extractive body cue:** Thus, for instance, a variation at the end of a movement will not affect the parameter values at the beginning of a movement, which creates ...

- **Evidence anchors reviewed:** datasets p. 22 (3 Evaluations), p. 22 (3 Evaluations), p. 24 (3 Evaluations), p. 26 (3 Evaluations), p. 26 (3 Evaluations), p. 27 (3 Evaluations), metrics p. 22 (3 Evaluations), p. 29 (3 Evaluations), p. 29 (3 Evaluations), p. 30 (3 Evaluations), p. 30 (3 Evaluations), p. 33 (Figure/Table caption), baselines p. 23 (3 Evaluations), p. 33 (Figure/Table caption), p. 9 (Figure/Table caption), p. 24 (3 Evaluations), p. 26 (3 Evaluations), p. 29 (3 Evaluations), results p. 29 (3 Evaluations), p. 30 (3 Evaluations), p. 22 (3 Evaluations), p. 9 (Figure/Table caption), p. 33 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
