# Method - LIO-SAM: Tightly-coupled Lidar Inertial Odometry via Smoothing and Mapping

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (8 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2007.00258; PDF retrieval source: https://arxiv.org/pdf/2007.00258. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA2 targeted source review: 2026-10-23; PDF pp. 4. 손상 구간·직접 연결된 표 분류만 원문 이미지와 대조했다. 전체 주장 정독·실험 검증·reading status 승격을 뜻하지 않는다. [URL·PDF hash·수정 기록](../../../../work/sources/pdf_note_review_followup_2026-10-23.json).

## DOC-QA3 — scan-matching solver

**원문 근거:** PDF p. 4 §III-C의 displayed objective에는 거리 residual의 제곱이 명시되지 않는다.

**공식 코드 근거:** ROS1 master의 `scan2MapOptimization`은 corner/plane 대응을 계산하고 `combineOptimizationCoeffs` → `LMOptimization`으로 전달한다. Corner의 거리와 plane의 signed distance에 각각 s를 곱하며 Jacobian 계수에도 s를 곱한다. `b=−coeff.intensity`, `AᵀA`, `Aᵀb`를 구성해 QR로 normal equations를 풀고 degeneracy projection을 적용한다.

**연구자 해석:** 각 선형화 단계는 `minδ ||Aδ−b||²`인 가중 최소제곱이다. 원래 residual 기준으로 weight가 s²이지만, 대응과 s가 갱신되므로 이를 고정된 전역 objective와 동일시하지 않는다. 인쇄된 거리 합을 그대로 L1 solver로 구현하지 않으며, 함수명만으로 damping을 포함한 LM이라고 단정하지 않는다. 2023 commit의 정적 검토이고 2020 논문 실행 버전·성능의 재현은 아니다.

대조 근거: [원문](https://arxiv.org/abs/2007.00258) · [공식 구현 0be1fbe6275f](https://github.com/TixiaoShan/LIO-SAM/blob/0be1fbe6275fb8366d5b800af4fc8c76a885c869/src/mapOptmization.cpp#L1182-L1255) · [전체 호출 경로·파일 hash](../../../../work/sources/paper_code_formula_review_2026-10-23.json). 검토일 2026-10-23. 지정 구간을 정적으로 읽었으며 코드 실행·의존성 설치는 하지 않았다. 논문 실험과 이 commit의 동일성 및 저자 확인 정오표는 미확인이다. 사용자 reading status는 유지한다.

## Method in One Sentence

PDF body method statement (p. 2 (III. LIDAR INERTIAL ODOMETRY VIA), p. 3 (III. LIDAR INERTIAL ODOMETRY VIA), p. 3 (III. LIDAR INERTIAL ODOMETRY VIA), p. 1 (Abstract), p. 2 (III. LIDAR INERTIAL ODOMETRY VIA), p. 4 (III. LIDAR INERTIAL ODOMETRY VIA)): We use a factor graph to model this problem, as it is better suited to perform inference when compared with Bayes nets.

## Method Body Digest

- **p. 2 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** We use a factor graph to model this problem, as it is better suited to perform inference when compared with Bayes nets.
- **p. 3 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** Since we extract two types of features in the previous feature extraction step, Mi is composed of two subvoxel maps that are denoted Me i, ...
- **p. 3 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** Lidar Odometry Factor When a new lidar scan arrives, we first perform feature extraction.
- **p. 1 / Abstract - extractive body cue:** We propose a framework for tightly-coupled lidar inertial odometry via smoothing and mapping, LIO-SAM, that achieves highly accurate, real-time mobile robot trajectory estimation and map-building.
- **p. 2 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** We seek to estimate the state of the robot and its trajectory using the observations of these sensors.
- **p. 4 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** each feature in ′Fe i+1 or ′Fp i+1, we then find its edge or planar correspondence in Me i or Mp i .
- **p. 4 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** When a new state xi+1 is added to the factor graph, we first search the graph and find the prior states that are close to ...
- **p. 2 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** Note that without loss of generality, the proposed system can also incorporate measurements from other sensors, such as elevation from an altimeter or heading from ...

## Design Rationale

- **p. 1 / I. INTRODUCTION - extractive body cue:** Scan-matching at a local scale instead of a global scale significantly improves the real-time performance of the system, as does the selective introduction of keyframes, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** In this paper, we propose a framework for tightly-coupled lidar inertial odometry via smoothing and mapping, LIOSAM, to address the aforementioned problems.
- **p. 2 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** We introduce four types of factors along with one variable type for factor graph construction.

## Source Evidence Cues

- **p. 2 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** We use a factor graph to model this problem, as it is better suited to perform inference when compared with Bayes nets.
- **p. 3 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** Since we extract two types of features in the previous feature extraction step, Mi is composed of two subvoxel maps that are denoted Me i, ...
- **p. 3 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** Lidar Odometry Factor When a new lidar scan arrives, we first perform feature extraction.
- **p. 1 / Abstract - extractive body cue:** We propose a framework for tightly-coupled lidar inertial odometry via smoothing and mapping, LIO-SAM, that achieves highly accurate, real-time mobile robot trajectory estimation and map-building.
- **p. 2 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** We seek to estimate the state of the robot and its trajectory using the observations of these sensors.
- **p. 4 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** each feature in ′Fe i+1 or ′Fp i+1, we then find its edge or planar correspondence in Me i or Mp i .
- **p. 4 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** When a new state xi+1 is added to the factor graph, we first search the graph and find the prior states that are close to ...
- **Detected method headings:** none reliably recovered

## Pipeline

라이다 점군·IMU와 선택적 GPS 관측 → 관성·라이다·루프 폐쇄·GPS의 요인 그래프 → 추정 궤적과 지도. [방법·평가의 원문 근거](./01_overview.md#observation-state-and-output-interface)

## Objective / Update Rule

- **p. 2 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** Note that without loss of generality, the proposed system can also incorporate measurements from other sensors, such as elevation from an altimeter or heading from ...
- **p. 3 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** Besides its efficiency, applying IMU preintegration also naturally gives us one type of constraint for the factor graph - IMU preintegration factors.
- **PDF p. 4, §III-C scan matching (DOC-QA2 원문 대조):** Gauss–Newton으로 edge-feature point-to-line distances와 planar-feature point-to-plane distances를 합한 scan-matching objective를 최소화해 transformation을 얻는다. 해당 PDF의 displayed objective에는 d_k^e와 d_k^p의 제곱이 따로 표기되지 않아 관행적인 squared-residual 식으로 임의 변경하지 않았다.
- **p. 4 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** 3) Relative transformation: The distance between a feature and its edge or planar patch correspondence can be computed using the following equations: dek =
- **p. 1 / I. INTRODUCTION - extractive body cue:** This collection of factors from various sources is used for joint optimization of the graph.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Its online optimization process becomes less efficient when this voxel map becomes dense in a feature-rich environment.
- **Formal bridge:** 라이다 점군·IMU와 선택적 GPS 관측 → 관성·라이다·루프 폐쇄·GPS의 요인 그래프 → 추정 궤적과 지도.
- **Equation/algorithm anchors:** p. 2 (III. LIDAR INERTIAL ODOMETRY VIA), p. 3 (III. LIDAR INERTIAL ODOMETRY VIA), p. 4 (III. LIDAR INERTIAL ODOMETRY VIA), p. 4 (III. LIDAR INERTIAL ODOMETRY VIA).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | seek, estimate, state, robot, trajectory, observations, sensors, estimation, localization, mapping, fundamental, prerequisites, successful, intelligent | 라이다 점군·IMU와 선택적 GPS 관측 | body cue; exact tensor/frame verify |
| State/latent | seek, estimate, state, robot, trajectory, observations, sensors, estimation, localization, mapping | 관성·라이다·루프 폐쇄·GPS의 요인 그래프 | body cue; notation verify |
| Action/output | Scan-matching, local, scale, instead, global, significantly, improves, real-time, performance, system | 추정 궤적과 지도 | body cue; unit/decoder verify |
| Objective/constraint | Note, without, loss, generality, system, incorporate, measurements, other, sensors, elevation | path cost, risk or goal utility | equation anchor required |

## Observation–State–Action Interface

- **p. 2 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** We seek to estimate the state of the robot and its trajectory using the observations of these sensors.
- **p. 1 / I. INTRODUCTION - extractive body cue:** State estimation, localization and mapping are fundamental prerequisites for a successful intelligent mobile robot, required for feedback control, obstacle avoidance, and planning, among many other ...
- **p. 3 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** Since we extract two types of features in the previous feature extraction step, Mi is composed of two subvoxel maps that are denoted Me i, ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** Many lidar-based state estimation and mapping methods have been proposed in the last two decades.
- **p. 2 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** This state estimation problem can be formulated as a maximum a posteriori (MAP) problem.
- **p. 3 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** A new robot state node x is added to the graph when the change in robot pose exceeds a user-defined threshold.
- **p. 4 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** Throughout this paper, we choose the index m to be 12, and the search distance for loop closures is set to be 15m from a ...
- **Normalized interface:** observation=라이다 점군·IMU와 선택적 GPS 관측; state=관성·라이다·루프 폐쇄·GPS의 요인 그래프; output/action=추정 궤적과 지도.

## Temporal and Runtime Contract

| Contract | PDF body cue | Unresolved detail |
|---|---|---|
| Horizon | Adding keyframes in this way not only achieves a balance between map density and memory consumption but also helps maintain a relatively ... | episode/sequence/action-chunk boundary |
| Rate / latency | We propose a framework for tightly-coupled lidar inertial odometry via smoothing and mapping, LIO-SAM, that achieves highly accurate, real-time mobile robot trajectory ... | Hz/fps, inference time and control rate |
| Memory | Adding keyframes in this way not only achieves a balance between map density and memory consumption but also helps maintain a relatively ... | window and reset |
| Compute | In other words, some lidar frames are dropped if the runtime takes more than 100ms when the lidar rotation rate is 10Hz. | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / III. LIDAR INERTIAL ODOMETRY VIA - extractive body cue:** We use a factor graph to model this problem, as it is better suited to perform inference when compared with Bayes nets.

## Method-Specific Formal Details

- **Body-defined terms:** factor, graph, model, problem, better, suited, perform, inference, when, compared, Bayes, nets, Since, extract, types, features, previous, feature, extraction, step.
- **Relevant PDF headings:** not reliably recovered.

## Evaluation Link

| 평가 근거 | 원문에서 추출한 내용 | 원문 위치 |
|---|---|---|
| 원문 대조 | Similar to the problems encountered in the Park dataset, LIO-GPS is unable to close the loop when returning to the robot's initial ... | p. 6 (IV. EXPERIMENTS), p. 6 (IV. EXPERIMENTS) |
| 원문 대조 | The maximum data playback speed is recorded and shown in the last column of Table IV when LIO-SAM achieves similar performance without ... | p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |
| 원문 대조 | The maximum data playback speed is recorded and shown in the last column of Table IV when LIO-SAM achieves similar performance without ... | p. 7 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS) |

## Failure and Ablation Link

- **p. 5 / IV. EXPERIMENTS - extractive body cue:** We note that only the CPU is used for computation, without parallel computing enabled.
- **p. 5 / IV. EXPERIMENTS - extractive body cue:** Because LIOM uses the same initialization pipeline from [25], it inherits the same initialization sensitivity of visual-inertial SLAM and is not able to initialize properly ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** Without the correction of GPS data, the trajectory of LIO-odom begins to visibly drift at the lower right corner of the map.
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** LIO-SAM produces a map that is consistent with the Google Earth imagery, without using GPS. mapping area, GPS reception is rarely available and inaccurate most ...
- **p. 7 / IV. EXPERIMENTS - extractive body cue:** The maximum data playback speed is recorded and shown in the last column of Table IV when LIO-SAM achieves similar performance without failure compared with ...
- **p. 7 / Figure/Table caption - extractive body cue:** Fig. 5: Results of various methods using the Campus dataset that is gathered on the MIT campus. The red dot indicates the start and end ...
- **p. 6 / IV. EXPERIMENTS - extractive body cue:** The results of LIOM are not shown due to its failure to initialize properly and produce meaningful results.

## Reproduction Checklist

[공통 검토 기준](../../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 2 (III. LIDAR INERTIAL ODOMETRY VIA), p. 3 (III. LIDAR INERTIAL ODOMETRY VIA), p. 3 (III. LIDAR INERTIAL ODOMETRY VIA), p. 1 (Abstract), p. 2 (III. LIDAR INERTIAL ODOMETRY VIA), p. 4 (III. LIDAR INERTIAL ODOMETRY VIA), objective p. 2 (III. LIDAR INERTIAL ODOMETRY VIA), p. 3 (III. LIDAR INERTIAL ODOMETRY VIA), p. 4 (III. LIDAR INERTIAL ODOMETRY VIA), p. 4 (III. LIDAR INERTIAL ODOMETRY VIA), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), temporal p. 3 (III. LIDAR INERTIAL ODOMETRY VIA), p. 1 (Abstract), p. 1 (Abstract), p. 4 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS), p. 5 (IV. EXPERIMENTS).
