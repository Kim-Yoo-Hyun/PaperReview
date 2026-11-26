# Method - FAST-LIO2: Fast Direct LiDAR-inertial Odometry

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-03 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2107.06829; PDF retrieval source: https://arxiv.org/pdf/2107.06829. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Method in One Sentence

PDF body method statement (p. 4 (IV. STATE ESTIMATION), p. 7 (V. MAPPING), p. 4 (IV. STATE ESTIMATION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 5 (IV. STATE ESTIMATION)): Kinematic Model We first derive the system model, which consists of a state transition model and a measurement model.

## Method Body Digest

- **p. 4 / IV. STATE ESTIMATION - extractive body cue:** Kinematic Model We first derive the system model, which consists of a state transition model and a measurement model.
- **p. 7 / V. MAPPING - extractive body cue:** For a given point p in {G¯pj} from the state estimation module (see Algorithm 1) and downsample resolution l, the algorithm partitions the space evenly ...
- **원문 대조:** 첫 IMU frame을 전역 좌표계 G로 두며, LiDAR–IMU 외부 파라미터를 회전과 병진의 쌍 I_T_L=(I_R_L, I_p_L)로 나타낸다. ([PDF p. 4](https://arxiv.org/pdf/2107.06829#page=4), §IV-A.1 State Transition Model).
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, the performance of the feature extraction module is easily influenced by the environment.
- **p. 1 / I. INTRODUCTION - extractive body cue:** The localization provides state feedback for the robot onboard controllers, while the dense 3D map provides necessary information about the environment (i.e., free space and ...
- **p. 5 / IV. STATE ESTIMATION - extractive body cue:** It consists of two key steps: propagation upon each IMU measurement and iterated update upon each LiDAR scan, both step estimates the state naturally on ...
- **p. 5 / IV. STATE ESTIMATION - extractive body cue:** IV-B3) is bxκ k, when κ = 0 (i.e., before the first iteration), bxκ k = bxk, the predicted state from the propagation in (6).
- **p. 2 / I. INTRODUCTION - extractive body cue:** Besides efficient nearest neighbor search, the new data structure supports incremental map update (i.e., point insertion, on-tree downsampling, points delete) and dynamic re-balancing at minimal ...

## Design Rationale

- **p. 2 / I. INTRODUCTION - extractive body cue:** More specifically, our contributions are as follows: 1) We develop an incremental k-d tree data structure, ikd-Tree, to represent a large dense point cloud map ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** 2) Allowed by the increased computation efficiency of ikd-Tree, we directly register raw points to the map, which enables more accurate and reliable scan registration ...
- **p. 1 / Abstract - extractive body cue:** The elimination of a hand-engineered feature extraction module also makes it naturally adaptable to emerging LiDARs of different scanning patterns; The second main novelty is ...

## Source Evidence Cues

- **p. 4 / IV. STATE ESTIMATION - extractive body cue:** Kinematic Model We first derive the system model, which consists of a state transition model and a measurement model.
- **p. 7 / V. MAPPING - extractive body cue:** For a given point p in {G¯pj} from the state estimation module (see Algorithm 1) and downsample resolution l, the algorithm partitions the space evenly ...
- **원문 대조:** 첫 IMU frame을 전역 좌표계 G로 두며, LiDAR–IMU 외부 파라미터를 회전과 병진의 쌍 I_T_L=(I_R_L, I_p_L)로 나타낸다. ([PDF p. 4](https://arxiv.org/pdf/2107.06829#page=4), §IV-A.1 State Transition Model).
- **p. 1 / I. INTRODUCTION - extractive body cue:** However, the performance of the feature extraction module is easily influenced by the environment.
- **p. 1 / I. INTRODUCTION - extractive body cue:** The localization provides state feedback for the robot onboard controllers, while the dense 3D map provides necessary information about the environment (i.e., free space and ...
- **p. 5 / IV. STATE ESTIMATION - extractive body cue:** It consists of two key steps: propagation upon each IMU measurement and iterated update upon each LiDAR scan, both step estimates the state naturally on ...
- **p. 5 / IV. STATE ESTIMATION - extractive body cue:** IV-B3) is bxκ k, when κ = 0 (i.e., before the first iteration), bxκ k = bxk, the predicted state from the propagation in (6).
- **Detected method headings:** 1 Algorithm Start (p. 8); 9 Algorithm End (p. 8)

## Pipeline

| Module | Purpose | Input | Operation | Output | PDF body cue | Anchor |
|---|---|---|---|---|---|---|
| 관성 전파 | 스캔 사이의 상태를 예측한다 | IMU 가속도·각속도 | 상태 전파와 스캔 내 운동 보상 | 스캔 끝의 사전 상태 | 그림 1과 상태 천이식 | PDF 4–5쪽 |
| 점군 정합 | 포즈를 보정한다 | 운동 보상된 점과 로컬 지도 | 점–평면 잔차로 반복 필터 갱신 | 보정된 상태 | 알고리즘 1과 측정식 | PDF 5–6쪽 |
| 지도 갱신 | 다음 정합에 사용할 이웃을 유지한다 | 갱신한 포즈와 스캔 점들 | ikd-Tree에 점을 삽입하고 이동 영역에서 벗어난 점을 삭제한다 | 갱신된 로컬 지도 | V절 지도 작성 | PDF 6–7쪽 |

- Pipeline rows are domain labels; the paper-specific operations are the extractive cues and section anchors in the same row.

## Objective / Update Rule

- **p. 2 / I. INTRODUCTION - extractive body cue:** Besides efficient nearest neighbor search, the new data structure supports incremental map update (i.e., point insertion, on-tree downsampling, points delete) and dynamic re-balancing at minimal ...
- **원문 대조:** 현재 반복 상태 추정값에서 point-to-plane 측정식을 1차 선형화하여 잔차, 상태 오차의 Jacobian 항, 측정 잡음으로 표현한다. 잘린 기존 수식은 완전한 등식으로 사용하지 않는다. ([PDF p. 5](https://arxiv.org/pdf/2107.06829#page=5), §IV-B.2 Residual Computation, Eqs. (8)–(9)).
- **p. 1 / I. INTRODUCTION - extractive body cue:** The considerably reduced cost, size, weight, and power of these LiDARs hold the potential to benefit a broad scope of existing and emerging robotic applications.
- **p. 1 / I. INTRODUCTION - extractive body cue:** Recent developments in LiDAR technologies have enabled the commercialization and mass production of more lightweight, cost-effective (in a cost range similar to global shutter cameras), ...
- **p. 8 / 9 Algorithm End - extractive body cue:** 10 11 Function Insert(T, p, father,SW) 12 if T is empty then 13 Initialize(T,p,father); 14 else 15 ax ←T.axis; 16 if p[ax] < T.point[ax] then ...
- **p. 8 / 24 End Function - extractive body cue:** The funcAlgorithm 3: Box-wise Delete Input : Operation Cuboid CO, k-d Tree Node T, Switch of Parallelly Re-building SW 1 Function BoxwiseDelete(T,CO,SW) 2 CT ←T.range; ...
- **Formal bridge:** 원시 LiDAR·IMU 측정과 이전 관성 상태 -> 관성 상태 추정치와 점군 지도 -> 점–평면 측정 잔차와 관성 사전 추정의 결합 -> 궤적 추정 정확도와 스캔당 처리 시간.
- **Equation/algorithm anchors:** p. 5 (IV. STATE ESTIMATION), p. 1 (Abstract), p. 1 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 4 (III. SYSTEM OVERVIEW), p. 5 (IV. STATE ESTIMATION).

## Variables and Parameters

| Role | PDF-derived terms | Normalized robotics interpretation | Status |
|---|---|---|---|
| Input/observation | prevent, size, going, unbound, only, points, large, local, region, length, around, LiDAR, current, position | 원시 LiDAR 스캔과 IMU 가속도·각속도 | body cue; exact tensor/frame verify |
| State/latent | prevent, size, going, unbound, only, points, large, local, region, length | 관성 상태와 로컬 점군 지도 | body cue; notation verify |
| Action/output | More, specifically, contributions, follows, develop, incremental, tree, data, structure, ikd-Tree | 추정한 자세·위치와 갱신된 점군 지도 | body cue; unit/decoder verify |
| Objective/constraint | Besides, efficient, nearest, neighbor, search, data, structure, supports, incremental, update | 점–평면 측정 잔차와 관성 사전 추정의 결합 | equation anchor required |

## Observation–State–Action Interface

- **p. 6 / V. MAPPING - extractive body cue:** To prevent the size of the map from going unbound, only map points in a large local region of length L around the LiDAR current ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** The localization provides state feedback for the robot onboard controllers, while the dense 3D map provides necessary information about the environment (i.e., free space and ...
- **p. 4 / IV. STATE ESTIMATION - extractive body cue:** Based on the ⊞ operation defined in [22], the continuous kinematic model (1) can be discretized at the IMU sampling period ∆t [55]: xi+1 = ...
- **p. 4 / III. SYSTEM OVERVIEW - extractive body cue:** As a result, the ikd-Tree tracks all map points in a large cube area with a certain length (referred to as "map size" in this ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** 40The central requirement for adopting LiDAR-based SLAM approaches to these widespread applications is to obtain accurate, low-latency state estimation and dense 3D map with limited ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** To further speed up the computation, a new and mathematically equivalent formula of computing the Kalman gain is used to reduce the computation complexity to ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** The elimination of a hand-engineered feature extraction makes the system naturally applicable to different LiDAR sensors; 3) We integrate these two key techniques into a ...
- **Normalized interface:** observation=원시 LiDAR 스캔과 IMU 가속도·각속도; state=관성 상태와 로컬 점군 지도; output/action=추정한 자세·위치와 갱신된 점군 지도.

## Temporal and Runtime Contract

| Contract | Generic domain prior | PDF body cue | Unresolved detail |
|---|---|---|---|
| Horizon | 스캔이 도착할 때마다 그동안 누적한 IMU 측정으로 상태를 전파한다. | Private Dataset 1) Detail Evaluation of Processing Time: In order to validate the real-time performance of FAST-LIO2, we use the handheld platform ... | 스캔 축적과 IMU 시간 범위 |
| Rate / latency | 스캔별 오도메트리·지도 갱신 시간을 측정한다. | The map built by FAST-LIO2 in real-time is shown in Fig. | 스캔 주기와 처리 시간 |
| Memory | 로컬 점군 지도를 ikd-Tree로 유지한다. | not recovered | 로컬 지도 범위와 제거되는 점 |
| Compute | 최근접점 검색과 점의 삽입·삭제가 지도 갱신 비용에 기여한다. | Private Dataset 1) Detail Evaluation of Processing Time: In order to validate the real-time performance of FAST-LIO2, we use the handheld platform ... | hardware, batch and throughput |

## Training vs Inference

- **p. 2 / I. INTRODUCTION - extractive body cue:** These features make the ikd-Tree very suitable for LiDAR odometry and mapping application, leading to 100 Hz odometry and mapping on computationallyconstrained platforms such as ...

## Method-Specific Formal Details

- **Body-defined terms:** Kinematic, Model, first, derive, system, consists, state, transition, measurement, given, point, estimation, module, Algorithm, downsample, resolution, partitions, space, evenly, cubes.
- **Relevant PDF headings:** 1 Algorithm Start (p. 8); 9 Algorithm End (p. 8).

## Evaluation Link

| Method component | Evaluation evidence to inspect | PDF anchor |
|---|---|---|
| 센서 구성 | 항공·지상 등 데이터별 LiDAR와 IMU 입력 사양 | PDF 11쪽 표 II |
| 추정치의 사용 예 | 저자가 인용한 과거의 UAV 장애물 회피 응용 | PDF 16쪽 |
| 실시간 처리 | 점군 규모에 따른 추정·지도 작성 시간 | PDF 15–16쪽 |

## Failure and Ablation Link

- **p. 4 / Figure/Table caption - extractive body cue:** Fig. 1. System overview of FAST-LIO2. with on-tree downsampling which is a common requirement in mapping, whereas downsampling must be done outside before inserting new ...
- **p. 6 / Figure/Table caption - extractive body cue:** Fig. 3. 2D demonstration of map region management. In (a), the blue rectangle is the initial map region with length L. The red circle is ...
- **p. 9 / Figure/Table caption - extractive body cue:** Fig. 4. Re-building an unbalanced sub-tree nodes (i.e., labeled as "deleted") on the sub-trees are removed to reduce tree size. Reducing the height and size ...
- **p. 14 / VII. REAL-WORLD EXPERIMENTS - extractive body cue:** The detailed time consumption of individual components for processing a scan is shown in Table.
- **p. 13 / 100 Hz - extractive body cue:** LIO-SAM shows good performance in its own sequences liosam 2 and liosam 3 but cannot keep it on other sequences such as ulhk.
- **p. 14 / VII. REAL-WORLD EXPERIMENTS - extractive body cue:** It should be noted that the LILI-OM also supports solid-state LiDAR, but it fails in this data since its feature extraction module produces too few ...
- **p. 15 / VII. REAL-WORLD EXPERIMENTS - extractive body cue:** As can be seen, the averaging mapping time per scan for FAST-LIO exceeds 10 ms hence cannot be processed in real-time for this large scene.

## Reproduction Checklist

[공통 검토 기준](../../../research/READING_STATUS.md#note-checks)

## Verification Questions

- **Evidence anchors reviewed:** method p. 4 (IV. STATE ESTIMATION), p. 7 (V. MAPPING), p. 4 (IV. STATE ESTIMATION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 5 (IV. STATE ESTIMATION), objective p. 2 (I. INTRODUCTION), p. 5 (IV. STATE ESTIMATION), p. 1 (I. INTRODUCTION), p. 1 (I. INTRODUCTION), p. 8 (9 Algorithm End), p. 8 (24 End Function), temporal p. 14 (VII. REAL-WORLD EXPERIMENTS), p. 14 (VII. REAL-WORLD EXPERIMENTS), p. 15 (VII. REAL-WORLD EXPERIMENTS), p. 16 (VII. REAL-WORLD EXPERIMENTS), p. 16 (VII. REAL-WORLD EXPERIMENTS), p. 3 (II. RELATED WORKS).
