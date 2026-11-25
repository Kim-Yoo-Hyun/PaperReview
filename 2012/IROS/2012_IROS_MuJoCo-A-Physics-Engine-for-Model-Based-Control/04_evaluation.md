# Evaluation - MuJoCo: A Physics Engine for Model-Based Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://api.crossref.org/works/10.1109/IROS.2012.6386109; PDF retrieval source: https://doi.org/10.1109/IROS.2012.6386109. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Evaluation in One Sentence

PDF body evaluation/result cue (p. 2 (I. INTRODUCTION), p. 4 (5) Integrate numerically to obtain the next state), p. 5 (5) Integrate numerically to obtain the next state), p. 5 (5) Integrate numerically to obtain the next state), p. 3 (5) Integrate numerically to obtain the next state), p. 4 (5) Integrate numerically to obtain the next state)): Although this approach is a significant improvement over earlier spring-damper models of contact, it still requires manual tuning and small time steps.

## Evaluation Body Digest

- **p. 5 / 5) Integrate numerically to obtain the next state - extractive body cue:** It can be used to analyze data or to compute the torques that will cause a robot to follow a reference trajectory.
- **p. 2 / I. INTRODUCTION - extractive body cue:** This limits their applications to robotics where contact dynamics are key.
- **p. 5 / 5) Integrate numerically to obtain the next state - extractive body cue:** However in the presence of branch-induced sparsity typical in robotics these algorithms are not much faster than the present approach [4].
- **p. 6 / III. MODELING - extractive body cue:** Once a valid model object is created in the runtime environment by either method, the built-in compiler converts it into a low-level C structure used ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Note that contact simulation is an area of active research, unlike simulation of smooth multi-joint dynamics where the book has basically been written [4].
- **p. 4 / 5) Integrate numerically to obtain the next state - extractive body cue:** Furthermore the number of Newton-like iterations 0 200 400 600 simulation time (ms) vertical velocity normal impulse Fig.
- **p. 4 / 5) Integrate numerically to obtain the next state - extractive body cue:** Instead of following the LCP approach, MuJoCo implements three new algorithms for contact simulation based on our recent work, as summarized next.
- **p. 6 / III. MODELING - extractive body cue:** The built-in parser loads the MJCF file and creates a runtime C++ object describing the entire model.

## Evaluation Type and Scope

- **Evaluation type:** `BENCHMARK / DATASET`.
- **Target system/task:** physics simulation의 robot/environment model.
- **Input boundary:** simulated state, geometry, contact와 control input.
- **Output/decision under evaluation:** simulation step, trajectory 또는 environment query.
- **Primary target:** physical plausibility, speed, reproducibility와 task utility.
- **Detected evaluation headings:** not reliably recovered.

## Experimental Matrix

| Body section | Type | PDF body experiment/result cue | Anchor |
|---|---|---|---|
| I. INTRODUCTION | BENCHMARK / DATASET | Although this approach is a significant improvement over earlier spring-damper models of contact, it still requires manual tuning and small time steps. | p. 2 (I. INTRODUCTION) |
| §II-C 비선형 해법 | 반복 계산의 비용 | 각 뉴턴 반복에서 $k\times k$ 행렬을 LU 분해한다. $k$는 접촉 충격량 벡터의 차원이다(§II-B). | [§II-C 비선형 해법 · PDF 4쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=4) |
| §II-G 역동역학 | 모델 성질 | 관입 등 제약을 위반하는 운동에도 역동역학을 정의한다. 그 위반을 일으키려면 해당 부분공간에서 추정 제어력 $\tau$가 커야 한다. | [§II-G 역동역학 · PDF 5쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=5) |
| 5) Integrate numerically to obtain the next state | BENCHMARK / DATASET | While these theoretical results are important for understanding how the CPU time will scale with the number of DOFs, in practice the performance of ... | p. 5 (5) Integrate numerically to obtain the next state) |
| 5) Integrate numerically to obtain the next state | BENCHMARK / DATASET | The vector v0 is the contact velocity which results in the absence of an impulse. | p. 3 (5) Integrate numerically to obtain the next state) |

## Dataset / Benchmark Role

