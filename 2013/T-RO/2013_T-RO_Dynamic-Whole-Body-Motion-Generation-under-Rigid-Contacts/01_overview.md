# Dynamic Whole-Body Motion Generation under Rigid Contacts and Other Unilateral Constraints

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://hal.science/lirmm-00831097.
> PDF retrieval source: https://hal-lirmm.ccsd.cnrs.fr/file/index/docid/831097/filename/2013_itro_saab-Dynamic_Whole_Body_Motion_Generation.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2013 / T-RO
- Authors: not duplicated here when not verified in the registry source
- Primary track: Planning and control
- Tier: CORE
- Tags: Robotics, whole-body control, rigid contact, hierarchical control
- Official paper: https://hal.science/lirmm-00831097
- Full-text retrieval: https://hal-lirmm.ccsd.cnrs.fr/file/index/docid/831097/filename/2013_itro_saab-Dynamic_Whole_Body_Motion_Generation.pdf
- Code/Project: not identified
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-02 (18 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Planning and control의 humanoid 문제를 이해하기 위해 읽는다. 본문은 However, inequality constraints cannot be taken into account explicitly.를 문제로 두고, In this paper, we propose a generic solution to take into account equalities and inequalities in a strict hierarchy to generate a dynamic motion.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 2 / Abstract - extractive body cue:** The most widely-used technique to generate wholebody motions on a humanoid robot accounting for various tasks and constraints is the inverse kinematics.
- **p. 2 / Abstract - extractive body cue:** Based on the taskfunction approach, this class of methods makes possible the coordination of the robot movements to execute several tasks in parallel and account ...
- **p. 2 / Abstract - extractive body cue:** To some extent, it also enables dealing with some of the robot constraints (e.g. joint limits or visibility) and managing the quasi-static balance of the ...
- **p. 2 / Abstract - extractive body cue:** In order to fully use the whole range of possible motions, this paper proposes to extend the task-function approach to handle the full dynamics of ...
- **p. 2 / Abstract - extractive body cue:** The definition of multiple objectives is made possible by ordering them inside a strict hierarchy.
- **p. 2 / I. INTRODUCTION - extractive body cue:** However, inequality constraints cannot be taken into account explicitly.
- **p. 2 / I. INTRODUCTION - extractive body cue:** The motion manifold cannot be sampled directly but by projection [10].

## Core Idea

- **p. 3 / I. INTRODUCTION - extractive body cue:** In this paper, we propose a generic solution to take into account equalities and inequalities in a strict hierarchy to generate a dynamic motion.
- **p. 7 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** To cope with this problem we propose to include the contact forces f in the optimization variables of the QP resolution.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In total, the motion has to be designed in a set that lives in the high-dimensional configuration space but is implicitly limited to a much ...
- **p. 7 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Including the contact forces within the QP Solver Condition (32) must now be introduced in the HQP proposed at the end of Section IV-B 1) ...
- **p. 8 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Opening to other classes of contacts The model (22)-(38) is built on the rigid point contact.
- **p. 8 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Finally, the complete HQP for n contacts and k tasks is written: (39) ≺(22.1) ≺(38.1) ≺... ≺(22.n) ≺(38.n) ≺ (14.1) ≺... ≺(14.k) ≺(40), with the ...
- **p. 9 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Submitted to IEEE Transaction on Robotics 8 of motion (22) [40].
- **p. 9 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** Motions with slips are made possible by removing the motion constraint (22) in the tangent directions, and setting a constraint on the tangent force to ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | It also eases the use of sensory feedback, since the sensory space is often a good task-space candidate [14], [15]. | proprioception, reference pose/motion, visual or language command | p. 2 (I. INTRODUCTION), p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS) |
| State/latent | eases, sensory, feedback, since, space, often, good, task-space, candidate, notation, necessary, sufficient | whole-body pose, balance/contact state와 skill/mode | p. 2 (I. INTRODUCTION), p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 3 (I. INTRODUCTION) |
| Output/action | Using this notation, the necessary and sufficient condition to ensure the contact stability (in the sense that the contact remains in the same phase of the complementary condition, i.e. no take off) ... | joint/whole-body action, motion target 또는 task trajectory | p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 3 (I. INTRODUCTION), p. 8 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS) |
| Objective/outcome | Elastic contact can be defined by modifying the equation 8Similarly, the constraint can be imposed on a least-square τ. | tracking, balance, skill/task success와 recovery | p. 8 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 8 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS) |

