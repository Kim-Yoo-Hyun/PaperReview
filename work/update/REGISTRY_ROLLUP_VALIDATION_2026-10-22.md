# 후보 요약·registry 갱신 검증 — 2026-10-22

결과: **PASS**. 문서·registry 유지보수 검증이며 연구 효과 검증이 아니다. [변경 범위](./REGISTRY_ROLLUP_2026-10-22.md), [주제별 요약](../research_candidates/summaries/README.md).

## 실행한 검사

| 검사 | 실제 결과 |
|---|---|
| 변경 전 `audit_repository.py` | 990편·4,950개 note, error 0 / warning 0 |
| 등록 전 dry-run | 신규 47 / 기존 title 중복 0 / identifier 충돌 0; alias 포함 별도 정규화 비교 통과 |
| `py_compile` | `build_reading_tiers.py`, `register_papers.py`, `reconcile_registry.py` 통과 |
| `build_reading_tiers.py` | CORE 47 / NEXT 275 / REFERENCE 473 / ARCHIVE 242 |
| `reconcile_registry.py --priorities-only` | 검토 후 apply: 신규 47개 record·47개 overview header만 동기화. 후속 dry-run 0 changes |
| Catalog / registry views | Dry-run 검토 후 apply. Benchmark 51·metric 29·통합 resources 521·index 1,037행 |
| `test_reading_history.py` | 3 tests PASS |
| `test_document_maintenance.py` | 4 tests PASS |
| Abstract note renderer | 47개 입력의 5개 note 생성·미식별 project의 잘못된 상대 링크 부재 검사 PASS |
| 변경 후 repository audit | 1,037편·5,185개 note·active 322·history 47. Schema/identity/title/path/tier/queue/Markdown 검사 error 0 / warning 0 |
| `git diff --check` | PASS |

첫 변경 후 audit에서 신규 2편의 잘못된 curation role enum과 `control/Control` 표기 중복을 발견했다. 신규 input/manifest/해당 overview만 수정하고 registry·생성 view를 다시 동기화한 뒤 통과했다. 기존 기록에 소급 적용하지 않았다.

## 기존 작업 보존

등록 전에 기존 4,950개 표준 note의 SHA-256, manifest 990개 record, active/history 351행을 별도 보관하여 비교했다. [실제 비교 결과](../sources/candidate_rollup_preservation_2026-10-22.json).

- 기존 **4,950개 note 내용과 hash 모두 동일**.
- 기존 **990개 manifest record 전체 동일**. Source evidence·publication·curation·review date를 바꾸지 않았다.
- 기존 **351행의 status·evidence_level·날짜·사용자 분석·메모 모두 동일**. 자동 sequence 필드와 신규 row는 별도로 취급했다.
- 기존 history 47행은 전체 동일. 사용자 READ 5편은 active 1 / history 4로 유지했다.
- 신규 47편은 모두 표준 note 5개·ABSTRACT_CHECKED. NEXT 18편만 active tracker에 UNREAD로 추가했다.
- Summary topic 파일 16개와 index 1개. 별도 research priority register는 만들지 않았다.

Priority sync가 과거 검토 날짜를 오늘 날짜 또는 과거의 공통 날짜로 재기록하지 않도록, 신규 ID별 날짜와 같은 rationale의 기존 basis/date 보존을 적용했다. 위 기존 manifest 전체 동등성과 후속 dry-run 무변경이 실제 회귀 확인이다.

## 검증하지 않은 범위

새 policy inference·simulation·학습·성능 측정·dependency 설치는 없다. GPU 확보 뒤의 최소 검증은 계획이며 실행 결과가 아니다. 기존 NO-GO/HOLD/RETIRED와 외부 피드백 미확보 상태는 유지했다. 새 note를 실제 정독·재현으로 승격하지 않았다. PDF 다운로드 없이 local `paper.pdf` cache 0개를 유지했다.
