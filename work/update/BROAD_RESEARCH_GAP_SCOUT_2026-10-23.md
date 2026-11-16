# 2024–2026 분야별 연구 공백 탐색 — VLA 밖으로의 확장

- 조사일: **2026-10-23 KST** / 작업: **GAP-W1**
- 성격: registry와 외부 primary 문헌의 **선택적 scoping review**. 전체 proceedings 정독·체계적 문헌고찰·신규성 입증은 아니다.
- 질문의 유지·수정은 아래 링크의 **각 synthesis Open Questions**가 담당한다. 이 파일은 이번 검색과 판단의 날짜별 기록이며 새 gap registry나 읽기 우선순위 source가 아니다.
- [직전 VLA 조사](./VLA_GAP_SCOUT_2026-10-23.md) · [이번 source ledger](../sources/broad_gap_scout_2026-10-23.json) · [buildup 절차](../../research/IDEA_BUILDUP_GUIDE.md) · [다음 작업](../../TODO.md)

## 1. 조사 결과와 해석

VLA를 필수 요소로 두지 않고 **9개 연구 질문**을 추가했다. 범위는 control·causal/offline RL·data-centric learning·sim-to-real·변형체/역물리·world models·장시간 whole-body 운용·3D vision·HRI/multi-agent다. 일반 ML의 식별 가능성과 데이터 선택도 포함하지만, 의학·금융·보안·모든 컴퓨터과학을 조사한 것은 아니다.

중요한 구별은 **분야의 열린 문제**와 **우리가 주장할 신규 기여**다. 좋은 선행 연구가 있다는 사실은 그 분야가 해결됐다는 뜻이 아니다. 반대로 선행 논문의 limitation에 적혀 있거나 registry에 없다는 이유만으로 새 논문 주제가 확보되는 것도 아니다. 이번에는 알려진 답을 좁히고, 그 경계 밖에서 답에 따라 실제 선택이 달라지는 질문을 남겼다.

이번 판단으로는 **3D 지도의 실제 collision 위험, 모델 구조 오류와 parameter 오류의 구분, 데이터 선택 효과의 policy 간 전달**을 다음 문헌 심화의 첫 비교 대상으로 삼을 만하다. 이는 효과 크기나 채택 확률의 순위가 아니다. 비교 조건을 명확히 만들 수 있는지, 기존 자산으로 작은 검증을 설계할 여지가 있는지에 대한 잠정 판단이다. 변형체 식별도 근거가 선명하지만 물성·고정 조건의 ground truth가 필요하다.

## 2. 무엇을 어디까지 조사했는가

Registry **1,037편**의 metadata를 대상으로 title·identifier·분야를 교차 검색했다. 이 중 2024–2026 항목은 **757편**이며, 1,037편 또는 757편을 전부 새로 읽었다는 뜻은 아니다. 기존 7개 synthesis의 질문과 후보별 결과도 중복/재명명 여부 판단에 사용했다.

이번 근거 목록은 논문 **40건**이다. 이는 웹 검색에서 나온 모든 결과 수가 아니라, 질문 또는 강한 대안과 직접 연결돼 기록에 남긴 자료 수다.

| 확인 구분 | 수 | 근거 경계 |
|---|---:|---|
| 공식 proceedings/publisher로 publication 확인 | 33 | PMLR·CVF·ECVA·NeurIPS/ICLR proceedings·RSS·IEEE. 일부는 직접 페이지 접근 실패 후 공식 도메인의 검색 색인으로 확인 |
| 저자에게서만 venue 표기를 확인 | 2 | ASTRA의 RA-L/IROS, AirSplan의 IROS. 독립적인 공식 acceptance 확인과 분리 |
| 확인한 버전 기준 arXiv, venue 미확정 | 5 | peer-reviewed 결과와 같은 지위로 합산하지 않음 |
| 지정 본문 구간 확인 | 7 | SPI-Active, PGND, JIGGLE, Who Moved My Distribution?, Imperfect World Models, thermal residual policy, SAFER-Splat. 전체 정리·증명·코드 감사가 아님 |
| 저자 project의 method 설명 확인 | 1 | ASTRA. 논문 본문 전체 확인을 대신하지 않음 |
| Abstract/공식 색인 중심 | 32 | 세부 method·trial·실험에서 다루지 않은 조건을 단정하지 않음 |
| Registry identity 연결 | 6 | 정규화 제목/관측한 arXiv ID 기준. 나머지 34건은 “미연결”이며 최종 admission 중복 심사를 끝낸 신규 논문 수가 아님 |

