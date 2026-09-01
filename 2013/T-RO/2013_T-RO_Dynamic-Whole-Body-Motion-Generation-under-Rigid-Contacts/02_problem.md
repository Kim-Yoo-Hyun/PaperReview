# Problem - Dynamic Whole-Body Motion Generation under Rigid Contacts and Other Unilateral Constraints

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://hal.science/lirmm-00831097; PDF retrieval source: https://hal-lirmm.ccsd.cnrs.fr/file/index/docid/831097/filename/2013_itro_saab-Dynamic_Whole_Body_Motion_Generation.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 3 (I. INTRODUCTION)): However, inequality constraints cannot be taken into account explicitly.

## PDF Body Digest

- **p. 2 / Abstract - extractive body cue:** The most widely-used technique to generate wholebody motions on a humanoid robot accounting for various tasks and constraints is the inverse kinematics.
- **p. 2 / Abstract - extractive body cue:** Based on the taskfunction approach, this class of methods makes possible the coordination of the robot movements to execute several tasks in parallel and account ...
- **p. 2 / Abstract - extractive body cue:** To some extent, it also enables dealing with some of the robot constraints (e.g. joint limits or visibility) and managing the quasi-static balance of the ...
- **p. 2 / Abstract - extractive body cue:** In order to fully use the whole range of possible motions, this paper proposes to extend the task-function approach to handle the full dynamics of ...
- **p. 2 / Abstract - extractive body cue:** The definition of multiple objectives is made possible by ordering them inside a strict hierarchy.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, inequality constraints cannot be taken into account explicitly.
- **p. 2 / I. INTRODUCTION - extractive body cue:** The motion manifold cannot be sampled directly but by projection [10].

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, inequality constraints cannot be taken into account explicitly. | high-DoF humanoid whole-body dynamics와 contacts | body wording is the source claim |
| Observation / input | It also eases the use of sensory feedback, since the sensory space is often a good task-space candidate [14], [15]. | proprioception, reference pose/motion, visual or language command | exact sensor/frame/preprocessing from PDF |
| State / latent | eases, sensory, feedback, since, space, often, good, task-space, candidate, notation | whole-body pose, balance/contact state와 skill/mode | notation and tensor shape require body check |
| Output / action | Submitted, IEEE, Transaction, Robotics, quadratic, program, point, clouds | joint/whole-body action, motion target 또는 task trajectory | exact unit/frame/decoder require body check |
| Target outcome | motion/task success and recovery | tracking, balance, skill/task success와 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | whole-body pose/contact/reference state; body terms: eases, sensory, feedback, since, space, often, good, task-space, candidate, notation | p. 2 (I. INTRODUCTION), p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 3 (I. INTRODUCTION) |
| Decision / output variable | joint/whole-body action; body terms: generic, solution, take, account, equalities, inequalities, strict, hierarchy | p. 3 (I. INTRODUCTION), p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | tracking/balance/task objective; cue terms: Elastic, contact, defined, modifying, equation, Similarly, constraint, imposed | p. 8 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 8 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 9 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 9 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 9 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS) |
| Success / guarantee | motion/task success and recovery | p. 10 (VII. EXPERIMENTS), p. 10 (VII. EXPERIMENTS), p. 11 (VII. EXPERIMENTS) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 2 / I. INTRODUCTION - extractive body cue:** The motion manifold cannot be sampled directly but by projection [10].
- **p. 3 / I. INTRODUCTION - extractive body cue:** In [36], a first solution to handle inequalities in the stack of tasks was proposed, but cannot set any inequality constraint on the contact forces.
- **p. 3 / I. INTRODUCTION - extractive body cue:** In [25], a method to extend the QP formulation to any number of priority levels is given.

## What the Paper Changes

PDF contribution framing (p. 3 (I. INTRODUCTION), p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 2 (I. INTRODUCTION)): In this paper, we propose a generic solution to take into account equalities and inequalities in a strict hierarchy to generate a dynamic motion.

- **p. 7 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** To cope with this problem we propose to include the contact forces f in the optimization variables of the QP resolution.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In total, the motion has to be designed in a set that lives in the high-dimensional configuration space but is implicitly limited to a much ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 10 | The simulator checks the collision, computes the acceleration from the collision set and the torque input using a ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | To prevent a collision when grasping, an intermediate point is first reached, above the grasping position. | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | In reaction, all the other aligned joints move to overrun the neck limitation (chest joint of course, but ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | Fig. 4. At low frequency, the ZMP does not saturate because the demanded accelerations are small enough. At ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

humanoid writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 2 (I. INTRODUCTION), p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 3 (I. INTRODUCTION), p. 8 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), interface p. 2 (I. INTRODUCTION), p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 3 (I. INTRODUCTION), p. 8 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), objective p. 8 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 8 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 9 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
