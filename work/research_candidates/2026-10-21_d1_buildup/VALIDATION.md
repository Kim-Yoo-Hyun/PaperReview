# 단계별 검증 기록 — d1_buildup

2026-10-23 통합. 각 절은 원래 날짜·범위·검사 결과를 보존한다. 당시 registry 수치는 역사적 snapshot이며 정책 효과나 현재 재개 자격을 뜻하지 않는다.

<a id="stage-0"></a>

## VALIDATION.md

D1 / registry 변경 검증

2026-10-21. 이 문서는 repository 무결성 검사이며 D1의 VLA 효과 검증이 아니다.

- Before: 974편, CORE 47 / NEXT 246 / REFERENCE 439 / ARCHIVE 242; standard note 4,870개. 사전 audit 오류·경고 0.
- After: 990편, CORE 47 / NEXT 257 / REFERENCE 444 / ARCHIVE 242; intensive 304편, standard note 4,950개.
- Registration: 16편 dry-run accepted, identifier/title collision 0; `--apply`로 등록. 기존 974편의 record와 4,870개 note는 작업 전 snapshot으로 보호했다.
- 새 NEXT 11편의 상태는 UNREAD, evidence는 ABSTRACT_CHECKED. 기존 293개 active row에서 생성 sequence만 달라지며 사용자 상태·분석을 보존한다. Inactive history 47편은 유지한다.
- 실행한 생성 명령: `register_papers.py` dry-run/apply, `build_reading_tiers.py`, `build_registry_catalogs.py` dry-run/apply, `build_registry_views.py --apply`.
- 최종 `py_compile`, reading-tier 재생성, repository audit, `git diff --check` 통과. Markdown 5,028개·링크 8,316개, 오류 0·경고 0. [validation_result.json](./validation_result.json)에 실제 결과를 기록했다. 기존 974개 record와 4,870개 note, 사용자 tracker 분석·history의 보존을 재확인했다. 기존 수동 synthesis matrix 106행·completed 5행은 유지한다.
- Docker의 stdlib 반례와 public-source read만 수행했다. 19개 upstream source/config/README, 179,227 bytes를 container 내에서 읽었으며 host에는 짧은 evidence cue와 hash만 남겼다.
- Native policy inference·physics rollout·training update는 모두 0회. Runtime·source·script/result hash는 [runtime_manifest.json](./runtime_manifest.json)을 따른다.
- 소유한 Python image와 전용 `--rm` container를 정리했다. 정리 후 container 0개·image 0개이며 기존 `minikube` volume은 보존했다. Inventory와 결과 hash 일치도 validation JSON에서 확인했다.

남은 substantive gate: 실제 VLA clean competence/input-use, matched baseline headroom, 일부 direct collision 전체 method/code, 외부 연구자 피드백. 문헌과 합성 분석을 정책 실험 완료로 승격하지 않는다.


<a id="stage-1"></a>

## BASELINE_VALIDATION_2026-10-22.md

D1 baseline 문헌 확보 — repository 검증

2026-10-22. 문헌·source identity·문서 무결성 검사이며 정책 성능 검증이 아니다.

- 사전 `audit_repository.py`: 990편, 4,950개 표준 note, intensive 304, 오류 0·경고 0.
- 작업 전 manifest·PAPER·tier generator·tier/tracker/history·표준 note 4,956개 파일의 hash snapshot 생성.
- 신규 산출물: baseline dossier와 4개 repository / 9개 source 파일의 정적 기록, update log.
- `python3 -m py_compile work/scripts/build_reading_tiers.py`: exit 0.
- `python3 work/scripts/build_reading_tiers.py`: exit 0; CORE 47 / NEXT 257 / REFERENCE 444 / ARCHIVE 242.
- `python3 work/scripts/audit_repository.py`: exit 0; registry 990, intensive 304, history 47, 표준 note 4,950, Markdown 5,031개·상대 링크 8,349개. 오류 0·경고 0.
- `git diff --check`: exit 0. 기존 dirty worktree를 되돌리지 않았다.
- 작업 전 hash와 최종 hash를 비교한 **4,956개 파일 모두 동일**. 전체 paper manifest·PAPER·tier generator·tier/tracker/history·4,950개 표준 note가 보존됐다. Synthesis manual comparison matrix는 106행, completed 5행 유지.
- 새 source JSON 파싱 확인: 4개 repository, 9개 source 파일, 110,878 bytes의 읽기 근거, checkpoint 목록 25개. Weight payload는 내려받지 않았으며 repository revision을 payload hash라고 부르지 않는다.

