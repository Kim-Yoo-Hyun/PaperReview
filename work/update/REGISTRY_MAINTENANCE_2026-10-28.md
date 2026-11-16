# Registry 최신화·정리 — 2026-10-28

- Task: `REG-R4`
- Started: 2026-10-28 KST / final validation: 2026-10-29 KST
- Scope: 현재 registry·안내 문서·dependency/cache 정리. 기존 dirty worktree를 출발점으로 사용했다.
- [변경·삭제·보존·검증 ledger](../sources/registry_maintenance_2026-10-28.json)

## Registry 보완

| 신규 항목 | 확인한 출처·status | 등록 이유 |
|---|---|---|
| [Mobi-π](../../2025/CoRL/2025_CoRL_Mobi-pi-Mobilizing-Your-Robot-Learning-Policy/01_overview.md) · pr-1073 | [CoRL 2025 / PMLR](https://proceedings.mlr.press/v305/yang25b.html), [저자 project](https://mobipi.github.io/), [공식 code](https://github.com/yjy0625/mobipi) | 조작 정책에 적합한 base pose 선택을 다루는 HANDOFF 직접 선행. Whole-body/mobile manipulation NEXT |
| [Behavior-Skill](../../2026/arXiv/2026_arXiv_Behavior-Skill-A-Fine-Grained-Benchmark-for-Evaluating-Vis/01_overview.md) · pr-1074 | [arXiv 2026](https://arxiv.org/abs/2608.30536), [공식 code](https://github.com/nubot-nudt/Behavior-Skill). Peer-reviewed venue 미확인 | 복원된 시작 상태의 skill 평가와 실제 연결 실행을 비교할 현재 prerequisite. VLA NEXT |

두 논문은 최근 HANDOFF 검토에 쓰였지만 registry에 빠져 있었다. Title/alias·arXiv ID와 기존 manifest를 대조하고 등록기를 dry-run한 뒤 추가했다. 표준 노트 10개는 이번 공식 abstract/project 수준의 `ABSTRACT_CHECKED`, 사용자 읽기 상태는 `UNREAD`다. 기존 지정 본문·code 구간 검토는 [H1 source](../research_topics/mobile_policy_transfer/내용/sources.json), [H2 source](../research_topics/mobile_policy_transfer/내용/sources.json), [H3 source](../research_topics/mobile_policy_transfer/내용/sources.json)의 범위로 보존한다.

현재 **1,074편 / CORE 47 · NEXT 299 · REFERENCE 486 · ARCHIVE 242**, 집중 읽기 346편·history 47편이다. 표준 노트는 5,370개다. 모든 1,074편의 최신 게재 상태를 다시 조사한 전수 문헌 검토는 아니다. 현재 직접 선행의 누락 보완과 전체 로컬 무결성 검사다. 기존 Semantic Handoff는 [arXiv 서지](https://arxiv.org/abs/2607.06256)의 RSS SemRob Workshop 표기를 확인했지만 main-track 논문으로 승격하거나 이번 등록에 추가하지 않았다.

## 병합·삭제와 보존

- TODO의 완료 행 **45개**를 [단일 완료 이력](./TASK_HISTORY_2026-10-28.md)으로 이동했다. ID·판정·근거는 보존하고 상대 링크만 재배치했다. TODO에는 활성/대기와 직전 완료만 남긴다.
- Root README, research/synthesis/work/update 안내의 반복된 현재 상태·과거 목록을 줄이고 canonical 문서로 연결했다. Registry snapshot·읽기 queue·catalog·resource/index를 동기화했다.
- 실험 index에 HANDOFF P0를 연결하고 P3 안내의 오래된 “후속 비교 미실행” 문장을 P3 범위와 이미 완료된 P4 결과로 구분했다. P0의 native image/adapter/manifest 미완료와 기존 연구 gate는 유지한다.
- Python bytecode 12개와 `.DS_Store` 1개, 총 **475,951 bytes**를 삭제했다. Host 가상환경·node_modules·vendored site-packages는 발견되지 않았으며 host package 설치/삭제는 수행하지 않았다.
- C3 portable Docker recipe와 parent 관계로 특정한 private/reclaimable 빌드 캐시 **18개**, Docker 보고 **584MB**를 제거했다. [공식 ID filter](https://docs.docker.com/reference/cli/docker/buildx/prune/#provide-filter-values---filter)를 이용했고 대상 밖 15개 record는 보존했다. 전체 system/image/volume prune은 하지 않았다. 재빌드 recipe와 hash 고정 requirements는 남아 있으며 다음 C3 build에는 dependency 재확보가 필요하다.
- Portable replay의 NumPy는 NPZ 재분석에, P3 이미지의 RVO2는 저장 결과 재분석에 사용된다. C1 Dockerfile은 당시 환경 근거다. 사용처가 있는 dependency 명세·실행 코드·checkpoint/source hash를 삭제하지 않았다.
- 기존 P3 image `paper-gap-p3:rvo-c2c46ba`와 무관한 `minikube` volume은 보존했다. 실행 중/종료 container는 0개였다. 동일 내용의 `docker_version.json` 2개는 서로 다른 run의 provenance이므로 유지했다.
- 기존 논문 노트·PDF·source ledger·원시 trace·연구 판정·사용자 읽기 기록은 삭제하지 않았다. 새 실험·학습·PDF 다운로드도 수행하지 않았다.

## 검증

- 전체 audit: **오류 0 / 경고 0**. 1,074편·5,370개 표준 노트·346개 queue·Markdown 5,559개·링크 11,051개 검사 통과.
- 기존 1,072편 manifest record와 tier를 보존했다. 기존 표준 노트 5,360개는 작업 전 SHA256과 모두 같고, active/history 합계 391행의 사용자 입력도 보존했다. 신규 2행은 `UNREAD`다.
- 완료 TODO 45행은 상대 링크 변환을 제외하고 동일하며 대기/PARTIAL 9행도 보존했다. 기존 dirty 파일의 임의 삭제·이전 삭제 파일의 복원은 없다.
- 읽기 이력 테스트 3개·문서 유지보수 테스트 5개, 두 생성 script compile, 생성 view 14개의 재실행 불변성, `git diff --check` 통과.
- Priority-only dry-run은 paper/header 변경 0이다. 신규 tag의 대소문자 불일치를 발견해 기존 `VLA` 표기와 맞췄고 재검사를 통과했다.
- Benchmark 52·metric 29·통합 resource 552개를 생성했다. 자동 resource 연결은 계속 `cue_only`이며 실제 evaluation role의 증거로 사용하지 않는다.

## 다음 행동

[TODO](../../TODO.md)의 HANDOFF-P0 자원 대기를 유지한다. [재개 준비](../research_topics/mobile_policy_transfer/재현%20방법/README.md#execution)에서 현재 컴퓨터의 로컬 Docker 조건을 확인하고, 충족 시 허용된 최소 실행을 진행한다. 이번 유지보수만으로 연구 효과·신규성·native 실행 가능성을 입증하지 않는다. Git commit/push는 이번 범위에 포함하지 않았다.
