# PaperReview — Robotics-first Literature System

- Snapshot verified: 2026-09-02 KST

`PaperReview`는 3D vision, robotics, VLA를 함께 다루되 **Robotics를 주 연구축**으로 삼는 장기 문헌 연구 저장소다. 논문을 모으는 데서 끝내지 않고, foundation → 최신 방법 → failure mode → 검증 가능한 연구 질문으로 연결한다.

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
| 전체 논문 registry | [PAPER.md](./PAPER.md) |
| machine-readable identity/provenance | [work/sources/papers.json](./work/sources/papers.json), [registry.schema.json](./work/sources/registry.schema.json), [registry_meta.json](./work/sources/registry_meta.json) |
| 검색·필터용 registry view | [REGISTRY_INDEX.csv](./research/REGISTRY_INDEX.csv), [REGISTRY_STATS.md](./research/REGISTRY_STATS.md) |
| evaluation·code/resource view | [resources.json](./work/sources/resources.json) |
| note artifact audit | [audit report](./work/sources/note_artifact_audit_2026-09-02.json), [audit script](./work/scripts/audit_note_artifacts.py) |
| 우선순위·읽기 순서·CORE/NEXT | [research/READING_PLAN.md](./research/READING_PLAN.md) |
| 전체 tier assignment | [research/READING_TIERS.csv](./research/READING_TIERS.csv) |
| 정독 진행 상태 | [research/READING_STATUS.csv](./research/READING_STATUS.csv), [research/READING_STATUS.md](./research/READING_STATUS.md) |
| 연구 공백 | [research/RESEARCH_GAPS.md](./research/RESEARCH_GAPS.md) |
| 연구 아이디어·가설 | [research/RESEARCH_IDEAS.md](./research/RESEARCH_IDEAS.md) |
| 실행 단계 연구 프로젝트 문서 | [RP-2 Failure Recovery](./research/projects/RP-2_FAILURE_RECOVERY.md), [RP-3 Memory Expiry](./research/projects/RP-3_MEMORY_EXPIRY.md) |
| 계보·트랙별 synthesis | [synthesis/README.md](./synthesis/README.md) |
| 최신 변경 기록 | [work/update/UPDATES_2026-09-02.md](./work/update/UPDATES_2026-09-02.md) |

## 현재 snapshot

| 항목 | 수치 |
|---|---:|
| 전체 registry | **950편** |
| CORE / NEXT | **77 / 234편** |
| REFERENCE / ARCHIVE | **397 / 242편** |
| intensive reading set | **311편** |
| paper당 표준 Markdown note | **4,750개** |
| `01_overview`–`04_evaluation` PDF-body review | **950 / 950편** |
| `05_insights` PDF-body review | **950 / 950편** |
| PDF-body extraction audit | **949 high / 1 medium** |
| `05_insights` extraction audit | **634 high / 0 failed** |
| curation rationale | **950 recorded / 0 pending** |
| legacy note artifact audit | **4,750 scanned / 0 high-confidence findings** |
| local PDF cache | 0개 |
| canonical category | 23개 |
| 대상 연도 | 1960–2026 |
| 2024–2026 논문 | 678편 |
| 2025–2026 논문 | 524편 |
| 2026 논문 | 181편 |

`CORE/NEXT`는 논문 수를 맞추기 위한 quota가 아니다. 연구의 prerequisite와 현재 연구축에 따라 중요도가 바뀔 수 있다. PDF 보유 여부는 tier, 우선순위, 연구 relevance의 기준이 아니다.

전체 950편의 `01_overview.md`–`04_evaluation.md`는 2026-09-03 기준 검증된 full-text source에서 갱신했고, 이어서 기존 Abstract/Curation-only 634편의 `05_insights.md`도 PDF 본문 기반으로 보강했다. 추가로 CORE/NEXT 311편은 2026-09-03 semantic QA에서 contribution·method·evaluation·failure·research question을 본문 anchor와 대조했으며, 309편은 PDF text/OCR로 교차검토하고 GR00T N1.5/N1.6은 PDF 부재 source-boundary로 유지했다. 01–04 중 64편은 스캔·인코딩 문제로 OCR fallback을 사용했고, GR00T N1.5/N1.6은 저자 제공 publication PDF를 확인하지 못해 공식 NVIDIA technical page를 작업용 PDF snapshot으로 렌더링한 예외다. 해당 provenance boundary와 각 pass의 범위는 [전체 full-text audit manifest](./work/sources/fulltext_all_review_manifest_2026-09-02.json), [insights full-text audit manifest](./work/sources/fulltext_insights_review_manifest_2026-09-03.json), [CORE/NEXT semantic QA report](./work/sources/core_next_semantic_qa_2026-09-03.json)에 기록되어 있다. `05_insights.md`는 모두 `FULL_TEXT_CHECKED`이며, 별도 artifact audit에서 명백한 metadata/extraction 잔여물도 제거했다.

