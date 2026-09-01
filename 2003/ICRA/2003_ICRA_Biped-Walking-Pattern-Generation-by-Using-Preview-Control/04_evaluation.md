# Evaluation - Biped Walking Pattern Generation by using Preview Control of Zero-Moment Point

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1109/ROBOT.2003.1241826; PDF retrieval source: https://doi.org/10.1109/ROBOT.2003.1241826. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 6 (Figure/Table caption), p. 4 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction)): Figure 11: Modified ZMP of multibody model These information are stored to the buffer memory and loaded to use after delay time of T ∗NL. By this way, we can ...

## Evaluation Body Digest

- **p. 3 / 1 Introduction - extractive body cue:** ZMP τ x x cz xp m O Figure 3: A cart-table model 3 Walking pattern generation for given ZMP 3.1 Pattern generation as an ...
- **p. 2 / 1 Introduction - extractive body cue:** For the 3D-LIPM with the horizontal constraint (kx = ky = 0), we can easily calculate the zeromoment point (ZMP), which is widely used in ...
- **p. 2 / 1 Introduction - extractive body cue:** 2 Dynamic Models of Biped Robot 2.1 3D Linear Inverted Pendulum Mode and Zero-moment point When we apply a constraint control to an inverted pendulum ...
- **p. 4 / 1 Introduction - extractive body cue:** CoM of a robot that walks one step forward dynamically.
- **p. 4 / 1 Introduction - extractive body cue:** The robot supports its body by hind-leg from 0s to 1.5s, and has support exchange at 1.5s followed by the foreleg support until 3.0s.
- **p. 5 / 1 Introduction - extractive body cue:** HRP-2P is a humanoid robot of 154cm height and weighs 58kg developed in Humanoid Robotics Project (HRP) of METI [21].
- **p. 5 / 1 Introduction - extractive body cue:** 3.4 Pattern generation for multibody model The walking pattern is calculated by solving an inverse kinematics such that the CoM of the robot follows the ...
- **p. 3 / 1 Introduction - extractive body cue:** Then the inverse FFT returns the resulted CoM trajectory into time domain.

## Evaluation Type and Scope

- **Evaluation type:** `SYSTEM / EVALUATION SCOPE UNRESOLVED`.
- **Target system/task:** high-DoF humanoid whole-body dynamics와 contacts.
- **Input boundary:** proprioception, reference pose/motion, visual or language command.
- **Output/decision under evaluation:** joint/whole-body action, motion target 또는 task trajectory.
- **Primary target:** tracking, balance, skill/task success와 recovery.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| Figure/Table caption | SYSTEM / EVALUATION SCOPE UNRESOLVED | Figure 11: Modified ZMP of multibody model These information are stored to the buffer memory and loaded to use after delay time of T ... | p. 6 (Figure/Table caption) |
| 1 Introduction | SYSTEM / EVALUATION SCOPE UNRESOLVED | We can see a smooth trajectory of CoM (dashed line) is generated and the resulted ZMP (bold line) follows the reference (thin line) with ... | p. 4 (1 Introduction) |
| 1 Introduction | SYSTEM / EVALUATION SCOPE UNRESOLVED | When the ZMP reference can be previewed for NL step future at every sampling time, the optimal controller which minimizes the performance index (14) ... | p. 4 (1 Introduction) |
| 1 Introduction | SYSTEM / EVALUATION SCOPE UNRESOLVED | It should be noted that even ZMP tracking performance is poor, the system still remains stable thanks to the term of the state feedback. | p. 5 (1 Introduction) |

## Dataset / Benchmark Role

