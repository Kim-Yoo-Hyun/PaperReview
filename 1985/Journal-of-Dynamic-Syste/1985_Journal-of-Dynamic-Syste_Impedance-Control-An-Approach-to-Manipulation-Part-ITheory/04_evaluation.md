# Evaluation - Impedance Control: An Approach to Manipulation: Part I—Theory

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1115/1.3140702; PDF retrieval source: https://doi.org/10.1115/1.3140702. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 5 (1 Y)): The separation of the controller action into a (vector) motion component and a impedance component (which has the properties of a tensor) can be achieved for a general class of ...

## Evaluation Body Digest

- **p. 2 / Front matter - extractive body cue:** This organization has been proposed as a general form of control and communication for man/machine systems [26]: it is commonly used for robots [2]; and ...
- **p. 2 / Front matter - extractive body cue:** A unified framework for considering the action of both hardware and software in the control of dynamic behavior can be obtained by making the reasonable ...
- **p. 3 / Front matter - extractive body cue:** The real-world phenomenon of stiction is typically represented by a dissipative element with a noninvertible relation between force and velocity.
- **p. 4 / Front matter - extractive body cue:** Thus a general strategy for controlling a manipulator is to control its motion (as in conventional robot control) and in addition give it a "disturbance ...
- **p. 4 / Front matter - extractive body cue:** Now, for almost all manipulatory tasks the environment at least contains inertias and/or kinematic constraints, physical systems which accept force inputs and which determine their ...
- **p. 5 / 1 Y - extractive body cue:** 5 A bond graph equivalent network representation of the minimum necessary structure of an impedance-controlled machine including both nodic (Zo) and non-nodic (Zn) Impedance giving ...
- **p. 3 / Front matter - extractive body cue:** Assume that this system may interact with its environment across an interaction port at the tip of the linkage.
- **p. 5 / 1 Y - extractive body cue:** The non-nodic components should be coupled to a one-junction5 shared by the manipulator and the environmental admittance.

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / REAL-ROBOT OR HARDWARE`.
- **Target system/task:** rigid/articulated object와 robot manipulator contact scene.
- **Input boundary:** RGB-D/point cloud, object state와 contact/task observation.
- **Output/decision under evaluation:** grasp, pose, force 또는 end-effector trajectory.
- **Primary target:** task completion, contact success, pose/force error와 generalization.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF experiment/result cue | Anchor |
|---|---|---|---|
| 1 Y | EMPIRICAL / REAL-ROBOT OR HARDWARE | The separation of the controller action into a (vector) motion component and a impedance component (which has the properties of a tensor) can be ... | p. 5 (1 Y) |

## Dataset / Benchmark Role

- **p. 2 / Front matter - extractive body cue:** This organization has been proposed as a general form of control and communication for man/machine systems [26]: it is commonly used for robots [2]; and ...
- **p. 2 / Front matter - extractive body cue:** A unified framework for considering the action of both hardware and software in the control of dynamic behavior can be obtained by making the reasonable ...
- **p. 3 / Front matter - extractive body cue:** The real-world phenomenon of stiction is typically represented by a dissipative element with a noninvertible relation between force and velocity.
- **p. 4 / Front matter - extractive body cue:** Thus a general strategy for controlling a manipulator is to control its motion (as in conventional robot control) and in addition give it a "disturbance ...
- **p. 4 / Front matter - extractive body cue:** Now, for almost all manipulatory tasks the environment at least contains inertias and/or kinematic constraints, physical systems which accept force inputs and which determine their ...
- **p. 5 / 1 Y - extractive body cue:** 5 A bond graph equivalent network representation of the minimum necessary structure of an impedance-controlled machine including both nodic (Zo) and non-nodic (Zn) Impedance giving ...
- **p. 3 / Front matter - extractive body cue:** Assume that this system may interact with its environment across an interaction port at the tip of the linkage.
- **p. 5 / 1 Y - extractive body cue:** The non-nodic components should be coupled to a one-junction5 shared by the manipulator and the environmental admittance.

- Names are treated as evaluation resources only when the body sentence places them in a task, split, experiment or benchmark role.

## Figures / Tables as Body Evidence

- figure/table caption cue 없음

## Embodiment / Environment

| Dimension | PDF-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | This organization has been proposed as a general form of control and communication for man/machine systems [26]: it is commonly used for robots [2]; ... | embodiment, simulator version and control stack | p. 2 (Front matter), p. 2 (Front matter) |
| Task/environment | A unified framework for considering the action of both hardware and software in the control of dynamic behavior can be obtained by making the ... | reset, timeout, object/scene variation | p. 2 (Front matter), p. 3 (Front matter) |
| Observation/sensor | RGB-D/point cloud, object state와 contact/task observation | calibration, preprocessing, privileged input | p. 2 (Front matter), p. 2 (Front matter) |
| Output/decision | grasp, pose, force 또는 end-effector trajectory | action frame, controller and termination | p. 3 (Front matter), p. 6 (1 Y) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Strategies directed toward the control of a vector quantity such as position, velocity, or force will be inadequate as they are insufficient to control ... | definition/direction/unit from same section | p. 2 (Front matter) |
| Physical Equivalence Throughout this paper it will be assumed that the complete controlled system is hierarchically organized: a high-level supervisory system plans movement task ... | definition/direction/unit from same section | p. 2 (Front matter) |
| As discussed above, pure force control is also inadequate; however, the term is applied loosely to control strategies using force feedback in combination with ... | definition/direction/unit from same section | p. 4 (Front matter) |
| Thus a general strategy for controlling a manipulator is to control its motion (as in conventional robot control) and in addition give it a ... | definition/direction/unit from same section | p. 4 (Front matter) |
| Nodicity refers to the invariance of the constitutive equation of an element under a change in the reference value (origin) of its argument. | definition/direction/unit from same section | p. 5 (1 Y) |
| Writing the environmental admittance in general form: dy/dt=Ys{y,F) (14) Admittance V=7o(y) (15) The two sets of equations may be combined to write the complete ... | definition/direction/unit from same section | p. 6 (1 Y) |

- Exact success denominator, collision/contact rule, timeout and primary-vs-auxiliary metric are recorded only when the body specifies them.

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| The superposition properties of the Norton equivalent network have been retained without restriction to linear systems. | comparison identity and matched condition | p. 5 (1 Y) |

| Fairness dimension | Required matched condition |
|---|---|
| Observation/action | sensor modality, frame, preprocessing, action space and controller |
| Data | training split, demonstrations, pretraining, labels and leakage |
| Compute | parameter budget, inference steps, hardware, latency and control rate |
| Protocol | reset/timeout, seeds, trials, held-out variation and success denominator |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| In fact, linearized components of the impedance such as the stiffness and the viscosity are second-rank twice covariant tensors. | component/input/data sensitivity | p. 4 (Front matter) |
| Consider again the static relation between force and position: The nodic component of this relation is the part which may be maintained invariant under ... | component/input/data sensitivity | p. 5 (1 Y) |
| The controller must specify a vector quantity such as the desired position, but it must also specify a quantity which is fundamentally different: a ... | component/input/data sensitivity | p. 4 (Front matter) |
| The superposition properties of the Norton equivalent network have been retained without restriction to linear systems. | component/input/data sensitivity | p. 5 (1 Y) |
| Each component of the total impedance is represented by a generalized Norton equivalent network. | component/input/data sensitivity | p. 6 (1 Y) |
| Note that any non-nodic component of the manipulator behavior may be included in this equivalent network by associating it with a flow source identically ... | component/input/data sensitivity | p. 6 (1 Y) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| In Part I this approach is developed by considering the mechanics of interaction between physical systems. | The separation of the controller action into a (vector) motion component and a impedance component (which has the properties of a tensor) can be ... | PDF body cue; verify exact table/figure and matched conditions | p. 5 (1 Y) |
| Primary metric/result | not separately recovered | numeric claim only at cited anchor | 본문 anchor 없음 |

- Numeric sentences retained from the body:
- **p. 5 / 1 Y - extractive body cue:** 0 ^ 1 S, - V0(l) i T / \ i zn z0 I NON-NODIC NODIC I IMPEDANCE IMPEDANCE ENVIRONMENTAL ADMITTANCE CONTROLLED MANIPULATOR Fig.
- **p. 5 / 1 Y - extractive body cue:** 0 ^ 1 S, - V0(l) i T / \ i zn z0 I NON-NODIC NODIC I IMPEDANCE IMPEDANCE ENVIRONMENTAL ADMITTANCE CONTROLLED MANIPULATOR Fig.

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | Real physical elastic devices exist which cannot be described in the derivative causal form with force as the input variable and motion as the ... | p. 3 (Front matter) |
| body limitation/failure cue | However, as described above, while a constrained inertial object can always be pushed on, it cannot always be moved; These systems are properly described ... | p. 4 (Front matter) |
| body limitation/failure cue | The behavior of the manipulator may now be written as follows (assuming a state-determined system): V 0=V 0:jc) Virtual Source (10) f = V ... | p. 5 (1 Y) |
| body limitation/failure cue | The high-level supervisor, while it may have access to sensory data, does not use that data in an immediate feedback control mode to modulate ... | p. 2 (Front matter) |
| body limitation/failure cue | The kinematic transformation equations are: X1=Ll cos 6{+L2 cos d2+L3 cos d3 (3) X2=Lt smdl+L2smd2+L3sm61 (4) Again, joint angles uniquely define end-point position but ... | p. 3 (Front matter) |
| body limitation/failure cue | Note that nonlinearity does not enter into these definitions. | p. 5 (1 Y) |

- Do not treat unseen objects/tasks/scenes, sensor noise, contact changes, dynamic obstacles or recovery as evaluated unless the body reports them.

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| A unified framework in which to consider the action of both hardware and software in controlling dynamic interaction is desirable. | p. 2 (Front matter) |
| Any of the several graphical techniques for describing physical systems may now be applied to the complete system, controller plus hardware. | p. 2 (Front matter) |

| Audit field | Current status |
|---|---|
| Trials/episodes/seeds | use only body sentences above; otherwise not reported |
| Mean/standard deviation/confidence interval | use only body table/figure; otherwise not reported |
| Latency/throughput | separate inference latency, control rate and simulator throughput |
| Train/eval split/leakage | verify dataset/protocol section |
| Code/checkpoint/environment | see 01_overview.md; not duplicated as evidence |

## Limitations and Verification Questions

- **p. 3 / Front matter - extractive body cue:** Real physical elastic devices exist which cannot be described in the derivative causal form with force as the input variable and motion as the output ...
- **p. 4 / Front matter - extractive body cue:** However, as described above, while a constrained inertial object can always be pushed on, it cannot always be moved; These systems are properly described as ...
- **p. 5 / 1 Y - extractive body cue:** The behavior of the manipulator may now be written as follows (assuming a state-determined system): V 0=V 0:jc) Virtual Source (10) f = V 0 ...
- **p. 2 / Front matter - extractive body cue:** The high-level supervisor, while it may have access to sensory data, does not use that data in an immediate feedback control mode to modulate its ...
- **p. 3 / Front matter - extractive body cue:** The kinematic transformation equations are: X1=Ll cos 6{+L2 cos d2+L3 cos d3 (3) X2=Lt smdl+L2smd2+L3sm61 (4) Again, joint angles uniquely define end-point position but the ...
- **p. 5 / 1 Y - extractive body cue:** Note that nonlinearity does not enter into these definitions.

- **PDF anchors reviewed:** datasets p. 2 (Front matter), p. 2 (Front matter), p. 3 (Front matter), p. 4 (Front matter), p. 4 (Front matter), p. 5 (1 Y), metrics p. 2 (Front matter), p. 2 (Front matter), p. 4 (Front matter), p. 4 (Front matter), p. 5 (1 Y), p. 6 (1 Y), baselines p. 5 (1 Y), results p. 5 (1 Y).
- Which table/figure establishes the primary claim, and what is the exact denominator and uncertainty?
- Which comparison is fair after matching observation, data, compute, action interface, horizon and controller?
- What negative result or untested regime does the paper leave open?
