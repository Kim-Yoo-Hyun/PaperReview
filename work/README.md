# Work — 근거·검증·유지보수

- Updated: 2026-11-18 KST

저장소 루트는 paper registry다. `work/`에는 문헌 운영 코드, source provenance, 후보별 상세 검토와 실험 근거를 분리한다. 유지 3개·예비 1개와 폐기 7개의 판정은 [주제 index](./research_topics/README.md), 선택한 다음 행동은 [TODO](../TODO.md)를 따른다. [기존 주제별 요약](./research_candidates/summaries/README.md)은 과거 판정, [synthesis](../synthesis/README.md)는 논문 간 질문을 보존한다.

| 경로 | 보존할 내용·수정 원칙 |
|---|---|
| [research_topics](./research_topics/README.md) | 유지 3개·예비 1개와 새 탐색 주제의 `내용/`·`재현 방법/`. 주제별 핵심 문서와 재현 안내 각 1개를 갱신하며 별도 중복 보고서를 늘리지 않는다. |
| [scripts](./scripts/) | 현행 registry 생성·audit·review 도구. Note migration/전체 재생성은 별도 검토 없이 실행하지 않는다. |
| [sources](./sources/) | Canonical manifest/schema, admission·full-text/source 감사, 생성 catalog/view. 당시 cohort를 현재 수로 소급 변경하지 않는다. |
| [research_candidates](./research_candidates/) | 과거 후보의 summary·source·검토 보존. 현재 유지 주제와 폐기 요약은 위 research_topics index를 따른다. D1/D3/E1 등 과거 경로와 과학적 판단은 유지한다. |
| [experiments](./experiments/README.md) | 과거 실행의 driver·manifest·raw evidence 및 현재 주제의 재현 안내 연결. 과거 driver를 최신 실행 명령처럼 사용하지 않는다. |
| [portable](./experiments/portable/README.md) | 다른 위치/컴퓨터에서 재분석할 Docker entrypoint, hash·의존성·연구 gate. |
| [update](./update/) | 날짜별 작업 이력·검증. [완료 TODO 이력](./update/TASK_HISTORY_2026-10-28.md)는 역사이며 활성 queue가 아니다. |

## 보존과 정리