- **p. 3 / 1 Introduction - extractive body cue:** ZMP τ x x cz xp m O Figure 3: A cart-table model 3 Walking pattern generation for given ZMP 3.1 Pattern generation as an ...
- **p. 2 / 1 Introduction - extractive body cue:** For the 3D-LIPM with the horizontal constraint (kx = ky = 0), we can easily calculate the zeromoment point (ZMP), which is widely used in ...
- **p. 2 / 1 Introduction - extractive body cue:** 2 Dynamic Models of Biped Robot 2.1 3D Linear Inverted Pendulum Mode and Zero-moment point When we apply a constraint control to an inverted pendulum ...
- **p. 4 / 1 Introduction - extractive body cue:** CoM of a robot that walks one step forward dynamically.
- **p. 4 / 1 Introduction - extractive body cue:** The robot supports its body by hind-leg from 0s to 1.5s, and has support exchange at 1.5s followed by the foreleg support until 3.0s.
- **p. 5 / 1 Introduction - extractive body cue:** HRP-2P is a humanoid robot of 154cm height and weighs 58kg developed in Humanoid Robotics Project (HRP) of METI [21].
- **p. 5 / 1 Introduction - extractive body cue:** 3.4 Pattern generation for multibody model The walking pattern is calculated by solving an inverse kinematics such that the CoM of the robot follows the ...
- **p. 3 / 1 Introduction - extractive body cue:** Then the inverse FFT returns the resulted CoM trajectory into time domain.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- **p. 1 / Figure/Table caption - extractive body cue:** Figure 1: Walking on randomly placed stepping-stones Proceedings of the 2003 IEEE International Conference on Robotics & Automation Taipei, Taiwan, September 14-19, 2003 0-7803-7736-2/03/$17.00 ©2003 ...
- **p. 2 / Figure/Table caption - extractive body cue:** Figure 2: A pendulum under constraint where (px, py) is the location of the ZMP on the floor. By substituting Eqs. (5) to the 3D-LIPM ...
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 3: A cart-table model 3 Walking pattern generation for given ZMP 3.1 Pattern generation as
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 4: Pattern generation as ZMP tracking control 0 0.5 1 1.5 2 2.5 -0.05
- **p. 3 / Figure/Table caption - extractive body cue:** Figure 5: ZMP and CoM trajectory interesting feature of this problem as follows. Figure 5 illustrates the ideal trajectories of the ZMP and the 1622
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 6: Preview controller gain Gp (T = 5[ms], zc = 0.814[m], Qe = 1.0, Qx = 0, R = 1.0 × 10-6) Figure 7 ...
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 7: Body trajectory obtained by preview con- trol, previewing period T ∗NL = 1.6(s) 0 1 2 3 4 5
- **p. 5 / Figure/Table caption - extractive body cue:** Figure 8: With shorter previewing period T ∗NL = 0.8(s) follow the reference (thin line) well. We observe un- dershooting in the sagittal motion and ...

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | ZMP τ x x cz xp m O Figure 3: A cart-table model 3 Walking pattern generation for given ZMP 3.1 Pattern generation as ... | embodiment, simulator version and control stack | p. 3 (1 Introduction), p. 2 (1 Introduction) |
| Task/environment | For the 3D-LIPM with the horizontal constraint (kx = ky = 0), we can easily calculate the zeromoment point (ZMP), which is widely used ... | reset, timeout, object/scene variation | p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Observation/sensor | proprioception, reference pose/motion, visual or language command | calibration, preprocessing, privileged input | p. 4 (1 Introduction), p. 2 (1 Introduction) |
| Output/decision | joint/whole-body action, motion target 또는 task trajectory | action frame, controller and termination | p. 3 (1 Introduction), p. 4 (1 Introduction) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| We can see a smooth trajectory of CoM (dashed line) is generated and the resulted ZMP (bold line) follows the reference (thin line) with ... | definition/direction/unit from same section | p. 4 (1 Introduction) |
| With the given reference of ZMP pref(k), the performance index is specified as J = ∞  i=k {Qee(i)2+∆xT (i)Qx∆x(i)+R∆u2(i)}, (14) where e(i) ≡p(i)-pref(i) ... | definition/direction/unit from same section | p. 4 (1 Introduction) |
| To fix the ZMP error, again we can use the preview control. | definition/direction/unit from same section | p. 5 (1 Introduction) |
| The maximum ZMP error was 2.3cm in x-direction and 1.6cm in y-direction. | definition/direction/unit from same section | p. 5 (1 Introduction) |
| However, if the cart accelerates with a proper rate, the table can keep upright for a while. | definition/direction/unit from same section | p. 2 (1 Introduction) |
| Then the inverse FFT returns the resulted CoM trajectory into time domain. | definition/direction/unit from same section | p. 3 (1 Introduction) |
| The system generates the CoM trajectory such that the resulted ZMP follows the given reference. | definition/direction/unit from same section | p. 3 (1 Introduction) |

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
| In this paper we introduce a novel walking pattern generation that allows arbitrary foot placements as a mixture of the ZMP based and the ... | Figure 11: Modified ZMP of multibody model These information are stored to the buffer memory and loaded to use after delay time of T ... | PDF body cue; verify exact table/figure and matched conditions | p. 6 (Figure/Table caption), p. 4 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction) |
| Primary metric/result | We can see a smooth trajectory of CoM (dashed line) is generated and the resulted ZMP (bold line) follows the reference (thin line) with ... | numeric claim only at cited anchor | p. 4 (1 Introduction) |