## 어떤 종류의 논문이 있는가

### Intensive reading set의 연구 트랙

| 트랙 | CORE | NEXT | 주로 다루는 질문 |
|---|---:|---:|---|
| Planning, decision, control foundations | 16 | 13 | belief/state, motion planning, task-and-motion planning, feasibility, whole-body constraint |
| RL, IL, offline learning, robot data | 20 | 45 | expert distribution, policy/value learning, offline conservatism, data coverage |
| Manipulation, contact, tactile, dexterity | 10 | 45 | grasp/contact dynamics, force/tactile feedback, deformable and dexterous interaction |
| VLA, cross-embodiment, long horizon | 11 | 56 | generalist policy, action interface, memory, skill composition, feedback |
| World models, safety, uncertainty, recovery | 5 | 30 | runtime monitoring, calibration, safety filter, failure diagnosis, recovery |
| Locomotion, whole-body, mobile manipulation, humanoid | 8 | 26 | balance, contact switching, loco-manipulation, sim-to-real, humanoid execution |
| Robotics-enabling 3D perception | 7 | 19 | geometry, SLAM, spatial memory, active perception, 3D-to-control utility |
| **합계** | **77** | **234** | **Robotics-first intensive reading** |

전체 registry의 canonical category는 더 세분화되어 VLA/generalist, 3D vision-language, scene representation, embodied navigation, robot data, world models/safety, locomotion, manipulation/contact, planning/control foundation 등 23개로 관리된다. 자세한 분류는 [PAPER.md](./PAPER.md)와 [READING_TIERS.csv](./research/READING_TIERS.csv)에서 검색한다.

2026-09-01 3D-heavy `REFERENCE` audit에서는 실제 manipulation/navigation/control에 연결된 16편을 `NEXT`로 승격했다. FastSLAM·ORB-SLAM을 포함한 state-estimation foundation은 `REFERENCE`에 유지했고, 순수 Gaussian Splatting/NeRF reconstruction·scene rendering 계열 15편은 registry에서 삭제하지 않고 `ARCHIVE`로 분리했다. 세부 근거와 대상 목록은 [2026-09-01 update log](./work/update/UPDATES_2026-09-01.md)에 기록했다.

2026-09-02 robotics-first 재분류에서는 direct planning/control 2편을 `ARCHIVE→NEXT`, SLAM·world-model·generic 3D foundation 4편을 `ARCHIVE→REFERENCE`, generic 3D foundation 3편을 `NEXT→REFERENCE`로 조정하고, 최근 manipulation/VLA/navigation/world-model/whole-body 논문 26편을 `REFERENCE→NEXT`로 승격했다. 이어 robotics missing-link 26편을 신규 등록(20편 `NEXT`, 6편 `REFERENCE`)하고, ACT·NoMaD·PointFlowMatch·CALVIN·LIBERO·FurnitureBench·MimicPlay·LIBERO-Safety를 `NEXT`로 보강했다. 현재 snapshot은 **CORE 77 / NEXT 234 / REFERENCE 397 / ARCHIVE 242**이며, intensive reading set은 **311편**이다. 세부 대상과 provenance는 [최신 update log](./work/update/UPDATES_2026-09-02.md)에 기록했다.

### 논문이 맡는 역할

