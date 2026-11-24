# Method - MuJoCo: A Physics Engine for Model-Based Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://api.crossref.org/works/10.1109/IROS.2012.6386109; PDF retrieval source: https://doi.org/10.1109/IROS.2012.6386109. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

## Method in One Sentence

PDF body method statement (p. 7 (III. MODELING), p. 2 (II. ALGORITHMIC FOUNDATIONS), p. 2 (II. ALGORITHMIC FOUNDATIONS), p. 6 (III. MODELING), p. 6 (III. MODELING), p. 7 (III. MODELING)): The tendon path is the shortest path that passes through a sequence of specified sites or wraps around specified geoms. h) Actuator: Actuators have control inputs, optional activation states (used ...

## Method Body Digest

- **p. 7 / III. MODELING - extractive body cue:** The tendon path is the shortest path that passes through a sequence of specified sites or wraps around specified geoms. h) Actuator: Actuators have control ...
- **p. 2 / II. ALGORITHMIC FOUNDATIONS - extractive body cue:** We start with notation and smooth dynamics which are fairly standard, then explain the contact simulation algorithms in more detail, followed by computational complexity and ...
- $q$와 $v$는 일반화 좌표의 위치와 속도, $M$은 관성 행렬이다. $b$는 코리올리·원심·중력·스프링 항을 포함하는 편향력이다. [§II-A 운동 방정식 · PDF 2쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=2)
- 하나의 MuJoCo 모델은 하나 이상의 운동학적 트리로 구성된다. 각 트리의 기저는 공간에서 자유롭게 움직일 수 있어 독립된 물체도 표현할 수 있다. [§III-B 강체 모델 · PDF 6쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=6)
- **p. 6 / III. MODELING - extractive body cue:** A full explanation of the modeling convention is beyond the scope of this paper, but one important feature is the ability to specify body inertial ...
- **p. 7 / III. MODELING - extractive body cue:** However they can also be used during model construction to specify the inertial properties of the body to which they belong.
- **p. 2 / II. ALGORITHMIC FOUNDATIONS - extractive body cue:** The procedure for solving the above equations of motion consists of the following steps:
- **p. 7 / III. MODELING - extractive body cue:** They are used in the engine to route tendons and apply certain types of forces, but can also be used by the user's program to ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** This is useful for approximating derivatives via finite differencing, which in turn enables numerical optimization. • Inverse dynamics can always be computed, even in the ...
- **p. 2 / II. ALGORITHMIC FOUNDATIONS - extractive body cue:** The procedure for solving the above equations of motion consists of the following steps:
- 하나의 MuJoCo 모델은 하나 이상의 운동학적 트리로 구성된다. 각 트리의 기저는 공간에서 자유롭게 움직일 수 있어 독립된 물체도 표현할 수 있다. [§III-B 강체 모델 · PDF 6쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=6)

## Source Evidence Cues

