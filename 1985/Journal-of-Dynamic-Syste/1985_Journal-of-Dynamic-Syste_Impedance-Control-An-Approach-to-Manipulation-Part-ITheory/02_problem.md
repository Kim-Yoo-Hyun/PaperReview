# Problem - Impedance Control: An Approach to Manipulation: Part I—Theory

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (7 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://doi.org/10.1115/1.3140702; PDF retrieval source: https://doi.org/10.1115/1.3140702. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 4 (Front matter), p. 3 (Front matter), p. 3 (Front matter), p. 1 (Front matter), p. 1 (Front matter)): However, as described above, while a constrained inertial object can always be pushed on, it cannot always be moved; These systems are properly described as admittances.

## PDF Body Digest

- **p. 1 / Front matter - extractive body cue:** Neville Hogan Associate Professor, Department of Mechanical Engineering and Laboratory for Manufacturing and Productivity, Massachusetts Institute of Technology, Cambridge, Mass.
- **p. 1 / Front matter - extractive body cue:** 02139 Impedance Control: An Approach to Manipulation: Pari S-Theory Manipulation fundamentally requires the manipulator to be mechanically coupled to the object being manipulated; the manipulator ...
- **p. 1 / Front matter - extractive body cue:** This three-part paper presents an approach to the control of dynamic interaction between a manipulator and its environment.
- **p. 1 / Front matter - extractive body cue:** In Part I this approach is developed by considering the mechanics of interaction between physical systems.
- **p. 1 / Front matter - extractive body cue:** Control of position or force alone is inadequate; control of dynamic behavior is also required.
- **p. 4 / Front matter - extractive body cue:** However, as described above, while a constrained inertial object can always be pushed on, it cannot always be moved; These systems are properly described as ...
- **p. 3 / Front matter - extractive body cue:** Real physical elastic devices exist which cannot be described in the derivative causal form with force as the input variable and motion as the output ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, as described above, while a constrained inertial object can always be pushed on, it cannot always be moved; These systems are ... | rigid/articulated object와 robot manipulator contact scene | body wording is the source claim |
| Observation / input | As the constitutive equation for a point mass is invertible the equations may also be written with Nomenclature W = mechanical work ... | RGB-D/point cloud, object state와 contact/task observation | exact sensor/frame/preprocessing from PDF |
| State / latent | constitutive, equation, point, mass, invertible, equations, written, Nomenclature, mechanical, force | object geometry, affordance, contact mode 또는 end-effector state | notation and tensor shape require body check |
| Output / action | Seen, sytsem, properly, described, admittance, force, output, variable | grasp, pose, force 또는 end-effector trajectory | exact unit/frame/decoder require body check |
| Target outcome | completion, contact success and robustness | task completion, contact success, pose/force error와 generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | object geometry/contact state; body terms: constitutive, equation, point, mass, invertible, equations, written, Nomenclature, mechanical, force | p. 2 (Front matter), p. 2 (Front matter), p. 3 (Front matter) |
| Decision / output variable | grasp/pose/force/trajectory; body terms: Part, developed, considering, mechanics, interaction, between, physical, systems | p. 1 (Front matter), p. 1 (Front matter), p. 2 (Front matter) |
| Objective / loss / cost | task/contact/pose objective; cue terms: Examples, latter, include, constraints, imposed, finite, workspace, nonmobile | p. 5 (1 Y), p. 5 (1 Y), p. 6 (1 Y), p. 6 (1 Y) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (1 Y), p. 6 (1 Y), p. 6 (1 Y) |
| Success / guarantee | completion, contact success and robustness | p. 2 (Front matter), p. 2 (Front matter), p. 4 (Front matter) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 3 / Front matter - extractive body cue:** Real physical elastic devices exist which cannot be described in the derivative causal form with force as the input variable and motion as the output ...
- **p. 3 / Front matter - extractive body cue:** The kinematic transformation equations are: X1=Ll cos 6{+L2 cos d2+L3 cos d3 (3) X2=Lt smdl+L2smd2+L3sm61 (4) Again, joint angles uniquely define end-point position but the ...
- **p. 1 / Front matter - extractive body cue:** It will be shown (in Parts II and III) that the approach can lead to a simplification of some problems in manipulator control.
- **p. 1 / Front matter - extractive body cue:** It is shown that as manipulation is a fundamentally nonlinear problem, the distinction between impedance and admittance is essential, and given the environment contains inertial ...

## What the Paper Changes

PDF contribution framing (p. 1 (Front matter), p. 1 (Front matter), p. 2 (Front matter)): In Part I this approach is developed by considering the mechanics of interaction between physical systems.

- **p. 1 / Front matter - extractive body cue:** The approach developed encompasses and includes the simple positioning or transporting tasks typically performed by robots and/or prostheses.
- **p. 2 / Front matter - extractive body cue:** In the following it is developed from some simple and physically reasonable assumptions.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 3 | Real physical elastic devices exist which cannot be described in the derivative causal form with force as the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | However, as described above, while a constrained inertial object can always be pushed on, it cannot always be ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | The behavior of the manipulator may now be written as follows (assuming a state-determined system): V 0=V 0:jc) ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 2 | The high-level supervisor, while it may have access to sensory data, does not use that data in an ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (Front matter), p. 2 (Front matter), p. 3 (Front matter), p. 6 (1 Y). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 4 (Front matter), p. 3 (Front matter), p. 3 (Front matter), p. 1 (Front matter), p. 1 (Front matter), interface p. 2 (Front matter), p. 2 (Front matter), p. 3 (Front matter), p. 6 (1 Y), objective p. 5 (1 Y), p. 5 (1 Y), p. 6 (1 Y), p. 6 (1 Y).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