- **Foundation:** Kalman filter, A*, ICP, force/impedance control, ZMP, POMDP, PRM/RRT, TAMP, TD/Q/policy-gradient learning 등 후속 논문을 이해하기 위한 기반.
- **Policy and data:** behavior cloning, offline RL, diffusion/flow action policy, generalist robot policy, cross-embodiment data.
- **Physical interaction:** contact-rich manipulation, tactile/force feedback, dexterity, deformables, assembly.
- **VLA and long horizon:** RT-1/RT-2, PaLM-E, Open X-Embodiment, Octo, OpenVLA, π0/π0.5, memory, atomic skills, progress estimation.
- **Safety and recovery:** failure prediction, uncertainty calibration, safety alignment, retry/reset, diagnosis, rollback, recovery selection.
- **Benchmark and evidence:** MuJoCo, Meta-World, robosuite, ManiSkill, LIBERO, CALVIN, RLBench, FurnitureBench, VLA-Arena와 real-robot evaluation.
- **Institutional lineages:** Google/DeepMind의 DQN–A3C–MPO–MT-Opt–Gato–RT-H–Gemini Robotics와 NVIDIA의 Isaac Gym–Isaac Lab–Eureka/DrEureka–GR00T–DreamGen/DreamDojo–SONIC 계보.
- **Robotics-enabling perception:** PointNet, SLAM, 3DGS, DUSt3R/VGGT, semantic mapping, active view, 3D-aware policy state.

## 읽는 방법

장기 정독 순서와 프로젝트별 우선순위는 [READING_PLAN.md](./research/READING_PLAN.md)에서 dependency 단위로 관리한다. CORE/NEXT 전체 계보를 먼저 확인하고, foundation → learning/data → physical interaction → generalist policy → safety/recovery → embodiment → action-relevant 3D 순서로 필요한 가지를 확장한다.

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
4. `register_papers.py`로 stable `paper_id`, structured source/publication/provenance field와 5개 표준 note를 만든다. human-readable metadata는 `01_overview.md`에 한 번만 기록하고, 나머지 note는 canonical metadata pointer만 둔다. 원문을 아직 확인하지 않은 내용은 `CURATION_ONLY` 또는 `UNVERIFIED`로 둔다.
5. CORE/NEXT를 바꿀 때는 CSV를 직접 수정하지 않고 `build_reading_tiers.py`의 canonical group을 수정한다.
6. `normalize_taxonomy.py`, `build_reading_tiers.py`, `reconcile_registry.py --apply`, `build_registry_views.py --apply`, `audit_repository.py`, `git diff --check`를 순서대로 실행한다. schema migration은 `migrate_registry_schema.py --apply`를 사용한다. `build_registry_catalogs.py`는 기존 benchmark/metric cue를 갱신할 때만 실행한다.

논문을 정독한 뒤에는 `05_insights.md`, `READING_STATUS.csv`, 해당 synthesis matrix, 필요하면 `RESEARCH_GAPS.md`를 함께 갱신한다. 개인 note의 해석과 paper가 직접 보고한 결과를 분리한다. 구현 단계의 연구 문서는 literature collision, exact environment/checkpoint, method contract, baseline, metric, ablation, reject rule, pre-implementation freeze를 갖춘 실행 명세로 유지한다.

## Curation and maintenance policy

- 2024–2026은 현재 robotics/VLA frontier와 benchmark를 넓게 수집한다.
- 오래된 foundation은 후속 연구의 prerequisite이거나 연구 문제를 정의하면 포함한다.
- 최신 논문은 venue 이름보다 method novelty, closed-loop relevance, evaluation quality, research gap 연결을 우선한다.
- Foundation, frontier, benchmark, dataset, safety/recovery, enabling perception을 서로 다른 역할로 구분한다.
- 논문 수나 venue quota를 채우기 위해 약한 논문을 추가하지 않는다.
- 공식 proceedings/project/abstract를 우선 사용하고, 불확실한 claim은 `CURATION_ONLY` 또는 `UNVERIFIED`로 표시한다.
- 생성·검증 workflow는 [work/README.md](./work/README.md)에 있다.

```bash
python3 work/scripts/audit_repository.py
python3 work/scripts/register_papers.py --input /path/to/new_papers.json
python3 work/scripts/register_papers.py --input /path/to/new_papers.json --apply
python3 work/scripts/normalize_taxonomy.py
python3 work/scripts/build_reading_tiers.py
python3 work/scripts/reconcile_registry.py --apply
python3 work/scripts/build_registry_views.py --apply
python3 work/scripts/audit_repository.py
```

현재 snapshot의 상세 변경은 [work/update/UPDATES_2026-09-02.md](./work/update/UPDATES_2026-09-02.md), 운영 규칙은 [AGENTS.md](./AGENTS.md)에 기록한다.

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
- 전체 논문 목록과 별개로 **gap → hypothesis → minimum experiment → reject criterion**을 유지한다.
- registry snapshot, 최신 frontier update, reading status, synthesis queue를 서로 다른 artifact로 분리한다.
