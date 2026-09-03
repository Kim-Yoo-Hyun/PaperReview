# Registry Work

- Updated: 2026-09-03 KST

이 디렉토리는 registry source, 반복 실행 가능한 유지보수 도구, 날짜별 update log를 관리한다. Python 도구는 `scripts/`에 모아두며, 모든 active command는 PDF availability를 중요도나 완료 기준으로 사용하지 않는다.

## Active tools

- `scripts/audit_repository.py`: read-only 전체 무결성 검사
- `scripts/register_papers.py`: `--input` JSON을 검사하며 기본은 dry-run, `--apply`일 때만 신규 논문과 5종 curation note 등록; paper metadata는 `01_overview.md`에만 쓰고 나머지 note는 pointer를 사용
- `scripts/build_reading_tiers.py`: tier, reading plan, tracker 자동 필드와 synthesis queue 재생성
- `scripts/normalize_taxonomy.py`: canonical category/tag를 manifest, registry와 note header에 반영
- `scripts/reconcile_registry.py`: review manifest·note evidence·tracker evidence를 맞추고 curation role/facet, source scope, provenance가 있는 고신뢰 lineage/dependency relation을 manifest에 반영; sparse relation은 기존 confidence를 보존하면서 basis/source/evidence scope/date를 보강한다. `--backfill-priority-rationales` 또는 `--backfill-reference-archive-rationales`를 명시할 때 해당 tier의 pending rationale을 paper-specific 문장으로 기록
- `scripts/build_registry_views.py`: manifest와 기존 cue catalog에서 하나의 resource view, relation-aware 검색용 paper index, 통계 view를 생성
- `scripts/migrate_registry_schema.py`: 기존 manifest에 stable paper ID, public identifiers, publication/source/artifact 분리, canonical primary track, curation와 provenance field를 추가; 기본은 dry-run
- `scripts/build_registry_catalogs.py`: `04_evaluation.md`의 benchmark/metric cue를 paper ID에 연결한 탐색용 catalog 생성; 모든 reference는 `cue_only`
- `scripts/registry_schema.py`: manifest schema 상수, ID/source/venue/track helper와 dependency-free record validation
- `scripts/build_lit_survey.py`: 역사적 전체 build helper. 인자 없이 read-only이며 mutation은 각각 명시적 flag가 필요하다.
- `scripts/migrate_problem_notes.py`: 전체 `02_problem.md`에서 paper metadata를 제거하고 공통 formulation-first schema로 정규화; 현재 CORE/NEXT papers는 문제·model·objective·constraint·failure boundary profile을 채운다. 기본은 dry-run이며 `--apply`일 때만 기록한다.
- `scripts/migrate_method_notes.py`: 전체 `03_method.md`에서 반복 metadata를 제거하고 pipeline/objective/variables/runtime/training-inference/evaluation-link schema로 정규화; 현재 CORE/NEXT papers는 method profile과 04 baseline/ablation 연결을 채운다. 기본은 dry-run이며 `--apply`일 때만 기록한다.
- `scripts/migrate_evaluation_notes.py`: 전체 `04_evaluation.md`에서 반복 metadata를 제거하고 evaluation type/scope, experimental matrix, dataset role, embodiment/environment, metric, baseline fairness, ablation, result, failure, statistics/reproducibility schema로 정규화; 현재 CORE/NEXT papers는 기존 source cue와 problem/method profile을 연결해 상세 audit를 채운다. 기본은 dry-run이며 `--apply`일 때만 기록한다.
- `scripts/enrich_remaining_notes.py`: CORE/NEXT를 제외한 639편의 `02_problem.md`, `03_method.md`, `04_evaluation.md`를 domain-specific formulation bridge, module pipeline, interface, evaluation matrix와 source-bounded verification field로 확장한다. tracked legacy cue와 `01_overview.md`를 사용하며, PDF를 다운로드하거나 reading status/evidence를 올리지 않는다. 기본은 dry-run이며 `--apply`일 때만 기록한다.
- `scripts/download_fulltext_pdfs.py`: `--tiers CORE,NEXT`처럼 지정한 tier의 paper를 대상으로 task-scoped PDF를 다운로드하고 PDF magic/page validity를 검증한다. `--paper-ids`로 단일 source를 재검증할 수 있으며, 임시 캐시만 사용하고 tier, reading status, evidence level은 변경하지 않는다.
- `scripts/review_fulltext_notes.py`: 검증된 PDF 본문을 PyMuPDF/pdftotext로 추출하고 필요한 경우 tesseract OCR로 보완한 뒤, page/section anchor와 함께 `02_problem.md`–`04_evaluation.md`를 갱신한다. 기본은 dry-run이며 `--apply`일 때만 note와 compact manifest를 기록한다.
- `scripts/review_core_next_fulltext.py`: 지정한 tier의 papers를 대상으로 본문 evidence cue를 추출해 `01_overview.md`–`05_insights.md`를 갱신한다. PDF가 공개되지 않은 경우 official source exception을 명시하며, tier·reading status·tracker evidence는 변경하지 않는다. 기본은 dry-run이며 `--apply`일 때만 기록한다.
- `scripts/semantic_qa_core_next.py`: CORE/NEXT 311편의 검증된 PDF를 section-aware selector와 OCR fallback으로 재검토하고, generic fallback·잘못 선택된 failure cue·paper-specific method/evaluation/research question을 보정한다. tier·reading status·tracker evidence는 변경하지 않으며, `--apply` 시 5개 표준 note와 semantic QA report만 기록한다.
- `scripts/audit_note_artifacts.py`: 950개 paper folder의 5개 standard note를 읽기 전용으로 검사하고, 명백한 legacy PDF-extraction artifact만 `--apply`로 보수적으로 정리한다. PDF 다운로드·note 재생성·reading status 변경은 하지 않으며 audit 결과는 `sources/note_artifact_audit_2026-09-02.json`에 남긴다.
- `scripts/migrate_insights_notes.py`: 기존 `05_insights.md`를 evidence-bounded `Paper-supported conclusion` / `Researcher interpretation` schema로 이관; 기본은 dry-run이며 `--apply`일 때만 기록한다.
- `scripts/taxonomy.py`: active tool들이 공유하는 canonical category/tag 규칙