이번 연구 코드 실행·policy inference·simulation·training·dependency 설치·PDF 다운로드는 모두 0회다. Repository 생성·문서 검사와 연구 실험을 구분한다. 과거 diagnostic 결과나 runtime manifest를 이번 실행 결과로 바꾸지 않았다.


<a id="stage-2"></a>

## TODO_VALIDATION_2026-10-22.md

TODO와 D1-L1/L2 후속 — 검증 기록

2026-10-22 KST. 이전 baseline 검증과 구분한 이번 후속 문서 변경의 기록이다. 정책 성능 검증이 아니다.

### 범위

- Root TODO 생성, 직접 방법 감사·source 기록·주장/증거 계약 작성, 기존 dossier/pilot/navigation/log 갱신.
- 사전 repository audit: 990편, CORE 47 / NEXT 257 / REFERENCE 444 / ARCHIVE 242, intensive 304, history 47, 표준 note 4,950. 오류 0·경고 0.
- 작업 전 manifest·PAPER·tier generator·tier/tracker/history·표준 note를 포함한 4,956개 파일 hash snapshot을 보존 검증에 사용한다.
- 연구 policy/physics/training 실행, dependency 설치, model/data/PDF 다운로드는 없다. 공개 코드의 AST 정적 파싱은 실행·import와 구분한다.

### 최종 유지보수 검사

- `python3 -m py_compile work/scripts/build_reading_tiers.py`: exit 0.
- `python3 work/scripts/build_reading_tiers.py`: exit 0. Tier 47 / 257 / 444 / 242 유지.
- `python3 work/scripts/audit_repository.py`: exit 0. Registry 990, intensive 304, history 47, 표준 note 4,950, Markdown 5,035개·상대 링크 8,407개. 오류 0·경고 0.
- `git diff --check`: exit 0. 새 Markdown 4개의 trailing whitespace도 별도 검사하여 0건.
- 새 source JSON 파싱 성공: 고정 GAP commit, 9개 source/config metadata, 27개 blob tree. 정적 파싱 결과는 training 파일 1개 오류·다른 Python 3개 통과이며 policy 실행 결과가 아니다.
- 작업 전 hash와 대조한 **4,956개 파일 모두 동일**. Manifest·PAPER·tier generator·tier/tracker/history·4,950개 표준 note를 보존했다. 기존 dirty worktree를 되돌리지 않았다.
- Synthesis manual comparison matrix 106행·completed 5행 유지. 추가한 것은 Open Questions의 후속 문헌·분석 링크이며 사용자 읽기 상태 승격이 아니다.

D1-L1/L2는 정의한 문헌·분석 산출물 범위에서 DONE이다. D1-L3는 READY이며 아직 task 적합성 확인이나 정책 실험을 완료하지 않았다. 기존 Oct21 실험 결과·runtime manifest와 첫 Oct22 baseline validation은 덮어쓰지 않았다.

최종 evidence 판정은 [claim 계약](./CLAIM_EVIDENCE_CONTRACT.md)을 따른다. 문서/registry 검사 통과를 D1 연구 효과의 입증으로 해석하지 않는다.


<a id="stage-3"></a>

## TASK_VALIDATION_2026-10-22.md

D1-L3 task·관측 경로 감사 — repository 검증

2026-10-22 KST. Task/source 문서와 보존 상태의 검증이며 VLA 효과·runtime 검증이 아니다.

