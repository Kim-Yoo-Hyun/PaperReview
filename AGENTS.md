# PaperReview Agent Operating Guide

- Updated: 2026-08-28 KST

이 파일은 `PaperReview/`와 모든 하위 디렉토리에 적용된다. 이 저장소에서 논문을 조사·추가·분류·요약·합성하는 에이전트는 아래 규칙을 기본 계약으로 따른다.

## 1. Mission and Research Stance

이 저장소는 논문을 최대한 많이 모으는 목록이 아니다. **Robotics를 주 연구축으로 삼아, foundation에서 최신 연구까지 읽고 비교하여 연구 질문으로 연결하는 장기 literature system**이다.

연구축의 우선관계는 다음과 같다.

1. **Robotics:** planning, control, RL/IL, manipulation, contact, locomotion, whole-body/mobile manipulation, safety, world models, data and evaluation.
2. **VLA:** robot policy interface와 scaling paradigm. Language 이해 자체보다 action representation, robot data, embodiment transfer, control frequency, memory, feedback, safety를 본다.
3. **3D Vision:** robot state estimation과 behavior를 바꾸는 enabling stack. Reconstruction benchmark 자체보다 manipulation, navigation, SLAM, semantic memory, active perception, collision avoidance에 주는 효과를 본다.

항상 다음 폐루프를 기준으로 논문을 해석한다.

`observation → state/world model → task & motion decision → policy/control → contact → feedback/failure recovery`

Humanoid는 별도 taxonomy로 만들지 않는다. Locomotion, whole-body control, imitation, mobile/loco-manipulation 안에 포함한다.

## 2. Non-Negotiable Rules

- PDF 보유 여부는 중요도, tier, 읽기 순서, 완료 여부의 기준이 아니다.
- PDF가 없다는 이유로 논문을 제외하거나 낮은 tier로 내리지 않는다.
- PDF 확보를 작업의 blocker나 품질 문제로 보고하지 않는다. 사용자가 필요할 때 직접 확보한다.
- `paper.pdf`는 선택적 local cache다. 사용자 요청 없이 다운로드하거나 삭제하지 않는다.
- 논문 수와 venue quota를 채우기 위해 약한 논문을 추가하지 않는다.
- 오래된 foundation과 최근 trend를 분리해 평가하되, 최근 논문이라는 이유만으로 승격하지 않는다.
- 3D Vision 논문은 downstream robot behavior와의 연결을 명시할 수 있을 때만 CORE/NEXT 우선순위를 높인다.
- 자동 생성 노트가 존재한다는 사실을 실제 정독으로 간주하지 않는다.
- 불확실한 정보는 추측해서 채우지 말고 `확인 필요`, `abstract 기반`, `본문 수동 확인 필요`처럼 provenance를 표시한다.
- 기존 dirty worktree와 사용자 변경을 보존한다. 관련 없는 파일을 되돌리거나 정리하지 않는다.

### Update Direction

- 새 논문은 실제 paper folder와 5개 표준 note file로 등록한다. `paper.pdf`는 선택 사항이다.
- `PAPER.md`는 전체 registry와 topic navigation에 집중한다.
- 읽기 우선순위, tier, 장기 순서, 연구 관점은 `READING_PLAN.md` 하나에 통합한다.
- `README.md`의 snapshot, 문서 링크, workflow는 registry와 생성 결과가 바뀔 때 함께 갱신한다.
- 향후 추가는 dataset/benchmark, canonical task formulation, field-shaping foundation, 최신 핵심 trend-flow를 incremental method보다 우선한다.

## 3. Repository Sources of Truth

