# PaperReview — Robotics-first Literature System

- Snapshot verified: 2026-08-28 KST

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
| 우선순위·읽기 순서·CORE/NEXT | [research/READING_PLAN.md](./research/READING_PLAN.md) |
| 전체 tier assignment | [research/READING_TIERS.csv](./research/READING_TIERS.csv) |
| 정독 진행 상태 | [research/READING_STATUS.csv](./research/READING_STATUS.csv), [research/READING_STATUS.md](./research/READING_STATUS.md) |
| 연구 공백 | [research/RESEARCH_GAPS.md](./research/RESEARCH_GAPS.md) |
| 연구 아이디어·가설 | [research/RESEARCH_IDEAS.md](./research/RESEARCH_IDEAS.md) |
| 실행 단계 연구 프로젝트 문서 | [RP-2 Failure Recovery](./research/projects/RP-2_FAILURE_RECOVERY.md), [RP-3 Memory Expiry](./research/projects/RP-3_MEMORY_EXPIRY.md) |
| 계보·트랙별 synthesis | [synthesis/README.md](./synthesis/README.md) |
| 최신 변경 기록 | [work/update/UPDATES_2026-08-28.md](./work/update/UPDATES_2026-08-28.md) |

## 현재 snapshot

| 항목 | 수치 |
|---|---:|
| 전체 registry | **872편** |
| CORE / NEXT | **77 / 113편** |
| REFERENCE / ARCHIVE | **449 / 233편** |
| intensive reading set | **190편** |
| paper당 표준 Markdown note | **4,360개** |
| local PDF cache | 0개 |
| canonical category | 23개 |
| 대상 연도 | 1960–2026 |
| 2024–2026 논문 | 607편 |
| 2025–2026 논문 | 475편 |
| 2026 논문 | 179편 |

`CORE/NEXT`는 논문 수를 맞추기 위한 quota가 아니다. 연구의 prerequisite와 현재 연구축에 따라 중요도가 바뀔 수 있다. PDF 보유 여부는 tier, 우선순위, 연구 relevance의 기준이 아니다.

## 어떤 종류의 논문이 있는가

### Intensive reading set의 연구 트랙

| 트랙 | CORE | NEXT | 주로 다루는 질문 |
|---|---:|---:|---|
| Planning, decision, control foundations | 16 | 2 | belief/state, motion planning, task-and-motion planning, feasibility, whole-body constraint |
| RL, IL, offline learning, robot data | 20 | 21 | expert distribution, policy/value learning, offline conservatism, data coverage |
| Manipulation, contact, tactile, dexterity | 10 | 24 | grasp/contact dynamics, force/tactile feedback, deformable and dexterous interaction |
| VLA, cross-embodiment, long horizon | 11 | 23 | generalist policy, action interface, memory, skill composition, feedback |
| World models, safety, uncertainty, recovery | 5 | 16 | runtime monitoring, calibration, safety filter, failure diagnosis, recovery |
| Locomotion, whole-body, mobile manipulation, humanoid | 8 | 16 | balance, contact switching, loco-manipulation, sim-to-real, humanoid execution |
| Robotics-enabling 3D perception | 7 | 11 | geometry, SLAM, spatial memory, active perception, 3D-to-control utility |
| **합계** | **77** | **113** | **Robotics-first intensive reading** |

전체 registry의 canonical category는 더 세분화되어 VLA/generalist, 3D vision-language, scene representation, embodied navigation, robot data, world models/safety, locomotion, manipulation/contact, planning/control foundation 등 23개로 관리된다. 자세한 분류는 [PAPER.md](./PAPER.md)와 [READING_TIERS.csv](./research/READING_TIERS.csv)에서 검색한다.

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

- `01_overview.md`: 문제, 핵심 아이디어, interface, contribution, limitation
- `02_problem.md`: formulation, bottleneck, 가정, closed-loop 위치
- `03_method.md`: pipeline, objective, state/action, temporal horizon, implementation
- `04_evaluation.md`: robot, task, data, metric, baseline, ablation, failure, 재현성
- `05_insights.md`: 선행/후속 연결, 연구 relevance, 최소 재현과 아이디어

새 논문은 [work/sources/papers.json](./work/sources/papers.json)을 canonical manifest로 등록한다. PDF는 선택적 local cache이며 paper inclusion이나 priority를 결정하지 않는다.

## 논문 추가와 provenance 규칙

이 저장소는 exhaustive bibliography가 아니라 **근거와 연구 연결을 보존하는 curated registry**다. 새 논문은 다음 admission checklist를 통과해야 한다.

1. `PAPER.md`, `READING_TIERS.csv`, `work/sources/papers.json`에서 제목·subtitle·conference version 중복을 확인한다.
2. 공식 proceedings, publisher, OpenReview, CVF/PMLR/RSS page 또는 저자 project page에서 title·year·venue/status를 확인한다.
3. primary category, tags, `foundation / frontier / benchmark / dataset / safety-recovery` 역할과 registry에 추가하는 이유를 기록한다.
4. `register_papers.py`로 5개 표준 note를 만들고, 원문을 아직 확인하지 않은 내용은 `CURATION_ONLY` 또는 `UNVERIFIED`로 둔다.
5. CORE/NEXT를 바꿀 때는 CSV를 직접 수정하지 않고 `build_reading_tiers.py`의 canonical group을 수정한다.
6. `normalize_taxonomy.py`, `build_reading_tiers.py`, `audit_repository.py`, `git diff --check`를 순서대로 실행한다.

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
python3 work/scripts/audit_repository.py
```

현재 snapshot의 상세 변경은 [work/update/UPDATES_2026-08-28.md](./work/update/UPDATES_2026-08-28.md), 운영 규칙은 [AGENTS.md](./AGENTS.md)에 기록한다.

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
