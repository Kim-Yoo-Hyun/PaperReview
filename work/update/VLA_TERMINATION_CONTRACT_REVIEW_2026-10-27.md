# GAP-TERM1 — 자율 종료 평가의 선행·성공 predicate·controller 계약 심사

- 확인일: 2026-10-27 KST
- 작업: **DONE**, 비실험. [GAP-S2](./VLA_GAP_RESELECTION_2026-10-27.md)의 좁힌 질문을 [buildup 절차](../../research/IDEA_BUILDUP_GUIDE.md)에 따라 심사했다.
- 결론: **현재 형태의 독립 연구 채택 NO-GO / 평가 진단 HOLD**. 종료기를 바꿀 때 정책 순위가 달라질 수 있다는 질문만으로는 단순 대안 이후의 새 설명을 확보하지 못했다. 실험으로 효과를 반증한 결론이나 종료 연구 전체에 대한 판단은 아니다.
- 범위: 직접 선행 4편(지정 본문 3, 공식 abstract/metadata 1), 공개 저장소 3개 revision의 source/config/doc 21개 지정 구간. [근거·hash·계약 ledger](../sources/vla_termination_contract_review_2026-10-27.json).
- 실행·설치·Docker/GPU probe·local PDF·weight/dataset/init-state payload 수집·신규 등록·읽기 상태 변경은 없다. Registry 1,072편 유지.

## 1. 이번에 판별한 질문

Frozen action policy 두 개의 관측·시간·종료 후 동작을 맞추면, 공통 관측 기반 종료기와 native 종료기에 따라 유효한 자율 완료의 상대 순위가 달라지는가? 그 차이를 task의 goal 유지 조건으로 미리 예측할 수 있으며, threshold·연속 판정·fixed deadline 이후에도 남는가?

중요한 실무 문제라는 사실과 독립 연구 기여는 다르다. 이번 검토는 비교 가능한 계약을 만들 수 있는지, 그리고 **어느 조건에서 단순 대안이 실패하는지를 시험 전에 구별할 근거**가 있는지를 확인했다. 효과가 이미 입증되어야 실험할 수 있다는 요구가 아니다.

## 2. 직접 선행과 아직 모르는 범위

