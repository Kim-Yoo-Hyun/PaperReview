# Evaluation - Dynamic Safety in Complex Environments: Synthesizing Safety Filters with Poisson's Equation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p137.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p137.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 8 (B. Hardware Experiments), p. 8 (B. Hardware Experiments)): For dynamic environments, we improve the ‘computational speed of our PDE solver by warm-starting each PDE solution with the previous safety function, producing

## Evaluation Body Digest

- **p. 8 / B. Hardware Experiments - extractive body cue:** First, we perceive and segment the environment using fixed RGB camera and the Meta SAM2 [49] segmentation algorithm, Next, we generate a 2D occupancy map, ...
- **p. 8 / B. Hardware Experiments - extractive body cue:** Robot states are estimated by an OptiTrack motion capture system,
- **p. 8 / B. Hardware Experiments - extractive body cue:** ‘To demonstrate the practical performance of our proposed algorithm in synthesizing safe sets, we applied it to several collision avoidance scenarios using Unitree's Go2 quadruped ...
- **p. 8 / B. Hardware Experiments - extractive body cue:** For dynamic environments, we improve the ‘computational speed of our PDE solver by warm-starting each PDE solution with the previous safety function, producing
- **p. 8 / B. Hardware Experiments - extractive body cue:** The results corresponding to this experiment are depicted in Fig 5,
- **p. 9 / 2 Nomina (Orange) & Safe (Bie) Inputs - extractive body cue:** ‘A fundamental limitation of the proposed algorithm (and a limitation of all non-predictive safety filters) is that such safety-critical controllers may introduce undesired equilibria, These ...
- **p. 7 / VI. DEMONSTRATIONS - extractive body cue:** Simulations: Double Integrator We define a 2D occupancy map defined by an open, bounded and connected domain © where J® characterizes obstacle surfaces. and consider ...
- **p. 8 / B. Hardware Experiments - extractive body cue:** From these results, itis clear thatthe Poisson safety funetion enabled collision avoidance without hindering the nominal objective.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** B. Hardware Experiments (p. 8).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| B. Hardware Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | For dynamic environments, we improve the ‘computational speed of our PDE solver by warm-starting each PDE solution with the previous safety function, producing | p. 8 (B. Hardware Experiments) |
| B. Hardware Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | The results corresponding to this experiment are depicted in Fig 5, | p. 8 (B. Hardware Experiments) |

## Dataset / Benchmark Role

- **p. 8 / B. Hardware Experiments - extractive body cue:** First, we perceive and segment the environment using fixed RGB camera and the Meta SAM2 [49] segmentation algorithm, Next, we generate a 2D occupancy map, ...
- **p. 8 / B. Hardware Experiments - extractive body cue:** Robot states are estimated by an OptiTrack motion capture system,

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1: Safe set synthesis from perception data via Poisson's equation Hardware experimental footage: hitps//youtu.be/TBRUkAJGixL,
- **p. 5 / Figure/Table caption - extractive body cue:** Fig. 3: Smooth guidance field generation via Laplace' equation (26) [left] Boundary conditions ¥ = bi encoding the desired negative ux fon obstacle surfaces: and ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 4: Double integrator simulations using safety filers synthesized from: (el) Signed Distance Function (40); and {middle and right) the Poisson Safety Function, constructed with ...
- **p. 13 / Figure/Table caption - extractive body cue:** Fig. 7: Interior sphere condition for [left] smooth boundary and [right] Lipschitz boundary.

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | First, we perceive and segment the environment using fixed RGB camera and the Meta SAM2 [49] segmentation algorithm, Next, we generate a 2D occupancy ... | embodiment, simulator version and control stack | p. 8 (B. Hardware Experiments), p. 8 (B. Hardware Experiments) |
| Task/environment | Robot states are estimated by an OptiTrack motion capture system, | reset, timeout, object/scene variation | p. 8 (B. Hardware Experiments) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 6 (B. Indirect Assignment - Variational Approach), p. 1 (1. IyrRopUCTION) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 2 (1. IyrRopUCTION), p. 3 (B. Ouputs and Relative Degree) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| ‘To demonstrate the practical performance of our proposed algorithm in synthesizing safe sets, we applied it to several collision avoidance scenarios using Unitree's Go2 ... | definition/direction/unit from same section | p. 8 (B. Hardware Experiments) |
| First, we perceive and segment the environment using fixed RGB camera and the Meta SAM2 [49] segmentation algorithm, Next, we generate a 2D occupancy ... | definition/direction/unit from same section | p. 8 (B. Hardware Experiments) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| In each ease, the nominal controller attempted to drive the system directly 10 the goal without safety considerations. | comparison identity and matched condition | p. 8 (B. Hardware Experiments) |
| From these results, itis clear thatthe Poisson safety funetion enabled collision avoidance without hindering the nominal objective. | comparison identity and matched condition | p. 8 (B. Hardware Experiments) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In each ease, the nominal controller attempted to drive the system directly 10 the goal without safety considerations. | component/input/data sensitivity | p. 8 (B. Hardware Experiments) |
| From these results, itis clear thatthe Poisson safety funetion enabled collision avoidance without hindering the nominal objective. | component/input/data sensitivity | p. 8 (B. Hardware Experiments) |
| Fig. 3: Smooth guidance field generation via Laplace' equation (26) [left] Boundary conditions ¥ = bi encoding the desired negative ux fon obstacle surfaces: ... | component/input/data sensitivity | p. 5 (Figure/Table caption) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| The main contributions are threefold: (I) we present a constructive way of generating safe sets for complex environments from perception data via Poisson's equation, ... | For dynamic environments, we improve the ‘computational speed of our PDE solver by warm-starting each PDE solution with the previous safety function, producing | PDF body cue; verify exact table/figure and matched conditions | p. 8 (B. Hardware Experiments), p. 8 (B. Hardware Experiments) |
| Primary metric/result | The results corresponding to this experiment are depicted in Fig 5, | numeric claim only at cited anchor | p. 8 (B. Hardware Experiments) |

