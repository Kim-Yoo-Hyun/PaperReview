# 레지스트리 진단

2026-11-19 KST · 신규 등록 전 1,227편의 파일 기반 진단. 이후 등록·교정이 반영된 수치는 [현재 통계](./REGISTRY_STATS.md)에서 확인한다.

별도의 첨부 파일이 없어 저장소 논문 원장을 진단 대상으로 삼았다. 원장·등급표·검색 색인의 1,227개 `paper_id`를 1:1로 대조했다. 논문별 요약은 로컬 overview의 절과 텍스트 유무를 집계했다. 링크는 파일의 문자열과 출처 분류를 확인했다. 외부 검색·HTTP 요청과 데이터 수정은 하지 않았다. [논문 원장](../work/sources/papers.json) · [등급표](./READING_TIERS.csv) · [검색 색인](./REGISTRY_INDEX.csv)

## 먼저 손봐야 할 문제 Top 5

| 순위 | 심각도 | 문제 | 파일 근거 | 우선 조치 |
|---|---|---|---|---|
| 1 | 최우선 | 최근 6개월 정식 발표 비중 산출 불가 | 발표 월·일 필드 1,227편 누락(100.0%). 2026년 표기 354편 중 6개월 구간을 판정할 구조화 날짜가 없다. | 정식 게재일과 최초 공개일을 별도 필드에 출처와 날짜 정밀도까지 기록한다. |
| 2 | 높음 | 공개 식별자와 게재 근거 연결 부족 | 공개 ID 없음 366편(29.8%), 그중 CORE/NEXT 87편. 주 출처가 학회 목록인 43편과 arXiv를 주 출처로 두고 게재 확인용 링크 필드가 비어 있는 peer-reviewed 233편을 확인했다. | CORE/NEXT부터 논문별 공식 게재 근거와 DOI·arXiv·OpenReview 식별자를 대조한다. 학회 목록과 논문별 URL의 구분을 검토한다. |
| 3 | 높음 | 태그 표기 분산 | 대소문자·공백·하이픈 차이 63묶음이 581편에 걸친다. `Reinforcement Learning`만 검색하면 동의 태그까지 포함한 119편 중 37편을 놓친다. | 표준 태그와 별칭 표를 도입한다. 희소 태그는 표기 중복과 독립 개념을 구분해 검토한다. |
| 4 | 중간 | 기계 판독용 요약 접근성 | `problem`·`method`를 모두 갖추지 않은 항목 821편(66.9%), 그중 CORE/NEXT 173편. overview 요약 절은 1,227편에 있다. | 기존 overview에서 읽기 전용 요약 색인을 만들면 논문 노트와 중복 입력을 줄일 수 있다. |
| 5 | 중간 | 레거시 링크와 발표처 표기 혼재 | URL 위치에 상태 문구를 넣은 `project` 617편(50.3%). RA-L은 짧은 이름 32편과 정식 이름 3편으로 갈라진다. | 집계·내보내기는 `sources.*.url`과 검토한 발표처 대응표를 사용한다. 링크 여부와 공개 상태를 분리한다. |

## 1. 논문 분포

전체 **1,227편**. 기록 연도 기준 2024–2026년 **934편(76.1%)**이며 2025년이 409편으로 가장 많다. 아래 연도·발표처는 원장에 기록된 값을 사용했다.

| Tier | 편수 | 전체 비중 |
|---|---|---|
| CORE | 50 | 4.1% |
| NEXT | 427 | 34.8% |
| REFERENCE | 508 | 41.4% |
| ARCHIVE | 242 | 19.7% |

### 연도별

| 연도 | 편수 | 전체 비중 |
|---|---|---|
| 2026 | 354 | 28.9% |
| 2025 | 409 | 33.3% |
| 2024 | 171 | 13.9% |
| 2023 | 60 | 4.9% |
| 2022 | 47 | 3.8% |
| 2021 | 37 | 3.0% |
| 2020 | 33 | 2.7% |
| 2019 | 20 | 1.6% |
| 2018 | 19 | 1.5% |
| 2017 | 18 | 1.5% |
| 2016 | 9 | 0.7% |
| 2015 | 7 | 0.6% |
| 2014 | 5 | 0.4% |
| 2013 | 4 | 0.3% |
| 2012 | 1 | 0.1% |
| 2011 | 6 | 0.5% |
| 2010 | 1 | 0.1% |
| 2009 | 1 | 0.1% |
| 2008 | 1 | 0.1% |
| 2007 | 1 | 0.1% |
| 2005 | 1 | 0.1% |
| 2004 | 1 | 0.1% |
| 2003 | 1 | 0.1% |
| 2002 | 3 | 0.2% |
| 1999 | 3 | 0.2% |
| 1998 | 2 | 0.2% |
| 1996 | 1 | 0.1% |
| 1995 | 1 | 0.1% |
| 1992 | 4 | 0.3% |
| 1988 | 1 | 0.1% |
| 1987 | 1 | 0.1% |
| 1985 | 1 | 0.1% |
| 1981 | 1 | 0.1% |
| 1968 | 1 | 0.1% |
| 1960 | 1 | 0.1% |

