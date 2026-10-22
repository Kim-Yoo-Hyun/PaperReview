# Work — 근거·검증·유지보수

- Updated: 2026-10-23 KST

저장소 루트는 paper registry다. `work/`에는 문헌 운영 코드, source provenance, 후보별 상세 검토와 실험 근거를 분리한다. 활성 순서는 [TODO](../TODO.md), 연구 판단은 [주제별 단일 요약](./research_candidates/summaries/README.md)을 따른다.

| 경로 | 보존할 내용·수정 원칙 |
|---|---|
| [scripts](./scripts/) | 현행 registry 생성·audit·review 도구. Note migration/전체 재생성은 별도 검토 없이 실행하지 않는다. |
| [sources](./sources/) | Canonical manifest/schema, admission·full-text/source 감사, 생성 catalog/view. 당시 cohort를 현재 수로 소급 변경하지 않는다. |
| [research_candidates](./research_candidates/) | 주제별 summary 1개와 독립 source ledger·claim contract·실제 검토. D1/D3/E1 단계별 검증은 각 `VALIDATION.md`에 통합했다. |
| [experiments](./experiments/README.md) | 실제 실행의 driver·manifest·raw evidence. 과거 driver를 최신 실행 명령처럼 사용하지 않는다. |
| [portable](./experiments/portable/README.md) | 다른 위치/컴퓨터에서 재분석할 Docker entrypoint, hash·의존성·연구 gate. |
| [update](./update/) | 날짜별 작업 이력·검증. [과거 TODO](./update/TASK_HISTORY_2026-10-22.md)는 역사이며 활성 queue가 아니다. |

## 보존과 정리

완료된 일회성 augmentation·PDF retry·scaffold script, 사용되지 않는 ICRA/OpenReview 후보 dump와 bytecode cache를 제거했다. 과거 JSON report 16개는 [한 파일](./sources/legacy_maintenance_reports.json)로 통합했다. [삭제/병합 ledger](./sources/workspace_cleanup_2026-10-23.json)는 원래 경로·SHA256·이유·대체 위치를 기록한다.

`sources/candidates/cvf_candidates.json`과 `sources/imports/`는 현행 `build_lit_survey.py` 입력이다. Full-text/QA manifest, 사용자 읽기 기록, 실험 원시 결과·실행 당시 driver/hash는 재검토 근거이므로 보존한다. 큰 파일이라는 이유만으로 삭제하지 않는다. 모델·dataset·실험 dependency는 Docker 내부에서만 확보한다.

<a id="safe-workflow"></a>

## 변경 범위별 명령

| 작업 | 실행 범위와 주의점 |
|---|---|
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

현재 초점은 VLA 기반 manipulation·navigation이며 RL은 선택 사항이다. 실제 tier 조정이 필요할 때만 `build_reading_tiers.py`의 CORE/NEXT group과 paper-specific rationale을 수정한 뒤 다음을 실행한다. Evidence를 다시 조사하지 않는 tier 조정에는 전체 reconcile보다 이 경로를 사용한다.

```bash
python3 work/scripts/build_reading_tiers.py
python3 work/scripts/reconcile_registry.py --priorities-only
python3 work/scripts/reconcile_registry.py --priorities-only --apply
python3 work/scripts/build_registry_views.py --apply
python3 work/scripts/test_reading_history.py
python3 work/scripts/audit_repository.py
git diff --check
```

`research/READING_STATUS_HISTORY.csv`는 비활성 논문의 읽기 기록이며 새 읽기 목록이 아니다. Tier 재생성 전후 active/history 합집합의 사용자 입력을 비교한다. 과거 full-text/semantic QA manifest의 당시 311편 범위는 역사적 evidence로 보존하고 현재 322편에 맞춰 소급 변경하지 않는다.
