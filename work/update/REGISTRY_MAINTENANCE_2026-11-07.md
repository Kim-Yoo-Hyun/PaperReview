# Registry 최신화·직접 선행 등록·중복 정리

- Work ID: **REG-R11** / 2026-11-07 KST
- 범위: 전체 registry의 로컬 identity·분류·노트·링크·생성 view 감사와 최근 HINDSIGHT 검토의 미등록 직접 선행 5편 확인. 전체 논문의 최신 게재·본문을 웹으로 전수 조사한 것은 아니다.
- [처리·보존·검증 원장](../sources/registry_maintenance_2026-11-07.json) · [등록 입력](../sources/registry_admissions_2026-11-07.json) · [현재 TODO](../../TODO.md)

<a id="admissions"></a>

## 추가한 직접 선행

| 논문·registry ID | 검증한 출판 상태·범위 | 등록 이유·주의점 |
|---|---|---|
| [LfH, pr-1113](../../2026/arXiv/2026_arXiv_Learning-from-Hindsight-for-VLA-Reinforcement-Learning/01_overview.md) | [arXiv v2](https://arxiv.org/abs/2607.09042), 2026. Main-conference 채택 미확인 | 실패의 보조 목표와 원 지시를 함께 RL로 학습하는 직접 선행. Project의 과거 제목은 alias로 연결하며 별도 논문을 만들지 않음. Code placeholder를 공개 구현으로 표시하지 않음 |
| [SPRINT, pr-1114](../../2024/ICRA/2024_ICRA_SPRINT-Scalable-Policy-Pre-Training-via-Language-Instructi/01_overview.md) | [IEEE-deposited metadata](https://api.crossref.org/works/10.1109/ICRA57147.2024.10610606), ICRA 2024; 저자 abstract/README | 언어 재라벨·skill chaining의 offline RL 계보. 저장소 heading의 Semantic은 alias이며 공식 DOI 제목을 사용 |
| [SOAR, pr-1115](../../2024/CoRL/2024_CoRL_Autonomous-Improvement-of-Instruction-Following-Skills-via/01_overview.md) | [PMLR paper](https://proceedings.mlr.press/v270/zhou25b.html)·[volume](https://proceedings.mlr.press/v270/): CoRL 행사2024 / proceedings 발행2025 | 자율 수집·image-goal 재라벨 시스템과 단일 VLA RL을 구분하는 대조. 공식 project가 연결하는 [code release](https://github.com/soar-autonomous-improvement/code-release)로 기존 조사 원장의 URL을 교정 |
| [ReinFlow, pr-1116](../../2025/NeurIPS/2025_NeurIPS_ReinFlow-Fine-tuning-Flow-Matching-Policy-with-Online-Rein/01_overview.md) | [NeurIPS 2025 공식 proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/98d6f928497d9eaad9f320fb2db3040d-Abstract-Conference.html) | Flow 경로의 학습 noise·likelihood를 online RL과 연결하는 비교 방법. 최신 repository의 VLA 지원을 원 논문 실험으로 소급하지 않음 |
| [CAST, pr-1117](../../2025/arXiv/2025_arXiv_CAST-Counterfactual-Labels-Improve-Instruction-Following-i/01_overview.md) | [arXiv](https://arxiv.org/abs/2508.13446): 최초2025 / 최신 v2는2026. Main venue 미확인 | Counterfactual instruction/action 증강과 실제 실패의 참인 hindsight 라벨을 구분하는 직접 대조 |

Exact/normalized title·alias·DOI/arXiv/OpenReview 중복을 확인했고 registration dry-run은 5편 모두 신규로 판정했다. 각 5개 표준 노트와 source·artifact metadata를 작성했다. 신규 논문은 **NEXT·UNREAD·ABSTRACT_CHECKED**로 시작한다. Dossier의 지정 본문/code 검토와 paper note 전체의 정독은 구별한다. 기존 1,112편의 tier·사용자 읽기 이력을 바꾸지 않았다.

## 삭제·병합 범위

- `tmp/pdfs/` 아래 과거 visual-QA PNG **15개, 6,296,364 bytes**를 삭제했다. 현재 문서·코드의 참조가 없고 재현 입력도 아닌 임시 렌더다. 파일별 이전 hash·크기는 원장에 남겼다. 논문 PDF·표준 노트·source review manifest는 삭제하지 않았다.
- Root README의 수동 트랙별 집계는 생성된 읽기 계획으로 통합했다. Root에는 필수 snapshot만 남기고 research/synthesis의 중복 후보 현황은 주제 index·TODO로 연결했다. HINDSIGHT의 오래된 비교 초안은 현행 N2 계약과 차별적 대조 설명으로 합쳤다. 과거 판정·N2 연구 계약·P0 실행 코드는 유지한다.
- 완전히 같은 bytes인 `reactive_nav_pilot`/`reactive_nav_contract`의 `docker_version.json` 2개는 서로 다른 실행 당시 증거여서 각각 보존했다. 비슷한 topic별 launcher/requirements도 동결된 실행 계약과 fingerprint에 속하므로 공통 파일로 임의 병합하지 않았다.
- 사용되지 않는 host package/dependency가 있다는 근거는 없었다. 환경 설치·패키지 삭제·Docker 실험·PDF/weight 다운로드·git commit/push는 수행하지 않았다.

## 현행 규모와 검증

전체 **1,117편·표준 노트5,585개**, **CORE47 / NEXT339 / REFERENCE489 / ARCHIVE242**다. Active386 / history47이며 기존 사용자 입력428건을 보존하고 새5건만 UNREAD로 추가했다. Source evidence는 FULL_TEXT_CHECKED967 / ABSTRACT_CHECKED150이다. Resource593·curated relation49개이며 새 source 연결을 검증된 citation edge로 자동 승격하지 않았다.

등록 dry-run/apply, tier 생성기 compile/rebuild, priority-only reconcile, cue catalog/resource/index/stats 재생성을 완료했다. 읽기 이력 검사6개와 `git diff --check`를 통과했고 repository audit는 Markdown5,801개·내부 링크12,184개, **오류0 / 경고0**이다. 기존 metadata1,112편·표준 노트5,560개·읽기 입력428건·주제별 재현 자료85개·과거 실험 근거·staged 변경을 보존했다. HINDSIGHT 실행 fingerprint도 동일하다. 실제 수치·검증 범위는 위 원장의 `validation`에 기록했다. Native 정책·연구 효과 검증과 별개다.

다음 연구 행동은 HINDSIGHT-P0의 호환 local NVIDIA 검증이다. 이번 registry 등록이나 cache 정리로 연구 가설·출판 가능성·실험 준비의 native 검증 상태를 승격하지 않는다.