- **p. 5 / 5) Integrate numerically to obtain the next state - extractive body cue:** It can be used to analyze data or to compute the torques that will cause a robot to follow a reference trajectory.
- **p. 2 / I. INTRODUCTION - extractive body cue:** This limits their applications to robotics where contact dynamics are key.
- **p. 5 / 5) Integrate numerically to obtain the next state - extractive body cue:** However in the presence of branch-induced sparsity typical in robotics these algorithms are not much faster than the present approach [4].
- **p. 6 / III. MODELING - extractive body cue:** Once a valid model object is created in the runtime environment by either method, the built-in compiler converts it into a low-level C structure used ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Note that contact simulation is an area of active research, unlike simulation of smooth multi-joint dynamics where the book has basically been written [4].
- **p. 4 / 5) Integrate numerically to obtain the next state - extractive body cue:** Furthermore the number of Newton-like iterations 0 200 400 600 simulation time (ms) vertical velocity normal impulse Fig.
- **p. 4 / 5) Integrate numerically to obtain the next state - extractive body cue:** Instead of following the LCP approach, MuJoCo implements three new algorithms for contact simulation based on our recent work, as summarized next.
- **p. 6 / III. MODELING - extractive body cue:** The built-in parser loads the MJCF file and creates a runtime C++ object describing the entire model.

## Figures / Tables as Body Evidence

- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 1. Left: the algorithm is tested on a system consisting of several balls moving inside a cube. Right: average number of Newton-like iterations as ...
- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 2. Left: Rendering of a humanoid (used for testing) in the MuJoCo interactive 3D GUI. Right: a ball-drop test of the convex contact solver. ...
- 접촉·등식 제약이 없는 동역학의 초당 평가 횟수를 단일 스레드에서 측정했다. 표의 값은 100회 실행의 평균을 가장 가까운 1,000회/초 단위로 반올림한 것이다. [§IV 표 1 · PDF 7쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=7)
- **p. 7 / Figure/Table caption - extractive body cue:** Table 2: CPU time (in seconds) for one evaluation of the trajectory cost, gradient and Hessian. The number of states where the dynamics are evaluated ...
- **p. 8 / Figure/Table caption - extractive body cue:** Fig. 3. Illustration of projects where we have used MuJoCo for control synthesis and modeling. A,B are from [9]. C is from [3]. D is ...
- **p. 8 / Figure/Table caption - extractive body cue:** Table 3: This is the inverse of Table 2. Here we show the number of dynamics evaluations per second. The results are quite remarkable. One ...

## Embodiment / Environment

| Dimension | PDF body-grounded cue | Unresolved condition | Anchor |
|---|---|---|---|
| Robot/hardware/simulator | It can be used to analyze data or to compute the torques that will cause a robot to follow a reference trajectory. | embodiment, simulator version and control stack | p. 5 (5) Integrate numerically to obtain the next state), p. 2 (I. INTRODUCTION) |
| Task/environment | This limits their applications to robotics where contact dynamics are key. | reset, timeout, object/scene variation | p. 2 (I. INTRODUCTION), p. 5 (5) Integrate numerically to obtain the next state) |
| Observation/sensor | simulated state, geometry, contact와 control input | calibration, preprocessing, privileged input | p. 7 (III. MODELING), p. 2 (I. INTRODUCTION) |
| Output/decision | simulation step, trajectory 또는 environment query | action frame, controller and termination | p. 2 (I. INTRODUCTION), p. 7 (III. MODELING) |

## Metrics and Success Definition

| Metric/result evidence | Definition and aggregation to verify | Anchor |
|---|---|---|
| Furthermore the pyramid approximation introduces errors. | definition/direction/unit from same section | p. 4 (5) Integrate numerically to obtain the next state) |
| Convex solver A favorable trade-off between speed and accuracy is obtained by replacing the nonlinear complementarity constraints (4, 5) with a convex optimization problem, ... | definition/direction/unit from same section | p. 4 (5) Integrate numerically to obtain the next state) |
| Gauss-Seidel) may be faster and have comparable accuracy. | definition/direction/unit from same section | p. 5 (5) Integrate numerically to obtain the next state) |
| This is sensible when simulating a large number of mostly disconnected bodies with few joint constraints, however it becomes both inaccurate and inefficient when ... | definition/direction/unit from same section | p. 2 (I. INTRODUCTION) |
| Solving for the contact impulse We now return to step 4. | definition/direction/unit from same section | p. 3 (5) Integrate numerically to obtain the next state) |
| 접촉 충격량 $\mathbf f_C$를 구하면 식 2로 다음 속도 $\mathbf v_{t+h}$를 계산하고 위치를 적분한다. | 시뮬레이터의 한 스텝에서 속도·위치를 갱신하는 순서 | [§II-A 식 2 · PDF 3쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=3) |
| Diagonal solver The least accurate but fastest contact solver is a diagonal solver, which can be thought of as a mass-aware springdamper. | definition/direction/unit from same section | p. 5 (5) Integrate numerically to obtain the next state) |
| Different ways to construct a MuJoCo model MuJoCo models can exist on three levels of description: • XML model file in a new format ... | definition/direction/unit from same section | p. 6 (III. MODELING) |

