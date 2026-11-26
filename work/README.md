# 연구 작업

- [연구 후보](./research_topics/README.md) · 질문, 결과, 재현 방법
- [Docker 재현](./experiments/README.md) · 실행 안내와 저장 결과 재분석
- [조사와 변경](./update/README.md) · 로보틱스 동향, 등록 변경, Git 이력
- [논문 원장](./sources/papers.json) · 논문 식별자와 출처
- [다음 작업](../TODO.md) · 우선순위와 재개 조건

<a id="registry-maintenance"></a>

## 레지스트리 유지보수

저장소 루트에서 변경한 원본에 해당하는 명령을 실행한다. `paper_id`는 판본이나 폴더가 바뀌어도 유지한다. [원장](./sources/papers.json) · [스키마](./sources/registry.schema.json) · [배치·검증 메타데이터](./sources/registry_meta.json)

| 변경 | 명령과 확인 사항 |
|---|---|
| 논문 등록 | `python3 work/scripts/register_papers.py --input <json>`으로 미리 보기 후 같은 명령에 `--apply`를 붙인다. 다섯 노트와 [논문 목록](../PAPER.md)의 행을 대조한다. 목록만 다시 만들 때는 `python3 work/scripts/build_lit_survey.py --write-registry`를 사용한다. |
| 등급·읽기 순서 | `build_reading_tiers.py`의 `CORE_GROUPS`·`NEXT_GROUPS`를 수정하고 `python3 work/scripts/build_reading_tiers.py`를 실행한다. 읽기 계획, 등급표, 현재·이전 읽기 기록, 분야별 대기열을 함께 생성한다. 등록·등급 변경 뒤 `python3 work/scripts/reconcile_registry.py --priorities-only`로 차이를 확인하고 `--apply`로 반영한다. 이때 인사이트 노트에서 낡은 등급·트랙·태그 문장은 해당 논문 개요 링크로 바뀐다. |
| 원장 구조·검색 색인 | 구조 변경은 `python3 work/scripts/migrate_registry_schema.py`의 미리 보기와 `--apply`로 적용한다. 평가 노트나 평가 용어가 바뀌면 `python3 work/scripts/build_registry_catalogs.py --apply`로 사전과 원장의 검색 단서를 동기화한다. 그다음 `python3 work/scripts/build_registry_views.py --apply`로 색인·통계·통합 자료 목록을 재생성한다. |
| 원문 감사 | 논문별 판정·열어 본 원문·교정 전 값을 [감사 원장](./sources/batches/source_audit_2026_11.jsonl)에 반영한 뒤 `python3 work/scripts/render_source_audit.py --write --verify-corrections`를 실행한다. |
| 마무리 | `python3 work/scripts/audit_repository.py`로 ID·서지·등급·다섯 노트·대기열·상대 링크를 확인한다. 읽기 상태·날짜·분석은 현재·이전 기록을 함께 대조한다. [공통 검증 명령](../AGENTS.md#완료-전-검증) |

`build_lit_survey.py`는 인자 없이 읽기 전용이다. 메타데이터 갱신·PDF 수집·원장 쓰기는 각각 명시한 옵션을 사용한다. PDF 수집 오류는 명령의 표준 오류 출력에서 확인한다. `--overwrite-notes`는 사용자가 전체 노트 재생성을 요청한 경우에만 쓴다. 원문 근거 자체를 고칠 때는 `reconcile_registry.py` 전체 실행의 차이를 먼저 검토한다. 경로 변경 시 실제 대소문자·안정 ID를 확인하고 검토 당시 판본은 `identity_at_review`로 보존한다.

벤치마크·지표 사전의 자동 연결(`cue_only`)은 원문을 찾기 위한 단서다. 데이터 분할·지표 정의·실행 가능 여부는 논문과 배포 파일에서 확인한다. [벤치마크 사전](./sources/benchmark_catalog.json) · [지표 사전](./sources/metric_catalog.json) · [통합 자료 목록](./sources/resources.json)

에이전트의 공통 지침과 완료 명령은 [AGENTS.md](../AGENTS.md)에 있다. [OpenAI의 AGENTS.md 안내](https://developers.openai.com/codex/guides/agents-md/)