- 사전 audit: 990편, tier 47 / 257 / 444 / 242, intensive 304, history 47, 표준 note 4,950, Markdown 5,035·상대 링크 8,407. 오류 0·경고 0.
- 신규 artifact: task/observability 감사, source identity JSON, 실행 불가능한 task 후보 JSON, 이 검증 기록. 기존 문서·TODO·log 갱신.
- 보존 검사: 작업 전 4,956개 manifest·PAPER·tier generator·tier/tracker/history·표준 note의 hash snapshot 생성.
- `python3 -m py_compile work/scripts/build_reading_tiers.py`: exit 0.
- `python3 work/scripts/build_reading_tiers.py`: exit 0. CORE 47 / NEXT 257 / REFERENCE 444 / ARCHIVE 242 유지.
- `python3 work/scripts/audit_repository.py`: exit 0. Registry 990, intensive 304, history 47, 표준 note 4,950, Markdown 5,037개·상대 링크 8,435개. 오류 0·경고 0.
- `git diff --check`: exit 0. 새 Markdown 2개와 TODO의 trailing whitespace 검사도 0건.
- Source JSON: unique revision/path 90개, text 618,642 bytes, task definition 40개와 5종 atomic predicate 집계 일치. 오류 record 없음. SHA-256 identity 형식 확인.
- 후보 JSON: ID 0/8/1/7의 suite/order/slug·goal·prompt·BDDL hash를 source 기록과 대조하여 일치 확인. `executable=false`, runtime freeze false, 초기 상태 index·clean success는 null 유지.
- 작업 전 snapshot과 비교한 **4,956개 파일 모두 동일**. Manifest·PAPER·tier generator·tier/tracker/history·4,950개 표준 note 보존. 기존 사용자 변경을 되돌리지 않았다.
- Synthesis manual comparison matrix 106행·completed 5행 유지. D1-L3 링크는 Open Questions에만 추가했다.

D1-L3 DONE은 source 기반 task·interface 심사 완료를 뜻한다. D1-L4는 READY이며 새 policy 효과·실제 observation visibility·공정 paired reset은 미검증이다. 이전 실험 결과, runtime manifest, 앞선 validation 기록은 덮어쓰지 않았다.

연구 실험·upstream code import·package 설치·weight/data/PDF payload 다운로드는 하지 않았다. 공개 text를 메모리에서 읽고 구조·해시를 기록했으며 이를 native 재현으로 표시하지 않는다.


<a id="stage-4"></a>

## CONTRACT_VALIDATION_2026-10-22.md

D1-L4 비실험 계약 — repository 검증

2026-10-22 KST. 문서·설계 artifact의 정합성 검증이며 simulator/runtime·정책 효과 검증이 아니다.

- 사전 audit: registry 990, CORE 47 / NEXT 257 / REFERENCE 444 / ARCHIVE 242, intensive 304, history 47, 표준 note 4,950, Markdown 5,037개·상대 링크 8,435개. 오류 0·경고 0.
- 신규 artifact: [계약](./PRE_EXPERIMENT_CONTRACT.md), [설계 spec](./PILOT_SPEC.json), [source identity](./contract_sources_2026-10-22.json), 이 검증 기록. TODO·후속 문서·navigation·log를 갱신했다.
- 작업 전 4,956개 canonical manifest·PAPER·tier generator·tier/tracker/history·표준 note의 SHA-256 snapshot을 생성했다.

