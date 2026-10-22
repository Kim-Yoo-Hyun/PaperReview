# 단계별 검증 기록 — d3_buildup

2026-10-23 통합. 각 절은 원래 날짜·범위·검사 결과를 보존한다. 당시 registry 수치는 역사적 snapshot이며 정책 효과나 현재 재개 자격을 뜻하지 않는다.

<a id="stage-0"></a>

## VALIDATION.md

D3 비실험 buildup — 검증 기록

- 검증일: 2026-10-22 KST
- 범위: 문헌/source 읽기와 repository 문서 유지보수. 정책·runtime 검증이 아니다.
- 작업 전 repository audit: 오류 0, 경고 0. Registry 990 / intensive 304 / history 47 / 표준 note 4,950.
- 작업 후 필수 유지보수 검사와 보존 비교 통과. 아래 결과는 연구 가설 입증과 구분한다.

### 실제 유지보수 검사

- `python3 -m py_compile work/scripts/build_reading_tiers.py`: exit 0.
- `python3 work/scripts/build_reading_tiers.py`: exit 0. CORE 47 / NEXT 257 / REFERENCE 444 / ARCHIVE 242 유지.
- `git diff --check`: 통과. Untracked D3 파일·TODO의 trailing whitespace도 별도로 검사했다.
- `python3 work/scripts/audit_repository.py`: exit 0, 오류 0·경고 0. Registry 990, intensive 304, history 47, notes 4,950, resources 496, index 990. Markdown 5,051개·links 8,597개, comparison rows 106/completed 5.
- 작업 시작 SHA-256 snapshot과 보호 파일 4,956개를 비교해 차이 0. PAPER/manifest/generator/tier/active·history tracker/표준 paper notes를 보존했다.
- Source JSON parse, paper 8개 중 외부 4개, source text 23개, repo+commit+path uniqueness, commit/hash 형식을 확인했다. 총 395,889 bytes이며 원문 전체를 저장한 것이 아니라 identity metadata를 저장했다.
- 신규 artifact 5개: README, CLOSEST_WORK, TASK_CONTRACT, sources JSON, 이 검증 기록. 실행 manifest나 실험 결과 파일은 만들지 않았다.

### 연구 증거 경계

문헌 관련 절·공개 text source를 읽고 hash/commit을 기록했다. Simulation, policy inference, training, 성능 측정, Docker preflight는 수행하지 않았다. 의존성 설치·model/data/PDF 저장·외부 연구자 연락도 하지 않았다. Source identity는 실행 artifact의 재현성 증명이 아니다.

신규 파일은 결과, 문헌 대조, task 계약, source JSON, 이 검증 기록이다. Case matrix는 설계이며 실제 episode가 아니다. Registry 신규 등록·tier 변경·사용자 reading status 승격을 하지 않는다. 기존 dirty worktree를 보존한다.


<a id="stage-1"></a>

## L1_VALIDATION.md

D3-L1 문서·metadata 검증

- 2026-10-22 KST. Source/annotation의 정적 감사와 repository maintenance만 수행했다.
- 작업 전 audit: 오류 0·경고 0. Registry 990, intensive 304, history 47, 표준 note 4,950.
- 작업 후 필수 유지보수 검사·보존 비교 통과. 연구 성능 검증과 구분한다.

### 실제 검사 결과

- `python3 -m py_compile work/scripts/build_reading_tiers.py`: exit 0.
- `python3 work/scripts/build_reading_tiers.py`: exit 0. CORE 47 / NEXT 257 / REFERENCE 444 / ARCHIVE 242 유지.
- `git diff --check`: exit 0. Untracked D3 Markdown도 별도 whitespace 검사 통과.
- `python3 work/scripts/audit_repository.py`: exit 0, 오류 0·경고 0. Registry 990, intensive 304, history 47, 표준 note 4,950, resources 496, index 990. Markdown 5,053개·links 8,623개, comparison rows 106/completed 5.
- 작업 시작 시 보호 snapshot 4,956개와 비교해 SHA-256 차이 0. PAPER/manifest/generator/tier/active·history tracker/표준 paper notes 보존.
- Source ledger와 qualification JSON parse 통과. 고유 repo+revision+path 232개, revision/hash 형식, 총 text bytes 2,316,063 확인. Source 32개와 annotation 200개에 중복 집계 없음.
- Annotation metadata의 skill count 합계 2,599, final skill count 합계 200, 수집 오류 0을 확인했다. 이는 성능·관측 가능성 검사 결과가 아니다.
- D3 문서·TODO의 로컬 링크 대상 및 heading anchor 검사 통과. Spec의 `implemented=false`, `executable=false`, `policy_rollouts=0` 확인.
- 신규 artifact 4개: TASK_POLICY_AUDIT, QUALIFICATION_SPEC, qualification_sources JSON, 이 검증 기록. 기존 B1 문서는 최신 후속 링크를 추가하고 역사적 분석을 보존했다.

