# Problem - MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://proceedings.mlr.press/v305/wu25c.html; PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v305/main/assets/wu25c/wu25c.pdf. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Problem in One Sentence

PDF body framing (p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction)): Get the Water Cook Food Pick up the Fruit Mobile Trajectory Arm Trajectory Fixed-base Manipulation MoTo AnyGrasp OpenVLA RDT-1B iDP3 Figure 1: MoTo can be plugged into any fixed-base manipulation ...

## PDF Body Digest

- **p. 1 / Abstract - extractive body cue:** Mobile manipulation is the fundamental challenge for robotics in assisting humans with diverse tasks and environments in everyday life.
- **p. 1 / Abstract - extractive body cue:** Conventional mobile manipulation approaches often struggle to generalize across different tasks and environments due to the lack of large-scale training.
- **p. 1 / Abstract - extractive body cue:** However, recent advances in manipulation foundation models demonstrate impressive generalization capability on a wide range of fixed-base manipulation tasks, which are still limited to a ...
- **p. 1 / Abstract - extractive body cue:** Therefore, we devise a plug-in module named MoTo, which can be combined with any off-the-shelf manipulation foundation model to empower them with mobile manipulation ability.
- **p. 1 / Abstract - extractive body cue:** Specifically, we propose an interactionaware navigation policy to generate robot docking points for generalized mobile manipulation.
- **p. 2 / 1 Introduction - extractive body cue:** Get the Water Cook Food Pick up the Fruit Mobile Trajectory Arm Trajectory Fixed-base Manipulation MoTo AnyGrasp OpenVLA RDT-1B iDP3 Figure 1: MoTo can be ...
- **p. 1 / 1 Introduction - extractive body cue:** However, the requirements to perform diverse tasks in unstructured environments (e.g., assisting humans in their daily lives) present significant challenges.

## System and Scope

| Dimension | PDF body evidence | Registry/robotics interpretation | Boundary |
|---|---|---|---|
| Target problem | Get the Water Cook Food Pick up the Fruit Mobile Trajectory Arm Trajectory Fixed-base Manipulation MoTo AnyGrasp OpenVLA RDT-1B iDP3 Figure 1: ... | mobile base와 one/two-arm manipulation environment | body wording is the source claim |
| Observation / input | Based on robot scanning RGB-D observation to get 3D scene point clouds and graphs, we utilize VLM and multi-view consistency voting to ... | egocentric RGB-D, language/task goal, base-arm proprioception | exact sensor/frame/preprocessing from PDF body |
| State / latent | robot, scanning, RGB-D, observation, scene, point, clouds, graphs, utilize, VLM | map/object/contact state와 base-arm coordination decision | notation and tensor shape require body check |
| Output / action | interaction-aware, navigation, policy, generates, suitable, base, docking, points | base motion plus arm/gripper action | exact unit/frame/decoder require body check |
| Target outcome | task completion and recovery | long-horizon task success, reachability, collision과 recovery | metric/denominator are in 04 evidence |

## Formal Problem Formulation

| Formulation field | PDF body-grounded record | Evidence anchor |
|---|---|---|
| State / observation variable | base-arm-object state and language/task goal; body terms: robot, scanning, RGB-D, observation, scene, point, clouds, graphs, utilize, VLM | p. 4 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Decision / output variable | base plus arm/gripper action; body terms: solve, problem, mobile, manipulation, interaction-aware, navigation, policy, namely | p. 2 (1 Introduction), p. 3 (1 Introduction), p. 5 (4 Approach) |
| Objective / loss / cost | long-horizon task utility under reachability/contact constraints; cue terms: Therefore, robot, action, abase, aarm, solved, optimization, problem | p. 5 (4 Approach), p. 6 (4 Approach), p. 6 (4 Approach), p. 7 (4 Approach), p. 7 (4 Approach), p. 13 (A.3 Training Details) |
| Constraint / feasibility | paper-specific constraints are recorded only where the body states them; otherwise unresolved | p. 13 (A.3 Training Details), p. 6 (4 Approach), p. 6 (4 Approach) |
| Success / guarantee | task completion and recovery | p. 8 (5 Experiment), p. 8 (5 Experiment), p. 7 (5 Experiment) |

