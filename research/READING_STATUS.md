# 읽기 상태

정독 대상은 CORE와 NEXT다. 현재 500편의 순서와 등급은 읽기 계획에서 확인한다. 집중 읽기 대상에서 빠진 논문의 개인 기록은 이력 파일에 보관하고 재편입하면 복원한다. [읽기 계획](./READING_PLAN.md) · [현재 읽기 기록](./READING_STATUS.csv) · [이전 기록](./READING_STATUS_HISTORY.csv)

## Status

| Status | Meaning | Minimum evidence |
|---|---|---|
| `UNREAD` | 아직 읽기 시작하지 않음 | 없음 |
| `SKIMMED` | 문제, 기여, 주요 그림과 실험 구조를 파악함 | `problem_and_assumptions`, `next_action` |
| `READ` | 방법과 실험을 정독함 | 핵심 분석 필드와 failure mode 작성 |
| `SYNTHESIZED` | 같은 트랙의 논문과 비교까지 완료함 | synthesis comparison matrix와 `Open Questions` 갱신 |
| `REPRODUCED` | 코드 실행 또는 핵심 실험 재현 완료 | 재현 조건과 결과를 `personal_notes`에 기록 |

`REPRODUCED`는 필수 최종 단계가 아니다. 이론·시스템 논문은 `SYNTHESIZED`에서 완료될 수 있다.

## Evidence Level

읽기 진행도와 주장 근거 수준은 별개로 관리한다. 노트 파일이나 로컬 PDF가 있다는 사실만으로 evidence level을 올리지 않는다.

| Evidence level | Meaning | 허용되는 사용 |
|---|---|---|
| `CURATION_ONLY` | metadata, 공식 abstract/project cue 또는 읽기 전 구조화만 있음 | 읽기 순서와 검증 질문 수립 |
| `ABSTRACT_CHECKED` | 공식 abstract/proceedings 또는 저자 project의 claim 범위를 확인함; source와 검토일 기록 | 해당 source가 직접 지지하는 문제·기여만 인용 |
| `FULL_TEXT_CHECKED` | method, experiment, limitation과 source location을 확인함 | comparison matrix와 gap evidence 갱신 |
| `EXPERIMENT_CHECKED` | 코드 실행 또는 핵심 실험 재현 근거가 있음 | 재현 조건 안에서 empirical claim 사용 |

상태 전환의 최소 조합은 `SKIMMED + ABSTRACT_CHECKED`, `READ + FULL_TEXT_CHECKED`, `REPRODUCED + EXPERIMENT_CHECKED`다. `SYNTHESIZED`는 `FULL_TEXT_CHECKED` 논문 사이의 비교를 요구한다.

`audit_repository.py`는 위 최소 조합과 status별 분석 필드 완성도를 검사하며, 상태나 개인 분석 필드를 자동으로 변경하지 않는다.

## Tracker Fields

| Field | What to record |
|---|---|
| `tier`, `track`, `primary_track`, `paper_id`, `sequence` | 자동 관리되는 읽기 위치. `track`은 상세 reading subgroup, `primary_track`은 7개 canonical robotics track, `paper_id`는 manifest와 synthesis를 연결하는 stable ID |
| `status` | 위 다섯 상태 중 하나 |
| `evidence_level` | 위 네 단계 중 현재 claim 근거 수준 |
| `started_on`, `completed_on` | `YYYY-MM-DD`; 완료일은 `SYNTHESIZED` 또는 `REPRODUCED` 시점 |
| `problem_and_assumptions` | 해결 문제와 성립에 필요한 핵심 가정 |
| `observation_state_action_control` | 입력, 내부 state, action 표현, controller 연결 방식 |
| `embodiment_task_data_metrics` | robot body, task, data, benchmark, metric |
| `failure_modes` | 논문이 인정하거나 실험에서 드러난 실패 조건 |
| `research_relevance` | 현재 연구에 재사용·반박·확장할 지점 |
| `next_action` | 정독, 비교, 코드 확인, 재현 등 다음 한 단계 |
| `personal_notes` | 자유 메모와 외부 자료 링크 |