### 증거 경계

공개 text source 32개·annotation metadata 200개, 총 고유 파일 232개를 원격으로 읽고 identity와 분석만 기록했다. Annotation payload 원문을 로컬에 보관하지 않았다. Metadata 집계는 정책 성능 실험이 아니다.

Simulation·policy inference·학습·Docker/resource preflight·의존성 설치를 하지 않았다. Weight·Parquet action/state·HDF5·video·PDF를 다운로드하거나 로컬에 저장하지 않았다. Gated model의 조건 수락·계정 사용·외부 연락도 없었다.

기존 source ledger는 B1 당시 증거로 보존한다. 신규 source/qualification 명세는 `executable=false`이며 model card 수치를 독립 재현 결과로 바꾸지 않는다. Registry 신규 등록·tier·사용자 reading status를 변경하지 않는다.


<a id="stage-2"></a>

## R1_VALIDATION.md

D3-R1 문서·근거 보존 검증

- 2026-10-22 KST. 공개 문헌·code text·metadata와 저자 보고를 읽은 비실험 작업이다.
- 작업 전 repository audit: 오류 0·경고 0. Registry 990, intensive 304, history 47, paper notes 4,950.
- 최종 유지보수 검사 결과는 아래에 기록한다. 정책 효과 검증과 구분한다.

### 실제 검사 결과

- `python3 -m py_compile work/scripts/build_reading_tiers.py`: exit 0.
- `python3 work/scripts/build_reading_tiers.py`: exit 0. CORE 47 / NEXT 257 / REFERENCE 444 / ARCHIVE 242 유지.
- `git diff --check`: 오류 출력 없음. Untracked R1 문서를 포함한 관련 Markdown 10개도 별도 whitespace 검사 통과.
- `python3 work/scripts/audit_repository.py`: exit 0, 오류 0·경고 0. Registry 990, intensive 304, history 47, 표준 notes 4,950, resources 496, index 990. Markdown 5,055개·links 8,652개, comparison rows 106/completed 5.
- 작업 시작 보호 snapshot 4,956개와 SHA-256 비교: 변경 0. PAPER/manifest/generator/tier/active·history tracker/표준 paper notes 보존.
- R1 증거 명세·source ledger·L1 design JSON parse와 상태 확인 통과. `executable=false`, `implemented=false`, `policy_rollouts=0`; 현재 handoff는 R1 DONE/gate NOT_MET → R2 WAITING_EVIDENCE다.
- Ledger 고유 URL 36개 = 성공 32개 + 404 응답 4개. 성공 text/metadata bytes 합계 3,089,503, SHA-256 형식·URL 중복 검사 통과. 응답 수를 code file 수로 부르지 않는다.
- Raw 파일 metadata 200개와 L1 annotation 200개의 stem 일치, 차집합 0. 해당 listing의 다음 페이지 Link 없음. 성능·관측 가능성 검사 결과가 아니다.
- 새 artifact 4개: R1_REVIEW, R1_EVIDENCE_REQUIREMENTS, r1_sources JSON, 이 검증 문서. L1 source ledger와 validation은 당시 기록으로 보존했고 design에 최신 handoff만 추가했다.

### 증거 경계

- Source ledger는 URL별 마지막 조회의 identity·SHA-256·접근 실패를 기록한다. GitHub issue/API metadata·논문 HTML·source text를 포함하며 전부 code file 수로 세지 않는다. 조회 성공은 source의 모든 주장 검증을 의미하지 않는다.
- 200개 raw file과 기존 200개 annotation의 stem 비교는 **metadata 연결 검사**다. Binary payload checksum·실제 trajectory·Cooked timestamp·RGB cue는 확인하지 않았다.
- 공개 저자의 skill 수치는 우리의 독립 재현 결과가 아니다. P2 skill evaluator의 미공개 경계와 P4 checkpoint 미식별을 유지한다.
- Simulation·policy inference·학습·Docker/resource preflight·package 설치를 하지 않았다. Weight·Parquet trajectory·HDF5·video·PDF를 다운로드/저장하지 않았다. Source/metadata는 메모리에서 읽고 identity와 분석만 보존했다.
- 사용자 reading status·registry/tier를 바꾸지 않았다. 외부 메시지 발송·계정 로그인·gated 조건 수락은 없었다.
