# 로보틱스 연구 동향

2026-11-19 KST · 2024~2026년 로보틱스 문헌과 실험실 장비를 기준으로 한 후속 검토

**최근 논문에서 반복되는 변화는 개별 알고리즘 성능을 넘어 실제 작업이 막히는 지점을 측정하는 것이다.** 접촉 조작은 파지의 성립뿐 아니라 힘·미끄러짐·재파지를 다룬다. 이동에서는 추정 오차와 지연이 정지·재계획·재개를 어떻게 바꾸는지 본다. 현장에서는 장비·지형·통신·작업자 개입이 바뀌어도 같은 임무를 지속하는지가 중요하다. 이러한 문제는 학습, 모델 기반 제어, 기구 설계 모두에서 나타난다.

**처음의 24편 조사를 확장하면서 좁혀진 질문이 있다.** 위험 기반 재계획, 감각 오차를 반영한 지도, 물성을 확인하는 짧은 시험 동작은 이미 선행이 있다. 석사 연구의 초기 가설은 이런 방법이 존재하는지보다, 비교 조건을 맞춘 뒤 어떤 실패 원인이나 비용 차이가 남는지에 두는 편이 구체적이다. [CERT-Replan](https://arxiv.org/html/2610.09302) · [Certifiably-Correct Mapping](https://roboticsproceedings.org/rss21/p007.html) · [AdaptiGraph](https://arxiv.org/html/2407.07889)

## 조사 범위와 읽기 수준

| 확인 단계 | 편수와 범위 |
|---|---:|
| 출판 목록에서 수집한 고유 URL | **22,274**. 로보틱스 키워드 선별 전 목록 규모 |
| 관련 키워드 후보 | **6,590편**. URL·정규화 제목 중복 제거 후 자동 선별. 관련성이 약한 후보도 포함될 수 있음 |
| 초록 본문을 확보해 주제를 분류한 논문 | **3,016편**. 공식 초록·출판사 기탁·동일 제목 저자 초록 **2,834편**, CoRL 공개 목록과 ID·제목을 맞춘 초록 사본 **182편** |
| 제목 수준 후보 | **3,574편**. 이 행을 초록·내용 검토에 포함하지 않음 |
| 초록의 방법·결과 문장을 대조한 표본 | **144편**. 12개 분야에서 2026년 6편·2025년 3편·2024년 2편씩 뽑고, ACM THRI 12편으로 사용자 연구를 보완. 위 초록 확보 집합에 포함 |
| 본문 구간을 대조한 비교 논문 | **21편**. 실험·한계·배포 절에서 비교 조건을 확인했다. 초록 표본과 16편이 겹친다. 본문 검토 중 18편은 CSV에 있으며, 보완 확인 3편을 포함한 전체 목록은 아래 표에 있다. |

초록 전체 텍스트는 자동 선별과 분야 분류에 사용했다. 같은 분야·연도 내에서 제목과 초록의 관련어가 두드러지고 출판처가 분산된 항목을 뽑았다. 이 표본의 지정 문장을 읽고 대표 연구의 본문 절을 확인했다. CSV에서 논문마다 제목·venue·연도·원출처·읽기 범위를 찾을 수 있다. CoRL의 연도는 행사 기준이다. [논문별 조사 근거 CSV](../sources/robotics_trends_2026-11-18.csv)

| 출판처 | 2024 후보 / 초록 | 2025 후보 / 초록 | 2026 후보 / 초록 |
|---|---:|---:|---:|
| ACM THRI | 68 / 67 | 79 / 79 | 83 / 83 |
| CoRL | 233 / 233 | 217 / 217 | 435 / 423 |
| CVPR | 56 / 43 | 76 / 67 | 113 / 99 |
| ICCV | — | 71 / 63 | — |
| IJRR | 99 / 99 | 116 / 116 | 99 / 98 |
| Journal of Field Robotics | 179 / 179 | 222 / 222 | 199 / 199 |
| L4DC | 4 / 4 | 8 / 8 | 9 / 9 |
| RA-L | 858 / 0 | 990 / 0 | 1,110 / 0 |
| RSS | 119 / 119 | 146 / 146 | 159 / 159 |
| Science Robotics | 95 / 95 | 100 / 100 | 75 / 75 |
| Swarm Intelligence | 10 / 5 | 8 / 6 | 8 / 3 |
| T-RO | 151 / 0 | 237 / 0 | 158 / 0 |

RSS 2024–2026의 전체 proceedings와 CoRL 2024–2025 PMLR 목록 및 CoRL 2026 공식 채택 목록을 출발점으로 삼았다. CVPR 2024–2026·ICCV 2025·L4DC 2024–2026은 제목에서 로봇 시스템과 연결되는 항목을 중심으로 골랐다. 저널은 Crossref의 출판사 기탁 레코드를 사용했다. ICRA, IROS, IEEE 저널 및 ECCV·ICLR·NeurIPS는 관련 개별 논문을 보완 대조했다. 기존 registry는 선행 확인과 중복 판별에 사용했다. [RSS 2024](https://roboticsproceedings.org/rss20/) · [RSS 2025](https://roboticsproceedings.org/rss21/) · [RSS 2026](https://roboticsproceedings.org/rss22/) · [CoRL 2024](https://proceedings.mlr.press/v270/) · [CoRL 2025](https://proceedings.mlr.press/v305/) · [CoRL 2026 공식 채택 목록](https://www.corl.org/program/accepted-papers) · [기존 registry](../../PAPER.md)

CoRL 2026은 공식 목록에서 제목과 OpenReview ID를 확인했다. 초록이 표시된 공개 목록을 두 값으로 대조하고, 연결된 arXiv에서 동일 제목의 저자 초록을 확보한 경우 원출처를 사용했다. 초록 사본은 독립적인 공식 초록으로 세지 않고 별도 출처 표기를 붙였다. IEEE 회의의 전체 논문 일괄 수집은 차단·제한 응답으로 이어져 개별 IEEE Xplore 초록을 사용했다. RA-L·T-RO의 대량 집계는 주로 제목이며 논문 내용 분석은 개별 확인 자료에 한정한다. 2026년은 11월 18일까지이며 학회별 공개 시점과 초록 확보율이 다르다. 아래의 흐름은 서로 다른 출처의 연구에서 반복된 방향을 설명한다. 연도별 성장률이나 분야별 중요도 순서로 읽을 수 있는 표본은 아니다.

<a id="verified-gap-analysis"></a>

## 검증 원장에서 찾은 연구 공백

2026-11-19 기준. 아래는 실험실 장비를 구체화하기 전에 제안했던 다섯 질문의 조사 근거다. 장비 조건을 반영한 [재판정·새 검색](#lab-gap-screen)과 [현행 후보](../research_topics/README.md#robotics-gap-candidates)를 함께 참조한다. 전체 1,250편 중 원장의 본문 확인 표시는 991편, 초록 확인은 259편이다. 본문 표시는 확인한 절의 범위를 포함한다. [원장](../sources/papers.json)

### 태그 교차 집계

표준 다축 태그가 있는 표본은 첫 정규화 배치 50편과 실제 등록 배치 23편의 합집합 **73편**이다. `registry_id` 중복은 없고 64편이 본문 확인 991편과 겹친다. 73편 모두 문서 전체의 검증 상태는 `부분확인`이다. `확인됨`만 허용하면 이 두 배치의 표본은 0편이다. 아래에서는 개별 축에서 확인된 값만 사용했다. CORE 심화 17편은 12편이 겹치고 같은 공통 태그 열이 없어 분모에 더하지 않았다. 보류·중복·발견 후보도 집계에서 제외했다. [첫 배치](../sources/batches/core_next_01.yaml) · [등록 배치 A](../sources/batches/gapfill_2026_11.yaml) · [CORE 심화](../sources/batches/tier1_vla_humanoid.yaml)

| 표준 태그 조합 | 본문 확인 64편 중 교집합 / 두 축 확인 | 73편 전체 중 교집합 / 두 축 확인 | 73편 중 두 축 중 하나 이상 미확인 |
|---|---:|---:|---:|
| 조작 × IL | 28 / 53 | 31 / 59 | 14 |
| 조작 × RL | 13 / 53 | 15 / 59 | 14 |
| 조작 × 모델기반 | 7 / 53 | 7 / 59 | 14 |
| 조작 × 고전제어 | 1 / 53 | 1 / 59 | 14 |
| 내비게이션 × 고전제어 | 0 / 53 | 0 / 59 | 14 |
| 조작 × 촉각 | 9 / 58 | 9 / 65 | 8 |
| 전신제어 × 촉각 | 0 / 58 | 0 / 65 | 8 |
| 내비게이션 × 실제로봇 데이터 | 0 / 48 | 1 / 55 | 18 |
| 사족보행 × 고유수용감각 | 2 / 51 | 3 / 57 | 16 |

두 축의 리스트 어디에도 `unknown`이 없는 행을 분모에 두고, 지정한 두 값이 각각 자기 축에 있는 논문 ID를 한 번 세었다. 한 논문이 여러 조합에 포함될 수 있다. 데이터 출처의 `실제로봇`은 `혼합`을 포함하지 않으며 실물에서 평가했는지와도 다르다.

| 원래 영문 태그 정확 교집합 | 본문 확인 991편 | 전체 1,250편 | [해석] 희소한 이유와 원문 대조 결과 |
|---|---:|---:|---|
| `motion planning` × `collision avoidance` | 1 | 1 | 일반 충돌 검사는 확립된 문제다. CHOMP·STOMP에도 충돌 비용이 있지만 태그는 다르다. 검증할 부분은 **시간 매개화 뒤 실행 경로**까지 검사했을 때의 계획기 선택이다. |
| `SLAM` × `multi-robot` | 0 | 0 | S3E 자체가 다중 로봇 SLAM 자료인데 원장 태그가 `Robotics` 하나다. 수집·태그 누락이 명확하다. 통신 재개 뒤 유효한 루프 폐쇄를 얼마나 빨리 복구하는지는 별도 질문이다. |
| `tactile sensing` × `pose tracking` | 1 | 1 | ViTaSCOPE는 `in-hand pose estimation`을 쓴다. 접촉 상실 구간의 정답 자세와 조작 가능한 물체 대칭을 함께 제공하는 실측 자료의 비용도 크다. |
| `policy evaluation` × `real-to-sim` | 1 | 1 | PolaRiS는 `policy-evaluation`을 쓴다. 실제 시행 분배와 정책 순위 연구가 이미 있어, 집계만 보면 선점 위험을 크게 과소평가한다. |
| `quadruped locomotion` × `slip detection` | 0 | 0 | 적응 보행과 미끄럼 감지는 각각 선행이 있다. 독립적인 발 미끄럼 정답·개입 시점·넘어짐 결과를 같은 실기 자료로 얻기 어렵다. |

영문 표는 각 논문의 `tags`에 두 문자열이 모두 있는지를 대소문자·공백·하이픈 그대로 검사했다. **희소성은 탐색 단서**다. 다섯 조합 모두 해당 분야를 이미 연구한 반례가 있다. 아래에서 '열려 있다'는 판단은 구체적인 비교 조건에만 적용한다. 실기 자료를 갖추는 비용이 결과 활용 가치를 넘으면, 미연구 영역이어도 주제로 삼을 이유가 약하다.

### 저자가 반복해서 밝힌 한계와 현재 논쟁

73편 중 저자 보고 한계가 YAML에 적힌 것은 33편, `unknown`은 40편이다. 한계의 출현 빈도로 분야 전체를 순위화하기에는 누락이 많다. 아래에는 원문에서 직접 확인한 한계·향후 과제를 쌍으로 묶었고, 그로부터 도출한 검증 질문은 마지막 열에 두었다.

| 반복된 문제 | 원문에서 확인한 경계 | 논쟁과 이를 가를 비교 [해석] |
|---|---|---|
| 저장한 경로와 실행 경로의 차이 | TrajOpt는 연속 구간의 swept volume을 근사한다. MoveIt의 시간 매개화 문서는 허용 오차 안에서 경로가 변해 추가 충돌 검사가 필요할 수 있다고 명시한다. PrismPlan은 공통 백엔드에서 최초 해와 경로 품질의 우위가 서로 다르다고 보고한다. [TrajOpt p.7](https://rll.berkeley.edu/trajopt/ijrr/2013-IJRR-TRAJOPT.pdf#page=7) · [MoveIt](https://moveit.picknik.ai/main/doc/examples/time_parameterization/time_parameterization_tutorial.html) · [PrismPlan §7](https://arxiv.org/pdf/2610.23884#page=17) | 빠른 해를 찾는 계획기와 실행 조건을 통과하는 해를 빨리 찾는 계획기가 같은가. 같은 장면·시간 예산에서 검증 비용까지 포함한 순위와 제외한 순위를 짝지어 비교한다. |
| 제한된 통신에서의 지도 복구 | S3E는 시스템 확장과 통신·연산 제약을 한계로, MR-COGraphs는 제약 환경에서의 자율 탐색을 후속 과제로 제시한다. SKiD-SLAM은 임의의 이상치와 네트워크 조건에서의 강건성 보장이 없음을 명시한다. [S3E p.7](https://arxiv.org/pdf/2210.13723#page=7) · [MR-COGraphs p.8](https://arxiv.org/pdf/2412.18381#page=8) · [SKiD-SLAM §X](https://arxiv.org/pdf/2610.38141#page=25) | 평균 대역폭·최종 궤적 오차가 같아도 긴 단절 직후의 잘못된 병합이 임무까지 남는 시간이 다를 수 있다. 연결이 회복된 순간부터의 오차·복구시간을 별도 측정한다. |
| 가림 뒤 느리거나 불확실한 상태 복원 | UniTac2Pose는 초기 자세 추정이 추적보다 느리다고 밝힌다. ViTaSCOPE는 촉각 전단 측정의 잡음·순응성과 추론 속도를 한계로 든다. AURORA도 가림·약한 텍스처에서의 자세 오차를 명시한다. [UniTac2Pose p.9](https://raw.githubusercontent.com/mlresearch/v305/main/assets/wu25d/wu25d.pdf#page=9) · [ViTaSCOPE p.10](https://arxiv.org/pdf/2506.12239#page=10) · [AURORA §5](https://arxiv.org/pdf/2609.08493#page=9) | 관측을 계속 융합하는 편이 유리한가, 언제 추정을 포기하고 다시 초기화해야 하는가. 프레임 평균 오차와 잘못된 자세를 신뢰한 시간을 구별한다. |
| 시뮬레이션에서 맞은 순위의 적용 범위 | SIMPLER는 강체·고정 카메라 등 환경 가정을 밝힌다. YUBI-Real2Sim은 보지 않은 장면에서 재구성 품질로 정책 순위의 신뢰성을 판정하는 일반 규칙을 아직 확립하지 못했다고 보고한다. PolaRiS는 짝지은 실물·시뮬레이션 환경에서 순위를 검증했다. [SIMPLER pp.10–11](https://arxiv.org/pdf/2405.05941#page=10) · [YUBI-Real2Sim](https://arxiv.org/abs/2610.17521) · [PolaRiS §5](https://arxiv.org/pdf/2512.16881#page=10) | 장면별 순위가 달라지는 조건에서 전체 평균 하나로 배포 정책을 고를 수 있는가. 실물 시행의 불확실성과 시뮬레이터의 체계적 순위 오류를 분리한다. |
| 지형에 닿아야 위험을 알게 되는 보행 | RMA는 맹목 보행에서 갑작스러운 계단 하강·복수 다리 방해에 실패할 수 있다고 적었다. DreamWaQ는 다리가 먼저 장애물에 닿아야 적응하는 한계를 명시한다. LUNA 실기에서는 침하·미끄럼과 조명에 따른 인지 실패가 동시에 관찰됐다. [RMA p.9](https://arxiv.org/pdf/2107.04034#page=9) · [DreamWaQ p.6](https://arxiv.org/pdf/2301.10602#page=6) · [LUNA 현장 보고](https://arxiv.org/abs/2610.12276) | 정책 내부 적응만으로 충분한가, 별도 감속 판단이 도움이 되는가. 동일 보행 정책·센서·오경보 예산에서 실패 전 확보한 시간과 잘못 정지한 비용을 함께 비교한다. |

### 최근 3개월의 선점 조사

arXiv Atom API를 2026-11-19에 검색했다. 최초 제출일 범위는 2026-08-19부터 검색 시점까지이고 수정본은 arXiv ID로 묶었다. 각 질의에 `submittedDate:[202608190000 TO 202611192359]`를 AND로 결합했다. 아래 각 행의 두 줄은 별도 질의다. 각 용어는 초록 필드(`abs:`)의 인용구로 검색했다. 응답 상한은 질의당 80건이었고 잘린 질의는 없었다. [arXiv API](https://info.arxiv.org/help/api/user-manual.html)

| 후보 | 초록 검색식 두 개 | 응답 건수 → 분야 내 고유 제목 | 주요 대조 원고 |
|---|---|---:|---|
| 계획 | (motion planning OR trajectory optimization) AND (collision checking OR continuous collision OR collision detection OR motion validation)<br>(motion planning OR robot motion planner) AND (benchmarking OR collision-free trajectories) AND (manipulator OR robot arm OR manipulation) | 11+7 → 18 | [PrismPlan, 9/26](https://arxiv.org/abs/2610.23884) · [좁은 단계 충돌 검사 순서, 9/24](https://arxiv.org/abs/2609.30599) |
| 공동 SLAM | (collaborative SLAM OR multi-robot SLAM OR multi-robot mapping OR distributed SLAM) AND (communication OR bandwidth OR loop closure)<br>(loop closure OR place recognition) AND (communication OR bandwidth) | 2+6 → 8 | [SKiD-SLAM, 10/28](https://arxiv.org/abs/2610.38141) · [분산 불변 EKF SLAM, 10/22](https://arxiv.org/abs/2610.31221) |
| 촉각 | (tactile OR visuotactile) AND (pose estimation OR pose tracking OR object tracking) AND (contact OR in-hand)<br>(in-hand OR in hand) AND (loss of contact OR relocalization OR occlusion OR re-initialization) | 3+61 → 63 | [AURORA, 9/8](https://arxiv.org/abs/2609.08493) · [OccluDex, 9/30](https://arxiv.org/abs/2609.39017) |
| 정책 평가 | (robot OR robotic) AND (policy ranking OR policy rankings OR sim-real correlation OR simulation-real correlation OR real-world policy evaluation)<br>(policy evaluation OR policy selection OR ranking consistency) AND (manipulation OR robot policies) | 7+31 → 36 | [AnyRank, 10/10](https://arxiv.org/abs/2610.14603) · [YUBI-Real2Sim, 10/13](https://arxiv.org/abs/2610.17521) · [RoboFQE, 10/13](https://arxiv.org/abs/2610.18699) |
| 보행 | (quadruped OR quadrupedal OR legged locomotion) AND (slip OR slippery OR friction)<br>(legged OR quadruped) AND (fall prediction OR failure prediction OR safe stopping OR fall prevention) | 9+0 → 9 | [토양 마찰 추정, 9/29](https://arxiv.org/abs/2609.36582) · [LUNA, 10/8](https://arxiv.org/abs/2610.12276) |

검색된 고유 ID는 총 134개다. 통신 일반·사람 손 추적 등의 부적합 결과도 포함된 검색 분모다. 가까운 원고는 제목·초록으로 선별하고, 갈림점은 원문이나 공식 문서에 연결했다. 최근 3개월에 낸 원고가 적다는 이유만으로 통신·보행의 선점 위험을 낮추지 않았다. 이전부터 존재하는 경쟁 방법도 후보별 비교에 넣었다.

<a id="lab-gap-screen"></a>

## 실물 장비를 기준으로 다시 찾은 연구 공백

2026-11-19 KST. 학교의 RTX 5090·로봇팔·Unitree G1과 6개월~1년의 연구 기간을 반영했다. 과거 검색의 다섯 주제와 새 질문을 모두 직접 선행에 대조했다. 아래는 이 날짜에 공개된 문헌을 대상으로 한 탐색이다. [새 후보별 가장 가까운 연구·파일럿·중단 조건](../research_topics/README.md#robotics-gap-candidates)

### 기존 다섯 제안의 재판정

| 기존 제안 | 이미 알려진 부분과 투자 판단 |
|---|---|
| 실행 궤적으로 계획기 재평가 | MoveIt는 시간 매개화 후 경로 재검사가 필요할 수 있다고 명시하고 PrismPlan은 공통 검사기·시간 예산에서 계획기를 비교한다. 특정 제어기에서 순위가 바뀔 수 있다는 가능성만으로 별도 평가 연구를 시작할 근거가 약하다. [MoveIt](https://moveit.picknik.ai/main/doc/examples/time_parameterization/time_parameterization_tutorial.html) · [PrismPlan](https://arxiv.org/abs/2610.23884) |
| 다중 로봇 재접속 후 루프 폐쇄 전송 | Swarm-SLAM은 제한된 예산에서 유망한 루프 후보를 고르고 SKiD-SLAM은 제한된 통신에서 실기 분산 SLAM을 검증했다. 재접속 시점의 바이트당 이득은 여전히 물을 수 있으나, 같은 현상을 측정할 복수 이동 플랫폼·기록이 현재 자원의 강점은 아니다. [Swarm-SLAM](https://arxiv.org/abs/2301.06230) · [SKiD-SLAM](https://arxiv.org/abs/2610.38141) |
| 손안 자세 추적의 재초기화 | UniTac2Pose가 불확실성을 이용해 추적 드리프트를 찾고 AURORA가 자세 불확실성으로 회전 행동을 고른다. 재초기화 시점 하나의 추가 이득이 작을 수 있고 보유 손의 촉각 구성도 미확인이다. [UniTac2Pose, CoRL](https://proceedings.mlr.press/v305/wu25d.html) · [AURORA](https://arxiv.org/abs/2609.08493) |
| 시뮬레이션으로 실물 정책 순위 판정 | AnyRank는 제한된 시행으로 정책을 순차 비교하고 YUBI-Real2Sim은 보지 않은 장면에서 순위 신뢰성이 달라지는 문제를 다룬다. 배포 장면 비중에 따른 조건부 결론만으로 독립 방법을 추천하기 어렵다. [AnyRank](https://arxiv.org/abs/2610.14603) · [YUBI-Real2Sim](https://arxiv.org/abs/2610.17521) |
| 사족 로봇 미끄럼 뒤 감속 | 미끄럼 감지와 회복을 연결한 실물 사족 연구가 있고 후속 센서도 있다. G1의 이족 회복으로 옮기면 접촉·기저 제어기가 달라져 사족 주장의 검증이 되지 않는다. [IEEE T-IE](https://ieeexplore.ieee.org/document/10769508) · [SlipSense](https://ieeexplore.ieee.org/document/11696041) |

### 검증 원장에서 얼마나 보이는가

`papers.json` 1,250편 중 `provenance.content_evidence == FULL_TEXT_CHECKED`인 991편의 기존 `tags`만 사용했다. 아래 영문 표기는 소문자화하고 공백·하이픈·밑줄을 공백 하나로 바꾼 뒤 태그 전체와 비교한 값이다. 한 칸의 여러 표기는 OR이며 논문별로 한 번 센다. A·B 열은 각 집합의 크기다. 같은 연구가 제목 또는 본문에서 확인되는데도 교집합이 0인 사례가 아래에 있다. 정규화 배치 1의 별도 축으로 집계한 통계는 [검증 표본](#verified-gap-analysis)에 있다. [원장](../sources/papers.json)

| 제안 | 태그 A | 태그 B | A | B | A ∩ B |
|---|---|---|---:|---:|---:|
| 시행 간 영향 | reset / reset distribution / reset free learning | evaluation / benchmark / policy evaluation | 2 | 47 | 0 |
| 조립 복구 | assembly / precision assembly | recovery / failure detection / failure diagnosis / failure recovery | 8 | 10 | 0 |
| 제한된 시연 | imitation learning | constraint / constraints / constrained learning / active learning / active exploration | 62 | 3 | 0 |
| 당김 해제 | whole body control / whole body | force control / force feedback | 25 | 5 | 0 |
| 하중 운반 | humanoid / locomotion / whole body control | payload / system identification / sloshing | 53 | 0 | 0 |

[해석] 0이 나온 가장 명백한 이유는 수집과 색인이다. AutoEval의 공식 본문이 리셋을, REASSEMBLE의 본문이 접촉 조립을, Brace Yourself의 본문이 전신 힘 제어를 직접 다룬다. 특히 마지막 행은 하중 관련 B 태그가 한 건도 없어 교집합에 정보가 없다. 문헌에 남는 질문은 서로 다른 입력이나 행동을 공정하게 비교할 수 있는지에서 찾았다. [AutoEval](https://proceedings.mlr.press/v305/zhou25a.html) · [REASSEMBLE](https://www.roboticsproceedings.org/rss21/p059.html) · [Brace Yourself](https://arxiv.org/html/2609.25486)

### 최근 3개월의 경쟁 연구와 확인 범위

arXiv 최초 제출 2026-08-19~2026-11-19를 기준으로 제목·초록의 동의어를 검색하고, 관련 원고의 최초 제출일을 초록 페이지에서 대조했다. 아래 질의어를 arXiv와 웹 검색에 조합했고, PMLR·RSS·저자 원문·출판사 페이지로 과거 직접 선행까지 추적했다. 좁은 Atom 초록 질의는 리셋·내부 하중에서 0건, 조립에서 2건이었고 시연·전신 힘 질의는 시간 초과·요청 제한으로 건수를 확보하지 못했다. 제목·웹 검색이 앞의 0건과 누락을 보완했다. 아래 수록 원고는 직접 대조한 예이며 기간 전체의 전수 목록은 아니다. [arXiv API 검색 규약](https://info.arxiv.org/help/api/user-manual.html)

| 후보와 검색어 | 기간 내 확인한 가까운 arXiv | 무엇이 이미 해결됐고 무엇을 검증할 것인가 |
|---|---|---|
| 시행 간 영향 · `robot policy evaluation reset carryover`, `previous trial initial conditions robot manipulation`, `autonomous manipulation evaluation reset` | [HALTER, 09-16](https://arxiv.org/abs/2609.19413) · [AnyRank, 10-10](https://arxiv.org/abs/2610.14603) · [Practice Is Not Free, 11-15](https://arxiv.org/abs/2611.19979) | HALTER §III-D는 장면 그래프로 리셋을 검증하고 Practice §5는 시행 간 독립 가정의 한계를 직접 언급한다. 정책 순위 추정·자동 리셋·시행 비용은 선행이 있다. 물리적 완전 복원으로 이전 정책의 영향을 없앴을 때 선택이 바뀌는지 확인한 결과는 이 원문들에서 찾지 못했다. |
| 조립 복구 · `peg insertion failure recovery grasp slip movable fixture`, `assembly exception strategy active probing`, `dual control active estimation peg insertion` | [VFAL, 09-12](https://arxiv.org/abs/2609.14133) · [Task-aware DMPs, 09-19](https://arxiv.org/abs/2609.23151) | VFAL §V는 먼저 파지돼 있는 부품을 가정하고, DMP §V는 정렬 실패 후 나선 탐색을 수행한다. 고전 연구는 오류에 맞는 복구를 고르며 최근 저널은 탐촉으로 위치 추정과 삽입을 함께 개선했다. 독립 근거가 필요한 부분은 고장이 구별되지 않는 조건에서 비용을 지불해 두 기준 좌표 중 하나를 관측한 뒤 복구 동작을 바꾸는 효과다. [ICRA의 복구 전략](https://hcr.ijs.si/resources/papers/icra20.pdf) · [IEEE T-ASE의 이중 제어](https://doi.org/10.1109/TASE.2026.3679278) |
| 제한된 시연 · `active imitation learning projected demonstrations choose constraints`, `constraint-consistent learning from demonstration`, `performance guided data collection robot demonstrations` | [Touch2Robot, 09-21](https://arxiv.org/abs/2609.24660) · [Mulligan, 10-05](https://arxiv.org/abs/2610.05882) | 촉각 피드백을 보면서 시연을 수집하거나, 성능을 보고 추가 시연 위치를 고르는 방법이 있다. Mulligan §5는 초기 상태의 매개변수화·배치 가능성을 가정한다. 상태에 더해 어느 제약 방향을 바꿀지 선택하는 비용 대비 이득이 필요하다. [Mulligan §5](https://arxiv.org/html/2610.05882#S5) |
| 당김 해제 · `humanoid sudden loss of hand contact pulling latch`, `humanoid bracing force control load release balance` | [실물 문 열기, 09-01](https://arxiv.org/abs/2609.01518) · [Brace Yourself, 09-21](https://arxiv.org/abs/2609.25486) · [Ctrl-F, 11-03](https://arxiv.org/abs/2611.05507) | 문을 열고 지지하고 힘을 추종하는 기능은 이미 존재한다. Ctrl-F §5는 보지 않은 동작으로의 전이를 한계로 든다. 해제 전 작업량과 시간을 맞춘 과도 응답에서 단순 제어를 이겨야 한다. |
| 하중 운반 · `humanoid dynamic payload identification object transport`, `internal payload sloshing input shaping robot arm`, `quadruped compliant payload interactions` | [HOTICE, 09-21](https://arxiv.org/abs/2609.25363) · [Feeling Through the Load, 10-06](https://arxiv.org/abs/2610.08637) | 전신 장애물 회피 운반과 외부에서 하중에 가한 힘에 대한 순응이 연구됐다. 같은 기간 저널에는 보이지 않는 내부 하중을 다룬 조작 연구도 있다. 팔에서 얻은 식별값의 기종 간 전이로 절감되는 보정 시행 수가 남는 조건이다. [10월 저널](https://link.springer.com/article/10.1007/s44443-026-01376-0) |

**논쟁과 해석 경계.** 실물 평가는 리셋 장면이 시각적으로 같으면 충분한지, 기계적 상태까지 맞춰야 정책을 공정하게 비교할 수 있는지가 쟁점이다. 접촉 조작은 원인을 구별하기 전에 범용 순응 제어로 해결할 수 있는 범위가 얼마나 넓은지에 달려 있다. 시연·운반은 더 복잡한 학습기를 쓰기 전에 원래 명령 기록·고전 식별만으로 같은 이득을 얻는지가 쟁점이다. 이는 문헌에서 도출한 경쟁 가설이고 효과 크기는 미측정이다. 원장과 공개 검색은 미발표 연구, 구현의 공정성, 실험실 하드웨어 접근 조건까지 판정할 수 없다.


## 1. 접촉 조작과 촉각

**흐름.** 손의 자유도가 늘면서 좋은 파지 자세를 생성하는 연구와 파지 이후 접촉을 유지하는 연구가 나뉜다. GraspQP는 힘 폐쇄를 최적화하고, Dexonomy와 DexEvolve는 서로 다른 파지 유형과 초기 자세를 확보하려 한다. CGP는 미래 촉각·로봇 상태를 순응 제어 목표에 연결한다. FARM은 자세·폭·힘을 함께 출력한다. Minimalist Compliance Control은 전류·전압으로 외력을 추정하는 비교 기준을 제시한다. [GraspQP, CoRL 2025](https://proceedings.mlr.press/v305/zurbrugg25a.html) · [Dexonomy, RSS 2025](https://roboticsproceedings.org/rss21/p105.html) · [DexEvolve, RSS 2026](https://roboticsproceedings.org/rss22/p059.html) · [CGP, RSS 2026](https://roboticsproceedings.org/rss22/p005.html) · [FARM, ICRA 2026](https://ieeexplore.ieee.org/abstract/document/11695850) · [Minimalist Compliance Control, RSS 2026](https://roboticsproceedings.org/rss22/p123.html)

**공백과 후속 연구.** 시각 없이 촉각으로 파지한 연구에서는 초기 접촉 뒤 안정한 접촉점으로 옮기지 못하거나 들어올리는 중 놓치는 실패가 남았다. 단일 삽입 또는 들어올리기에서 센서와 제어기를 교차 비교한다. 같은 속도·이득·action에서 촉각을 추가하고, 같은 입력에서 순응 제어기를 바꾼다. 초기 위치·마찰을 나눠 미끄러짐 이후 회복률, 최대 힘, 완료 시간을 비교한다. 촉각이 도움이 되는 접촉 단계와 저비용 전류 관측이 충분한 단계를 가르는 것이 기여 후보다. [Blind Dexterous Grasping, §5 및 부록 D](https://arxiv.org/html/2606.11767)

## 2. 시연 수집과 실세계 학습

**흐름.** UMI와 DexUMI는 사람의 움직임을 로봇이 학습할 수 있는 형식으로 기록하며, EgoVerse와 BiDemoSyn은 각각 여러 기관의 수집과 적은 초기 시연에서 파생 시연을 만드는 비용을 다룬다. HIL-SERL과 Sirius는 배포·훈련 중 사람의 개입을 학습 자료로 활용한다. 자율 수집을 더 많이 돌리는 접근이 같은 노력의 추가 사람 시연보다 항상 유리하지 않다는 CoRL 초기 비교도 있다. [UMI, RSS 2024](https://roboticsproceedings.org/rss20/p045.html) · [DexUMI, CoRL 2025](https://proceedings.mlr.press/v305/xu25b.html) · [EgoVerse, RSS 2026](https://roboticsproceedings.org/rss22/p092.html) · [BiDemoSyn, RSS 2026](https://roboticsproceedings.org/rss22/p001.html) · [HIL-SERL, Science Robotics 2025](https://doi.org/10.1126/scirobotics.ads5033) · [Sirius, IJRR](https://doi.org/10.1177/02783649241273901) · [Autonomous Robot Data Collection, CoRL 2024](https://proceedings.mlr.press/v270/mirchandani25a.html)

**공백과 후속 연구.** 사람의 시간이 같은 경우, 정상 시연 추가와 위험 상태에서 짧게 교정하는 방법 중 어느 쪽이 새 초기 상태에서 더 유용한가? 실패 직전 과제 하나를 고르고 개입 시점, 시연 시간, 리셋 횟수, 로봇 점유 시간을 분리한다. WARP-RM은 역재생을 진행 역행의 감독 신호로 쓰며, 저자도 실제 실패나 복구와의 차이를 한계로 둔다. 정상 시연을 더 모으는 기준과 실제 실패를 복구한 자료를 비교할 근거가 있다. [WARP-RM, §5](https://arxiv.org/html/2606.28320)

## 3. 시뮬레이션, 시스템 식별과 실기 전이

**흐름.** 시뮬레이션의 사실성에는 외관, 접촉, 구동계, 제어 지연이 포함된다. RE3SIM은 장면 재구성과 물리 시뮬레이션을 결합한다. ASAP은 구동 동역학 차이를 보완하고, SPI-Active는 어떤 실기 동작을 수행해야 파라미터가 잘 식별되는지 다룬다. Tune to Learn은 위치 제어 gain의 선호 조건이 학습 및 전이 방식에 따라 달라짐을 보여준다. SPiDR는 시뮬레이션 파라미터 불확실성을 안전 제약에 반영한다. [RE3SIM, ICRA 2026](https://ieeexplore.ieee.org/abstract/document/11695858) · [ASAP, RSS 2025](https://roboticsproceedings.org/rss21/p066.html) · [SPI-Active, CoRL 2025](https://proceedings.mlr.press/v305/sobanbabu25a.html) · [Tune to Learn, RSS 2026](https://roboticsproceedings.org/rss22/p139.html) · [SPiDR, NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/82eb7f4f7377fc5dc81ca85fc90fa735-Abstract-Conference.html)

**공백과 후속 연구.** 실기 측정 예산이 작을 때 오차를 어느 순서로 보정해야 시뮬레이션에서 좋은 정책을 올바르게 고를 수 있는가? 비교 단위를 영상 유사도에서 **보지 않은 과제의 정책 순위와 실패 사건**으로 옮긴다. 외관·물성·지연 중 두 가지를 교차 개입하고, 지연만 보정하는 단순 기준과 domain randomization을 같은 정책·데이터에서 비교한다. 실기에서 순위 역전이 지속되면 파라미터 재조정으로 해결되는 경우와 누락된 물리 상태가 필요한 경우를 나눠 볼 수 있다. [RE3SIM, §IV](https://arxiv.org/html/2502.08645) · [기존 시스템 식별 비교](../../synthesis/05_safety.md#gap-sysid-2026)

## 4. 휴머노이드와 이동 조작

**흐름.** WoCoCo의 순차 접촉, HugWBC의 전신 명령, X-Loco의 이동·넘어짐 회복 통합이 이어진다. FALCON은 외력과 토크 제한을 고려하고, FT-WBC는 특정 구동기 고장을 포함한 전신 제어를 비교했다. PADP와 같이 학습된 이동 행동을 접촉 제약을 만족하는 전신 동역학 변수로 바꿔 기존 제어와 연결하는 흐름도 있다. [WoCoCo, CoRL 2024 행사](https://proceedings.mlr.press/v270/zhang25a.html) · [HugWBC, RSS 2025](https://roboticsproceedings.org/rss21/p067.html) · [X-Loco, RSS 2026](https://roboticsproceedings.org/rss22/p022.html) · [FALCON, L4DC 2026](https://proceedings.mlr.press/v331/zhang26a.html) · [FT-WBC, CoRL 2026](https://openreview.net/forum?id=mjvsJNQuFV) · [PADP, RA-L 2026](https://ieeexplore.ieee.org/abstract/document/11692614/) · [HWC-Loco, ICLR 2026](https://iclr.cc/virtual/2026/poster/10011640)

**공백과 후속 연구.** FT-WBC 실기 검증에서 고장은 단일 구동기에 한정되고 이동과 조작은 주로 순차적이었다. TARC의 가변 제어 주기도 실기 시험이 짧아 에너지 절약을 직접 측정할 수 없었다. 작은 이동 조작 플랫폼으로 운반 중 정지·재개 또는 이동에서 적재로 넘어가는 전환을 하나 고른다. 같은 계산량에서 고정 주기, 사건 기반 주기, 단순 속도 제한을 비교한다. 완주율, 재개 시간, 처리량, 전력·열 제한을 함께 보되 계산 호출 감소를 전력 절약으로 환산하지 않는다. [FT-WBC, §4.3·6](https://arxiv.org/html/2606.24466) · [TARC, CoRL 2026 공식 항목](https://openreview.net/forum?id=WvR13cRtRf) · [TARC, §7](https://arxiv.org/html/2510.23176)

## 5. 상태 추정, 지도와 관측 선택

**흐름.** MASt3R-SLAM이 3D prior를 dense SLAM에 사용했고 DROID-SLAM in the Wild는 불확실성으로 동적 장면을 다룬다. Dr-BA는 레이더 측정에서 직접 최적화하고, 2Fast-2Lamaa는 연속 거리장으로 대규모 LiDAR 기록을 평가한다. Boreas-RT는 더 어려운 실제 경로에서 기존 위치 추정 성능이 저하되는 사례를 제공한다. 위치 추정 정확도와 안전 행동을 직접 연결하는 지도 연구도 이미 있다. [MASt3R-SLAM, CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/html/Murai_MASt3R-SLAM_Real-Time_Dense_SLAM_with_3D_Reconstruction_Priors_CVPR_2025_paper.html) · [DROID-SLAM in the Wild, CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Li_DROID-SLAM_in_the_Wild_CVPR_2026_paper.html) · [Dr-BA, RSS 2026](https://roboticsproceedings.org/rss22/p046.html) · [2Fast-2Lamaa, IJRR](https://doi.org/10.1177/02783649261451003) · [Certifiably-Correct Mapping, RSS 2025](https://roboticsproceedings.org/rss21/p007.html)

**공백과 후속 연구.** 위치 드리프트, 물체 가림, 오래된 점유 정보는 같은 평균 오차에서도 서로 다른 행동을 요구한다. 같은 지도·planner에서 업데이트 지연과 위치 오차를 각각 바꿔, 관측 시각·미관측 여부를 분리할 때 위험 구간의 감속이 달라지는지 확인한다. 고정 여유, unknown-space 회피, 지도 나이만 쓰는 단순 기준으로 충분하다면 추가 학습보다 진단 결과가 중심이다. 공개 로그는 후보 사건을 선정하는 데 쓰고, 다른 행동의 결과는 로봇이 반응할 수 있는 환경에서 평가한다. [관련 3D 지도 공백](../../synthesis/07_perception.md#gap-geometry-2026)

## 6. 계획, 제어와 안전

**흐름.** Neural CBF와 MPC를 연결해 짧은 예측 지평 너머의 안전을 다루는 연구, 분포 변화와 반응형 환경을 포함하는 conformal 계획, 사건 기반 재계획이 있다. CERT-Replan은 위험을 신호로 재계획 시점을 정하고 실기에서 계산 가능성을 확인했다. 원문의 보장 범위는 평가한 유한 지평이며, 시뮬레이션의 장애물은 서로를 피하지만 로봇 행동에는 반응하지 않는다. 다른 L4DC 연구는 이미 반응형 환경을 직접 대상으로 삼는다. [Safe Beyond the Horizon, RSS 2025](https://roboticsproceedings.org/rss21/p112.html) · [Crowd Navigation, CoRL 2025](https://proceedings.mlr.press/v305/yao25a.html) · [Interactive Safe Planning, L4DC 2026](https://proceedings.mlr.press/v331/mirzaeedodangeh26a.html) · [CERT-Replan, §6·부록 G](https://arxiv.org/html/2610.09302)

**공백과 후속 연구.** 안전 조건이 발동한 뒤 정지에서 다시 움직이기까지의 교착과 반복 intervention을 비교할 여지가 있다. 반복 재계획, threshold 기반 감속·정지, CERT-Replan 및 기존 반응형 계획의 예측기와 실행 시간을 맞춘다. 상대 반응과 관측 지연을 독립적으로 바꿔 충돌 여유, 도착률, 교착·재개 시간을 본다. 보장 사건과 시간 범위를 명시하고 횟수가 적은 pilot에서 드문 사고율을 추정하지 않는다.

## 7. 지상 현장 로봇

**흐름.** 지형의 표면 모양을 추정하는 것에서 마찰·통과 비용·차량 동역학을 계획 입력으로 쓰는 방향이 보인다. TravSUITE와 AnyNav는 이 연결을 각각 지도와 마찰 학습으로 다뤘다. 현장 응용에서는 건설 현장 지게차 ADAPT, 서로 다른 유압 장비에서 비교한 굴착기 제어처럼 실제 작업 조건을 포함하는 경우가 있다. 오프로드 동역학 연구는 어려운 장면을 따로 발굴했으며 지도를 조회하는 계산 비용도 보고했다. [TravSUITE, RSS 2026](https://roboticsproceedings.org/rss22/p070.html) · [AnyNav, IJRR](https://doi.org/10.1177/02783649261496456) · [ADAPT, Journal of Field Robotics](https://doi.org/10.1002/rob.70321) · [Off-road Dynamics, CoRL 2026 §5–6](https://arxiv.org/html/2610.22900) · [T-CBF, IROS 2025](https://ieeexplore.ieee.org/abstract/document/11247669)

**공백과 후속 연구.** 보는 모양이 비슷해도 비가 온 뒤나 하중이 바뀌면 통과 가능성이 달라진다. 같은 경로에서 노면 접지와 하중을 분리해 변동시키고, 지도 기반 선제 감속과 바퀴 슬립 뒤 반응하는 제어의 시간·안정성 차이를 본다. 최소 trial은 차량 한 대와 구간 두 곳으로 줄일 수 있다. 현장 평가는 주행 거리당 중단, 통과 시간, 개입이 필요했던 상황을 기록한다.

## 8. 다중 로봇과 통신 제약

**흐름.** 비동기 조립 APEX-MR, 달 표면·용암 동굴을 모사한 이종 로봇 협업, 제한된 네트워크에서의 Commerge가 각각 작업 순서, 플랫폼 역할, 지도 전송을 다룬다. Science Robotics의 swarm 연구에는 작은 구조화 정책이 연속 행동 기준보다 실기 전이에서 유리한 비교도 있다. 복잡한 다중 로봇 정책이 필요하다는 가설을 세울 때 간단한 분산 규칙이 중요한 대안이다. [APEX-MR, RSS 2025](https://roboticsproceedings.org/rss21/p098.html) · [Planetary Skylight and Lava Cave, Science Robotics 2025](https://doi.org/10.1126/scirobotics.adj9699) · [Commerge, IJRR](https://doi.org/10.1177/02783649261464202) · [Structural Bias for Robot Swarms, Science Robotics 2026](https://doi.org/10.1126/scirobotics.adw4624) · [Fault-Tolerant Multimodal Localization, T-RO 2026](https://ieeexplore.ieee.org/abstract/document/11551518)

**공백과 후속 연구.** 지도 압축·병합과 분산 위치 추정은 이미 활발하다. 조건을 **부분 연결 상태에서 임무 할당의 회복**으로 좁혀, 재접속 시 지도·발견 사건·약속한 역할 변경 중 어떤 정보를 먼저 보내야 하는지 본다. 같은 통신 예산과 사람 개입 시간을 맞추고, 중복 구역 방문과 임무 완료 시간으로 비교한다. 로봇별 위치 추정과 주행 정책을 먼저 고정하면 네트워크 손실과 협업 결정을 구분할 수 있다. [Robots as Tokens, §7의 교착 사례](https://arxiv.org/html/2606.15550)

## 9. 변형체 조작

**흐름.** AdaptiGraph는 몇 번의 상호작용으로 물성을 적응시키고 JIGGLE은 고정 경계의 능동 추정을 다룬다. PGND와 생성 동역학 기반 MPC는 부분 관측을 다룬다. 단순 줄 모형 기반 작업 오차 보정도 실기에서 성립한다. CORD-SLS는 줄과 천에서 강건 MPC와 불확실성 보정을 결합한다. 모델이 정교해질수록 적은 시도나 낮은 손상으로 이어지는지 같은 작업에서 비교할 필요가 있다. [AdaptiGraph, RSS 2024](https://arxiv.org/html/2407.07889) · [JIGGLE, RSS 2024](https://roboticsproceedings.org/rss20/p007.html) · [PGND, RSS 2025](https://roboticsproceedings.org/rss21/p036.html) · [Task-Level ILC, RSS 2026](https://roboticsproceedings.org/rss22/p126.html) · [CORD-SLS, CoRL 2026](https://arxiv.org/html/2606.14188)

**공백과 후속 연구.** 이미 물성 추정, 능동 관측, 반복 보정 각각의 직접 선행이 있다. 같은 겉모양에서 재질과 고정 조건이 구별되지 않아 **실제로 다른 행동을 선택해야 하는 경우**를 먼저 찾는다. 간단한 변위 관측, 능동 탐색, 횟수를 맞춘 ILC와 정답 물성을 받는 비교를 둔다. 정답 정보까지 있어도 성공·손상·시도 횟수가 같다면 선택한 과제는 추정 비교에 부적합하다. [기존 물성·고정 조건 심사](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/cb650415f47a2a45ad883dabe5bd20c382b5c183/work/update/DEFORMABLE_IDENTIFICATION_REVIEW_2026-10-24.md)

## 10. 하드웨어, 소프트 로봇과 공동 설계

**흐름.** 파라미터화한 손 설계, 능동 손바닥, 기저부 힘을 이용한 연속체 상태 추정은 센싱·구동을 기구 구조에서 바꾸는 예다. 부서지기 쉬운 식품에서는 말단 장치와 제어를 함께 최적화했고, motion-conditioned co-design은 제한된 시제품 실험까지 했다. 부품을 추가해 얻는 안정성·정확도와 제어 복잡도·제작 비용을 함께 측정해야 비교가 가능하다. [Open Parametric Hand Design, Science Robotics 2025](https://doi.org/10.1126/scirobotics.ads6437) · [Active Palm, Science Robotics 2026](https://doi.org/10.1126/scirobotics.aei2046) · [Continuum State Estimation, IJRR](https://doi.org/10.1177/02783649261483674) · [Latent Diffeomorphic Co-Design, RSS 2026](https://roboticsproceedings.org/rss22/p195.html) · [Transformer Transformer, CoRL 2026](https://arxiv.org/html/2607.25798)

**공백과 후속 연구.** 고정 예산에서 기구적인 순응성과 능동 제어 중 무엇이 교란을 더 잘 흡수하는가? 교체 가능한 손가락 패드 두 종류와 동일 controller, 또는 동일 패드와 gain 두 조건을 교차 비교한다. 부품 마모·반복 조립 뒤 보정 비용, 손상률과 학습에 없던 물체에서의 성능을 기록한다. 이 설계는 신규 손 전체를 제작하지 않고도 일부 기구 변수의 효과를 볼 수 있다.

## 11. 사람과 로봇의 협업, 보조와 의료

**흐름.** Just-Right Assistance는 사용자의 도달 가능 범위를 추정하고, 휠체어 shared control 연구는 단순한 결정 규칙과 사용자별·과제별 효과를 비교했다. IMPLIED는 사람 피드백을 고정 규칙으로 해석할 때 생기는 차이를 봤다. 보행 보조에서는 시뮬레이션에서 학습한 외골격 제어, 재활 현장에서는 치료사와 사용자의 운동을 연결하는 제어를 각각 평가했다. 실험 참가자·환자 특성과 의료 평가의 범위가 달라 직접 비교에 주의한다. [Just-Right Assistance, RSS 2026](https://roboticsproceedings.org/rss22/p119.html) · [Wheelchair Shared Control, RSS 2026](https://roboticsproceedings.org/rss22/p120.html) · [IMPLIED, CoRL 2026 §5·7](https://arxiv.org/html/2609.13982) · [Exoskeleton Assistance, Nature 2024](https://www.nature.com/articles/s41586-024-07382-4) · [Therapist–Exoskeleton–Patient, Science Robotics 2026](https://doi.org/10.1126/scirobotics.adz9628)

ACM THRI에서도 보조 급식 연구의 신뢰도·수용성 증가와 행성 탐사 협업 연구의 신뢰도 조건 차이 미검출이 함께 나타난다. 과제별 사용성과 실제 작업 안전, 자기보고 신뢰도를 분리할 이유다. [Assistive Feeding, ACM THRI 2025](https://doi.org/10.1145/3758103) · [Planetary Exploration Teaming, ACM THRI 2026](https://doi.org/10.1145/3822499)

**공백과 후속 연구.** 능력 부족과 도움을 받고 싶은 선호는 서로 다르며 훈련 중에도 바뀐다. 동일 작업에서 명시적 요청, 고정 임계값, 온라인 적응을 비교한다. 과도한 도움·늦은 도움·자력으로 완료한 단계·사용자 부담을 분리한다. 좁은 비의료 협업 과제에서 도움 시점의 영향을 먼저 확인하고, 한 번 측정한 능력으로 장기간 반응을 추정하는 문제가 실제 차이를 만드는지 살핀다.

## 12. 공중·수중 및 특수 플랫폼

**흐름.** 작은 비행체의 실시간 LiDAR 계획, 공중 플랫폼과 로봇 팔의 결합을 조사하는 AM-Bench, 수상 환경의 예측 계획, 수중 다중 SLAM이 대표적이다. 특수 플랫폼에서는 같은 팔이라도 기체와 하중 사이의 동역학, 센서의 거리·시야, 통신이 바뀐다. AM-Bench는 단일 멀티로터의 강체 팔이 중심이며 협업 운반이나 연성 기구는 별도 문제로 남긴다. [Safety-Assured MAV Navigation, Science Robotics 2025](https://doi.org/10.1126/scirobotics.ado6187) · [AM-Bench, CoRL 2026 §4.4·6](https://arxiv.org/html/2609.00641) · [Predictive USV Navigation, Journal of Field Robotics](https://doi.org/10.1002/rob.22612) · [Cooperative UAV Field Evaluation, Journal of Field Robotics 2026](https://onlinelibrary.wiley.com/doi/10.1002/rob.70248) · [Electro-SLAM, IJRR](https://doi.org/10.1177/02783649251414426)

**공백과 후속 연구.** 기체를 움직여 관측을 얻는 데 필요한 비용과 접촉 중 안정성을 같은 과제에서 비교할 가치가 있다. 모의 환경의 검사·채집처럼 명료한 작업을 고르고, 한 방향 관측·추가 관측·작업 중 포즈를 유지하는 제어를 같은 시간에서 비교한다. 센싱 복구 시간, 에너지당 유효 작업과 하중 변화 뒤의 재개 성공을 지표로 삼는다. 같은 기구 구성의 소규모 실험에서 반복되는 차이를 먼저 확인한다.

## 석사 연구로 압축하면

| 조건 | 먼저 검증할 질문 | 구분할 기준 | 가치가 낮아지는 결과 |
|---|---|---|---|
| 공개 기록·시뮬레이션부터 사용 | 지도 갱신 시각과 위치 오차를 분리하면 정지·재개 판단이 달라지는가 | 지도 나이·고정 여유·기존 위험 기반 재계획과 같은 비용에서 비교 | 지도 나이만 쓰는 규칙이 모두 설명하거나 기록 재생에서만 차이가 난다. |
| 소형 로봇 팔 접근 가능 | 촉각이 필요한 접촉 단계와 전류·순응 제어로 충분한 단계가 구분되는가 | 속도·제어기·물체·접촉 단계의 요인 비교 | 하나의 센서나 고정 gain으로 항상 같은 성능이 나온다. |
| 반복 실기 계측 가능 | 적은 측정으로 sim-to-real 정책 순위가 뒤집히는 원인을 식별할 수 있는가 | 외관과 지연·gain, 단순 보정과 domain randomization | 보정 예산을 맞추면 단순 지연 보정과 차이가 없다. |
| 시뮬레이션 두 대부터 시작 | 재접속 후 어떤 임무 상태 공유가 중복 작업을 줄이는가 | 지도·발견 사건·역할 변경, 같은 통신 예산 | 주기적 사건 공유만으로 충분하다. |

이 표는 장비를 특정하기 전의 조건별 탐색 질문이다. 학교 로봇팔과 G1의 접근성을 반영한 우선순위 및 기존 실기 전이·지도 제안의 투자 판단은 [현행 후보](../research_topics/README.md#robotics-gap-candidates)와 [선행 재검토](#lab-gap-screen)에 정리했다.

## 본문에서 확인한 비교 경계

| 비교 논문 | 대조 구간 | 후속 질문에 중요한 확인 내용 |
|---|---|---|
| [CERT-Replan](https://arxiv.org/html/2610.09302) | §6·부록 G | 유한 지평에서의 위험 경계다. 실기 주행의 장애물은 가상이며 시뮬레이션 상대는 로봇에 반응하지 않는다. |
| [CORD-SLS](https://arxiv.org/html/2606.14188) | §6 | 변형체 MPC에 부드러운 접촉 모델과 인식 오차 보정을 결합한다. 안전 확률의 범위는 고려한 모델·오차 집합에 의존한다. |
| [HumanoidMimicGen](https://arxiv.org/html/2605.27724) | §6.1·7 | 수동 skill 분절, 작업 순서와 성공 조건의 설계가 파생 시연을 제한한다. |
| [FT-WBC](https://arxiv.org/html/2606.24466) | §4.3·6 | 실기 pick-and-place 보정에서 단일 구동기 고장을 다뤘으며 걸으며 조작하는 조건은 후속이다. |
| [Robots as Tokens](https://arxiv.org/html/2606.15550) | §5.3·7 | 일부 지도에서 교착에 빠졌을 때 탈출 시연 부족과 시야 범위의 한계가 남는다. |
| [ExpertGen](https://arxiv.org/html/2603.15956) | §7·부록 C.3 | 시뮬레이션에서 행동 prior를 보정한 뒤 Franka·평행 그리퍼·세 카메라 구성으로 실기 전이를 평가했다. |
| [Transformer Transformer](https://arxiv.org/html/2607.25798) | §5 | 시뮬레이션의 서로 다른 기구 설계 비교와 실기 제작을 통한 검증의 범위를 구별한다. |
| [WARP-RM](https://arxiv.org/html/2606.28320) | §5·부록 D | 실제 역행 감독을 대신한 역재생, 단일 양팔 플랫폼, 수집 행동 범위가 한계다. |
| [SEED-UMI](https://arxiv.org/html/2609.11753) | 평가 프로토콜·§7 | 같은 외골격을 활용해도 다른 손의 링크 구조와 관절 범위에 맞춘 기구·보정 작업이 남는다. |
| [DexCraft 연구](https://arxiv.org/html/2606.30749) | §8 | 수동 하위 목표 라벨, 각 과제의 단일 물체 instance, 시뮬레이션 시연 방식 때문에 실기 일반화의 범위가 제한된다. |
| [Blind Dexterous Grasping](https://arxiv.org/html/2606.11767) | §5 | 접촉 이후 파지점을 안정화하지 못해 빈 파지나 들어올릴 때 미끄러지는 실패가 남는다. |
| [IMPLIED](https://arxiv.org/html/2609.13982) | §5.2·7 | 실제 협업 실험과 선호 특징의 종류를 미리 알고 가중치를 추정하는 가정을 확인했다. |
| [Off-road Dynamics](https://arxiv.org/html/2610.22900) | §6 | 실기 자료 수집 비용과 지도 조회·보간 시간의 증가가 강한 이동 성능과 함께 보고된다. |
| [AM-Bench](https://arxiv.org/html/2609.00641) | §4.4·6 | 실기는 시뮬레이션 거동과 한 학습 경로의 확인이며 범위는 단일 강체 팔을 단 멀티로터다. |
| [Simulator-in-the-Loop Cloth](https://arxiv.org/html/2606.24552) | §6 | 옷의 메시 복원과 real-to-sim 보정이 새 옷마다 필요하며 rollout 예산이 제어율을 제한한다. |
| [TARC](https://arxiv.org/html/2510.23176) | §4·7 | 하나의 공통 유지 시간으로 제어하며 짧은 실험에서 에너지 절약은 직접 측정하지 않았다. 명시적 안전 제약은 별도다. |
| [AdaptiGraph](https://arxiv.org/html/2407.07889) | §IV | 물성 변화에 대한 예측, 실기 몇 회 탐색의 식별, 계획 이득을 구별해 평가한다. |
| [PGND](https://arxiv.org/html/2506.15680) | §V | 일정한 입자 수를 가정하며 짧은 관측 이력으로 물성을 암묵적으로 추정한다. |
| [Exoskeleton Assistance](https://pmc.ncbi.nlm.nih.gov/articles/PMC11344585/) | Discussion | 실측할 수 있는 웨어러블 센서 신호만 제어 입력에 사용하고 근육 상태 등의 모의 변수를 분리한다. |
| [HIL-SERL](https://arxiv.org/html/2410.21845) | §6 | 실세계 RL의 작동 범위를 학습 설계·과제·인간 개입 속에서 해석한다. |
| [RE3SIM](https://arxiv.org/html/2502.08645) | §IV·IV-A | 실기 검증은 Franka 평행 그리퍼와 손목·외부 카메라 구성을 사용한다. |
