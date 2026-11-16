# VLA의 부분 지시 수정: 제약 유지와 철회

**현행 투자 판단 — 2026-11-07:** [8개 후보 비교](../../README.md#candidate-priority)의 VLA 단독 대안 우선이다. 남는 제약·철회의 공동 이행과 의미/행동 오류 분해는 비교적 선명하지만 H/R·정답 지시 대조 이후 남는 기여는 미검증이다. RL 결합을 필수로 하지 않을 때의 주요 선택지이며 전체 순위와 기존 3개 packet 내 순위를 구별한다.

현행 비실험 상태 검토: **2026-11-05** · [7단계 상태·기여 가설·판단 분기](#buildup-status). 기존 문헌/계약/결과를 대조한 보강이며 새 효과 관측은 없다.

**11/05 통합 판단:** VLA 단독 대안의 우선 후보로 유지한다. 새 직접 선행 BAS-VLA가 목표뿐 아니라 관계·순서 변경도 평가하므로 일반 instruction switching으로 차별화하지 않는다. 남는 질문은 여러 수정에서 유지할 제약과 철회할 제약의 공동 이행이다. H 전체 이력 재작성·R 규칙·O 정답 완전 지시·A atomic 능력을 대조한다. O부터 실패하면 semantic updater의 가치로 해석하지 않는다. RL은 추가 필요성이 확인될 때만 고려한다.

근거·전체 상대 비교: [기존 6개+새 2개 공백 검토](../../../update/INTEGRATED_GAP_REVIEW_2026-11-05.md). 신규 paper별 확인 절과 status는 [등록 원장](../../../sources/registry_admissions_2026-11-05.json)에 통합한다. 기존 실행 계약·원시 결과·과거 source 날짜는 보존한다.

현재 판단: 좁은 평가 후보 유지·native 효과 미검증. 아래 개요와 단일 비교 계약이 현행 설계다. 과거 별도 brief·source 검토·사례집을 통합했다. 중복된 작업 인계·저장소 수량은 제거하고 구체적인 source·의미 사례를 보존했다.

[연구 내용](../내용/README.md) · [재현 방법](../재현%20방법/README.md)

<a id="buildup-status"></a>

## 비실험 buildup 현행 상태 — 2026-11-04

**판정: 좁은 평가 후보 유지 · 내부 비실험 설계 정리 · updater/observer·정책 효과 미검증.** [7단계 비실험 절차](../../../../research/IDEA_BUILDUP_GUIDE.md#nonexperimental-workflow)를 기존 문헌·논리·계약에 적용해 정리했다. 아래 상태는 새 실험 결과나 11/04 신규 문헌 전수조사가 아니다.

**한 문단 기여 가설:** 부분 수정 후에도 유효한 조건을 따르는 로봇이 필요하다. 기여 후보는 **현재 지시를 잘못 갱신한 오류와, 올바른 지시를 행동으로 이행하지 못한 오류를 구분하고 유용한 개선 지점을 찾는 것**이다. 일반적인 대화 memory·제약 목록 관리는 선행과 구별되는 기여가 아니다.

| 비실험 단계 | 상태 | 현재 근거·완료 경계 |
|---|---|---|
| 1 문제·독자 | 정리됨 | [개요](#overview): 실행 중 목적지 변경·금지 철회를 사용하는 VLA interaction. 허용과 의무, 과거 위반과 이후 유효 구간을 구분 |
| 2 가까운 선행 | 지정 범위 확인 | [source 비교](#source-review): Hi Robot·ReSteer·How-level, 계약의 ReBIND 인접 선행. 일반 feedback·constraint ledger는 기존 원리 |
| 3 질문·대안 | 정리됨 | 8개 의미 사례, 전체 이력 재작성 H·상태 갱신 S·제한 규칙 R·정답 지시 O·단일 작업 A. 우연한 제약 준수와 이해를 구분 |
| 4 기여 서술 | 가설 초안 | 위 오류 분해와 joint goal/constraint 결과가 중심. 단일 prompt나 작은 상위 모델의 차이만으로 일반 기억 능력 주장은 불가 |
| 5 최소 비교 | 설계됨·미실행 | [비교 계약](../재현%20방법/COMPARISON_CONTRACT.json): R1/R4 중심, R7/R8 control, 공통 renderer·동일 분기 상태. 기존 R8 P0와 효과 비교는 별개 |
| 6 실행 부담 | 준비 코드 있음·교정 미완 | P0 recipe/launcher는 있으나 image/native 실행은 미검증. 상위 updater·규칙 parser·renderer·observer·상태 복원 구현과 교정 필요 |
| 7 외부 비판 | 질문 준비·미수신 | [기존 검토 질문](../../../update/THREE_CANDIDATES_NONEXPERIMENTAL_2026-11-01.md#revision)과 아래 반론. 응답 기록 없음 |

**결과에 따른 판단 — 아직 관측하지 않은 분기 포함**

| 다음 증거 | 바뀌는 판단 | 이 증거만으로 하지 않을 주장 |
|---|---|---|
| 자동 의미 출력은 틀리지만 정답 지시 O와 단일 작업 A는 성공 | 의미 갱신을 개선할 질문으로 좁힘 | 관측 전부터 S의 우월성을 확정 |
| O도 실패하지만 A는 성공 | 복합 제약의 정책 입력/실행·물리 경로를 검토 | 철회 기억만의 문제라는 단정 |
| A도 실패하거나 정답/상태 복원이 불일치 | 기본 능력·평가 구현을 먼저 교정 | 지시 이해 실패율로 집계 |
| H 또는 R이 같은 공동 목표·제약 성능을 충분히 냄 | 단순 갱신 경로와 그 적용 범위를 결과로 남김 | 새 memory 모델의 필요성 |

상위 모델 호출·입력 token·공통 renderer 비용과 VLA 제어 시간을 별도로 기록한다. 동일한 의미 정답이 동일 렌더링 입력으로 이어지는지부터 확인해야 한다. 상위 모델은 계약에 고정됐지만 weights·실행 prompt·메모리 사용은 미검증이며 전체 구현 공수는 아직 산정할 근거가 없다.

**외부 검토 준비:** 가장 강한 외부 질문은 “명세 컴파일 선행에 비해 로봇의 시간별 제약 이행에서 새로 얻는 지식은 무엇이며, 정답 지시 대조가 그 주장을 실제로 구별하는가?”다. 위 개요와 사례 R1/R4, 비교 계약을 함께 제시한다. 실제 응답·반영이 생기면 내용과 source 위치를 기록한다. 미수신은 작은 탐색을 금지하는 진입 조건이 아니다.

**다음 확인과 문서 종료점:** 문헌·의미 설계는 현재 범위에서 정리됐다. 첫 구현 주의 산출물은 공통 schema/renderer 연결과 observer의 참/거짓 사례 판별이며, native 효과는 이후 단계다. 실제 모델/시뮬레이션 검사는 재개 시 local Docker에서 수행한다. 동일 관측·동일 렌더링인데 결과가 달라지면 먼저 난수·상태·큐·구현 차이를 조사한다. 새로운 직접 선행·자료·반례·피드백 없이 같은 문서 검토를 반복할 내부 과제로 만들지 않는다. 실행 범위·상한은 기존 계약과 [재현 안내](../재현%20방법/README.md)가 관리한다.


<a id="overview"></a>

<a id="overview-vla의-부분-지시-수정에서-제약-유지와-철회"></a>
## VLA의 부분 지시 수정에서 제약 유지와 철회

*Constraint Preservation and Revocation under Partial Instruction Revisions for Vision-Language-Action Policies*

2026-11-01 · 비실험 문헌·분석 설계 보완 완료 · NVIDIA GPU 환경에서의 구현·실행·비교 검증 대기

**핵심 질문:** 로봇이 작업하는 도중 사용자가 지시 일부를 바꾸면, VLA는 바뀐 목표를 수행하면서 여전히 유효한 제약을 유지하고 명시적으로 철회된 제약을 제거할 수 있는가? 전체 대화를 바탕으로 현재 지시를 매번 다시 작성하는 단순 방법만으로 충분한가?

예를 들어 “그릇을 접시에 놓되 병은 움직이지 마”라는 지시에서 목적지만 캐비닛으로 바꾸면 병의 이동 금지는 유지되어야 한다. 이후 “병 이동 금지를 취소하고 병을 랙에 놓아”라고 하면 새로운 목표에는 병 이동이 필요하다. 단순히 “병을 움직여도 된다”라고 한 경우에는 실제로 병을 움직이지 않아도 올바른 행동이다. 철회 이후의 허용이 이전에 발생한 위반까지 없애지는 않는다.

[Hi Robot, ICML 2025](https://proceedings.mlr.press/v267/shi25d.html)은 계층적 VLA로 복잡한 지시와 실행 중 피드백을 처리하며, [ReSteer, RSS 2026](https://roboticsproceedings.org/rss22/p143.html)는 중간 상태에서 새로운 작업 지시를 따르는 능력을 평가·개선한다. 본 후보는 이를 바탕으로 **부분 수정 후 어떤 조건이 유효한지에 대한 의미 판단과 실제 행동의 제약 준수를 함께 비교**하려는 질문이다. 일반적인 지시 전환이나 피드백 대응을 새로운 기여로 주장하지 않으며, 이 좁은 비교의 신규성과 연구 가치는 아직 확정되지 않았다.

첫 실험 대상은 ReSteer의 공개 LIBERO 장면과 공개 π0.5 LIBERO 정책이다. 그릇·병·접시·캐비닛·랙에 연결한 수작업 사례 8개를 정리했으며, 먼저 목적지 변경 후 제약 유지와 금지 철회 후 필요한 행동 수행을 조사한다. 이 사례들은 실제 정책 실패가 관측된 데이터나 검증된 benchmark가 아니다. [사례·근거 검토](README.md#source-review).

| 비교 조건 | 확인하려는 내용 |
|---|---|
| 전체 대화에서 현재 지시를 매번 다시 작성 | 단순한 자동 재명시로 충분한가 |
| 목표·제약 목록을 유지하고 수정 발화를 반영 | 명시적인 상태 관리가 재명시보다 도움이 되는가 |
| 사람이 작성한 정확한 전체 현재 지시 | 의미 갱신 오류를 제외해도 정책이 행동할 수 있는가 |
| 제약을 제외한 짧은 단일 작업 지시 | 같은 물리 상태에서 기본 작업을 수행할 능력이 있는가 |

자동 방법끼리는 같은 상위 모델·관측·대화 이력과 고정된 저수준 VLA를 사용하고, 입력 길이·호출 수·추론 비용을 기록한다. 사람이 작성한 정답 지시는 진단용이며 자동 방법에 제공하지 않는다. 같은 중간 상태에서 분기하고, 의미가 바뀌지 않는 재진술을 대조로 사용해 재질의·행동 큐 초기화의 영향을 구분한다. 이 전체 비교와 자동 의미 갱신기는 아직 구현하지 않았다.

[GPU 전 추가 검토](../../../update/PRE_GPU_BUILDUP_REVIEW_2026-10-31.md#instruction-revision)에서 규칙 기반 갱신 대안, 공통 의미 출력·문장 renderer, 수정 전후 위반·기술 오류의 분리 기준을 보완했다. 제약을 무시해도 병이 움직이지 않는 장면은 성공하더라도 지시 이해의 증거가 약하므로 제약 없는 목표 지시와 비교한다. 규칙 parser·상위 모델 검증은 아직 수행하지 않았다.

[후속 비실험 보완](../../../update/PRE_GPU_BUILDUP_REVIEW_2026-10-31.md#remaining-work-review)에서 [8개 영문 발화·의미 정답](../재현%20방법/SEMANTIC_CASES.json)을 작성했다. 정답 문장에만 남아 있던 R4/R5의 취소·허용 표현을 제거해 자동 방법과 같은 활성 조건을 전달하도록 맞췄다. 수정 직전 action의 결과를 먼저 채점한 뒤 새 제약을 적용하고, 후속 비교는 같은 horizon에서 판단한다. 수작업 명세이며 실제 renderer·observer 실행이나 모델 정확도 검증은 아니다.

주요 결과는 **수정 목표 달성과 유효한 기간 동안의 제약 준수를 함께 만족한 비율**이다. 목표 성공만으로 제약 준수를 판단하지 않고, 물체 위치·자세의 시간별 변화와 제약 추가·철회 시점을 기록한다. 이동 금지와 접촉 금지도 구별한다. 행동 실패만으로 철회된 금지가 기억에 남았다고 단정하지 않으며, 같은 상태의 직접 작업 지시와 비교한다. 측정 허용 오차와 상태 복원·평가 종료 조건은 비교 전에 고정해야 한다.

현재 문헌 검토·사례 명세·코드와 체크포인트 버전 고정·Docker recipe·최소 실행 코드를 작성했다. **이미지 빌드와 native 정책 실행은 미검증**이다. 10월 31일 현재 Docker ARM64 환경에서 GPU 할당이 실패했으며, 패키지·모델을 host에 설치하지 않았다. [환경 설정·재개 절차](../재현%20방법/README.md#execution).

NVIDIA CUDA·EGL을 지원하는 Linux x86-64 로컬 Docker에서 먼저 단순 목적지 전환 1건으로 실제 관측·두 추론 응답·행동 큐 교체를 확인한다. 최대 7회 정책 action의 이 검사는 연구 효과나 기본 작업 성공을 입증하지 않는다. 이후 시간별 제약 측정과 동일 상태 복원을 구현하고, 정확한 전체 지시 및 단일 작업 지시로 능력을 확인한 뒤 자동 방법을 비교한다. 설치·추론·시뮬레이션은 모두 Docker 내부에서 수행한다.

전체 지시의 자동 재작성으로 충분하다면 복잡한 기억 구조나 추가 학습의 필요성은 줄어든다. 정확한 지시에서도 실패하면 물리적 수행 능력·제약 실행·정책 입력 표현을 먼저 조사한다. 의미 채점의 차이만 있고 행동 결과와 연결되지 않으면 VLA 연구 기여는 제한된다. 남은 buildup은 작은 공정 비교로 이 분기를 확인하고 선행 대비 지식·한계 및 외부 피드백을 검토해 진행·수정·중단을 판단하는 것이다. 한 번의 GPU 실행이나 유리한 결과를 완료 조건으로 삼지 않는다.

11/01 [세 후보 비실험 완결 검토](../../../update/THREE_CANDIDATES_NONEXPERIMENTAL_2026-11-01.md#revision)에서 인접 분야의 제약 철회·명세 컴파일 선행을 반영했다. [비교 계약](../재현%20방법/COMPARISON_CONTRACT.json)에 H/S의 첫 공통 모델 revision·decoding, 규칙 갱신·공통 renderer, 위치/회전 observer 정의와 조건부 교정 절차를 명시했다. 문헌·논리·분석 설계는 완료했지만 실제 updater/observer 구현·정책 효과·독립 외부 피드백은 남아 있다. 첫 모델에서의 차이를 일반 memory 우월성이나 새 ledger 방법으로 주장하지 않는다.

현재 작업은 [TODO](../../../../TODO.md), 연구 질문의 상세 비교는 [VLA synthesis](../../../../synthesis/04_vla_generalist.md#gap-instruction-revision-2026)를 따른다. 이 문서는 연구 개요이며 별도의 우선순위 목록이나 실행 명세가 아니다.

<a id="source-review"></a>

<a id="source-review-2-공개-interface에서-확인한-것"></a>
### 2. 공개 interface에서 확인한 것

ReSteer는 commit `7329c159319a346b7245a69c128e5d4940c0763b`, How-level 공개 코드는 `478fad54689126e4303bdc6bcb3c8e064e5934ab`의 파일을 읽었다. 두 GitHub tree는 응답이 잘리지 않았음을 확인했다. Source를 읽은 것이 native 실행 검증이나 전체 code audit를 뜻하지 않는다.

| 확인 대상 | 실제 source 사실 | 이번 설계에 주는 결론 |
|---|---|---|
| ReSteer [task 표](https://github.com/ChenZhenY/ReSteer/blob/7329c159319a346b7245a69c128e5d4940c0763b/resteer/tasks.py), [장면](https://github.com/ChenZhenY/ReSteer/blob/7329c159319a346b7245a69c128e5d4940c0763b/third_party/libero/libero/libero/bddl_files/libero_steerability/libero_goal_steerability.bddl) | Bowl/plate/bottle/cream cheese 등이 같은 장면에 있고 task별 goal key를 선택한다. BDDL 전체 goal 묶음과 한 target task의 성공은 다르다 | 설명용 색 블록 대신 실제 object ID에 사례를 연결했다. 복합 제약을 수행할 능력이 있다는 뜻은 아님 |
| ReSteer [policy input](https://github.com/ChenZhenY/ReSteer/blob/7329c159319a346b7245a69c128e5d4940c0763b/resteer/sim/libero.py#L95), [interface 문서](https://github.com/ChenZhenY/ReSteer/blob/7329c159319a346b7245a69c128e5d4940c0763b/docs/interfaces.md) | 두 RGB·robot state와 `prompt` 문자열을 websocket 입력으로 전달 | 재작성한 문장을 전달할 경로는 있다. 복합/부정 지시·긴 history의 이해, token 제한, truncation은 별도 미검증 |
| ReSteer [switch rollout](https://github.com/ChenZhenY/ReSteer/blob/7329c159319a346b7245a69c128e5d4940c0763b/resteer/eval/rollout.py#L63) | 지정 step에 task를 바꾸고 action queue를 비운다. `step > switch_step`에서 target goal이 처음 성립하면 return한다 | 즉시 재질의의 재사용 경로. 기존 제약의 위반 이력이나 고정 종료 시점의 복합 결과를 그대로 얻는 평가기는 아님 |
| ReSteer [평가 loop](https://github.com/ChenZhenY/ReSteer/blob/7329c159319a346b7245a69c128e5d4940c0763b/resteer/eval/steerability.py#L143) | Target/repeat별 `sim.reset` 후 source→target rollout. RNG 기반 재개를 지원하지만 모든 arm이 같은 실제 중간 상태를 공유하는 구조는 아님 | 같은 seed라고 paired intermediate state라고 기록하지 않는다. Native branch 검증이 추가로 필요 |
| ReSteer [state restore](https://github.com/ChenZhenY/ReSteer/blob/7329c159319a346b7245a69c128e5d4940c0763b/third_party/libero/libero/libero/envs/env_wrapper.py#L121), [CMI state 설정](https://github.com/ChenZhenY/ReSteer/blob/7329c159319a346b7245a69c128e5d4940c0763b/resteer/cmi/sample_actions.py#L67) | Flattened sim state의 get/set과 observation 재생성 함수가 있다. CMI helper는 reset/set/forward 뒤 **zero action 한 step**을 추가한다 | 이 helper를 같은 시점 복원의 증거로 쓰지 않는다. Controller 목표·환경 clock·action queue·policy RNG/내부 상태·object pose까지 실제 검증 필요 |
| ReSteer [pose 접근](https://github.com/ChenZhenY/ReSteer/blob/7329c159319a346b7245a69c128e5d4940c0763b/third_party/libero/libero/libero/envs/object_states/base_object_states.py#L47), [success dict](https://github.com/ChenZhenY/ReSteer/blob/7329c159319a346b7245a69c128e5d4940c0763b/third_party/libero/libero/libero/envs/problems/libero_tabletop_manipulation.py#L144) | Object position/quaternion 및 goal별 predicate를 읽는 경로가 있다. 이 fork의 object `check_ontop`은 xy threshold 0.1을 사용한다 | 보호 물체의 구간별 pose 검사에는 새 observer가 필요. Predicate와 movement tolerance를 섞지 않고, dict 전체의 truthiness를 성공으로 쓰지 않음 |
| How-level [온라인 correction](https://github.com/sangwu99/how-level-vla-Arxiv/blob/478fad54689126e4303bdc6bcb3c8e064e5934ab/diagnosis/online_intervention/system1/correction_pi0_evaluator.py#L112) | 고정 `base_instr`에 현재 correction을 붙이고 correction이 달라지면 queue를 비운다. SKIP이면 correction을 제거한다 | 자유로운 사용자 목표 수정·기간별 금지 관리와 동일한 계약은 아니다. 단순 append-only 대안으로 참고할 수 있음 |
| SIMPLER-IN [episode loop](https://github.com/sangwu99/how-level-vla-Arxiv/blob/478fad54689126e4303bdc6bcb3c8e064e5934ab/simpler_in/eval/eval_client_pi0.py#L34), [평가 정의](https://github.com/sangwu99/how-level-vla-Arxiv/blob/478fad54689126e4303bdc6bcb3c8e064e5934ab/simpler_in/envs/simpler_in_envs.py) | Reset 후 instruction을 얻고 episode에서 사용한다. `success`와 `constraint_ok`를 따로 기록하며, Grasp는 grasp event, Place는 첫 landing을 저장한다 | 조건 준수 자체가 이미 평가 대상이다. 첫 grasp/landing을 고정하는 정의를 중간 수정·최종 상태 채점에 그대로 사용할 수 없음. Path/Grasp/Place의 `constraint_ok` 정의도 서로 같지 않음 |

**Hi Robot:** [본문 §4–5](https://arxiv.org/html/2502.19417v1)은 사용자 개입 후 고수준 inference, 기존 지시 복귀, 부정 제약과 상황 피드백을 다룬다. 인간 고수준 oracle과 같은 저수준 정책을 쓰는 비교도 있다. [공식 project](https://www.pi.website/research/hirobot)에서 이번 검토에 필요한 task/evaluator·고수준 checkpoint의 재현 경로는 식별하지 못했다. 이를 전체 코드가 없다는 단정이나 논문 가치 판단으로 바꾸지 않는다. 우리의 정답 재명시 조건은 skill sequence까지 주는 Hi Robot oracle보다 적은 정보를 준다.

이번 직접 대조는 세 논문의 지정 구간과 관련 공개 파일에 한정한다. SwitchVLA·Causeway 등은 10/29 경계 판단을 재사용하며 전체 방법을 새로 심사한 것으로 표시하지 않는다. README의 실행 명령은 실행하지 않았다. ReSteer가 보고한 release 재실행 결과와 논문의 수치도 혼합하지 않았다.

<a id="source-review-3-사례별-선행-중복과-평가-가능성"></a>
### 3. 사례별 선행 중복과 평가 가능성

정확한 최초/수정/전체 지시·유효 시간·필요 행동은 [CASEBOOK](README.md#cases)이 소유한다.

| 사례 | 기존 범위와의 관계 | 필요한 관측·현재 배치 |
|---|---|---|
| R1 목적지 변경 + 기존 금지 유지 | Hi Robot의 동적 제약과 직접 인접. 일반 “제약 유지”는 신규 아님 | 기존 bowl 목표 + 병 pose trajectory. **핵심**; 제약이 실제 행동 선택에 영향을 주는 장면인지는 미확인 |
| R2 대상 변경 + 다른 물체 보호 | ReSteer task switching + 보호 조건 | Target goal·cheese pose. Grasp 전환의 추가 교란 때문에 후속 확장 |
| R3 제한 추가 | Hi Robot의 실행 중 “leave it alone”과 직접 중첩 | 추가 시점의 pose 기준·과거 비소급. 시간 의미 확장 |
| R4 금지 철회 + 필요한 대상 이동 | Hi Robot의 interjection 뒤 복귀와 인접. ReSteer의 target 성공만으로 의미 원인을 알 수 없음 | 병이 랙 밖인 witness + 병→랙 능력. **핵심**; 실패는 철회 실패와 동의어가 아님 |
| R5 허용만 추가 | Dialogue-state semantics이며 action을 반드시 바꾸지 않음 | 의미 대조군. 행동상 비이동을 실패로 세지 않음 |
| R6 달성한 하위 목표 유지 | 계층적 계획·복합 목표의 기존 범위 | 실제 prefix·병-on-rack의 구간별 유지. 첫 pilot에서는 제외 |
| R7 의미 불변 재진술 | Instruction paraphrase와 reset/requery 영향의 기존 문제 | R1과 동일 source prefix·기존 제한. 대조군 |
| R8 제약 없는 전환 | ReSteer가 이미 다루는 목표 전환 | 기본 IO·switch/continuation 대조군. 새 기여로 세지 않음 |

**공백의 현재 표현:** “VLA가 조건을 유지하지 못한다”가 아니라, **동일한 실행 상태에서 부분 수정의 의미를 자동 재명시하는 것만으로 goal·활성 제약의 공동 준수가 어느 범위까지 회복되는가?**이다. 이 답이 기존 방법을 어떻게 사용하는지 바꾸면 평가 기여가 될 수 있다. 단순 prompt 차이 하나의 성능 수치만으로 독립 연구 가치를 확정하지 않는다.

<a id="source-review-4-단순-baseline과-의미행동의-분리"></a>
### 4. 단순 baseline과 의미/행동의 분리

자동 baseline은 **원문 사용자 발화만으로** 현재 목표·조건을 추정해야 한다. CASEBOOK의 정답 슬롯, 수정 유형 ID, goal key, simulator 물체 pose, 정답 active interval을 입력으로 주면 자동 의미 해석을 검증한 것이 아니다.

| arm | 허용된 정보와 처리 | 역할 |
|---|---|---|
| H: 전체 이력 재해석 | 최초 지시+모든 수정 발화를 같은 고정 상위 모델에 주고 현재 목표/조건을 출력. 고정 renderer가 policy 문장으로 바꿈 | 강한 기본 baseline |
| S: 조건 목록 갱신 | 최초 상태부터 **자신이 추정한** 목표/조건 목록+새 발화를 같은 모델로 갱신. H와 같은 출력 형식·renderer·관측·호출 예산 | 학습 없는 단순 대안. 이전 목록을 매번 gold로 교체하지 않음 |
| O: 정답 전체 지시 | 사람이 검수한 전체 현재 지시를 같은 frozen VLA에 제공 | 의미 업데이트 오류를 제외하는 정보 oracle. 배포 가능 방법과 동등한 정보 조건은 아님 |
| A: 짧은 atomic task 지시 | 같은 상태에서 bowl→cabinet 또는 bottle→rack 같은 기존 task 문장 | 기본 continuation competence 대조. 보호 제약을 제거한 조건의 성공은 복합 제약 능력이 아님 |

마지막 발화만 전달하거나 긴 대화를 raw prompt로 VLA에 직접 주는 조건은 선택적 약한 대조군이다. 그것을 이기는 것으로 S의 가치를 주장하지 않는다. 11/01 비교 계약에 H/S의 첫 공통 Qwen3-8B revision·decoding과 schema/renderer·parse failure 처리 명세를 고정했다. 실제 updater 구현·prompt의 실행 검증·weights/package 검증은 남아 있다. 초기에는 명시적 물체 이름을 사용해 text 의미 업데이트를 분리한다. 나중에 “그것” 같은 상황 지시를 추가하면 두 arm에 같은 이미지·history를 제공하고 별도 비교로 다룬다.

ReSteer의 `prompt` 필드는 위 결과 문자열을 받는 경로일 뿐이다. Public policy가 해당 복합 문장을 이해하는지, tokenization에서 조건이 잘리는지, 원래 task label과 문체가 달라진 영향인지는 검증해야 한다. 따라서 **처음부터 H/S 모델을 설치·학습하기보다 O/A에서 능력과 관측 경로를 확인**한다. H/S를 비교할 때는 동일 상위 모델의 호출 수·입력 길이·추론 지연을 기록한다. 선언된 동일 token cap과 실제 사용 비용은 구별한다.

의미 정확도는 목표/대상/유지/철회·유효 시간 정답과 비교한다. 행동 결과는 목표 성공과 기간별 제약 준수의 joint outcome으로 별도 기록한다. 이 둘을 비교한다고 곧바로 causal mediation이 증명되지는 않는다. O에서도 실패하면 상위 언어 문제가 아니라 continuation·제약 실행·prompt 분포·controller 차이 등이 남는다. 본 문제의 text-only 정답표만으로 VLA 논문 효과를 주장하지 않는다.

<a id="cases"></a>

<a id="cases-부분-지시-수정-수작업-사례-8개"></a>
## 부분 지시 수정: 수작업 사례 8개

- 작성: 2026-10-31 KST / GAP-REVISION1
- 성격: **연구자가 작성한 의미·평가 사례**. 공개 데이터의 실제 episode, 정책 실패 사례, 실행 가능한 benchmark가 아니다. 모델 호출·시뮬레이션 없이 작성했다.
- 연결: [공개 interface 검토와 판단](README.md#source-review), [canonical 연구 질문](../../../../synthesis/04_vla_generalist.md#gap-instruction-revision-2026), [TODO](../../../../TODO.md).
- 후속 보완: [GPU 전 의미·평가 계약](../../../update/PRE_GPU_BUILDUP_REVIEW_2026-10-31.md#instruction-revision). 제약 없는 목표·규칙형 갱신 대안, 공통 renderer, 수정 전 위반과 수정 후 비교, 비정보적 준수·기술 오류의 처리 기준을 추가했다. 아래 8개 사례의 의미는 유지하며 실제 정책 검증으로 승격하지 않는다.
- 기반 장면: [ReSteer의 공개 LIBERO 장면](https://github.com/ChenZhenY/ReSteer/blob/7329c159319a346b7245a69c128e5d4940c0763b/third_party/libero/libero/libero/bddl_files/libero_steerability/libero_goal_steerability.bddl). 아래 object 이름과 일부 goal predicate가 존재한다는 사실만 확인했으며, 복합 지시 수행 능력은 미확인이다.

<a id="cases-공통-의미와-평가-규칙"></a>
### 공통 의미와 평가 규칙

`bowl` = `akita_black_bowl_1`, `bottle` = `wine_bottle_1`, `cheese` = `cream_cheese_1`, `plate` = `plate_1`. `cabinet top`은 `wooden_cabinet_1_top_side`, `rack`은 `wine_rack_1_top_region`이다. 이전 문서의 빨간/파란 블록은 설명용 예시였으며 실제 실행 대상으로 확정하지 않았다.

- `t0`: 초기 안정화 뒤 첫 task action 직전. `τ`: 수정 발화 수신·반영 직전의 action 경계. `T`: 해당 비교의 평가 종료. 실제 step·시간·deadline은 아직 동결하지 않았다.
- `U(x,r,[a,b))`: 기준 시점 `r`의 물체 pose에서 허용 오차 이상 이동/회전하지 않았음을 구간 전체에서 확인한다. **접촉 금지와 다르다.** 위치·회전 tolerance와 측정 주기는 후속 최소 검증 전에 정한다. 시작·끝 pose만 같다고 중간 이동까지 없었다고 판정하지 않는다.
- `G(x,d)`: 최종 평가 시점에 물체 x가 목적지 d에 놓였다는 목표. 공개 `On` predicate의 기하·접촉 의미를 그대로 사용할지 명시해야 하며, 언어상 “올려놓기”와 완전히 같다고 가정하지 않는다.
- `[t0,τ)`의 위반은 이후 철회해도 남는다. `τ`에 추가한 제한은 과거에 소급하지 않는다. 각 경계에서 pre-action/post-action 상태를 일관되게 기록하고, 종료 순간도 포함해 평가한다.
- 아래 **전체 현재 지시**는 사람이 작성한 정답 조건이다. 자동 baseline에 제공하지 않는다. 자동 방법은 사용자 발화·자신의 추정 상태·동일하게 허용된 관측만 받는다.
- 한국어는 검토용이고, 최초·수정 영문 발화와 수정 전후 의미 정답은 [SEMANTIC_CASES.json](../재현%20방법/SEMANTIC_CASES.json)에 고정했다. 이는 수작업 명세이며 실행 데이터·모델 정확도 결과가 아니다. 실제 tokenizer·물리 상태·상위 updater와의 연결은 미검증이다. 기존 P0 launcher는 이 파일을 읽지 않으며 R8 IO 예산은 그대로다.
- 전체 현재 지시는 공통 renderer가 활성 목표·제약만 표현한 정답 후보다. R4/R5의 취소·허용 이력은 의미 감사에만 보존하고 VLA prompt에 추가하지 않는다. 세부 [표현·시점·종료 계약](../../../update/PRE_GPU_BUILDUP_REVIEW_2026-10-31.md#remaining-work-review)을 따른다.
- 제약 유효 구간은 **action 경계**로 해석한다. `τ` 직전 action이 만든 post-state `s_τ`는 이전 제약으로 검사한 뒤 수정 발화를 적용한다. 철회와 같은 tick에서 관측된 직전 이동을 누락하지 않는다. 이 명세가 연속 시간 전체를 관측했다는 뜻은 아니다.

<a id="cases-r1-목적지만-교체하고-기존-이동-금지를-유지"></a>
### R1. 목적지만 교체하고 기존 이동 금지를 유지

- **최초:** “그릇을 접시 위에 놓아. 병은 지금 위치에서 움직이지 마.”
- **수정:** “그릇의 목적지만 캐비닛 위로 바꿔 줘.”
- **전체 현재 지시:** `Put the bowl on top of the cabinet. Keep the wine bottle at its original position and orientation.`
- **시간별 정답:** `G(bowl,plate)`를 `τ`에 `G(bowl,cabinet top)`으로 교체. `U(bottle,t0,[t0,T])`는 유지. 취소된 접시 목표를 추가로 달성할 필요는 없다.
- **필요 능력·시점:** 그릇 접근/파지/배치, 병을 건드리지 않는 이동. 첫 후보 시점은 그릇 파지 전, 후속은 파지 후이며 실제 feasible state는 미확인이다.
- **관측·공개 연결:** `on_akita_black_bowl_1_wooden_cabinet_1_top_side`는 기존 task 5의 goal key. 병 pose의 시간별 측정은 가능성이 확인된 source 경로가 있지만 `U` evaluator는 미구현이다.
- **정보성·한계:** 병에 전혀 접근하지 않는 장면이면 제약을 무시해도 통과할 수 있다. R8과 함께 비교하고, 실패를 유도하려고 물체를 임의로 배치한 경우 자연 발생 사례와 구별한다. **핵심 탐색 사례**.

<a id="cases-r2-조작-대상을-교체하고-별도-물체의-제한을-유지"></a>
### R2. 조작 대상을 교체하고 별도 물체의 제한을 유지

- **최초:** “그릇을 캐비닛 위에 놓아. 크림치즈는 움직이지 마.”
- **수정:** “그릇 대신 병을 옮겨 줘. 목적지는 그대로야.”
- **전체 현재 지시:** `Put the wine bottle on top of the cabinet. Keep the cream cheese at its original position and orientation.`
- **시간별 정답:** `G(bowl,cabinet top)` → `G(bottle,cabinet top)`; `U(cheese,t0,[t0,T])` 유지. 그릇을 원래 위치로 돌려놓으라는 요구는 없다.
- **필요 능력·시점:** 첫 범위는 그릇 파지 전. 파지 후에는 내려놓기·재접근 능력이 추가되므로 별도 확대 조건이다.
- **관측·공개 연결:** task 8의 `on_wine_bottle_1_wooden_cabinet_1_top_side`, cheese pose. 대상 전환 자체는 ReSteer 선행과 겹친다.
- **정보성·한계:** object selection과 유지 제약을 분리할 수 있으나 R1보다 grasp 전환 교란이 크다. **확장 사례**, 첫 pilot 필수 항목은 아니다.

<a id="cases-r3-실행-도중-새로운-금지를-추가"></a>
### R3. 실행 도중 새로운 금지를 추가

- **최초:** “그릇을 캐비닛 위에 놓아.”
- **수정:** “지금부터 병은 현재 위치에서 움직이지 마.”
- **전체 현재 지시:** `Put the bowl on top of the cabinet. From now on, keep the wine bottle at its current position and orientation.`
- **시간별 정답:** 목표는 그대로. `τ`부터 `U(bottle,τ,[τ,T])` 추가. 병이 `τ` 이전에 움직였어도 이 새 제한의 위반은 아니다.
- **필요 능력·시점:** R1과 같은 조작 능력. `τ`의 병 pose를 정답 evaluator가 저장한다. 이 simulator 정답 pose를 policy에 추가 입력하지 않는다.
- **관측·공개 연결:** task 5 goal과 병 pose. 유지 제한 R1의 기준 pose `t0`와 이 사례의 `τ`를 섞지 않는다.
- **정보성·한계:** 병이 이미 계속 움직이는 상태에서는 즉시 제한 준수가 불가능할 수 있다. 정지 상태에서의 feasible witness가 필요하다. **시간 의미 확장 사례**.

<a id="cases-r4-금지를-명시적으로-철회하고-그-행동이-필요한-목표로-변경"></a>
### R4. 금지를 명시적으로 철회하고 그 행동이 필요한 목표로 변경

- **최초:** “그릇을 접시에 놓아. 병은 움직이지 마.”
- **수정:** “병을 움직이지 말라는 제한은 취소할게. 그릇 작업 대신 병을 랙 위에 놓아 줘.”
- **전체 현재 지시:** `Put the wine bottle on the rack.`
- **시간별 정답:** `U(bottle,t0,[t0,τ))`의 과거 감사는 보존하고 `τ` 이후 금지는 제거. 그릇 목표는 취소하고 `G(bottle,rack)`을 활성화한다.
- **필요 능력·시점:** 병이 랙 밖에 있고 목표 tolerance 밖에 있어야 한다. 그릇 파지 전부터 시작해 별도 rollback 요구를 피한다. 실제 병 파지·운반 능력과 도달 가능성은 미확인이다.
- **관측·공개 연결:** task 7의 `on_wine_bottle_1_wine_rack_1_top_region`. 올바른 성공은 병 이동을 요구한다. 실패만으로 “금지 기억이 남았다”고 단정하지 않고, 동일 상태의 직접 병→랙 지시와 비교한다.
- **정보성·한계:** 물체가 이미 랙 위라면 철회 효과를 행동으로 구별할 수 없어 제외 사유를 사전에 기록한다. **핵심 탐색 사례**.

<a id="cases-r5-허용만-추가하고-이동을-요구하지-않음"></a>
### R5. 허용만 추가하고 이동을 요구하지 않음

- **최초:** “그릇을 접시에 놓아. 병은 움직이지 마.”
- **수정:** “병을 움직여도 돼.”
- **전체 현재 지시:** `Put the bowl on the plate.`
- **시간별 정답:** `G(bowl,plate)` 유지. 병 금지는 `τ`에 철회하되 과거 위반은 유지한다. 병을 옮기는 새 목표는 만들지 않는다.
- **필요 능력·관측:** task 3의 `on_akita_black_bowl_1_plate_1`과 의미 업데이트 기록. 병의 이동/비이동 모두 목표와 양립할 수 있다.
- **정보성·한계:** 병이 안 움직였다는 이유로 철회 실패 처리하지 않는다. R4의 **채점 오류 방지용 의미 대조군**이며 행동적 철회 효과의 주 지표에는 넣지 않는다.

<a id="cases-r6-이미-달성한-하위-목표를-유지하며-다음-목적지를-수정"></a>
### R6. 이미 달성한 하위 목표를 유지하며 다음 목적지를 수정

- **최초:** “먼저 병을 랙에 놓고, 병이 랙 위에 있는 상태를 유지하면서 그릇을 접시에 놓아.”
- **수정:** “그릇의 목적지만 캐비닛 위로 바꿔 줘.”
- **전체 현재 지시:** `Put the bowl on top of the cabinet while keeping the wine bottle on the rack.`
- **시간별 정답:** 앞선 행동으로 병→랙이 달성된 뒤를 `τ`로 정한다. `G(bowl,plate)` → `G(bowl,cabinet top)`. 병→랙의 관계가 달성된 시점부터 `T`까지 유지되어야 한다. 랙 안에서 허용되는 작은 움직임까지 금지하는 R1의 pose 불변 조건과 다르다.
- **필요 능력·관측:** task 7을 실제 완료한 prefix와 task 5의 continuation. 매 step의 bottle-on-rack predicate 및 bowl 최종 predicate가 필요하다.
- **정보성·한계:** 이미 완성된 장면을 임의로 로드한 사례와 실제 prefix가 만든 상태를 구분한다. 병이 떨어질 수 있는 상태에서 유지 능력을 따로 확인해야 한다. **후속 복합 목표 사례**.

<a id="cases-r7-의미가-바뀌지-않는-재진술"></a>
### R7. 의미가 바뀌지 않는 재진술

- **최초:** “그릇을 접시에 놓아. 병은 움직이지 마.”
- **수정:** “그릇은 여전히 접시 위에 두면 돼.”
- **전체 현재 지시:** `Put the bowl on the plate. Keep the wine bottle at its original position and orientation.`
- **시간별 정답:** 목표와 `U(bottle,t0,[t0,T])` 모두 유지. 기존 금지를 되풀이하지 않았다는 이유로 제거하지 않는다.
- **필요 능력·관측:** R1과 같은 actor·pose 기록, 최종 goal은 task 3. R1과 동일한 source prefix에서 branch하는 대조 조건으로 설계한다.
- **정보성·한계:** 재질의·action queue 초기화·언어 길이 변화 자체의 영향을 볼 **재진술 대조군**이다. 단 한 문장의 무효과로 paraphrase robustness를 일반화하지 않는다.

<a id="cases-r8-기존-보호-제약이-없는-목적지-전환"></a>
### R8. 기존 보호 제약이 없는 목적지 전환

- **최초:** “그릇을 접시에 놓아.”
- **수정:** “그릇의 목적지만 캐비닛 위로 바꿔 줘.”
- **전체 현재 지시:** `Put the bowl on top of the cabinet.`
- **시간별 정답:** task 3 → task 5. 병 금지는 원래 없고 새로 생성해서도 안 된다.
- **필요 능력·관측:** 기존 goal keys와 단순 instruction switch. 첫 범위는 그릇 파지 전이며 prompt·queue 변경 후의 직접 실행을 확인할 수 있다.
- **정보성·한계:** **기본 switching/continuation 대조군**이다. ReSteer가 이미 다루는 task 전환 범위이며 독립 새 기여가 아니다. 자연 rollout을 각자 시작하면 R1과 같은 prefix가 보장되지 않으므로 paired 비교는 명시적으로 상태를 공유해야 한다.

<a id="cases-이번-선정과-정답표의-한계"></a>
### 이번 선정과 정답표의 한계

첫 native 검증 후보는 **R8의 기본 입출력/전환**, 그다음 **R1·R4의 정확한 전체 지시 조건**이다. 비교를 확대할 때 R7과 R4의 직접 병→랙 지시를 대조군으로 사용한다. R5는 반드시 의미 검수에 포함하되 행동 성능 표의 철회 실패 분모에 섞지 않는다. R2·R3·R6는 첫 실행에 모두 넣지 않는다.

8개 사례는 서로 독립적인 실험 표본 8개가 아니다. 겹치는 source prefix와 task가 있고, 수작업 정답은 다른 사람이 검수한 정답도 아니다. 지금 확인한 것은 의미 계약의 논리와 source 연결이며 **실제 feasible state, 정책 역량, 자연 실패 빈도, statistical power는 모두 미확인**이다. 평가 정답의 시간 정보·simulator pose·goal key는 자동 baseline과 policy 입력에서 분리한다.