- **p. 7 / III. MODELING - extractive body cue:** The tendon path is the shortest path that passes through a sequence of specified sites or wraps around specified geoms. h) Actuator: Actuators have control ...
- **p. 2 / II. ALGORITHMIC FOUNDATIONS - extractive body cue:** We start with notation and smooth dynamics which are fairly standard, then explain the contact simulation algorithms in more detail, followed by computational complexity and ...
- 위치 $q$와 속도 $v$를 일반화 좌표로 표현하고, 관성 행렬 $M$과 편향력 $b$로 운동 방정식을 구성한다. [§II-A 운동 방정식 · PDF 2쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=2)
- 하나의 MuJoCo 모델은 하나 이상의 운동학적 트리로 구성된다. 각 트리의 기저는 공간에서 자유롭게 움직일 수 있어 독립된 물체도 표현할 수 있다. [§III-B 강체 모델 · PDF 6쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=6)
- **p. 6 / III. MODELING - extractive body cue:** A full explanation of the modeling convention is beyond the scope of this paper, but one important feature is the ability to specify body inertial ...
- **p. 7 / III. MODELING - extractive body cue:** However they can also be used during model construction to specify the inertial properties of the body to which they belong.
- **Detected method headings:** II. ALGORITHMIC FOUNDATIONS (p. 2); III. MODELING (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Physics state / interface | robot·environment state를 simulator contract로 표현한다 | geometry, dynamics, contact, control input | rigid-body/contact/differentiable state를 구성 | simulator state | The tendon path is the shortest path that passes through a sequence of specified sites or wraps around specified geoms. h) Actuator: ... | p. 7 (III. MODELING), p. 2 (II. ALGORITHMIC FOUNDATIONS) |
| Rollout / model query | candidate action의 consequence를 계산한다 | state와 action | physics step, learned dynamics, parallel 또는 differentiable rollout을 수행 | trajectory/reward/prediction | We start with notation and smooth dynamics which are fairly standard, then explain the contact simulation algorithms in more detail, followed by ... | p. 2 (II. ALGORITHMIC FOUNDATIONS), p. 2 (II. ALGORITHMIC FOUNDATIONS) |
| Learning / transfer handoff | simulation result를 policy 또는 real deployment로 전달한다 | rollout과 task objective | gradient, replay, randomization, calibration 또는 transfer adaptation을 적용 | policy/controller/data | Equations of motion and smooth dynamics We will use the following notation: q position in generalized coordinates v velocity in generalized coordinates ... | p. 2 (II. ALGORITHMIC FOUNDATIONS), p. 6 (III. MODELING) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- 등식 제약을 처리한 뒤, 접촉 충격량 $\mathbf f_C$에서 속도 $\mathbf v=PJ_C^\top\mathbf f_C+\mathbf r$를 구한다. [§II-A 식 2 · PDF 3쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=3)
- **p. 2 / II. ALGORITHMIC FOUNDATIONS - extractive body cue:** The procedure for solving the above equations of motion consists of the following steps:
- **p. 7 / III. MODELING - extractive body cue:** They are used in the engine to route tendons and apply certain types of forces, but can also be used by the user's program to ...
- **p. 7 / III. MODELING - extractive body cue:** MuJoCo has several predefined types of constraints: 3D position constraint forcing two points on two bodies to coincide (effectively creating another ball joint), joint angle ...
- **Formal bridge:** sim state s_t and parameters δ -> sim action/rollout -> physics/model/planning objective -> fidelity, throughput and downstream task utility.
- **Equation/algorithm anchors:** p. 2 (II. ALGORITHMIC FOUNDATIONS), p. 2 (II. ALGORITHMIC FOUNDATIONS), p. 7 (III. MODELING), p. 7 (III. MODELING).
- Do not infer optimizer, sign convention, target-network schedule, solver tolerance or stopping criterion unless the PDF states it.

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | tendon, path, shortest, passes, through, sequence, specified, sites, wraps, around, geoms, Actuator, Actuators, have | simulated state, geometry, contact와 control input | body cue; exact tensor/frame verify |
| State/latent | tendon, path, shortest, passes, through, sequence, specified, sites, wraps, around | dynamics/contact state 또는 learned simulator representation | body cue; notation verify |
| Action/output | useful, approximating, derivatives, finite, differencing, turn, enables, numerical, optimization, Inverse | simulation step, trajectory 또는 environment query | body cue; unit/decoder verify |
| Objective/constraint | Equations, motion, smooth, dynamics, will, following, notation, position, generalized, coordinates | physics/model/planning objective | equation anchor required |

## Observation–State–Action Interface

- **p. 7 / III. MODELING - extractive body cue:** The tendon path is the shortest path that passes through a sequence of specified sites or wraps around specified geoms. h) Actuator: Actuators have control ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** These observations indicated that we need a new engine, representing the state in joint coordinates and simulating contacts in ways that are related to LCP ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** On the other end of the spectrum are engines such as SD/FAST and OpenSim, which represent the system state and perform all computations in joint ...
- **p. 7 / III. MODELING - extractive body cue:** They are used in the engine to route tendons and apply certain types of forces, but can also be used by the user's program to ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Either way, optimizing a controller requires a vast number of dynamics evaluations for different states and controls.
- **p. 1 / I. INTRODUCTION - extractive body cue:** ODE as well as other game-oriented engines (such as NVIDIA PhysX and Bullet Physics) represent the system state in over
- **p. 6 / III. MODELING - extractive body cue:** DOFs have damping, maximum velocity, armature inertia.
- **Normalized interface:** observation=simulated state, geometry, contact와 control input; state=dynamics/contact state 또는 learned simulator representation; output/action=simulation step, trajectory 또는 environment query.
- Verify whether output is directly actuated or passed through a planner, reference generator, controller, decoder or safety filter.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | simulator step, rollout length와 task episode horizon을 분리한다. | Although this approach is a significant improvement over earlier spring-damper models of contact, it still requires manual tuning and small time steps. | episode/sequence/action-chunk boundary |
| Rate / latency | simulation step rate와 learned policy/control rate를 별도로 기록한다. | Equations of motion and smooth dynamics We will use the following notation: q position in generalized coordinates v velocity in generalized coordinates ... | Hz/fps, inference time and control rate |
| Memory | sim state, contact state와 rollout/replay buffer. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | physics solver, parallel environments와 differentiable rollout cost가 결정한다. | not stated or recoverable in the selected PDF body | hardware, batch and throughput |

## Training vs Inference

- 한 스텝에서 일반화 속도를 먼저 갱신하고 그 속도로 위치를 적분한다. [§II-A 식 2 · PDF 3쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=3)
- **p. 4 / 5) Integrate numerically to obtain the next state - extractive body cue:** Convex solver A favorable trade-off between speed and accuracy is obtained by replacing the nonlinear complementarity constraints (4, 5) with a convex optimization problem, whose ...

- Training inputs, privileged information, data augmentation and inference-time feedback must be recorded separately; they are not interchangeable.

## Method-Specific Formal Details

