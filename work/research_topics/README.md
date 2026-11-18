# 현재 연구 후보 — 유지 3개·예비 1개와 추가 탐색

Updated: 2026-11-18 KST. 큰 줄기는 **VLA + RL + Computer Vision + Robotics**다. 최신 사용자 지정의 **pose estimation·active perception / 3D reconstruction·estimation**을 [추가 탐색](../update/NEW_FIELD_SCOUT_2026-11-17.md#pose-reconstruction)했다. 새 두 후보 중 POSE-ACTIVE-N1/N2·P0 코드 준비를 완료했고 현재 local daemon 실패로 제한된 native 검증을 대기한다. 앞선 **접촉 관계 기반 RL 탐색**은 N1/N2·P0 코드 작성 후 native 검증 대기를 유지한다. 아래 보존 후보·실행 준비·초기 질문의 성숙도를 구별한다. 기존 7개 [폐기 판정](./retired/README.md)은 유지한다. [11/18 registry 보강](../update/REGISTRY_MAINTENANCE_2026-11-18.md)으로 전체1,224편과 직접 선행의 읽기 우선순위를 갱신했으며 연구 후보 성숙도는 바꾸지 않았다.

아래는 석사 연구에 투자할 상대적 판단이다. 유지가 신규성·성능·출판 가능성의 입증은 아니며, 폐기도 실험적 반증은 아니다. GPU 부재로 탈락시키지 않았다. 선행 대비 남는 기여, 실제 로봇 행동과의 연결, 강한 단순 대안, 구현·검증 부담을 함께 비교했다. 작은 탐색에 완성된 결과를 요구하지 않는다.

<a id="candidate-priority"></a>
<a id="masters-publication-comparison"></a>

## 현재 투자 판단

| 역할 | 질문과 남기는 이유 | 가장 큰 위험·다음 유효 증거 | 내용 / 재현 방법 |
|---|---|---|---|
| **유지·후속 보류: 시각 피드백·실패 원인** | 새 관측의 행동상 가치와 RL 후학습의 관계를 분석한다. 사용자가 강조한 시각 신뢰성·복구 문제로 이어갈 기반이 있다 | 일반 실패 탐지·온라인 보정은 선행과 중복. 전체 영상 지연은 순수 물체 인식 오류가 아니며 공개 RL/SFT 차이는 인과효과가 아님. 최신 요청에 따라 이번 후속 대신 새 분야를 탐색 | [질문·최신 선행](./visual_feedback/내용/README.md#reliability-scout-2026) / [기존 FEEDBACK P0](./visual_feedback/재현%20방법/README.md#resume) |
| **유지: 단일 VLA RL의 지시별 행동 보존** | 보상으로 성능을 올릴 때 언어에 따른 행동 구분이 보존되는 조건. 단일 정책 내부 RL과 직접 연결되고 목표별 비교가 구체적 | 일반 actor–critic 간섭이나 KL·데이터 조정으로 설명될 수 있음. LANGRET의 native IO·초기 목표별 능력과 단순 대안 비교가 남음 | [LANGRET·U1](./unified_vla_rl/내용/README.md#langret-n2) / [LANGRET P0](./unified_vla_rl/재현%20방법/README.md#langret-p0-preparation) |
| **유지: 접촉 적응** | 한 VLA에서 동작과 관절 강성 배율을 RL로 함께 학습해 삽입 저항 변화에 적응하는가. 접촉 행동에 직접 연결되는 방법 후보 | 동작+강성/RL의 조합 자체는 선행에 있음. Force-rule·고정 gain 대비 차이, physics/sensor/controller의 타당성·실제 로봇 검증 부담 | [좁힌 질문·비교](./contact_adaptation/내용/README.md) / [CONTACT P0](./contact_adaptation/재현%20방법/README.md#resume) |
| **예비: 부분 지시 수정** | 여러 수정 뒤 유지할 제약과 철회할 제약의 공동 이행. 의미 갱신 오류와 행동 능력 오류를 나누는 평가가 비교적 명확 | RL은 현재 필수가 아니며 ReSteer/BAS-VLA 및 이력 재작성·규칙 대조 이후 차이가 남아야 함. 당장 실행 queue에 올리지 않음 | [질문·비실험 설계](./instruction_revision/내용/README.md) / [보존한 준비 자료](./instruction_revision/재현%20방법/README.md) |

세 유지 후보 모두 native 정책 효과는 미확인이다. 과거 Docker 제어 검사는 실행 준비의 일부일 뿐이다. LANGRET·CONTACT·FEEDBACK의 기존 실행 상한과 미구현 항목은 각 재현 문서가 소유한다. U1은 UNIFIED 안의 과거 대안으로 보존하며 다섯 번째 활성 후보로 세지 않는다. 새 질문에 기존 FEEDBACK adapter를 그대로 쓸 수 있다고 가정하지 않는다.

## 새로운 분야의 초기 후보 — 기존 실행 대기와 별도

| 현재 선택 | 기여 가설·가장 큰 불확실성 | 근거와 다음 행동 |
|---|---|---|
| **새 분야 우선 탐색: 작업에 필요한 물체 자세의 능동 관측** | 여러 pose 가설에서도 성공할 공통 행동이 있는지 학습해 유효한 행동 다양성과 관측 부족을 구별. DISaM·ATAP·허용 오차 기반 성공 평가 이후 차이가 남아야 함 | [내용](./pose_active_perception/내용/README.md) / [재현 전 확인](./pose_active_perception/재현%20방법/README.md). N1/N2·Docker P0 recipe/scene·후보 IO probe 작성. Local daemon 실패(exit3), Docker 검사/native 실행0. Task 통계·기본 능력·전체 label/head 미확보. 다음 호환 NVIDIA P0; 공유 VLA 학습의 이득 미확인 |
| **새 분야 2순위: 조작 허용 오차를 반영하는 3D 추정** | 같은 평균 3D 오차에서 위치·방향·원인별 행동 실패를 설명하는 표현/학습. Robo3R·GeoPredict·PRISM·ROI/tolerance rule 이후 차이 미확인 | [내용](./task_geometry_estimation/내용/README.md) / [재현 전 확인](./task_geometry_estimation/재현%20방법/README.md). SpatialVLA depth 입력 지점은 교차 확인. 개입 adapter·좌표 정합·task evaluator가 남음. 1번보다 어렵다고 단정하지 않음. 초기 탐색, GPU 대기 주제 아님 |
| **P0 코드 준비·탐색 계속: 접촉 관계 기반 탐색 분포** | VLA feature와 실제 관절 상태에서 양팔 상대 운동의 결합 weight를 학습. Lattice와 RL-SCT phase 전환 이후 차이를 보기 위해 큰 relation graph를 축소. Generic covariance·수작업 rule 대비 효과 미확인 | [내용·기여·비교](./relation_exploration/내용/README.md) / [source·재현 조건](./relation_exploration/재현%20방법/README.md). N2 계약·portable P0 코드 작성. 다음 P0: native loader/IO/FK/contact/선택적 gradient; launcher는 daemon 연결 실패(exit3), native 미실행 |

모두 **CURATION-HYPOTHESIS**다. POSE-ACTIVE는 N1/N2 내부 문헌·source·비교 명세를 마쳤고, TASK-GEOMETRY는 초기 탐색·일부 입력 경로 확인까지 진행했다. 소규모 탐색을 시작할 여지는 있지만 신규성이나 top-tier 출판 가능성을 확정하지 않았다. POSE-ACTIVE의 우선순위는 질문 구체화 순서다. 구현이 더 쉽거나 연구 잠재력·효과가 더 높다고 입증한 순위는 아니다. 관계 기반 탐색과 POSE-ACTIVE는 현재 범위의 N1/N2·제한된 P0 코드 작성을 마쳤고, 각 checkpoint/image/native 호환·효과는 미확인이다. 상세 내용은 주제별 두 폴더, 출처는 기존 공통 JSON을 사용한다. R1의 [카메라 장착 적응](../update/NEW_FIELD_SCOUT_2026-11-17.md#camera)·[환경별 RL 병합](../update/NEW_FIELD_SCOUT_2026-11-17.md#merge)은 현재 선택에서 제외한 판단을 유지한다. 새 object pose 질문을 과거 손목 장착 적응이나 C1/D3의 자동 재개로 해석하지 않는다. 다음 행동은 [TODO](../../TODO.md)가 소유한다.

## 폐기한 7개

| 기존 주제 | 이번 폐기 판단 |
|---|---|
| [행동 토큰화](./retired/README.md#action_tokenization) | 실제 결과가 제한된 복원 진단이며 로봇 정책·방법 선택을 바꾸는 기여가 약함 |
| [시연 검색](./retired/README.md#context_retrieval) | 선행 이후 차이가 좁고 시연 provenance·native 입력 확보 부담이 큼 |
| [집합·수량 지시](./retired/README.md#object_set) | 반복·counter 이후 차이가 미확인이고 benchmark/evaluator 구축 비중이 큼 |
| [모바일 정책 교체](./retired/README.md#mobile_policy_transfer) | 좁은 전이 질문에 비해 mobile stack·상태 분기·일반화 검증 부담이 큼 |
| [과제 배분](./retired/README.md#task_allocation) | 일반 RL sampling/weighting 문제에 가까우며 현 설계의 로봇·비전 기여가 약함 |
| [Hindsight 목표 선택](./retired/README.md#hindsight_transfer) | LfH 이후 남는 차이에 비해 목표 유효성·전이·학습 비교 부담이 큼 |
| [Residual 재사용](./retired/README.md#vla_residual_update) | A에서 보정 학습 후 B 적응까지 필요하며 warm-start·gain·모방 대비 기여가 불확실 |

이 분야들을 영구 금지하는 판단은 아니다. 같은 설계에 GPU만 추가해 자동 재개하지 않고, 다른 중요한 로봇 문제나 판단을 바꾸는 근거가 생기면 새 후보로 비교한다. 실제 결과·계약 7파일은 폐기 요약 아래 보존했고 실행 코드·dependency recipe·중복 문서는 제거했다. 원래 상세 기록은 요약의 고정 Git commit 링크로 추적할 수 있다.

## 파일 운영

유지·예비 주제는 `내용/README.md`와 `재현 방법/README.md`에 통합한다. Source는 기존 단일 원장을 사용하고 필요한 코드·계약·원시 결과는 재현 폴더에 둔다. 새 brief·날짜별 주제 문서를 늘리지 않는다. `retired/`는 다섯 번째 연구 후보가 아니라 7개 폐기 판단과 핵심 증거의 보관 위치다.

[검색 용어·검색식](../../research/IDEA_BUILDUP_GUIDE.md#search-map-2026-11-17), [7개 synthesis](../../synthesis/README.md), [이전 16개 후보 요약](../research_candidates/summaries/README.md), [원래 이관 기록](./ORGANIZATION.json)을 함께 사용한다. 이전 C/D/E의 HOLD/NO-GO는 이번 정리로 바뀌지 않는다.

<a id="nonexperimental-process-audit"></a>
<a id="additional-gaps-2026-11-09"></a>
<a id="hindsight-exploration"></a>

## 과거 비교의 위치

11/04의 [6개 비실험 감사](../update/SIX_CANDIDATE_BUILDUP_STATE_2026-11-04.md), 11/09의 [추가 공백 조사](../update/VLA_RL_ADDITIONAL_GAPS_2026-11-09.md)는 당시 기록이다. 11/07의 8개 순위와 HINDSIGHT·ALLOC의 실행 대기를 현재 계획으로 사용하지 않는다. 중복된 현황 표는 이 문서에서 제거했고 [폐기 전 index](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/5bec2cfa8a31758ca8e5be9c19c39dc4c23bb096/work/research_topics/README.md)에 보존되어 있다.