[11/16 Ψ₀·정확성 보완](./update/REGISTRY_ACCURACY_PSI0_2026-11-16.md)에서 직접 논문3편을 등록하고 AMO OCR·SONIC 공개 자료를 교정했다. 11/18 [REG-R17](./update/REGISTRY_MAINTENANCE_2026-11-18.md)에서 미등록 직접 선행18편과 문서/생성 view를 보강했다. 후속 [REG-R18](./update/REGISTRY_MAINTENANCE_2026-11-18.md#reg-r18)에서 geometry 직접 선행3편을 등록하고 중복된 완료 안내·재생성 가능한 cache를 정리했다. 현재 수량은 [생성 통계](../research/REGISTRY_STATS.md), 과거 등록·삭제 근거는 [update index](./update/README.md), 후보·준비/실행 범위는 주제 index가 소유한다.

이전의 보고서 병합·일회 script 제거·source report 통합은 [update index](./update/README.md)의 날짜별 기록을 따른다. 현재 source나 실행 근거가 없는 파일로 확인된 경우에만 정리하며, 오래됐다는 이유만으로 역사적 증거를 지우지 않는다.

`sources/candidates/cvf_candidates.json`과 `sources/imports/`는 과거 발견 목록을 재검토하는 입력으로 보존한다. 일반 `build_lit_survey.py` CLI는 **현재 canonical manifest**를 읽으며, 과거 `build_papers()` 발견 목록을 전체 registry로 쓰지 않는다. Full-text/QA manifest, 사용자 읽기 기록, 실험 원시 결과·계약/hash는 재검토 근거로 보존한다. 11/17 폐기 후보의 실행 driver·recipe는 명시적 사용자 요청에 따라 제거했고 고정 Git commit에서 이력을 추적한다. 모델·dataset·실험 dependency는 Docker 내부에서만 확보한다.

<a id="safe-workflow"></a>

## 변경 범위별 명령

| 작업 | 실행 범위와 주의점 |
|---|---|
| PAPER table 재생성 | `build_lit_survey.py --write-registry`는 현재 manifest의 전체 항목을 사용한다. 기존 stable ID 누락을 감지하면 쓰기 전에 중단한다. Flag 없는 실행은 read-only이며 note/PDF/manifest 갱신은 각각 별도 opt-in이다. |
| 신규 논문 | `register_papers.py --input <json>` dry-run 후 `--apply`. Canonical group을 수정한 뒤 아래 priority/view 절차를 실행한다. Abstract만 확인한 논문에는 `abstract_analysis_v1`과 논문별 분석 필드를 사용한다. |
| Taxonomy 변경 | `normalize_taxonomy.py`는 즉시 manifest·PAPER·note header를 기록한다. 변경 범위를 먼저 확인한다. 신규 등록 때마다 전체 실행할 필요는 없다. |
| Schema 변경 | `migrate_registry_schema.py` dry-run 후 검토한 migration만 `--apply`한다. |
| Benchmark/metric cue 변경 | `build_registry_catalogs.py` dry-run 후 `--apply`, 이어 view를 재생성한다. 모든 자동 연결은 `cue_only`다. |
| Source/evidence 변경 | 전체 `reconcile_registry.py` dry-run 결과를 검토한다. `--apply`는 evidence·profile·relation을 갱신하므로 priority-only 작업과 구분한다. |
| 전체 profile 재생성 | `enrich_registry_metadata.py`는 기존 profile을 다시 만든다. Abstract provenance나 수동 profile의 보존 범위를 검토하기 전에는 일반 유지보수에서 실행하지 않는다. |
| 본문·note 재작성 | `review_*`, `semantic_qa_*`, `migrate_*_notes.py`, `enrich_remaining_notes.py`는 별도 내용 검토 작업이다. 이번 문서 최신화에 일괄 `--apply`하지 않는다. |
| Extraction artifact | `audit_note_artifacts.py`는 기본 read-only다. 실제 cleanup이 필요한 경우만 검토 후 `--apply --report work/sources/note_artifact_audit_YYYY-MM-DD.json`을 사용해 과거 report를 보존한다. |

`resources.json`은 benchmark/dataset·metric·code/project를 합친 생성 view다. Cue catalog가 바뀌지 않았다면 매번 다시 만들 필요는 없다. `READING_STATUS.csv`의 사용자 status·날짜·분석과 inactive history는 재생성 전후 비교한다. Paper-level `provenance.review`와 note-level `provenance.note_review`는 서로 다른 근거 층이며, source 검토는 사용자의 정독 이력이 아니다.

## Priority-only update

현재 새 연구 탐색은 VLA + RL 기반 manipulation·navigation을 우선하며 기존 비-RL 후보와 넓은 문헌 범위를 보존한다. 실제 tier 조정이 필요할 때만 `build_reading_tiers.py`의 CORE/NEXT group과 paper-specific rationale을 수정한 뒤 다음을 실행한다. Evidence를 다시 조사하지 않는 tier 조정에는 전체 reconcile보다 이 경로를 사용한다.

```bash
python3 work/scripts/build_reading_tiers.py
python3 work/scripts/reconcile_registry.py --priorities-only
python3 work/scripts/reconcile_registry.py --priorities-only --apply
python3 work/scripts/build_registry_views.py --apply
python3 work/scripts/test_reading_history.py
python3 work/scripts/audit_repository.py
git diff --check
```

`research/READING_STATUS_HISTORY.csv`는 비활성 논문의 읽기 기록이며 새 읽기 목록이 아니다. Tier 재생성 전후 active/history 합집합의 사용자 입력을 비교한다. 과거 full-text/semantic QA manifest의 당시 311편 범위는 역사적 evidence로 보존하고 현재 집중 읽기 규모에 맞춰 소급 변경하지 않는다.
