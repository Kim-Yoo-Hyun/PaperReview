# Registry Work

이 디렉토리는 registry source, 반복 실행 가능한 유지보수 도구, 날짜별 update log를 관리한다. Python 도구는 `scripts/`에 모아두며, 모든 active command는 PDF availability를 중요도나 완료 기준으로 사용하지 않는다.

## Active tools

- `scripts/audit_repository.py`: read-only 전체 무결성 검사
- `scripts/register_papers.py`: `--input` JSON을 검사하며 기본은 dry-run, `--apply`일 때만 신규 논문과 5종 curation note 등록
- `scripts/build_reading_tiers.py`: tier, reading plan, tracker 자동 필드와 synthesis queue 재생성
- `scripts/normalize_taxonomy.py`: canonical category/tag를 manifest, registry와 note header에 반영
- `scripts/build_lit_survey.py`: 역사적 전체 build helper. 인자 없이 read-only이며 mutation은 각각 명시적 flag가 필요하다.
- `scripts/taxonomy.py`: active tool들이 공유하는 canonical category/tag 규칙

## Sources

- `sources/papers.json`: 현재 821편 registry metadata의 canonical manifest
- `sources/imports/`: 과거 batch별 admission metadata
- `sources/candidates/`: screening에 사용한 broad candidate census. 등록 논문 목록이 아니다.

## Archive

- `scripts/archive/`: 완료된 one-off augmentation, PDF retry, CORE scaffold upgrade, synthesis seed와 migration script. 실행 대상으로 간주하지 않는다.
- `archive/reports/`: 과거 실행 log와 audit snapshot. 현재 상태의 source of truth가 아니다.
- `update/`: 날짜별 registry·frontier·gap 변경 기록. 최신 update는 이 경로에 작성한다.

## Safe workflow

```bash
python3 work/scripts/audit_repository.py
python3 work/scripts/register_papers.py --input /path/to/new_papers.json
python3 work/scripts/register_papers.py --input /path/to/new_papers.json --apply
python3 work/scripts/normalize_taxonomy.py
python3 work/scripts/build_reading_tiers.py
python3 work/scripts/audit_repository.py
```

기존 note를 다시 만드는 명령은 기본 workflow에 포함하지 않는다. `build_lit_survey.py --overwrite-notes`는 명시적인 전체 재생성 승인이 있을 때만 사용한다.