`year`와 `publication.venue_year`가 다른 항목은 6편이다. 모두 2025년 기록에 2024년 venue year가 붙어 있다. 이 차이는 집계 열 선택에 따라 2024·2025년 숫자를 바꾸므로 원장 값의 출처를 확인할 대상이다. [pr-1044](../2024/CoRL/2024_CoRL_Simple-Masked-Training-Strategies-Yield-Control-Policies-T/01_overview.md) · [pr-1059](../2024/CoRL/2024_CoRL_ReMix-Optimizing-Data-Mixtures-for-Large-Scale-Imitation-L/01_overview.md) · [pr-1061](../2024/CoRL/2024_CoRL_TRANSIC-Sim-to-Real-Policy-Transfer-by-Learning-from-Onlin/01_overview.md) · [pr-1063](../2024/CoRL/2024_CoRL_Mobility-VLA-Multimodal-Instruction-Navigation-with-Long-C/01_overview.md) · [pr-1064](../2024/CoRL/2024_CoRL_TidyBot++-An-Open-Source-Holonomic-Mobile-Manipulator-for/01_overview.md) · [pr-1068](../2024/CoRL/2024_CoRL_Learning-Visuotactile-Estimation-and-Control-for-Non-prehe/01_overview.md)

### 발표처별

기록 라벨 **57개**다. arXiv·Technical Report·Unverified도 기록값별 표에 포함했다. 게재 상태는 peer-reviewed 1,134편, preprint 88편, technical report 4편, 미확인 1편이다.

| 발표처 표기 | 편수 | 전체 비중 |
|---|---|---|
| CVPR | 175 | 14.3% |
| RSS | 149 | 12.1% |
| ICLR | 135 | 11.0% |
| ICML | 99 | 8.1% |
| ICCV | 96 | 7.8% |
| NeurIPS | 95 | 7.7% |
| CoRL | 93 | 7.6% |
| arXiv | 88 | 7.2% |
| ICRA | 70 | 5.7% |
| ECCV | 60 | 4.9% |
| RA-L | 32 | 2.6% |
| IROS | 22 | 1.8% |
| 3DV | 16 | 1.3% |
| AAAI | 13 | 1.1% |
| Science Robotics | 7 | 0.6% |
| IJRR | 6 | 0.5% |
| T-RO | 6 | 0.5% |
| WACV | 5 | 0.4% |
| Technical Report | 4 | 0.3% |
| Autonomous Robots | 3 | 0.2% |
| IEEE Robotics and Automation Letters | 3 | 0.2% |
| Machine Learning | 3 | 0.2% |
| SIGGRAPH | 3 | 0.2% |
| ACM Transactions on Graphics | 2 | 0.2% |
| Artificial Intelligence | 2 | 0.2% |
| EMNLP | 2 | 0.2% |
| IJCAI | 2 | 0.2% |
| ISMAR | 2 | 0.2% |
| Journal of Dynamic Systems, Measurement, and Control | 2 | 0.2% |
| Nature | 2 | 0.2% |
| NeurIPS Datasets and Benchmarks | 2 | 0.2% |
| Robotics: Science and Systems | 2 | 0.2% |
| TOG | 2 | 0.2% |
| ACL | 1 | 0.1% |
| AISTATS | 1 | 0.1% |
| Annual Review of Control, Robotics, and Autonomous Systems | 1 | 0.1% |
| CVPR-Workshop | 1 | 0.1% |
| Entropy | 1 | 0.1% |
| ICAPS | 1 | 0.1% |
| IEEE JRA | 1 | 0.1% |
| IEEE T-RA | 1 | 0.1% |
| IEEE Transactions on Pattern Analysis and Machine Intelligence | 1 | 0.1% |
| IEEE Transactions on Systems Science and Cybernetics | 1 | 0.1% |
| IJHR | 1 | 0.1% |
| Industrial Robot | 1 | 0.1% |
| JMLR | 1 | 0.1% |
| Journal of Basic Engineering | 1 | 0.1% |
| NAACL | 1 | 0.1% |
| Nature Machine Intelligence | 1 | 0.1% |
| Neural Computation | 1 | 0.1% |
| NeurIPS Workshop | 1 | 0.1% |
| Sensors | 1 | 0.1% |
| TAC | 1 | 0.1% |
| The International Journal of Robotics Research | 1 | 0.1% |
| TMLR | 1 | 0.1% |
| TOG / SIGGRAPH | 1 | 0.1% |
| Unverified | 1 | 0.1% |

동일 발표처로 볼 표기 쌍의 합계는 아래와 같다. 학회 본편·워크숍·별도 트랙은 표에 기록된 구분을 사용했다.

| 발표처 | 기록 표기 | 합계 |
|---|---|---|
| RSS | RSS 149 · Robotics: Science and Systems 2 | 151 |
| RA-L | RA-L 32 · IEEE Robotics and Automation Letters 3 | 35 |
| IJRR | IJRR 6 · The International Journal of Robotics Research 1 | 7 |
| TOG | TOG 2 · ACM Transactions on Graphics 2 | 4 |