## Baselines and Fairness

| PDF baseline/comparison cue | Fair comparison field | Anchor |
|---|---|---|
| Performance on smooth dynamics compared to SD/FAST We measured the speed of multi-joint dynamics simulation in the absence of contacts or equality constraints. | comparison identity and matched condition | p. 7 (IV. TIMING TESTS) |
| Section IV presents timing tests and comparisons to SD/FAST - which does not handle contacts, but is the best prior engine for multi-joint dynamics ... | comparison identity and matched condition | p. 2 (I. INTRODUCTION) |
| 볼록 접촉 해법은 특이할 수 있는 $A$에 대각 정규화 행렬 $R$을 더한다. 접촉 거리와 함께 $R$을 키우면 떨어진 물체 사이에도 약한 접촉력을 모델링할 수 있다. | 해법 비교에서 명시할 정규화 조건 | [§II-D 식 6 · PDF 4쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=4) |
| When there are no equality constraints and the contact solver has an exact inverse, the inverse dynamics can be computed without resorting to posthoc ... | comparison identity and matched condition | p. 6 (5) Integrate numerically to obtain the next state) |
| A unique feature of MuJoCo is that the primitive joint types can be composed into more complex joints, without having to define intermediate dummy ... | comparison identity and matched condition | p. 6 (III. MODELING) |
| This was done not only for speed comparisons, but also for debugging MuJoCo and making sure the results are numerically correct. | comparison identity and matched condition | p. 7 (IV. TIMING TESTS) |

## Ablations and Sensitivity

| PDF ablation/sensitivity cue | What it isolates | Anchor |
|---|---|---|
| 볼록 접촉 해법은 특이할 수 있는 $A$에 대각 정규화 행렬 $R$을 더한다. 접촉 거리와 함께 $R$을 키우면 떨어진 물체 사이에도 약한 접촉력을 모델링할 수 있다. | 민감도를 조사할 수 있는 정규화 항 | [§II-D 식 6 · PDF 4쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=4) |
| When there are no equality constraints and the contact solver has an exact inverse, the inverse dynamics can be computed without resorting to posthoc ... | component/input/data sensitivity | p. 6 (5) Integrate numerically to obtain the next state) |
| A unique feature of MuJoCo is that the primitive joint types can be composed into more complex joints, without having to define intermediate dummy ... | component/input/data sensitivity | p. 6 (III. MODELING) |
| 단일 접촉의 충격량 $\mathbf f_C$를 법선 성분 $f^{\mathcal N}$과 접선 평면의 두 성분 $\mathbf f^{\mathcal F}\in\mathbb R^2$로 나눈다. | 법선과 접선 방향의 구성 요소 | [§II-B 접촉 충격량 · PDF 3쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=3) |
| In the normal direction for example, if the corresponding component of x is positive it encodes force (in which case the velocity is 0), ... | component/input/data sensitivity | p. 4 (5) Integrate numerically to obtain the next state) |
| $\operatorname{diag}(A)\mathbf f_C=\mathbf v_C^\ast-\mathbf v_0$를 근사적으로 풀고 각 접촉의 충격량을 마찰원뿔에 투영한다. 이 근사에서는 접촉점 사이의 결합을 생략한다. | 접촉 사이의 결합을 생략하는 근사 | [§II-E 대각 해법 · PDF 5쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=5) |

## Main Results / Claim–Evidence Map

