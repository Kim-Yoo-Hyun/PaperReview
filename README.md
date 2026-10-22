# PaperReview — Robotics-first Literature System

- Snapshot verified: 2026-10-23 KST

`PaperReview`는 **VLA를 기반으로 다양한 로봇의 manipulation·navigation을 다루는 연구**를 중심으로 삼는 장기 문헌 연구 저장소다. RL은 선택 사항이다. 현재 [E2 buildup](./work/research_candidates/2026-10-22_e2_buildup/README.md)은 시간 표현·관측 갱신·controller 효과를 대조해 **일반 신규 방법 NO-GO·진단 REVISE/HOLD**로 판단했다. 주력 연구 채택 근거·native 효과는 미확보이며 E1 보류도 유지한다. 3D vision은 행동을 개선하는 표현과 상태 추정으로 연결한다. 논문을 모으는 데서 끝내지 않고, foundation → 최신 방법 → failure mode → 검증 가능한 연구 질문으로 연결한다.

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
| 읽기·상태·buildup 운영 | [research 안내](./research/README.md), [READING_PLAN](./research/READING_PLAN.md) |
| 논문 간 비교·검증 가능한 질문 | [7개 synthesis와 교차 분류](./synthesis/README.md) |
| 후보별 결과·GPU 후속·한계 | [16개 주제별 요약](./work/research_candidates/summaries/README.md) |
| Clone 후 Docker 실행·연구 재개 조건 | [실행 안내](./work/experiments/portable/README.md), [실험 근거 index](./work/experiments/README.md) |
| Canonical identity·source·resource | [papers.json](./work/sources/papers.json), [schema](./work/sources/registry.schema.json), [resources](./work/sources/resources.json) |
| Registry 운영·최근 정리 | [work 안내](./work/README.md), [2026-10-23 정리/검증](./work/update/WORKSPACE_UPGRADE_2026-10-23.md) |
| 직전 47편 등록·공식 발표 확인 | [등록 report](./work/update/REGISTRY_ROLLUP_2026-10-22.md) |

## 현재 snapshot

| 항목 | 수치 |
|---|---:|
| 전체 registry | **1,037편** |
| CORE / NEXT | **47 / 275편** |
| REFERENCE / ARCHIVE | **473 / 242편** |
| intensive reading set | **322편** |
| inactive reading history | **47편** |
| 기록된 READ | **총 5편: active 1 / history 4** |
| 표준 Markdown note 총수 | **1,037편 × 5개 = 5,185개** |
| `01_overview`–`04_evaluation` 기존 PDF-body review | **950 / 1,037편** |
| `05_insights` 기존 PDF-body review | **950 / 1,037편** |
| 신규 abstract/project 기반 note | **87편 / 435개** |
| PDF-body extraction audit | **949 high / 1 medium** |
| `05_insights` extraction audit | **634 high / 0 failed** |
| structured evaluation profile | **1,037 / 1,037편** |
| reproducibility profile | **1,037 / 1,037편** |
| lineage coverage profile | **1,037 / 1,037편** |
| curation rationale | **1,037 recorded / 0 pending** |
| legacy note artifact audit (기존 cohort) | **4,750 scanned / 0 high-confidence findings** |
| Markdown 정비 audit (아이디어 가이드 추가 전 snapshot) | **4,896개 문서 / 2026-10-19** |
| local PDF cache | 0개 |
| canonical category | 23개 |
| 대상 연도 | 1960–2026 |
| 2024–2026 논문 | 757편 |
| 2025–2026 논문 | 602편 |
| 2026 논문 | 240편 |

`CORE/NEXT`는 논문 수를 맞추기 위한 quota가 아니다. 연구의 prerequisite와 현재 연구축에 따라 중요도가 바뀔 수 있다. PDF 보유 여부는 tier, 우선순위, 연구 relevance의 기준이 아니다.

기존 950편의 `01_overview.md`–`04_evaluation.md`는 2026-09-03 기준 검증된 full-text source에서 갱신했고, 이어서 기존 Abstract/Curation-only 634편의 `05_insights.md`도 PDF 본문 기반으로 보강했다. 추가로 당시 CORE/NEXT 311편은 2026-09-03 semantic QA에서 contribution·method·evaluation·failure·research question을 본문 anchor와 대조했으며, 309편은 PDF text/OCR로 교차검토하고 GR00T N1.5/N1.6은 PDF 부재 source-boundary로 유지했다. 01–04 중 64편은 스캔·인코딩 문제로 OCR fallback을 사용했고, GR00T N1.5/N1.6은 저자 제공 publication PDF를 확인하지 못해 공식 NVIDIA technical page를 작업용 PDF snapshot으로 렌더링한 예외다. 해당 provenance boundary와 각 pass의 범위는 [전체 full-text audit manifest](./work/sources/fulltext_all_review_manifest_2026-09-02.json), [insights full-text audit manifest](./work/sources/fulltext_insights_review_manifest_2026-09-03.json), [CORE/NEXT semantic QA report](./work/sources/core_next_semantic_qa_2026-09-03.json)에 기록되어 있다. 당시 950편의 `05_insights.md`는 `FULL_TEXT_CHECKED`이며, 별도 artifact audit에서 명백한 metadata/extraction 잔여물도 제거했다. 2026-10-19·21·22 신규 등록 총 87편은 이 과거 full-text cohort에 포함되지 않으며, 5개 노트 모두 `ABSTRACT_CHECKED`다. Structured profile의 존재는 상세 실험 검증을 의미하지 않는다.