## 2. 필드별 누락

누락은 빈 문자열·null·빈 목록을 뜻한다. 발표처는 미확인 상태도 별도로 집계했다. 선택적인 PDF·코드·프로젝트의 빈 값은 등록 오류 수로 사용하지 않는다.

| 필드 | 누락 편수 | 누락률 | 해석 |
|---|---|---|---|
| 식별 키·제목·연도·Tier·분류·태그 | 0 | 0.0% | 각 필드 0건 |
| 발표처 필드 | 0 | 0.0% | 빈 값 기준 |
| 발표처 미확인 | 1 | 0.1% | Unverified 1편 · DialogVLA [pr-0988](../2026/IROS/2026_IROS_DialogVLA-Bridging-Reasoning-Action-in-Bimanual-Manipulati/01_overview.md) |
| 논문 페이지·주 출처 URL | 0 | 0.0% | `page`와 `sources.primary.url` 각각 |
| 논문 단위 주 출처 | 43 | 3.5% | 학회 목록 43편. 프리프린트/PDF 등 대체 URL이 각 항목에 있음 |
| PDF URL | 356 | 29.0% | 선택 필드 · 로컬 PDF 캐시와 별도 |
| 프로젝트 URL | 636 | 51.8% | `sources.project.url` |
| 코드 URL | 970 | 79.1% | `sources.code.url` |
| 공개 식별자 | 366 | 29.8% | `identifiers`가 비어 있음 |
| arXiv ID | 649 | 52.9% | arXiv에 올리지 않은 논문과 미기록 상태를 함께 포함 |
| Primary track | 23 | 1.9% | REFERENCE 22편 · ARCHIVE 1편 |
| 요약 필드 | 1,227 | 100.0% | 전용 `summary` 필드 없음 |
| 구조화 문제·방법 | 821 | 66.9% | 두 항목을 모두 채운 논문 406편 |
| 발표 월·일 | 1,227 | 100.0% | `publication`에 연도 값만 존재 |

overview 1,227개에서 문제·핵심 아이디어·기여 중 하나 이상의 비어 있지 않은 요약 절을 1,227개 확인했다. 요약의 정확성이나 읽기 완료 여부는 검사 범위 밖이다.

학회 목록을 주 출처로 쓰는 43편은 ICRA 28편·3DV 15편이다. NEXT 4편, REFERENCE 23편, ARCHIVE 16편이다. FP3의 ICRA 연도별 수상 목록은 `paper_specific`으로 기록돼 있어 범위 라벨의 별도 재검토 사례다. 링크된 페이지의 원문은 열지 않았다. [pr-0184](../2026/ICRA/2026_ICRA_FP3-A-3D-Foundation-Policy-for-Robotic-Manipulation/01_overview.md)

## 3. 중복 의심

| 검사 | 발견 | 판정 |
|---|---|---|
| 정규화 제목 완전 일치 | 0 | NFKC·대소문자·구두점·공백 정규화 |
| 동일 arXiv ID | 0 | 식별자와 논문 URL에서 확인, arXiv 버전 접미사 제거 |
| 동일 DOI / OpenReview ID | 0 / 0 | 원장 식별자 기준 |
| 동일 논문 단위 주 출처 URL | 0 | 공유 학회 목록 URL은 제외 |
| 높은 제목 유사도 | 1 | GR00T N1.5 / N1.6, 문자 0.987·토큰 0.846. 출처 경로가 다르고 원장에 후속 관계가 기록됨 · [pr-0917](../2025/Technical-Report/2025_Technical-Report_GR00T-N1.5-An-Improved-Open-Foundation-Model-for-Generalis/01_overview.md) · [pr-0918](../2025/Technical-Report/2025_Technical-Report_GR00T-N1.6-An-Improved-Open-Foundation-Model-for-Generalis/01_overview.md) |
| 별도 arXiv 레코드 / 게재본 의심 | 0 | 완화 제목 조건과 포함 관계에서도 후보 0쌍. peer-reviewed 490편은 arXiv ID를 같은 레코드에 함께 저장 |

제목 752,151쌍을 검사했다. 높은 유사도는 문자 SequenceMatcher ≥0.90 또는 공통 단어 5개 이상이면서 단어 Jaccard ≥0.80으로 정의했다. arXiv 대 peer-reviewed 쌍은 임계값을 각각 0.86과 0.70으로 낮추고, 5단어 이상인 제목 전체가 상대 제목에 포함되면서 길이 비율이 0.65 이상인 경우도 확인했다. 제목을 크게 바꾼 버전은 저자·링크에 추가 근거가 없으면 탐지 범위에서 빠질 수 있다.

## 4. 태그 일관성

원장에 기록된 태그는 **896종**, 논문-태그 연결은 4,563건이다. 한 논문 안에서 같은 원문 태그를 반복한 행은 0개다. 표기 차이 63묶음에는 대소문자·공백·하이픈·밑줄만 정규화했다. `RRT`와 `RRT*`처럼 별표가 달라지는 명칭은 구별했다.

