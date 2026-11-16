# GAP-DE1 — 변형체의 물성·고정 조건 식별과 작업에 필요한 탐색

- 검토일: 2026-10-24 KST. 작업 완료: **DONE**. 연구 판단: **일반 방법 NO-GO / 조건부 진단 REVISE·HOLD / native VLA HOLD**.
- Canonical 질문: [GAP-DEFORM](../../synthesis/03_manipulation_contact.md#gap-deform-2026). [Source/code ledger](../sources/deformable_identification_review_2026-10-24.json). 절차: [buildup guide](../../research/IDEA_BUILDUP_GUIDE.md)의 공백 → 직접 충돌 → 경쟁 설명 → 최소 비교 → 기각 조건.
- 2024–2026 관련 논문 11편과 이전 기반 2편의 **지정 본문 구간**, 공개 code 6개 revision·21개 파일(README 6, source/config/doc 15)을 대조했다. 전편 정독·전 venue 전수 조사·실행 검증을 뜻하지 않는다. Registry의 PGND(pr-0890)를 출발점으로 외부 문헌까지 확인했다.
- 신규 등록·tier/reading status 변경 없음. 실험·설치·PDF/데이터/checkpoint 다운로드 없음. 작은 HTML/source 임시 사본은 URL·revision·hash 기록 뒤 삭제한다.

## 1. 결론과 연구 가치

**“물성을 추정하고, 불확실성이 큰 곳을 탐색하고, 작업에 유용한 정보만 얻는다”는 조합만으로 새 연구를 시작할 근거는 부족하다.** 경계 조건의 능동 추정은 IJRR 2014, 작업 목적을 직접 반영한 탐색은 RSS 2020에 이미 있다. AdaptiGraph는 다중 물성과 uncertainty-driven probing까지 비교했다. 단순히 VLA를 앞단에 붙여도 이 충돌은 해소되지 않는다. [경계 식별](https://pmc.ncbi.nlm.nih.gov/articles/PMC4324691/), [task-oriented exploration](https://roboticsproceedings.org/rss16/p085.html), [AdaptiGraph Appendix C](https://arxiv.org/html/2407.07889v1#A3).

남겨 둘 것은 **“어떤 물성·고정 조건의 모호성이 실제 작업 행동을 바꾸며, 언제 추가 탐색이 단순 feedback보다 가치 있는가?”라는 조건 예측**이다. 다만 task-relevance라는 원리 자체도 선행이므로, material–attachment 조합을 바꾼 미관측 조건에서 새로운 예측·실패 경계를 제시해야 한다. 아래는 그 가능성을 검토할 질문이며, 미해결임이 입증된 분야 공백이나 채택된 방법은 아니다.

| 판단 대상 | 현재 판단 | 이유 |
|---|---|---|
| 일반 물성 적응·joint parameter estimation | NO-GO | 재질·마찰 동시 추정과 test-time adaptation 선행이 존재 |
| uncertainty/task-driven probe의 일반 제안 | NO-GO | 두 탐색 계열과 단순 변위 heuristic 비교가 이미 존재 |
| 숨은 attachment와 material의 혼동이 만드는 task별 행동 차이 진단 | REVISE/HOLD | 문제는 타당하지만 matched 관측·실행 가능 행동·공정 baseline을 잇는 사례 미확보 |
| 언어 지시에 따른 probe 투자 선택을 하는 VLA | HOLD | instruction이 물리적 목표/제약을 바꾸는 평가와 고정 정책의 기본 능력 미검증 |
| 바로 큰 학습 또는 GPU sweep | 진행하지 않음 | 현재 미결점은 자원량보다 비교 대상·관측 조건·작업 증거 |

## 2. 직접 문헌 비교와 확인 깊이

아래의 각 행은 논문이 지지하는 사실과 적용 한계를 함께 적는다. 공식 proceedings/publisher로 확인한 최근 논문은 8편, 공식 IROS 발표 program 확인 1편, 독립 acceptance 확인을 못 한 최신 자료 2편이다. 제목·version·세부 source anchor는 ledger에 보존했다. 문헌의 연결은 **비교상 관계**이며 모두 JIGGLE/PGND를 인용한 직접 후속이라고 주장하지 않는다.

| 자료·공식 status | 이번에 확인한 구간 | 이미 해결하거나 보여 준 부분 | 이번 질문에 바로 사용할 수 없는 부분 |
|---|---|---|---|
| [Boundary Constraints, IJRR 2014](https://journals.sagepub.com/doi/10.1177/0278364914536939) | [저자 본문](https://pmc.ncbi.nlm.nih.gov/articles/PMC4324691/) §2·4·9 | 변형 관측으로 고정된 경계 추정, entropy를 줄이는 grasp/action 선택 | 고정 attachment·근사 FEM 가정. 중력 등 모델 오차를 가짜 고정점으로 설명할 수 있음 |
| [Task-Oriented Exploration, RSS 2020](https://roboticsproceedings.org/rss16/p085.html) | [v1](https://arxiv.org/html/2006.01952v1) abstract·§III-A | 파라미터 복원 정확도보다 후속 task를 위한 탐색 최적화 | 식별 가능한 모델군·알려진 구조/초기 상태 가정. 숨은 attachment의 새 조건 예측과는 구별 |
| [JIGGLE, RSS 2024](https://roboticsproceedings.org/rss20/p007.html) | [v1](https://arxiv.org/html/2405.09743v1) §III·IV-C/D/E·V-C/E/F·VI 지정 구간 | XPBD/EKF로 attachment stiffness 추정·능동 sensing·topology change | §IV-C joint는 **boundary와 state**. 물성과 boundary의 동시 식별을 완료했다는 뜻이 아님. 전체 능동 loop는 sim, 실제 조직은 estimation 평가 |
| [AdaptiGraph, RSS 2024](https://roboticsproceedings.org/rss20/p010.html) | [v1](https://arxiv.org/html/2407.07889v1) §III-C/D·IV-D/E·Appendix C | material-conditioned dynamics·online inverse fitting·MPC. 부록에 stiffness+friction 동시 추정 및 uncertainty probe | 숨은 고정 topology와 마찰 계수는 같은 미지수가 아님. 5개 rope 비교에서 uncertainty 방식의 사후 variance 우위가 일관되지 않음 |
| [PGND, RSS 2025](https://roboticsproceedings.org/rss21/p036.html), registry pr-0890 | [v1](https://arxiv.org/html/2506.15680v1) §IV-F·V | geometry/짧은 motion history를 사용하는 particle-grid dynamics·MPC; 4개 task 각 10회 | 물성은 암묵적이며 해석 가능한 test-time 식별/적응은 후속 방향. 고정 particle 수·perception/tracking 의존 |
| [PhysTwin, ICCV 2025](https://openaccess.thecvf.com/content/ICCV2025/html/Jiang_PhysTwin_Physics-Informed_Reconstruction_and_Simulation_of_Deformable_Objects_from_Videos_ICCV_2025_paper.html) | [v1](https://arxiv.org/html/2503.17973v1) §4.3·5.3 지정 구간·Appendix D | sparse multi-view RGB-D에서 물리 digital twin, 새로운 상호작용/계획 | 단일 interaction modality 한계. 서로 다른 material/attachment 설명의 유일한 식별을 입증한 것은 아님 |
| [DPSI, IJRR 2025](https://journals.sagepub.com/doi/full/10.1177/02783649251334661) | [v2](https://arxiv.org/html/2411.00554v2) §3.3–3.5·결과의 초기화/국소해 논의·§5.1 | E·ν·yield·density와 table/manipulator friction 식별; 접촉을 늘린 motion 비교 | 알려진 constitutive family, 초기 형상 추정, 초기화/손실 의존. Poke와 poke-shift는 동일 시간 비교가 아님 |
| [INR-DOM, RSS 2025](https://roboticsproceedings.org/rss21/p035.html) | [v1](https://arxiv.org/html/2505.00500v1) §III-A·VII | partial point cloud/proprio를 implicit shape state와 정책에 연결 | 가림에 강한 표현은 material/attachment를 구별해야 하는 task 증거와 별개 |
| [Task-Level ILC, RSS 2026](https://roboticsproceedings.org/rss22/p126.html) | [v1](https://arxiv.org/html/2602.21302v1) §IV·V-D/G/H·VI 지정 구간 | 근사 rope 모델과 task critical-point 오차로 반복 보정, 여러 rope로 전이 | mocap·시연·critical event 표시·반복/reset 비용. 성공 명령 학습 후 40회 평가는 모든 학습 trial의 100% 성공이 아님 |
| [SV-DRO, RSS 2026](https://roboticsproceedings.org/rss22/p061.html) | [v1](https://arxiv.org/html/2605.19029v1) §III-A·IV-A·VI | task-sensitive uncertainty와 robust control. 정밀 식별 없이 성공하는 강한 대안 | 정해진 불확실성 모델군 밖의 접촉 물리까지 보장하지 않음. 이번 지정 구간 외 심화는 기존 GAP-W2 참조 |
| [Make a Donut, IROS 2025 발표](https://ras.papercept.net/conferences/conferences/IROS25/program/IROS25_ContentListWeb_3.html) | [v2](https://arxiv.org/html/2311.02787v2) §III-A·IV-D·V | GPT-4 tool/subgoal 생성과 differentiable physics의 계층 계획 | LLM planner와 native VLA는 구별. v2 실제 로봇 결과는 정성적. RA-L 2025는 [저자 표기](https://qq456cvb.github.io/projects/donut), 이번 publisher DOI 독립 확인 실패 |
| [PhysCoRe, 2026 preprint](https://arxiv.org/html/2607.20653v1) | §4.2·5.1·5.4–5.5·7 및 boundary 설명 | material/confidence field와 physics residual, 실제 probing에서 confidence 지도 | [project](https://lunarlab-gatech.github.io/PhysCoRe-website/)의 CoRL 2026 표기는 저자 주장; 공식 acceptance 미확인. 지정 구간에서 동일 비용 closed-loop task utility 비교는 확인하지 못함 |
| [FORM, 2026 preprint](https://arxiv.org/html/2609.38105v1) | §III·III-D·IV·V 지정 구간 | constitutive law의 weak-form 식별과 새 geometry/motion에 적용 | 알려진 law family·조건별 다른 관측 channel. 일부 positions-only에서는 탄성값을 고정하고 rollout scan. 실행 중 관측으로 재계획하는 closed loop는 아님 |

JIGGLE와 같은 제목의 OpenReview PDF 검색 결과를 별도 CoRL 논문으로 세지 않았다. Task-Level ILC의 저자 project/code에는 “Learning Dynamic Rope Manipulation…”이라는 제목도 쓰이지만 같은 arXiv identity로 연결한다. Make a Donut의 최초 preprint는 2023년이며, 이를 2025년에 처음 나온 방법으로 설명하지 않는다.

## 3. 처음 가정에서 고쳐야 할 부분

**추정 대상을 분리한다.** 물성(stiffness/yield 등), 마찰, attachment 위치·강도, 현재 형상/속도, constitutive model class는 서로 다르다. “joint estimation이 없다”는 주장은 AdaptiGraph·DPSI에 의해 반박된다. 반대로 마찰을 함께 맞춘 결과를 숨은 attachment topology 식별로 확대하면 안 된다. JIGGLE의 heterogeneous tissue 한계는 후보의 출발점이지만 후속 연구의 부재를 증명하지 않는다.

**추정 성능이 곧 행동 가치가 아니다.** 동일한 관측을 설명하는 물리 모델이 여러 개여도 모든 모델에 통하는 feedback 행동이 있으면 추가 식별은 불필요할 수 있다. Task-oriented exploration·SV-DRO·ILC를 빼고 parameter error만 개선하면 이 질문을 답하지 못한다. 특히 AdaptiGraph의 부록은 더 복잡한 uncertainty 목표가 단순한 변위 최대화보다 항상 낫다는 가정을 지지하지 않는다. 이 비교는 사후 분산/계산 비용에 대한 결과이며 모든 task 성공률의 동등성을 뜻하지 않는다.

**실제 실험 범위와 비용을 맞춘다.** JIGGLE의 real estimation과 sim active loop를 합쳐 real closed-loop 성공으로 쓰지 않는다. DPSI의 복잡한 probe는 시간도 달라진다. ILC에서는 시연·실패 시도·reset·mocap 비용을 포함해야 한다. FORM의 작은 linear solve 시간은 관측·probe·계획을 합친 end-to-end 지연이 아니다. 서로 다른 논문의 숫자를 이 비용 차이를 무시하고 순위로 만들지 않았다.

## 4. 공개 code/interface 정적 대조

각 revision은 **이번에 본 공개 상태**이며 논문 실험에 실제 사용한 commit이라는 확인은 없다. 다운로드한 source를 실행하거나 import하지 않았다. File hash·지정 line range는 ledger에 있다.

| 저장소·고정 revision | 확인 경로·근거 | 비교 설계에 주는 제약 |
|---|---|---|
| [AdaptiGraph `a7c7535`](https://github.com/Boey-li/AdaptiGraph/tree/a7c75357793422e9108c36f58c6928f3f8a123ad) | `physics_param_optimizer.py:34–64`는 interaction의 act/state_init/state_pred/state_real를 모아 fitting; `plan.py`는 goal cost와 online update | 상태 관측·기존 interaction 이력·optimization 비용을 baseline끼리 맞춰야 함 |
| [PGND `06ef5db`](https://github.com/kywind/pgnd/tree/06ef5dbbe9612b56aaee317c938dcf953074c05f) | `real_world/plan.py` → `planning_env.py:172–181`의 SegmentPerception → `segment_perception.py:41–60` GroundingDINO text 입력. 목표는 target point cloud 경로 | `text_prompts`는 segmentation cue. 이를 task instruction을 이해하는 VLA의 증거로 사용하지 않음. capture FPS도 control Hz가 아님 |
| [PhysCoRe `ba7ddf7`](https://github.com/lunarlab-gatech/PhysCoRe/tree/ba7ddf744c7468369529d3baf996fb829fec30dd) | boundary setter가 제공된 cuboid/collider/velocity를 적용; MfM의 material/confidence 출력; dataset의 particle flow·material 필드 resolver | 설정된 boundary를 적용하는 코드와 숨은 boundary를 추론하는 코드는 다름. Dataset 필드 존재만으로 real deployment 입력/누출을 단정하지 않음 |
| [FORM `e75611e`](https://github.com/form-robots/FORM/tree/e75611e8b752c372c2c7e842625a3dcb5c164cff) | `identify_no_stress.py:399–445` positions_only+plasticine/sand branch에서 truth E/ν를 assumed_parameters로 명시; reproduction 문서의 fixed contact/motion clock | 해당 tier의 나머지 물성만 식별하는 비교와 완전 blind 식별을 구분. README는 dataset 공개 hosting이 아직 없다고 명시 |
| [Task-Level ILC `f336b32`](https://github.com/krish-suresh/flying_knots_public/tree/f336b325caa297d1f515012f1a778f0f975999c2) | real config·learning loop, `learning.py:307–324` frame drop/parse failure 시 실제 trial 반복 | 새 비교에서는 실패한 재시도도 시간/interaction 예산에 기록. 이 코드만으로 논문의 비용 누락을 단정하지 않음. xArm7/Vicon 자산 필요 |
| [DPSI `d4f01a5`](https://github.com/IanYangChina/SI4RP-data/tree/d4f01a503aa6700c1fe6222f81c10ecf1ca4c013) | optimise의 motion level·parameter 초기화, env의 mesh/table/cube boundary | material+friction 비교 자산 후보지만 숨은 attachment를 독립 변화시키는 완성 task packet은 확인하지 못함 |

AdaptiGraph의 선택적 마지막 fitting branch에는 정적 불일치가 있다. [`random_interact.py:278`](https://github.com/Boey-li/AdaptiGraph/blob/a7c75357793422e9108c36f58c6928f3f8a123ad/src/planning/random_interact.py#L278)의 `iteration=-1`은 [`optimize(..., iterations=50)`](https://github.com/Boey-li/AdaptiGraph/blob/a7c75357793422e9108c36f58c6928f3f8a123ad/src/planning/physics_param_optimizer.py#L34)와 인자명이 다르고 함수는 양수 iterations를 요구한다. 정상 online call과 이 선택적 branch를 구분한다. 실행 실패를 재현한 것은 아니며 외부 code를 수정하지 않았다.

JIGGLE는 이번 제한된 검색에서 저자 공식 구현을 식별하지 못했다. 이는 코드가 없다는 확정이 아니며 문헌상 능동 boundary 추정의 존재를 약화하지 않는다. 다른 저장소의 source·데이터 링크가 존재하는 사실도 통합 실행 가능성의 증거는 아니다.

## 5. 남은 질문과 경쟁 설명

**연구자 가설:** 같은 짧은 관측 이력에 부합하는 material–attachment 조합에서, **목표/제약에 따른 허용 행동의 불일치**가 단순 parameter uncertainty보다 추가 probe의 순이득을 잘 예측하는가? 특히 재질과 attachment의 새로운 조합에서도 fixed/max-displacement probe, history feedback, task-oriented exploration 및 robust control 이후에 그 예측이 남는가?

“행동에 필요한 정보”라는 개념은 신규 contribution이 아니다. 새로 남을 수 있는 지식은 특정 deformable task에서 **탐색을 생략해도 되는 조건과 꼭 투자해야 하는 조건의 검증된 구분**이다. 다음 세 경우를 함께 포함해야 한다.

| 경우 | 기대되는 판단 — 아직 실험 결과 아님 | 반대 설명 |
|---|---|---|
| 물성 설명은 다르지만 공통의 안전한 성공 행동이 있음 | probe를 생략하는 쪽이 비용상 유리 | 매번 식별하는 방법의 불필요한 비용 |
| 현재 관측은 비슷하지만 목표별 feasible 행동이 갈리고 제한된 probe로 구별 가능 | task와 결합된 추가 관측의 이득 가능 | 충분한 history·느린 feedback·고정 probe만으로 이미 해결될 수 있음 |
| 현재 모델군 밖의 접촉/소성/미끄럼 등이 발생 | 높은 confidence도 정답을 보장하지 않음 | parameter 식별 문제가 아니라 model-class 오류일 수 있음 |

단지 외관이 같은 물체 두 개를 준비하는 것으로 두 번째 경우가 성립하지 않는다. **정책이 실제로 보는 history/proprio/force까지 맞춘 관측**, 허용한 controller의 공통 성공 행동, probe 이후의 물리 상태 변화와 정보 효과를 구별해야 한다. 현재 이 세 경우의 실제 matched 사례는 확보하지 못했다.

## 6. 최소 비교 계약 초안 — 실행 manifest가 아님

| 항목 | 먼저 고정할 내용 |
|---|---|
| Task 후보 | 의료 환경을 제외한 elastic sheet/band의 목표 형상·위치 도달. 같은 초기 형상에서 material와 가려진 anchor 위치/강도를 독립 변화. 구체 물체/fixture·값·관측 tolerance는 미정 |
| Task pair | 같은 object/history에서 서로 다른 목표 위치 또는 허용 force 제약을 제공. 자연어 paraphrase만 바꾸지 않고 실제 feasible action이 바뀌는지 확인. 아직 실증 사례 아님 |
| 입력 | timestamped RGB-D/point cloud·proprio와 선택한 force channel. Ground-truth 물성/anchor는 evaluator와 oracle baseline만 사용. Visibility·noise·history 길이는 모든 비교에 동일 |
| 행동·시점 | 같은 grasp/controller·probe/action 후보·목표 도달 action set. Probe도 물체 상태를 바꾸므로 sensing-only 무료 단계로 두지 않음. 정해진 관측 prefix 뒤 선택·추정·control 시점을 기록 |
| Baseline | no-extra-probe+history feedback, fixed probe, 최대 변위 probe, parameter-uncertainty probe, 기존 task-oriented exploration, robust MPC. 반복 가능한 task에는 ILC 추가; 시연/reset 비용 포함 |
| 비용 | force 상한·누적 변위·물리 시간·interaction/reset 수·계산 지연을 각각 기록. 공통 hard cap 아래 비용–성공 곡선을 비교. 알고리즘 iteration 수를 초로 치환하지 않음 |
| Metric | 전체 시도 기준 task success/constraint violation·peak force·시간. Held-out action prediction과 parameter error는 보조. Probe가 목표를 직접 진행시킨 효과와 정보에 의한 후속 선택 효과를 분리 |
| Split | 동일 물체의 frame을 나누지 않음. Material·attachment·목표의 조합 holdout과 모델군 밖 조건을 구별. Threshold/예산은 dev에서 정하고 test 전에 고정 |
| Ablation | material-only/boundary-only/joint/oracle, 충분한 history/force 유무, task 목표·constraint 변경, 같은 probe 뒤 추정 정보 사용/비사용 비교 |
| 기각/수정 | 공통 feedback 행동으로 해결되거나 fixed probe/ILC가 비용까지 설명하면 추가 식별 주장을 기각. 관측상 동등하지 않으면 ambiguity 주장을 수정. Oracle에서도 task 실패면 정책/제어 전제부터 수정 |

현재 estimator·수치 budget·checkpoint·seed·fixture·평가기·sample size가 미정이므로 **executable=false**다. 효과를 미리 증명하라는 요구가 아니라, 효과가 없을 때도 해석 가능한 비교를 만들기 위한 준비 조건이다.

## 7. VLA로 연결할 수 있는 범위

PGND의 segmentation text, Make a Donut의 LLM tool planner, PhysCoRe의 confidence 시각화는 각각 유용하지만 고정 VLA가 task-conditioned probe를 선택한 실험과 다르다. VLA를 채택하려면 먼저 동일 policy/controller에서 **지시가 바뀌어 목표·제약·필요 정보가 달라지는 task pair**와 oracle 정보 하의 기본 수행 능력을 확보해야 한다.

VLA의 출력은 probe/작업 option 또는 native action 중 무엇인지 정하고, option selector 실험을 native action policy 향상으로 확대하지 않는다. 두 로봇으로 확장한다면 force calibration·grasp·action unit·control rate까지 맞춰야 한다. 현재 연구 가치의 전제는 multi-robot transfer나 RL 학습이 아니다. 검토 논문과 정적 code만으로 VLA 효과·외부 연구자 피드백을 확인했다고 주장하지 않는다.

## 8. 다음 TODO와 종료 조건

**GAP-DE2 — 한 번의 비실험 자료 충분성 심사**를 다음으로 둔다. AdaptiGraph의 material/interaction 자산과 JIGGLE의 boundary formulation을 우선 비교하되, 별도 세계의 결과를 합쳐 하나의 paired dataset으로 간주하지 않는다. PGND/DPSI는 관측·task/evaluator 연결의 대안이다.

완료 기준은 (1) material와 attachment를 독립 설정하는 source/config, (2) 행동 전 관측·행동·시각·결과의 identity 연결, (3) 다른 목표/제약의 실제 action 차이를 평가할 방법, (4) 충분한 history feedback와 fixed probe를 포함한 비교 가능성, (5) 공개 자산으로 가능한 부분과 새 수집이 필요한 부분을 각 하나의 표로 확정하는 것이다. 사례의 성공 효과를 미리 요구하지 않는다. Runtime·rollout·학습은 이 작업에 포함하지 않는다.

이 제한된 심사에서도 비교 가능한 자산/차별적 예측이 남지 않으면 **현재 공개 자산 설계를 종료하고 문헌 진단만 보존**한다. 같은 metadata 검색을 반복하거나 자동으로 DE3/큰 학습을 만들지 않는다. GPU 확보만으로 이 gate를 넘지 못한다. 추후 실제 fixture·동기화된 관측·새 직접 비교 근거가 생기면 재심사한다.

## 9. 검증과 보존

문서·source ledger의 유지보수 검증은 ledger의 `validation`에 기록한다. Registry 1,037편·tier·읽기 입력을 보존하고 기존 GAP-P3/P4 실험과 관련 없는 dirty 변경을 수정하지 않는다. 이번 작업은 Git commit/push를 포함하지 않는다.