## Sources

- `sources/papers.json`: 현재 950편 registry metadata의 canonical manifest
- `sources/registry.schema.json`: structured manifest의 JSON Schema; legacy flat fields는 호환성을 위해 허용
- `sources/registry_meta.json`: manifest schema/count/identity/version/evidence policy metadata
- `sources/resources.json`: benchmark/dataset·metric·code/project를 함께 보여주는 생성 resource view; benchmark/metric 항목은 `cue_only`, code/project는 manifest link일 뿐 재현성 보장이 아님
- `papers.json`의 `relations`: directed paper lineage/dependency edges의 canonical store. `from` paper의 relation이 `paper_id` target을 가리키며, 관리 edge는 `type`, `confidence`, `basis`, `source`, `evidence_scope`, `reviewed_on`을 함께 가진다. 이는 exhaustive citation graph가 아니며, `baseline_for`는 baseline paper → 이를 평가한 paper 방향이다.
- `sources/benchmark_catalog.json`, `sources/metric_catalog.json`: evaluation note cue 기반 paper-ID navigation catalog. 역할·split·정의의 최종 근거가 아님
- `sources/fulltext_review_manifest.json`: PDF 본문 검토의 paper ID, source, hash, page 수, 추출 방식/품질, title match와 evidence count를 보존하는 compact audit manifest. 원본 PDF 캐시는 canonical source가 아니다.
- `sources/fulltext_core_next_review_manifest.json`: 현재 CORE/NEXT 311편 full-text/source audit, 추출 품질, page/section evidence count와 source exception을 보존하는 compact manifest. 작업용 PDF 캐시는 검증 후 삭제되며 canonical source가 아니다.
- `sources/fulltext_reference_reinforcement_2026-09-02_review_manifest.json`: 현재 REFERENCE 6편에 대한 별도 targeted full-text audit manifest. intensive reading complement로 해석하지 않는다.
- `sources/fulltext_all_review_manifest_2026-09-02.json`: 전체 950편의 `01_overview.md`–`04_evaluation.md` 본문 검토 범위, source/hash, page 수, 추출 방식·품질, title match와 note 작성 수를 보존하는 최신 audit manifest. 작업용 PDF 캐시는 검증 후 삭제되며 canonical source가 아니다.
- `sources/fulltext_insights_review_manifest_2026-09-03.json`: 기존 Abstract/Curation-only 634편의 `05_insights.md` PDF 본문 보강 범위, source/hash, page 수, 추출 방식·품질과 note 작성 수를 보존하는 targeted audit manifest. `reconcile_registry.py`는 이를 paper-level review와 분리해 `provenance.note_review["05_insights.md"]`로 연결한다. 작업용 PDF 캐시는 검증 후 삭제되며 canonical source가 아니다.
- `sources/core_next_semantic_qa_2026-09-03.json`: CORE/NEXT 311편의 PDF-body semantic cross-check 범위, OCR/text extraction, title overlap, section anchor, generic-marker before/after와 source-boundary 예외를 보존하는 QA report.
- `sources/note_artifact_audit_2026-09-02.json`: standard note의 legacy extraction artifact 검사 범위, before/after finding과 보수적 cleanup 결과를 보존하는 audit report.
- `sources/imports/`: 과거 batch별 admission metadata
- `sources/candidates/`: screening에 사용한 broad candidate census. 등록 논문 목록이 아니다.
- `../research/REGISTRY_INDEX.csv`, `../research/REGISTRY_STATS.md`: manifest·tier·tracker에서 생성되는 검색/진단 view. 직접 수정하지 않는다.

