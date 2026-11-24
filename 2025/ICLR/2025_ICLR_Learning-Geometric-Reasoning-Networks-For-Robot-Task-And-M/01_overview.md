# Learning Geometric Reasoning Networks For Robot Task And Motion Planning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://proceedings.iclr.cc/paper_files/paper/2025/hash/561dd71d04695c85e1c0f6a0fbe0bd85-Abstract-Conference.html.
> PDF retrieval source: https://chatpaper.com/api/v1/articles/download/112460. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: Smail Ait Bouhsain, Rachid Alami, Thierry Simeon
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: Robotics, Graph Reasoning
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/561dd71d04695c85e1c0f6a0fbe0bd85-Abstract-Conference.html
- Full-text retrieval: https://proceedings.iclr.cc/paper_files/paper/2025/file/561dd71d04695c85e1c0f6a0fbe0bd85-Paper-Conference.pdf
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (24 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 요약과 핵심 기여 두 개를 각 문장에 연결한 판본에서 확인했다.

> DOC-QA2 targeted source review: 2026-10-23; PDF pp. 4. 손상 구간·직접 연결된 표 분류만 원문 이미지와 대조했다. 전체 주장 정독·실험 검증·reading status 승격을 뜻하지 않는다. [URL·PDF hash·수정 기록](../../../work/sources/pdf_note_review_followup_2026-10-23.json).

## Why This Paper Is Here

GRN은 작업·동작 계획에서 어떤 행동과 파지를 기하학적으로 실행할 수 있는지 예측해 비용이 큰 동작 계획기 호출을 줄인다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/561dd71d04695c85e1c0f6a0fbe0bd85-Paper-Conference.pdf#page=1)

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
- **PDF p. 4, §3 / Eq. (2) (DOC-QA2 원문 대조):** GRN은 feasibility classifier f_F와 IK classifier f_κ, obstruction regressor f_ρ를 학습한다. f_F는 object/environment와 예측 κ_G, ρ_G를 사용해 action·grasp feasibility 벡터 [F_a,F_G]ᵀ를 출력한다.
- **p. 14 / A IMPLEMENTATION DETAILS - extractive body cue:** Exceptionally, when training on the PR2-3D-4 dataset, we use a hidden size of 256 for the GO module as it yields better results.
- **p. 14 / A IMPLEMENTATION DETAILS - extractive body cue:** During the pre-training stage, each module is trained for 100 epochs.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Object O와 environment E의 graph, 그리고 IK/obstruction predictions κ_G·ρ_G | 3D object geometry와 관계 graph; image/language/proprioception template을 제거 | PDF p. 4, Eq. (2), §4.1; DOC-QA2 |
| State/latent | summary, task, hand, learn, classification, functions, regression, function, where, GEOMETRIC, REASONING, NETWORKS | language-grounded task state와 action-policy context | p. 4 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 6 (1 INTRODUCTION) |
| Output/action | Task and Motion Planning (TAMP) (Garrett et al., 2021) is a robotics problem in which the goal is to find a sequence of robot actions and their corresponding motions to transition an ... | continuous action, pose 또는 action chunk | p. 1 (1 INTRODUCTION), p. 6 (1 INTRODUCTION), p. 3 (1 INTRODUCTION) |
| Objective/outcome | The total inference time of GRN is 5.5 ms in average, with the most significant portion spent on scene graph construction with an average time cost of 3 ms. | instruction following, task success, generalization과 latency | p. 14 (A IMPLEMENTATION DETAILS), p. 14 (A IMPLEMENTATION DETAILS) |

## Main Claims and Actual Contribution

- 장면 그래프에서 역기구학의 가능성과 파지를 가로막는 물체를 함께 추정해 후보가 실패할 원인을 계획 탐색에 제공한다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/561dd71d04695c85e1c0f6a0fbe0bd85-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/561dd71d04695c85e1c0f6a0fbe0bd85-Paper-Conference.pdf#page=5)
- 더 복잡한 장면, 다른 물체 모양과 로봇 구성으로 옮겼을 때 예측과 계획 효율을 비교하고 실물 로봇에서도 적용을 평가했다. [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/561dd71d04695c85e1c0f6a0fbe0bd85-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/561dd71d04695c85e1c0f6a0fbe0bd85-Paper-Conference.pdf#page=9) · [PDF 10쪽](https://proceedings.iclr.cc/paper_files/paper/2025/file/561dd71d04695c85e1c0f6a0fbe0bd85-Paper-Conference.pdf#page=10)

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

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 14 (A IMPLEMENTATION DETAILS)이다.