| 동의·형식 변형 예시 | 원문별 편수 | 합친 편수 |
|---|---|---|
| Reinforcement Learning | `Reinforcement Learning` 82 · `reinforcement-learning` 27 · `RL` 10 | 119 |
| Imitation Learning | `Imitation Learning` 63 · `imitation-learning` 8 | 71 |
| Vision-Language Model | `Vision-Language Model` 119 · `VLM` 17 | 136 |
| Vision-Language-Action | `VLA` 236 · `Vision-Language-Action` 6 | 242 |
| World Model | `world model` 38 · `world-model` 9 | 47 |
| Offline RL | `offline-RL` 11 · `offline reinforcement learning` 6 · `offline RL` 2 | 19 |
| Online RL | `online-RL` 7 · `online RL` 1 | 8 |
| Behavior Cloning | `behavior cloning` 1 · `behavior-cloning` 1 | 2 |
| Flow Matching | `Flow Matching` 7 · `flow-matching` 6 | 13 |
| Mobile Manipulation | `mobile manipulation` 16 · `mobile-manipulation` 8 | 24 |
| Vision-Language Navigation | `Vision-Language Navigation` 9 · `VLN` 1 · `vision-language-navigation` 1 | 11 |
| Robot Data | `robot data` 20 · `robot-data` 6 | 26 |

태그 묶음은 연결된 `paper_id`의 합집합으로 계산한다. 사용자가 제시한 `IL`, `모방학습`에 해당하는 단독 태그는 없었다. 아래 희소 태그는 원문별 빈도다.

| 사용 빈도 | 태그 수 | 전체 태그에서 비중 |
|---|---|---|
| 1 | 585 | 65.3% |
| 2 | 99 | 11.0% |
| 1–2회 합계 | 684 | 76.3% |
| 3회 이상 | 212 | 23.7% |

희소 태그를 하나 이상 가진 논문은 499편(40.7%), 모든 태그가 희소한 논문은 4편이다. 사용 빈도에는 세부 개념의 범위와 등록 시점도 영향을 준다.

<details><summary>1회 사용 태그 585개</summary>