- **Formulation status:** domain mapping is an analyst bridge; symbols, initial/terminal conditions, transition/observation model and guarantees are attributed to the paper only at the cited PDF body anchors.

## Bottleneck in Prior Work

- **p. 1 / 1 Introduction - extractive body cue:** However, the requirements to perform diverse tasks in unstructured environments (e.g., assisting humans in their daily lives) present significant challenges.
- **p. 2 / 1 Introduction - extractive body cue:** However, naive combining navigation and manipulation results in compounding errors since the large gap between the goals of navigation and manipulation [17].
- **p. 3 / 1 Introduction - extractive body cue:** 3 Problem Statement Our goal is to enable robots to perform long-horizon mobile manipulation tasks with strong generalization ability to unseen environments and goals.
- **p. 3 / 1 Introduction - extractive body cue:** More recently, foundation-model-based frameworks like VoxPoser [37] and ReKep [38] leverage pretrained priors to infer physical constraints, which significantly improve generalization.

## What the Paper Changes

PDF body contribution framing (p. 2 (1 Introduction), p. 3 (1 Introduction), p. 5 (4 Approach), p. 3 (1 Introduction)): In this paper, we propose to solve the problem of mobile manipulation with an interaction-aware navigation policy, namely Move and Touch (MoTo).

- **p. 3 / 1 Introduction - extractive body cue:** Inspired by ReKep, we propose a multi-view voting strategy to generate scene-level interaction keypoints to fine-grain guide mobile manipulation trajectory generation.
- **p. 5 / 4 Approach - extractive body cue:** Therefore, we propose a two-stage VLM-based method to generate keypoints for an image, which is divided into keypoint proposal stage and keypoint selection stage.
- **p. 3 / 1 Introduction - extractive body cue:** With the fast development of manipulation foundation models [37, 11, 12, 38], we believe this assumption is reasonable and feasible.

## Assumptions and Failure Boundary

| Body anchor | Observed limitation/failure cue | Interpretation boundary |
|---|---|---|
| body cue at p. 16 | Figure 6: Visualization results for keypoint generation. MoTo selects keypoint proposals (red points) from multi-views, projects them into ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 16 | Figure 7: Failure Cases in real-world experiments. D.1 Manipulation Visualization Figure 6 demonstrates the scene keypoint generation and ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | 5.3 Real World Experiments The OVMM baseline cannot be directly deployed in the real world due to the ... | reported limitation/failure wording; scope must be verified |
| body cue at p. 8 | The inconsistency of multi-view keypoints in the "w/o Fusion" setting results in a serious performance drop (2.42% lower ... | reported limitation/failure wording; scope must be verified |

- Explicit body limitations and domain stress tests are kept separate; an unreported failure is not inferred from a keyword.

## Position in the Robotics Loop

mobile_manipulation writing domain maps to observation -> state/world model -> task and motion decision -> policy/control -> feedback. Evidence interface anchors: p. 4 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction). The downstream handoff is claimed only when the body describes it.

## Verification Questions

- **Evidence anchors reviewed:** problem p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), interface p. 4 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), objective p. 5 (4 Approach), p. 6 (4 Approach), p. 6 (4 Approach), p. 7 (4 Approach), p. 7 (4 Approach), p. 13 (A.3 Training Details).
- Which exact equation or algorithm defines the state, transition/observation model, objective and constraints?
- What are the observation frame, state memory, output/action frame, horizon and termination rule?
- Which assumption is explicitly stated by the authors, and which is only a reproduction stress test?
- Does the evaluation measure the stated target, or only an upstream proxy?
