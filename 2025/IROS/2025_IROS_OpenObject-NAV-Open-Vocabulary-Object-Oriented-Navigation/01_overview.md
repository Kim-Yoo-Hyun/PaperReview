# OpenObject-NAV: Open-Vocabulary Object-Oriented Navigation Based on Dynamic Carrier-Relationship Scene Graph

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/2409.18743.
> PDF retrieval source: https://arxiv.org/pdf/2409.18743. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2025 / IROS
- Authors: Yujie Tang, Meiling Wang, Yinan Deng, Zibo Zheng, Jiagui Zhong, Tiancheng Liu, Chenjie Zhao, Yufeng Yue
- IROS 출판사 서지는 저자 8명을 기록한다. 요약에 사용한 arXiv v1 표제면에는 6명이 있으며, 게재 서지에 Tiancheng Liu와 Chenjie Zhao가 추가됐다. [출판사 서지](https://api.crossref.org/works/10.1109/iros60139.2025.11247413) · [저자판 표제면](https://arxiv.org/pdf/2409.18743v1#page=1)
- Primary track: Robotics-enabling 3D perception
- Tier: REFERENCE
- Tags: Navigation, Graph Reasoning, semantic
- Official paper: https://arxiv.org/abs/2409.18743
- Venue verification: https://api.crossref.org/works/10.1109/iros60139.2025.11247413
- DOI: https://doi.org/10.1109/iros60139.2025.11247413
- Full-text retrieval: https://arxiv.org/pdf/2409.18743
- Code/Project: not identified
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (7 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

OpenObject-NAV는 자주 옮겨지는 물건과 이를 받치는 가구의 관계를 갱신해 로봇이 이동한 목표를 다시 찾도록 한다. [PDF 1쪽](https://arxiv.org/pdf/2409.18743v1#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** In everyday life, frequently used objects like cups often have unfixed positions and multiple instances within the same category, and their carriers frequently change as ...
- **p. 1 / Abstract - extractive body cue:** As a result, it becomes challenging for a robot to efficiently navigate to a specific instance.
- **p. 1 / Abstract - extractive body cue:** To tackle this challenge, the robot must capture and update scene changes and plans continuously.
- **p. 1 / Abstract - extractive body cue:** However, current object navigation approaches primarily focus on semantic-level and lack the ability to dynamically update scene representation.
- **p. 1 / Abstract - extractive body cue:** This paper captures the relationships between frequently used objects and their static carriers.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, they struggle to represent everyday dynamic environments due to two key challenges.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, they are often limited to searching for semantic-level objects and lack the capability to update scenes.

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** In summary, our contributions are as follows: • We present an adaptable carrier relationship scene graph (CRSG) that primarily describes the dynamic carrier and carried ...
- **p. 3 / III. METHOD - extractive body cue:** The OpenObject-NAV system framework consists of two main modules.
- **p. 1 / I. INTRODUCTION - extractive body cue:** This update enables efficient point-to-point navigation for the third task. dynamic and subject to interference, making it challenging to efficiently and effectively navigate to them.
- **p. 2 / I. INTRODUCTION - extractive body cue:** Based on the CRSG, we designed an object-oriented navigation strategy, modeling the object search process as a Markov Decision Process (MDP) [21].
- **p. 3 / III. METHOD - extractive body cue:** The robot selects the next action at ∈A based on the current state St according to a specific policy π(·) in (8). at = π(St) ...
- **p. 4 / III. METHOD - extractive body cue:** Leveraging the LLM's commonsense understanding of object-carrier relationships (e.g., "a cup is unlikely to be placed on a toilet"), the LLM identifies the carrier object ...
- **p. 2 / III. METHOD - extractive body cue:** Unlike ConceptGraph [19], each instance object Oi ∈O (O is the set of all objects) not only contains a CLIP feature V Fi but also ...
- **p. 4 / III. METHOD - extractive body cue:** The RGB images are processed through CropFormer [38], Tokenize Anything model [35], CLIP [22] and SBERT [36] to obtain instance masks, captions, encoded CLIP features ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The robot selects the next action at ∈A based on the current state St according to a specific policy π(·) in (8). at = π(St) (8) policy π(·): Given current state St ... | camera/depth stream, pose, map와 language goal | p. 3 (III. METHOD), p. 3 (III. METHOD) |
| State/latent | robot, selects, next, action, current, state, according, specific, policy, Given, CRt, CTt | robot pose, free-space/semantic map와 local goal | p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Output/action | We model the exploration of a displaced object as a fixedpolicy Markov decision process (MDP) below. state space S: In the current step t, we define: 1. the robot's pose Lt ∈L, ... | collision-free trajectory 또는 velocity command | p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD) |
| Objective/outcome | The cost function is defined as follows: P L = T X t=1 Length(Lt, Lt+1) (1) Let Lt represent the position of the exploration target at step t, and Length(Lt, Lt+1) denote ... | goal reach, safety, localization error와 replanning latency | p. 2 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD) |

## Main Claims and Actual Contribution

- 탐색 중 지지 관계 그래프를 수정하고 언어모델의 상식과 시각·언어 유사도로 다음에 조사할 위치를 고른다. [PDF 3쪽](https://arxiv.org/pdf/2409.18743v1#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2409.18743v1#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2409.18743v1#page=5)
- Habitat에서 물건을 옮기는 연속 과제를 구성해 탐색을 평가하고 실제 로봇에서도 이동한 물체를 찾는 사례를 제시했다. [PDF 5쪽](https://arxiv.org/pdf/2409.18743v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2409.18743v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2409.18743v1#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 5 (1. Does the carrier-relationship scene graph (CRSG) im), p. 4 (1. Does the carrier-relationship scene graph (CRSG) im) |
| Embodiment/environment | Real-World Validation We validated our algorithm using an Autolabor robot in a real scene, equipped with an industrial computer featuring an NVIDIA GeForce RTX 3080. | hardware/simulator version and reset protocol | p. 6 (1. Does the carrier-relationship scene graph (CRSG) im), p. 3 (III. METHOD) |
| Dataset/benchmark | Leveraging the LLM's commonsense understanding of object-carrier relationships (e.g., "a cup is unlikely to be placed on a toilet"), the LLM identifies the carrier object where the target object is most likely ... | role, split, size and leakage | p. 6 (1. Does the carrier-relationship scene graph (CRSG) im), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 5 (1. Does the carrier-relationship scene graph (CRSG) im) |
| Metric | We report Success Rate(SR) and Success weighted by inverse Path Length (SPL) [39]. | definition, denominator, direction and uncertainty | p. 4 (1. Does the carrier-relationship scene graph (CRSG) im), p. 4 (1. Does the carrier-relationship scene graph (CRSG) im), p. 5 (1. Does the carrier-relationship scene graph (CRSG) im) |
| Baseline/ablation | The resulting feature is then compared with the SBERT or CLIP features of each object in the CRSG S G using cosine similarity, similar to Eq. | fair input/data/compute/action matching | p. 3 (III. METHOD), p. 4 (III. METHOD), p. 6 (1. Does the carrier-relationship scene graph (CRSG) im) |

## Explicit Limitations and Failure Boundary

- **p. 4 / 1. Does the carrier-relationship scene graph (CRSG) im - extractive body cue:** If the robot fails to reach the target, the SPL score is zero.
- **p. 5 / 1. Does the carrier-relationship scene graph (CRSG) im - extractive body cue:** VLMap Ours ConceptGraph Result: Success Result: Success Result: Failed ---Find a chair Result: Failed ---Find yellow bottle Result: Failed ---Find chairs Task 1: black bottle ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 2 (III. METHOD)이다.
