# Evaluation - A Realtime Pattern Generator for Biped Walking

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/ROBOT.2002.1013335; PDF retrieval source: https://www.cs.cmu.edu/~cga/legs/kuff1e.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (4 Experiments), p. 6 (4 Experiments), p. 4 (Figure/Table caption)): From the experimental results, the effectiveness of the proposed realtime walk generation method was confirmed.

## Evaluation Body Digest

- **p. 5 / 4 Experiments - extractive body cue:** of realtime bipped walking 4.1 Biped robot HRP-2L The biped robot HRP-2L, which is the leg module for HRP-21, is used for the experiments.
- **p. 5 / 4 Experiments - extractive body cue:** 300 300 91 358 574 945 120 190 1412.9 Figure 9: Biped robot HRP-2L Its weight is 58.2 [kg] including 11.4 [kg] batteries and 22.6 ...
- **p. 6 / 4 Experiments - extractive body cue:** The realtime walk generation was tested on a 12 d.o.f. biped robot HRP-2L with the game pad interface, and a dynamically stable walk was successfully ...
- **p. 6 / 4 Experiments - extractive body cue:** Although we assume an ideal robot, which can step towards any direction at all time, in the former section, HRP-2L has the limit of joint ...
- **p. 6 / 4 Experiments - extractive body cue:** In order to reduce the error between the desired ZMP trajectory and the actual ZMP, the horizontal position of the torso is adjusted.
- **p. 5 / 4 Experiments - extractive body cue:** It ganerates the desired pose of both legs and ZMP according to a command from the input device server.
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 6: Two successive steps in the sagittal plane are illustrated. The body travels from B to D in the single-leg support phase, then moves ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: 3D Pendulum leg which is the distance between the origin and the point mass. Let (τr, τp, f) be the actuator torque and ...

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SOURCE-REPORTED EVALUATION`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** 4 Experiments (p. 5).

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | From the experimental results, the effectiveness of the proposed realtime walk generation method was confirmed. | p. 6 (4 Experiments) |
| 4 Experiments | EMPIRICAL / SOURCE-REPORTED EVALUATION | The realtime walk generation was tested on a 12 d.o.f. biped robot HRP-2L with the game pad interface, and a dynamically stable walk was ... | p. 6 (4 Experiments) |
| Figure/Table caption | EMPIRICAL / SOURCE-REPORTED EVALUATION | Figure 6: Two successive steps in the sagittal plane are illustrated. The body travels from B to D in the single-leg support phase, then ... | p. 4 (Figure/Table caption) |

## Dataset / Benchmark Role

- **p. 5 / 4 Experiments - extractive body cue:** of realtime bipped walking 4.1 Biped robot HRP-2L The biped robot HRP-2L, which is the leg module for HRP-21, is used for the experiments.
- **p. 5 / 4 Experiments - extractive body cue:** 300 300 91 358 574 945 120 190 1412.9 Figure 9: Biped robot HRP-2L Its weight is 58.2 [kg] including 11.4 [kg] batteries and 22.6 ...
- **p. 6 / 4 Experiments - extractive body cue:** The realtime walk generation was tested on a 12 d.o.f. biped robot HRP-2L with the game pad interface, and a dynamically stable walk was successfully ...
- **p. 6 / 4 Experiments - extractive body cue:** Although we assume an ideal robot, which can step towards any direction at all time, in the former section, HRP-2L has the limit of joint ...

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 2 / Figure/Table caption - extractive body cue:** Figure 1: 3D Pendulum leg which is the distance between the origin and the point mass. Let (τr, τp, f) be the actuator torque and ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 2: 3D Linear Inverted Pendulum Mode Eqs. (13) and (14) can be regarded as a repulsive force field for a unit mass. f = ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3: 3D-LIPM projected onto XY plane 3 3D walking pattern generation 3.1 Outline Figure 4 shows an example of a walking pattern based on ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 4: Walking pattern generated from the 3D- LIPM. A robot takes seven steps from left to right. Motion of the tip of the inverted ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 5: XY -position and velocity in a walk of the figure 4. The thick line shows x motion and the thin line shows y ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 6: Two successive steps in the sagittal plane are illustrated. The body travels from B to D in the single-leg support phase, then moves ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 7: Changing walking direction frame for the calculations after that. First, current body position and speed are converted, then the new foot place P4 ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 9: Biped robot HRP-2L Its weight is 58.2 [kg] including 11.4 [kg] batteries and 22.6 [kg] dummy weights corresponding to those of arms and ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | of realtime bipped walking 4.1 Biped robot HRP-2L The biped robot HRP-2L, which is the leg module for HRP-21, is used for the experiments. | embodiment, simulator version and control stack | p. 5 (4 Experiments), p. 5 (4 Experiments) |
| Task/environment | 300 300 91 358 574 945 120 190 1412.9 Figure 9: Biped robot HRP-2L Its weight is 58.2 [kg] including 11.4 [kg] batteries and ... | reset, timeout, object/scene variation | p. 5 (4 Experiments), p. 6 (4 Experiments) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 3 (1 Introduction), p. 1 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| In order to reduce the error between the desired ZMP trajectory and the actual ZMP, the horizontal position of the torso is adjusted. | definition/direction/unit from same section | p. 6 (4 Experiments) |
| It ganerates the desired pose of both legs and ZMP according to a command from the input device server. | definition/direction/unit from same section | p. 5 (4 Experiments) |
| The realtime walk generation was tested on a 12 d.o.f. biped robot HRP-2L with the game pad interface, and a dynamically stable walk was ... | definition/direction/unit from same section | p. 6 (4 Experiments) |
| Figure 6: Two successive steps in the sagittal plane are illustrated. The body travels from B to D in the single-leg support phase, then ... | definition/direction/unit from same section | p. 4 (Figure/Table caption) |
| Figure 1: 3D Pendulum leg which is the distance between the origin and the point mass. Let (τr, τp, f) be the actuator torque ... | definition/direction/unit from same section | p. 2 (Figure/Table caption) |
| Figure 4: Walking pattern generated from the 3D- LIPM. A robot takes seven steps from left to right. Motion of the tip of the ... | definition/direction/unit from same section | p. 3 (Figure/Table caption) |
| Figure 7: Changing walking direction frame for the calculations after that. First, current body position and speed are converted, then the new foot place ... | definition/direction/unit from same section | p. 5 (Figure/Table caption) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| no baseline sentence selected | not reported | verify comparison table |

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
| It allows a separate controller design for the sagittal (x-z) and the lateral (y-z) motions and simplifies a walking pattern generation a great deal. | From the experimental results, the effectiveness of the proposed realtime walk generation method was confirmed. | PDF body cue; verify exact table/figure and matched conditions | p. 6 (4 Experiments), p. 6 (4 Experiments), p. 4 (Figure/Table caption) |
| Primary metric/result | The realtime walk generation was tested on a 12 d.o.f. biped robot HRP-2L with the game pad interface, and a dynamically stable walk was ... | numeric claim only at cited anchor | p. 6 (4 Experiments) |

- Numeric sentences retained from the body:
- **p. 6 / 4 Experiments - extractive body cue:** Input Device Server Measured joint angles Control values Goal joint angles Desired pose and ZMP Request Input Device State Foothold, Rotational angle of reference frame ...
- **p. 6 / 4 Experiments - extractive body cue:** It went forward at first 3 steps, turned right from 4th step to 11th step, then went backward to the end of steps.
- **p. 3 / 1 Introduction - extractive body cue:** 0 0.05 0.1 0.15 0.2 0.25 0.3 -0.05 0 0.05 0.1 0.15 X [m] Y [m] Figure 4: Walking pattern generated from the 3DLIPM.
- **p. 4 / 1 Introduction - extractive body cue:** 0 0.5 1 1.5 2 2.5 3 3.5 4 -0.1 -0.05 0 0.05 0.1 x,y [m] 0 0.5 1 1.5 2 2.5 3 3.5 4 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Although we assume an ideal robot, which can step towards any direction at all time, in the former section, HRP-2L has the limit of ... | p. 6 (4 Experiments) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| HRP-2L took nineteen steps in the experiment. | p. 6 (4 Experiments) |
| It went forward at first 3 steps, turned right from 4th step to 11th step, then went backward to the end of steps. | p. 6 (4 Experiments) |
| A robot takes seven steps from left to right. | p. 3 (1 Introduction) |
| E F x z vf (1) = vi (2) vi (1) vf (2) xi (1) xf (1) xi (2) xf (2) d D' Figure ... | p. 4 (C D) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 6 / 4 Experiments - extractive body cue:** Although we assume an ideal robot, which can step towards any direction at all time, in the former section, HRP-2L has the limit of joint ...

- **Evidence anchors reviewed:** datasets p. 5 (4 Experiments), p. 5 (4 Experiments), p. 6 (4 Experiments), p. 6 (4 Experiments), metrics p. 6 (4 Experiments), p. 5 (4 Experiments), p. 6 (4 Experiments), p. 4 (Figure/Table caption), p. 2 (Figure/Table caption), p. 3 (Figure/Table caption), baselines 본문 anchor 없음, results p. 6 (4 Experiments), p. 6 (4 Experiments), p. 4 (Figure/Table caption).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