공식 근거가 남은 venue는 CVPR·ICCV·ECCV·NeurIPS·ICLR·ICML·CoRL·RSS·ICRA·IROS·T-RO·AISTATS다. L4DC·Humanoids는 분야의 직접 선행을 확인하는 보조 범위다. 학회별 편수를 맞추지 않았다. Journal은 T-RO 근거가 있으나 IJRR·Science Robotics까지 충분히 포괄했다고 할 수 없으며, 2026년은 조사일까지 공개된 자료에 한정한다.

검색은 분야명에 `assumption / limitation / active / uncertainty / calibration / transfer / identifiability / evaluation`과 venue/year를 결합하고, 직접 선행이 나오면 exact title·official domain·관련 본문 구간으로 좁혔다. 포함 기준은 문제의 존재/가정을 설명하거나 제안을 대체할 강한 방법·benchmark인 경우다. 일반적인 주제 소개, 상태를 확인하지 못한 검색 결과, 동일 연구의 반복 hit는 근거 편수에 넣지 않았다. ASID·CERT-Replan 등 발견했지만 공식 상태/본문 검토가 덜 된 단서는 완결된 비교 근거로 사용하지 않았다.

## 3. 분야별 공백과 연구 질문

아래 질문은 모두 **CURATION-HYPOTHESIS**다. 논문 사실과 우리 질문을 구분했으며, 실제 비교·가설 검증은 아직 수행하지 않았다. 완전한 비교 계약과 후속 판단은 링크된 synthesis에 있다.

