# 단계별 검증 기록 — e1_buildup

2026-10-23 통합. 각 절은 원래 날짜·범위·검사 결과를 보존한다. 당시 registry 수치는 역사적 snapshot이며 정책 효과나 현재 재개 자격을 뜻하지 않는다.

<a id="stage-0"></a>

## VALIDATION.md

E1 buildup 유지보수 검증

- 날짜: 2026-10-22. 문서·registry 보존 검사이며 정책 효과 검증이 아니다.
- 사전 repository audit: errors 0 / warnings 0. Registry 990, CORE 47 / NEXT 257 / REFERENCE 444 / ARCHIVE 242, tracker 304 / history 47.
- 변경 전 보호 hash: 표준 paper notes 4,950개와 PAPER/manifest/tier/tracker/history/generator 6개, 합계 4,956개.
- `python3 -m py_compile work/scripts/build_reading_tiers.py`: PASS.
- `python3 work/scripts/build_reading_tiers.py`: PASS. Tier 수 47 / 257 / 444 / 242 유지.
- `git diff --check`: PASS.
- 최종 `audit_repository.py`: errors 0 / warnings 0. Markdown 5,064개·링크 8,733개, comparison 106행/완료 5행 검사. Registry 990·notes 4,950·resource 496·index 990 유지.
- 보호 hash: **4,955개 동일 / 1개 의도한 변경 / 누락 0**. 변경 파일은 generator의 현재 E1 판단/navigation 문구다. PAPER, manifest, tier CSV, active/history tracker와 paper note 4,950개 모두 byte-identical. CORE/NEXT 선정 규칙·rationale 변경 없음.
- 새 JSON 2개 파싱 PASS. `EVIDENCE_REQUIREMENTS.json`의 `executable=false`, runtime/checkpoint/split 미확보, policy runs 0을 유지했다.

### Source와 변경 범위

- Text 조회 기록 56개, 고유 URL 47개, 최종 성공 고유 URL 46개·9,160,329 bytes. 이는 HTTP metadata/tree/공개 text 응답 합계이며 다운로드한 trajectory 크기나 정독 논문 수가 아니다. 별도 web 원문 검토는 local hash 없이 구분했다.
- 실패 attempt 2개를 보존: MIR의 잘못된 abstract URL 404, 큰 annotation의 초기 4 MB bound 초과. 각각 공식 PDF의 정확한 repo와 16 MB 범위의 text 재조회로 필요한 후속 자료를 확인했다.
- 새 작업 artifact 7개: README, CLOSEST_WORK, SOURCE_ASSET_AUDIT, CLAIM_CONTRACT, EVIDENCE_REQUIREMENTS.json, sources ledger, 이 검증 문서.
- TODO·AGENTS·root/work README·최초 scout/card·수동 VLA Open Question·update log를 정합화했다. Generator 현재 안내만 수정해 READING_PLAN을 재생성했으며 queue·tracker 입력은 보존했다.
- 작업 중 만든 보호 hash·source ledger 임시본·text 조회 helper의 정확한 임시 파일 3개를 최종 보존 비교 후 제거했다. 사용자의 기존 파일·Docker 자원은 건드리지 않았다.

### 근거 경계

공개 text/metadata의 identity는 `sources_2026-10-22.json`에 기록했다. Public annotation 6,073개는 task 설명/path metadata이며 physical trajectory 검증 결과가 아니다. 응답 실패와 text 크기 제한 후 재시도를 숨기지 않는다. 직접 원문·public source 정적 심사로 사용자 reading status를 올리지 않는다.

실험·inference·학습·FK 실행·Docker preflight·dependency 설치·model/trajectory/video/PDF 저장·외부 연락 없음. Paper note·registry identity·tier assignment를 변경하지 않는 작업이다. 이전 dirty worktree를 되돌리지 않았다.


<a id="stage-1"></a>

## R1_VALIDATION.md

E1-R1 문서·registry 유지보수 검증

- 날짜: 2026-10-22. 연구 효과 검증과 구분한다.
- 사전 audit: errors 0 / warnings 0. Registry 990, CORE 47 / NEXT 257 / REFERENCE 444 / ARCHIVE 242, active tracker 304 / history 47.
- 보호 snapshot: 표준 paper notes 4,950개와 PAPER/manifest/tier/active tracker/history/generator 6개, 합계 4,956개.
- `python3 -m py_compile work/scripts/build_reading_tiers.py`: PASS.
- `python3 work/scripts/build_reading_tiers.py`: PASS, tier 47 / 257 / 444 / 242 유지.
- `git diff --check`: PASS.
- `python3 work/scripts/audit_repository.py`: errors 0 / warnings 0. Registry 990·notes 4,950·active 304/history 47·resources 496·index 990 유지. Comparison 106행/완료 5행 검사.
- 보호 hash: **4,955개 동일 / 1개 의도한 변경 / 누락 0**. Generator의 현재 E1-R1 판단 안내만 변경했다. PAPER·manifest·tier CSV·active/history tracker·paper note 4,950개는 byte-identical이다. CORE/NEXT 선정 규칙·rationale은 변경하지 않았다.
- 새 JSON 3개 파싱 PASS. 66/98 task ID 집합의 교집합 59, parsed key 82,920·unparsed 0, R1 review DONE/gate NOT_MET, executable=false, policy_runs=0, 선택 runtime 필드 null 확인.

### 변경 범위와 근거 경계

- 신규 artifact: R1_REVIEW.md, R1_EVIDENCE_REQUIREMENTS.json, R1_METADATA_AUDIT.json, r1_sources_2026-10-22.json, 이 검증 문서.
- 기존 1차 판정과 source ledger/requirements는 역사적 근거로 보존했다. README·TODO·현재 navigation·수동 synthesis·generator 현재 판단 문구를 갱신했다.
- 새 metadata 계산은 공개 text key/clip 범위의 파싱이다. 82,920 view keys와 82,894 converted episode rows를 같은 분모로 사용하지 않는다. Array/video를 읽지 않았고 source join·시간 정렬·실제 효과는 검증하지 않았다.
- Public text/API 54회, 고유 URL 45개, 고유 최종 성공 응답 합계 20,864,937 bytes. 이는 정독 논문 수·trajectory 크기가 아니다. 별도 web의 verification/403 경계는 ledger에 분리했다.
- 모델 inference·학습·simulation·FK·Docker preflight·dependency 설치·weight/trajectory/video/PDF 저장·외부 연락은 없다. R1 review DONE과 gate NOT_MET, executable=false, 정책 실행 0회를 구분한다.
- 기존 dirty worktree를 되돌리거나 관련 없는 파일·Docker 자원을 정리하지 않았다.
