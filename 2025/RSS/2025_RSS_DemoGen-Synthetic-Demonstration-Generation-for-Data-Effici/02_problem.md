# Problem - DemoGen: Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (20 pages; tesseract OCR fallback; extraction quality: high); canonical paper source: https://www.roboticsproceedings.org/rss21/p157.html; PDF retrieval source: https://www.roboticsproceedings.org/rss21/p157.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 5 (A. Problem Formulation)): The observation: or includes both the point cloud data and the proprioceptive feedback from the robot: 0 = (of, of", of), where of?" and 0} reflect the current state of ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Visuomotor policies have shown great promise in robotic manipulation but often require substantial hur collected data for effective per factor driving the high data demands ...
- **p. 1 / Abstract - extractive body cue:** In this work, we present Demo a low-cost, fully synthetic approach for automatic demonstration generation.
- **p. 1 / Abstract - extractive body cue:** Using only one human-collected demonstration per ly augmented demonstrations trajectory to novel object configurations.
- **p. 1 / Abstract - extractive body cue:** Visual observations are synthesized by leveraging, 3D point clouds as the modality and rearranging the subjects in the scene via 3D editing, Empirically, DemoGen significantly ...
- **p. 1 / Abstract - extractive body cue:** Furthermore, DemoGen can be extended to enable additional out-of-distibution capabilities, including disturbance resistance and obstacle avoidance.
- **p. 5 / A. Problem Formulation - extractive body cue:** The observation: or includes both the point cloud data and the proprioceptive feedback from the robot: 0 = (of, of", of), where of?" and 0} ...
- **p. 4 / A. Problem Formulation - extractive body cue:** The action a, consists of the robot arm and robot hhand commands, represented as a - (a""a!!™), where a7" © AP" is the target SE(3) ...

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | The observation: or includes both the point cloud data and the proprioceptive feedback from the robot: 0 = (of, of", of), where ... | demonstration으로 정의된 robot task distribution | body wording is the source claim |
| Observation / input | The observation: or includes both the point cloud data and the proprioceptive feedback from the robot: 0 = (of, of", of), where ... | observation history와 expert trajectory/action | exact sensor/frame/preprocessing from PDF body |
| State / latent | observation, includes, point, cloud, data, proprioceptive, feedback, robot, where, reflect | behavior policy와 temporal action context | notation and tensor shape require body check |
| Output / action | Details, Policy, Training, Fora, fair, comparison, total, steps | predicted action 또는 action chunk | exact unit/frame/decoder require body check |
| Target outcome | closed-loop task success and robustness | imitation error, task success, robustness와 compounding error | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | observation history o_{t−H:t}; body terms: observation, includes, point, cloud, data, proprioceptive, feedback, robot, where, reflect | p. 5 (A. Problem Formulation), p. 4 (A. Problem Formulation), p. 17 (A. Policy Training and Implementation Details) |
| Decision / output variable | expert-like action/chunk a_{t:t+H}; body terms: action, consists, robot, hhand, commands, represented, where, target | p. 4 (A. Problem Formulation) |
| Objective / loss / cost | imitation or action-distribution loss; cue terms: Details, Policy, Training, Fora, fair, comparison, total, steps | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 17 (A. Policy Training and Implementation Details), p. 6 (C. TAMP-based Action Generation), p. 17 (A. Policy Training and Implementation Details) |
| Success / guarantee | closed-loop task success and robustness | p. 4 (B. Benchmarking Spatial Generalization Capability), p. 18 (Figure/Table caption), p. 4 (B. Benchmarking Spatial Generalization Capability) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 5 / A. Problem Formulation - extractive body cue:** The observation: or includes both the point cloud data and the proprioceptive feedback from the robot: 0 = (of, of", of), where of?" and 0} ...

## What the Paper Changes

PDF body contribution framing (p. 4 (A. Problem Formulation)): The action a, consists of the robot arm and robot hhand commands, represented as a - (a""a!!™), where a7" © AP" is the target SE(3) end-effector pose inthe world frame, ...

- additional contribution PDF body cue not selected; no claim inferred

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 12 | Trained on the source demonstrations without obstacles, the visuomotor policy fails to account for potential collisions, e.g., it ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 12 | Obstacle-avoiding trajectories are generated by a motion planning tool [28], ensuring collision-free actions. | reported limitation/failure wording; scope must be verified |
| body cue at p. 11 | When the scene becomes even more complex, e.g. clutter, DemoGen does not necessarily work well. | reported limitation/failure wording; scope must be verified |
| body cue at p. 4 | We vary the number of demonstrations from 25 to 400, The object configurations are randomly sampled from a ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

il writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 5 (A. Problem Formulation), p. 4 (A. Problem Formulation), p. 17 (A. Policy Training and Implementation Details), p. 17 (A. Policy Training and Implementation Details). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 5 (A. Problem Formulation), interface p. 5 (A. Problem Formulation), p. 4 (A. Problem Formulation), p. 17 (A. Policy Training and Implementation Details), p. 17 (A. Policy Training and Implementation Details), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (20 pages; tesseract OCR fallback; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Target problem:** The observation: or includes both the point cloud data and the proprioceptive feedback from the robot: 0 = (of, of", of), where of?" and 0} reflect the current state of ... (p. 5, A. Problem Formulation).
- **Formulation-changing contribution:** In this work, we present Demo a low-cost, fully synthetic approach for automatic demonstration generation. (p. 1, Abstract).
- **Assumption/failure evidence:** Failure-free action execution, ‘To ensure the validity of synthetic demonstrations without on-robot rollouts to filter ut failed trajectories, we require failure-Free action execution Unlike previous works (3, 20] that rely ... (p. 6, C. TAMP-based Action Generation).
- **Interpretation rule:** no state, transition, constraint, guarantee, or downstream claim is inferred when the PDF body does not state it.
