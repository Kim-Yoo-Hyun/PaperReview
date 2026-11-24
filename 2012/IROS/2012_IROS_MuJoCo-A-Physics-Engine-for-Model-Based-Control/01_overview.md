# MuJoCo: A Physics Engine for Model-Based Control

> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0); canonical paper source: https://api.crossref.org/works/10.1109/IROS.2012.6386109.
> PDF retrieval source: https://doi.org/10.1109/IROS.2012.6386109. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> Evidence boundary: selected PDF body sentences, captions and section anchors; exact table/equation values remain at those anchors.

- Year/Venue: 2012 / IROS
- Authors: Emanuel Todorov, Tom Erez, Yuval Tassa
- Primary track: Planning and control
- Tier: CORE
- Tags: Robotics, simulation, Physics Engine, Control
- Official paper: https://api.crossref.org/works/10.1109/IROS.2012.6386109
- Full-text retrieval: https://roboti.us/lab/papers/TodorovIROS12.pdf
- Code/Project: https://mujoco.org/
- Paper type: benchmark_or_dataset
- Source audit: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; title-token overlap first two pages=1.0). 2026-11-24 저자판 PDF에서 §II의 접촉 계산과 §IV 표 1을 육안 대조했다.

## Why This Paper Is Here

MuJoCo는 접촉이 있는 다관절 동역학을 모델 기반 제어에 필요한 속도로 계산하는 물리 엔진이다.

## Problem and Motivation

- **p. 1 / Abstract - extractive body cue:** We describe a new physics engine tailored to model-based control.
- **p. 1 / Abstract - extractive body cue:** Multi-joint dynamics are represented in generalized coordinates and computed via recursive algorithms.
- **p. 1 / Abstract - extractive body cue:** Contact responses are computed via efficient new algorithms we have developed, based on the modern velocity-stepping approach which avoids the difficulties with spring-dampers.
- **p. 1 / Abstract - extractive body cue:** Models are specified using either a high-level C++ API or an intuitive XML file format.
- **p. 1 / Abstract - extractive body cue:** A built-in compiler transforms the user model into an optimized data structure used for runtime computation.
- **p. 1 / I. INTRODUCTION - extractive body cue:** However they lack the speed, accuracy and overall feature sets needed to automate the controller design process itself.
- **p. 1 / I. INTRODUCTION - extractive body cue:** What is less obvious however is that, in the context of control optimization, these requirements become so demanding that none of the existing physics engines ...

## Core Idea

- **p. 2 / I. INTRODUCTION - extractive body cue:** This is useful for approximating derivatives via finite differencing, which in turn enables numerical optimization. • Inverse dynamics can always be computed, even in the ...
- **p. 2 / II. ALGORITHMIC FOUNDATIONS - extractive body cue:** The procedure for solving the above equations of motion consists of the following steps:
- 하나의 MuJoCo 모델은 하나 이상의 운동학적 트리로 구성된다. 각 트리의 기저는 공간에서 자유롭게 움직일 수 있어 독립된 물체도 표현할 수 있다. [§III-B 강체 모델 · PDF 6쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=6)
- **p. 1 / I. INTRODUCTION - extractive body cue:** Existing physics engines can be used to test controllers that are already designed.
- **p. 1 / I. INTRODUCTION - extractive body cue:** As Sims [7] pointed out, if the physics engine allows cheating the optimization algorithm will find a way to exploit it - and produce a ...
- **p. 7 / III. MODELING - extractive body cue:** The tendon path is the shortest path that passes through a sequence of specified sites or wraps around specified geoms. h) Actuator: Actuators have control ...
- **p. 2 / II. ALGORITHMIC FOUNDATIONS - extractive body cue:** We start with notation and smooth dynamics which are fairly standard, then explain the contact simulation algorithms in more detail, followed by computational complexity and ...
- $q$와 $v$는 일반화 좌표의 위치와 속도, $M$은 관성 행렬이다. $b$는 코리올리·원심·중력·스프링 항을 포함하는 편향력이다. [§II-A 운동 방정식 · PDF 2쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=2)

## Observation, State, and Output Interface