| Claim or target | Result/condition cue | Evidence strength | Anchor |
|---|---|---|---|
| This is useful for approximating derivatives via finite differencing, which in turn enables numerical optimization. • Inverse dynamics can always be computed, even in ... | Although this approach is a significant improvement over earlier spring-damper models of contact, it still requires manual tuning and small time steps. | PDF body cue; verify exact table/figure and matched conditions | p. 2 (I. INTRODUCTION), p. 4 (5) Integrate numerically to obtain the next state), p. 5 (5) Integrate numerically to obtain the next state), p. 5 (5) Integrate numerically to obtain the next state), p. 3 (5) Integrate numerically to obtain the next state), p. 4 (5) Integrate numerically to obtain the next state) |
| 비선형 해법의 계산 비용 | 각 뉴턴 반복에서 $k\times k$ 행렬을 LU 분해한다. $k$는 접촉 충격량 벡터의 차원이다(§II-B). | 반복당 분해 크기 | [§II-C 비선형 해법 · PDF 4쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=4) |

- Numeric sentences retained from the body:
- 등식 제약이 없을 때는 $P=M^{-1}$, $\mathbf r=M^{-1}\mathbf s$가 된다. [§II-A 식 2 아래 · PDF 3쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=3)
- 법선 방향에서는 $f^{\mathcal N}\ge0$, $v^{\mathcal N}\ge0$, $f^{\mathcal N}v^{\mathcal N}=0$이라는 상보성 조건을 적용한다. [§II-B 식 4 · PDF 3쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=3)

## Generalization and Failure Cases

| Body cue type | Observed cue or missing regime | Anchor |
|---|---|---|
| body limitation/failure cue | 1) Compute the Cartesian positions and orientations of all rigid bodies (i.e. the forward kinematics), detect potential collisions (with some safety margin), and construct ... | p. 3 (II. ALGORITHMIC FOUNDATIONS) |
| 쿨롱 마찰 모델 | 접선 속도와 마찰 충격량은 평행하고 $\langle\mathbf v^{\mathcal F},\mathbf f^{\mathcal F}\rangle\le0$이다. 마찰원뿔의 경계는 $\lVert\mathbf f^{\mathcal F}\rVert\le\mu f^{\mathcal N}$이며 $\mu$는 마찰계수다. | [§II-B 식 5 · PDF 3쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=3) |
| body limitation/failure cue | Since the underlying problem is NP-hard, the algorithm cannot always find the exact solution (which has 0 residual). | p. 4 (5) Integrate numerically to obtain the next state) |
| 접촉 행렬의 특이성 | 볼록 접촉 해법은 특이할 수 있는 $A$에 대각 정규화 행렬 $R$을 더한다. 접촉 거리와 함께 $R$을 키우면 떨어진 물체 사이에도 약한 접촉력을 모델링할 수 있다. | [§II-D 식 6 · PDF 4쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=4) |
| 대각 해법의 가정 | 대각 해법은 관입이 임계 감쇠 스프링처럼 줄고 미끄러짐이 없을 때의 다음 접촉 속도 $\mathbf v_C^\ast$를 목표로 둔다. | [§II-E 대각 해법 · PDF 5쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=5) |
| body limitation/failure cue | Their primary use in the engine is collision detection as well as tendon wrapping. | p. 7 (III. MODELING) |

## Statistics, Efficiency, and Reproducibility

| Body reproducibility cue | Anchor |
|---|---|
| $M^{-1}$과의 곱은 희소 분해 뒤 후진 대입으로 계산한다. 반복해서 쓰는 $M^{-1}J_E^\top=(J_E M^{-1})^\top$는 저장해 재사용한다. | [§II-A 희소 행렬 계산 · PDF 3쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=3) |
| The procedure for solving the above equations of motion consists of the following steps: | p. 2 (II. ALGORITHMIC FOUNDATIONS) |
| Although this approach is a significant improvement over earlier spring-damper models of contact, it still requires manual tuning and small time steps. | p. 2 (I. INTRODUCTION) |
| $A\mathbf f_C+\mathbf v_0=\mathbf v_C$에서 $A=J_C P J_C^\top$와 $\mathbf v_0=J_C\mathbf r$는 알려져 있다. 미지수는 접촉 충격량 $\mathbf f_C$와 접촉 속도 $\mathbf v_C$다. | [§II-B 식 3 · PDF 3쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=3) |
| In the normal direction for example, if the corresponding component of x is positive it encodes force (in which case the velocity is 0), ... | p. 4 (5) Integrate numerically to obtain the next state) |
| Convex solver A favorable trade-off between speed and accuracy is obtained by replacing the nonlinear complementarity constraints (4, 5) with a convex optimization problem, ... | p. 4 (5) Integrate numerically to obtain the next state) |
| 접촉이 없는 순동역학은 자유도 $n$에 대해 $O(n)$인 재귀 알고리즘으로도 계산할 수 있다. | [§II-F 계산 복잡도 · PDF 5쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=5) |
| It can be used to analyze data or to compute the torques that will cause a robot to follow a reference trajectory. | p. 5 (5) Integrate numerically to obtain the next state) |

