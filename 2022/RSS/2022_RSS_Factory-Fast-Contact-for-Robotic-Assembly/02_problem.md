# Problem - Factory: Fast Contact for Robotic Assembly

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2205.03532; PDF retrieval source: https://arxiv.org/pdf/2205.03532. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): However, assembly has been exceptionally difficult to automate due to physical complexity, part variability, and strict reliability requirements [42].

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Robotic assembly is one of the oldest and most challenging applications of robotics.
- **p. 1 / Abstract - extractive body cue:** In other areas of robotics, such as perception and grasping, simulation has rapidly accelerated research progress, particularly when combined with modern deep learning.
- **p. 1 / Abstract - extractive body cue:** However, accurately, efficiently, and robustly simulating the range of contact-rich interactions in assembly remains a longstanding challenge.
- **p. 1 / Abstract - extractive body cue:** In this work, we present Factory, a set of physics simulation methods and robot learning tools for such applications.
- **p. 1 / Abstract - extractive body cue:** We achieve real-time or faster simulation of a wide range of contact-rich scenes, including simultaneous simulation of 1000 nut-and-bolt interactions.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, assembly has been exceptionally difficult to automate due to physical complexity, part variability, and strict reliability requirements [42].
- **p. 1 / I. INTRODUCTION - extractive body cue:** In research, methods for robotic assembly often use lessexpensive equipment, require fewer custom fixtures, achieve increased robustness to variation, and may recover from failure [35, ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | However, assembly has been exceptionally difficult to automate due to physical complexity, part variability, and strict reliability requirements [42]. | rigid/articulated object와 robot manipulator contact scene | body wording is the source claim |
| Observation / input | The contact forces generated during policy execution are compared to literature values from the real world and show strong consistency. | RGB-D/point cloud, object state와 contact/task observation | exact sensor/frame/preprocessing from PDF body |
| State / latent | contact, forces, generated, during, policy, execution, compared, literature, values, real | object geometry, affordance, contact mode 또는 end-effector state | notation and tensor shape require body check |
| Output / action | Specifically, uniquely, combine, SDF, collisions, contact, reduction, Gauss-Seidel | grasp, pose, force 또는 end-effector trajectory | exact unit/frame/decoder require body check |
| Target outcome | completion, contact success and robustness | task completion, contact success, pose/force error와 generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | object geometry/contact state; body terms: contact, forces, generated, during, policy, execution, compared, literature, values, real | p. 2 (I. INTRODUCTION), p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 4 (III. CONTACT-RICH SIMULATION METHODS) |
| Decision / output variable | grasp/pose/force/trajectory; body terms: present, Factory, physics, simulation, methods, robot, learning, tools | p. 1 (I. INTRODUCTION), p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 1 (I. INTRODUCTION) |
| Objective / loss / cost | task/contact/pose objective; cue terms: contact, position, face, determined, performing, iterative, local, minimization | p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 5 (III. CONTACT-RICH SIMULATION METHODS), p. 5 (III. CONTACT-RICH SIMULATION METHODS) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 5 (III. CONTACT-RICH SIMULATION METHODS), p. 5 (III. CONTACT-RICH SIMULATION METHODS) |
| Success / guarantee | completion, contact success and robustness | p. 10 (V. REINFORCEMENT LEARNING), p. 11 (VI. DISCUSSION), p. 8 (V. REINFORCEMENT LEARNING) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** In research, methods for robotic assembly often use lessexpensive equipment, require fewer custom fixtures, achieve increased robustness to variation, and may recover from failure [35, ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** As an example, we simulate 1000 simultaneous nut-and-bolt assemblies in real-time on a single GPU, whereas the prior state-ofthe-art was a single nut-and-bolt assembly at ...

## What the Paper Changes

PDF body contribution framing (p. 1 (I. INTRODUCTION), p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION)): In this work, we present Factory, a set of physics simulation methods and robot learning tools for such interactions (Fig.

- **p. 4 / III. CONTACT-RICH SIMULATION METHODS - extractive body cue:** Specifically, given a triangle mesh representing the boundaries of the object, we generate an SDF for the mesh at initialization time and store it as ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Meanwhile, physics simulation has become a powerful tool for robotics development.
- **p. 2 / I. INTRODUCTION - extractive body cue:** The suite includes 60 carefully-designed assets, 3 robotic assembly environments, and 7 classical robot controllers.
- **p. 2 / I. INTRODUCTION - extractive body cue:** We aim for Factory to greatly accelerate research and development in robotic assembly, as well as serve as a powerful tool for contact-rich simulation of ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | A common initial failure case during training was collision between the gripper and the bolt, dislodging the nut. | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Nevertheless, training was replete with a diverse range of pathologies, including high-energy collision with the bolt shank, roll-pitch ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | Within simulation, we plan to make 3 improvements to our SDF collision scheme: 1) the ability to robustly ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 10 | Although Factory was developed with robotic assembly as a motivating application, there are no limitations on using our ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 2 (I. INTRODUCTION), p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 5 (III. CONTACT-RICH SIMULATION METHODS). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), interface p. 2 (I. INTRODUCTION), p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 5 (III. CONTACT-RICH SIMULATION METHODS), objective p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 4 (III. CONTACT-RICH SIMULATION METHODS), p. 5 (III. CONTACT-RICH SIMULATION METHODS), p. 5 (III. CONTACT-RICH SIMULATION METHODS).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (21 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** However, assembly has been exceptionally difficult to automate due to physical complexity, part variability, and strict reliability requirements [42]. (p. 1, I. INTRODUCTION).
- **Formulation-changing contribution:** In this work, we present Factory, a set of physics simulation methods and robot learning tools for such interactions (Fig. (p. 1, I. INTRODUCTION).
- **Assumption/failure evidence:** A common initial failure case during training was collision between the gripper and the bolt, dislodging the nut. (p. 9, V. REINFORCEMENT LEARNING).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