| Role | PDF body evidence | Robotics interpretation | Anchor |
|---|---|---|---|
| Observation/input | The tendon path is the shortest path that passes through a sequence of specified sites or wraps around specified geoms. h) Actuator: Actuators have control inputs, optional activation states (used to model ... | simulated state, geometry, contact와 control input | p. 7 (III. MODELING), p. 2 (I. INTRODUCTION) |
| State/latent | tendon, path, shortest, passes, through, sequence, specified, sites, wraps, around, geoms, Actuator | dynamics/contact state 또는 learned simulator representation | p. 7 (III. MODELING), p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Output/action | These observations indicated that we need a new engine, representing the state in joint coordinates and simulating contacts in ways that are related to LCP but better. | simulation step, trajectory 또는 environment query | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 7 (III. MODELING) |
| Dynamics variables | $q$와 $v$는 일반화 좌표의 위치와 속도, $M$은 관성 행렬이다. $b$는 코리올리·원심·중력·스프링 항을 포함하는 편향력이다. | 관성 및 편향력과 접촉 충격량은 별도의 항이다. | [§II-A 운동 방정식 · PDF 2쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=2) |

## Main Claims and Actual Contribution

- 일반화 좌표와 재귀 계산으로 다관절 계를 표현하고 속도 단계에서 접촉 반응을 계산한다.
- 순·역동역학을 제공하고 여러 상태·제어의 계산을 병렬화해 샘플링과 유한차분 기반 최적화를 지원한다.

[저자 원문](https://homes.cs.washington.edu/~todorov/papers/TodorovIROS12.pdf)

## Evaluation Scope

| Dimension | Body-grounded record | Boundary | Anchor |
|---|---|---|---|
| Evaluation type | BENCHMARK / DATASET | do not infer unreported downstream behavior | p. 2 (I. INTRODUCTION), p. 4 (5) Integrate numerically to obtain the next state) |
| Embodiment/environment | It can be used to analyze data or to compute the torques that will cause a robot to follow a reference trajectory. | hardware/simulator version and reset protocol | p. 5 (5) Integrate numerically to obtain the next state), p. 2 (I. INTRODUCTION) |
| Dataset/benchmark | However in the presence of branch-induced sparsity typical in robotics these algorithms are not much faster than the present approach [4]. | role, split, size and leakage | p. 5 (5) Integrate numerically to obtain the next state), p. 2 (I. INTRODUCTION), p. 5 (5) Integrate numerically to obtain the next state), p. 6 (III. MODELING) |
| Metric | Furthermore the pyramid approximation introduces errors. | definition, denominator, direction and uncertainty | p. 4 (5) Integrate numerically to obtain the next state), p. 4 (5) Integrate numerically to obtain the next state), p. 5 (5) Integrate numerically to obtain the next state) |
| Baseline/ablation | Performance on smooth dynamics compared to SD/FAST We measured the speed of multi-joint dynamics simulation in the absence of contacts or equality constraints. | fair input/data/compute/action matching | p. 7 (IV. TIMING TESTS), p. 2 (I. INTRODUCTION), p. 4 (5) Integrate numerically to obtain the next state) |

## Explicit Limitations and Failure Boundary

- **p. 3 / II. ALGORITHMIC FOUNDATIONS - extractive body cue:** 1) Compute the Cartesian positions and orientations of all rigid bodies (i.e. the forward kinematics), detect potential collisions (with some safety margin), and construct the ...
- 접선 속도와 마찰 충격량은 평행하고 $\langle\mathbf v^{\mathcal F},\mathbf f^{\mathcal F}\rangle\le0$이다. 마찰원뿔의 경계는 $\lVert\mathbf f^{\mathcal F}\rVert\le\mu f^{\mathcal N}$이며 $\mu$는 마찰계수다. [§II-B 식 5 · PDF 3쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=3)
- **p. 4 / 5) Integrate numerically to obtain the next state - extractive body cue:** Since the underlying problem is NP-hard, the algorithm cannot always find the exact solution (which has 0 residual).
- 볼록 접촉 해법은 특이할 수 있는 $A$에 대각 정규화 행렬 $R$을 더한다. 접촉 거리와 함께 $R$을 키우면 떨어진 물체 사이에도 약한 접촉력을 모델링할 수 있다. [§II-D 식 6 · PDF 4쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=4)
- 대각 해법은 관입이 임계 감쇠 스프링처럼 줄고 미끄러짐이 없을 때의 다음 접촉 속도 $\mathbf v_C^\ast$를 목표로 둔다. [§II-E 대각 해법 · PDF 5쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=5)
- **p. 7 / III. MODELING - extractive body cue:** Their primary use in the engine is collision detection as well as tendon wrapping.
- **p. 7 / III. MODELING - extractive body cue:** Collision detection uses dedicated pair-wise functions when possible, and otherwise defaults to a general-purpose convex collider (implemented by libccd).

## Why Read It

방법과 평가 범위를 대조할 원문 구간은 p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 7 (III. MODELING), p. 2 (II. ALGORITHMIC FOUNDATIONS)이다.

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Problem/bottleneck:** However they lack the speed, accuracy and overall feature sets needed to automate the controller design process itself. (p. 1, I. INTRODUCTION).
- **Actual contribution:** This is useful for approximating derivatives via finite differencing, which in turn enables numerical optimization. • Inverse dynamics can always be computed, even in the presence of contacts and equality ... (p. 2, I. INTRODUCTION).
- **Evaluation boundary:** Table 3: This is the inverse of Table 2. Here we show the number of dynamics evaluations per second. The results are quite remarkable. One a single desktop machine, we ... (p. 8, Figure/Table caption).
- **Explicit failure boundary:** In the absence of adequate tools, the field continues to rely on manual controller designs - which may be a large part of the reason why present-day robots do not ... (p. 1, I. INTRODUCTION).