## 어떤 종류의 논문이 있는가

### Intensive reading set의 연구 트랙

| 트랙 | CORE | NEXT | 주로 다루는 질문 |
|---|---:|---:|---|
| Planning and control | 4 | 16 | POMDP, impedance, NoMaD·NavDP navigation interface |
| RL, IL, offline learning, robot data | 20 | 55 | DPPO·FQL, chunked RL, DSRL, real-robot learning |
| Manipulation, contact, tactile, dexterity | 2 | 49 | ACT·DP3, Tac2Real과 contact/force policy 확장 |
| VLA and generalist policies | 13 | 80 | OFT·ConRFT, SimpleVLA-RL·RLux-VLA, streaming/social navigation |
| World models, safety, recovery | 2 | 41 | VLAW·VLA-MBPO·RISE·PointWorld, damage-aware evaluation |
| Locomotion, whole-body, mobile manipulation | 2 | 12 | ViNT·Mobile ALOHA와 navigation/manipulation 연결 |
| Robotics-enabling 3D perception | 4 | 22 | ConceptFusion·RVT·VLFM·VLN-CE·LoGoPlanner, action-relevant state |
| **합계** | **47** | **275** | **VLA 기반 manipulation/navigation** |

전체 registry의 canonical category는 더 세분화되어 VLA/generalist, 3D vision-language, scene representation, embodied navigation, robot data, world models/safety, locomotion, manipulation/contact, planning/control foundation 등 23개로 관리된다. 자세한 분류는 [PAPER.md](./PAPER.md)와 [READING_TIERS.csv](./research/READING_TIERS.csv)에서 검색한다.

2026-09-01 3D-heavy `REFERENCE` audit에서는 실제 manipulation/navigation/control에 연결된 16편을 `NEXT`로 승격했다. FastSLAM·ORB-SLAM을 포함한 state-estimation foundation은 `REFERENCE`에 유지했고, 순수 Gaussian Splatting/NeRF reconstruction·scene rendering 계열 15편은 registry에서 삭제하지 않고 `ARCHIVE`로 분리했다. 세부 근거와 대상 목록은 [2026-09-01 update log](./work/update/UPDATES_2026-09-01.md)에 기록했다.

2026-09-02 robotics-first 재분류에서는 direct planning/control 2편을 `ARCHIVE→NEXT`, SLAM·world-model·generic 3D foundation 4편을 `ARCHIVE→REFERENCE`, generic 3D foundation 3편을 `NEXT→REFERENCE`로 조정하고, 최근 manipulation/VLA/navigation/world-model/whole-body 논문 26편을 `REFERENCE→NEXT`로 승격했다. 이어 robotics missing-link 26편을 신규 등록(20편 `NEXT`, 6편 `REFERENCE`)하고, ACT·NoMaD·PointFlowMatch·CALVIN·LIBERO·FurnitureBench·MimicPlay·LIBERO-Safety를 `NEXT`로 보강했다. 당시 snapshot은 **CORE 77 / NEXT 234 / REFERENCE 397 / ARCHIVE 242**였다.

2026-10-22에는 후보 검토에 사용한 미등록 baseline·frontier 47편을 추가했다. 현재 **1,037편 / CORE 47 · NEXT 275 · REFERENCE 473 · ARCHIVE 242**, 집중 읽기 **322편**이다. 새 47편은 표준 5개 note를 `ABSTRACT_CHECKED`로 등록했고 NEXT 18편의 사용자 상태는 `UNREAD`다. 기존 990편과 사용자 읽기 이력은 보존했다. [등록 범위·발표 상태·검증](./work/update/REGISTRY_ROLLUP_2026-10-22.md).

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

읽기 우선순위는 [READING_PLAN.md](./research/READING_PLAN.md)에서 관리한다. VLA+RL manipulation, action representation, navigation/mobile manipulation, action-relevant 3D, evaluation/recovery의 dependency를 따라 읽는다. 해당 branch의 CORE 선행 개념을 이해하면 NEXT를 병행하며, CORE 전체 완독을 시작 조건으로 두지 않는다. 오래된 논문도 최신 방법의 objective나 interface를 이해하는 데 필요하면 유지한다.

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

현재 snapshot의 상세 변경은 [최신 update log](./work/update/UPDATES_2026-10-19.md), 운영 규칙은 [AGENTS.md](./AGENTS.md)에 기록한다.

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
