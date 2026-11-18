# TODO — 현재 선택과 다음 행동

Updated: 2026-11-18 KST. 연구 후보 판단은 [통합 index](./work/research_topics/README.md), 논문 읽기 순서는 [READING_PLAN](./research/READING_PLAN.md)이 관리한다.

## 직전 완료

- **REG-R18 — 정합 검증·게시 준비:** [직접 선행3편/15노트와 registry 정리](./work/update/REGISTRY_MAINTENANCE_2026-11-18.md#reg-r18). Geometry Impact의 ECCV2026 정식 출판 확인, EDI·PRISM Precision Forcing은 preprint. 전체1,227편·CORE50/NEXT427/REFERENCE508/ARCHIVE242. 사용자 읽기 기록과 기존 연구 판단 보존.
- **TASK-GEOMETRY-P0-PREP — DONE (준비 범위):** [Depth override·scene/strict loader·2지시×4조건·Docker recipe·검사11개](./work/research_topics/task_geometry_estimation/재현%20방법/README.md#resume) 작성. 정적 컴파일 확인, 새 launcher는 **BLOCKED_DAEMON / exit3**. Docker 검사/native/학습/host 설치0. [내용·한계](./work/research_topics/task_geometry_estimation/내용/README.md#p0-preparation-result), [원장](./work/sources/new_field_scout_2026-11-17.json). 다음은 호환 local NVIDIA의 bounded P0다.

N1/N2의 문헌·설계, POSE-ACTIVE·관계 기반 탐색의 준비, REG-R17 등록·게시와 후보 폐기 이력은 [update index](./work/update/README.md)와 각 주제 문서에 보존한다. TODO에는 최근 완료·다음 행동·재개 조건만 유지한다.

## 다음 TODO

| ID | 상태 | 구체 행동·종료 산출물 |
|---|---|---|
| **TASK-GEOMETRY-P0** | **NATIVE_RESOURCE_WAIT; PREPARED_UNEXECUTED** | [launcher check/run](./work/research_topics/task_geometry_estimation/재현%20방법/README.md#resume)으로 현재 local endpoint·daemon·GPU/BF16/EGL을 확인하고 조건 충족 시 Docker 검사11개·scene·payload/strict loader·depth 개입 IO 실행. Scene1·camera1·지시2·geometry4·query≤8/AR≤96·physics≤10,000·VLA physical command0/optimizer0. 실패 단계 기록; 입력 진단을 task 성공이나 학습 효과로 세지 않음 |
| **POSE-ACTIVE-P0** | **NATIVE_RESOURCE_WAIT; PREPARED_UNEXECUTED** | 호환 NVIDIA 컴퓨터에서 [launcher check/run](./work/research_topics/pose_active_perception/재현%20방법/README.md#resume)으로 현재 local endpoint·daemon·GPU/CUDA/EGL을 확인한다. 조건 충족 시 image build·Docker 제어10검사·payload hash·scene/evaluator·고정 camera/제한된 복원·VLA loader/12-token 후보/순차 재채점 검사. Scene1·지시2·view≤2·pose≤2·지시별 candidate≤2, 전역 control≤20/physics≤10,000/AR step≤96/register0/optimizer0. Task normalizer 없음: VLA physical command 금지. Native 실패 원인 보존; label dataset·SFT·학습 자동 시작 금지 |
| **GAP-RELATION-EXPLORE-P0** | **NATIVE_RESOURCE_WAIT; PREPARED_UNEXECUTED** | 호환 NVIDIA 컴퓨터에서 [launcher check/run](./work/research_topics/relation_exploration/재현%20방법/README.md#resume)으로 로컬 endpoint·daemon·GPU/CUDA/graphics를 새로 확인한다. 조건 충족 시 image build·Docker 제어 검사·payload hash·strict loader/IO·actual q/FK/contact·동일 ξ/u 재채점, 선택적 backward1회까지 실행한다. Query≤3/replay≤3/command≤3/backward≤1/optimizer0; setup≤6·physics≤33,000. FK는 관측당25/총75회로 명확화했다. Native 호환 실패 시 원인을 보존하며 자동 SFT·다른 checkpoint·큰 sweep으로 전환하지 않는다 |

현재 선택은 **TASK-GEOMETRY(2번)의 작은 P0 native 검증 대기**다. N1 내부 비실험 검토와 제한된 P0 코드 준비를 마쳤고, 이번 새 launcher에서도 local daemon 실패를 확인했다. GPU 조건이 맞는 컴퓨터에서 위 bounded P0를 재개한다. 전체 task evaluator·normalizer·기본 능력·학습은 별도 미구현/미확인이다. POSE-ACTIVE의 기존 N1/N2·P0 준비는 보존한다. [원장 task_geometry_p0_preparation](./work/sources/new_field_scout_2026-11-17.json). 새 문헌 보고서를 반복하지 않으며 준비를 효과 입증으로 승격하지 않는다.

앞선 관계 기반 탐색은 **비실험 계약·P0 구현 준비 완료, native 검증 대기**를 유지한다. Portable recipe·adapter·launcher·제어 검사 코드는 있지만 실제 확인은 host launcher의 daemon 실패 차단과 정적 검사까지다. Image/package·payload·checkpoint 의미 호환·FK/contact·gradient는 미검증이고, 전체 task evaluator·deterministic controller·PPO trainer/critic은 미구현이다. [기존 원장 relation_p0_preparation](./work/sources/new_field_scout_2026-11-17.json)과 [내용](./work/research_topics/relation_exploration/내용/README.md)을 보존한다. **GAP-RELIABILITY-N1은 DEFERRED**, 폐기7개와 C/D/E의 기존 판단도 유지한다. 자원 부족과 연구 가설 반증을 혼동하지 않는다.

## 유지한 실행 준비 — 자원과 구현은 별도

다음은 새 주제의 비실험 탐색과 별도로 보존한 조건부 실행 후속이다. 재개 요청 시 현재 사용자 컴퓨터의 **로컬 Docker** endpoint·daemon·architecture·NVIDIA/CUDA/graphics를 새로 확인한다. 조건이 맞으면 정해진 최소 실행 검증까지 진행하고, 맞지 않으면 clone 재개 자료를 보완한다. 과거 Mac의 실패를 현재 측정으로 쓰지 않는다.

| 후보·후속 | 준비 완료 / 실제 확인 | 남은 조건·범위 |
|---|---|---|
| **단일 VLA RL — LANGRET P0** | 전용 recipe·source/checkpoint metadata·paired IO·launcher 작성. 11/12 Docker 제어22검사 | 호환 NVIDIA에서 native image/payload·IO·gradient·목표별 기본 능력 확인. [재개 명령과 상한](./work/research_topics/unified_vla_rl/재현%20방법/README.md#langret-p0-preparation). 큰 학습은 별도이며 기존 U1을 동시에 실행하지 않음 |
| **접촉 적응 — CONTACT P0-A** | Physics recipe·gain/sensor probe·launcher 작성. 11/09 Docker stdlib16검사 | Native physics/RGB/sensor/gain·asset 검증. [재개 명령과 P0-A/B 구분](./work/research_topics/contact_adaptation/재현%20방법/README.md#resume). P0-A는 VLA 효과·전체 학습 환경 검증이 아님 |
| **시각 피드백 — FEEDBACK P0** | Loader/asset pin·adapter 초안·launcher 작성. 11/06 Docker CPU 제어9검사 | Native build/IO·payload·CUDA/BF16/Vulkan 교정. reset2·query3·control6·event1·physics2,000 상한. [재개 명령](./work/research_topics/visual_feedback/재현%20방법/README.md#resume). 전체 상태 분기·성공률·새 failure monitor는 미구현 |
| **부분 지시 수정 — 예비** | 기존 recipe·R8 IO probe·환경 명세 보존 | 현 탐색의 자동 실행 대상 아님. 선택 시 [기존 준비/미구현 경계](./work/research_topics/instruction_revision/재현%20방법/README.md#execution)부터 확인 |

현재 유지 후보들의 실제 native 정책 효과와 독립 외부 연구자 피드백은 미확인이다. 질문 준비를 피드백 수신으로 세지 않으며 사용자 지시 없이 타인에게 메시지를 보내지 않는다.

## 폐기·과거 보류

CODEC1·RETRIEVAL·SET·HANDOFF·ALLOC·HINDSIGHT·VRL은 **RETIRED**이며 실험 대기에서 제거했다. [핵심 결과·이유](./work/research_topics/retired/README.md). GPU 확보로 자동 재개하지 않는다.

그 이전 16개 후보의 C/D/E·초기 RL 전이·RP-2/RP-3 판단은 [역사 요약](./work/research_candidates/summaries/README.md)을 따른다. TERM/AUTH/관측 계약 등 과거 gate는 [폐기 전 TODO](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/5bec2cfa8a31758ca8e5be9c19c39dc4c23bb096/TODO.md)와 [완료 이력](./work/update/README.md)에 남는다. 현재 실행 queue로 간주하지 않는다. [C3 portable replay](./work/experiments/portable/README.md)는 저장 진단의 재분석이며 새로운 정책 효과 실험이 아니다.

## 갱신 규칙

`DONE`은 해당 작업 완료, `READY_NONEXPERIMENTAL`은 문헌·source 검토 가능, `READY_IMPLEMENTATION`은 명세 후 구현 가능, 실행의 자원/구현 대기는 각각 미확인 조건을 뜻한다. `RETIRED`는 현재 설계에 대한 투자 종료다. 준비 자료·실제 실행·연구 효과를 분리하고 긴 작업 이력은 [update index](./work/update/README.md)에 연결한다. 운영 참고: [GitHub Issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/about-issues), [The Turing Way](https://github.com/the-turing-way/the-turing-way/blob/main/ways_of_working.md).