| 분야 / 질문 | 이미 연구된 부분 | 이번에 좁힌 공백 후보 | 성립하지 않게 만들 가장 쉬운 설명 |
|---|---|---|---|
| [GAP-PLAN — interactive safety](../../synthesis/01_planning_control.md#gap-plan-2026) | Adaptive conformal navigation, ego 행동이 유발하는 분포 변화 | 상대의 반응 모드가 갑자기 바뀔 때 calibration 실패를 감지하며 안전과 진행을 함께 유지할 조건 | Predictor·latency 개선 또는 기존 adaptive CP만으로 충분 |
| [GAP-CAUSAL — causal/offline RL](../../synthesis/02_rl_il_offline.md#gap-causal-2026) | 식별 가능/불가능 조건, confounding-robust OPE/RL | Coverage 부족과 교란을 분리하고 정책 선택을 바꿀 최소 추가 cue/개입 결정 | 교란이 아니라 단순 coverage 부족; 유효 bound가 너무 넓어 결정에 무용 |
| [GAP-DATA-TRANSFER — data-centric ML/IL](../../synthesis/02_rl_il_offline.md#gap-data-transfer-2026) | 다양성·scaling·policy-aware data selection | 한 policy의 subset 선택이 다른 policy에서도 유효한 조건과 순위 역전의 원인 | Task 분포·중복·학습량을 맞추면 차이 소멸 |
| [GAP-SYSID — identification/sim-to-real](../../synthesis/05_world_models_safety.md#gap-sysid-2026) | Active/online ID, history abstraction, task-sensitive robust control | Parameter 재보정과 omitted-state/model-class 수정 중 무엇이 필요한지 적은 interaction으로 판단 | 단순 delay 보정·history 추가가 전부 설명 |
| [GAP-DEFORM — deformables/inverse physics](../../synthesis/03_manipulation_contact.md#gap-deform-2026) | Neural dynamics, attachment sensing, 반복 보정 | 형상이 비슷한 재질/고정 조건을 행동에 필요한 정도로 구별하는 probe | 단순 feedback·ILC로 충분하거나 물성 oracle도 task 결정을 바꾸지 않음 |
| [GAP-WM — decision quality of world models](../../synthesis/05_world_models_safety.md#gap-wm-2026) | Environment queries, policy-ranking inversion, conservative planning | Planner 최적화 범위가 바뀔 때 실제 decision 실패를 예측하는 신호의 전달 | Support 제한·짧은 horizon·기존 robust planner로 동일 결과 |
| [GAP-THERMAL — long-duration control](../../synthesis/06_locomotion_whole_body.md#gap-thermal-2026) | Thermal-aware RL/residual policy, force adaptation, cooling hardware | Payload·ambient·task switching 아래 task 처리량과 열 제약을 함께 유지 | Derating/rest schedule만으로 동일 처리량 |
| [GAP-GEOMETRY — 3D perception/navigation](../../synthesis/07_robotics_3d_perception.md#gap-geometry-2026) | Geometry foundation, uncertainty SLAM, dynamic reconstruction, safe splat planning | 빠진 장애물/미관측 공간과 위치 오차를 구별해 false-free-space 위험을 예측 | Pose/scale 보정·unknown-space 처리·고정 margin만으로 충분 |
| [GAP-HRI — human/multi-agent cooperation](../../synthesis/01_planning_control.md#gap-hri-2026) | Intent calibration, execute/clarify/intervene, intent communication | 응답 지연·오답·partner 능력 변화 아래 도움 형태의 효과와 사용자 부담 | Base skill 부족 또는 기존 UPS/RCIP 보정으로 모두 설명 |

서로 다른 질문의 uncertainty를 같은 변수로 취급하지 않는다. PLAN은 상호 행동의 변화, CAUSAL은 효과의 식별 가능성, SYSID/DEFORM은 숨은 dynamics, GEOMETRY는 관측하지 못한 공간, HRI는 사람의 의도·응답 비용을 다룬다.

## 4. 특히 근거가 구체적인 경계

- **3D 지도와 실제 공간:** SAFER-Splat은 §VIII에서 정확한 GSplat 지도를 가정하며 dynamic object와 pose 오차를 한계로 적는다. 따라서 다음 검토는 더 예쁜 reconstruction보다 false-free-space와 실제 swept-volume risk를 연결하는 데 초점을 둔다. 다만 새 confidence/CBF 결합의 신규성을 입증한 것은 아니다. [SAFER-Splat 본문](https://arxiv.org/html/2409.09868v1).
- **변형체의 물성/고정 조건:** PGND는 test-time 물성 식별을, JIGGLE은 heterogeneous material/boundary 공동 추정을 후속 문제로 명시한다. 같은 외관에서 다른 조작이 필요한 상황은 검토할 근거가 있다. 이 limitation의 후속 연구가 없는지는 아직 확인되지 않았다. [PGND §V](https://arxiv.org/html/2506.15680v1), [JIGGLE §VI](https://arxiv.org/html/2405.09743v1).
- **Active system ID의 적용 범위:** SPI-Active의 offline·motion-policy 가정, online KF의 parameter correction, ASTRA의 history abstraction은 서로 다른 오차를 다룬다. 차별점은 이들을 단순히 합치는 것이 아니라 어떤 데이터로 필요한 수정을 구별할 수 있는가에 있다. [SPI-Active §7](https://arxiv.org/html/2505.14266v1), [IROS 2025 KF](https://ieeexplore.ieee.org/document/11246753/), [ASTRA 저자 설명](https://pages.cs.wisc.edu/~gearless_joe/astra/).
- **이미 많이 다룬 질문:** World-model score와 실제 성능의 불일치, thermal reward, 불확실할 때 clarification은 각각 직접 선행이 있다. 이번 범위 확장은 이러한 분야를 폐기하는 판단이 아니라, 새 주장에 필요한 조건을 좁히는 작업이다. [Imperfect World Models](https://arxiv.org/html/2605.15960v2), [thermal residual policy](https://arxiv.org/html/2605.27046v3), [UPS](https://roboticsproceedings.org/rss22/p142.html).

## 5. 다음 buildup에 필요한 것과 자원

| 질문 묶음 | 지금 할 수 있는 비실험 작업 | 이후의 최소 자원 | 현재 제안 |
|---|---|---|---|
| GEOMETRY | Map-relative vs real-world guarantee, sensor/pose/unknown-space 가정 및 공개 데이터 GT 감사 | RGB-D/geometry·collision 평가, 추후 Docker inference; 실환경 주장은 robot | 다음 심화 비교 |
| SYSID | Parameter family·omitted state·probe budget·classical ID/dual-control 비교 | Native telemetry·time alignment, dynamics simulator; 실제 transfer는 hardware | 다음 심화 비교 |
| DATA-TRANSFER | Source/target policy·surrogate·data pool·split·selection-cost 대조 | 공개 episode ID·성공 evaluator·GPU 학습 예산 | 다음 심화 비교 |
| DEFORM | Material/boundary 공동 추정 후속 문헌·probe와 ILC 비교 | 변형체·고정 장치·물성/힘 ground truth·robot | 조건부 심화 |
| CAUSAL / PLAN / WM | 정리의 가정·반례·보장 단위·강한 classical baseline 대조 | 작은 생성 모형부터 시작 가능; 일반화 주장은 별도 데이터/환경 | 이론/진단 가능성 비교 |
| HRI | 응답 reliability·partner split·clarification 비용의 기존 protocol 감사 | 참여자/상호작용 데이터·독립 task outcome | 데이터 확보 조건부 |
| THERMAL | 온도 모델·운용 제한·task schedule·derating 선행 비교 | 실제 온도/전류 telemetry와 장시간 운용 가능한 robot | Hardware 확보 전 보존 |

GPU 없이도 문헌·가정·비교 설계를 계속할 수 있다. 반대로 GPU만 있어서는 hidden cue·실제 물성·thermal state·human workload의 ground truth를 확보할 수 없다. 이번에는 학습·simulation·policy inference·성능 측정을 실행하지 않았다. 후속 실험은 현재 사용자가 선택한 컴퓨터의 Docker에서만 수행한다.

**다음 작업 GAP-W2:** 위 첫 세 질문의 가장 가까운 3–5편을 본문/부록/공개 code interface 수준에서 비교하고, 기존 방법과 다른 예측이 남는지, 공정한 검증 packet을 만들 수 있는지 판정한다. 세 질문 모두의 학습을 시작한다는 뜻은 아니다. 기존 GAP-CONTACT의 GAP-R2는 대기 심화로 유지한다.

## 6. Registry와 기존 후보에 미치는 영향

- 정식 신규 등록·tier 변경·읽기 상태 승격은 없다. Registry 1,037편과 CORE 47 / NEXT 275 / REFERENCE 473 / ARCHIVE 242를 유지한다.
- 외부 자료 40건은 이번 조사 ledger다. 이 목록이 paper folder/5개 note를 갖춘 정식 registry entry를 대신하지 않는다. 등록하려면 canonical identity·version·관련성 심사 후 기존 등록기를 사용한다.
- Splat-Nav는 registry `pr-0284`의 IROS 2025 표기와 [IEEE T-RO 2025 publication](https://doi.org/10.1109/tro.2025.3552348)이 다르다. [저자 연구실 목록](https://sites.temple.edu/trail/publications/)은 IROS를 presentation으로 분리한다. 이번 질문은 journal 근거를 사용하며, manifest/path/notes의 정합은 후속 META-W1로 남겼다. 중복 논문으로 추가하지 않는다.
- C1–C6, D1–D3, E1/E2와 초기 RL 전이·RP-2/RP-3의 기존 판단은 유지한다. 새로운 gap 카드가 과거 설계의 재개 근거가 되려면 이전의 막힌 전제를 실제로 바꿔야 한다.
- 기존 DOC-QA1 및 GAP-R1 변경을 보존한다. Local PDF, package, experiment container, Git commit/push는 이번 작업에서 만들지 않는다.

## 7. 논문 근거 목록

아래 W-ID는 이번 날짜별 source audit의 식별자다. 본문 확인 구간·알려진 답·registry 연결·status의 정확한 경계는 [JSON ledger](../sources/broad_gap_scout_2026-10-23.json)에 있다. Code/project 링크를 확인한 것과 실제 release·runtime 검증은 별개다.

| ID | 논문 / 확인된 venue·연도 | 확인 깊이 | Registry |
|---|---|---|---|
| W01 | [Towards Generalizable Safety in Crowd Navigation via Conformal Uncertainty Handling](https://proceedings.mlr.press/v305/yao25a.html) — CoRL 2025 | abstract/공식 색인 | 미연결 |
| W02 | [Who Moved My Distribution? Conformal Prediction for Interactive Multi-Agent Systems](https://arxiv.org/html/2511.11567v1) — arXiv 2025 | 지정 본문 | 미연결 |
| W03 | [Offline Policy Evaluation and Optimization Under Confounding](https://proceedings.mlr.press/v238/kausik24a.html) — AISTATS 2024 | abstract/공식 색인 | 미연결 |
| W04 | [Two-way Deconfounder for Off-policy Evaluation in Causal Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/hash/8ecf25e3a462e9bb1e29662dfe7258fe-Abstract-Conference.html) — NeurIPS 2024 | abstract/공식 색인 | 미연결 |
| W05 | [Confounding Robust Deep Reinforcement Learning: A Causal Approach](https://proceedings.neurips.cc/paper_files/paper/2025/hash/c9a177f06ecd9892cd1664d89994fb58-Abstract-Conference.html) — NeurIPS 2025 | abstract/공식 색인 | 미연결 |
| W06 | [Automatic Reward Shaping from Confounded Offline Data](https://proceedings.mlr.press/v267/li25dr.html) — ICML 2025 | abstract/공식 색인 | 미연결 |
| W07 | [Data Scaling Laws in Imitation Learning for Robotic Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/hash/88b7b2c896506daabc8d3fd587055167-Abstract-Conference.html) — ICLR 2025 | abstract/공식 색인 | pr-0580 |
| W08 | [What Matters in Learning from Large-Scale Datasets for Robot Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/hash/16466b6c95c5924784486ac5a3feeb65-Abstract-Conference.html) — ICLR 2025 | abstract/공식 색인 | 미연결 |
| W09 | [DataMIL: Selecting Data for Robot Imitation Learning with Datamodels](https://proceedings.iclr.cc/paper_files/paper/2026/hash/033d9e8dbbbc0ad90e59222cf1db0fc2-Abstract-Conference.html) — ICLR 2026 | abstract/공식 색인 | 미연결 |
| W10 | [Difference-Aware Retrieval Policies for Imitation Learning](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8c2ecd140ebe227a531edc9a0c3b69d4-Abstract-Conference.html) — ICLR 2026 | abstract/공식 색인 | 미연결 |
| W11 | [Sampling-based System Identification with Active Exploration for Legged Sim2Real Learning](https://proceedings.mlr.press/v305/sobanbabu25a.html) — CoRL 2025 | 지정 본문 | 미연결 |
| W12 | [Adaptive Model-Based Control of Quadrupeds via Online System Identification using Kalman Filter](https://ieeexplore.ieee.org/document/11246753/) — IROS 2025 | abstract/공식 색인 | 미연결 |
| W13 | [Abstract Sim2Real through Approximate Information States](https://pages.cs.wisc.edu/~gearless_joe/astra/) — RA-L / IROS (author-reported) 2026 | 저자 method 설명 | 미연결 |
| W14 | [Distributionally Robust Control via Stein Variational Inference for Contact-rich Manipulation](https://www.roboticsproceedings.org/rss22/p061.html) — RSS 2026 | abstract/공식 색인 | 미연결 |
| W15 | [Particle-Grid Neural Dynamics for Learning Deformable Object Models from RGB-D Videos](https://www.roboticsproceedings.org/rss21/p036.html) — RSS 2025 | 지정 본문 | pr-0890 |
| W16 | [JIGGLE: An Active Sensing Framework for Boundary Parameters Estimation in Deformable Surgical Environments](https://www.roboticsproceedings.org/rss20/p007.html) — RSS 2024 | 지정 본문 | 미연결 |
| W17 | [Implicit Neural-Representation Learning for Elastic Deformable-Object Manipulations](https://roboticsproceedings.org/rss21/p035.html) — RSS 2025 | abstract/공식 색인 | 미연결 |
| W18 | [Learning Deformable Object Manipulation Using Task-Level Iterative Learning Control](https://www.roboticsproceedings.org/rss22/p126.html) — RSS 2026 | abstract/공식 색인 | 미연결 |
| W19 | [Latent Diffeomorphic Co-Design of End-Effectors for Deformable and Fragile Object Manipulation](https://roboticsproceedings.org/rss22/p195.html) — RSS 2026 | abstract/공식 색인 | 미연결 |
| W20 | [Benchmarking World-Model Learning with Environment-Level Queries](https://proceedings.mlr.press/v306/warrier26a.html) — ICML 2026 | abstract/공식 색인 | 미연결 |
| W21 | [Imperfect World Models are Exploitable](https://arxiv.org/html/2605.15960v2) — arXiv 2026 | 지정 본문 | 미연결 |
| W22 | [Parallel Stochastic Gradient-Based Planning for World Models](https://proceedings.mlr.press/v306/psenka26a.html) — ICML 2026 | abstract/공식 색인 | 미연결 |
| W23 | [General agents need world models](https://proceedings.mlr.press/v267/richens25a.html) — ICML 2025 | abstract/공식 색인 | 미연결 |
| W24 | [FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation](https://proceedings.mlr.press/v331/zhang26a.html) — L4DC 2026 | abstract/공식 색인 | 미연결 |
| W25 | [Learning Thermal-Aware Locomotion Policies for an Electrically-Actuated Quadruped Robot](https://arxiv.org/abs/2603.01631) — arXiv 2026 | abstract/공식 색인 | 미연결 |
| W26 | [Learning to Balance Motor Thermal Safety and Quadrupedal Locomotion Performance with Residual Policy](https://arxiv.org/html/2605.27046v3) — arXiv 2026 | 지정 본문 | 미연결 |
| W27 | [Development of the Leg Structure with Concentrated Liquid-Cooling Actuators for Long-Term Operation](https://ieeexplore.ieee.org/abstract/document/11203109) — Humanoids 2025 | abstract/공식 색인 | 미연결 |
| W28 | [VGGT: Visual Geometry Grounded Transformer](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.html) — CVPR 2025 | abstract/공식 색인 | pr-0056 |
| W29 | [CG-SLAM: Efficient Dense RGB-D SLAM in a Consistent Uncertainty-aware 3D Gaussian Field](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3580_ECCV_2024_paper.php) — ECCV 2024 | abstract/공식 색인 | pr-0402 |
| W30 | [POMATO: Marrying Pointmap Matching with Temporal Motions for Dynamic 3D Reconstruction](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_POMATO_Marrying_Pointmap_Matching_with_Temporal_Motions_for_Dynamic_3D_ICCV_2025_paper.html) — ICCV 2025 | abstract/공식 색인 | 미연결 |
| W31 | [Emergent Outlier View Rejection in Visual Geometry Grounded Transformers](https://openaccess.thecvf.com/content/CVPR2026/html/Han_Emergent_Outlier_View_Rejection_in_Visual_Geometry_Grounded_Transformers_CVPR_2026_paper.html) — CVPR 2026 | abstract/공식 색인 | 미연결 |
| W32 | [Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps](https://doi.org/10.1109/tro.2025.3552348) — T-RO 2025 | abstract/공식 색인 | pr-0284 |
| W33 | [SAFER-Splat: A Control Barrier Function for Safe Navigation with Online Gaussian Splatting Maps](https://arxiv.org/html/2409.09868v1) — arXiv 2024 | 지정 본문 | 미연결 |
| W34 | [AirSplan: Risk-Aware Motion Planning for Quadrotors in Cluttered 3D Gaussian Splats](https://arxiv.org/abs/2609.21226) — IROS (author-reported) 2026 | abstract/공식 색인 | 미연결 |
| W35 | [PARTNR: A Benchmark for Planning and Reasoning in Embodied Multi-agent Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a3cf318fbeec1126da21e9185ae9908c-Abstract-Conference.html) — ICLR 2025 | abstract/공식 색인 | pr-0082 |
| W36 | [Risk-Calibrated Human-Robot Interaction via Set-Valued Intent Prediction](https://www.roboticsproceedings.org/rss20/p027.html) — RSS 2024 | abstract/공식 색인 | 미연결 |
| W37 | [When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering](https://roboticsproceedings.org/rss22/p142.html) — RSS 2026 | abstract/공식 색인 | 미연결 |
| W38 | [CoRI: Communication of Robot Intent for Physical Human-Robot Interaction](https://proceedings.mlr.press/v305/wang25e.html) — CoRL 2025 | abstract/공식 색인 | 미연결 |
| W39 | [LLawCo: Learning Laws of Cooperation for Modeling Embodied Multi-Agent Behavior](https://proceedings.mlr.press/v306/zhou26i.html) — ICML 2026 | abstract/공식 색인 | 미연결 |
| W40 | [Bandwidth-Efficient Multi-Agent Communication through Information Bottleneck and Vector Quantization](https://ieeexplore.ieee.org/abstract/document/11696376) — ICRA 2026 | abstract/공식 색인 | 미연결 |

## 8. 검증

- `python3 -m py_compile work/scripts/build_reading_tiers.py` 및 tier 생성 통과. CORE 47 / NEXT 275 / REFERENCE 473 / ARCHIVE 242.
- `python3 work/scripts/audit_repository.py` 통과: 논문 1,037편, 표준 note 5,185개, Markdown 5,326개, 내부 링크 9,738개, 오류·경고 0.
- `git diff --check` 통과. Source ID/URL 40개, registry 연결 6개와 해당 overview 파일, 9개 고유 gap anchor, publication/확인 깊이 집계를 검사했다.
- Manifest·tier CSV·active/history reading CSV의 SHA256이 GAP-W1 시작 시점과 동일하다. [보존 hash와 결과](../sources/broad_gap_scout_2026-10-23.json)의 `validation`을 참조한다.

문서 무결성 통과는 위 가설의 입증이 아니다. 공식 source 전체를 정독하거나 모든 후속 연구의 부재를 확인한 것은 아니며, 다음 심화에서 직접 충돌 범위를 좁혀야 한다.
