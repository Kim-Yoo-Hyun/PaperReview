# TODO — 현재 선택과 다음 행동

Updated: 2026-11-18 KST. 연구 후보 판단은 [통합 index](./work/research_topics/README.md), 논문 읽기 순서는 [READING_PLAN](./research/READING_PLAN.md)이 관리한다.

## 직전 완료

- **REG-R17 — registry 갱신·게시 준비:** [직접 선행18편/90노트 보강 및 정합 검토](./work/update/REGISTRY_MAINTENANCE_2026-11-18.md). ActiveAlign 중복 제외, SaPaVe·ActiveAlign NEXT 승격, 사용자 읽기 이력·실험 대기/폐기 판단 보존. 최종 GitHub 게시 확인은 해당 보고서를 따른다.

- **POSE-ACTIVE-P0-PREP — DONE (준비 범위):** [Docker recipe·PLAN·launcher·scene/evaluator·camera/제한된 복원·VLA 12-token 후보/순차 재채점·제어 검사10개](./work/research_topics/pose_active_perception/재현%20방법/README.md#p0-preparation)를 작성했다. Python 정적 컴파일 확인. 새 launcher의 실제 `run`은 현재 local daemon 연결 실패로 **BLOCKED_DAEMON / exit3**. Image build·Docker 검사·native 실행·host package/weight/asset 설치는 없다. VLA physical command는 task normalizer 부재로 차단하며 FoundationPose·물리 camera·전체 label/학습은 미구현이다. [판정](./work/research_topics/pose_active_perception/내용/README.md#p0-preparation-result)은 좁은 탐색 CONTINUE·효과/신규성 미확립. 다음은 호환 local NVIDIA의 bounded P0다.

- **POSE-ACTIVE-N2 — DONE (비실험 비교 명세):** SpatialVLA의 실제 4-step/12-token 설정과 source를 확인해 후보 생성·개별 decode·누출 없는 순차 재채점, FoundationPose 집합 갱신, 같은 물체의 PLACE/ALIGN evaluator와 counterfactual label, 정보/비용/분할을 [계약](./work/research_topics/pose_active_perception/재현%20방법/README.md#n2-contract)으로 구체화했다. 같은 RGB 복제를 pose별 action KL로 부르지 않고 명시적 학습 comparator로 수정했다. 추가 task-sufficiency preprint는 개념 제안/예정 평가로 구별했다. [판정](./work/research_topics/pose_active_perception/내용/README.md#n2-result): 좁은 탐색 CONTINUE, 현재 범위의 내부 비실험 검토 종료. 새 scene·normalizer·VLA task 능력·효과는 미확보. 당시 다음 P0-PREP는 구현 준비였으며 실제 작성 결과는 위 완료 항목에 기록했다. 실험·설치·신규 등록·읽기 상태 변경 없음.

- **POSE-ACTIVE-N1 — DONE (비실험):** DISaM·ATAP·Naik의 objective와 ActiveAlign·EyeRobot 비교 경계를 확인하고 네 논리 사례 및 6개 공개 repo의 source/README/XML 27개를 검토했다. **REVISE 후 좁은 탐색 CONTINUE.** 불확실성을 남긴 관측 중단 원리는 기존에 있고, DISaM은 원시 행동 분산이 아닌 분포 간 KL이므로 valid multimodality를 자동 실패 사례로 보지 않는다. [내용·판정](./work/research_topics/pose_active_perception/내용/README.md#n1-result) / [source·미구현 경계](./work/research_topics/pose_active_perception/재현%20방법/README.md#n1-source-audit). 1번이 더 쉽다는 초기 판단은 유보하고 2번의 SpatialVLA depth 개입 경로도 반영했다. Native 실행·설치·신규 paper 등록·reading status 변경 없음. 다음 N2는 아직 비실험 계약 작업이다.

- **POSE-RECON-SCOUT — DONE (추가 주제 탐색):** 사용자 지정 pose estimation·active perception·3D reconstruction·VLA·Robotics를 기존 registry와 외부 논문 **20편**으로 대조했다. 2024–2026 공식 proceedings/publisher와 venue 미확인 preprint를 구별하고, [물체 자세의 행동 양립성에 따른 능동 관측](./work/research_topics/pose_active_perception/내용/README.md)을 우선 후보, [조작 허용 오차를 반영하는 3D 추정](./work/research_topics/task_geometry_estimation/내용/README.md)을 두 번째 후보로 정리했다. DISaM·ATAP·Naik·Robo3R·GeoPredict·PRISM과의 중복을 반영했다. **초기 후보이며 비실험 buildup 전체 완료·독립 신규성·실행 효과는 미확립.** 각 두 폴더 구성, 공통 source 원장 기록. 논문 등록/읽기 상태 변경·실험·설치 없음.

- **GAP-RELATION-EXPLORE-P0-PREP — DONE (준비 범위):** [Docker recipe·PLAN·launcher·actor/FK/contact adapter·제어 검사9개](./work/research_topics/relation_exploration/재현%20방법/README.md#p0-preparation)를 작성하고 Python 정적 검사를 수행했다. Source/image metadata pin·clone 재개 명령·전역 상한·중단 조건을 반영했다. 새 launcher는 현재 로컬 daemon 연결 실패로 **BLOCKED_DAEMON / exit3**. **Image build·Docker 검사9개·native 정책/physics/gradient는 미실행**이며 host package/weight/asset 설치도 없다. [연구 판단](./work/research_topics/relation_exploration/내용/README.md#p0-preparation-result)은 좁은 탐색 CONTINUE, 효과·신규성 미확립이다.

- **GAP-RELATION-EXPLORE-N2 — DONE:** π₀.₅ 재구성 loader·quantile/state-token·14D 행동 변환·실제 qpos/TCP·접촉 사건·시간/로그·최초 P0 상한을 [계약](./work/research_topics/relation_exploration/재현%20방법/README.md#n2-interface)으로 고정했다. 원 Motus fork/weight 호환은 미확정이므로 strict load/IO를 먼저 확인하고 실패 시 공통 SFT 경로로 전환한다. RL 경로의 정지 잡음·downsampling과 no-grad 추론 경계도 반영했다. **로컬 Docker daemon 연결 실패 확인, native 실행0·학습0.** [연구 판단](./work/research_topics/relation_exploration/내용/README.md#n2-result): 탐색 CONTINUE, 기여/효과 미확립.
- **GAP-RELATION-EXPLORE-N1 — DONE:** 직접 선행·공개 코드·세 양팔 task·checkpoint/asset metadata를 대조했다. RL-SCT의 phase 전환과 Lattice의 learned covariance 때문에 **설계 REVISE 후 좁은 탐색 CONTINUE**로 판정했다. Main contribution은 영상/지시/상태로 양팔 결합 weight를 학습하는 actor로 한정한다. [내용·기여·비교 설계](./work/research_topics/relation_exploration/내용/README.md) / [source·입출력·실행 조건](./work/research_topics/relation_exploration/재현%20방법/README.md). Native 실행·효과·외부 피드백 미확인.
- **NEW-FIELD-SCOUT-R1/R2 — DONE:** 앞선 카메라 적응·정책 병합은 현재 선택에서 제외하고 [공통 선정 이력](./work/update/NEW_FIELD_SCOUT_2026-11-17.md)에 보존했다. 관계 기반 탐색의 상세 내용은 위 두 폴더로 통합했다.
- **CANDIDATE-TRIAGE-R2 — DONE:** 기존 11개 후보를 비교해 **3개 유지·1개 예비·7개 폐기**. 폐기는 투자 판단이며 가설 반증이 아니다. 7개 주제의 실행 코드·recipe·반복 문서를 제거하고 핵심 증거를 압축 보존했다. [폐기 이유](./work/research_topics/retired/README.md) · [정리와 검증](./work/update/CANDIDATE_TRIAGE_2026-11-17.md).
- **RELIABILITY-SCOUT — 범위 제한 문헌 확인 완료:** Sentinel·SAFE·AHA·FAIL-Detect 및 최신 preprint의 이미 해결한 문제를 대조했다. AHEAD·B2FF·SFF의 지정 한계/실험 절을 확인했고, 탐지·보정·복구를 새 조합만으로 기여라고 부르지 않도록 [탐색 질문](./work/research_topics/visual_feedback/내용/README.md#reliability-scout-2026)에 반영했다. 새 공백 확정·코드 확인·실험은 미완료다.
- **현재 registry:** REG-R17 이후 1,224편·6,120노트, CORE50/NEXT424/REFERENCE508/ARCHIVE242. 사용자 읽기 상태는 보존하며 신규 집중 읽기는 UNREAD다.

## 다음 TODO

| ID | 상태 | 구체 행동·종료 산출물 |
|---|---|---|
| **POSE-ACTIVE-P0** | **NATIVE_RESOURCE_WAIT; PREPARED_UNEXECUTED** | 호환 NVIDIA 컴퓨터에서 [launcher check/run](./work/research_topics/pose_active_perception/재현%20방법/README.md#resume)으로 현재 local endpoint·daemon·GPU/CUDA/EGL을 확인한다. 조건 충족 시 image build·Docker 제어10검사·payload hash·scene/evaluator·고정 camera/제한된 복원·VLA loader/12-token 후보/순차 재채점 검사. Scene1·지시2·view≤2·pose≤2·지시별 candidate≤2, 전역 control≤20/physics≤10,000/AR step≤96/register0/optimizer0. Task normalizer 없음: VLA physical command 금지. Native 실패 원인 보존; label dataset·SFT·학습 자동 시작 금지 |
| **TASK-GEOMETRY-N1** | **INITIAL_EXPLORATION — 후순위** | [3D 추정 후보](./work/research_topics/task_geometry_estimation/내용/README.md)의 SpatialVLA depth 입력 지점은 N1에서 부분 확인했다. 개입 adapter·좌표/scale·local shape/camera/pose 분리와 evaluator를 더 확인한다. GeoPredict·PRISM·단순 ROI/tolerance 대조 이후 차이가 있어야 방법 설계로 확장. 현재 실행 recipe 없음 |
| **GAP-RELATION-EXPLORE-P0** | **NATIVE_RESOURCE_WAIT; PREPARED_UNEXECUTED** | 호환 NVIDIA 컴퓨터에서 [launcher check/run](./work/research_topics/relation_exploration/재현%20방법/README.md#resume)으로 로컬 endpoint·daemon·GPU/CUDA/graphics를 새로 확인한다. 조건 충족 시 image build·Docker 제어 검사·payload hash·strict loader/IO·actual q/FK/contact·동일 ξ/u 재채점, 선택적 backward1회까지 실행한다. Query≤3/replay≤3/command≤3/backward≤1/optimizer0; setup≤6·physics≤33,000. FK는 관측당25/총75회로 명확화했다. Native 호환 실패 시 원인을 보존하며 자동 SFT·다른 checkpoint·큰 sweep으로 전환하지 않는다 |

현재 선택은 **POSE-ACTIVE의 작은 P0 native 검증 대기**다. N1/N2와 P0 코드 준비를 마쳤으며 추가 문서 단계 N3를 자동 반복하지 않는다. POSE-ACTIVE·관계 탐색의 제한된 IO/fixture 준비를 전체 task 실험 준비나 효과 확인으로 세지 않는다. TASK-GEOMETRY는 초기 탐색을 유지한다. 11/17에 read-only local Docker 확인만 수행했고 실험은 없었다. 11/18 유지보수에서는 환경을 재측정하지 않았다. 근거는 [원장 pose_active_p0_preparation](./work/sources/new_field_scout_2026-11-17.json)에 둔다.

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