`3D action` · `3D attention` · `3D correspondence` · `3D Gaussian` · `3D interaction` · `3D linear inverted pendulum` · `3D motion field` · `3D navigation` · `3D QA` · `3D reasoning`
`3D Registration` · `3D scene` · `3D scene flow` · `3D segmentation` · `3D semantic` · `3D spatial` · `3D spatial representation` · `3D Vision-Language` · `3D visual reasoning` · `3D-2D alignment`
`3d-gaussian-splatting` · `3D-grounding` · `3D-point-flow` · `3D-representation` · `3DGS` · `4D` · `A*` · `A3C` · `action chunk` · `action diffusion`
`action generation` · `Action Hierarchy` · `action manifold` · `action noise` · `action policy` · `action tokenization` · `action tokens` · `action-alignment` · `action-chunk` · `action-conditioned-dynamics`
`action-context` · `action-generation` · `action-history` · `action-representation` · `action-tokenization` · `activation-intervention` · `active exploration` · `adaptation` · `adaptive-computation` · `ADMM`
`advantage-estimation` · `advantage-weighting` · `adversarial learning` · `aerial manipulation` · `air flow` · `analytic grasp metric` · `apprenticeship learning` · `articulated object manipulation` · `articulation` · `asymptotic optimality`
`asynchronous` · `atomic skills` · `attention` · `audio-visual pretraining` · `augmented Lagrangian` · `autonomous-data` · `autoregressive-policy` · `base-placement` · `batch online RL` · `behavior cloning`
`behavior diversity` · `behavior-cloning` · `behavioral-probing` · `binary-contact` · `branched-rollout` · `cable manipulation` · `camera pose` · `camera space` · `Cassie` · `causal-attribution`
`causal-inference` · `chunked-critic` · `classical planning` · `closed-loop control` · `co-training` · `code generation` · `community data` · `compliance` · `compositional generalization` · `compositional-generalization`
`compositional-reasoning` · `compounding error` · `conditional flow matching` · `configuration space` · `conservative learning` · `conservative-learning` · `consistency distillation` · `consistency policy` · `contact invariant` · `contact maps`
`contact prediction` · `contact-phase` · `contact-rich` · `continuous normalizing flow` · `continuous-latent` · `contrast-sets` · `contrastive imitation` · `control limits` · `control-horizon` · `controllability`
`controllable generation` · `controlled-exploration` · `controller-gain` · `convex relaxation` · `correspondence` · `counterfactual-data` · `counting` · `covariate-shift` · `critic` · `cross-platform`
`cross-view generalization` · `curriculum learning` · `DAgger` · `damage-aware` · `data curation` · `data diversity` · `data generation` · `data scaling` · `data-generation` · `data-mixture`
`data-scaling` · `decision making` · `Deep Q-Network` · `deformable` · `deformable manipulation` · `Dense Descriptors` · `deployment` · `detection` · `diagnosis` · `diagnostic-benchmark`
`differentiable optimization` · `differentiable physics` · `differentiable-RL` · `direct registration` · `distillation` · `distractor` · `distributed-system` · `distributed-training` · `distribution shift` · `distributional-robustness`
`domain adaptation` · `domain randomization` · `drone-navigation` · `dynamic manipulation` · `dynamical systems` · `dynamics model` · `efficient attention` · `efficient deployment` · `efficient inference` · `embodied navigation`
`embodied reasoning` · `embodiment alignment` · `end-effector stabilization` · `energy-based model` · `environment-query` · `episodic-memory` · `event camera` · `exoskeleton` · `experience-retrieval` · `exposure-bias`
`expressive-policy` · `extrapolation` · `extrinsic manipulation` · `eye-in-hand` · `factor graph` · `failure diagnosis` · `failure prediction` · `failure prevention` · `failure-data` · `fall recovery`
`feasibility` · `few-shot` · `few-shot learning` · `few-shot-adaptation` · `fine-grained action` · `Fleet Learning` · `flight control` · `flow` · `Force` · `force sensing`
`force uncertainty` · `force-limit` · `force-torque` · `foresight` · `forgetting` · `formal guarantee` · `foundation controller` · `frozen-policy` · `Gaussian Process` · `gaussian-splatting`
`Generalist Agent` · `generalist reinforcement learning` · `generative modeling` · `geometric planning` · `geometry fusion` · `goal-conditioned learning` · `goal-conditioned RL` · `goal-conditioned-policy` · `goal-conditioned-RL` · `graph neural network`
`Grasp Planning` · `guidance` · `guided policy search` · `hardware-shift` · `heterogeneous data` · `heterogeneous-data` · `hierarchical control` · `hierarchical QP` · `hierarchical-control` · `high-frequency control`
`high-speed locomotion` · `hindsight-learning` · `hindsight-relabeling` · `history` · `holonomic-base` · `home rearrangement` · `household manipulation` · `household robotics` · `human demonstration` · `human intervention`
`human interventions` · `human-preference` · `human-robot interaction` · `human-to-humanoid` · `human-to-robot transfer` · `hybrid force-position control` · `hybrid-control` · `ICP` · `imagination-RL` · `Impedance Control`
`implicit Q-learning` · `implicit representation` · `in-context learning` · `in-hand manipulation` · `in-the-wild` · `incremental search` · `industrial robotics` · `inference-efficiency` · `information-constraint` · `insertion`
`instruction-coverage` · `instruction-grounding` · `interaction-frame` · `interactive simulator` · `interpretability` · `interruption` · `intervention` · `inverse-physics` · `Kalman Filter` · `keyframes`
`kinodynamic planning` · `language embedding` · `language instruction` · `language planning` · `language supervision` · `language-conditioned` · `language-conditioned control` · `language-conditioned-reward` · `language-relabeling` · `latent alignment`
`latent exploration` · `latent plans` · `latent representation` · `latent-dynamics` · `latent-motion` · `latent-noise` · `latent-reasoning` · `learning from human videos` · `learning from play` · `legged`
`legged robot` · `lifelong learning` · `local-navigation` · `locomotion planning` · `long-context` · `long-horizon prediction` · `low latency` · `low-level control` · `LQR` · `LVLM`
`Mamba` · `manipulation planning` · `manipulation policy` · `massively parallel simulation` · `matching` · `mechanistic-interpretability` · `meta-learning` · `metric scale` · `metric-geometry` · `mid-level representation`
`mixture-of-experts` · `mobile robot` · `momentum control` · `motion cones` · `motion primitives` · `motion retargeting` · `Motion Tracking` · `motion transfer` · `motor control` · `movement primitives`
`multi-agent-RL` · `multi-contact` · `multi-hypothesis` · `multi-rate control` · `Multi-Task Learning` · `multi-task manipulation` · `multimodal` · `Multimodal Learning` · `multimodal reasoning` · `multimodal representation`
`multimodal sensing` · `multimodal-feedback` · `multimodal-instructions` · `multimodal-learning` · `multitask-RL` · `noise-injection` · `non-curated data` · `non-prehensile` · `novel objects` · `object completion`
`object properties` · `object reconstruction` · `Off-Policy Learning` · `off-policy-RL` · `offline-evaluation` · `on-policy RL` · `on-policy-RL` · `one-shot learning` · `one-step generation` · `online RL`
`online-interaction` · `OOD-instructions` · `Open X-Embodiment` · `open-vocabulary perception` · `OpenVLA` · `operational space` · `operational space control` · `optical-flow` · `options` · `pairwise-evaluation`
`part discovery` · `part-level grounding` · `partial references` · `partial-observability` · `particle filter` · `partner-modeling` · `path planning` · `peg-in-hole` · `physical-reasoning` · `Physics Engine`
`physics-based control` · `physics-informed learning` · `pixel-to-action` · `plan verification` · `point-language` · `policy` · `policy factorization` · `policy fine-tuning` · `policy head` · `policy steering`
`policy transfer` · `policy-evaluation` · `policy-extraction` · `policy-finetuning` · `policy-improvement` · `policy-invariance` · `policy-likelihood` · `policy-mobilization` · `policy-search` · `policy-utility`
`pose tokens` · `pose uncertainty` · `post-deployment` · `potential-function` · `PPO` · `precision manipulation` · `precision-assembly` · `predictive geometry` · `predictive-learning` · `preference-learning`
`privileged value` · `privileged-training` · `PRM` · `process-reward` · `process-specification` · `program synthesis` · `progress estimation` · `progress-critic` · `progress-value` · `pushing`
`Q-filter` · `quadratic programming` · `quasi-dynamic model` · `reactive-control` · `reactivity` · `real-robot` · `real-robot-benchmark` · `real-robot-learning` · `real-time-control` · `real-world adaptation`
`real-world control` · `real-world learning` · `real-world reinforcement learning` · `reconstruction` · `recovery policy` · `recurrent policy` · `recurrent state` · `regularization` · `REINFORCE` · `representation alignment`
`representation probing` · `representation-learning` · `reproducibility` · `reset` · `reset-distribution` · `reset-free learning` · `residual dynamics` · `resource-allocation` · `retry` · `Reward Design`
`reward learning` · `reward model` · `reward-hacking` · `reward-modeling` · `RGB` · `rigid contact` · `risk-aware planning` · `RL-finetuning` · `robomimic` · `robot dataset`
`robot policy` · `robot self-improvement` · `robot state` · `robot-control` · `robot-manipulation` · `robot-RL` · `Robotarium` · `robust control` · `robust locomotion` · `robust perception`
`RRT` · `RRT*` · `runtime monitoring` · `safe control` · `safe deployment` · `safe locomotion` · `safety constraints` · `safety filter` · `Safety Gym` · `safety recovery`
`safety-critical control` · `scene` · `scene flow` · `score model` · `SE(3) equivariance` · `SE(3) pose` · `selective-regularization` · `self-reference` · `self-reflection` · `self-supervised learning`
`self-supervised-learning` · `semantic map` · `semantic mapping` · `semantic memory` · `semantic occupancy` · `semantic reasoning` · `semantic-calibration` · `semantic-grounding` · `semantic-preservation` · `semantic-steering`
`semi-MDP` · `sensor transfer` · `sequential contacts` · `shape` · `shape completion` · `shared control` · `simulator` · `situated planning` · `skill abstraction` · `skill chaining`
`skill composition` · `skill discovery` · `skill-chaining` · `skill-evaluation` · `slip detection` · `slow-fast control` · `social navigation` · `social-navigation` · `sparse footholds` · `sparse rewards`
`spatial-grounding` · `spatial-memory` · `spatial-representation` · `standing up` · `statistical guarantees` · `steerability` · `stochastic optimization` · `streaming-memory` · `structured exploration` · `successor-features`
`surface reconstruction` · `surgical robotics` · `symbolic planning` · `symmetry` · `tactile-RL` · `tactile/force` · `task generalization` · `task success` · `task-switching` · `teacher-student learning`
`temporal correlation` · `temporal-context` · `temporal-shortcuts` · `termination` · `terrain estimation` · `test-time computation` · `test-time reasoning` · `test-time-adaptation` · `test-time-compute` · `test-time-scaling`
`text-to-3D` · `theory` · `tolerance` · `topological-map` · `torque control` · `tracking` · `tracking control` · `trajectory following` · `trajectory prediction` · `trajectory representation`
`trajectory-generation` · `trajectory-reasoning` · `truncation-bias` · `unified-generation` · `value guidance` · `value-calibration` · `value-guidance` · `value-learning` · `variance-reduction` · `video action model`
`video diffusion` · `video model` · `video policy` · `video segmentation` · `video-memory` · `video-prediction` · `video-pretraining` · `vision-based manipulation` · `vision-language-navigation` · `visual attention`
`visual grounding` · `visual imitation` · `visual manipulation` · `visual navigation` · `Visual Pretraining` · `visual representation` · `visual-fidelity` · `visual-grounding` · `visual-inertial odometry` · `Visual-Language Grounding`
`visuo-haptic perception` · `visuomotor policy` · `visuotactile` · `VLA-RL` · `VLM verifier` · `VLN` · `VLN-CE` · `whole-body` · `whole-body autonomy` · `whole-body perception`
`whole-body teleoperation` · `whole-body-control` · `wrench-prediction` · `zero-shot policy` · `ZMP`

