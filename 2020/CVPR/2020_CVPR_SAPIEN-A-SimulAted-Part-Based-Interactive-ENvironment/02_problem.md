# Problem - SAPIEN: A SimulAted Part-Based Interactive ENvironment

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (11 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://openaccess.thecvf.com/content_CVPR_2020/html/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.html; PDF retrieval source: https://openaccess.thecvf.com/content_CVPR_2020/papers/Xiang_SAPIEN_A_SimulAted_Part-Based_Interactive_ENvironment_CVPR_2020_paper.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 1 (1. Introduction), p. 1 (1. Introduction)): It faces challenges from four main aspects: 1) The environment needs to reproduce the real-world physics to some level.

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Building home assistant robots has long been a goal for vision and robotics researchers.
- **p. 1 / Abstract - extractive body cue:** To achieve this task, a simulated environment with physically realistic simulation, sufficient articulated objects, and transferability to the real robot is indispensable.
- **p. 1 / Abstract - extractive body cue:** Existing environments achieve these requirements for robotics simulation with different levels of simplification and focus.
- **p. 1 / Abstract - extractive body cue:** We take one step further in constructing an environment that supports household tasks for training robot learning algorithm.
- **p. 1 / Abstract - extractive body cue:** Our work, SAPIEN, is a realistic and physics-rich simulated environment that hosts a large-scale set of articulated objects.
- **p. 1 / 1. Introduction - extractive body cue:** It faces challenges from four main aspects: 1) The environment needs to reproduce the real-world physics to some level.
- **p. 1 / 1. Introduction - extractive body cue:** One direct way to address the problem is to train robots by interacting with the real environment [30, 4, 27].

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | It faces challenges from four main aspects: 1) The environment needs to reproduce the real-world physics to some level. | defined robot simulator/hardware task suite | body wording is the source claim |
| Observation / input | In this way, we factor out the perception module and allow algorithms to focus on robotic control and interaction tasks; 2) using ... | standardized observation, action, task state와 evaluation split | exact sensor/frame/preprocessing from PDF body |
| State / latent | factor, perception, module, allow, algorithms, focus, robotic, control, interaction, tasks | benchmark state/goal와 method decision | notation and tensor shape require body check |
| Output / action | input, agent, consists, point, clouds, normal, maps, segmentation | policy/controller trajectory 또는 measured result | exact unit/frame/decoder require body check |
| Target outcome | comparable score and protocol validity | success metric, robustness, generalization과 reproducibility | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | standardized episode e and interface; body terms: factor, perception, module, allow, algorithms, focus, robotic, control, interaction, tasks | p. 7 (4.2. Robotic Interaction), p. 8 (4.2. Robotic Interaction), p. 8 (4.2. Robotic Interaction) |
| Decision / output variable | method trajectory/action; body terms: input, agent, consists, point, clouds, normal, maps, segmentation | p. 8 (4.2. Robotic Interaction), p. 1 (1. Introduction), p. 7 (4.2. Robotic Interaction) |
| Objective / loss / cost | benchmark score and failure cost; cue terms: During, training, agents, receive, positive, rewards, when, target | no optimization/equation sentence selected |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 8 (4.2. Robotic Interaction) |
| Success / guarantee | comparable score and protocol validity | p. 8 (4.2. Robotic Interaction), p. 8 (4.2. Robotic Interaction), p. 7 (4.1. Robotic Perception) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1. Introduction - extractive body cue:** One direct way to address the problem is to train robots by interacting with the real environment [30, 4, 27].

## What the Paper Changes

PDF body contribution framing (p. 8 (4.2. Robotic Interaction), p. 1 (1. Introduction), p. 7 (4.2. Robotic Interaction), p. 7 (4.2. Robotic Interaction), p. 8 (4.2. Robotic Interaction)): The input of the agent consists of point clouds, normal maps and segmentation masks captured by three fixed cameras mounted on the left, right and front of the arena respectively.

- **p. 1 / 1. Introduction - extractive body cue:** We show the ray-traced scene (top) and robot camera views (bottom): RGB image, surface normals, depth and semantic segmentation of motion parts, while a robot ...
- **p. 7 / 4.2. Robotic Interaction - extractive body cue:** Also, this mode enables end-toend learning for perception and interactions (e.g., learning perception with a specific interaction target).
- **p. 7 / 4.2. Robotic Interaction - extractive body cue:** Having both diverse object categories and rich intra-class instance variations allows us to perform such tasks on multiple object instances at category levels.
- **p. 8 / 4.2. Robotic Interaction - extractive body cue:** To demonstrate our simulator in manipulation tasks, we first use manually designed heuristic pipelines to solve the tasks.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 7 | If the agent cannot move the joint to the given threshold or move 11103 | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | in the opposite direction, then it fails. | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | During training, agents receive positive rewards when the target part approaches the joint limit with the opening door/drawer, ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

benchmark writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 7 (4.2. Robotic Interaction), p. 8 (4.2. Robotic Interaction), p. 8 (4.2. Robotic Interaction), p. 1 (1. Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 1 (1. Introduction), p. 1 (1. Introduction), interface p. 7 (4.2. Robotic Interaction), p. 8 (4.2. Robotic Interaction), p. 8 (4.2. Robotic Interaction), p. 1 (1. Introduction), objective no optimization/equation sentence selected.
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