- `python3 -m py_compile work/scripts/build_reading_tiers.py`: exit 0.
- `python3 work/scripts/build_reading_tiers.py`: exit 0. CORE 47 / NEXT 257 / REFERENCE 444 / ARCHIVE 242 유지.
- `python3 work/scripts/audit_repository.py`: exit 0. Registry 990, intensive 304, history 47, 표준 note 4,950, Markdown 5,039개·상대 링크 8,473개. 오류 0·경고 0.
- `git diff --check`: exit 0. 신규 4개 artifact의 별도 trailing-whitespace 검사도 0건.
- JSON 정합성: task/policy/source revision 대조, task ID 0/8/1/7의 일치, 38-query 상한, G1 140 episode·calibration 24개, G2 method당 280 episode 상한의 산술 일치 확인. 이는 실행 수나 성능 검증이 아니다.
- Source identity: unique revision/path 8개, 공개 text 160,928 bytes. 그중 L3에서 확인한 6개는 hash가 같고 2개는 추가 source다. SHA-256 형식 및 revision/path 중복 검사를 통과했다.
- Spec은 executable=false, runtime freeze false, 모든 baseline implemented=false, G0–G4 NOT_RUN이다. 실제 payload·split ledger·holdout 통계 계약은 null/미확보로 남겼다.
- 작업 전 snapshot과 비교한 **4,956개 파일 모두 동일**. Manifest·PAPER·tier generator·tier/tracker/history·4,950개 표준 note를 보존했다. 기존 사용자 변경을 되돌리지 않았다.
- Synthesis comparison matrix 106행·completed 5행 유지. D1-L4 링크는 Open Questions 영역에만 추가했다.
- 현재 TODO의 L4는 DONE이고 다음은 E1 WAITING_RESOURCE다. 이전 날짜/단계의 validation과 update log의 과거 READY 기록은 역사적 snapshot으로 보존했다.

실험 episode는 0이다. 공개 text를 메모리로 읽고 source identity를 기록했으며 upstream code 실행·패키지 설치·model/data/PDF payload 다운로드를 하지 않았다. Spec은 executable=false, baseline 구현과 native G0–G4는 모두 미실행이다. 기존 10-21 실행 artifact와 앞선 validation 기록은 보존했다.


<a id="stage-5"></a>

## NONEXPERIMENTAL_VALIDATION_2026-10-22.md

D1-N1–N4 비실험 재심사 문서 검증

- 날짜: 2026-10-22 KST.
- 대상: [결과](./NONEXPERIMENTAL_REVIEW.md), [source 기록](./nonexperimental_sources_2026-10-22.json), 현재 TODO·navigation·설계 JSON.
- 검증 성격: repository 유지보수. 정책·simulator·학습·수치 실험 결과가 아니다.

### 검증 기록

| 검사 | 실제 결과 |
|---|---|
| 변경 전 audit_repository.py | 990편, errors 0 / warnings 0 |
| python3 -m py_compile work/scripts/build_reading_tiers.py | exit 0 |
| python3 work/scripts/build_reading_tiers.py | exit 0; CORE 47 / NEXT 257 / REFERENCE 444 / ARCHIVE 242 |
| 변경 후 audit_repository.py | 5,043개 Markdown / 8,522개 상대 링크 검사; errors 0 / warnings 0 |
| git diff --check | exit 0 |
| 보호 파일 SHA256 비교 | 4,956개 모두 동일; 표준 note 4,950개·manifest·PAPER·tier generator·tier CSV·active/history tracker 보존 |
| JSON·TODO 교차 검사 | N1–N4 DONE, R2 WAITING_EVIDENCE, E1/E2 HOLD_RESEARCH 일치; executable=false |
| 새 review를 가리키는 fragment 링크 | 7개 anchor 확인 |
| Source 재확인 | 고정 commit의 6개 text 파일 SHA256가 기존 기록과 일치 |

Registry는 990편, 집중 tracker 304행·history 47행, comparison 106행·completed 5행으로 유지된다. 위 명령은 유지보수 검사이며 모델·simulator를 실행하지 않았다. 기존 dirty diff 전체를 이번 수정량으로 집계하지 않는다.

### 보존 범위

작업 전 manifest·PAPER·tier generator·tier CSV·active/history tracker와 4,950개 표준 note를 포함한 4,956개 파일의 hash snapshot을 만들었다. 기존 dirty worktree를 유지하고 과거 실험 결과·source snapshot·validation 기록을 덮어쓰지 않았다. 신규 paper admission·tier 변경·사용자 reading status 승격은 없다.

### Evidence 경계

직접 문헌의 지정 절·표 및 공개 source를 읽었으며 최신 ReViP 연결 원문과 G-PSMR 전체 table/실행 자산의 접근 한계는 남는다. N1–N4 DONE은 이 범위의 검토 완료다. Native 효과 검증과 외부 피드백은 미완료이며 E1/E2는 연구 보류다.
