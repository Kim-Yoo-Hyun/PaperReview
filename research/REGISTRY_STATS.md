# 레지스트리 통계

2026-11-26 KST 기준 **1,280편**. 연도·발표처·태그를 조합해 찾을 때는 [검색 색인](./REGISTRY_INDEX.csv), 교정 후 오류율과 미확인 항목은 [원문 감사](./SOURCE_AUDIT.md)를 사용한다.

## 등록 분포

| 등급 | 편수 |
|---|---:|
| CORE | 50 |
| NEXT | 450 |
| REFERENCE | 538 |
| ARCHIVE | 242 |

| 등록 연도 | 편수 |
|---|---:|
| 2024 | 183 |
| 2025 | 415 |
| 2026 | 389 |
| 그 밖의 연도 | 293 |

| 발표처·공개처 | 편수 |
|---|---:|
| CVPR | 177 |
| RSS | 159 |
| ICLR | 137 |
| CoRL | 117 |
| NeurIPS | 101 |
| ICML | 100 |
| ICCV | 96 |
| arXiv | 76 |
| 그 밖의 발표처·공개처 | 317 |

프리프린트는 등록한 공개 연도를 따른다. 등급별 선정 이유는 [읽기 계획](./READING_PLAN.md)에 있다.

## 읽기 상태

| 사용자 기록 | 현재 정독 대상 | 이전 정독 대상 |
|---|---:|---:|
| UNREAD | 499 | 43 |
| SKIMMED | 0 | 0 |
| READ | 1 | 4 |
| SYNTHESIZED | 0 | 0 |
| REPRODUCED | 0 | 0 |
| 합계 | 500 | 47 |

이전 대상의 분석은 재편입 시 복원된다. [현재 기록](./READING_STATUS.csv) · [이전 기록](./READING_STATUS_HISTORY.csv)

## 원문과 공개 자료

| 확인 범위 | 원장 분포 |
|---|---|
| 판본 유형 | `conference` 1,099 · `journal` 99 · `preprint` 76 · `technical_report` 4 · `workshop` 2 |
| 문헌 검토 근거 | `FULL_TEXT_CHECKED` 1,084 · `ABSTRACT_CHECKED` 196 |
| 코드 배포 | `not_identified` 575 · `released` 535 · `project_only` 147 · `not_released` 23 |
| 데이터 배포 | `not_identified` 965 · `released` 240 · `not_applicable` 68 · `not_released` 7 |
| 체크포인트 기록 | `not_recorded` 1,068 · `reported` 206 · `not_applicable` 4 · `not_released` 2 |

DOI·arXiv·OpenReview ID 없이 원문 주소로 식별한 논문은 363편, 근거가 `MISSING`으로 표시된 표준 노트는 0개다. 코드·데이터의 `not_identified`는 공개 여부 미확인, 체크포인트의 `reported`는 노트에 관련 기록이 있다는 뜻이다. 논문별 판정에는 [감사 원장](../work/sources/batches/source_audit_2026_11.jsonl)을 참조한다.

## 평가 자료와 인용 관계

[통합 자료 목록](../work/sources/resources.json)에 벤치마크·지표·배포처 798개가 있다. 시행 횟수나 시드가 검색 단서로 기록된 논문은 262편이다. 실제 평가 분할·지표·실행 조건은 해당 논문의 평가 노트에서 확인한다.

원장의 방향성 있는 관계 100개는 출발 논문 78편, 양끝을 합쳐 118편에 걸친다. 색인의 `outgoing_relations`에서 상대 ID를 찾고 원장의 `relations`에서 관계 방향·유형·근거를 확인한다. [논문 원장](../work/sources/papers.json) · [OpenVLA 인용 계보](./OPENVLA_LINEAGE.md)