| Artifact | Role | Editing rule |
|---|---|---|
| [PAPER.md](./PAPER.md) | 전체 872편 registry와 topic navigation | 구조를 유지한다. 논문 추가 시 row와 실제 folder가 일치해야 한다. |
| [READING_PLAN.md](./research/READING_PLAN.md) | 우선순위 기준, 연구 관점, 읽기 순서, CORE/NEXT 장기 정독 목록 | `build_reading_tiers.py`가 생성한다. 직접 수정하지 않는다. |
| [READING_TIERS.csv](./research/READING_TIERS.csv) | 전체 registry의 단일 tier assignment | 생성 파일. 직접 수정하지 않는다. |
| [READING_STATUS.csv](./research/READING_STATUS.csv) | 190편 정독 진행 상태와 사용자 분석 | 상태·분석 필드는 직접 편집 가능. 생성기는 기존 입력을 보존해야 한다. |
| [READING_STATUS.md](./research/READING_STATUS.md) | 상태값과 완료 규칙 | 상태 정의 변경 시 tracker와 synthesis 규칙도 함께 점검한다. |
| [synthesis/](./synthesis/) | 7개 트랙의 cross-paper comparison과 paper lineage | queue marker 내부는 자동 생성, 나머지는 수동 합성 영역이다. |
| [RESEARCH_GAPS.md](./research/RESEARCH_GAPS.md) | 트랙을 가로지르는 failure·assumption·evaluation gap | gap 설명의 canonical source다. |
| [RESEARCH_IDEAS.md](./research/RESEARCH_IDEAS.md) | gap에서 파생한 가설과 최소 실험 | gap 내용을 복제하지 않고 gap ID를 참조한다. |
| [research/projects/](./research/projects/) | 구현 직전 scoped project의 executable specification | gap/idea보다 구체적인 환경·checkpoint·option/method contract·baseline·metric·ablation·reject rule·freeze artifact를 관리한다. |
| [work/update/UPDATES_2026-08-28.md](./work/update/UPDATES_2026-08-28.md) | 최신 registry·frontier·gap 갱신 기록 | 날짜별 audit log로 유지하고 canonical gap/plan 내용을 중복 관리하지 않는다. 앞으로의 update log도 `work/update/`에 작성한다. |
| [work/scripts/build_reading_tiers.py](./work/scripts/build_reading_tiers.py) | tier·plan·tracker·synthesis queue 생성 규칙 | CORE/NEXT membership의 canonical source다. |
| [work/sources/papers.json](./work/sources/papers.json) | 전체 registry metadata의 canonical manifest | 신규 등록은 `register_papers.py`를 사용한다. |
| [work/scripts/audit_repository.py](./work/scripts/audit_repository.py) | registry·tier·tracker·queue·note·taxonomy 무결성 검사 | read-only이며 주요 변경 전후에 실행한다. |

현재 snapshot은 CORE 77편, NEXT 113편, REFERENCE 449편, ARCHIVE 233편이다. 이 숫자는 결과이지 목표 quota가 아니다. 논문 중요성 때문에 필요하면 CORE/NEXT를 늘릴 수 있으며, 장기 정독 규모 100–150편은 운영상 가이드일 뿐 hard cap이 아니다.

## 4. Canonical Robotics Taxonomy

모든 CORE/NEXT 논문은 아래 7개 primary track 중 하나에만 배정한다. Cross-cutting 성격은 tags와 synthesis 연결로 표현하며 논문을 중복 등록하지 않는다.

1. **Planning and control**
2. **RL, IL, offline learning, and robot data**
3. **Manipulation, contact, tactile, and dexterity**
4. **VLA and generalist robot policies**
5. **World models, safety, uncertainty, and recovery**
6. **Locomotion, whole-body, mobile manipulation, and humanoids**
7. **Robotics-enabling 3D perception**

새 논문이 여러 축에 걸치면 논문의 핵심 contribution과 가장 직접적인 evaluation을 기준으로 primary track을 정한다. 예를 들어 tactile VLA라도 핵심 contribution이 high-frequency force feedback이면 manipulation/contact에, generalist action interface면 VLA에 둔다.

## 5. Tier Policy

### CORE

CORE는 후속 연구를 판단하기 위한 공통 좌표계다. 다음 기준을 복수로 만족해야 한다.

- 여러 Robotics 세부 분야가 반복해서 의존하는 conceptual or algorithmic foundation이다.
- 후속 논문의 문제 설정, objective, action/control interface를 이해하기 위한 prerequisite다.
- 특정 benchmark나 일시적 architecture를 넘어 개념적 수명이 길다.
- 실제 robot의 closed-loop action/control, contact, adaptation, deployment에 직접 연결된다.
- 표준 baseline, 대표 system, 공개 생태계 또는 연구 패러다임을 형성했다.
- 3D/VLM foundation이라면 이후 robot policy나 state representation을 이해하는 데 필수다.

CORE 승격 시 “유명하다”가 아니라 **어떤 후속 논문을 이해하는 데 왜 필요한지**를 한 문장으로 기록한다.

### NEXT

NEXT는 CORE를 전제로 읽는 전문화·확장·frontier다.

