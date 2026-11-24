# Towards Tight Convex Relaxations for Contact-Rich Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://www.roboticsproceedings.org/rss20/p132.html.
> PDF retrieval source: https://www.roboticsproceedings.org/rss20/p132.pdf. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2024 / RSS
- Authors: Bernhard Paus Graesdal, Shao Yuan Chew Chia, Tobia Marcucci, Savva Morozov, Alexandre Amice, Pablo A. Parrilo, Russ Tedrake
- 저자 표기 근거 — RSS 표제면에서 Pablo A. Parrilo의 가운데 이니셜을 확인했다. [표제면](https://www.roboticsproceedings.org/rss20/p132.pdf#page=1)
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: Robotics, contact-rich manipulation, convex relaxation, trajectory optimization
- Official paper: https://www.roboticsproceedings.org/rss20/p132.html
- Full-text retrieval: https://www.roboticsproceedings.org/rss20/p132.pdf
- Code/Project: https://bernhardgraesdal.com/rss24-towards-tight-convex-relaxations/
- Paper type: method
- Source audit: full-text PDF body checked on 2026-09-03 (12 pages; PyMuPDF text; title-token overlap first two pages=1.0)

## Why This Paper Is Here

이 연구는 평면 밀기에서 접촉 순서와 물체 궤적을 함께 구하는 전역 계획 문제에 볼록 완화를 적용한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss20/p132.pdf#page=1)

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We present a novel method for global motion planning of robotic systems that interact with the environment through contacts.
- **p. 1 / Abstract - extractive body cue:** Our method directly handles the hybrid nature of such tasks using tools from convex optimization.
- **p. 1 / Abstract - extractive body cue:** We formulate the motion-planning problem as a shortest-path problem in a graph of convex sets, where a path in the graph corresponds to a contact ...
- **p. 1 / Abstract - extractive body cue:** For each contact mode, we use semidefinite programming to relax the nonconvex dynamics that results from the simultaneous optimization of the object's pose, contact locations, ...
- **p. 1 / Abstract - extractive body cue:** The result is a tight convex relaxation of the overall planning problem, that can be efficiently solved and quickly rounded to find a feasible contact-rich ...
- **p. 3 / V. BACKGROUND AND OPTIMIZATION TOOLS - extractive body cue:** The optimality gap δopt can then be overestimated as δopt = Cround -Copt Copt ≤Cround -Crelax Crelax = δrelax (2) Finally, we note that the ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** It generally involves both a hybrid and underactuated dynamical system, making planning and control difficult.

## Core Idea

- **p. 1 / I. INTRODUCTION - extractive body cue:** Our method approximates these bilinearities using a tight Semidefinite Programming (SDP) relaxation for each contact mode.
- **p. 1 / I. INTRODUCTION - extractive body cue:** As a first application for evaluating our method, this work explores the task of planar pushing, first studied by Mason in [2].
- **p. 2 / I. INTRODUCTION - extractive body cue:** of planar pushing, the technique we introduce generalizes naturally to more complex multi-contact problems.
- **p. 3 / IV. HIGH-LEVEL APPROACH - extractive body cue:** The second step in our method is to formulate the global motion planning problem as an SPP in a GCS [1].
- **p. 2 / III. PROBLEM STATEMENT - extractive body cue:** As a first application of our method, we explore planar pushing, a non-prehensile manipulation task where the robot uses a cylindrical finger to manipulate the ...
- **p. 7 / VII. MOTION PLANNING FOR PLANAR PUSHING - extractive body cue:** A feasible path p through G then has the interpretation as a continuous trajectory from the initial state to the target state, that consists of ...
- **p. 3 / IV. HIGH-LEVEL APPROACH - extractive body cue:** The first step in formulating our motion planning method is to consider the dynamics and kinematics in a fixed contact mode.
- **p. 7 / VII. MOTION PLANNING FOR PLANAR PUSHING - extractive body cue:** Specifically, for each edge e = (u, v) ∈E we enforce that the last state in the trajectory in vertex u is equal to the ...

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | We represent a trajectory segment within each mode for the slider-pusher system by N discrete knot points for the state and N -1 knot points for the input: x0, x1, . . ... | RGB-D/point cloud, object state와 contact/task observation | p. 6 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING) |
| State/latent | represent, trajectory, segment, within, mode, slider-pusher, system, discrete, knot, points, state, input | object geometry, affordance, contact mode 또는 end-effector state | p. 6 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING) |
| Output/action | The point xv ∈Xv now corresponds to a trajectory of length N of states and inputs for the sliderpusher system in mode Ci. | grasp, pose, force 또는 end-effector trajectory | p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 3 (III. PROBLEM STATEMENT) |
| Objective/outcome | In principle, this does not include all the tightening constraints (4d) and yields a potentially weaker convex relaxation, but in practice, we find that the loss in tightness is negligible while significantly ... | task completion, contact success, pose/force error와 generalization | p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING), p. 4 (V. BACKGROUND AND OPTIMIZATION TOOLS) |