- Numeric sentences retained from the body:
- **p. 8 / B. Hardware Experiments - extractive body cue:** After considering the entire processing chain, we update the Poisson safety function A online at approximately 10 Hz.
- **p. 6 / B. Indirect Assignment - Variational Approach - extractive body cue:** The terms n,,ny,r. represent the components of the outward unit normal vector fi = (Mg, ny, 7s) 9 > B® such that V(y) = W(y)A(y) ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | ‘A fundamental limitation of the proposed algorithm (and a limitation of all non-predictive safety filters) is that such safety-critical controllers may introduce undesired equilibria, ... | p. 9 (2 Nomina (Orange) & Safe (Bie) Inputs) |
| body limitation/failure cue | Simulations: Double Integrator We define a 2D occupancy map defined by an open, bounded and connected domain © where J® characterizes obstacle surfaces. and ... | p. 7 (VI. DEMONSTRATIONS) |
| body limitation/failure cue | From these results, itis clear thatthe Poisson safety funetion enabled collision avoidance without hindering the nominal objective. | p. 8 (B. Hardware Experiments) |
| body limitation/failure cue | ‘To demonstrate the practical performance of our proposed algorithm in synthesizing safe sets, we applied it to several collision avoidance scenarios using Unitree's Go2 ... | p. 8 (B. Hardware Experiments) |
| body limitation/failure cue | Examining the value of h during the experiment, it ean be ‘observed that the robot effectively employed its safety filter to avoid collisions. | p. 9 (2 Nomina (Orange) & Safe (Bie) Inputs) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| Another approach of constructing a forcing function is by designing a guidance vector field ¥ : % -> R°, which encodes the desired flux ... | p. 5 (B. Indirect Assignment - Variational Approach) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 9 / 2 Nomina (Orange) & Safe (Bie) Inputs - extractive body cue:** ‘A fundamental limitation of the proposed algorithm (and a limitation of all non-predictive safety filters) is that such safety-critical controllers may introduce undesired equilibria, These ...
- **p. 7 / VI. DEMONSTRATIONS - extractive body cue:** Simulations: Double Integrator We define a 2D occupancy map defined by an open, bounded and connected domain © where J® characterizes obstacle surfaces. and consider ...
- **p. 8 / B. Hardware Experiments - extractive body cue:** From these results, itis clear thatthe Poisson safety funetion enabled collision avoidance without hindering the nominal objective.
- **p. 8 / B. Hardware Experiments - extractive body cue:** ‘To demonstrate the practical performance of our proposed algorithm in synthesizing safe sets, we applied it to several collision avoidance scenarios using Unitree's Go2 quadruped ...
- **p. 9 / 2 Nomina (Orange) & Safe (Bie) Inputs - extractive body cue:** Examining the value of h during the experiment, it ean be ‘observed that the robot effectively employed its safety filter to avoid collisions.

- **Evidence anchors reviewed:** datasets p. 8 (B. Hardware Experiments), p. 8 (B. Hardware Experiments), metrics p. 8 (B. Hardware Experiments), p. 8 (B. Hardware Experiments), baselines p. 8 (B. Hardware Experiments), p. 8 (B. Hardware Experiments), results p. 8 (B. Hardware Experiments), p. 8 (B. Hardware Experiments).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