- CORE의 명확한 한계나 빈틈을 보완한다.
- 특정 embodiment, sensor, contact regime, task, data setting을 깊게 다룬다.
- 최근 연구 흐름을 대표하며 연구 아이디어와 직접 연결된다.
- real-robot 또는 설득력 있는 physics evaluation이 있다.
- cross-embodiment, long-horizon, tactile/force VLA, world model, humanoid, active 3D처럼 선택한 연구축에 따라 중요도가 커진다.
- 아직 장기 foundation인지 확정되지 않았더라도 강한 비교 기준이나 새로운 interface를 제공한다.

### REFERENCE

- 중요한 foundation, baseline, dataset, benchmark, survey이지만 현재 190편 정독 흐름의 prerequisite는 아니다.
- 특정 실험이나 아이디어를 설계할 때 찾아 읽는다.
- `READING_PLAN.md`의 CORE/NEXT와 비교해 중요한 논문이 REFERENCE에 남아 있지 않은지 정기적으로 승격 감사한다.

### ARCHIVE

- 현재 robotics-first 연구 범위와 직접 연결되지 않는다.
- 삭제 대상이 아니라 검색·역사 자료다.
- 연구축이 바뀌면 언제든 REFERENCE/NEXT/CORE로 승격할 수 있다.

Tier 결정에서 PDF, 로컬 노트 개수, 다운로드 성공 여부는 절대 사용하지 않는다.

## 6. Internet Research Protocol

### Discovery and authority

외부 awesome list, survey repository, lab reading list는 **후보 발견과 taxonomy 비교**에만 사용한다. 논문 metadata와 status의 최종 근거로 사용하지 않는다.

출처 우선순위는 다음과 같다.

1. 공식 conference/journal proceedings 또는 publisher page
2. 공식 OpenReview forum, CVF Open Access, PMLR, RSS proceedings, conference program/award page
3. 저자·연구실 project page와 공식 code repository
4. arXiv abstract/PDF
5. Semantic Scholar, DBLP 등 index
6. GitHub awesome list, 블로그, 소셜 미디어

최신 정보, venue, acceptance, award, 발표 연도는 반드시 인터넷으로 재검증한다. 공식 발표가 확인되지 않으면 venue를 추정하지 말고 `arXiv` 또는 `under review / status unverified`로 둔다.

### Search scope

- 최근 trend window는 원칙적으로 현재 연도를 포함한 최근 3개 calendar year다. 2026년 기준 2024–2026이다.
- 우선 venue: NeurIPS, CVPR, ECCV, ICCV, ICRA, CoRL, ICLR, IROS.
- Robotics relevance가 높으면 RSS, T-RO, RA-L, IJRR, Science Robotics, ICML, 3DV, SIGGRAPH/TOG도 포함한다.
- Venue별 수를 맞추지 않는다. 연구 흐름을 형성하거나 gap을 메우는 논문만 선택한다.
- Survey와 curated repo의 `latest` 목록은 후보 생성에 쓰고, seminal/foundation은 citation lineage와 후속 사용을 따로 확인한다.

### Web research output

새 논문마다 최소한 다음을 확보한다.

- 정확한 title, year, venue/status
- official paper or abstract URL
- project/code URL if public
- primary track과 tags
- foundation/current-trend/benchmark 중 역할
- 기존 CORE/NEXT와의 관계
- 왜 지금 이 registry에 추가해야 하는지

직접 인용은 최소화하고 사실은 paraphrase한다. 웹 조사 결과를 보고할 때는 claim 근처에 직접 근거 링크를 둔다.

## 7. Paper Admission and Deduplication

논문을 추가하기 전에 다음을 모두 확인한다.

1. `rg -i`로 exact title과 distinctive title phrase를 `PAPER.md`, `READING_TIERS.csv`, `work/sources/*.json`에서 검색한다.
2. punctuation, subtitle, `+`, Greek symbol, arXiv→conference version 차이를 정규화해 중복을 검사한다.
3. Conference version이 생기면 별도 논문으로 중복 등록하기보다 기존 entry의 venue/status를 갱신하는 것을 우선한다.
4. 같은 연구의 tech report와 peer-reviewed version을 모두 남겨야 한다면 차이와 이유를 명시한다.
5. 새 논문이 기존 gap을 실제로 메우는지, 단지 비슷한 방법 하나를 더 추가하는지 판단한다.

