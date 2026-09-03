# Problem - SPIN: Simultaneous Perception, Interaction and Navigation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (10 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content/CVPR2024/html/Uppal_SPIN_Simultaneous_Perception_Interaction_and_Navigation_CVPR_2024_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content/CVPR2024/papers/Uppal_SPIN_Simultaneous_Perception_Interaction_and_Navigation_CVPR_2024_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1. Introduction), p. 2 (1. Introduction)): We evaluate across 6 benchmarks in simulation ranging from easy, medium, and hard difficulty, and two real-world environments with a similar level of clutter as the hard environments in simulation ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** While there has been remarkable progress recently in the fields of manipulation and locomotion, mobile manipulation remains a long-standing challenge.
- **p. 1 / Abstract - extractive body cue:** Compared to locomotion or static manipulation, a mobile system must make a diverse range of long-horizon tasks feasible in unstructured and dynamic environments.
- **p. 1 / Abstract - extractive body cue:** While the applications are broad and interesting, there are a plethora of challenges in developing these systems such as coordination between the base and arm, ...
- **p. 1 / Abstract - extractive body cue:** Prior works approach the problem using disentangled modular skills for mobility and manipulation that are trivially tied together.
- **p. 1 / Abstract - extractive body cue:** This causes several limitations such as compounding errors, delays in decision-making, and no whole-body coordination.
- **p. 2 / 1. Introduction - extractive body cue:** We evaluate across 6 benchmarks in simulation ranging from easy, medium, and hard difficulty, and two real-world environments with a similar level of clutter as ...
- **p. 2 / 1. Introduction - extractive body cue:** We train our approach via reinforcement learning (RL), and to get around the computational bottleneck of rendering depth images, we use a teacher-student training framework ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | We evaluate across 6 benchmarks in simulation ranging from easy, medium, and hard difficulty, and two real-world environments with a similar level ... | mobile base와 one/two-arm manipulation environment | body wording is the source claim |
| Observation / input | In particular, the policy gets proprioception xt and only visible scandots ˜st = F(st, xt) as observation and has to predict both ... | egocentric RGB-D, language/task goal, base-arm proprioception | exact sensor/frame/preprocessing from PDF body |
| State / latent | particular, policy, gets, proprioception, only, visible, scandots, observation, predict, camera | map/object/contact state와 base-arm coordination decision | notation and tensor shape require body check |
| Output / action | latent, passed, student, policy, predict, actions, arobot, acam | base motion plus arm/gripper action | exact unit/frame/decoder require body check |
| Target outcome | task completion and recovery | long-horizon task success, reachability, collision과 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | base-arm-object state and language/task goal; body terms: particular, policy, gets, proprioception, only, visible, scandots, observation, predict, camera | p. 4 (2. Method), p. 4 (2. Method), p. 5 (2.2. Phase 2 - From Scandots to Depth) |
| Decision / output variable | base plus arm/gripper action; body terms: find, outperforms, classical, methods, baselines, active, vision, Coupled | p. 2 (1. Introduction), p. 3 (2. Method), p. 4 (2. Method) |
| Objective / loss / cost | long-horizon task utility under reachability/contact constraints; cue terms: Rewards, navigation, task, distance, goal, reward, along, forward | p. 5 (2.2. Phase 2 - From Scandots to Depth), p. 4 (2. Method), p. 4 (2. Method), p. 5 (2.2. Phase 2 - From Scandots to Depth) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 3 (2. Method), p. 3 (2. Method), p. 5 (2.2. Phase 2 - From Scandots to Depth) |
| Success / guarantee | task completion and recovery | p. 7 (4.2. Real-world results), p. 7 (4.3. Simulation results), p. 8 (4.3. Simulation results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 2 / 1. Introduction - extractive body cue:** We train our approach via reinforcement learning (RL), and to get around the computational bottleneck of rendering depth images, we use a teacher-student training framework ...

## What the Paper Changes

PDF body contribution framing (p. 2 (1. Introduction), p. 3 (2. Method), p. 4 (2. Method), p. 2 (1. Introduction), p. 4 (2. Method)): We find that our method outperforms classical methods and baselines which do not use active vision.

- **p. 3 / 2. Method - extractive body cue:** We propose two methods: (1) Coupled Visuomotor Optimization (CVO) learns robot and camera actions at the same time.
- **p. 4 / 2. Method - extractive body cue:** We present two approaches to tackle this problem.
- **p. 2 / 1. Introduction - extractive body cue:** We now discuss our approach in detail.
- **p. 4 / 2. Method - extractive body cue:** The agent learns to develop whole-body coordination such as the robot's arm movement in the last two frames, in order to reactively adapt and navigate ...

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 4 | Figure 4. We illustrate one scenario of the simulation benchmark here with many obstacles in a narrow passage. ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 5 | What are the limitations of the latter? | reported limitation/failure wording; scope must be verified |
| body cue at p. 6 | We observe that in cases when there is no feasible path for the robot to navigate through, it ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 7 | 2 we compare success rate and average number of collisions. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

mobile_manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (2. Method), p. 4 (2. Method), p. 5 (2.2. Phase 2 - From Scandots to Depth), p. 2 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1. Introduction), p. 2 (1. Introduction), interface p. 4 (2. Method), p. 4 (2. Method), p. 5 (2.2. Phase 2 - From Scandots to Depth), p. 2 (1. Introduction), objective p. 5 (2.2. Phase 2 - From Scandots to Depth), p. 4 (2. Method), p. 4 (2. Method), p. 5 (2.2. Phase 2 - From Scandots to Depth).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (10 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** We evaluate across 6 benchmarks in simulation ranging from easy, medium, and hard difficulty, and two real-world environments with a similar level of clutter as the hard environments in simulation ... (p. 2, 1. Introduction).
- **Formulation-changing contribution:** We now discuss our approach in detail. (p. 2, 1. Introduction).
- **Assumption/failure evidence:** It has the emergent ability to avoid a new obstacle in space, whereas the classical baseline relies on the pre-built map and fails entirely. (p. 7, 4.2. Real-world results).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
