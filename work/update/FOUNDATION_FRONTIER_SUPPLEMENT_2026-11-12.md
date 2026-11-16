# 기반 원전과 최신 VLA·Robotics 문헌 보강

- Work ID: **REG-R15** / 2026-11-12 KST
- 범위: 2024–2026 최신 흐름과 그 기여를 판별하는 기반 원전·표준 비교 연구의 누락 보강. 전체 registry의 최신 게재·본문을 전수 검토한 것은 아니다.
- [등록 입력](../sources/foundation_frontier_admissions_2026-11-12.json) · [출처·보존·검증 원장](../sources/foundation_frontier_supplement_2026-11-12.json) · [읽기 계획](../../research/READING_PLAN.md) · [직전 REG-R14](./REGISTRY_MAINTENANCE_2026-11-12.md)

**24편·표준 노트120개 추가 → 총1,203편.** 2024–2026년12편과 그 이전 기반·핵심 비교12편을 추가했다. 신규 분류는 CORE3·NEXT16·REFERENCE5이며 공식 conference/journal18편과 게재 미확인 preprint6편을 구분했다. 숫자는 quota가 아니라 현재 연구 질문에 필요한 논문을 선별한 결과다.

## 기반 원전·표준 비교 논문

| 논문·ID | 확인한 게재/상태 | Tier·추가 이유 |
|---|---|---|
| [High-Dimensional Continuous Control Using Generalized Advantage Estimation — pr-1180](../../2016/ICLR/2016_ICLR_High-Dimensional-Continuous-Control-Using-Generalized-Adva/01_overview.md) | [ICLR 2016](https://www.iclr.cc/archive/www/2016.html) | **CORE** · PPO 기반 VLA RL에서 advantage·bootstrap·시간 단위가 학습에 미치는 영향을 해석하기 위한 공통 원전이므로 CORE다. |
| [Policy invariance under reward transformations: Theory and application to reward shaping — pr-1181](../../1999/ICML/1999_ICML_Policy-invariance-under-reward-transformations-Theory-and/01_overview.md) | [ICML 1999](https://people.eecs.berkeley.edu/~russell/publications) | **CORE** · VLM progress·단계 보상·접촉 보상으로 목표를 변경하는지 판단할 공통 이론 원전이므로 CORE다. |
| [Universal Value Function Approximators — pr-1182](../../2015/ICML/2015_ICML_Universal-Value-Function-Approximators/01_overview.md) | [ICML 2015](https://proceedings.mlr.press/v37/schaul15.html) | **CORE** · HER·HIQL·목표 조건부 critic과 단일 VLA의 지시별 가치 표현을 이해하는 원전이므로 CORE다. |
| [Successor Features for Transfer in Reinforcement Learning — pr-1183](../../2017/NeurIPS/2017_NeurIPS_Successor-Features-for-Transfer-in-Reinforcement-Learning/01_overview.md) | [NeurIPS 2017](https://proceedings.neurips.cc/paper/2017/hash/350db081a661525235354dd3e19b8c05-Abstract.html) | **NEXT** · 보상 전이와 로봇 동역학 전이를 혼동하지 않게 하는 명확한 이론·로봇 비교 기준이다. |
| [AWAC: Accelerating Online Reinforcement Learning with Offline Datasets — pr-1184](../../2020/arXiv/2020_arXiv_AWAC-Accelerating-Online-Reinforcement-Learning-with-Offli/01_overview.md) | [arXiv 2020](https://arxiv.org/abs/2006.09359) | **NEXT** · RL 이득이 성공 선택이나 weighted imitation으로 설명되는지 비교할 핵심 baseline이다. |
| [Relative Entropy Policy Search — pr-1185](../../2010/AAAI/2010_AAAI_Relative-Entropy-Policy-Search/01_overview.md) | [AAAI 2010](https://ojs.aaai.org/index.php/AAAI/article/view/7727) | **REFERENCE** · TRPO·MPO·KL 제약의 개념 계보를 보완할 원전이며 현재 공통 정독은 GAE/PPO를 우선한다. |
| [DART: Noise Injection for Robust Imitation Learning — pr-1186](../../2017/CoRL/2017_CoRL_DART-Noise-Injection-for-Robust-Imitation-Learning/01_overview.md) | [CoRL 2017](https://proceedings.mlr.press/v78/laskey17a.html) | **NEXT** · 복구 성공을 RL 고유 이득으로 해석하기 전 넘어야 할 강한 데이터 수집·모방 대안이다. |
| [Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning — pr-1187](../../1999/Artificial-Intelligence/1999_Artificial-Intelligence_Between-MDPs-and-semi-MDPs-A-framework-for-temporal-abstra/01_overview.md) | [Artificial Intelligence 1999](https://www.sciencedirect.com/science/article/pii/S0004370299000521) | **REFERENCE** · 가변 chunk·재계획·중단을 해석할 기본 formulation을 보완하며 계층형 주제로 전환하라는 의미는 아니다. |
| [Reinforcement learning in robotics: A survey — pr-1188](../../2013/IJRR/2013_IJRR_Reinforcement-learning-in-robotics-A-survey/01_overview.md) | [IJRR 2013](https://journals.sagepub.com/doi/abs/10.1177/0278364913495721) | **REFERENCE** · 로봇 문제의 제약에서 연구 질문을 세우기 위한 기반 survey로 최신 VLA 방법의 전제 점검에 필요하다. |
| [D4RL: Datasets for Deep Data-Driven Reinforcement Learning — pr-1189](../../2020/arXiv/2020_arXiv_D4RL-Datasets-for-Deep-Data-Driven-Reinforcement-Learning/01_overview.md) | [arXiv 2020](https://arxiv.org/abs/2004.07219) | **REFERENCE** · CQL·IQL·Cal-QL의 데이터 조건과 결과를 읽기 위한 표준 benchmark의 누락을 보완한다. |
| [Cal-QL: Calibrated Offline RL Pre-Training for Efficient Online Fine-Tuning — pr-1190](../../2023/NeurIPS/2023_NeurIPS_Cal-QL-Calibrated-Offline-RL-Pre-Training-for-Efficient-On/01_overview.md) | [NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/c44a04289beaf0a7d968a94066a1d696-Abstract-Conference.html) | **NEXT** · 초기 성능 손실을 semantic forgetting으로만 설명하지 않게 하는 critic calibration baseline이다. |
| [HIQL: Offline Goal-Conditioned RL with Latent States as Actions — pr-1191](../../2023/NeurIPS/2023_NeurIPS_HIQL-Offline-Goal-Conditioned-RL-with-Latent-States-as-Act/01_overview.md) | [NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/6d7c4a0727e089ed6cdd3151cbe8d8ba-Abstract-Conference.html) | **NEXT** · 공유 가치함수와 계층 정책을 단일 actor 공동 학습과 구별하고 장기 credit 문제의 강한 대안으로 비교한다. |

## 2024–2026 최신 연구

| 논문·ID | 확인한 게재/상태 | Tier·추가 이유 |
|---|---|---|
| [Is Value Learning Really the Main Bottleneck in Offline RL? — pr-1192](../../2024/NeurIPS/2024_NeurIPS_Is-Value-Learning-Really-the-Main-Bottleneck-in-Offline-RL/01_overview.md) | [NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/8ffb4e3118280a66b192b6f06e0e2596-Abstract-Conference.html) | **NEXT** · 단일 VLA critic 개선 후보가 actor 학습·coverage 효과를 놓치지 않도록 하는 핵심 원인 분석이다. |
| [Horizon Reduction Makes RL Scalable — pr-1193](../../2025/NeurIPS/2025_NeurIPS_Horizon-Reduction-Makes-RL-Scalable/01_overview.md) | [NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0c66099070429b9b49ad8bb19c740c22-Abstract-Conference.html) | **NEXT** · Chunk 길이·목표 분해와 데이터 scaling의 효과를 분리할 최신 기준 연구다. |
| [Deep Reinforcement Learning for Robotics: A Survey of Real-World Successes — pr-1194](../../2025/Annual-Review-of-Control/2025_Annual-Review-of-Control_Deep-Reinforcement-Learning-for-Robotics-A-Survey-of-Real/01_overview.md) | [Annual Review of Control, Robotics, and Autonomous Systems 2025](https://www.annualreviews.org/content/journals/10.1146/annurev-control-030323-022510) | **REFERENCE** · 석사 연구 후보의 구현 부담과 로봇 행동 기여를 평가할 최신 survey로 2013 원전과 함께 사용한다. |
| [Act2Goal: From World Model To General Goal-conditioned Policy — pr-1195](../../2026/RSS/2026_RSS_Act2Goal-From-World-Model-To-General-Goal-conditioned-Poli/01_overview.md) | [RSS 2026](https://www.roboticsproceedings.org/rss22/p015.html) | **NEXT** · Hindsight 목표 변경·world model·단일 정책 연결의 직접 선행이며 언어 VLA와 시각 목표 정책의 경계를 드러낸다. |
| [Causal World Modeling for Robot Control — pr-1196](../../2026/RSS/2026_RSS_Causal-World-Modeling-for-Robot-Control/01_overview.md) | [RSS 2026](https://www.roboticsproceedings.org/rss22/p016.html) | **NEXT** · Architecture 통합과 RL 공동 갱신을 구별할 world-action 비교 대상으로 보완한다. |
| [Tune to Learn: How Controller Gains Shape Robot Policy Learning — pr-1197](../../2026/RSS/2026_RSS_Tune-to-Learn-How-Controller-Gains-Shape-Robot-Policy-Lear/01_overview.md) | [RSS 2026](https://www.roboticsproceedings.org/rss22/p139.html) | **NEXT** · 접촉 VLA RL의 이득을 baseline gain 튜닝과 분리해야 함을 보이는 직접 선행이다. |
| [Offline Policy Evaluation for Manipulation Policies via Discounted Liveness Formulation — pr-1198](../../2026/RSS/2026_RSS_Offline-Policy-Evaluation-for-Manipulation-Policies-via-Di/01_overview.md) | [RSS 2026](https://www.roboticsproceedings.org/rss22/p154.html) | **NEXT** · 실험 rollout 종료와 실제 실패를 구별하고 가치 진단의 target을 정할 최신 기준이다. |
| [AC2-VLA: Action-Context-Aware Adaptive Computation in Vision-Language-Action Models for Efficient Robotic Manipulation — pr-1199](../../2026/IJCAI/2026_IJCAI_AC2-VLA-Action-Context-Aware-Adaptive-Computation-in-Visio/01_overview.md) | [IJCAI 2026](https://ijcai.org/proceedings/2026/228) | **NEXT** · RL 기반 시간 적응과 비교할 학습된 계산 절감 baseline이며 지연·feedback·성능의 비용 분리를 돕는다. |
| [WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning — pr-1200](../../2026/arXiv/2026_arXiv_WCM-A-World-Critic-Model-for-Vision-Language-Action-Reinfo/01_overview.md) | [arXiv 2026](https://arxiv.org/abs/2607.29613) | **NEXT** · 공유 표현·가치 공동 학습 후보의 직접 경쟁 선행이므로 단순 world-model 보조 loss를 신규 기여로 재제안하지 않게 한다. |
| [Reinforcement Learning for Real-Time Vision-Language-Action Policies — pr-1201](../../2026/arXiv/2026_arXiv_Reinforcement-Learning-for-Real-Time-Vision-Language-Actio/01_overview.md) | [arXiv 2026](https://arxiv.org/abs/2609.18207) | **NEXT** · 지연·feedback 공백의 직접 선행이자 단일 정책 선호와 별도로 보존할 강한 editor pipeline baseline이다. |
| [RoboAlign: Learning Test-Time Reasoning for Language-Action Alignment in Vision-Language-Action Models — pr-1202](../../2026/arXiv/2026_arXiv_RoboAlign-Learning-Test-Time-Reasoning-for-Language-Action/01_overview.md) | [arXiv 2026](https://arxiv.org/abs/2603.21341) | **NEXT** · VLM의 RL 정렬과 배포 VLA의 직접 RL 갱신을 구분할 선행으로 단일 정책 연구의 기여 경계를 보완한다. |
| [STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models — pr-1203](../../2025/arXiv/2025_arXiv_STARE-VLA-Progressive-Stage-Aware-Reinforcement-for-Fine-T/01_overview.md) | [arXiv 2025](https://arxiv.org/abs/2512.05107) | **NEXT** · 단계별 credit·보상 shaping 자체가 기존 방법임을 반영하고 원 보상 보존·추가 supervision을 비교하는 직접 선행이다. |

## 기반과 최신 연구의 연결

- **GAE·보상 shaping·UVFA를 CORE로 추가했다.** Advantage 추정, reward transformation의 가정, 목표 조건부 value는 최신 PPO/VLA·progress reward·hindsight 연구를 이해하는 공통 좌표계다. 최근 논문이거나 유명하다는 이유로 CORE에 넣지 않았다.
- **AWAC·Cal-QL·DART·Successor Features·HIQL은 NEXT**로 두어 offline→online 전환, 회복 시연, 전이 가정, 계층적 목표 정책을 비교한다. REPS·options·D4RL·두 survey는 필요한 branch에서 찾는 REFERENCE다. 계층적 논문을 추가한 것이 단일 VLA 내부 학습의 사용자 우선순위를 바꾼 것은 아니다.
- [RL 비교 질문](../../synthesis/02_rl_il_offline.md#foundation-frontier-2026)과 [VLA 학습/배포 구조](../../synthesis/04_vla_generalist.md#foundation-frontier-2026)에 기존 기반 → 새 선행의 연결을 정리했다. Controller gain과 recovery/truncation은 [접촉](../../synthesis/03_manipulation_contact.md)·[world model/evaluation](../../synthesis/05_world_models_safety.md)에 보강했다. 단순 성능 수치 집계나 정독 완료 comparison matrix로 만들지 않았다.

## 출처·중복·주장 경계

- 논문별 초록·공식 metadata와 명시한 저자 project/code를 확인했다. 모든 신규 노트는 **ABSTRACT_CHECKED**이며, 신규 집중 읽기19편은 **UNREAD**다. 원전 정리·CORE 승격과 실제 사용자 정독을 구분한다. 정확한 loss·theorem 조건·trial count·metric·실패 원인은 본문 확인 항목으로 남겼다.
- **AWAC·D4RL·WCM·Real-Time EXPO-FT·RoboAlign·STARE-VLA는 arXiv**로 등록했다. AWAC·RoboAlign·STARE-VLA의 학회 주장 또는 검색 색인을 공식 acceptance로 승격하지 않았다. Official forum의 접근 실패도 게재 증거로 쓰지 않았다.
- GAE는 ICLR2016 공식 accepted list로 확인하고 최초2015 preprint와 최신v6를 별도 등록하지 않았다. 보상 shaping은 저자 원전·publication list에서 ICML1999를 확인했으며 확인하지 못한 DOI는 채우지 않았다. Kober survey의 publisher 직접 접근은 timeout이었고 publisher 검색 결과·저자 서지로 보완했다.
- Annual Review survey는 volume의 **2025**를 사용한다. Online-first2024와 AAAI2025의 같은 제목 요약을 별도 논문으로 추가하지 않았다. Tune to Learn의 공식 제목은 *Shape*이며 저자 페이지의 *Affect* 및 workshop award를 별도 논문·RSS award로 바꾸지 않았다.
- **Causal World Modeling의 RSS CauVA와 동일 제목 arXiv LingBot-VA 연결은 미확인**이다. 이름·저자·방법 차이를 남기고 arXiv ID/code를 RSS entry에 복사하지 않았다. Liveness OPE의 RSS 초록과 arXiv 추가 실험도 구분했다. 상세 URL과 버전 경계는 원장과 각 overview에 보존했다.
- 기존 GR00T N1.6·MobileVLA-R1·ReSteer·TMRL·Robometer·Contact-Anchored Policies·Action Chunking RL·LDA-1B·OGBench 등의 identity를 대조해 중복 등록하지 않았다. 이 검색은 모든 분야의 의미상 중복 부재를 증명하지 않는다.

## 현행 snapshot·검증

전체1,203편·노트6,015개, **CORE50 / NEXT402 / REFERENCE509 / ARCHIVE242**, active452 / history47이다. Source evidence는 FULL_TEXT_CHECKED967 / ABSTRACT_CHECKED236이다. 기존 실제 READ5편의 기록을 유지한다.

<!-- VALIDATION:START -->
등록 dry-run/apply, tier 생성기 compile/rebuild, priority-only reconcile, benchmark/metric catalog·resource/index/stats 재생성을 완료했다. 최종 reconcile의 추가 변경은0건이다. 읽기 이력 회귀 검사 **6개 통과**, working/staged `git diff --check` 통과, 전체 audit **오류0 / 경고0**이다. Markdown6,241개·내부 링크13,440개·registry1,203행·표준 노트6,015개를 검사했다. 신규 노트96개의 근거 헤더 형식 불일치를 수정한 뒤 재검사를 통과했으며 근거 등급은 바뀌지 않았다.

기존 paper metadata1,179편·표준 노트5,895개·tier1,179건·사용자 읽기 입력480건을 보존했다. 신규 집중 읽기19건만 UNREAD로 추가했다. 주제별 재현 자료·과거 실험236개 및 기존 staged patch가 byte-identical이다. 기존 파일 삭제0개, 새 repository 파일123개(노트120·등록 입력·원장·이 보고서)이며 이번 작업의 임시 파일은 제거했다. Resource655개·curated relation50개이며 benchmark/metric 연결은 계속 cue_only다.
<!-- VALIDATION:END -->

## 연구 작업에 미치는 영향

현재 다음 행동은 [TODO](../../TODO.md)의 LANGRET-P0다. WCM·RoboAlign/STARE-VLA·Tune to Learn·Act2Goal은 관련 후보의 **P1 비교/신규성 주장 전 본문 대조**에 추가한다. 초록 등록만으로 기존 후보를 채택·종료하거나 과거 NO-GO/HOLD를 해제하지 않는다. 실제 정책 효과·외부 연구자 피드백·독립 기여는 여전히 미검증이다.

이번 작업은 문헌과 registry 유지보수다. 실험·Docker 실행·host dependency 설치·PDF/weights 다운로드·git commit/push는 수행하지 않았다.
