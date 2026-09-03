# Learning Geometric Reasoning Networks For Robot Task And Motion Planning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=ajxAJ8GUX4.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/112460. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: not duplicated here when not verified in the registry source
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Robotics, Graph Reasoning
- Official paper: https://openreview.net/forum?id=ajxAJ8GUX4
- Full-text retrieval: https://chatpaper.com/api/v1/articles/download/112460
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, action feasibility prediction presents several challenges.를 문제로 두고, The contributions of this paper are threefold: (1) We propose a novel GNN-based model for efficient and accurate action and grasp feasibility prediction in complex 3D environments.를 통해 observation-to-action closed loop의 한 지점을 바꾼다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Task and Motion Planning (TAMP) is a computationally challenging robotics problem due to the tight coupling of discrete symbolic planning and continuous geometric planning of ...
- **p. 1 / ABSTRACT - extractive body cue:** In particular, planning manipulation tasks in complex 3D environments leads to a large number of costly geometric planner queries to verify the feasibility of considered ...
- **p. 1 / ABSTRACT - extractive body cue:** To address this issue, we propose Geometric Reasoning Networks (GRN), a graph neural network (GNN)-based model for action and grasp feasibility prediction, designed to significantly ...
- **p. 1 / ABSTRACT - extractive body cue:** Moreover, we introduce two key interpretability mechanisms: inverse kinematics (IK) feasibility prediction and grasp obstruction (GO) estimation.
- **p. 1 / ABSTRACT - extractive body cue:** These modules not only improve feasibility predictions accuracy, but also explain why certain actions or grasps are infeasible, thus allowing a more efficient search for ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** However, action feasibility prediction presents several challenges.
- **p. 3 / 1 INTRODUCTION - extractive body cue:** These methods, however, lack interpretability and can not provide feedback on why actions are infeasible.

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** The contributions of this paper are threefold: (1) We propose a novel GNN-based model for efficient and accurate action and grasp feasibility prediction in complex ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** To address these limitations, we propose a novel approach that leverages a GNN-based model for robot action and grasp feasibility prediction.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Our method constructs a graph representation of 3D environments, where fixed and movable objects are represented as nodes, and edges capture spatial relationships and interaction ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** (3) We provide comprehensive experiments showcasing our method's state-of-the-art (SOTA) performance, including evaluations of its interpretability and generalization capabilities.
- **p. 4 / 1 INTRODUCTION - extractive body cue:** In summary, the task at hand is to learn two classification functions fF , fκ, and a regression function fρ s.t.:  Fa FG  ...
- **p. 14 / A IMPLEMENTATION DETAILS - extractive body cue:** Exceptionally, when training on the PR2-3D-4 dataset, we use a hidden size of 256 for the GO module as it yields better results.
- **p. 14 / A IMPLEMENTATION DETAILS - extractive body cue:** During the pre-training stage, each module is trained for 100 epochs.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | In summary, the task at hand is to learn two classification functions fF , fκ, and a regression function fρ s.t.:  Fa FG  = fF (O, E, κG, ρG) where ... | image/video, language instruction, proprioception과 history | p. 4 (1 INTRODUCTION), p. 1 (1 INTRODUCTION) |
| State/latent | summary, task, hand, learn, classification, functions, regression, function, where, GEOMETRIC, REASONING, NETWORKS | language-grounded task state와 action-policy context | p. 4 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 6 (1 INTRODUCTION) |
| Output/action | Task and Motion Planning (TAMP) (Garrett et al., 2021) is a robotics problem in which the goal is to find a sequence of robot actions and their corresponding motions to transition an ... | continuous action, pose 또는 action chunk | p. 1 (1 INTRODUCTION), p. 6 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Objective/outcome | The total inference time of GRN is 5.5 ms in average, with the most significant portion spent on scene graph construction with an average time cost of 3 ms. | instruction following, task success, generalization과 latency | p. 14 (A IMPLEMENTATION DETAILS), p. 14 (A IMPLEMENTATION DETAILS) |

## Main Claims and Actual Contribution