## Main Claims and Actual Contribution

- **p. 3 / I. INTRODUCTION - extractive body cue:** In this paper, we propose a generic solution to take into account equalities and inequalities in a strict hierarchy to generate a dynamic motion.
- **p. 7 / V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS - extractive body cue:** To cope with this problem we propose to include the contact forces f in the optimization variables of the QP resolution.
- **p. 2 / I. INTRODUCTION - extractive body cue:** In total, the motion has to be designed in a set that lives in the high-dimensional configuration space but is implicitly limited to a much ...
- **p. 12 / VII. EXPERIMENTS - extractive body cue:** To improve the naturalness of the motion, a task egaze defined by (50) is set to constrain the gaze toward the armrest to be grasped.
- **p. 14 / VII. EXPERIMENTS - extractive body cue:** The second gripper helps to improve the stability by decreasing the tangent forces at each contact point.
- **p. 10 / VII. EXPERIMENTS - extractive body cue:** The second one presents a complex sequence of tasks to make the robot sit in an armchair using several successive contacts.
- **p. 10 / VII. EXPERIMENTS - extractive body cue:** However, this solution has the drawback that the servo is on the position variables, while, as explained in the previous section, the robustness mainly relies ...
- **p. 11 / VII. EXPERIMENTS - extractive body cue:** 2) Results: The experiment is summed up by Figures 3 to 6.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SIMULATION | do not infer unreported downstream behavior | p. 12 (VII. EXPERIMENTS), p. 14 (VII. EXPERIMENTS) |
| Embodiment/environment | The result of this simulation is a joint trajectory of the robot, that complies to the multi-body dynamics. | hardware/simulator version and reset protocol | p. 10 (VII. EXPERIMENTS), p. 10 (VII. EXPERIMENTS) |
| Dataset/benchmark | A tracking task is imposed to the robot head to make it oscillate. | role, split, size and leakage | p. 10 (VII. EXPERIMENTS), p. 10 (VII. EXPERIMENTS), p. 11 (VII. EXPERIMENTS), p. 11 (VII. EXPERIMENTS) |
| Metric | However, this solution has the drawback that the servo is on the position variables, while, as explained in the previous section, the robustness mainly relies on the accuracy of the force variables. | definition, denominator, direction and uncertainty | p. 10 (VII. EXPERIMENTS), p. 10 (VII. EXPERIMENTS), p. 11 (VII. EXPERIMENTS) |
| Baseline/ablation | All the joints are properly stopped at the limit, and can leave the neighborhood of the limit without being stuck as it may appear with some avoidance techniques. | fair input/data/compute/action matching | p. 12 (VII. EXPERIMENTS), p. 14 (VII. EXPERIMENTS), p. 12 (VII. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 10 / VII. EXPERIMENTS - extractive body cue:** The simulator checks the collision, computes the acceleration from the collision set and the torque input using a linear solver and numerically integrates ¨q using ...
- **p. 12 / VII. EXPERIMENTS - extractive body cue:** To prevent a collision when grasping, an intermediate point is first reached, above the grasping position.
- **p. 12 / VII. EXPERIMENTS - extractive body cue:** In reaction, all the other aligned joints move to overrun the neck limitation (chest joint of course, but also hip and ankle joints).
- **p. 11 / Figure/Table caption - extractive body cue:** Fig. 4. At low frequency, the ZMP does not saturate because the demanded accelerations are small enough. At medium frequency, the accelerations are larger and ...
- **p. 15 / VIII. CONCLUSION - extractive body cue:** Experiment C: Robustness criterion VI-C.
- **p. 10 / VII. EXPERIMENTS - extractive body cue:** However, this solution has the drawback that the servo is on the position variables, while, as explained in the previous section, the robustness mainly relies ...
- **p. 11 / VII. EXPERIMENTS - extractive body cue:** The robustness criterion is finite when the friction cones are considered.

## Why Read It

Planning and control의 humanoid 문제를 이해하기 위해 읽는다. 본문은 However, inequality constraints cannot be taken into account explicitly.를 문제로 두고, In this paper, we propose a generic solution to take into account equalities and inequalities in a strict hierarchy to generate a dynamic motion.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 3 (I. INTRODUCTION), p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS), p. 7 (V. REDUCED FORMULATION OF RIGID PLANAR CONTACTS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
