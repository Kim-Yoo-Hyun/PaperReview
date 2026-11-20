# Multi-Robot Motion Planning with Diffusion Models

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://openreview.net/forum?id=AUCYptvAf3.
> PDF retrieval source: https://arxiv.org/pdf/2410.03072. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / ICLR
- Authors: Yorai Shaoul, Itamar Mishani, Shivam Vats, Jiaoyang Li, Maxim Likhachev
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: Robotics, multi-robot, motion planning, diffusion model
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/eee6efe709623f36483e3fbb0bb513dd-Abstract-Conference.html
- Full-text retrieval: https://arxiv.org/pdf/2410.03072
- Code/Project: not identified
- Paper type: system
- Source audit: full-text PDF body checked on 2026-09-03 (21 pages; PyMuPDF text; title-token overlap first two pages=1.0)

> DOC-QA2 targeted source review: 2026-10-23; PDF pp. 4. 손상 구간·직접 연결된 표 분류만 원문 이미지와 대조했다. 전체 주장 정독·실험 검증·reading status 승격을 뜻하지 않는다. [URL·PDF hash·수정 기록](../../../work/sources/pdf_note_review_followup_2026-10-23.json).

## Why This Paper Is Here

MMD는 단일 로봇 데이터로 학습한 확산 모델을 조합해 여러 로봇의 장시간 경로를 계획한다.

## Problem and Motivation

- **p. 1 / ABSTRACT - extractive body cue:** Diffusion models have recently been successfully applied to a wide range of robotics applications for learning complex multi-modal behaviors from data.
- **p. 1 / ABSTRACT - extractive body cue:** However, prior works have mostly been confined to single-robot and small-scale environments due to the high sample complexity of learning multi-robot diffusion models.
- **p. 1 / ABSTRACT - extractive body cue:** In this paper, we propose a method for generating collision-free multi-robot trajectories that conform to underlying data distributions while using only single-robot data.
- **p. 1 / ABSTRACT - extractive body cue:** Our algorithm, Multi-robot Multi-model planning Diffusion (MMD), does so by combining learned diffusion models with classical search-based techniques-generating data-driven motions under collision constraints.
- **p. 1 / ABSTRACT - extractive body cue:** Scaling further, we show how to compose multiple diffusion models to plan in large environments where a single diffusion model fails to generalize well.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** Importantly, our approach calls for learning only single-robot diffusion models, which does away with the difficulty of obtaining multi-robot interaction data and breaks the curse ...
- **p. 1 / 1 INTRODUCTION - extractive body cue:** Multi-robot motion planning (MRMP) is a fundamental challenge in many real-world applications where teams of robots have to work in close proximity to each other ...

## Core Idea

- **p. 2 / 1 INTRODUCTION - extractive body cue:** Our contributions in this paper are threefold: (1) We propose a novel data-efficient framework for multirobot diffusion planning inspired by constraint-based search algorithms.
- **p. 2 / 1 INTRODUCTION - extractive body cue:** In this paper, we propose a data-efficient and scalable multi-robot diffusion planning algorithm, Multi-robot Multi-model planning Diffusion (MMD), that addresses both these challenges by combining ...
- **p. 3 / 3 METHOD - extractive body cue:** Next, we introduce five MMD algorithms, each inspired by a MAPF algorithm regarding constraint placement and timing.
- **p. 3 / 3 METHOD - extractive body cue:** We present Multi-robot Multi-model planning Diffusion (MMD), an algorithm for flexibly scaling diffusion planning to multiple robots and long horizons using only single-robot data.
- **p. 4 / 3 METHOD - extractive body cue:** We propose five MMD variants, each inspired by a state-of-the-art search algorithm.
- **p. 14 / A.1.1 BEYOND FULL-HORIZON PLANNING - extractive body cue:** While full-horizon planners first generate a set of trajectories for all robots and then robots execute them as prescribed, windowed algorithms instead ask each robot ...
- **p. 6 / 3 METHOD - extractive body cue:** (6) In practice, MMD ensures proper sequencing of the L local diffusion models by introducing constraints requiring the last state of the trajectory from model ...
- **p. 4 / 3 METHOD - extractive body cue:** 2In MMD, we use the search or prioritization logic found in MAPF algorithms for placing "strong" constraints on diffusion models, while all other aspects of ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Algorithm 1 입력은 robot별 start state·goal conditions·single-robot diffusion model이며 출력은 robot별 trajectories다. MMD-CBS와 색으로 구분된 PP/ECBS variant의 제약·return 위치를 혼합하지 않는다. | Starts / goal conditions / per-robot diffusion models | PDF p. 4 Algorithm 1 |
| State/latent | Colored, lines, only, MMD-PP, MMD-ECBS, Input, Starts, goal, conditions, single-robot, diffusion, models | path, trajectory, symbolic state 또는 task-motion decision | p. 4 (3 METHOD), p. 6 (3 METHOD), p. 9 (3 METHOD) |
| Output/action | Each experiment with n robots begins by randomly picking start and goal states on a map for various algorithms to compute valid trajectories τ (or MAPF paths Π) between. | feasible action sequence 또는 minimum-cost plan | p. 6 (3 METHOD), p. 9 (3 METHOD), p. 4 (3 METHOD) |
| Objective/outcome | Each local model is trained to capture a particular motion pattern, i.e., a trajectory distribution generated by a hidden cost function defined by a specific task dataset. | path cost, goal reachability, feasibility와 computation | p. 5 (3 METHOD), p. 6 (3 METHOD), p. 5 (3 METHOD) |

