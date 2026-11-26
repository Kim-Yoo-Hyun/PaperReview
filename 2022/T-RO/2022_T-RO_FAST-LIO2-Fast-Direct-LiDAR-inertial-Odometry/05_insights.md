# Insights — FAST-LIO2: Fast Direct LiDAR-inertial Odometry

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> Analysis basis: full-text PDF body checked on 2026-09-02 (19 pages; PyMuPDF text; extraction quality: high); canonical paper source: https://arxiv.org/abs/2107.06829; PDF retrieval source: https://arxiv.org/pdf/2107.06829. The note is an evidence-anchored PDF body analysis; exact tables/equations remain at the cited page anchors. Evidence boundary: selected PDF body sentences, captions and section anchors were used; exact table/equation values remain at those anchors. Reading tracker status remains user-controlled; registry source evidence is reconciled separately.

> DOC-QA1 (2026-10-23): 제어문자·깨진 추출 구간과 직접 연결된 표 항목을 PDF 페이지 이미지와 대조했다. 확인 범위·원문 URL·페이지·수정 이력은 [대조 기록](../../../work/sources/pdf_note_review_2026-10-23.json)에 있다. 노트 전체의 정독이나 모든 기존 주장에 대한 재검증을 뜻하지 않으며 reading status는 유지한다.

## Paper-supported conclusion

> **Evidence boundary:** The following claims are restricted to selected PDF body sentences, captions and section anchors; exact table/equation values remain to be checked at those anchors.

### What was actually new

- **p. 2 / I. INTRODUCTION - extractive body cue:** More specifically, our contributions are as follows: 1) We develop an incremental k-d tree data structure, ikd-Tree, to represent a large dense point cloud map ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** 2) Allowed by the increased computation efficiency of ikd-Tree, we directly register raw points to the map, which enables more accurate and reliable scan registration ...
- **p. 1 / Abstract - extractive body cue:** The elimination of a hand-engineered feature extraction module also makes it naturally adaptable to emerging LiDARs of different scanning patterns; The second main novelty is ...
- **p. 4 / IV. STATE ESTIMATION - extractive body cue:** Kinematic Model We first derive the system model, which consists of a state transition model and a measurement model.
- **p. 1 / Abstract - extractive body cue:** This enables the exploitation of subtle features in the environment and hence increases the accuracy.
- **p. 7 / V. MAPPING - extractive body cue:** For a given point p in {G¯pj} from the state estimation module (see Algorithm 1) and downsample resolution l, the algorithm partitions the space evenly ...
- **원문 대조:** 첫 IMU frame을 전역 좌표계 G로 두며, LiDAR–IMU 외부 파라미터를 회전과 병진의 쌍 I_T_L=(I_R_L, I_p_L)로 나타낸다. ([PDF p. 4](https://arxiv.org/pdf/2107.06829#page=4), §IV-A.1 State Transition Model).
- **Contribution anchor:** p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION), p. 1 (Abstract), p. 4 (IV. STATE ESTIMATION), p. 1 (Abstract), p. 7 (V. MAPPING)

### Strongest assumption and failure boundary

- **p. 1 / I. INTRODUCTION - extractive body cue:** However, efficient and accurate LiDAR odometry and mapping are still challenging problems: 1) Current LiDAR sensors produce a large amount of 3D points from hundreds ...
- **p. 1 / I. INTRODUCTION - extractive body cue:** On the other hand, real-time dense mapping [5]-[8] based on visual sensors at high resolution and accuracy with only the robot onboard computation resources is ...
- **p. 2 / I. INTRODUCTION - extractive body cue:** Experiments on 18 sequences of various sizes show that ikdTree achieves superior performance against existing dynamic data structures (octree, R∗-tree, nanoflann k-d tree) in the ...
- **p. 13 / 100 Hz - extractive body cue:** LIO-SAM shows good performance in its own sequences liosam 2 and liosam 3 but cannot keep it on other sequences such as ulhk.
- **p. 14 / VII. REAL-WORLD EXPERIMENTS - extractive body cue:** It should be noted that the LILI-OM also supports solid-state LiDAR, but it fails in this data since its feature extraction module produces too few ...
- **p. 15 / VII. REAL-WORLD EXPERIMENTS - extractive body cue:** As can be seen, the averaging mapping time per scan for FAST-LIO exceeds 10 ms hence cannot be processed in real-time for this large scene.
- **p. 14 / VII. REAL-WORLD EXPERIMENTS - extractive body cue:** Since FAST-LIO2 does not extract features, it is naturally adaptable to this new LiDAR.
- **Boundary to test:** LIO-SAM shows good performance in its own sequences liosam 2 and liosam 3 but cannot keep it on other sequences such as ulhk.

### Claim–evidence link