</details>

<details><summary>2회 사용 태그 99개</summary>

`3D point cloud` · `3D representation` · `4D reasoning` · `6-DoF grasp` · `aerial robotics` · `camera` · `collision avoidance` · `consistency` · `control-interface` · `cooperative-manipulation`
`counterfactual` · `credit-assignment` · `decentralized-control` · `deformable objects` · `demonstration generation` · `dense-reward` · `dexterous-manipulation` · `diffusion model` · `digital twin` · `distribution-shift`
`dynamics` · `embodiment` · `equivariance` · `execution` · `failure data` · `flow policy` · `force feedback` · `force-control` · `force-feedback` · `generalist-policy`
`goal-conditioned policy` · `GPU` · `graph search` · `GRPO` · `hidden-confounding` · `hierarchical policy` · `hindsight` · `home robotics` · `human demonstrations` · `human-in-the-loop`
`instruction tuning` · `instruction-switching` · `interaction` · `inverse kinematics` · `kinematics` · `KL-divergence` · `Large Language Model` · `latent action` · `latent dynamics` · `latent imagination`
`latent-action` · `legged locomotion` · `LIBERO` · `LiDAR-inertial odometry` · `maximum entropy` · `model-based planning` · `model-based-RL` · `monocular geometry` · `multimodal actions` · `next-best-view`
`object-centric` · `occlusion` · `offline learning` · `offline RL` · `optimal control` · `optimization` · `parkour` · `PDDL` · `perceptive locomotion` · `physics`
`policy evaluation` · `Policy Gradient` · `policy-gradient` · `real-to-sim` · `real-world` · `real-world evaluation` · `referring segmentation` · `registration` · `replanning` · `RLVR`
`Robot Learning` · `rough terrain` · `safe navigation` · `sampling` · `scaling` · `scaling laws` · `skill-composition` · `survey` · `TAMP` · `task hierarchy`
`task planning` · `temporal difference` · `tool use` · `value-selection` · `verification` · `Video Generation` · `Vision Transformer` · `visual sim-to-real` · `zero-shot transfer`