다음 중 하나 이상을 충족해야 신규 등록할 가치가 있다.

- field-shaping foundation
- top-tier의 강한 최신 흐름
- 기존 taxonomy의 명백한 missing link
- 새로운 robot embodiment/contact/sensing/control regime
- 비교에 필요한 standard baseline, dataset, benchmark
- 실험 또는 연구 아이디어의 직접적 prerequisite

제외 또는 ARCHIVE 유지 사유:

- 제목/키워드만 Robotics이고 action/control과 연결되지 않음
- 공식 status와 기본 metadata를 검증할 수 없음
- 기존 논문과 실질적 차이가 없음
- evaluation 없이 과도한 claim만 있음
- 현재 연구축과 연결 설명이 불가능함

## 8. Directory and Naming Convention

논문 폴더는 다음 구조를 유지한다.

```text
<year>/<venue>/<year>_<venue>_<title-slug>/
```

- 표시 title은 공식 title을 그대로 쓴다.
- 폴더 slug는 기존 script의 ASCII-safe/truncated convention을 따른다.
- 이미 등록된 폴더를 cosmetic consistency만을 위해 mass rename하지 않는다.
- Markdown link는 repository-relative path를 사용한다.
- Year/venue hierarchy와 `PAPER.md` row가 일치해야 한다.
- `+`, `%2B`, Unicode symbol이 있는 경로는 실제 filesystem과 URL encoding 차이를 검증한다.

각 paper folder의 표준 파일은 다음과 같다.

```text
01_overview.md
02_problem.md
03_method.md
04_evaluation.md
05_insights.md
paper.pdf            # optional, non-canonical
```

## 9. Per-Paper Note Standard

노트는 metadata 재서술이 아니라 읽기와 비교를 가능하게 하는 evidence-backed 분석이어야 한다.

### Common header

가능한 경우 모든 노트에 다음을 기록한다.

- 정확한 title
- year / verified venue or status
- primary category and tags
- official paper/abstract URL
- project/code URL
- source audit: full text, abstract only, official project, manually reviewed date

PDF 경로를 필수 metadata로 두지 않는다.

### `01_overview.md`

- 해결하는 문제와 왜 중요한지
- 핵심 아이디어 2–4개
- observation/input, state representation, output/action
- main claims와 실제 contribution
- 명시적 limitation과 evaluation scope
- 이 논문을 읽어야 하는 이유 한 문장

### `02_problem.md`

- target problem과 기존 방법의 bottleneck
- 논문이 두는 핵심 가정
- 선행 연구 대비 바뀐 문제 formulation
- Robotics closed loop에서 이 문제가 나타나는 위치

### `03_method.md`

- system/policy/control pipeline
- objective, loss, optimization 또는 control law
- observation/state/action representation
- temporal horizon, control rate, memory, planner/controller interface
- training/inference 차이와 중요한 implementation choice

수식과 수치는 근거가 있을 때만 기록한다.

### `04_evaluation.md`

- embodiment, robot hardware/simulator, task
- dataset size/source와 train/test generalization setting
- benchmark, metric, baseline, ablation
- real-robot 여부와 trial count
- 주요 결과는 비교 가능한 수치와 조건을 함께 기록
- failure case, negative result, reproducibility constraints

단순 keyword match로 dataset이나 metric을 추론하지 않는다. 예를 들어 논문 본문에 이름이 등장했다는 이유만으로 실제 evaluation dataset으로 기록하지 않는다.

### `05_insights.md`

명확히 두 층으로 나눈다.

1. **Paper-supported conclusion:** 논문의 evidence가 직접 지지하는 결론
2. **Researcher interpretation:** 현재 연구 방향에서의 재사용, 반박, 확장 아이디어

다음을 포함한다.

- 무엇이 실제로 새로웠는가
- 가장 강한 가정과 취약한 failure mode
- 어떤 CORE 논문에서 출발했고 어떤 NEXT 논문으로 이어지는가
- 최소 재현 실험
- 연구 gap과 falsifiable research question

Generic한 “3D와 VLA를 결합할 수 있다” 문장을 반복하지 않는다. 해당 논문의 method/evaluation에서 도출되는 구체적 연결만 쓴다.

### Evidence failure

Full text를 확인하지 못했으면:

