# Problem - Robust Peg-in-Hole Assembly under Uncertainties via Compliant and Interactive Contact-Rich Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (16 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p060.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p060.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 3 (A. Preliminaries), p. 4 (B. Problem Statement), p. 4 (A. Preliminaries)): Fig, 2: (a) The peg-in-hole problem is considered as inserting peg into its matching hole on a planar board (a randomly generated peg is adopted as the example).

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Robust and adaptive robotic peg-in-hole assembly. tunder tight tolerances is e
- **p. 1 / Abstract - extractive body cue:** However, it remains an physical uncertainties from contact-rie exceed the allowed clearance.
- **p. 1 / Abstract - extractive body cue:** In this paper, we study hon age contact between the peg and its matching hole to ‘uncertainties in the assembly process under unstructured settings.
- **p. 1 / Abstract - extractive body cue:** By examining the role of compliance under contact constraints, ‘we present a manipulation system that plans coli
- **p. 1 / Abstract - extractive body cue:** interactions for the peg to 1) iter
- **p. 3 / A. Preliminaries - extractive body cue:** Fig, 2: (a) The peg-in-hole problem is considered as inserting peg into its matching hole on a planar board (a randomly generated peg is adopted ...
- **p. 4 / B. Problem Statement - extractive body cue:** As % shrinks over steps, the expected spread of Ton) decreases and the uncertainty range of the perceived hole's state is reduced,

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Fig, 2: (a) The peg-in-hole problem is considered as inserting peg into its matching hole on a planar board (a randomly generated ... | rigid/articulated object와 robot manipulator contact scene | body wording is the source claim |
| Observation / input | An interaction command cy = (xe, x3) at time ¢ is defined by its starting state x, (considered steady as %¢ - ... | RGB-D/point cloud, object state와 contact/task observation | exact sensor/frame/preprocessing from PDF |
| State / latent | interaction, command, time, defined, starting, state, considered, steady, desired, Execution | object geometry, affordance, contact mode 또는 end-effector state | notation and tensor shape require body check |
| Output / action | Interaction, inclined, states, designed, identify, exploit, environmental, contact | grasp, pose, force 또는 end-effector trajectory | exact unit/frame/decoder require body check |
| Target outcome | completion, contact success and robustness | task completion, contact success, pose/force error와 generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | object geometry/contact state; body terms: interaction, command, time, defined, starting, state, considered, steady, desired, Execution | p. 4 (A. Preliminaries), p. 4 (B. Problem Statement), p. 5 (A. Task Mechanics and Interaction Primitives) |
| Decision / output variable | grasp/pose/force/trajectory; body terms: paired, comer, hole, local, geometry, enables, downstream, iterative | p. 5 (A. Task Mechanics and Interaction Primitives), p. 5 (A. Task Mechanics and Interaction Primitives) |
| Objective / loss / cost | task/contact/pose objective; cue terms: forming, aligned, comer, between, inclined, target, hole, create | p. 5 (A. Task Mechanics and Interaction Primitives), p. 5 (A. Task Mechanics and Interaction Primitives) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 5 (A. Task Mechanics and Interaction Primitives), p. 5 (A. Task Mechanics and Interaction Primitives) |
| Success / guarantee | completion, contact success and robustness | p. 1 (Figure/Table caption), p. 5 (A. Task Mechanics and Interaction Primitives), p. 5 (A. Task Mechanics and Interaction Primitives) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 4 / B. Problem Statement - extractive body cue:** As % shrinks over steps, the expected spread of Ton) decreases and the uncertainty range of the perceived hole's state is reduced,
- **p. 4 / A. Preliminaries - extractive body cue:** Except for the virtually defined desired state x}, any physical existing state Xe.1 during this process is constrained by its task environment as follows:

## What the Paper Changes

PDF contribution framing (p. 5 (A. Task Mechanics and Interaction Primitives), p. 5 (A. Task Mechanics and Interaction Primitives)): (b) A paired comer on the peg and hole: this local geometry enables the downstream iterative insertion process.

- **p. 5 / A. Task Mechanics and Interaction Primitives - extractive body cue:** Interaction with inclined states is designed to identify and exploit its environmental contact constraints.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | pose +1 automatically falls into its nearby local minimum | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | The peg cannot break the alignment according to Lemma 4, as the result {M} is always lower than ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Theoretically, the robustness of the insertion process is conditioned on the peg's state x, instead of its geometric ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (A. Preliminaries), p. 4 (B. Problem Statement), p. 5 (A. Task Mechanics and Interaction Primitives), p. 5 (A. Task Mechanics and Interaction Primitives). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 3 (A. Preliminaries), p. 4 (B. Problem Statement), p. 4 (A. Preliminaries), interface p. 4 (A. Preliminaries), p. 4 (B. Problem Statement), p. 5 (A. Task Mechanics and Interaction Primitives), p. 5 (A. Task Mechanics and Interaction Primitives), objective p. 5 (A. Task Mechanics and Interaction Primitives), p. 5 (A. Task Mechanics and Interaction Primitives).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