</details>

## 5. 링크 형식

HTTP(S) 스킴, 호스트·포트, 공백과 퍼센트 이스케이프를 검사했다. arXiv는 링크 경로와 식별자에서 ID의 월·숫자 길이·버전 형태를 검사했다. 서버 응답은 점검하지 않았다.

| 검사 | 건수 | 범위 |
|---|---|---|
| 비어 있지 않은 링크 필드 | 7,015 | `page`, `pdf`, `project`, `sources.*.url`의 반복 등장 포함 |
| 상태 문구가 든 레거시 `project` | 617 | URL이 아닌 문자열. 아래 표 참조 |
| HTTP(S) 후보 중 URL 형식 이상 | 0 | 상태 문구를 제외한 6,398개 링크 등장 |
| arXiv ID / URL ID 형식 이상 | 0 / 0 | 신형 YYMM.NNNN[N] 및 구형 archive/YYMMNNN |
| arXiv 항목과 논문 링크 ID 불일치 | 0 | 프로젝트·코드 URL은 논문 ID 대조에서 제외 |

| `project`의 상태 문구 | 편수 |
|---|---|
| not identified | 403 |
| not identified from OpenReview | 101 |
| not identified from primary page | 59 |
| not identified from venue audit | 29 |
| not released | 25 |

## 6. 하위 주제와 연도

관심 주제 표는 분류와 태그를 합쳐 계산했다. 한 논문이 여러 주제에 들어갈 수 있다. 주제별 기준은 표 아래에 적었다. 공식 분류 표의 각 행은 상호 배타적이다.

| 주제 | 전체 | ≤2022 | 2023 | 2024 | 2025 | 2026 | 2024–2026 비중 |
|---|---|---|---|---|---|---|---|
| VLA·범용 정책 | 319 | 7 | 8 | 20 | 104 | 180 | 95.3% |
| 휴머노이드 | 39 | 7 | 1 | 7 | 17 | 7 | 79.5% |
| 조작·파지 | 220 | 44 | 15 | 34 | 74 | 53 | 73.2% |
| 내비게이션·매핑 | 87 | 9 | 6 | 13 | 30 | 29 | 82.8% |
| 이동·전신 제어 | 83 | 21 | 5 | 18 | 28 | 11 | 68.7% |
| 3D 비전 | 406 | 66 | 12 | 69 | 175 | 84 | 80.8% |
| 로봇 학습·데이터 | 194 | 66 | 14 | 30 | 47 | 37 | 58.8% |

VLA·범용 정책은 319편 중 180편(56.4%)이 2026년이고, 휴머노이드는 39편 중 17편(43.6%)이 2025년이다. 조작·파지는 2025년 74편에서 2026년 53편, 이동·전신 제어는 28편에서 11편으로 기록됐다. 2026년은 11월 19일 기준이고 수치는 이 레지스트리의 수집 구성을 보여 준다.

태그 기준은 단어 경계로 적용했다. VLA는 VLA/vision language action 태그 또는 VLA·범용 정책 분류, 휴머노이드는 humanoid(s) 태그다. 조작은 manipulation/grasping 태그 또는 조작 분류, 내비게이션은 navigation 태그 또는 내비게이션 분류, 이동은 locomotion/whole body/mobile manipulation/loco manipulation 태그 또는 이동 분류다. 3D 비전은 3D 관련 분류명 접두어 또는 정확한 3D Vision 태그를 사용했다. 로봇 학습은 현행·기초 학습 분류의 합이다.

<details><summary>공식 분류 23개 전체</summary>

