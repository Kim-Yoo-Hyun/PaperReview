# MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.mlr.press/v305/wu25c.html.
> PDF retrieval source: https://raw.githubusercontent.com/mlresearch/v305/main/assets/wu25c/wu25c.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / CoRL
- Authors: not duplicated here when not verified in the registry source
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: REFERENCE
- Tags: Navigation, mobile manipulation, VLM
- Official paper: https://proceedings.mlr.press/v305/wu25c.html
- Full-text retrieval: https://raw.githubusercontent.com/mlresearch/v305/main/assets/wu25c/wu25c.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (16 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Locomotion, whole-body, mobile manipulation, and humanoids의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 Get the Water Cook Food Pick up the Fruit Mobile Trajectory Arm Trajectory Fixed-base Manipulation MoTo AnyGrasp OpenVLA RDT-1B iDP3 Figure 1: MoTo can be plugged into any fixed-base manipulation model and ...를 문제로 두고, In this paper, we propose to solve the problem of mobile manipulation with an interaction-aware navigation policy, namely Move and Touch (MoTo).를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Mobile manipulation is the fundamental challenge for robotics in assisting humans with diverse tasks and environments in everyday life.
- **p. 1 / Abstract - extractive body cue:** Conventional mobile manipulation approaches often struggle to generalize across different tasks and environments due to the lack of large-scale training.
- **p. 1 / Abstract - extractive body cue:** However, recent advances in manipulation foundation models demonstrate impressive generalization capability on a wide range of fixed-base manipulation tasks, which are still limited to a ...
- **p. 1 / Abstract - extractive body cue:** Therefore, we devise a plug-in module named MoTo, which can be combined with any off-the-shelf manipulation foundation model to empower them with mobile manipulation ability.
- **p. 1 / Abstract - extractive body cue:** Specifically, we propose an interactionaware navigation policy to generate robot docking points for generalized mobile manipulation.
- **p. 2 / 1 Introduction - extractive body cue:** Get the Water Cook Food Pick up the Fruit Mobile Trajectory Arm Trajectory Fixed-base Manipulation MoTo AnyGrasp OpenVLA RDT-1B iDP3 Figure 1: MoTo can be ...
- **p. 1 / 1 Introduction - extractive body cue:** However, the requirements to perform diverse tasks in unstructured environments (e.g., assisting humans in their daily lives) present significant challenges.

## Core Idea

- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we propose to solve the problem of mobile manipulation with an interaction-aware navigation policy, namely Move and Touch (MoTo).
- **p. 3 / 1 Introduction - extractive body cue:** Inspired by ReKep, we propose a multi-view voting strategy to generate scene-level interaction keypoints to fine-grain guide mobile manipulation trajectory generation.
- **p. 5 / 4 Approach - extractive body cue:** Therefore, we propose a two-stage VLM-based method to generate keypoints for an image, which is divided into keypoint proposal stage and keypoint selection stage.
- **p. 3 / 1 Introduction - extractive body cue:** With the fast development of manipulation foundation models [37, 11, 12, 38], we believe this assumption is reasonable and feasible.
- **p. 6 / 4 Approach - extractive body cue:** Firstly, extracting the wrist keypoint from the RGB-D observation sw t , then projecting it to 3D space using Et.
- **p. 5 / 4 Approach - extractive body cue:** VLM(Tk, {Ik 1 , ..., Ik m}) generates target keypoint proposals in different images, which are then aggregated with a voting module V.
- **p. 5 / 4 Approach - extractive body cue:** Current segmentation models can only segment a laptop into screen and keyboard, and a table into surface and legs, which cannot provide detailed, actionable locations.
- **p. 7 / 4 Approach - extractive body cue:** Specifically, we generate initial solution proposals for the next time step from the search space and calculate the cost relative to the optimization objective for ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Based on robot scanning RGB-D observation to get 3D scene point clouds and graphs, we utilize VLM and multi-view consistency voting to get interaction keypoints, and generate mobile manipulation trajectories via proposed ... | egocentric RGB-D, language/task goal, base-arm proprioception | p. 4 (1 Introduction), p. 2 (1 Introduction) |
| State/latent | robot, scanning, RGB-D, observation, scene, point, clouds, graphs, utilize, VLM, multi-view, consistency | map/object/contact state와 base-arm coordination decision | p. 4 (1 Introduction), p. 2 (1 Introduction), p. 2 (1 Introduction) |
| Output/action | In this paper, we propose to solve the problem of mobile manipulation with an interaction-aware navigation policy, namely Move and Touch (MoTo). | base motion plus arm/gripper action | p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction) |
| Objective/outcome | Therefore, the robot's action (abase t , {aarm t }) can be solved as an optimization problem, which aims to minimize the distance between TK and AK as well as following several ... | long-horizon task success, reachability, collision과 recovery | p. 5 (4 Approach), p. 7 (4 Approach), p. 7 (4 Approach) |

