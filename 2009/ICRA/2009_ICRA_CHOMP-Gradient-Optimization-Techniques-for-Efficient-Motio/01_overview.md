# CHOMP: Gradient Optimization Techniques for Efficient Motion Planning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1109/ROBOT.2009.5152817.
> PDF retrieval source: https://www.ri.cmu.edu/pub_files/2009/5/icra09-chomp.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2009 / ICRA
- Authors: Nathan Ratliff, Matt Zucker, J. Andrew Bagnell, Siddhartha Srinivasa
- Primary track: Planning and control
- Tier: REFERENCE
- Tags: Robotics, motion planning, trajectory optimization, manipulation
- Official paper: https://api.crossref.org/works/10.1109/ROBOT.2009.5152817
- Full-text retrieval: https://www.ri.cmu.edu/pub_files/2009/5/icra09-chomp.pdf
- Code/Project: https://moveit.github.io/moveit_tutorials/doc/chomp_planner/chomp_planner_tutorial.html
- Paper type: theory_or_foundation
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0) 2026-11-24 한 줄 요약과 핵심 기여 두 개를 각 문장에 인용한 판본의 원문에서 확인했다.

## Why This Paper Is Here

CHOMP는 궤적의 매끄러움과 장애물 비용을 함께 줄이는 공변 경사 갱신으로 연속 동작 경로를 정제한다. [PDF 1쪽](https://www.ri.cmu.edu/pub_files/2009/5/icra09-chomp.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** Existing high-dimensional motion planning algorithms are simultaneously overpowered and underpowered.
- **p. 1 / Abstract - extractive body cue:** In domains sparsely populated by obstacles, the heuristics used by sampling-based planners to navigate "narrow passages" can be needlessly complex; furthermore, additional post-processing is required ...
- **p. 1 / Abstract - extractive body cue:** In this paper, we present CHOMP, a novel method for continuous path refinement that uses covariant gradient techniques to improve the quality of sampled trajectories.
- **p. 1 / Abstract - extractive body cue:** Our optimization technique converges over a wider range of input paths and is able to optimize higherorder dynamics of trajectories than previous path optimization strategies.
- **p. 1 / Abstract - extractive body cue:** As a result, CHOMP can be used as a standalone motion planner in many real-world planning queries.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Few current approaches to optimal control are equipped to handle obstacle avoidance, though.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Many optimal controllers which do handle obstacles are framed in terms of mixed integer programming, which is known to be an NP-hard problem [24], [9], ...

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we present Covariant Hamiltonian Optimization for Motion Planning (CHOMP), a novel method for generating and optimizing trajectories for robotic systems.
- **p. 1 / II. THE CHOMP ALGORITHM - extractive body cue:** In this section, we present CHOMP, a new trajectory optimization procedure based on covariant gradient descent.
- **p. 2 / II. THE CHOMP ALGORITHM - extractive body cue:** Given suitable finite differencing matrices Kd for d = 1, . . . , D, we can represent fprior as a sum of terms fprior(ξ) ...
- **p. 4 / II. THE CHOMP ALGORITHM - extractive body cue:** As we show in the next section, we could also derive the objective over a prespecified discretization, but we find that the properties of the ...
- **p. 3 / II. THE CHOMP ALGORITHM - extractive body cue:** We gain additional insight into the computational benefits of the covariant gradient based update by considering the analysis tools developed in the online learning/optimization literature, ...
- **p. 3 / II. THE CHOMP ALGORITHM - extractive body cue:** This normative approach makes it easy to derive the CHOMP update rule: we can understand equation 3 as the Lagrangian form of an optimization problem ...
- **p. 3 / II. THE CHOMP ALGORITHM - extractive body cue:** However, as we discuss in section V, while the algorithm solves a substantially larger breadth of planning problems than traditional trajectory optimization algorithms, it still ...
- **p. 2 / II. THE CHOMP ALGORITHM - extractive body cue:** For instance, the first term (d = 1) represents the total squared velocity along the trajectory.

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The approach shares much in common with elastic bands planning; however, unlike many previous path optimization techniques, we drop the requirement that the input path be Fig. | start/goal, map, dynamics와 successor/operator description | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION) |
| State/latent | shares, much, common, elastic, bands, planning, however, unlike, many, previous, path, optimization | path, trajectory, symbolic state 또는 task-motion decision | p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 2 (II. THE CHOMP ALGORITHM) |
| Output/action | Perhaps the most prevalent method of path optimization is the so-called "shortcut" heuristic, which picks pairs of configurations along the path and invokes a local planner to attempt to replace the intervening ... | feasible action sequence 또는 minimum-cost plan | p. 1 (I. INTRODUCTION), p. 2 (II. THE CHOMP ALGORITHM), p. 3 (II. THE CHOMP ALGORITHM) |
| Objective/outcome | Setting the gradient of the right hand side of equation 3 to zero and solving for the minimizer results in the following more succinct update rule: ξk+1 = ξk -1 λM -1gk ... | path cost, goal reachability, feasibility와 computation | p. 2 (II. THE CHOMP ALGORITHM), p. 3 (II. THE CHOMP ALGORITHM), p. 3 (II. THE CHOMP ALGORITHM) |

