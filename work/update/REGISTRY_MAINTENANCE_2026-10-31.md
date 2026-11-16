# Registry 최신화·중복 정리 — 2026-10-31

- Task: `REG-R5`
- 범위: 최근 연구 검토의 registry 누락 보완, 현재 안내 동기화, 두 검토 보고서 병합, 대소문자 경로의 Linux 이식성 수정.
- [등록 입력](../sources/registry_admissions_2026-10-31.json) · [병합·경로·보존 검증 ledger](../sources/registry_maintenance_2026-10-31.json)
- 기존 dirty worktree를 출발점으로 삼았다. 전체 논문의 최신 게재 상태를 전수 재조사한 것은 아니다.

## 1. Registry 보완

| 신규 논문 | 확인한 status/source | 등록 이유 |
|---|---|---|
| [ReSteer · pr-1075](../../2026/RSS/2026_RSS_ReSteer-Quantifying-and-Refining-the-Steerability-of-Multi/01_overview.md) | [RSS 2026 공식 proceedings](https://roboticsproceedings.org/rss22/p143.html), [project](https://resteer-vla.github.io/), [code](https://github.com/ChenZhenY/ReSteer) | 상태별 지시 전환 능력과 현재 P0 실행의 직접 선행 |
| [Causeway · pr-1076](../../2026/arXiv/2026_arXiv_Causeway-Restoring-Task-Accessibility-for-Instruction-Swit/01_overview.md) | [arXiv 2026](https://arxiv.org/abs/2609.30913). Peer-reviewed venue와 공식 code는 이번 확인 범위에서 미확인 | 물리적 접근 가능성의 실패를 의미 갱신 오류와 구분할 경쟁 설명 |
| [How-level instruction following · pr-1077](../../2026/arXiv/2026_arXiv_Do-VLAs-Really-Follow-Instructions-Diagnosing-How-Level-In/01_overview.md) | [arXiv 2026 v2](https://arxiv.org/abs/2610.21251), [code](https://github.com/sangwu99/how-level-vla-Arxiv). Preprint | 수행 조건 준수·행동 반응·목표 성공을 분리하는 진단과 SIMPLER-IN |

정확한 title/특징 구절·arXiv/DOI를 기존 manifest와 대조하고 등록기의 dry-run 뒤 추가했다. 세 논문은 모두 VLA primary track의 NEXT다. 공개 code가 있는 두 편도 재현 완료로 표시하지 않았다. Hi Robot·SwitchVLA·Mobi-π·Behavior-Skill은 기존 entry를 유지했다. 발견한 다른 preprint를 수량 확보 목적으로 추가하지 않았다.

현재 **1,077편 / CORE 47 · NEXT 302 · REFERENCE 486 · ARCHIVE 242**, active reading 349행·history 47행이다. 표준 노트는 **5,385개**다. 신규 15개는 `ABSTRACT_CHECKED`, 신규 읽기 행은 `UNREAD`이며 기존 지정 본문/code 검토는 원래 source ledger의 범위로 보존한다. SIMPLER-IN을 benchmark 탐색 vocabulary에 추가했고 benchmark 53·metric 29·통합 resource 555개를 생성했다. 자동 resource 연결은 계속 `cue_only`다.

## 2. 병합·삭제와 보존

- 두 후보의 같은 날 GPU 전 보고서를 [단일 검토 문서](./PRE_GPU_BUILDUP_REVIEW_2026-10-31.md)로 병합하고 원본 MD 2개를 삭제했다. 제목 수준 변경을 제외한 본문은 각각 원래 SHA256으로 복원·대조했다. 주제별 anchor를 사용해 brief·TODO·synthesis·casebook·실행 README의 참조를 바꿨고, 모바일 조작 JSON 설정도 새 파일로 연결했다.
- 주제별 brief 2개, 공유 source ledger, 고유한 과거 문헌/준비 보고서, 실행 recipe·원시 결과·checkpoint/source hash는 보존했다. 보고서 병합으로 의미 갱신 계약이나 단일 scene-template 제한을 삭제하지 않았다.
- Root/research/synthesis/work/update 안내의 현재 후보·다음 단계·registry 수치를 동기화했다. Synthesis 첫 화면의 오래된 “다음은 실행 준비”를 준비 완료/실제 실행 대기로 수정했다.
- 내용이 완전히 같은 파일은 두 실행의 `docker_version.json` 한 쌍이었다. 각각의 run provenance이므로 유지했다. `.pyc`·`.DS_Store`·임시/backup 파일과 host 가상환경·node_modules·site-packages는 발견되지 않았다. 삭제할 근거가 없는 dependency 명세는 유지했다.
- PDF, 모델·dataset, 설치 package, Docker image/container/volume은 이번 유지보수에서 다운로드·설치·삭제하지 않았다. Docker/GPU probe나 실험도 실행하지 않았다.

## 3. Linux 경로 문제와 생성기 보완

대소문자를 구별하지 않는 현재 filesystem의 `exists()` 검사는 3개 manifest 경로 불일치를 놓쳤다. `Preview-Control` 논문의 실제 `Using` 폴더를 manifest의 `using`에 맞췄고, 네 논문이 섞여 있던 `2022/arxiv` parent를 `2022/arXiv`로 통일했다. 기존 두 entry의 lowercase parent 참조는 manifest·source review 경로·문서 링크에서 수정했다. Leaf slug와 paper ID, 논문 내용은 바꾸지 않았다.

Git이 case-only 이동을 기록하도록 두 디렉토리를 임시 이름을 거쳐 `git mv`했다. **25개 파일의 경로 변경만 index에 올라갔으며 이전 index blob/mode는 모두 보존**했다. 기존 미커밋 note 수정 내용은 추가 staging하지 않았다. Commit/push는 수행하지 않았다.

읽기 생성기는 case-only 경로 변경에서 **유일한 새 경로와 같은 stable paper ID**가 확인될 때만 기존 사용자 필드를 이관한다. 임의의 누락 경로나 다른 ID는 계속 실패한다. REFERENCE/ARCHIVE 이력도 stable ID로 보존하도록 보완했고 기존 CFG의 REFERENCE 판단을 명시적으로 유지했다. Active/history 경로 이동·잘못된 ID·기존 tier 보존 회귀 검사를 추가했다.

Repository audit는 실제 디렉토리 entry의 대소문자를 확인하도록 강화했다. 이 수정은 경로 문제를 예방하며, 다른 컴퓨터의 Docker/native 실행까지 검증했다는 뜻은 아니다.

## 4. 검증

최종 전체 audit는 **오류 0 / 경고 0**이다. 논문 1,077편·표준 노트 5,385개·집중 읽기 349행·Markdown 5,583개·링크 11,199개를 검사했다. Reading history 회귀 검사 6개·문서 유지보수 검사 6개, 수정 Python 5개의 compile, 생성 view 14개 재실행 불변성, staged/unstaged `git diff --check`를 통과했다. 전체 표준 노트의 C0/C1 제어문자 잔여는 0개다.

보존 검사에서는 기존 표준 노트 5,370개 내용, 기존 active/history 393행의 모든 사용자 입력, 기존 tier 전체가 유지됨을 확인했다. 기존 1,074개 manifest record는 두 paper의 경로 치환을 제외하고 동일하다. 병합한 두 보고서의 본문과 Git index blob도 보존했다. 이 검증은 문서·경로·생성기의 검사이며 연구 효과를 측정한 결과가 아니다.

## 5. 다음 행동

[TODO](../../TODO.md)의 지시 수정 P0-R1과 모바일 조작 P0 자원 대기를 유지한다. 신규 registry 등록과 문서 병합은 native 실행·정책 효과·독립 논문 가치 입증이 아니다. [현재 두 후보의 비실험 검토](./PRE_GPU_BUILDUP_REVIEW_2026-10-31.md)에서 정한 비교 범위·미구현 사항을 다음 최소 실행에 적용한다.
