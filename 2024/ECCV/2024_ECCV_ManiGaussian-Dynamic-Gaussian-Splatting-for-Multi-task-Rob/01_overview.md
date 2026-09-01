# ManiGaussian: Dynamic Gaussian Splatting for Multi-task Robotic Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5194_ECCV_2024_paper.php.
> PDF retrieval source: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05194.pdf. Reading tracker status/evidence was not changed.

- Year/Venue: 2024 / ECCV
- Authors: not duplicated here when not verified in the registry source
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, Gaussian Splatting
- Official paper: https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5194_ECCV_2024_paper.php
- Full-text retrieval: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05194.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-02 (19 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

Manipulation, contact, tactile, and dexterity의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To address the challenges, previous arts have made great progress in general manipulation policy learning, which can be divided into two categories including perceptive methods and generative methods.를 문제로 두고, Our contributions can be summarized as follows: - We propose a dynamic Gaussian Splatting framework to learn the scenelevel spatiotemporal dynamics in general robotic manipulation tasks, so that the robotic agent can ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / 1 Introduction - extractive body cue:** Designing autonomous agents for language-conditioned manipulation tasks [2, 11, 28, 30, 57, 58, 60, 61, 75] has been highly desired in the pursuit of artificial ...
- **p. 1 / 1 Introduction - extractive body cue:** In realistic deployment, intelligent robots are usually required to deal with unseen scenarios in novel tasks.
- **p. 1 / 1 Introduction - extractive body cue:** Therefore, comprehending complex 3D structures in the deployment scenes is necessary for the robots to achieve high task success rates across diverse manipulation tasks. ⋆B ...
- **p. 2 / 1 Introduction - extractive body cue:** Lu et al.  Previous ManiGaussian Initial state ... "Stack two rose blocks" 𝒕 𝒕 𝒕+ 𝟏 ...
- **p. 2 / 1 Introduction - extractive body cue:** Representation Gaussian Point Human Instruction Fig.
- **p. 2 / 1 Introduction - extractive body cue:** To address the challenges, previous arts have made great progress in general manipulation policy learning, which can be divided into two categories including perceptive methods ...
- **p. 2 / 1 Introduction - extractive body cue:** However, the perceptive methods heavily rely on multi-view or gripper-mounted cameras to cover the whole workbench to deal with the occlusion problem within unstructured environments, ...

## Core Idea

- **p. 3 / 1 Introduction - extractive body cue:** Our contributions can be summarized as follows: - We propose a dynamic Gaussian Splatting framework to learn the scenelevel spatiotemporal dynamics in general robotic manipulation ...
- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we propose a ManiGaussian method that leverages a dynamic Gassuain Splatting framework for multi-task robotic manipulation.
- **p. 2 / 1 Introduction - extractive body cue:** Different from conventional methods which only focus on semantic representation, our method mines the scene-level spatiotemporal dynamics via future scene reconstruction.
- **p. 3 / 1 Introduction - extractive body cue:** We evaluate our ManiGaussian method on the RLBench dataset [26] with 10 tasks and 166 variants, where our method outperforms the state-of-the-art multi-task robotic manipulation ...
- **p. 5 / 3 Approach - extractive body cue:** In this section, we first briefly introduce preliminaries on the problem formulation (Section 3.1), and then we present an overview of our pipeline (Section 3.2).
- **p. 8 / 3 Approach - extractive body cue:** More specifically, the Gaussian world model contains a representation network qϕ that learns high-level visual features with rich semantics for the input observation, a Gaussian ...
- **p. 6 / 3 Approach - extractive body cue:** 3.3 Dynamic Gaussian Splatting for Robotic Manipulation In order to capture the scene-level dynamics for general manipulation tasks, we propose a dynamic Gaussian Splatting framework ...
- **p. 10 / 3 Approach - extractive body cue:** In training, we set a warm-up phase that freezes the deformation predictor to learn a stable representation model and a Gaussian regressor during the first ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | To learn the manipulation policy effectively, expert demonstrations as offline datasets are provided for imitation learning, where the sample triplets contain the visual input, language instruction and expert actions. | RGB-D, image set, point cloud, depth와 camera pose | p. 5 (3 Approach), p. 5 (3 Approach) |
| State/latent | learn, manipulation, policy, effectively, expert, demonstrations, offline, datasets, provided, imitation, learning, where | geometry, map, object/relationship state | p. 5 (3 Approach), p. 5 (3 Approach), p. 8 (3 Approach) |
| Output/action | Based on the visual input o(t) and the language instructions, the agent is required to generate the optimal action for the robot arm and grippers a(t) = (a(t) trans, a(t) rot, a(t) ... | point map, pose, scene graph, affordance 또는 query result | p. 5 (3 Approach), p. 8 (3 Approach), p. 8 (3 Approach) |
| Objective/outcome | We employ a multi-modal transformer PerceiverIO [25] to infer the selection probability of different action candidates based on the Gaussian parameters and the human language instructions, and leverage the cross-entropy loss CE ... | geometric accuracy, semantic consistency와 planning/manipulation utility | p. 9 (3 Approach), p. 8 (3 Approach), p. 9 (3 Approach) |

## Main Claims and Actual Contribution

- **p. 3 / 1 Introduction - extractive body cue:** Our contributions can be summarized as follows: - We propose a dynamic Gaussian Splatting framework to learn the scenelevel spatiotemporal dynamics in general robotic manipulation ...
- **p. 2 / 1 Introduction - extractive body cue:** In this paper, we propose a ManiGaussian method that leverages a dynamic Gassuain Splatting framework for multi-task robotic manipulation.
- **p. 2 / 1 Introduction - extractive body cue:** Different from conventional methods which only focus on semantic representation, our method mines the scene-level spatiotemporal dynamics via future scene reconstruction.
- **p. 3 / 1 Introduction - extractive body cue:** We evaluate our ManiGaussian method on the RLBench dataset [26] with 10 tasks and 166 variants, where our method outperforms the state-of-the-art multi-task robotic manipulation ...
- **p. 5 / 3 Approach - extractive body cue:** In this section, we first briefly introduce preliminaries on the problem formulation (Section 3.1), and then we present an overview of our pipeline (Section 3.2).
- **p. 11 / 4 Experiments - extractive body cue:** Our method achieves the best performance with an average success rate of 44.8%, which is state-of-the-art, outperforming the previous arts including both perceptive and generative-based ...
- **p. 12 / 4 Experiments - extractive body cue:** Though the dynamic loss may slightly impact short-term results due to the balance of different loss items, it significantly improves overall performance.
- **p. 10 / 4 Experiments - extractive body cue:** The diversity of these tasks requires the agent to acquire generalizable knowledge about the intrinsical scene-level spatial-temporal dynamics for manipulation, rather than solely relying on ...

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 11 (4 Experiments), p. 12 (4 Experiments) |
| Embodiment/environment | On the contrary, our ManiGaussian learns the scene dynamics with the proposed dynamic Gaussian Splatting framework, so that the robotic agent can complete human instructions with accurate action prediction in unstructured environments. | hardware/simulator version and reset protocol | p. 11 (4 Experiments), p. 10 (4 Experiments) |
| Dataset/benchmark | The evaluation metric is the task success rate, which measures the percentage of completed episodes. | role, split, size and leakage | p. 11 (4 Experiments), p. 10 (4 Experiments), p. 10 (4 Experiments), p. 11 (4 Experiments) |
| Metric | Our method achieves the best performance with an average success rate of 44.8%, which is state-of-the-art, outperforming the previous arts including both perceptive and generative-based methods by a sizable margin. | definition, denominator, direction and uncertainty | p. 11 (4 Experiments), p. 12 (4 Experiments), p. 10 (4 Experiments) |
| Baseline/ablation | Fig. 4: Case Study. The red mark signifies the pose deviates severely from the ex- pert demonstration, whereas the green mark indicates that the pose aligns with the expert trajectory. Our ManiGaussian ... | fair input/data/compute/action matching | p. 13 (Figure/Table caption), p. 11 (4 Experiments), p. 12 (4 Experiments) |

## Explicit Limitations and Failure Boundary

- **p. 14 / 5 Conclusion - extractive body cue:** The limitations stem from the necessity of multiple view supervision with camera calibration for the Gaussian Splatting framework.
- **p. 2 / Figure/Table caption - extractive body cue:** Fig. 1: Consider the human instruction "stack two rose blocks", where the task is con- sidered successful if two rose blocks are stacked upon the ...
- **p. 14 / 4 Experiments - extractive body cue:** First, based on the front view observation where the gripper shape cannot be seen, our ManiGaussian offers superior detail in modeling cubes in novel views.
- **p. 10 / 4 Experiments - extractive body cue:** We evaluated 25 episodes in the testing set for each task to avoid result bias from noise.
- **p. 11 / 4 Experiments - extractive body cue:** However, it ignores the scene-level spatiotemporal dynamics that demonstrate the interaction among objects, and the predicted actions still fail to achieve human goals because of ...
- **p. 11 / 4 Experiments - extractive body cue:** Planning Long Tools Motion Screw Occlusion Average ✗ ✗ ✗ 36.0 2.0 25.3 52.0 4.0 28.0 23.6 ✓ ✗ ✗ 46.0 4.0 52.0 52.0 24.0 ...
- **p. 12 / 4 Experiments - extractive body cue:** Especially, in the tasks that require geometric reasoning such as Occlusion, Tools and Screw, it outperforms the vanilla version by sizable margins, which proves the ...

## Why Read It

Manipulation, contact, tactile, and dexterity의 3d_perception 문제를 이해하기 위해 읽는다. 본문은 To address the challenges, previous arts have made great progress in general manipulation policy learning, which can be divided into two categories including perceptive methods and generative methods.를 문제로 두고, Our contributions can be summarized as follows: - We propose a dynamic Gaussian Splatting framework to learn the scenelevel spatiotemporal dynamics in general robotic manipulation tasks, so that the robotic agent can ...를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 8 (3 Approach), p. 6 (3 Approach), p. 10 (3 Approach) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