- abstract로 확인 가능한 내용만 작성한다.
- method detail, exact metric, limitation을 만들어내지 않는다.
- `abstract 기반 — 본문 확인 필요`를 표시한다.
- 자동 추출이 깨졌거나 affiliation/reference가 본문처럼 들어가면 해당 문장을 버린다.

## 10. Registry and Priority Notation

`PAPER.md` table은 기존 column을 유지한다.

```text
Year | Venue | Paper | Tags | PDF | Code/Project
```

PDF column은 compatibility를 위해 남아 있을 수 있지만 curation decision에는 사용하지 않는다. PDF가 없어도 paper overview와 official source가 있으면 정상 entry다.

표기 원칙:

- Venue는 공식 표기를 사용한다: `NeurIPS`, `ICRA`, `RA-L`, `T-RO`, `arXiv` 등.
- `poster`, `oral`, `spotlight`, award는 공식 source로 확인된 경우만 추가한다.
- Code가 없으면 `not released`와 `not identified`를 구분한다.
- Tags는 너무 넓게 늘리지 말고 search에 유용한 3–7개를 사용한다.
- 한 논문을 여러 category section에 복제하지 않는다. Cross-link만 허용한다.

우선순위와 읽기 순서는 `READING_PLAN.md` 하나에서 관리한다. 새 priority entry에는 단순 목록이 아니라 선정 이유와 연구 흐름을 함께 반영한다.

## 11. Reading Status Workflow

`READING_STATUS.csv`의 status는 다음 다섯 값만 사용한다.

| Status | Meaning |
|---|---|
| `UNREAD` | 읽기 시작 전 |
| `SKIMMED` | 문제, 기여, 핵심 그림과 실험 구조 파악 |
| `READ` | 방법과 실험을 정독하고 분석 필드 작성 |
| `SYNTHESIZED` | 같은 track 논문과 비교하고 research gap 반영 |
| `REPRODUCED` | 코드 실행 또는 핵심 실험 재현 |

`evidence_level`은 status와 별개이며 `CURATION_ONLY`, `ABSTRACT_CHECKED`, `FULL_TEXT_CHECKED`, `EXPERIMENT_CHECKED`만 사용한다. 최소 조합은 `SKIMMED + ABSTRACT_CHECKED`, `READ/SYNTHESIZED + FULL_TEXT_CHECKED`, `REPRODUCED + EXPERIMENT_CHECKED`다.

- 로컬 노트가 있다는 이유로 status를 올리지 않는다.
- 사용자의 실제 읽기 이력에 대한 근거가 없으면 `UNREAD`를 유지한다.
- `REPRODUCED`는 필수 최종 상태가 아니다. 이론·시스템 논문은 `SYNTHESIZED`에서 완료될 수 있다.
- 날짜는 `YYYY-MM-DD` 형식으로 기록한다.
- Tracker 재생성 시 `overview_path`를 key로 사용자 입력 필드를 보존한다.
- 상태와 분석 필드 정의는 [READING_STATUS.md](./research/READING_STATUS.md)를 따른다.
- gap과 idea의 evidence maturity는 `CURATION-HYPOTHESIS → READING-SUPPORTED → EXPERIMENT-SUPPORTED` 순서로만 올린다.

## 12. Cross-Paper Synthesis Workflow

논문 하나를 `READ`로 바꿀 때 해당 [synthesis](./synthesis/) 문서에 비교 행을 추가한다.

각 synthesis 문서는 다음 구조를 유지한다.

1. Scope
2. Reading Path
3. Generated Assigned Reading Queue
4. Comparison Matrix
5. Dependency and Evolution
6. Open Questions
7. Research Gaps

`<!-- READING_QUEUE:START -->`와 `<!-- READING_QUEUE:END -->` 사이를 직접 편집하지 않는다. 이 영역은 `build_reading_tiers.py`가 tracker 상태, evidence level과 논문 queue를 갱신한다. 현재 Comparison Matrix의 `CURATION-SEED` 행은 읽기 전 비교 가설이다. 정독 후 source location을 확인해 수동 수정하며, seed script를 다시 실행해 덮어쓰지 않는다.

`SYNTHESIZED`로 올리기 위한 최소 조건:

- tracker의 문제·interface·evaluation·failure field가 채워짐
- 같은 track의 선행/후속 논문과 차이가 comparison matrix에 기록됨
- Open Questions 또는 Research Gaps에 구체적이고 검증 가능한 함의가 추가됨

## 13. Automation and Safe Editing

