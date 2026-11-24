# Sampling-based Algorithms for Optimal Motion Planning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (76 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://arxiv.org/abs/1105.1186.
> PDF retrieval source: https://arxiv.org/pdf/1105.1186. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2011 / IJRR
- Authors: Sertac Karaman, Emilio Frazzoli
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: Robotics, motion planning, RRT*, asymptotic optimality
- Official paper: https://arxiv.org/abs/1105.1186
- Full-text retrieval: https://arxiv.org/pdf/1105.1186
- Code/Project: https://ompl.kavrakilab.org/
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (76 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

Karaman과 Frazzoli는 표본 수가 늘어날 때 표본 기반 경로 계획기가 찾는 경로 비용의 극한을 분석한다. [PDF 1쪽](https://arxiv.org/pdf/1105.1186v1#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** During the last decade, sampling-based path planning algorithms, such as Probabilistic RoadMaps (PRM) and Rapidly-exploring Random Trees (RRT), have been shown to work well in ...
- **p. 1 / Abstract - extractive body cue:** However, little effort has been devoted to the formal analysis of the quality of the solution returned by such algorithms, e.g., as a function of ...
- **p. 1 / Abstract - extractive body cue:** The purpose of this paper is to fill this gap, by rigorously analyzing the asymptotic behavior of the cost of the solution returned by stochastic ...
- **p. 1 / Abstract - extractive body cue:** A number of negative results are provided, characterizing existing algorithms, e.g., showing that, under mild technical conditions, the cost of the solution returned by broadly ...
- **p. 1 / Abstract - extractive body cue:** The main contribution of the paper is the introduction of new algorithms, namely, PRM∗and RRT∗, which are provably asymptotically optimal, i.e., such that the cost ...
- **p. 1 / 1 Introduction - extractive body cue:** An algorithm to address this problem is said to be complete if it terminates in finite time, returning a valid solution if one exists, and ...
- **p. 6 / 1 Introduction - extractive body cue:** The feasibility problem of path planning is to find a feasible path, if one exists, and report failure otherwise: Problem 2 (Feasible path planning) Given ...

## Core Idea

- **p. 4 / 1 Introduction - extractive body cue:** As in the early seminal papers on incremental samplingbased motion planning algorithms such as Kuffner and LaValle (2000), no differential constraints are considered (i.e., the ...
- **p. 11 / 1 Introduction - extractive body cue:** In its basic version, it consists of a pre-processing phase, in which a roadmap is constructed by attempting connections among n randomly-sampled points in Xfree, ...
- **p. 13 / 1 Introduction - extractive body cue:** Algorithm 3: RRT 1 V ←{xinit}; E ←∅; 2 for i = 1, . . . , n do 3 xrand ←SampleFreei; 4 xnearest ←Nearest(G ...
- **p. 2 / 1 Introduction - extractive body cue:** Important contributions towards broader applicability of these methods include navigation functions (Rimon and Koditschek, 1992) and randomization (Barraquand and Latombe, 1993).
- **p. 4 / 1 Introduction - extractive body cue:** A summary of the contributions can be found below, and is shown in Table 1.
- **p. 4 / 1 Introduction - extractive body cue:** 1.3 Statement of Contributions To the best of the author's knowledge, this paper provides the first systematic and thorough analysis of optimality and complexity properties ...
- **p. 2 / 1 Introduction - extractive body cue:** Instead of using an explicit representation of the environment, samplingbased algorithms rely on a collision checking module, providing information about feasibility of candidate trajectories, and ...
- **p. 7 / 1 Introduction - extractive body cue:** On the application side, in recent years, random geometric graphs have attracted significant attention as models of ad hoc wireless networks (Gupta and Kumar, 1998, ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | Informally speaking, given a robot with a description of its dynamics, a description of the environment, an initial state, and a set of goal states, the motion planning problem is to find ... | start/goal, map, dynamics와 successor/operator description | p. 1 (1 Introduction), p. 11 (1 Introduction) |
| State/latent | Informally, speaking, given, robot, description, dynamics, environment, initial, state, goal, states, motion | path, trajectory, symbolic state 또는 task-motion decision | p. 1 (1 Introduction), p. 11 (1 Introduction), p. 13 (1 Introduction) |
| Output/action | For convenience, inputs and outputs of the algorithms are not shown explicitly, but are as follows. | feasible action sequence 또는 minimum-cost plan | p. 11 (1 Introduction), p. 13 (1 Introduction), p. 2 (1 Introduction) |
| Objective/outcome | For example, one may be interested in solution paths of minimum cost, with respect to a given cost functional, such as the length of a path, or the time required to execute ... | path cost, goal reachability, feasibility와 computation | p. 3 (1 Introduction), p. 6 (1 Introduction), p. 6 (1 Introduction) |

## Main Claims and Actual Contribution

- RRT*는 새 정점의 부모를 비용에 따라 고르고 근처의 기존 연결도 낮은 비용 경로로 바꾼다. [PDF 15쪽](https://arxiv.org/pdf/1105.1186v1#page=15) · [PDF 16쪽](https://arxiv.org/pdf/1105.1186v1#page=16)
- 논문이 둔 정칙성 조건에서 PRM*와 RRT*의 점근적 최적성을 보이고 기존 RRT의 확률적 완전성과 구별한다. [PDF 5쪽](https://arxiv.org/pdf/1105.1186v1#page=5) · [PDF 21쪽](https://arxiv.org/pdf/1105.1186v1#page=21)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | SYSTEM / EVALUATION SCOPE UNRESOLVED | do not infer unreported downstream behavior | p. 31 (V RRT∗), p. 33 (V RRT∗) |
| Embodiment/environment | However, in many online real-time applications such as robotics, it is highly desirable to reduce the computation time of each iteration under sublinear bounds, e.g., in O(log n) time, especially for anytime ... | hardware/simulator version and reset protocol | p. 31 (V RRT∗), p. 25 (V RRT∗) |
| Dataset/benchmark | 4.3 Computational Complexity The objective of this section is to compare the computational complexity of the algorithms provided in Section 3. | role, split, size and leakage | p. 31 (V RRT∗), p. 25 (V RRT∗), p. 29 (V RRT∗), p. 31 (V RRT∗) |
| Metric | Figure 25: The set eBn,m of non-intersection balls is illustrated. Finally, the following lemma states that the cost of the minimum cost path in the graph returned by the PRM∗algorithm converges to ... | definition, denominator, direction and uncertainty | p. 61 (Figure/Table caption), p. 17 (Figure/Table caption), p. 33 (V RRT∗) |
| Baseline/ablation | Using these results, a thorough analysis of the computational complexity of the all the algorithms is given in terms of the number of simple operations, such as comparisons, additions, multiplications. | fair input/data/compute/action matching | p. 29 (V RRT∗), p. 32 (V RRT∗), p. 33 (V RRT∗) |

## Explicit Limitations and Failure Boundary

- **p. 35 / 6 Conclusion - extractive body cue:** In order to address these limitations of existing algorithms, a number of new algorithms are introduced, and proven to be asymptotically optimal and computational efficient, ...
- **p. 17 / Figure/Table caption - extractive body cue:** Figure 1: An illustration of the δ-interior of Xfree. The obstacle region Xobs is shown in dark grey and the δ-interior of Xfree is shown ...
- **p. 29 / V RRT∗ - extractive body cue:** First, each algorithm is analyzed in terms of the number of calls to the CollisionFree procedure.
- **p. 29 / V RRT∗ - extractive body cue:** Number of calls to the CollisionFree procedure Let MALG n denote the total number of calls to the CollisionFree procedure by algorithm ALG in iteration ...
- **p. 30 / V RRT∗ - extractive body cue:** The next lemma upper-bounds the number of calls to the CollisionFree procedure in the proposed algorithms.
- **p. 30 / V RRT∗ - extractive body cue:** Let A denote the event that the sample Xn drawn at the last iteration falls into the rn interior of Xfree.
- **p. 31 / V RRT∗ - extractive body cue:** The main result is based on Six and Wood (1982), which shows that checking collision with m obstacles can be executed in O(logd m) time ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (1 Introduction), p. 6 (1 Introduction), p. 2 (1 Introduction), p. 3 (1 Introduction), p. 4 (1 Introduction)이다.
