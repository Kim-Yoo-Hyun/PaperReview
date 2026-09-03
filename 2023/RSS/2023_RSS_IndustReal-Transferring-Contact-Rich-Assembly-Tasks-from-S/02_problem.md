# Problem - IndustReal: Transferring Contact-Rich Assembly Tasks from Simulation to Reality

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2305.17110; PDF retrieval source: https://arxiv.org/pdf/2305.17110. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (III. PROBLEM DESCRIPTION), p. 3 (III. PROBLEM DESCRIPTION)): Given modeling limitations and finite compute, simulation will always differ from reality; this reality gap has been notoriously large for robotics.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Robotic assembly is a longstanding challenge, requiring contact-rich interaction and high precision and accuracy.
- **p. 1 / Abstract - extractive body cue:** Many applications also require adaptivity to diverse parts, poses, and environments, as well as low cycle times.
- **p. 1 / Abstract - extractive body cue:** In other areas of robotics, simulation is a powerful tool to develop algorithms, generate datasets, and train agents.
- **p. 1 / Abstract - extractive body cue:** However, simulation has had a more limited impact on assembly.
- **p. 1 / Abstract - extractive body cue:** We present IndustReal, a set of algorithms, systems, and tools that solve assembly tasks in simulation with reinforcement learning (RL) and successfully achieve policy transfer ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Given modeling limitations and finite compute, simulation will always differ from reality; this reality gap has been notoriously large for robotics.
- **p. 2 / I. INTRODUCTION - extractive body cue:** To our knowledge, this is the first system for sim-to-real of all phases of the assembly problem: from detection, to grasping, to part alignment, to ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Given modeling limitations and finite compute, simulation will always differ from reality; this reality gap has been notoriously large for robotics. | rigid/articulated object와 robot manipulator contact scene | body wording is the source claim |
| Observation / input | We used proximal policy optimization (PPO) [53] to learn a stochastic policy a ∼πθ(o) (actor), mapping from observations o ∈O to actions ... | RGB-D/point cloud, object state와 contact/task observation | exact sensor/frame/preprocessing from PDF body |
| State / latent | proximal, policy, optimization, PPO, learn, stochastic, actor, mapping, observations, actions | object geometry, affordance, contact mode 또는 end-effector state | notation and tensor shape require body check |
| Output / action | sim-to-real, transfer, policy-level, action, integrator, PLAI, reduces, steady-state | grasp, pose, force 또는 end-effector trajectory | exact unit/frame/decoder require body check |
| Target outcome | completion, contact success and robustness | task completion, contact success, pose/force error와 generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | object geometry/contact state; body terms: proximal, policy, optimization, PPO, learn, stochastic, actor, mapping, observations, actions | p. 3 (IV. POLICY LEARNING IN SIMULATION), p. 7 (V. POLICY DEPLOYMENT IN REAL WORLD), p. 1 (I. INTRODUCTION) |
| Decision / output variable | grasp/pose/force/trajectory; body terms: secondary, contributions, following, Hardware, present, IndustRealKit, contains, CAD | p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Objective / loss / cost | task/contact/pose objective; cue terms: objective, learn, policy, maximized, expected, discounted, rewards, Unfortunately | p. 3 (IV. POLICY LEARNING IN SIMULATION), p. 7 (V. POLICY DEPLOYMENT IN REAL WORLD), p. 7 (V. POLICY DEPLOYMENT IN REAL WORLD), p. 4 (IV. POLICY LEARNING IN SIMULATION), p. 4 (IV. POLICY LEARNING IN SIMULATION), p. 5 (IV. POLICY LEARNING IN SIMULATION) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (IV. POLICY LEARNING IN SIMULATION), p. 5 (IV. POLICY LEARNING IN SIMULATION), p. 5 (IV. POLICY LEARNING IN SIMULATION) |
| Success / guarantee | completion, contact success and robustness | p. 8 (VI. REAL-WORLD EXPERIMENTS), p. 8 (VI. REAL-WORLD EXPERIMENTS), p. 4 (Figure/Table caption) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / I. INTRODUCTION - extractive body cue:** Robotic assembly is a longstanding challenge [70, 26].
- **p. 2 / I. INTRODUCTION - extractive body cue:** To our knowledge, this is the first system for sim-to-real of all phases of the assembly problem: from detection, to grasping, to part alignment, to ...
- **p. 2 / III. PROBLEM DESCRIPTION - extractive body cue:** Problem Setup Our problem setup is as follows: a Franka robot is mounted to a work surface.
- **p. 3 / III. PROBLEM DESCRIPTION - extractive body cue:** 2: Problem setup and decomposition.

## What the Paper Changes

PDF body contribution framing (p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 4 (IV. POLICY LEARNING IN SIMULATION)): Our secondary contributions are the following: • Hardware: We present IndustRealKit, which contains CAD models for all parts designed for our setup, as well as a list of all purchased ...

- **p. 1 / I. INTRODUCTION - extractive body cue:** Specifically, our primary contributions are the following: • Algorithms: For simulation, we propose three methods to allow RL agents to solve contact-rich tasks in a ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** IndustRealKit allows the research community to easily replicate our experimental hardware and benchmark their performance. • Software: We present IndustRealLib, a lightweight Python library that ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** We present IndustReal, a set of algorithms, systems, and tools for solving contact-rich assembly tasks in simulation and transferring behaviors to reality (Figure 1).
- **p. 4 / IV. POLICY LEARNING IN SIMULATION - extractive body cue:** In addition, for the Insert policies, we introduced observation noise.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | Second, our primary failure cases on the real system were due to slip of the object in the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Engagement failures were almost exclusively due to slip between the gripper and object; we hypothesize that a highforce ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | Our work has limitations, which lend themselves naturally to future research directions. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Failure cases were one missed detection of a peg, as well as one grasp of both a peg ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 3 (IV. POLICY LEARNING IN SIMULATION), p. 7 (V. POLICY DEPLOYMENT IN REAL WORLD), p. 1 (I. INTRODUCTION), p. 7 (V. POLICY DEPLOYMENT IN REAL WORLD). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 2 (III. PROBLEM DESCRIPTION), p. 3 (III. PROBLEM DESCRIPTION), interface p. 3 (IV. POLICY LEARNING IN SIMULATION), p. 7 (V. POLICY DEPLOYMENT IN REAL WORLD), p. 1 (I. INTRODUCTION), p. 7 (V. POLICY DEPLOYMENT IN REAL WORLD), objective p. 3 (IV. POLICY LEARNING IN SIMULATION), p. 7 (V. POLICY DEPLOYMENT IN REAL WORLD), p. 7 (V. POLICY DEPLOYMENT IN REAL WORLD), p. 4 (IV. POLICY LEARNING IN SIMULATION), p. 4 (IV. POLICY LEARNING IN SIMULATION), p. 5 (IV. POLICY LEARNING IN SIMULATION).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** Robotic assembly is a longstanding challenge [70, 26]. (p. 1, I. INTRODUCTION).
- **Formulation-changing contribution:** Specifically, our primary contributions are the following: • Algorithms: For simulation, we propose three methods to allow RL agents to solve contact-rich tasks in a simulator: a simulation-aware policy update ... (p. 1, I. INTRODUCTION).
- **Assumption/failure evidence:** Engagement failures were almost exclusively due to slip between the gripper and object; we hypothesize that a highforce gripper (e.g., Robotiq) would fully resolve this issue. (p. 8, VI. REAL-WORLD EXPERIMENTS).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