### Tier or registry update

CORE/NEXT membership을 바꿀 때는 `READING_PLAN.md`나 CSV를 직접 고치지 말고 [build_reading_tiers.py](./work/scripts/build_reading_tiers.py)의 `CORE_GROUPS` / `NEXT_GROUPS`를 수정한다.

그다음 실행한다.

```bash
python3 work/scripts/build_reading_tiers.py
```

이 명령은 다음을 갱신한다.

- `READING_PLAN.md`
- `READING_TIERS.csv`
- `READING_STATUS.csv`의 자동 관리 필드
- 각 synthesis 문서의 generated reading queue

사용자가 tracker에 입력한 상태와 분석 필드는 같은 `overview_path`가 유지되는 한 보존되어야 한다. 생성기 수정 후 반드시 이를 검증한다.

### Paper registration and full rebuild safety

- 신규 metadata는 `python3 work/scripts/register_papers.py --input <json>`으로 dry-run한 뒤 `--apply`로 등록한다.
- `build_lit_survey.py`는 인자 없이 read-only다. metadata refresh, PDF download, note overwrite, registry/manifest write는 각각 명시적 flag 없이는 실행되지 않아야 한다.
- `--overwrite-notes`는 기존 수동 분석을 덮어쓰므로 사용자의 명시적 전체 재생성 요청 없이는 사용하지 않는다.
- `work/scripts/archive/`의 one-off script와 `work/archive/reports/`의 과거 report는 실행하거나 현재 source of truth로 사용하지 않는다.

### File editing

- 수동 수정은 `apply_patch`를 우선한다.
- 기존 사용자 변경과 겹치는지 먼저 `git status --short`로 확인한다.
- destructive command, mass rename, broad delete를 사용하지 않는다.
- 논문 PDF, notes, registry를 대량 삭제하거나 덮어쓸 때는 명시적 사용자 요청이 필요하다.
- 자동화 script를 실행하기 전에 영향을 받는 파일을 확인한다.

### Scoped project implementation gate

- broad motivation과 이미 존재하는 method family를 contribution으로 다시 주장하지 않는다. 최신 direct collision paper는 full text와 공개 code/interface까지 확인한다.
- primary claim, estimator, policy-visible input, action/option set, decision timing, budget, baseline fairness, metric, ablation, reject/revise rule을 구현 전에 고정한다.
- environment, repository commit, checkpoint, seed, perturbation, split과 cost unit은 manifest로 만들 수 있을 정도로 구체화한다.
- 문서에 적힌 계획과 실제 생성·검증된 artifact를 구분한다. 생성되지 않은 schema/manifest/test report는 unchecked 상태로 둔다.
- 가장 작은 pilot에서 precondition이 실패하면 복잡한 learned method를 구현하지 않고 protocol·evaluation 결과로 축소한다.

## 14. Required Validation

변경 범위에 맞춰 아래를 수행한다.

### Always

```bash
python3 -m py_compile work/scripts/build_reading_tiers.py
python3 work/scripts/build_reading_tiers.py
git diff --check
```

### Registry integrity

- `PAPER.md`의 declared total과 table row 수가 일치하는가
- 각 paper overview link가 실제 파일에 연결되는가
- exact title 또는 normalized title 중복이 없는가
- Year/venue/path가 서로 일치하는가

### Tier integrity

- 모든 registry paper가 정확히 하나의 `CORE/NEXT/REFERENCE/ARCHIVE` tier에 속하는가
- CORE/NEXT 사이에 중복이 없는가
- CORE/NEXT 모든 paper가 `READING_PLAN.md`와 `READING_STATUS.csv`에 나타나는가
- 190편이 7개 synthesis queue에 정확히 한 번씩 배정되는가
- Tier 판단에 PDF 상태가 들어가지 않았는가

### Tracker integrity

- 허용된 status 값만 사용하는가
- 허용된 evidence level만 사용하며 status와 최소 조합이 맞는가
- 기존 사용자 입력이 재생성 후 보존되는가
- CORE와 NEXT sequence가 연속적인가
- Tracker에 PDF 관련 column을 추가하지 않았는가

### Notes integrity

- 5개 표준 note file이 존재하는가
- 제목, venue, source URL이 일치하는가
- 자동 추출 artifact나 근거 없는 dataset/metric이 없는가
- paper claim과 researcher interpretation이 구분되는가

## 15. Task-Specific Operating Modes