## Main Claims and Actual Contribution

- 접촉 모드를 볼록 집합의 그래프로 나타내고 각 모드의 준정적 동역학을 준정부호 계획으로 완화한다. [PDF 4쪽](https://www.roboticsproceedings.org/rss20/p132.pdf#page=4) · [PDF 5쪽](https://www.roboticsproceedings.org/rss20/p132.pdf#page=5)
- 완화해에서 실행 가능한 궤적을 복원해 평면 밀기의 최적 비용 하한과 비교하고 실제 로봇에서 계획을 시험했다. [PDF 8쪽](https://www.roboticsproceedings.org/rss20/p132.pdf#page=8) · [PDF 9쪽](https://www.roboticsproceedings.org/rss20/p132.pdf#page=9)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | EMPIRICAL / REAL-ROBOT OR HARDWARE | do not infer unreported downstream behavior | p. 9 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS) |
| Embodiment/environment | Execution on real hardware Finally, we demonstrate the feasibility of the obtained motion plans on a Kuka LBR iiwa 7 R800 7-DOF robotic arm, with a T-shaped slider object. | hardware/simulator version and reset protocol | p. 10 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS) |
| Dataset/benchmark | This section contains both numerical and hardware experiments. | role, split, size and leakage | p. 10 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS), p. 8 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS) |
| Metric | As our method is capable of global reasoning and does not rely on an initial guess, it has a much higher success rate compared to the baseline. | definition, denominator, direction and uncertainty | p. 9 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 8 (VIII. EXPERIMENTS) |
| Baseline/ablation | Comparison with contact-implicit trajectory optimization To compare our method with a state-of-the-art baseline for contact-rich planning, we select a direct, contact-implicit trajectory optimization method similar to those proposed in ... | fair input/data/compute/action matching | p. 9 (VIII. EXPERIMENTS), p. 9 (VIII. EXPERIMENTS), p. 10 (VIII. EXPERIMENTS) |

## Explicit Limitations and Failure Boundary

- **p. 10 / IX. CONCLUSION AND FUTURE WORK - extractive body cue:** Future work will explore the ability of these reduction methods to accelerate the planning.
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3: a) An example of a configuration-space partitioning Q1, . . . , Q4 and the linear approximations ϕ1, . . . , ϕ4 ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 5: Our method is able to generate close-to globally optimal plans for pushing tasks with collision-free motion planning between contact modes. Here, two different ...
- **p. 9 / VIII. EXPERIMENTS - extractive body cue:** Our method also guarantees that the trajectory stays collision-free between contacts, while the baseline can be seen to clip the corners of the slider.
- **p. 10 / VIII. EXPERIMENTS - extractive body cue:** This limitation is not surprising, as the baseline is a local method that relies heavily on its initial guess.
- **p. 9 / VIII. EXPERIMENTS - extractive body cue:** As our method is capable of global reasoning and does not rely on an initial guess, it has a much higher success rate compared to ...

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 3 (V. BACKGROUND AND OPTIMIZATION TOOLS), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 7 (VII. MOTION PLANNING FOR PLANAR PUSHING)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (12 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** It generally involves both a hybrid and underactuated dynamical system, making planning and control difficult. (p. 1, I. INTRODUCTION).
- **Actual contribution:** Our method approximates these bilinearities using a tight Semidefinite Programming (SDP) relaxation for each contact mode. (p. 1, I. INTRODUCTION).
- **Evaluation boundary:** As our method is capable of global reasoning and does not rely on an initial guess, it has a much higher success rate compared to the baseline. (p. 9, VIII. EXPERIMENTS).
- **Explicit failure boundary:** In contrast, the baseline often fails, finding a solution in 58% of the instances for the box-shaped slider geometry and a mere 12% for the T-shaped slider. (p. 10, VIII. EXPERIMENTS).

## 배포 범위 대조

- 코드 — 저자 구현 파일 · planning_through_contact/planning/planar/planar_pushing_planner.py [배포 파일](https://raw.githubusercontent.com/bernhardpg/planning-through-contact/a3998f25b2868d865ec98b2b2dca38032b93e40b/planning_through_contact/planning/planar/planar_pushing_planner.py)