| Claim target | Body evidence | Anchor |
|---|---|---|
| Mechanism/contribution | More specifically, our contributions are as follows: 1) We develop an incremental k-d tree data structure, ikd-Tree, to represent a large dense point cloud map efficiently. | p. 2 (I. INTRODUCTION), p. 2 (I. INTRODUCTION) |
| Reported outcome | Notice that the considerably reduced processing time for FAST-LIO2 is achieved even at a much higher number of map points. | p. 16 (VII. REAL-WORLD EXPERIMENTS), p. 10 (VI. BENCHMARK RESULTS) |
| Failure/limitation | LIO-SAM shows good performance in its own sequences liosam 2 and liosam 3 but cannot keep it on other sequences such as ulhk. | p. 13 (100 Hz), p. 14 (VII. REAL-WORLD EXPERIMENTS) |

## Researcher interpretation

### Reusable lesson in the robotics loop

- **Closed-loop position:** `원시 LiDAR 스캔과 IMU 가속도·각속도 → 관성 상태와 로컬 점군 지도 → 추정한 자세·위치와 갱신된 점군 지도`.
- 이 논문의 재사용 가능한 지점은 To prevent the size of the map from going unbound, only map points in a large local region of length L around the LiDAR current position are maintained Algorithm 1: State Estimation ...를 The localization provides state feedback for the robot onboard controllers, while the dense 3D map provides necessary information about the environment (i.e., free space and obstacles) for trajectory planning.로 변환하는 body-defined interface를 분리해 보는 것이다. 따라서 관성 상태와 로컬 점군 지도가 실제 decision/control에 어떤 정보로 소비되는지, 그리고 LIO-SAM shows good performance in its own sequences liosam 2 and liosam 3 but cannot keep it on other sequences such as ulhk.에서 feedback/recovery가 유지되는지를 동일 protocol로 비교해야 한다.
- The paper-specific mechanism to preserve in a reproduction is: More specifically, our contributions are as follows: 1) We develop an incremental k-d tree data structure, ikd-Tree, to represent a large dense point cloud map efficiently.
- Do not credit a downstream robotics benefit unless the body evaluation reports the corresponding task, metric and feedback condition.

### Dependency and evolution

- **Registry position:** `REFERENCE` in `Robotics-enabling 3D perception`; tags: `Robotics, state estimation, LiDAR-inertial odometry, SLAM, direct registration, real-time`.
- **Reading predecessor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- **Reading successor in the generated track queue:** not recorded (queue adjacency, not a confirmed citation).
- Direct citation predecessor/successor is not asserted automatically; verify the paper's reference section before recording lineage as fact.
- **Body-defined next pressure:** LIO-SAM shows good performance in its own sequences liosam 2 and liosam 3 but cannot keep it on other sequences such as ulhk.; this is the most direct route from the paper's reported scope to a falsifiable extension.

### Minimal reproduction

1. Reconstruct the body-defined input/state/output interface and record the exact equation or algorithm anchors.
2. Use the paper-reported resource/task cue: 11 TABLE II THE DATASETS FOR BENCHMARK LiDAR IMU Type Line Type Rate lili Solid-state - 6-axis.
3. Compare against the body-reported baseline or a matched simpler baseline: For example, our prior work [63] demonstrated the application of FAST-LIO2 on an autonomous UAV avoiding dynamic small objects (down to 9 mm) in complex indoor and outdoor environments..
4. Report the body metric and its denominator/aggregation: In this section, extensive experiments in terms of accuracy, robustness, and computational efficiency are conducted on various open datasets..
5. Re-run the body-reported ablation/failure condition: Fig. 1. System overview of FAST-LIO2. with on-tree downsampling which is a common requirement in mapping, whereas downsampling must be done outside before inserting new points into other dynamic data structures [38, ....
6. Add one matched stress test for the strongest assumption without changing observation, action, data, compute, horizon or controller.

### What would count as a successful reproduction

- The reported mechanism is present at p. 4 (IV. STATE ESTIMATION), p. 7 (V. MAPPING), p. 4 (IV. STATE ESTIMATION); the primary result is directionally consistent at p. 16 (VII. REAL-WORLD EXPERIMENTS), p. 10 (VI. BENCHMARK RESULTS), p. 10 (VI. BENCHMARK RESULTS); and the failure boundary is measured rather than omitted.

## Falsifiable research question

고정된 observation/action/data/compute budget에서 More, specifically, contributions mechanism이 For example, our prior work [63] demonstrated the application of FAST-LIO2 on an autonomous UAV avoiding ... 대비 In this section, extensive experiments in terms of accuracy, robustness, and computational efficiency are conducted on various open ...을 개선하고, LIO-SAM shows good performance in its own sequences liosam 2 and liosam 3 but cannot keep ... 조건에서도 closed-loop failure를 늘리지 않는가?

**Reject the hypothesis if** the primary body metric does not improve at matched budget, or if the method's added latency, data requirement, instability or assumption sensitivity outweighs the reported closed-loop gain.
