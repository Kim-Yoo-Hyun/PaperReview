# Survey Work

이 디렉토리는 registry source와 반복 실행 가능한 유지보수 도구만 최상위에 둔다. 모든 active command는 PDF availability를 중요도나 완료 기준으로 사용하지 않는다.

## Active tools

- `audit_repository.py`: read-only 전체 무결성 검사
- `register_papers.py`: `--input` JSON을 검사하며 기본은 dry-run, `--apply`일 때만 신규 논문과 5종 curation note 등록
- `build_reading_tiers.py`: tier, reading plan, tracker 자동 필드와 synthesis queue 재생성
- `normalize_taxonomy.py`: canonical category/tag를 manifest, registry와 note header에 반영
- `build_lit_survey.py`: 역사적 전체 build helper. 인자 없이 read-only이며 mutation은 각각 명시적 flag가 필요하다.

## Sources

- `sources/papers.json`: 현재 811편 registry metadata의 canonical manifest
- `sources/imports/`: 과거 batch별 admission metadata
- `sources/candidates/`: screening에 사용한 broad candidate census. 등록 논문 목록이 아니다.

## Archive

- `archive/scripts/`: 완료된 one-off augmentation, PDF retry, CORE scaffold upgrade, synthesis seed와 migration script. 실행 대상으로 간주하지 않는다.
- `archive/reports/`: 과거 실행 log와 audit snapshot. 현재 상태의 source of truth가 아니다.

## Safe workflow

```bash
python3 survey_work/audit_repository.py
python3 survey_work/register_papers.py --input /path/to/new_papers.json
python3 survey_work/register_papers.py --input /path/to/new_papers.json --apply
python3 survey_work/normalize_taxonomy.py
python3 survey_work/build_reading_tiers.py
python3 survey_work/audit_repository.py
```

기존 note를 다시 만드는 명령은 기본 workflow에 포함하지 않는다. `build_lit_survey.py --overwrite-notes`는 명시적인 전체 재생성 승인이 있을 때만 사용한다.