- **p. 2 / 1 INTRODUCTION - extractive body cue:** The contributions of this paper are threefold: (1) We propose a novel GNN-based model for efficient and accurate action and grasp feasibility prediction in complex ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** To address these limitations, we propose a novel approach that leverages a GNN-based model for robot action and grasp feasibility prediction.
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Our method constructs a graph representation of 3D environments, where fixed and movable objects are represented as nodes, and edges capture spatial relationships and interaction ...
- **p. 2 / 1 INTRODUCTION - extractive body cue:** (3) We provide comprehensive experiments showcasing our method's state-of-the-art (SOTA) performance, including evaluations of its interpretability and generalization capabilities.
- **p. 4 / 1 INTRODUCTION - extractive body cue:** In summary, the task at hand is to learn two classification functions fF , fκ, and a regression function fρ s.t.:  Fa FG  ...
- **p. 9 / 6 RESULTS - extractive body cue:** The results show that GRN achieves a better performance than the state-of-the-art on robots with various kinematics.
- **p. 8 / 6 RESULTS - extractive body cue:** This allows our model to achieve an F1 score up to 10.3% higher than other GNN-based baselines on action feasibility prediction, and up to 21.8% ...
- **p. 9 / 6 RESULTS - extractive body cue:** Moreover, the improved performance obtained using EGAT instead of classical GAT Veliˇckovi´c et al.

- Claims are retained as body cues; exact percentages and table values must be read at the cited result anchor.

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (6 RESULTS), p. 8 (6 RESULTS) |
| Embodiment/environment | Panda-3D-4: This is dataset is composed of 3D environments containing 4 movable objects, 1 to 4 structures and 0 to 4 obstacles and is annotated using a Panda robot. | hardware/simulator version and reset protocol | p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS) |
| Dataset/benchmark | This is due to the smaller number of training data of the PR2 dataset and the harder kinematics of the PR2 robot. | role, split, size and leakage | p. 7 (5 EXPERIMENTS), p. 7 (5 EXPERIMENTS), p. 9 (6 RESULTS), p. 10 (6 RESULTS) |
| Metric | Comparing the standard deviations across F1 scores of each grasp type shows that our proposed method has a more consistent performance across the different grasp types than other models. | definition, denominator, direction and uncertainty | p. 8 (6 RESULTS), p. 8 (5 EXPERIMENTS), p. 9 (6 RESULTS) |
| Baseline/ablation | 6.1 COMPARISON TO PRIOR WORK Table 1 shows that our proposed model outperforms all prior works on both action feasibility and grasp types feasibility predictions, and on all datasets. | fair input/data/compute/action matching | p. 8 (6 RESULTS), p. 7 (5 EXPERIMENTS), p. 9 (6 RESULTS) |

## Explicit Limitations and Failure Boundary

- **p. 16 / Figure/Table caption - extractive body cue:** Figure 5: Annotations statistics for the Panda-3D-4 training set. (a) Number of feasible and infeasi- ble actions (b) Number of feasible and infeasi- ble cases ...
- **p. 8 / 6 RESULTS - extractive body cue:** CNN-based methods, DVH and AGFP-Net, fall short compared to our approach, with a difference in F1 score on the Panda-3D-4 of 10% (resp.
- **p. 7 / 5 EXPERIMENTS - extractive body cue:** Feasibility-GCN (F-GCN): This baseline uses the same scene representation as F-GAT, except that GAT is replaced with a Graph Convolution Network (GCN), which does not ...
- **p. 10 / 6 RESULTS - extractive body cue:** Future work will include graph pooling layers to evaluate motion infeasibility across the entire scene graph.
- **p. 10 / 6 RESULTS - extractive body cue:** 7 DISCUSSION AND FUTURE WORK In this work, we propose a framework for action and grasp feasibility prediction in 3D environments.
- **p. 8 / 6 RESULTS - extractive body cue:** Indeed, image-based scene representation suffers from occlusions due to the 3D nature of the environment, resulting in inaccurate predictions for occluded objects.
- **p. 22 / Figure/Table caption - extractive body cue:** Table 7: Performance of GRN on the Panda-3D-4 test set with different levels of noise. No Noise 1cm, 1° 2cm, 2° Action (F1) 0.939 0.912 ...

## Why Read It

VLA and generalist robot policies의 vla 문제를 이해하기 위해 읽는다. 본문은 However, action feasibility prediction presents several challenges.를 문제로 두고, The contributions of this paper are threefold: (1) We propose a novel GNN-based model for efficient and accurate action and grasp feasibility prediction in complex 3D environments.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 1 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 14 (A IMPLEMENTATION DETAILS) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
