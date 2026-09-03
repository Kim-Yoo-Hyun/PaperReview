# Impedance Control: An Approach to Manipulation: Part I—Theory

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://doi.org/10.1115/1.3140702.
> PDF retrieval source: https://doi.org/10.1115/1.3140702. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 1985 / Journal of Dynamic Systems, Measurement, and Control
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: CORE
- Tags: Robotics, Impedance Control, contact, manipulation
- Official paper: https://doi.org/10.1115/1.3140702
- Full-text retrieval: https://doi.org/10.1115/1.3140702
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 manipulation 문제를 이해하기 위해 읽는다. 본문은 However, as described above, while a constrained inertial object can always be pushed on, it cannot always be moved; These systems are properly described as admittances.를 문제로 두고, In Part I this approach is developed by considering the mechanics of interaction between physical systems.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Neville Hogan.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** 02139 Impedance Control: An Approach to Manipulation: Pari S-Theory Manipulation fundamentally requires the manipulator to be mechanically coupled to the object being manipulated; the manipulator ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** This three-part paper presents an approach to the control of dynamic interaction between a manipulator and its environment.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** In Part I this approach is developed by considering the mechanics of interaction between physical systems.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** Control of position or force alone is inadequate; control of dynamic behavior is also required.
- **p. 4 / Body text (section boundary not confidently recovered) - extractive body cue:** However, as described above, while a constrained inertial object can always be pushed on, it cannot always be moved; These systems are properly described as ...
- **p. 3 / Body text (section boundary not confidently recovered) - extractive body cue:** Real physical elastic devices exist which cannot be described in the derivative causal form with force as the input variable and motion as the output ...

## Core Idea

- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** In Part I this approach is developed by considering the mechanics of interaction between physical systems.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** The approach developed encompasses and includes the simple positioning or transporting tasks typically performed by robots and/or prostheses.
- **p. 2 / Body text (section boundary not confidently recovered) - extractive body cue:** In the following it is developed from some simple and physically reasonable assumptions.
- **p. 2 / Body text (section boundary not confidently recovered) - extractive body cue:** This can be stated as the following postulate:1 "It is impossible to devise a controller which will cause a physical system to present an apparent ...
- **p. 4 / Body text (section boundary not confidently recovered) - extractive body cue:** If it is assumed that at a minimum the manipulator should be capable of stably.positioning a simple mass it can be seen that this network ...
- **p. 4 / Body text (section boundary not confidently recovered) - extractive body cue:** It might then be concluded that what is required in general is the control of a vector of interaction forces.
- **p. 2 / Body text (section boundary not confidently recovered) - extractive body cue:** If the environment is regarded as a source of "disturbances" to the manipulator, then modulating the "disturbance response" of the manipulator will permit control of ...
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** In other situations the manipulator encounters constraints in its environment and the interaction forces are not negligible.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | As the constitutive equation for a point mass is invertible the equations may also be written with Nomenclature W = mechanical work F,F, ,F2 = force TL,XX ,X2 = position Li,L2,L3 = ... | RGB-D/point cloud, object state와 contact/task observation | p. 2 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)) |
| State/latent | constitutive, equation, point, mass, invertible, equations, written, Nomenclature, mechanical, force, position, link | object geometry, affordance, contact mode 또는 end-effector state | p. 2 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)) |
| Output/action | For example, the constitutive equation for a point mass is fundamentally written with velocity as the output variable, defined as a function of momentum; momentum in turn is the integral of the ... | grasp, pose, force 또는 end-effector trajectory | p. 2 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)) |
| Objective/outcome | The kinematic transformations X = L(6) (equations (1), (2), (3) and (4)) are in fact part of the junction structure through which the various elements in a physical system interact2 and impose ... | task completion, contact success, pose/force error와 generalization | p. 3 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)) |

## Main Claims and Actual Contribution

- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** In Part I this approach is developed by considering the mechanics of interaction between physical systems.
- **p. 1 / Body text (section boundary not confidently recovered) - extractive body cue:** The approach developed encompasses and includes the simple positioning or transporting tasks typically performed by robots and/or prostheses.
- **p. 2 / Body text (section boundary not confidently recovered) - extractive body cue:** In the following it is developed from some simple and physically reasonable assumptions.
- **p. 5 / 1 Y - extractive body cue:** The separation of the controller action into a (vector) motion component and a impedance component (which has the properties of a tensor) can be achieved ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (1 Y) |
| Embodiment/environment | This organization has been proposed as a general form of control and communication for man/machine systems [26]: it is commonly used for robots [2]; and there is some evidence that the mammalian ... | hardware/simulator version and reset protocol | p. 2 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)) |
| Dataset/benchmark | The real-world phenomenon of stiction is typically represented by a dissipative element with a noninvertible relation between force and velocity. | role, split, size and leakage | p. 2 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)), p. 4 (Body text (section boundary not confidently recovered)) |
| Metric | Strategies directed toward the control of a vector quantity such as position, velocity, or force will be inadequate as they are insufficient to control the mechanical work exchanged between the manipulator and ... | definition, denominator, direction and uncertainty | p. 2 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)), p. 4 (Body text (section boundary not confidently recovered)) |
| Baseline/ablation | The superposition properties of the Norton equivalent network have been retained without restriction to linear systems. | fair input/data/compute/action matching | p. 5 (1 Y), p. 4 (Body text (section boundary not confidently recovered)), p. 5 (1 Y) |

## Explicit Limitations and Failure Boundary

- **p. 3 / Body text (section boundary not confidently recovered) - extractive body cue:** Real physical elastic devices exist which cannot be described in the derivative causal form with force as the input variable and motion as the output ...
- **p. 4 / Body text (section boundary not confidently recovered) - extractive body cue:** However, as described above, while a constrained inertial object can always be pushed on, it cannot always be moved; These systems are properly described as ...
- **p. 5 / 1 Y - extractive body cue:** The behavior of the manipulator may now be written as follows (assuming a state-determined system): V 0=V 0:jc) Virtual Source (10) f = V 0 ...
- **p. 2 / Body text (section boundary not confidently recovered) - extractive body cue:** The high-level supervisor, while it may have access to sensory data, does not use that data in an immediate feedback control mode to modulate its ...
- **p. 3 / Body text (section boundary not confidently recovered) - extractive body cue:** The kinematic transformation equations are: X1=Ll cos 6{+L2 cos d2+L3 cos d3 (3) X2=Lt smdl+L2smd2+L3sm61 (4) Again, joint angles uniquely define end-point position but the ...
- **p. 5 / 1 Y - extractive body cue:** Note that nonlinearity does not enter into these definitions.
- **p. 2 / Body text (section boundary not confidently recovered) - extractive body cue:** If the environment is regarded as a source of "disturbances" to the manipulator, then modulating the "disturbance response" of the manipulator will permit control of ...

## Why Read It

Planning and control의 manipulation 문제를 이해하기 위해 읽는다. 본문은 However, as described above, while a constrained inertial object can always be pushed on, it cannot always be moved; These systems are properly described as admittances.를 문제로 두고, In Part I this approach is developed by considering the mechanics of interaction between physical systems.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 4 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)), p. 3 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 1 (Body text (section boundary not confidently recovered)), p. 2 (Body text (section boundary not confidently recovered)) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (7 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, as described above, while a constrained inertial object can always be pushed on, it cannot always be moved; These systems are properly described as admittances. (p. 4, Body text (section boundary not confidently recovered)).
- **Actual contribution:** Control of position or force alone is inadequate; control of dynamic behavior is also required. (p. 1, Body text (section boundary not confidently recovered)).
- **Evaluation boundary:** This organization has been proposed as a general form of control and communication for man/machine systems [26]: it is commonly used for robots [2]; and there is some evidence that ... (p. 2, Body text (section boundary not confidently recovered)).
- **Explicit failure boundary:** A large class of manufacturing operations fall into this category: examples include drilling, reaming, routing, counterboring, grinding, bending, chipping, fettling-any task requiring work to be done on the environment. (p. 1, Body text (section boundary not confidently recovered)).