## Main Claims and Actual Contribution

- 여러 로봇과 구간의 경로 분포를 연결한다.
- 충돌 제약을 다루는 탐색 전략들을 같은 계획 문제에서 비교한다.

[저자 원문](https://proceedings.iclr.cc/paper_files/paper/2025/hash/eee6efe709623f36483e3fbb0bb513dd-Abstract-Conference.html)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 8 (Figure/Table caption), p. 15 (Figure/Table caption) |
| Embodiment/environment | Importantly, each dataset trajectory respects the motion pattern dictated by the map within which it is embedded. | hardware/simulator version and reset protocol | p. 20 (A.7 TRAINING AND DATASET GENERATION DETAILS), p. 20 (A.7 TRAINING AND DATASET GENERATION DETAILS) |
| Dataset/benchmark | We keep the number of robots low for clarity. | role, split, size and leakage | p. 20 (A.7 TRAINING AND DATASET GENERATION DETAILS), p. 20 (A.7 TRAINING AND DATASET GENERATION DETAILS), p. 16 (A.3 ADDITIONAL QUALITATIVE RESULTS), p. 17 (A.3 ADDITIONAL QUALITATIVE RESULTS) |
| Metric | Figure 3: Analysis of success rates and data adherence scores, in randomly generated planning queries, of all MMD instantiations and a MAPF method with and without a learned cost map. The left ... | definition, denominator, direction and uncertainty | p. 8 (Figure/Table caption), p. 15 (Figure/Table caption), p. 6 (Figure/Table caption) |
| Baseline/ablation | Figure 2: A comparison between MMD and "composite" diffusion models that generate trajectories for all agents at once. We observed consistent performance from MMD but a sharp decrease for the baseline, unable ... | fair input/data/compute/action matching | p. 6 (Figure/Table caption), p. 8 (Figure/Table caption), p. 15 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 10 / 6 CONCLUSION - extractive body cue:** Currently, MMD focuses on coordinating robots, seeking to produce collision-free data-driven trajectories.
- **p. 10 / 6 CONCLUSION - extractive body cue:** In this paper, we present MMD, a multi-robot motion planner that learns to generate smooth collision-free trajectories for dozens of robots in complex environments.
- **p. 14 / A.1 ADDITIONAL ALGORITHMIC DISCUSSION - extractive body cue:** Resembling their outcomes, we also observed a significant runtime improvement between prioritizing CT nodes based on their geometric quality and their collision count.
- **p. 14 / A.1 ADDITIONAL ALGORITHMIC DISCUSSION - extractive body cue:** Once the batch is generated, MMD iterates over the new resulting trajectories N.τ i and marks the one with the least collisions as the representative ...
- **p. 9 / Figure/Table caption - extractive body cue:** Figure 4: Scalability tests in high-congestion free-space MRMP. Circle (top row) asks robots to swap positions between opposite points on the perimeter. Weave (below), asks ...
- **p. 4 / Figure/Table caption - extractive body cue:** Figure 1: An illustration of how MMD- CBS generates collision-free trajectories with constrained diffusion models. 3.1 CONSTRAINTS IN DIFFUSION MODELS An intuitive and effective constraint ...
- **p. 20 / A.7 TRAINING AND DATASET GENERATION DETAILS - extractive body cue:** There, each data point is one, single-robot, trajectory from a random collision-free start configuration to a random collision-free goal configuration.

## Why Read It

Planning and control의 planning 문제를 이해하기 위해 읽는다. 본문은 Importantly, our approach calls for learning only single-robot diffusion models, which does away with the difficulty of obtaining multi-robot interaction data and breaks the curse of dimensionality.를 문제로 두고, Our contributions in this paper are threefold: (1) We propose a novel data-efficient framework for multirobot diffusion planning inspired by constraint-based search algorithms.를 통해 observation-to-action closed loop의 한 지점을 바꾼다. Revisit p. 2 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 1 (1 INTRODUCTION), p. 2 (1 INTRODUCTION), p. 3 (1 INTRODUCTION), p. 14 (A.1.1 BEYOND FULL-HORIZON PLANNING) to check whether the claimed mechanism survives the failure regime and evaluation boundary recorded above.