### “논문을 더 찾아라”

1. 현재 registry와 gap을 먼저 감사한다.
2. GitHub curated lists와 survey를 discovery source로 사용한다.
3. 공식 proceedings/project/arXiv로 metadata와 contribution을 확인한다.
4. 중복을 제거하고 신규 가치가 있는 논문만 제안한다.
5. primary track, provisional tier, 기존 계보와의 관계를 정한다.
6. Registry, notes, roadmap/priority, tiers를 필요한 범위만 갱신한다.

### “우선순위를 바꿔라”

1. PDF와 현재 note 상태를 보지 않는다.
2. CORE/NEXT 기준으로 importance audit를 한다.
3. 제한을 맞추기 위해 중요한 논문을 기계적으로 강등하지 않는다.
4. Generator source를 수정하고 모든 derived artifact를 재생성한다.
5. 승격/강등 이유를 연구 dependency 관점에서 보고한다.

### “논문을 정리해라”

1. 실제 source 범위를 먼저 밝힌다.
2. 5개 note schema를 따른다.
3. Tracker를 `SKIMMED` 또는 `READ`로 올릴 충분한 근거가 있는지 판단한다.
4. 해당 synthesis matrix와 research gap을 갱신한다.
5. 단일 논문 요약으로 끝내지 않고 선행/후속 차이를 남긴다.

### “현황을 알려라”

질문의 기준을 먼저 분리한다.

- Registry composition: 전체 872편 기준
- Intensive reading: CORE+NEXT 기준 (현재 190편)
- Reading progress: `READING_STATUS.csv` 기준
- Priority, reading order, detailed robotics coverage: `READING_PLAN.md` 기준

서로 다른 분모를 섞어 비율을 보고하지 않는다.

## 16. Patterns Adopted from Public Curation Repositories

이 운영 방식은 공개 paper curation 저장소의 장점을 참고하되 이 repository에 맞게 더 엄격하게 적용한다.

- [Awesome Physical AI](https://github.com/keon/awesome-physical-ai): foundation, architecture, action representation, world model, learning, deployment, safety처럼 pipeline과 research question 중심으로 taxonomy를 구성한다.
- [Awesome Learning for Manipulation](https://github.com/Noietch/Awesome-Learning-for-Manipulation): seminal/foundational과 연도별 최신 논문을 분리하고, venue/year/link와 짧은 TL;DR을 함께 둔다.
- [Awesome VLA Study](https://github.com/MilkClouds/awesome-vla-study): foundation→frontier 읽기 순서, prerequisite, phase, cross-paper key points를 제공한다.
- [bipedal-robot-learning-collection](https://github.com/zita-ch/bipedal-robot-learning-collection): 논문 폭증 시 active curated list와 historical archive를 분리하고, real-robot relevance와 명확한 subproblem을 우선한다.
- [Awesome RL for Legged Locomotion](https://github.com/apexrl/awesome-rl-for-legged-locomotion): 논문 제목뿐 아니라 sim-to-real, state estimation, controller structure, real-world deployment의 핵심 차이를 설명한다.
- [Papers We Love contribution guide](https://github.com/papers-we-love/papers-we-love/blob/main/.github/CONTRIBUTING.md): 논문을 추가할 때 단순 링크가 아니라 왜 중요한지 짧은 정당화를 요구하고, PDF 재배포 권리를 별도로 확인한다.
- [Awesome 3D Reconstruction](https://github.com/openMVG/awesome_3DReconstruction_list): 목록이 exhaustive하지 않음을 인정하고 reproducible research, datasets, libraries를 논문 목록과 함께 관리한다.

이 저장소는 위 패턴에서 **taxonomy, reading order, importance justification, archive separation, reproducibility**를 채택한다. 반면 star 수, hype, venue quota, PDF availability는 채택하지 않는다.

## 17. Completion Report

작업을 마칠 때 다음만 간결하게 보고한다.

- 무엇을 조사·추가·변경했는가
- CORE/NEXT/REFERENCE/ARCHIVE에 어떤 영향이 있었는가
- 어떤 공식 source로 최신 status를 검증했는가
- 어떤 생성·검증 명령을 실행했는가
- 남은 실질적 uncertainty 또는 manual review 항목은 무엇인가

PDF 미보유 개수는 사용자가 직접 요청하지 않는 한 문제나 후속 과제로 보고하지 않는다.