| 주제 | 전체 | ≤2022 | 2023 | 2024 | 2025 | 2026 | 2024–2026 비중 |
|---|---|---|---|---|---|---|---|
| VLA and Generalist Robot Policies | 279 | 5 | 7 | 20 | 98 | 149 | 95.7% |
| Robot Learning and Data | 153 | 28 | 12 | 30 | 46 | 37 | 73.9% |
| 3D Vision-Language Understanding | 104 | 5 | 2 | 26 | 48 | 23 | 93.3% |
| World Models, Safety, and Recovery | 71 | 10 | 1 | 3 | 23 | 34 | 84.5% |
| Manipulation, Contact, and Dexterity | 65 | 13 | 3 | 13 | 20 | 16 | 75.4% |
| Embodied Navigation and Mapping | 62 | 6 | 6 | 7 | 23 | 20 | 80.6% |
| Neural Scene Representations | 61 | 5 | 1 | 14 | 26 | 15 | 90.2% |
| Locomotion, Whole-Body, and Mobile Manipulation | 50 | 8 | 4 | 11 | 19 | 8 | 76.0% |
| 3D Generative Modeling | 45 | 0 | 1 | 11 | 27 | 6 | 97.8% |
| Benchmarks and Datasets | 45 | 17 | 2 | 6 | 8 | 12 | 57.8% |
| Language-Grounded 3D Scene Representations | 44 | 1 | 2 | 8 | 24 | 9 | 93.2% |
| Autonomous 3D Perception and Sensor Fusion | 41 | 10 | 6 | 3 | 16 | 6 | 61.0% |
| Robotics Foundations: Robot Learning | 41 | 38 | 2 | 0 | 1 | 0 | 2.4% |
| 3D Geometry, Reconstruction, and SLAM | 29 | 12 | 0 | 8 | 6 | 3 | 58.6% |
| Robotics Foundations: Planning and Control | 29 | 22 | 0 | 5 | 1 | 1 | 24.1% |
| 3D Geometry, Registration, and Equivariance | 23 | 7 | 0 | 2 | 8 | 6 | 69.6% |
| Robotics-Enabling 3D Perception | 22 | 9 | 1 | 1 | 6 | 5 | 54.5% |
| 3D Representation Learning | 19 | 11 | 1 | 0 | 6 | 1 | 36.8% |
| Foundations: Vision and Language Models | 18 | 12 | 4 | 1 | 1 | 0 | 11.1% |
| Planning and Long-Horizon Reasoning | 11 | 1 | 4 | 2 | 1 | 3 | 54.5% |
| Robotics Foundations: Contact and Whole-Body Control | 8 | 8 | 0 | 0 | 0 | 0 | 0.0% |
| Foundations: Generative Models | 6 | 5 | 1 | 0 | 0 | 0 | 0.0% |
| Multi-Robot Systems | 1 | 0 | 0 | 0 | 1 | 0 | 100.0% |

</details>

## 7. 최근 6개월

**2026-05-19~2026-11-19의 정식 발표 비중은 산출할 수 없다.** 원장의 연도 해상도는 1년이다. arXiv ID로 최초 등록월을 파악할 수 있는 578편만 별도 지표로 집계했다.

| 지표 | 편수 | 분모·비중 |
|---|---|---|
| 2026년 기록 전체 | 354 | 전체 1,227편 중 28.9% · peer-reviewed 300 · preprint 53 · 미확인 1 |
| arXiv 최초 등록월 파악 가능 | 578 | 전체 1,227편 중 47.1% |
| arXiv ID가 2026년 6–10월인 논문 | 60 | 전체 중 4.9% · 등록월 파악 가능 578편 중 10.4% |
| 같은 기간 중 arXiv 분류 레코드 | 40 | arXiv 분류 88편 중 45.5% |
| 월 단위 경계에 있는 논문 | 16 | 2026년 5월 14편·11월 2편. ID만으로 일자 판정 불가 |

| arXiv ID 등록월 | 모든 레코드 | 그중 arXiv 분류 |
|---|---|---|
| 2026-05 | 14 | 2 |
| 2026-06 | 15 | 4 |
| 2026-07 | 5 | 4 |
| 2026-08 | 8 | 4 |
| 2026-09 | 16 | 13 |
| 2026-10 | 16 | 15 |
| 2026-11 | 2 | 2 |

arXiv 등록월에는 정식 발표보다 앞선 사전 공개도 포함된다. 출처 확인일·레지스트리 등록일·발표 연도는 게재일로 사용하지 않았다.

## 집계 입력

| 입력 | SHA-256 |
|---|---|
| papers.json | `b3eb05c7ffeea5d2b8ce9a45c2ba4b3a2428b566832b845fea6ec3e19610d625` |
| READING_TIERS.csv | `de71d83149201f7366cf464386b02ddbfdda475cc81280d30d815fcc97b51516` |
| REGISTRY_INDEX.csv | `be8007f60bfb7e56fa2e33e9e16bc7d42188876684534f63b18c2efe67742ea0` |
