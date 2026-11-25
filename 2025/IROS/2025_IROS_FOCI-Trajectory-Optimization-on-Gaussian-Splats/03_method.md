# Method - FOCI: Trajectory Optimization on Gaussian Splats

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2505.08510; PDF retrieval source: https://arxiv.org/pdf/2505.08510. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

- **원문 대조:** 균일 cubic B-spline의 각 segment는 네 control point의 가중합이다. H개 control point에서 H−3개 segment를 만들고, 이산화한 trajectory는 X=ΦQ로 표현한다. 잘린 행렬은 원문의 식 (1)을 참조한다. ([PDF p. 3](https://arxiv.org/pdf/2505.08510#page=3), §III-A Trajectory Representation, Eqs. (1)–(2)).

## Method Body Digest

- **원문 대조:** 균일 cubic B-spline의 각 segment는 네 control point의 가중합이다. H개 control point에서 H−3개 segment를 만들고, 이산화한 trajectory는 X=ΦQ로 표현한다. 잘린 행렬은 원문의 식 (1)을 참조한다. ([PDF p. 3](https://arxiv.org/pdf/2505.08510#page=3), §III-A Trajectory Representation, Eqs. (1)–(2)).
- **p. 3 / III. METHOD - extractive body cue:** Our methodology can be split into three parts: 1) trajectory representation to create an initial spline, 2) collision measure and 3) optimization loop.
- **p. 4 / III. METHOD - extractive body cue:** The optimization problem is then solved via the interior point method (IPOPT) [28] with the custom overlap integral functor.
- **p. 4 / III. METHOD - extractive body cue:** Instead of directly constraining samples of the respective derivatives of the spline along the trajectory, we leverage the convex hull property of splines.
- **p. 6 / Method - extractive body cue:** A linear relation between robot complexity and optimization time shows the potential of modeling more complex robot geometry, allowing even tighter safety corridors on more ...
- **p. 6 / Method - extractive body cue:** Three metrics are used for evaluation, the speed of optimization, a path length relative to the scene scale, and minimum distance between the robot model ...
- **p. 7 / Method - extractive body cue:** 6: Optimization time for orientation-aware planning using increasingly complex robot models.
- **p. 4 / III. METHOD - extractive body cue:** We minimize the weighted sum of the obstacle cost, the jerk along the trajectory, and the distance of the final point to the goal with ...

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we propose an algorithm that enables a robot to perform trajectory optimization directly on the 3D Gaussians.
- **p. 2 / I. INTRODUCTION - extractive body cue:** The contributions of this work are therefore summarized as follows: • A novel collision measure between Gaussian Splats based on the overlap integral between Gaussians. ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** To overcome these challenges, we propose FOCI, a trajectory optimization algorithm that leverages the overlap integral - the spatial integral over the multiplication of two ...

## Source Evidence Cues

- **원문 대조:** 균일 cubic B-spline의 각 segment는 네 control point의 가중합이다. H개 control point에서 H−3개 segment를 만들고, 이산화한 trajectory는 X=ΦQ로 표현한다. 잘린 행렬은 원문의 식 (1)을 참조한다. ([PDF p. 3](https://arxiv.org/pdf/2505.08510#page=3), §III-A Trajectory Representation, Eqs. (1)–(2)).
- **p. 3 / III. METHOD - extractive body cue:** Our methodology can be split into three parts: 1) trajectory representation to create an initial spline, 2) collision measure and 3) optimization loop.
- **p. 4 / III. METHOD - extractive body cue:** The optimization problem is then solved via the interior point method (IPOPT) [28] with the custom overlap integral functor.
- **p. 4 / III. METHOD - extractive body cue:** Instead of directly constraining samples of the respective derivatives of the spline along the trajectory, we leverage the convex hull property of splines.
- **p. 6 / Method - extractive body cue:** A linear relation between robot complexity and optimization time shows the potential of modeling more complex robot geometry, allowing even tighter safety corridors on more ...
- **p. 6 / Method - extractive body cue:** Three metrics are used for evaluation, the speed of optimization, a path length relative to the scene scale, and minimum distance between the robot model ...
- **p. 7 / Method - extractive body cue:** 6: Optimization time for orientation-aware planning using increasingly complex robot models.
- **Detected method headings:** III. METHOD (p. 3); Method (p. 6)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| Trajectory representation | Smooth differentiable path 구성 | H개 control point | Cubic B-spline segment 평가 | Position/yaw trajectory; geometry 추정 단계와 구분 | 원문 대조: 균일 cubic B-spline의 각 segment는 네 control point의 가중합이다. H개 control point에서 H−3개 segment를 만들고, 이산화한 trajectory는 X=ΦQ로 표현한다. 잘린 행렬은 원문의 식 (1)을 참조한다. ([PDF p. 3](https://arxiv.org/pdf/2505.08510#page=3), §III-A Trajectory Representation, Eqs. (1)–(2)) | [PDF p. 3](https://arxiv.org/pdf/2505.08510#page=3), §III-A Trajectory Representation, Eqs. (1)–(2) |
| Semantic / temporal fusion | geometry에 semantics와 history를 정렬한다 | geometry, visual/language feature와 temporal context | feature lifting, scene graph, map update, tracking 또는 temporal fusion을 수행 | queryable 3D state | Our methodology can be split into three parts: 1) trajectory representation to create an initial spline, 2) collision measure and 3) optimization ... | p. 3 (III. METHOD), p. 4 (III. METHOD) |
| Robot query / planning handoff | 3D state를 task decision에 전달한다 | map/feature와 task query | target grounding, affordance, collision/free-space 또는 action cue를 생성 | goal, pose, path 또는 policy input | The optimization problem is then solved via the interior point method (IPOPT) [28] with the custom overlap integral functor. | p. 4 (III. METHOD), p. 4 (III. METHOD) |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 4 / III. METHOD - extractive body cue:** We minimize the weighted sum of the obstacle cost, the jerk along the trajectory, and the distance of the final point to the goal with ...
- **p. 4 / III. METHOD - extractive body cue:** The collision avoidance is included in the objective function instead of the constraints because the collision measure is not normalized, making finding an appropriate threshold ...
- **p. 3 / III. METHOD - extractive body cue:** 3) It should be differentiable to allow for gradient evaluations in optimization.
- **원문 대조:** 균일 cubic B-spline의 각 segment는 네 control point의 가중합이다. H개 control point에서 H−3개 segment를 만들고, 이산화한 trajectory는 X=ΦQ로 표현한다. 잘린 행렬은 원문의 식 (1)을 참조한다. ([PDF p. 3](https://arxiv.org/pdf/2505.08510#page=3), §III-A Trajectory Representation, Eqs. (1)–(2)).
- **p. 6 / Method - extractive body cue:** Runtime We evaluate the performance of our method by comparing the runtimes of the Casadi optimization on a single CPU core, multiple CPU cores, and ...
- **p. 6 / Method - extractive body cue:** A linear relation between robot complexity and optimization time shows the potential of modeling more complex robot geometry, allowing even tighter safety corridors on more ...
- **Formal bridge:** image/point input I/P and pose -> geometry/map/query r -> geometric/semantic reconstruction or matching loss -> spatial accuracy and downstream robot utility.
- **Equation/algorithm anchors:** p. 4 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | Since, spline, segment, lies, within, convex, hull, control, points, enough, constrain, norm, velocity, acceleration | RGB-D, image set, point cloud, depth와 camera pose | body cue; exact tensor/frame verify |
| State/latent | Since, spline, segment, lies, within, convex, hull, control, points, enough | geometry, map, object/relationship state | body cue; notation verify |
| Action/output | algorithm, enables, robot, perform, trajectory, optimization, directly, Gaussians, contributions, therefore | point map, pose, scene graph, affordance 또는 query result | body cue; unit/decoder verify |
| Objective/constraint | minimize, weighted, obstacle, cost, jerk, along, trajectory, distance, final, point | geometric/semantic reconstruction or matching loss | equation anchor required |

## Observation–State–Action Interface

- **p. 4 / III. METHOD - extractive body cue:** Since each spline segment lies within the convex hull of its control points, it is enough to constrain the norm of the velocity and acceleration ...
- **p. 6 / Method - extractive body cue:** In comparisons with similar methods (Table III, Figure 7) we are able to surpass the speed of traditional methods such as RRT* on large complex ...
- **p. 3 / III. METHOD - extractive body cue:** Instead of the full pose, only the position p ∈R3 and yaw angle ψ ∈R are optimized.
- **p. 3 / III. METHOD - extractive body cue:** Spline representations for Lie Groups have been discussed in robotics literature [22], which allow for pose optimization in SE(3), encoding orientations.
- **p. 4 / III. METHOD - extractive body cue:** We constrain the initial pose of the trajectory to the current position xstart.
- **p. 6 / Method - extractive body cue:** The narrow passages visible in Figure 4 required the robot to rotate in order to safely traverse the environment, while obstacles on the ground forced ...
- **p. 7 / Method - extractive body cue:** 7: The collection of paths used to evaluate different methods with various start and end goals around Stonehenge.
- **Normalized interface:** observation=RGB-D, image set, point cloud, depth와 camera pose; state=geometry, map, object/relationship state; output/action=point map, pose, scene graph, affordance 또는 query result.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | single frame, multi-view accumulation 또는 online map horizon; exact window 확인 필요. | Although this formulation is fully compatible with the proposed framework, we decided to follow a simpler parameterization because our target platform is ... | episode/sequence/action-chunk boundary |
| Rate / latency | 해당 근거는 spline 정의이므로 실행 속도를 확인하지 못함 | 원문 대조: 균일 cubic B-spline의 각 segment는 네 control point의 가중합이다. H개 control point에서 H−3개 segment를 만들고, 이산화한 trajectory는 X=ΦQ로 표현한다. 잘린 행렬은 원문의 식 (1)을 참조한다. ([PDF p. 3](https://arxiv.org/pdf/2505.08510#page=3), §III-A Trajectory Representation, Eqs. (1)–(2)) | Timing table 별도 확인 필요 |
| Memory | camera poses, map/scene graph/Gaussian state와 temporal feature. | not stated or recoverable in the selected PDF body | window and reset |
| Compute | 해당 근거는 X=ΦQ 표현이며 계산시간 수치가 아님 | 원문 대조: 균일 cubic B-spline의 각 segment는 네 control point의 가중합이다. H개 control point에서 H−3개 segment를 만들고, 이산화한 trajectory는 X=ΦQ로 표현한다. 잘린 행렬은 원문의 식 (1)을 참조한다. ([PDF p. 3](https://arxiv.org/pdf/2505.08510#page=3), §III-A Trajectory Representation, Eqs. (1)–(2)) | Hardware·throughput 별도 확인 필요 |

## Training vs Inference

- **p. 4 / III. METHOD - extractive body cue:** Instead of directly constraining samples of the respective derivatives of the spline along the trajectory, we leverage the convex hull property of splines.

## Method-Specific Formal Details

- **Body-defined terms:** spline, then, evaluated, discretizing, trajectory, discretization, points, constructing, matrix, Equation, progress, step, relationship, between, discretized, point, control, given, methodology, split.
- **Relevant PDF headings:** III. METHOD (p. 3); Method (p. 6).

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| Geometry / pose extraction | Environment Initial Guess Time Solve Time # of Gaussians Narrow Corridor 0.24s 0.47s 24k Pillars 0.25s 0.45s 49k Machine Hall 0.22s 2.12s ... | p. 5 (A. Trajectory Evaluation), p. 5 (A. Trajectory Evaluation) |
| Semantic / temporal fusion | Fig. 5: Comparison of the solver's creation and runtime running on the CPU and GPU for 50k environmental Gaus- sians and one ... | p. 7 (Figure/Table caption) |
| Robot query / planning handoff | 8: Optimized trajectory for which the collision avoidance fails. b) Trajectories are parameterized over an interval that depends only on the number ... | p. 7 (V. LIMITATIONS), p. 7 (V. LIMITATIONS) |

## Failure and Ablation Link

- **p. 7 / V. LIMITATIONS - extractive body cue:** 8: Optimized trajectory for which the collision avoidance fails. b) Trajectories are parameterized over an interval that depends only on the number of control points.
- **p. 7 / V. LIMITATIONS - extractive body cue:** This means that when computing the overlap integral over the environment, flat regions with text or patterns have a slightly higher collision cost than
- **p. 5 / A. Trajectory Evaluation - extractive body cue:** As Figure 2b shows, the planning algorithm effectively leverages the asymmetry of ANYmal to pass through the narrow opening collision-free.
- **p. 5 / A. Trajectory Evaluation - extractive body cue:** 2) General Trajectory Planning Through 3DGS: Figure 3 shows that we can plan collision-free trajectories through splats that were created directly from the real-world environments.

## Reproduction Checklist

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 4 (III. METHOD), p. 6 (Method), p. 6 (Method), objective p. 4 (III. METHOD), p. 4 (III. METHOD), p. 3 (III. METHOD), p. 3 (III. METHOD), p. 6 (Method), p. 6 (Method), temporal p. 3 (III. METHOD), p. 3 (III. METHOD), p. 4 (III. METHOD), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION).

## Semantic QA — PDF body cross-check

> Cross-checked on 2026-09-03 against the validated PDF body (8 pages; PyMuPDF text; extraction quality: high; title-token overlap: 1.0). This block is a source-quality correction and does not change reading status.

- **Paper-specific method/interface:** Our methodology can be split into three parts: 1) trajectory representation to create an initial spline, 2) collision measure and 3) optimization loop. (p. 3, III. METHOD).
- **Objective/update evidence:** 3) It should be differentiable to allow for gradient evaluations in optimization. (p. 3, III. METHOD).
- **Temporal/runtime evidence:** Although this formulation is fully compatible with the proposed framework, we decided to follow a simpler parameterization because our target platform is a legged robot. (p. 3, III. METHOD).
- **Implementation boundary:** architecture labels are not treated as paper-specific operations without a body anchor.