## Main Claims and Actual Contribution

- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we propose to solve the problem of mobile manipulation with an interaction-aware navigation policy, namely Move and Touch (MoTo).
- **p. 3 / 1 Introduction - extractive body cue:** Inspired by ReKep, we propose a multi-view voting strategy to generate scene-level interaction keypoints to fine-grain guide mobile manipulation trajectory generation.
- **p. 5 / 4 Approach - extractive body cue:** Therefore, we propose a two-stage VLM-based method to generate keypoints for an image, which is divided into keypoint proposal stage and keypoint selection stage.
- **p. 3 / 1 Introduction - extractive body cue:** With the fast development of manipulation foundation models [37, 11, 12, 38], we believe this assumption is reasonable and feasible.
- **p. 8 / 5 Experiment - extractive body cue:** All methods are run 10 times on the three types of mobile manipulation tasks, where the dots represent the performance of each test (Best view ...
- **p. 7 / 5 Experiment - extractive body cue:** As shown in Table 1, Home-Robot w/ MoTo outperforms Home-Robot (RL), achieving a 3.52% higher overall success rate.
- **p. 8 / 5 Experiment - extractive body cue:** Since L3MVN only ensures proximity to the target while ignoring the feasibility of subsequent manipulations, it yields only a marginal overall success rate gain of ...
- **p. 7 / 5 Experiment - extractive body cue:** The similar success rates in stages FindObj and Pick are due to MoTo's focus on interaction-aware navigation, which is invoked only after finding a container ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 8 (5 Experiment), p. 7 (5 Experiment) |
| Embodiment/environment | The OVMM benchmark consists of 60 extensive indoor scenes and contains more than 18k 3D models of everyday objects.OVMM utilizes Hello Robot as an agent to perform the "Move a target object ... | hardware/simulator version and reset protocol | p. 13 (A.1 Simulator Experiment), p. 13 (A.2 Real World Experiment) |
| Dataset/benchmark | Avg "Bring me food." "Serve me water." "Prepare a meal." 0 0.2 0.4 0.6 0.8 1 Success Rate Avg "Bring me food." "Serve me water." "Prepare a meal." 0 0.2 0.4 0.6 ... | role, split, size and leakage | p. 13 (A.1 Simulator Experiment), p. 13 (A.2 Real World Experiment), p. 8 (5 Experiment), p. 7 (5 Experiment) |
| Metric | All methods are run 10 times on the three types of mobile manipulation tasks, where the dots represent the performance of each test (Best view in color). success rate further improves by ... | definition, denominator, direction and uncertainty | p. 8 (5 Experiment), p. 8 (5 Experiment), p. 7 (5 Experiment) |
| Baseline/ablation | 5.1 Comparison with State-of-the-art Methods Table 1 demonstrates the performance of MoTo on the OVMM [18] validation set compared to the baseline, decomposing it into four sequential stages: finding the target (FindObj), ... | fair input/data/compute/action matching | p. 7 (5 Experiment), p. 7 (5 Experiment), p. 8 (5 Experiment) |

## Explicit Limitations and Failure Boundary

- **p. 16 / Figure/Table caption - extractive body cue:** Figure 6: Visualization results for keypoint generation. MoTo selects keypoint proposals (red points) from multi-views, projects them into 3D space and votes to generate keypoints ...
- **p. 16 / Figure/Table caption - extractive body cue:** Figure 7: Failure Cases in real-world experiments. D.1 Manipulation Visualization Figure 6 demonstrates the scene keypoint generation and mobile trajectory in task "Serve me water". ...
- **p. 8 / 5 Experiment - extractive body cue:** 5.3 Real World Experiments The OVMM baseline cannot be directly deployed in the real world due to the sim-to-real gap.
- **p. 8 / 5 Experiment - extractive body cue:** The inconsistency of multi-view keypoints in the "w/o Fusion" setting results in a serious performance drop (2.42% lower success rate compared to Single View), because ...

## Why Read It

Locomotion, whole-body, mobile manipulation, and humanoids의 mobile_manipulation 문제를 이해하기 위해 읽는다. 본문은 Get the Water Cook Food Pick up the Fruit Mobile Trajectory Arm Trajectory Fixed-base Manipulation MoTo AnyGrasp OpenVLA RDT-1B iDP3 Figure 1: MoTo can be plugged into any fixed-base manipulation model and ...를 문제로 두고, In this paper, we propose to solve the problem of mobile manipulation with an interaction-aware navigation policy, namely Move and Touch (MoTo).를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 1 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 3 (1 Introduction), p. 6 (4 Approach) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