## Archive

- `scripts/archive/`: 완료된 one-off augmentation, PDF retry, CORE scaffold upgrade, synthesis seed와 migration script. 실행 대상으로 간주하지 않는다.
- `archive/reports/`: 과거 실행 log와 audit snapshot. 현재 상태의 source of truth가 아니다.
- `update/`: 날짜별 registry·frontier·gap 변경 기록. 최신 update는 이 경로에 작성한다.

## Safe workflow

```bash
python3 work/scripts/audit_repository.py
python3 work/scripts/migrate_registry_schema.py
python3 work/scripts/migrate_registry_schema.py --apply
python3 work/scripts/build_registry_catalogs.py
python3 work/scripts/build_registry_catalogs.py --apply
python3 work/scripts/register_papers.py --input /path/to/new_papers.json
python3 work/scripts/register_papers.py --input /path/to/new_papers.json --apply
python3 work/scripts/normalize_taxonomy.py
python3 work/scripts/build_reading_tiers.py
python3 work/scripts/reconcile_registry.py
python3 work/scripts/reconcile_registry.py --apply
python3 work/scripts/reconcile_registry.py --backfill-priority-rationales
python3 work/scripts/reconcile_registry.py --apply --backfill-priority-rationales
python3 work/scripts/reconcile_registry.py --backfill-reference-archive-rationales
python3 work/scripts/reconcile_registry.py --apply --backfill-reference-archive-rationales
python3 work/scripts/build_registry_views.py
python3 work/scripts/build_registry_views.py --apply
python3 work/scripts/audit_note_artifacts.py
python3 work/scripts/audit_note_artifacts.py --apply
python3 work/scripts/review_core_next_fulltext.py --tiers CORE,NEXT,REFERENCE,ARCHIVE
python3 work/scripts/review_core_next_fulltext.py --tiers CORE,NEXT,REFERENCE,ARCHIVE --apply
python3 work/scripts/semantic_qa_core_next.py --ocr-low-confidence
python3 work/scripts/semantic_qa_core_next.py --ocr-low-confidence --apply
python3 work/scripts/migrate_problem_notes.py
python3 work/scripts/migrate_problem_notes.py --apply
python3 work/scripts/migrate_method_notes.py
python3 work/scripts/migrate_method_notes.py --apply
python3 work/scripts/migrate_evaluation_notes.py
python3 work/scripts/migrate_evaluation_notes.py --apply
python3 work/scripts/migrate_insights_notes.py
python3 work/scripts/migrate_insights_notes.py --apply --sync-evidence
python3 work/scripts/audit_repository.py
```

`resources.json`은 resource를 별도 catalog 여러 개로 분산하지 않기 위한 통합 view다. benchmark/metric의 기존 cue catalog를 갱신하지 않는 한 `build_registry_catalogs.py`를 매번 실행할 필요는 없다. `READING_STATUS.csv`의 사용자 `status`와 개인 분석 필드는 `reconcile_registry.py`가 변경하지 않으며, evidence만 review manifest와 정합화한다. paper-level `provenance.review`와 note-level `provenance.note_review`는 서로 다른 provenance 층으로 유지한다. `audit_repository.py`는 상태별 최소 분석 필드, evidence level, 완료 논문의 synthesis matrix 연결과 note-review manifest attachment도 함께 검사한다.

Lineage/dependency relation은 논문을 많이 연결하기 위한 citation dump가 아니다. 본문·공식 초록·공식 project page 또는 명시적 version title로 방향과 근거를 확인할 수 있는 연결만 seed하며, `inferred`는 representation/method family 수준의 해석임을 표시한다. `REGISTRY_INDEX.csv`의 `outgoing_relations`와 `incoming_relation_count`, `REGISTRY_STATS.md`의 relation type/confidence/evidence-scope 표는 이 연결을 검색·감사하기 위한 파생 view다.

기존 note를 다시 만드는 명령은 기본 workflow에 포함하지 않는다. `build_lit_survey.py --overwrite-notes`는 명시적인 전체 재생성 승인이 있을 때만 사용한다.
