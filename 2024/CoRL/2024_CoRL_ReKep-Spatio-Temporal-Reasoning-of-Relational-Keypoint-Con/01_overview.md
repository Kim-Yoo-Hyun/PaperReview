# ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (30 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v270/huang25g.html.
> PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v270/main/assets/huang25g/huang25g.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Planning, 3D geometry, Robotics, VLM
- Official paper: https://proceedings.mlr.press/v270/huang25g.html
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v270/main/assets/huang25g/huang25g.pdf
- Code/Project: https://github.com/huangwl18/ReKep
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (30 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, manual annotation is required per task, thus lacking scalability in open-world settings, which we aim to address in this work.를 문제로 두고, Our contributions are summarized as follows: 1) We formulate manipulation tasks as a hierarchical optimization problem with Relational Keypoint Constraints; 2) We devise a pipeline to automatically specify keypoints and constraints usin ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Representing robotic manipulation tasks as constraints that associate the robot and the environment is a promising way to encode desired robot behaviors.
- **p. 1 / Abstract - extractive body cue:** However, it remains unclear how to formulate the constraints such that they are 1) versatile to diverse tasks, 2) free of manual labeling, and 3) ...
- **p. 1 / Abstract - extractive body cue:** In this work, we introduce Relational Keypoint Constraints (ReKep), a visually-grounded representation for constraints in robotic manipulation.
- **p. 1 / Abstract - extractive body cue:** Specifically, ReKep is expressed as Python functions mapping a set of 3D keypoints in the environment to a numerical cost.
- **p. 1 / Abstract - extractive body cue:** We demonstrate that by representing a manipulation task as a sequence of Relational Keypoint Constraints, we can employ a hierarchical optimization procedure to solve for ...
- **p. 3 / 1 Introduction - extractive body cue:** However, manual annotation is required per task, thus lacking scalability in open-world settings, which we aim to address in this work.
- **p. 2 / 1 Introduction - extractive body cue:** However, effectively formulating these constraints for a large variety of real-world tasks presents significant challenges.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are summarized as follows: 1) We formulate manipulation tasks as a hierarchical optimization problem with Relational Keypoint Constraints; 2) We devise a pipeline ...
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we propose Relational Keypoint Constraints (ReKep).
- **p. 4 / 3 Method - extractive body cue:** 2, which consists of three stages: grasp, align, and pour.
- **p. 6 / 3 Method - extractive body cue:** This enables VLM to reason about 3D rotations with arithmetic operations in 3D Cartesian space, effectively circumventing the need for dealing with alternative 3D rotation ...
- **p. 6 / 3 Method - extractive body cue:** Seven tasks are designed to validate different aspects of our system, including in-the-wild specification with commonsense knowledge, multi-stage tasks with spatio-temporal dependencies, bimanual coordination with ...
- **p. 5 / 3 Method - extractive body cue:** 3.4 Keypoint Proposal and ReKep Generation To enable the system to perform tasks in-the-wild given a free-form task instruction, we devise a pipeline using large ...
- **p. 24 / A.8 Implementation Details of Sub-Goal Solver - extractive body cue:** We use sampling-based global optimization Dual Annealing [129] in the first iteration to quickly search the full space, which is followed by a gradient-based local ...
- **p. 22 / A.6 Querying Vision-Language Model - extractive body cue:** For the experiments conducted in this work, we use GPT-4o [6] as it is one of the latest available models at the time of the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Our contributions are summarized as follows: 1) We formulate manipulation tasks as a hierarchical optimization problem with Relational Keypoint Constraints; 2) We devise a pipeline to automatically specify keypoints and constraints usin ... | image/video, language instruction, proprioception과 history | p. 2 (1 Introduction), p. 3 (3 Method) |
| State/latent | contributions, summarized, follows, formulate, manipulation, tasks, hierarchical, optimization, problem, Relational, Keypoint, Constraints | language-grounded task state와 action-policy context | p. 2 (1 Introduction), p. 3 (3 Method), p. 4 (3 Method) |
| Output/action | (4) How to automatically obtain ReKep from RGB-D observations and language instructions (Sec. | continuous action, pose 또는 action chunk | p. 3 (3 Method), p. 4 (3 Method), p. 22 (A.6 Querying Vision-Language Model) |
| Objective/outcome | Namely, for each stage i, the optimization shall find an end-effector pose as next sub-goal, along with its timing, and a sequence of poses egi-1:gi that achieves the sub-goal, subject to the ... | instruction following, task success, generalization과 latency | p. 4 (3 Method), p. 24 (A.8 Implementation Details of Sub-Goal Solver), p. 4 (3 Method) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** Our contributions are summarized as follows: 1) We formulate manipulation tasks as a hierarchical optimization problem with Relational Keypoint Constraints; 2) We devise a pipeline ...
- **p. 2 / 1 Introduction - extractive body cue:** In this work, we propose Relational Keypoint Constraints (ReKep).
- **p. 4 / 3 Method - extractive body cue:** 2, which consists of three stages: grasp, align, and pour.
- **p. 6 / 3 Method - extractive body cue:** This enables VLM to reason about 3D rotations with arithmetic operations in 3D Cartesian space, effectively circumventing the need for dealing with alternative 3D rotation ...
- **p. 6 / 3 Method - extractive body cue:** Seven tasks are designed to validate different aspects of our system, including in-the-wild specification with commonsense knowledge, multi-stage tasks with spatio-temporal dependencies, bimanual coordination with ...
- **p. 7 / 4 Experiments - extractive body cue:** Folding 0/10 4/10 7/10 Total (%) 10.0% 44.3% 68.6% Table 1: Success rate on wheeled singlearm and stationary bimanual platforms.
- **p. 7 / 4 Experiments - extractive body cue:** Folding 0/10 3/10 5/10 Total (%) 6.7% 26.7% 46.7% Table 2: Success rate under external disturbances across both robot platforms.
- **p. 8 / 4 Experiments - extractive body cue:** Garment ReKep sweater shirt hoodie vest dress pants shorts scarf sweater shirt hoodie vest dress pants shorts scarf Total Strategy Success 6/10 4/10 4/10 6/10 ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Embodiment/environment | 5 Conclusion & Limitations In this work, we presented Relational Keypoint Constraints (ReKep), a structural task representation using constraints that operates on semantic keypoints to specify desired relations between robot arms, objec ... | hardware/simulator version and reset protocol | p. 8 (4 Experiments), p. 8 (4 Experiments) |
| Dataset/benchmark | For example, it can formulate correct temporal dependency in multi-stage tasks (e.g., spout needs to be aligned with the cup before pouring), leverage commonsense knowledge (e.g., coke cans should be recycled), and ... | role, split, size and leakage | p. 8 (4 Experiments), p. 8 (4 Experiments), p. 7 (4 Experiments), p. 7 (4 Experiments) |
| Metric | Folding 0/10 4/10 7/10 Total (%) 10.0% 44.3% 68.6% Table 1: Success rate on wheeled singlearm and stationary bimanual platforms. | definition, denominator, direction and uncertainty | p. 7 (4 Experiments), p. 7 (4 Experiments), p. 8 (4 Experiments) |
| Baseline/ablation | Compared to baselines, ReKep can effectively handle core challenges of each task. | fair input/data/compute/action matching | p. 7 (4 Experiments), p. 27 (A.12 Simulation Experiments), p. 7 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 8 / 4 Experiments - extractive body cue:** The optimization module, on the other hand, does not contribute as much to the failures despite given limited time budget, since there often exist many ...
- **p. 19 / Figure/Table caption - extractive body cue:** Figure 7: Stationary Dual-Arm Platform. A.2 Wheeled Single-Arm Platform One of our investigated platform is a Franka arm mounted on a wheeled base built with ...
- **p. 27 / A.11 Extended Discusssions on Limitations - extractive body cue:** Herein we present additional limitations of the existing system.
- **p. 27 / A.11 Extended Discusssions on Limitations - extractive body cue:** Bimanual Coordination: Although we demonstrate the application of ReKep to bimanual manipulation, we also identify several important limitations in this domain.
- **p. 7 / 4 Experiments - extractive body cue:** (3) How do the individual components contribute to the failure cases of the system (Sec.
- **p. 8 / 4 Experiments - extractive body cue:** In this section, we perform an empirical investigation by manually inspecting the failure cases of the experiments reported in Tab.
- **p. 25 / A.9 Implementation Details of Path Solver - extractive body cue:** We ignore the collision calculation with a 5cm radius near the start and the target poses, as this tends to stabilize the solution when solved ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, manual annotation is required per task, thus lacking scalability in open-world settings, which we aim to address in this work.를 문제로 두고, Our contributions are summarized as follows: 1) We formulate manipulation tasks as a hierarchical optimization problem with Relational Keypoint Constraints; 2) We devise a pipeline to automatically specify keypoints and constraints usin ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 3 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 5 (3 Method), p. 24 (A.8 Implementation Details of Sub-Goal Solver) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (30 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However, effectively formulating these constraints for a large variety of real-world tasks presents significant challenges. (p. 2, 1 Introduction).
- **Actual contribution:** Our contributions are summarized as follows: 1) We formulate manipulation tasks as a hierarchical optimization problem with Relational Keypoint Constraints; 2) We devise a pipeline to automatically specify keypoints and ... (p. 2, 1 Introduction).
- **Evaluation boundary:** Folding 0/10 3/10 5/10 Total (%) 6.7% 26.7% 46.7% Table 2: Success rate under external disturbances across both robot platforms. (p. 7, 4 Experiments).
- **Explicit failure boundary:** The optimization module, on the other hand, does not contribute as much to the failures despite given limited time budget, since there often exist many possible solutions for each problem. (p. 8, 4 Experiments).