| 자료 | 이번에 확인한 범위 | 채택 심사에 주는 제한 |
|---|---|---|
| [Every Failure Is a Timeout](https://openreview.net/forum?id=8GyKjbTQUd) | 2026 공개, **ICLR 2027 심사 중 제출본**. 공식 API version 2 abstract/metadata | Duration shortcut, fixed-horizon logging, achievement/terminal success 구별은 이미 제안됐다. 본문 미확인으로 정확한 정책×종료기 비교의 포함 여부는 **미확정**이다. |
| [Echo](https://arxiv.org/html/2610.31569v1) | 2026 preprint, A.1–A.2·A.8–A.10 | GT outcome boundary 뒤의 신호 인식 window와 실제 종료 제어는 다르다. Threshold/window 민감도 분석도 이미 있다. A.10 신호는 rollout을 종료하지 않는다. |
| [SEES](https://arxiv.org/html/2609.32698v1) | 2026 preprint, Appendix B | 기존 policy를 고정한 head 학습 및 0.95 threshold·3연속 step 판정이 선행이다. 기록의 끝/경계를 completion label로 쓴다. Oracle-controlled trajectory 감사는 online 종료 효과와 다르다. |
| [SparkVLA](https://arxiv.org/html/2608.16172v1) | 2026 preprint, Algorithm 2·evaluation controls/final-state criteria | Stop은 내부 subtask 전환이며 외부 global termination과 구별된다. 최종 물체 안정성 같은 task별 기준도 이미 사용한다. Stop token 존재만으로 전체 episode의 자율 종료를 입증하지 않는다. |

P12의 공식 [OpenReview API](https://api2.openreview.net/notes/search?term=Every%20Failure%20Is%20a%20Timeout&limit=3)를 재확인했다. PDF web 접근과 공식 title 검색으로 본문 범위는 추가 확보하지 못했다. 확인한 metadata에는 code link가 없지만 논문 전체에 없다고 단정하지 않는다. 접근 실패를 연구 가치의 문제나 실험 blocker로 삼지 않고, 더 이상 같은 접근을 반복하지 않았다. 아래 NO-GO는 **P12가 모든 비교를 이미 했다는 추정 없이도** 성립하는 현재 제안의 선택 판단이다.

Echo의 논문 A.10은 baseline의 최초 성공 중단과 Echo의 continuation을 구분한다. 반면 이번 [공개 runner revision](https://github.com/lyfeng001/Echo-Sim/blob/ed771cfcee11961529541edd7dcc7c16fee788d8/echo/evaluation/evaluate.py#L92)은 두 모델 모두 같은 고정 길이를 실행한다. 논문 점수와 이 code의 protocol을 합치지 않는다. SEES는 head와 VLM의 입력·판정 시점도 달라 그 차이를 head 품질만의 인과 효과로 쓰지 않는다.

## 3. 두 runner에서 실제로 무엇이 종료되는가

아래는 source 정적 확인이다. 해당 revision들이 논문 실행 당시의 environment/checkpoint 조합이었다는 증거는 아니며 실행도 하지 않았다.

| 구분 | OpenVLA 공개 LIBERO runner | Echo-Sim 공개 runner |
|---|---|---|
| revision | `c8f03f48af692657d3060c19588038c7220e9af9` | `ed771cfcee11961529541edd7dcc7c16fee788d8` |
| goal/current success | `env.step`의 `done`을 사용 | 같은 `done`을 action 이후 event로 저장 |
| 최초 성공 이후 | `if done: … break` | 같은 정책의 action을 계속 실행; 신호로 중단하지 않음 |
| budget 예 | `libero_goal` 300 action step + 초기 대기 | config 520 step·20 Hz, 예측 50개 중 8개 실행; settle 20 step 별도 |
| native stop | 이 runner에 정책의 별도 종료 선언 없음 | SS/FS 출력은 있으나 실행 종료 경로에 연결되지 않음 |
| 최종 상태 | 최초 성공 시 중단한 상태; post-stop 물리 관측 아님 | `terminal_success`는 정책이 계속 행동한 끝의 상태; stop-controller 결과 아님 |

근거: [OpenVLA runner L164–238](https://github.com/openvla/openvla/blob/c8f03f48af692657d3060c19588038c7220e9af9/experiments/robot/libero/run_libero_eval.py#L164), [Echo rollout L92–119 / record L219–224](https://github.com/lyfeng001/Echo-Sim/blob/ed771cfcee11961529541edd7dcc7c16fee788d8/echo/evaluation/evaluate.py#L219), [Echo evaluation config](https://github.com/lyfeng001/Echo-Sim/blob/ed771cfcee11961529541edd7dcc7c16fee788d8/configs/evaluation.json).

LIBERO `step`은 superclass의 `done`을 현재 `_check_success()`로 덮어쓴다. Wrapper는 이를 위임한다. Echo vendored판과 canonical LIBERO `8f1084e…`의 **이 두 파일만 SHA-256이 동일**하다. 전체 환경·asset·dependency가 같다는 뜻은 아니다. [Base domain L800–809](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/8f1084e3132a39270c3a13ebe37270a43ece2a01/libero/libero/envs/bddl_base_domain.py#L800), [wrapper L87–104](https://github.com/Lifelong-Robot-Learning/LIBERO/blob/8f1084e3132a39270c3a13ebe37270a43ece2a01/libero/libero/envs/env_wrapper.py#L87).

Echo의 [signal scorer L34–98](https://github.com/lyfeng001/Echo-Sim/blob/ed771cfcee11961529541edd7dcc7c16fee788d8/echo/evaluation/signals.py#L34)는 chunk 전체 50개 신호를 평균하고 다음 query까지 값을 유지한다. 같은 값을 3 control tick 연속 읽는 것은 서로 다른 관측의 3연속 확인과 다르다. 사후 GT 첫 성공을 기준으로 자른 평가 window 역시 online 종료 규칙으로 가져올 수 없다.

두 runner의 점수를 직접 비교하면 정책뿐 아니라 suite/scene·settling·horizon·controller·입력이 함께 달라진다. 위 표는 **평가 의미 비교이며 공정한 두 정책 실험 packet이 아니다**. Echo baseline/Echo 설정은 학습에 쓰는 failure 자료와 모델도 달라 단순히 같은 action policy의 stop head만 교체한 비교로 읽지 않는다.

## 4. 실제 task predicate와 종료 이후 controller

두 task는 Echo가 포함한 LIBERO Goal BDDL과 predicate 호출 경로에서 확인했다. Recovery 평가 scene과 같은 instance라고 보장하지 않는다. Pure holding task나 안정/불안정의 검증된 대조쌍은 확보하지 않았다.

| 과제 | Native goal와 source | Goal에 명시되지 않은 것 | 비교에 추가한다면 |
|---|---|---|---|
| Put the bowl on the plate | BDDL `On(akita_black_bowl_1, plate_1)`. `On→plate.check_ontop(bowl)`: plate의 z≤bowl의 z, 두 물체 contact, xy 거리<0.03 | Gripper release, 속도, 유지 시간 | Release·dwell 조건은 **더 강한 task variant**로 별도 보고한다. Native 평가 오류라고 부르지 않는다. |
| Open the middle drawer of the cabinet | BDDL `Open(wooden_cabinet_1_middle_region)`. Site joint→parent WoodenCabinet의 `qpos < -0.14` 판정 | Handle release, 속도, 유지 시간 | 정지 후 열린 상태 유지 조건과 controller를 별도로 정의한다. 해당 수치의 단위는 asset까지 검증하지 않았으므로 추가 해석하지 않는다. |

근거: [bowl BDDL L124](https://github.com/lyfeng001/Echo-Sim/blob/ed771cfcee11961529541edd7dcc7c16fee788d8/LIBERO/libero/libero/bddl_files/libero_goal/put_the_bowl_on_the_plate.bddl#L124), [drawer BDDL L123](https://github.com/lyfeng001/Echo-Sim/blob/ed771cfcee11961529541edd7dcc7c16fee788d8/LIBERO/libero/libero/bddl_files/libero_goal/open_the_middle_drawer_of_the_cabinet.bddl#L123), [predicate L62 / L101](https://github.com/lyfeng001/Echo-Sim/blob/ed771cfcee11961529541edd7dcc7c16fee788d8/LIBERO/libero/libero/envs/predicates/base_predicates.py#L62), [object state L78 / L206](https://github.com/lyfeng001/Echo-Sim/blob/ed771cfcee11961529541edd7dcc7c16fee788d8/LIBERO/libero/libero/envs/object_states/base_object_states.py#L78), [WoodenCabinet L173–194](https://github.com/lyfeng001/Echo-Sim/blob/ed771cfcee11961529541edd7dcc7c16fee788d8/LIBERO/libero/libero/envs/objects/articulated_objects.py#L173).

OpenVLA의 [dummy action](https://github.com/openvla/openvla/blob/c8f03f48af692657d3060c19588038c7220e9af9/experiments/robot/libero/libero_utils.py#L28)은 `[0,0,0,0,0,0,-1]`이며 runner는 `-1=open`으로 명시한다. 이를 모든 task의 “아무것도 하지 않는 종료”로 재사용하면 grasp 상태도 바꾼다. 물체를 잡아 유지해야 하는 task에는 보편적인 release 규칙을 적용할 수 없다. 이는 controller에 대한 반례이지 이번 두 task에서 관측한 실패가 아니다.

후속 비교의 최소 명세는 **정책 action 중단**, **physics 계속 진행**, **명시한 pose/gripper 유지 또는 task별 release controller**, **고정된 관측 시간 Δ**다. Zero Cartesian delta와 마지막 gripper command 유지도 검증 전 후보일 뿐 물리적 정지를 보장하지 않는다. Simulator freeze, 정책 continuation, 실제 stop-controller를 같은 outcome으로 합치지 않는다. Δ·controller gain·release timing은 아직 동결하지 않았으며 executable manifest도 없다.

## 5. 한 장 비교 계약 — 설계까지만 완료

| 항목 | 필요한 조건 / 현재 경계 |
|---|---|
| Primary estimand | 같은 task의 유효 자율 완료 확률 `Q(policy, stop rule; G, K, T, Δ)`. Goal 도달 `max G`, 종료 선언 `D`, 종료 후 유지 결과를 각각 기록한다. First-hit와 최종 success는 이미 존재하는 보조 지표다. |
| Action 고정 | 각 checkpoint의 action 생성·normalizer·controller를 비교 branch 사이 고정. Head가 action generation 자체를 바꾸면 종료기만의 효과로 해석하지 않는다. |
| 최소 baselines | B0 fixed deadline; B1 공통 관측 detector+threshold; B2 같은 detector+서로 다른 query 관측의 연속 판정; B3 native rule(실제 제공될 때만); B4 GT oracle는 reference 전용. |
| 정보·라벨·budget | 공통 observer의 RGB/state 범위·query 시점, calibration scene/label·tuning 예산, 물리 시간 T, Δ, inference/query 비용을 맞춘다. Native privileged feature를 맞출 수 없으면 별도 system 비교다. |
| 인과 시간 | Query는 action 전 관측을 읽고 goal truth는 action 후 state에 붙인다. Chunk token/held signal을 새 관측으로 세지 않는다. GT boundary·미래 성공을 online stop input에 넣지 않는다. |
| 후속 동작 | 동일 K에서 비교 후 task-valid K의 민감도를 별도로 본다. Goal/release 조건을 바꾼 결과는 task 변경 효과로 분리한다. Stop 후 새 goal을 만들어 주는 recovery를 단순 종료로 섞지 않는다. |
| Split / 단위 | Calibration/test는 scene·init-state 계보로 분리. 같은 scene의 frame·chunk token·여러 threshold는 독립 표본이 아니다. 실행 시간·query 수·실패/미종료도 함께 보고한다. |
| 누락 cell | OpenVLA runner에는 native stop이 없고 Echo 신호는 stop에 미연결이다. 빈 cell을 임의 head나 0값으로 채우지 않는다. 공통 observer의 양 정책 적용 및 같은 task/controller 지원도 미검증이다. |
| 필요한 artifact | 공통 task/init-state·환경 revision·checkpoint/normalizer·관측/행동 시각·GT·선언·실행 K·post-stop trace·scene split·baseline 설정. 이번에는 명세만 작성, payload/adapter/실행 결과 없음. |
| 순서 | 먼저 source/비교 가능한 cell과 예측을 확보한다. 그 뒤에만 사용자가 허용하는 로컬 Docker의 최소 paired pilot. GPU 확보나 문서 완료만으로 착수하지 않는다. |

## 6. 순위 변화만으로는 부족한 이유와 기각 기준

다음은 **연구자 해석인 조건부 항등식**이며 논문의 정리나 측정 결과가 아니다. Stop 이전 action/state prefix가 같고, 유효 완료가 선언 시 goal 충족을 요구하며, stop 후 controller가 새로운 goal 달성을 대신 만들어 주지 않는다고 하자. 정책 i의 oracle first-hit 확률을 `p_i`, 자율 완료 확률을 `q_i`, 손실을 `d_i = p_i - q_i ≥ 0`로 둔다. `p_A > p_B`일 때 자율 완료 순위가 뒤집히는 조건은 단순히

`q_A < q_B ⇔ d_A - d_B > p_A - p_B`

이다. 실제 `d` 값이나 역전은 측정하지 않았다. 이 관계만으로 **어떤 장면/정책의 d가 더 클지**는 예측하지 못한다. 조건이 다른 checkpoint·시간·controller를 섞으면 위 prefix 가정조차 성립하지 않는다.

| 경쟁 설명 | 구별하려면 | 현재 판단 |
|---|---|---|
| Detector calibration·짧은 transient 성공을 다시 측정한 것 | 동일 관측 B1/B2 및 T 이후에도 독립 task 조건에 따라 남는 차이 | Threshold/연속 판정이 이미 직접 선행이며, 그 이후 남는 조건 예측을 확보하지 못함 |
| Release·유지 조건/시간을 강화해 점수가 변한 것 | 같은 G/K/T에서 차이 확인, task variant는 분리 | 두 native predicate가 release/dwell을 보장하지 않는다는 사실만으로 새로운 실패 기제가 생기지 않음 |
| 신호의 시간 차이·정보량 차이를 종료 능력으로 부른 것 | 서로 다른 관측 query와 policy-visible input, offline/online 구분 | Echo/SEES/SparkVLA를 하나의 동일 종료 interface로 비교할 수 없음 |
| 사전 물리 조건이 관측 모호성과 종료 오류를 함께 예측함 | 단순 대안의 조건부 실패를 구별하는 자연 사례·외부 근거와 명확한 예측 | 잠재적 재개 방향이나 아직 사례·대조 조건 미확보. 기존 CONTACT/CF/종료 선행과 추가 충돌 심사 필요 |

**기각 규칙:** 새 metric의 재명명, post-hoc 순위 역전만의 주장, GT 정렬 누출, 중복 신호의 연속 판정, 추가 시간/정보/강화된 task 계약으로 설명되는 결과라면 현재 독립 후보를 채택하지 않는다. 공통 단순 detector가 충분하면 새 termination method를 만들지 않는다. 반대로 자연적인 조건 차이가 사전에 예측되고 같은 계약의 단순 대안이 왜 실패할지 구별할 수 있다면 작은 진단을 다시 심사할 수 있다. 실제 효과를 미리 증명할 필요는 없다.

## 7. 판정·인계

**GAP-TERM1 DONE. 현재 독립 후보 채택 NO-GO, 재사용할 평가 진단은 HOLD.** 성공 predicate·종료 후 행동·정보/시간 budget의 분리는 유용한 평가 원칙으로 남긴다. 연구 착수 판단을 낮춘 이유는 GPU 부족이나 PDF 접근 문제가 아니라, 기존 metric/종료 선행과 강한 단순 대안 이후의 조건부 설명이 아직 없기 때문이다. P12의 정확한 본문 범위는 끝내 미확인이며, 이 미확인을 “새롭다” 또는 “전부 해결됐다”로 해석하지 않는다.

- `GAP-TERM-R1 WAITING_EVIDENCE`: 동일 goal/controller/input 조건의 자연 사례, 단순 대안 이후 갈리는 사전 예측, 최신 직접 선행과의 차이가 새로 확보될 때만 재심사한다. 같은 metadata·PDF 경로 확인이나 문서 연장을 반복하지 않는다.
- 다음 **GAP-S3 READY**: VLA navigation·mobile manipulation의 공백을 새로 조사한다. 2024–2026 공식 proceedings/journal과 최신 direct collision을 대조하고, 이동–조작 연결에서 남는 질문이 있는지부터 확인한다. Retrieval/scene graph·기하 planner·skill handoff 같은 단순 대안, 기존 D2/D3·E2·RP-3·AUTH·reactive navigation의 폐기/보류 경계를 먼저 적용한다. 새 gap이 있다는 전제나 새 프로젝트 채택이 아니다.
- 상세 활성 순서는 [TODO](../../TODO.md), canonical 질문은 [GAP-TERM](../../synthesis/04_vla_generalist.md#gap-termination-2026). 기존 모든 후보의 보류/종료 판단은 유지한다.

## 8. 문서·저장소 검증

`py_compile`, reading tier generator, `git diff --check`, repository audit를 완료했다. Audit 오류·경고 **0**, registry **1,072편**, CORE/NEXT/REFERENCE/ARCHIVE **47/297/486/242**, active/history 읽기 기록 **344/47**, 표준 note **5,360개**를 유지한다. Markdown 5,537개·상대 링크 10,914개를 검사했다.

`PAPER.md`, canonical manifest/meta, tier CSV, active/history reading CSV의 6개 파일은 작업 전과 byte-identical이다. 작업 전 dirty 645개 중 이번 수정 7개를 제외한 **638개**와 기존 삭제 10개를 보존했다. 신규 파일은 이 보고서와 ledger 2개뿐이다. 확인에 쓴 임시 공개 source/config/doc 21개와 metadata 3개는 제거하고 revision·hash·지정 구간만 ledger에 남겼다. 문서 무결성 검사는 연구 실험·정책 효과 검증이 아니다.
