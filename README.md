# PaperReview — Robotics-first Literature System

- Snapshot verified: 2026-11-18 KST

`PaperReview`는 **VLA + RL + Computer Vision + Robotics**를 연구하는 문헌 저장소다. 최신 요청의 [물체 자세·능동 관측 / 3D 재구성·로봇 추정 탐색](./work/update/NEW_FIELD_SCOUT_2026-11-17.md#pose-reconstruction)에서 새 후보 두 개를 정리했다. [작업에 필요한 pose 모호성의 능동 관측](./work/research_topics/pose_active_perception/내용/README.md)은 N1/N2 비실험 검토와 행동 양립성 비교 명세를 완료했다. 이어 Docker recipe·custom evaluator·VLA 후보 IO probe를 작성했고 현재 로컬 daemon 연결 실패로 native 검증을 대기한다. [재개 방법·미검증 범위](./work/research_topics/pose_active_perception/재현%20방법/README.md#p0-preparation)를 남겼다. [조작 허용 오차를 반영하는 3D 추정](./work/research_topics/task_geometry_estimation/내용/README.md)은 두 번째 초기 후보다. 앞선 [접촉 관계 기반 RL 탐색](./work/research_topics/relation_exploration/내용/README.md)은 P0 코드 준비 후 native 검증 대기를 유지한다. [주제 index](./work/research_topics/README.md)는 유지3·예비1·새 탐색의 성숙도를 구별하고, [TODO](./TODO.md)는 다음 행동을 관리한다. 기존 7개 [폐기 판단](./work/research_topics/retired/README.md)은 유지한다. 새 두 후보의 신규성·정책 효과·실행 환경은 아직 확립되지 않았다.

최신 [REG-R17](./work/update/REGISTRY_MAINTENANCE_2026-11-18.md)에서 pose/active perception·3D geometry·RL exploration 직접 선행18편을 보강하고 SaPaVe·ActiveAlign을 NEXT로 조정했다. 앞선 Ψ₀ 등록·정확성 보완 범위는 [REG-R16](./work/update/REGISTRY_ACCURACY_PSI0_2026-11-16.md)에, 실험 준비·실제 확인·미구현 범위는 각 주제의 `재현 방법/`에 둔다. 문서와 제어 검사 완료를 정책 성능이나 독립 연구 기여의 증거로 해석하지 않는다.

핵심 폐루프는 다음과 같다.

```text
observation → state / belief / world model → task & motion decision
→ policy / control → contact → feedback / failure detection / recovery
```

Registry의 수집·정리 범위는 다음과 같다.

- **Robotics:** planning, control, RL/IL, offline learning, manipulation, contact, locomotion, whole-body control, safety, recovery를 중심에 둔다.
- **VLA:** language understanding 자체보다 action representation, feedback, latency, memory, embodiment transfer, long-horizon execution을 본다.
- **3D Vision:** 독립적인 reconstruction 성능보다 state estimation, spatial memory, active perception, collision/contact reasoning, robot control에 주는 효과를 본다.
- **Humanoid:** 별도 축이 아니라 locomotion, whole-body control, imitation, mobile/loco-manipulation 안에서 다룬다.

## Contents

- [빠른 탐색](#빠른-탐색)
- [현재 snapshot](#현재-snapshot)
- [어떤 종류의 논문이 있는가](#어떤-종류의-논문이-있는가)
- [읽는 방법](#읽는-방법)
- [문서 구조와 note 규칙](#문서-구조와-note-규칙)
- [논문 추가와 provenance 규칙](#논문-추가와-provenance-규칙)
- [Curation and maintenance policy](#curation-and-maintenance-policy)
- [공개 registry 참고](#공개-registry-참고)

## 빠른 탐색

| 목적 | 문서 |
|---|---|
| 지금 할 일·직전 완료·보류 사유 | [TODO](./TODO.md) |
| 전체 논문·검색·통계 | [PAPER](./PAPER.md), [registry index](./research/REGISTRY_INDEX.csv), [stats](./research/REGISTRY_STATS.md) |
| 읽기 순서·상태·buildup 절차 | [research 안내](./research/README.md), [READING_PLAN](./research/READING_PLAN.md), [buildup guide](./research/IDEA_BUILDUP_GUIDE.md) |
| 논문 간 비교·연구 공백 | [7개 synthesis와 교차 질문](./synthesis/README.md) |
| 검색 방향·석사 연구 적합성 | [분야별 검색 지도](./research/IDEA_BUILDUP_GUIDE.md#search-map-2026-11-17), [11/17 후보 폐기·선정](./work/update/CANDIDATE_TRIAGE_2026-11-17.md) |
| 유지 3개·예비 1개·새 탐색의 가능성·재현 방법 | [통합 index](./work/research_topics/README.md) — 기여 판단·준비/실제 실행 범위의 대표 문서 |
| 과거 후보의 결과·GPU 후속·한계 | [16개 주제별 요약](./work/research_candidates/summaries/README.md) |
| Clone 후 실행 준비·실험 근거 | [주제별 준비 상태·재현 안내](./work/research_topics/README.md), [과거 실험 index](./work/experiments/README.md), [C3 저장 결과 replay](./work/experiments/portable/README.md) |
| Canonical identity·source·resource | [papers.json](./work/sources/papers.json), [schema](./work/sources/registry.schema.json), [resources](./work/sources/resources.json) |
| 유지보수·최신 보강 | [work 안내](./work/README.md), [11/18 직접 선행·정합·게시](./work/update/REGISTRY_MAINTENANCE_2026-11-18.md) |
| 완료 작업·과거 source/검증 | [update index](./work/update/README.md), [10/23–28 작업 이력](./work/update/TASK_HISTORY_2026-10-28.md) |


## 현재 snapshot

| 항목 | 수치 |
|---|---:|
| 전체 registry / 표준 노트 | **1,224편 / 6,120개** |
| CORE / NEXT / REFERENCE / ARCHIVE | **50 / 424 / 508 / 242편** |
| 집중 읽기 / inactive history | **474 / 47편** |
| 사용자 READ 기록 | **5편: active 1 / history 4** |
| Source evidence | **FULL_TEXT_CHECKED 968 / ABSTRACT_CHECKED 256편** |
| Canonical category / primary reading track | **23 / 7개** |
| 전체 연도 / 최근 2024–2026 | **1960–2026 / 931편** |

연도·venue·source·resource 집계는 [REGISTRY_STATS](./research/REGISTRY_STATS.md)를 따른다. [11/16 보완](./work/update/REGISTRY_ACCURACY_PSI0_2026-11-16.md)에서 Ψ₀·EgoDex·Humanoid Everyday를 추가하고 AMO의 OCR 설명·SONIC의 공개 코드/식별자를 바로잡았다. 전체 구조·중복·링크를 검사했으며 전체1,224편의 과학적 내용을 전수 재검증한 것은 아니다. 과거 등록 규모·검토 범위는 [update index](./work/update/README.md)에 보존한다.

`FULL_TEXT_CHECKED`는 기록된 source 검토 범위이며 사용자 정독 완료나 모든 문장·실험 수치의 정확성을 인증하지 않는다. 기존 950편의 PDF 기반 기록과 후속 18편의 지정 본문 절 확인을 구분한다. 과거 OCR·추출·원문 대조의 cohort/예외는 [source review 기록](./work/sources/fulltext_all_review_manifest_2026-09-02.json)과 [품질 검토 이력](./work/update/README.md)에 보존한다. FlowDreamer의 safety 템플릿 해석 수정은 11/06 기록이다.

`CORE/NEXT`는 quota가 아니다. PDF 유무나 문서 수로 중요도·읽기 상태를 결정하지 않는다. Structured profile·공개 코드 링크는 실행 재현성의 증거가 아니다.

## 어떤 종류의 논문이 있는가

### Intensive reading set의 연구 트랙

7개 트랙별 CORE/NEXT 수와 queue는 [읽기 계획](./research/READING_PLAN.md)에 통합한다. Planning/control, RL/IL/data, manipulation/contact, VLA/generalist, world model/safety, locomotion/mobile manipulation, robotics-enabling 3D를 비교하며 이 문서에 별도 수동 집계표를 유지하지 않는다.

전체 registry의 canonical category는 더 세분화되어 VLA/generalist, 3D vision-language, scene representation, embodied navigation, robot data, world models/safety, locomotion, manipulation/contact, planning/control foundation 등 23개로 관리된다. 자세한 분류는 [PAPER.md](./PAPER.md)와 [READING_TIERS.csv](./research/READING_TIERS.csv)에서 검색한다.

현재 연구 질문·기여 경계와 준비 상태는 [주제 index](./work/research_topics/README.md), 실제 다음 행동은 [TODO](./TODO.md), 등록·비교·실행의 과거 근거는 [update index](./work/update/README.md)에 통합했다. 이 안내에 같은 완료 이력을 반복하지 않는다.

## 읽는 방법

읽기 우선순위는 [READING_PLAN.md](./research/READING_PLAN.md)에서 관리한다. VLA manipulation, RL/IL, action representation, navigation/mobile manipulation, action-relevant 3D, evaluation/recovery의 dependency를 따라 읽는다. 현재 새 연구 탐색은 VLA + RL 결합을 우선하되 registry의 기존 tier를 일괄 변경하지 않는다. 해당 branch의 CORE 선행 개념을 이해하면 NEXT를 병행하며, CORE 전체 완독을 시작 조건으로 두지 않는다. 오래된 논문도 최신 방법의 objective나 interface를 이해하는 데 필요하면 유지한다.

논문을 읽을 때는 다음 네 가지를 모두 기록한다.

- 문제 설정과 핵심 가정
- observation/state/action/control interface
- embodiment, task, data, metric, baseline, failure mode
- 현재 연구에서 재사용·반박·확장할 지점

## 문서 구조와 note 규칙

```text
<year>/<venue>/<year>_<venue>_<short-title>/
├── 01_overview.md
├── 02_problem.md
├── 03_method.md
├── 04_evaluation.md
└── 05_insights.md
```

- `01_overview.md`: paper별 human-readable canonical metadata와 문제, 핵심 아이디어, interface, contribution, limitation
- `02_problem.md`: `Problem in One Sentence` → `System and Scope` → `Formal Problem Formulation` → prior bottleneck/변경점 → assumption/failure boundary → closed-loop 위치; paper metadata는 `01_overview.md`를 참조
- `03_method.md`: method one-liner/rationale, source cues, module별 pipeline(input→operation→output→benefit→evidence), objective/update rule, variable table, observation–state–action interface, horizon/rate/memory, training-vs-inference, 04 baseline/ablation link와 reproduction checklist; metadata는 `01_overview.md`를 참조
- `04_evaluation.md`: evaluation type/scope, experimental matrix, dataset/benchmark role, embodiment/environment, metric/success definition, baseline fairness, ablation/sensitivity, claim–evidence map, generalization/failure, statistics/efficiency/reproducibility; 반복 metadata는 `01_overview.md`를 참조
- `05_insights.md`: paper-supported conclusion과 researcher interpretation, 선행/후속 연결, 최소 재현과 반증 가능한 질문; metadata는 `01_overview.md`를 참조

새 논문은 [work/sources/papers.json](./work/sources/papers.json)을 canonical manifest로 등록한다. 각 record는 `paper_id`를 내부 안정 ID로 사용하고, 가능한 경우 DOI/arXiv/OpenReview identifier와 `relations`에 version/same-work 또는 명시적인 계보·dependency 관계를 기록한다. relation은 `from` paper → `paper_id` target 방향의 directed edge이며, curated edge에는 type, confidence, basis, official source, evidence scope, review date를 남긴다. 이는 exhaustive citation graph가 아니므로 `inferred` 관계는 family-level 해석임을 명시한다. 출판 정보(`publication`), source URL(`sources`), artifact availability(`artifacts`), canonical `primary_track`, curation rationale·role·facet와 provenance를 note의 분석 내용과 분리해 저장한다. `provenance.content_evidence`는 paper-level 검토 근거이고, `provenance.note_evidence`는 5개 note별 근거다. PDF는 선택적 local cache이며 paper inclusion이나 priority를 결정하지 않는다.

검색을 위한 [REGISTRY_INDEX.csv](./research/REGISTRY_INDEX.csv)와 [resources.json](./work/sources/resources.json)은 manifest·tier·tracker에서 생성되는 보조 view다. resource view에는 benchmark/dataset, metric, code/project를 함께 두되, 기존 benchmark/metric 연결은 모두 `cue_only`로 유지한다. 따라서 dataset의 실제 role/split, metric의 공식 정의, code의 재현 가능성은 각 paper note와 원문에서 다시 확인한다. `provenance.review`는 paper-level source이고, targeted `05_insights` pass는 `provenance.note_review["05_insights.md"]`에 별도로 기록한다. 별도의 catalog를 계속 늘리지 않고, 기존 cue catalog는 생성 입력으로만 유지한다.

## 논문 추가와 provenance 규칙

이 저장소는 exhaustive bibliography가 아니라 **근거와 연구 연결을 보존하는 curated registry**다. 새 논문은 다음 admission checklist를 통과해야 한다.

1. `PAPER.md`, `READING_TIERS.csv`, `work/sources/papers.json`에서 제목·subtitle·conference version과 DOI/arXiv/OpenReview identifier 중복을 확인한다.
2. 공식 proceedings, publisher, OpenReview, CVF/PMLR/RSS page 또는 저자 project page에서 title·year·venue/status를 확인한다.
3. primary category, tags, `foundation / method / system / benchmark_or_dataset` 역할, 필요하면 coarse facet과 registry에 추가하는 이유를 기록한다.
4. `register_papers.py`로 stable `paper_id`, structured source/publication/provenance field와 5개 표준 note를 만든다. human-readable metadata는 `01_overview.md`에 한 번만 기록하고, 나머지 note는 canonical metadata pointer를 둔다. Abstract/project 내용을 확인했으면 `ABSTRACT_CHECKED`, 단순 후보 정리면 `CURATION_ONLY`로 기록한다. `UNVERIFIED`·`확인 필요`는 개별 claim의 설명이며 tracker evidence enum이 아니다.
5. CORE/NEXT를 바꿀 때는 CSV를 직접 수정하지 않고 `build_reading_tiers.py`의 canonical group을 수정한다.
6. `build_reading_tiers.py`, `reconcile_registry.py --priorities-only` dry-run과 `--apply`, `build_registry_views.py --apply`, `audit_repository.py`, `git diff --check`를 순서대로 실행한다. 등록기는 taxonomy를 적용하므로 전체 `normalize_taxonomy.py`는 taxonomy 변경 시에만 사용한다. Schema migration, 전체 evidence/profile reconciliation과 catalog 갱신은 [작업별 유지보수 절차](./work/README.md#safe-workflow)를 따른다.

논문을 정독한 뒤에는 `05_insights.md`, `READING_STATUS.csv`, 해당 synthesis matrix를 함께 갱신한다. 개인 note의 해석과 paper가 직접 보고한 결과를 분리한다. 별도 research-gap/idea/project overlay는 현재 삭제 정책에 따라 활성 문서로 유지하지 않는다. 과거 판단은 `work/update/`와 `research/projects/`의 명시적으로 폐기된 보존본에 남긴다.

## Curation and maintenance policy

- 2024–2026은 현재 robotics/VLA frontier와 benchmark를 넓게 수집한다.
- 오래된 foundation은 후속 연구의 prerequisite이거나 연구 문제를 정의하면 포함한다.
- 최신 논문은 venue 이름보다 method novelty, closed-loop relevance, evaluation quality, open-question 연결을 우선한다.
- Foundation, frontier, benchmark, dataset, safety/recovery, enabling perception을 서로 다른 역할로 구분한다.
- 논문 수나 venue quota를 채우기 위해 약한 논문을 추가하지 않는다.
- 공식 proceedings/project/abstract를 우선 사용한다. 문서의 evidence level과 개별 claim의 `확인 필요` 표기를 구분하며, note의 source 검토를 사용자의 정독으로 간주하지 않는다.
- 생성·검증 workflow는 [work/README.md](./work/README.md)에 있다.

```bash
python3 work/scripts/audit_repository.py
python3 work/scripts/register_papers.py --input /path/to/new_papers.json
python3 work/scripts/register_papers.py --input /path/to/new_papers.json --apply
python3 -m py_compile work/scripts/build_reading_tiers.py
python3 work/scripts/build_reading_tiers.py
python3 work/scripts/reconcile_registry.py --priorities-only
python3 work/scripts/reconcile_registry.py --priorities-only --apply
python3 work/scripts/build_registry_views.py --apply
python3 work/scripts/audit_repository.py
git diff --check
```

현재 snapshot의 상세 변경은 [최신 update log](./work/update/UPDATES_2026-10-25.md), 운영 규칙은 [AGENTS.md](./AGENTS.md)에 기록한다.

## 공개 registry 참고

README와 운영 방식은 다음 공개 paper/resource registry의 장점을 참고하되, 이 저장소의 robotics-first 연구 workflow에 맞게 변형했다.

- [Awesome Physical AI](https://github.com/junyuan-fang/awesome-physical-ai): `classic / must-read / project / code / benchmark` 역할을 구분하는 legend와 논문·dataset·simulator를 함께 보여주는 방식.
- [Awesome-VLA](https://github.com/KwanWaiPang/Awesome-VLA): 연도·venue·paper·repository·note를 한 행에 두고, 짧은 설명과 기여 안내를 제공하는 방식.
- [Awesome VLA/WAM](https://github.com/wangskyone/awesome-VLA-WAM): agentic robotics, world-action models, failure/recovery, efficient deployment처럼 현재 active direction을 먼저 제시하는 방식.
- [Awesome VLA](https://github.com/DravenALG/awesome-vla): VLA의 정의와 scope boundary를 먼저 명시하고, research flow를 계보로 설명하는 방식.
- [Papers We Love](https://github.com/papers-we-love/papers-we-love): contribution guideline, 디렉토리 규칙, 저작권과 PDF 재배포를 분리해서 관리하는 방식.

이 저장소에서 추가로 관리하는 부분은 다음과 같다.

- paper link 목록과 별도로 **CORE/NEXT/REFERENCE/ARCHIVE**를 운영한다.
- 각 paper에 문제·방법·평가·insight note를 고정 schema로 둔다.
- 전체 논문 목록과 별개로 paper-level `Open Questions`, minimum reproduction, and failure boundary를 유지한다. 별도 gap/idea/project overlay는 삭제 정책에 따라 활성 source of truth로 두지 않는다.
- registry snapshot, 최신 frontier update, reading status, synthesis queue를 서로 다른 artifact로 분리한다.
