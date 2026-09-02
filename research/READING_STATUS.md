# Reading Status Guide

- Updated: 2026-09-02 KST

- Canonical tracker: [READING_STATUS.csv](./READING_STATUS.csv)
- Scope: CORE 77편 + NEXT 234편 = 311편
- PDF 보유 여부는 읽기 우선순위, 상태 전환, 완료 판단에 사용하지 않는다.

## Status

| Status | Meaning | Minimum evidence |
|---|---|---|
| `UNREAD` | 아직 읽기 시작하지 않음 | 없음 |
| `SKIMMED` | 문제, 기여, 주요 그림과 실험 구조를 파악함 | `problem_and_assumptions`, `next_action` |
| `READ` | 방법과 실험을 정독함 | 핵심 분석 필드와 failure mode 작성 |
| `SYNTHESIZED` | 같은 트랙의 논문과 비교까지 완료함 | SYNTHESIS comparison matrix와 research gap 갱신 |
| `REPRODUCED` | 코드 실행 또는 핵심 실험 재현 완료 | 재현 조건과 결과를 `personal_notes`에 기록 |

`REPRODUCED`는 필수 최종 단계가 아니다. 이론·시스템 논문은 `SYNTHESIZED`에서 완료될 수 있다.

## Evidence Level

읽기 진행도와 주장 근거 수준은 별개로 관리한다. 노트 파일이나 로컬 PDF가 있다는 사실만으로 evidence level을 올리지 않는다.

| Evidence level | Meaning | 허용되는 사용 |
|---|---|---|
| `CURATION_ONLY` | metadata, 공식 abstract/project cue 또는 읽기 전 구조화만 있음 | 읽기 순서와 검증 질문 수립 |
| `ABSTRACT_CHECKED` | 공식 abstract/proceedings의 claim 범위를 사람이 확인함 | abstract가 직접 지지하는 문제·기여만 인용 |
| `FULL_TEXT_CHECKED` | method, experiment, limitation과 source location을 확인함 | comparison matrix와 gap evidence 갱신 |
| `EXPERIMENT_CHECKED` | 코드 실행 또는 핵심 실험 재현 근거가 있음 | 재현 조건 안에서 empirical claim 사용 |

상태 전환의 최소 조합은 `SKIMMED + ABSTRACT_CHECKED`, `READ + FULL_TEXT_CHECKED`, `REPRODUCED + EXPERIMENT_CHECKED`다. `SYNTHESIZED`는 `FULL_TEXT_CHECKED` 논문 사이의 비교를 요구한다.

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

## Update Workflow

1. 읽기 시작 시 `status=SKIMMED`, `started_on`을 기록한다.
2. 정독 후 분석 필드를 채우고 `status=READ`로 바꾼다.
3. 해당 [synthesis](../synthesis/README.md) 문서의 comparison matrix와 research gap evidence를 갱신한다.
4. 다른 논문과의 차이가 명시되면 `status=SYNTHESIZED`와 `completed_on`을 기록한다.
5. 사용한 근거 수준에 맞춰 `evidence_level`을 올리고 full-text claim에는 page/section/table 위치를 남긴다.
6. 분류표 재생성 시 `python3 work/scripts/build_reading_tiers.py`를 실행한다. 경로가 같은 논문의 사용자 입력 필드는 보존된다.