## Limitations and Verification Questions

- **p. 3 / II. ALGORITHMIC FOUNDATIONS - extractive body cue:** 1) Compute the Cartesian positions and orientations of all rigid bodies (i.e. the forward kinematics), detect potential collisions (with some safety margin), and construct the ...
- 접선 속도와 마찰 충격량은 평행하고 $\langle\mathbf v^{\mathcal F},\mathbf f^{\mathcal F}\rangle\le0$이다. 마찰원뿔의 경계는 $\lVert\mathbf f^{\mathcal F}\rVert\le\mu f^{\mathcal N}$이며 $\mu$는 마찰계수다. [§II-B 식 5 · PDF 3쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=3)
- **p. 4 / 5) Integrate numerically to obtain the next state - extractive body cue:** Since the underlying problem is NP-hard, the algorithm cannot always find the exact solution (which has 0 residual).
- 볼록 접촉 해법은 특이할 수 있는 $A$에 대각 정규화 행렬 $R$을 더한다. 접촉 거리와 함께 $R$을 키우면 떨어진 물체 사이에도 약한 접촉력을 모델링할 수 있다. [§II-D 식 6 · PDF 4쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=4)
- 대각 해법은 관입이 임계 감쇠 스프링처럼 줄고 미끄러짐이 없을 때의 다음 접촉 속도 $\mathbf v_C^\ast$를 목표로 둔다. [§II-E 대각 해법 · PDF 5쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=5)
- **p. 7 / III. MODELING - extractive body cue:** Their primary use in the engine is collision detection as well as tendon wrapping.

- **Evidence anchors reviewed:** datasets p. 5 (5) Integrate numerically to obtain the next state), p. 2 (I. INTRODUCTION), p. 5 (5) Integrate numerically to obtain the next state), p. 6 (III. MODELING), p. 2 (I. INTRODUCTION), p. 4 (5) Integrate numerically to obtain the next state), metrics p. 4 (5) Integrate numerically to obtain the next state), p. 4 (5) Integrate numerically to obtain the next state), p. 5 (5) Integrate numerically to obtain the next state), p. 2 (I. INTRODUCTION), p. 3 (5) Integrate numerically to obtain the next state), p. 3 (5) Integrate numerically to obtain the next state), baselines p. 7 (IV. TIMING TESTS), p. 2 (I. INTRODUCTION), p. 4 (5) Integrate numerically to obtain the next state), p. 6 (5) Integrate numerically to obtain the next state), p. 6 (III. MODELING), p. 7 (IV. TIMING TESTS), results p. 2 (I. INTRODUCTION), p. 4 (5) Integrate numerically to obtain the next state), p. 5 (5) Integrate numerically to obtain the next state), p. 5 (5) Integrate numerically to obtain the next state), p. 3 (5) Integrate numerically to obtain the next state), p. 4 (5) Integrate numerically to obtain the next state).

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Evaluation setup/result:** Table 3: This is the inverse of Table 2. Here we show the number of dynamics evaluations per second. The results are quite remarkable. One a single desktop machine, we ... (p. 8, Figure/Table caption).
- **Metric evidence:** Solving for the contact impulse We now return to step 4. (p. 3, 5) Integrate numerically to obtain the next state).
- **Baseline/ablation evidence:** Section IV presents timing tests and comparisons to SD/FAST - which does not handle contacts, but is the best prior engine for multi-joint dynamics in our opinion. (p. 2, I. INTRODUCTION).
- **Failure/negative evidence:** In the absence of adequate tools, the field continues to rely on manual controller designs - which may be a large part of the reason why present-day robots do not ... (p. 1, I. INTRODUCTION).