<a id="note-checks"></a>

## 논문 노트의 공통 검토 기준

| 노트 | 원문에서 확인할 질문 |
|---|---|
| 문제 | 식이나 알고리즘에서 상태·관측·의사결정·제약·종료를 어떻게 정의하는가? 저자가 명시한 가정과 실패, 읽는 사람이 제안한 스트레스 테스트를 구분한다. 평가 지표가 실제 목표를 측정하는지도 확인한다. |
| 방법과 재현 | 새로 제안한 모듈, 물려받은 기준선, 파라미터의 단위·초깃값·갱신식은 무엇인가? 학습 시에만 쓰는 정보와 실행 시 관측을 구분한다. 전처리부터 디코더·계획기·하위 제어기까지의 좌표계, 메모리, 실행 주기와 지연을 확인한다. |
| 비교와 구성요소 제거 실험 | 관측·행동 인터페이스, 제어기, 데이터 분할·시연·라벨, 모델 크기·연산 예산과 예측 구간을 맞춘다. 같은 조건에서 기준선과 개별 구성요소를 제거한 결과, 실패 조건을 함께 비교한다. |
| 평가와 통계 | 데이터가 학습·검증·평가 중 어디에 쓰였는지 확인한다. 성공·충돌·시간 초과의 정의, 시행·에피소드·시드 수, 평균과 불확실성, 분모를 원문 표·그림에 연결한다. 추론 지연, 제어 주파수, 시뮬레이터 처리량은 각각 기록한다. |
| 일반화와 배포 | 새 물체·장면·센서·접촉·복구 중 어떤 조건을 시험했는가? 코드·가중치·환경은 각 논문의 개요에서 확인하고, 측정하지 않은 범위와 독립 재현 여부를 표시한다. |

## Update Workflow

1. 읽기 시작 시 `started_on`을 기록한다. 문제·기여·주요 그림과 실험 구조를 파악하고 최소 분석 필드를 채운 뒤 `status=SKIMMED`, `evidence_level=ABSTRACT_CHECKED` 이상으로 바꾼다.
2. 정독 후 분석 필드를 채우고 `status=READ`로 바꾼다.
3. 해당 [synthesis](../synthesis/README.md) 문서의 comparison matrix와 `Open Questions` evidence를 갱신한다.
4. 다른 논문과의 차이가 명시되면 `status=SYNTHESIZED`와 `completed_on`을 기록한다.
5. 사용한 근거 수준에 맞춰 `evidence_level`을 올리고 full-text claim에는 page/section/table 위치를 남긴다.
6. 분류표 재생성 시 `python3 work/scripts/build_reading_tiers.py`를 실행한다. 경로가 같은 논문의 사용자 입력 필드는 보존된다. 집중 읽기에서 빠진 행은 history CSV로 이동하며 재승격 시 복원한다. `status`, `evidence_level`, 날짜·분석·개인 메모는 tier 변경으로 초기화하지 않는다. 전체 registry index는 active/history 양쪽의 읽기 기록을 보여주며, 통계는 두 분모를 분리한다.

2026-10-19 재분류 후 기존 READ 5편은 active 1편과 history 4편으로 보존되어 있다. 이는 읽기 완료의 취소가 아니라 현재 우선순위의 변경이다.

요약과 핵심 기여만 원문에 대조한 경우에는 확인한 문장에 쪽수나 절을 붙이고 논문별 감사 원장에 기록한다. 논문 전체의 근거 수준은 위 표의 방법·실험·한계 기준으로 판정한다. 사용자가 읽은 단계와 분석은 읽기 기록에 보존한다. [원문 감사](./SOURCE_AUDIT.md#요약기여-원문-대조) · [현재 읽기 기록](./READING_STATUS.csv)