- Numeric sentences retained from the body:
- **p. 3 / 1 Introduction - extractive body cue:** However, we must consider an xu ZMP reference Servo Controller Dynamic ZMP equation (12) p ref p x + - p ZMP CoM Figure 4: ...
- **p. 4 / 1 Introduction - extractive body cue:** The robot supports its body by hind-leg from 0s to 1.5s, and has support exchange at 1.5s followed by the foreleg support until 3.0s.
- **p. 4 / 1 Introduction - extractive body cue:** Thus the reference ZMP should have a step change at 1.5s and obviously the CoM must start moving before this.
- **p. 4 / 1 Introduction - extractive body cue:** 0 0.5 1 1.5 2 0 500 1000 1500 time [s] preview gain Figure 6: Preview controller gain Gp (T = 5[ms], zc = 0.814[m], ...
- **p. 5 / 1 Introduction - extractive body cue:** CoM Figure 7: Body trajectory obtained by preview control, previewing period T ∗NL = 1.6(s) 0 1 2 3 4 5 6 7 0 0.5 ...
- **p. 5 / 1 Introduction - extractive body cue:** 0 2 4 6 8 0 0.5 1 x [m] ZMP multibody ZMP cart-table CoM 0 2 4 6 8 -0.1 -0.05 0 0.05 0.1 ...

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 0 2 4 6 8 0 0.5 1 x [m] ZMP multibody ZMP cart-table CoM 0 2 4 6 8 -0.1 -0.05 0 0.05 ... | p. 5 (1 Introduction) |
| body limitation/failure cue | In this case, the resulted ZMP (bold line) does not 1623 | p. 4 (1 Introduction) |
| body limitation/failure cue | We see the controller does not need the information of far future because the magnitude of the preview gain Gp becomes very small in ... | p. 4 (1 Introduction) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| The generated walking pattern corresponds to the walking of three steps forward. | p. 4 (1 Introduction) |
| As the simpler implementation, we can also use the center of the pelvis link since it approximates the motion of the CoM. | p. 5 (1 Introduction) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 5 / 1 Introduction - extractive body cue:** 0 2 4 6 8 0 0.5 1 x [m] ZMP multibody ZMP cart-table CoM 0 2 4 6 8 -0.1 -0.05 0 0.05 0.1 ...
- **p. 4 / 1 Introduction - extractive body cue:** In this case, the resulted ZMP (bold line) does not 1623
- **p. 4 / 1 Introduction - extractive body cue:** We see the controller does not need the information of far future because the magnitude of the preview gain Gp becomes very small in the ...

- **PDF anchors reviewed:** datasets p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 4 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), metrics p. 4 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction), p. 5 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), baselines 본문 anchor 없음, results p. 6 (Figure/Table caption), p. 4 (1 Introduction), p. 4 (1 Introduction), p. 5 (1 Introduction).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