- **Body-defined terms:** tendon, path, shortest, passes, through, sequence, specified, sites, wraps, around, geoms, Actuator, Actuators, have, control, inputs, optional, activation, states, model.
- 식 2는 일반화 속도를 접촉 충격량의 함수로 나타낸다. [§II-A 식 2 · PDF 3쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=3)

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Physics state / interface | It can be used to analyze data or to compute the torques that will cause a robot to follow a reference trajectory. | p. 5 (5) Integrate numerically to obtain the next state), p. 2 (I. INTRODUCTION) |
| Rollout / model query | Performance on smooth dynamics compared to SD/FAST We measured the speed of multi-joint dynamics simulation in the absence of contacts or equality ... | p. 7 (IV. TIMING TESTS), p. 2 (I. INTRODUCTION) |
| Learning / transfer handoff | Although this approach is a significant improvement over earlier spring-damper models of contact, it still requires manual tuning and small time steps. | p. 2 (I. INTRODUCTION), p. 4 (5) Integrate numerically to obtain the next state) |

## Failure and Ablation Link

- 볼록 접촉 해법은 특이할 수 있는 $A$에 대각 정규화 행렬 $R$을 더한다. 접촉 거리와 함께 $R$을 키우면 떨어진 물체 사이에도 약한 접촉력을 모델링할 수 있다. [§II-D 식 6 · PDF 4쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=4)
- **p. 6 / 5) Integrate numerically to obtain the next state - extractive body cue:** When there are no equality constraints and the contact solver has an exact inverse, the inverse dynamics can be computed without resorting to posthoc mode.
- **p. 6 / III. MODELING - extractive body cue:** A unique feature of MuJoCo is that the primitive joint types can be composed into more complex joints, without having to define intermediate dummy bodies. ...
- 단일 접촉의 충격량 $\mathbf f_C$를 법선 성분 $f^{\mathcal N}$과 접선 평면의 두 성분 $\mathbf f^{\mathcal F}\in\mathbb R^2$로 나눈다. [§II-B 접촉 충격량 · PDF 3쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=3)
- **p. 4 / 5) Integrate numerically to obtain the next state - extractive body cue:** In the normal direction for example, if the corresponding component of x is positive it encodes force (in which case the velocity is 0), otherwise ...
- $\operatorname{diag}(A)\mathbf f_C=\mathbf v_C^\ast-\mathbf v_0$를 근사적으로 풀고 각 접촉의 충격량을 마찰원뿔에 투영한다. 이 근사에서는 접촉점 사이의 결합을 생략한다. [§II-E 대각 해법 · PDF 5쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=5)
- **p. 3 / II. ALGORITHMIC FOUNDATIONS - extractive body cue:** 1) Compute the Cartesian positions and orientations of all rigid bodies (i.e. the forward kinematics), detect potential collisions (with some safety margin), and construct the ...

- Causal attribution requires fixing data, input modality, compute, horizon, action interface and controller while removing one component.

## Reproduction Checklist

1. [ ] Re-read the cited method headings and record exact variables, dimensions, units and equation/algorithm numbers.
2. [ ] Separate objective, constraint, initialization, update schedule and inference decoding.
3. [ ] Fix observation preprocessing, action frame, horizon, memory, rate and feedback latency.
4. [ ] Match dataset split, baseline checkpoint, seed/trial count and success denominator from 04.
5. [ ] Re-run the body-reported ablation and at least one failure-boundary stress test.

## Verification Questions

- **Evidence anchors reviewed:** method p. 7 (III. MODELING), p. 2 (II. ALGORITHMIC FOUNDATIONS), p. 2 (II. ALGORITHMIC FOUNDATIONS), p. 6 (III. MODELING), p. 6 (III. MODELING), p. 7 (III. MODELING), objective p. 2 (II. ALGORITHMIC FOUNDATIONS), p. 2 (II. ALGORITHMIC FOUNDATIONS), p. 7 (III. MODELING), p. 7 (III. MODELING), temporal p. 2 (I. INTRODUCTION), p. 2 (II. ALGORITHMIC FOUNDATIONS), p. 3 (5) Integrate numerically to obtain the next state), p. 3 (5) Integrate numerically to obtain the next state), p. 6 (5) Integrate numerically to obtain the next state), p. 7 (IV. TIMING TESTS).
- Which module is genuinely new, and which is inherited infrastructure or a baseline?
- What exact computation consumes each observation and emits each action/output?
- Does the reported runtime include preprocessing, planning, safety filtering and low-level control?
- Are all claims supported by a body section, equation, table or figure rather than the abstract alone?

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** The tendon path is the shortest path that passes through a sequence of specified sites or wraps around specified geoms. h) Actuator: Actuators have control inputs, optional activation states (used ... (p. 7, III. MODELING).
- **속도 갱신.** 등식 제약을 처리한 뒤, 접촉 충격량 $\mathbf f_C$에서 속도 $\mathbf v=PJ_C^\top\mathbf f_C+\mathbf r$를 구한다. [§II-A 식 2 · PDF 3쪽](https://roboti.us/lab/papers/TodorovIROS12.pdf#page=3)
- **Temporal/runtime evidence:** The procedure for solving the above equations of motion consists of the following steps: (p. 2, II. ALGORITHMIC FOUNDATIONS).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