## Main Claims and Actual Contribution

- 로봇 몸체의 점들이 이동한 길이에 따라 장애물 비용을 적분하고 궤적 전체로 회피 변위를 분배한다. [PDF 3쪽](https://www.ri.cmu.edu/pub_files/2009/5/icra09-chomp.pdf#page=3) · [PDF 4쪽](https://www.ri.cmu.edu/pub_files/2009/5/icra09-chomp.pdf#page=4)
- 6자유도 팔의 장애물 회피와 사족 로봇의 보행 궤적 생성에 같은 최적화 원리를 적용한다. [PDF 5쪽](https://www.ri.cmu.edu/pub_files/2009/5/icra09-chomp.pdf#page=5) · [PDF 6쪽](https://www.ri.cmu.edu/pub_files/2009/5/icra09-chomp.pdf#page=6) · [PDF 7쪽](https://www.ri.cmu.edu/pub_files/2009/5/icra09-chomp.pdf#page=7)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / SOURCE-REPORTED EVALUATION | do not infer unreported downstream behavior | p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| Embodiment/environment | We chose 15 different configurations in a given scene representing various tasks such as picking up an object 3The last degree of freedom simply rotates the hand in place. | hardware/simulator version and reset protocol | p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| Dataset/benchmark | Left: This figure shows the joint angle traces that result from running CHOMP on the robot arm described in section III using the smooth projection procedure discussed in section II-F. | role, split, size and leakage | p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 5 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| Metric | Because the amount of rotation over a footstep is generally quite small (under 30◦), the error between the inner product on exponential map vectors and the true quaternion distance metric is negligible. | definition, denominator, direction and uncertainty | p. 7 (IV. IMPLEMENTATION ON A QUADRUPED ROBOT), p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM) |
| Baseline/ablation | CHOMP successfully found collision-free trajectories for 99 of the 105 problem.4 We additionally compared the performance of CHOMP when initialized to a straight-line trajectory through configuration space to its performance when initia ... | fair input/data/compute/action matching | p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 6 (III. EXPERIMENTS ON A ROBOTIC ARM), p. 1 (Figure/Table caption) |

## Explicit Limitations and Failure Boundary

- **p. 1 / Figure/Table caption - extractive body cue:** Fig. 1. Experimental robotic platforms: Boston Dynamics's LittleDog (left), and Barrett Technology's WAM arm (right). collision free. As a result, CHOMP can often transform a ...
- **p. 5 / III. EXPERIMENTS ON A ROBOTIC ARM - extractive body cue:** Section II-C discusses a heuristic based on the signed distance field under which the obstacles themselves specify how the robot should best remove itself from ...
- **p. 5 / III. EXPERIMENTS ON A ROBOTIC ARM - extractive body cue:** Intuitively, this heuristic suggests simply that the workspace gradients encountered after then first collision of a given configuration are invalid and should therefore be ignored.
- **p. 6 / III. EXPERIMENTS ON A ROBOTIC ARM - extractive body cue:** Without explicitly optimizing trajectory dynamics, the RRT returns a poor initial trajectory which causes CHOMP to quickly fall into a suboptimal local minimum. from the ...
- **p. 6 / III. EXPERIMENTS ON A ROBOTIC ARM - extractive body cue:** CHOMP successfully found collision-free trajectories for 99 of the 105 problem.4 We additionally compared the performance of CHOMP when initialized to a straight-line trajectory through ...
- **p. 7 / IV. IMPLEMENTATION ON A QUADRUPED ROBOT - extractive body cue:** The prior is defined as penalizing the distance below some known obstacle-free height when the swing leg is in collision with the terrain.
- **p. 7 / IV. IMPLEMENTATION ON A QUADRUPED ROBOT - extractive body cue:** As shown in figure 7, the initial trajectory for the footstep is not always feasible; however, the CHOMP algorithm is almost always able to find ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 3 (II. THE CHOMP ALGORITHM), p. 2 (II. THE CHOMP ALGORITHM)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** Many optimal controllers which do handle obstacles are framed in terms of mixed integer programming, which is known to be an NP-hard problem [24], [9], [17], [27]. (p. 1, I. INTRODUCTION).
- **Actual contribution:** In this paper, we present Covariant Hamiltonian Optimization for Motion Planning (CHOMP), a novel method for generating and optimizing trajectories for robotic systems. (p. 1, I. INTRODUCTION).
- **Evaluation boundary:** This section presents experimental results for our implementation of CHOMP on Barrett Technology's WAM arm shown in figure 1. (p. 5, III. EXPERIMENTS ON A ROBOTIC ARM).
- **Explicit failure boundary:** However, as we discuss in section V, while the algorithm solves a substantially larger breadth of planning problems than traditional trajectory optimization algorithms, it still falls prey to local minima ... (p. 3, II. THE CHOMP ALGORITHM).
