# Problem - Complementarity-Free Multi-Contact Modeling and Optimization for Dexterous Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (18 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p111.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p111.pdf. The note is an evidence-anchored body analysis; exact tables/equations remain at the cited page anchors. Reading tracker status/evidence was not changed.

## Problem in One Sentence

PDF body framing (p. 2 (Abstract), p. 1 (Abstract), p. 1 (Abstract), p. 2 (A. Rigid Body Multi-contact Models), p. 3 (C. Reinforcement Learning for Dexterous Manipulation)): (III) Fewer hyperparameters: the proposed model has fewer parameters, making it easy to tune, and it also supports model auto-tuning using any learning framework ‘The goal of the new contact ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** A significant barrier preventing model-based methods from achieving real-time and versatile dexterous robotic maniptation is the inherent complexity of multi-contact dynamics. ‘Traditionally formulated as complementarity ...
- **p. 1 / Abstract - extractive body cue:** Our new model, derived from the duality of optimization-based contact models, dispenses with the complementarity constructs entirely, providing
- **p. 1 / Abstract - extractive body cue:** 1s closed-form time stepping, uutomatic satisfaction with Coulomb's friction
- **p. 1 / Abstract - extractive body cue:** ind Allegro hand on-palm reorientation, all performed with rse objects.
- **p. 1 / Abstract - extractive body cue:** Our method consistently achieves state-of-the ) a 96.5% average success rate across all objects
- **p. 2 / Abstract - extractive body cue:** (III) Fewer hyperparameters: the proposed model has fewer parameters, making it easy to tune, and it also supports model auto-tuning using any learning framework ‘The ...
- **p. 1 / Abstract - extractive body cue:** This introduces computational challenges in both learning of contact dynamics [42] and combinatorics optimization of contact modes [14, 41.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | (III) Fewer hyperparameters: the proposed model has fewer parameters, making it easy to tune, and it also supports model auto-tuning using any ... | rigid/articulated object와 robot manipulator contact scene | body wording is the source claim |
| Observation / input | This implementation creates « closed-loop control effect on the real system, ie., feedback from system state qf to control input 1 (qi | RGB-D/point cloud, object state와 contact/task observation | exact sensor/frame/preprocessing from PDF |
| State / latent | implementation, creates, closed-loop, control, effect, real, system, feedback, state, input | object geometry, affordance, contact mode 또는 end-effector state | notation and tensor shape require body check |
| Output / action | simplicity, model, manipulation, system, quasi-dynamic, formulation, primarily, captures | grasp, pose, force 또는 end-effector trajectory | exact unit/frame/decoder require body check |
| Target outcome | completion, contact success and robustness | task completion, contact success, pose/force error와 generalization | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | object geometry/contact state; body terms: implementation, creates, closed-loop, control, effect, real, system, feedback, state, input | p. 4 (A. Optimization-based Quasi-Dynamic Contact Model), p. 4 (A. Optimization-based Quasi-Dynamic Contact Model), p. 3 (A. Optimization-based Quasi-Dynamic Contact Model) |
| Decision / output variable | grasp/pose/force/trajectory; body terms: consistently, achieves, state-of-the, average, success, rate, across, objects | p. 1 (Abstract), p. 1 (Front matter), p. 2 (Abstract) |
| Objective / loss / cost | task/contact/pose objective; cue terms: searches, optimal, input, sequence, control, bounds, minimizing, path | p. 2 (A. Rigid Body Multi-contact Models), p. 2 (A. Rigid Body Multi-contact Models), p. 3 (A. Optimization-based Quasi-Dynamic Contact Model), p. 3 (B. Planning and Control with Contact Dynamics), p. 4 (A. Duality of Optimization-based Contact Model), p. 4 (A. Duality of Optimization-based Contact Model) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 4 (A. Duality of Optimization-based Contact Model), p. 2 (A. Rigid Body Multi-contact Models), p. 3 (A. Optimization-based Quasi-Dynamic Contact Model) |
| Success / guarantee | completion, contact success and robustness | p. 12 (Figure/Table caption), p. 10 (B. MPC Setting and Results), p. 10 (B. MPC Setting and Results) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF anchors.

## Bottleneck in Prior Work

- **p. 1 / Abstract - extractive body cue:** This introduces computational challenges in both learning of contact dynamics [42] and combinatorics optimization of contact modes [14, 41.
- **p. 1 / Abstract - extractive body cue:** A primary challenge for model-based methods is the non-smooth and hybrid nature of contact-rich dynamics - smooth motions are frequently interrupted by discrete contact events ...
- **p. 2 / A. Rigid Body Multi-contact Models - extractive body cue:** Since the NCPs cannot be interpreted as the KKT conditions of a convex program, they are challenging to solve.
- **p. 3 / C. Reinforcement Learning for Dexterous Manipulation - extractive body cue:** Our proposed method aims to bridge this gap and even surpass state-of-the-art RL in suecess rate and manipulation accuracy.

## What the Paper Changes

PDF contribution framing (p. 1 (Abstract), p. 1 (Front matter), p. 2 (Abstract), p. 5 (B. New Complementarty-Free Multi-Contact Model), p. 2 (A. Rigid Body Multi-contact Models)): Our method consistently achieves state-of-the ) a 96.5% average success rate across all objects

- **p. 1 / Front matter - extractive body cue:** 1: We propose a complementarty-free multi-contact model that a various challenging dexterous manipulation tasks, including fingertip in-air manipulation (cols.
- **p. 2 / Abstract - extractive body cue:** Our method sets a new benchmark for model-based contact-rich dexterous manipulation: « Highly versatile dexterity: 96.5% average success rate across all objects and environments « ...
- **p. 5 / B. New Complementarty-Free Multi-Contact Model - extractive body cue:** To circumvent the dual complementarity in (13), we propose ‘new contact model based on Lemma 1.
- **p. 2 / A. Rigid Body Multi-contact Models - extractive body cue:** (62, 33] developed penalty-based contact models.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 9 | [1p Peargal] $0.02 tm), 1-(dhggecd™)? < 0.015, is deemed a failure if the object does not satisfy (33) ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 15 | Fig. 17: An failure case for stick reorientation, | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | Fig. 6: Left: cube free falling, rolling and sliding on ground. Middle and right: the horizontal and vertical ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 9 | The fingertips must coordinate to prevent the object from falling while moving it to the target. | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. PDF interface anchors: p. 4 (A. Optimization-based Quasi-Dynamic Contact Model), p. 4 (A. Optimization-based Quasi-Dynamic Contact Model), p. 3 (A. Optimization-based Quasi-Dynamic Contact Model), p. 2 (Abstract). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **PDF anchors reviewed:** problem p. 2 (Abstract), p. 1 (Abstract), p. 1 (Abstract), p. 2 (A. Rigid Body Multi-contact Models), p. 3 (C. Reinforcement Learning for Dexterous Manipulation), interface p. 4 (A. Optimization-based Quasi-Dynamic Contact Model), p. 4 (A. Optimization-based Quasi-Dynamic Contact Model), p. 3 (A. Optimization-based Quasi-Dynamic Contact Model), p. 2 (Abstract), objective p. 2 (A. Rigid Body Multi-contact Models), p. 2 (A. Rigid Body Multi-contact Models), p. 3 (A. Optimization-based Quasi-Dynamic Contact Model), p. 3 (B. Planning and Control with Contact Dynamics), p. 4 (A. Duality of Optimization-based Contact Model), p. 4 (A. Duality of Optimization-based Contact Model).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
