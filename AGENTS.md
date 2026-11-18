# PaperReview Agent Operating Guide

- Updated: 2026-11-18 KST

이 파일은 자신이 위치한 저장소 루트와 모든 하위 디렉토리에 적용된다. 이 저장소에서 논문을 조사·추가·분류·요약·합성하는 에이전트는 아래 규칙을 기본 계약으로 따른다.

## 1. Mission and Research Stance

**2026-11-17 최신 후속 지시:** 다음 TODO는 기존 질문의 연장이 아니라 새로운 검색 분야의 연구 후보 탐색이다. 기존 신뢰성 선호를 탐색 범위의 제한으로 해석하지 않는다. 이어진 사용자 요청에 따라 참신성과 명확한 main contribution을 우선하며, 문제 원인·변경할 학습 변수·행동상 예측·직접 선행 대비 차이를 함께 제시한다. [새 분야 비교](./work/update/NEW_FIELD_SCOUT_2026-11-17.md)의 초기 질문과 기존 4개 보존 후보를 구분하며, 실제 다음 행동은 TODO를 따른다. 과거 후보 폐기 판단·Docker 조건·결과 증거 기준은 유지한다.

**2026-11-17 사용자 지시:** 연구 탐색의 큰 줄기는 **VLA + RL + Computer Vision + Robotics**이며 **신뢰성·불확실성·실패 탐지/원인/복구를 우선**한다. 동적 장면·물체 상태·3D/4D·기억·보상·접촉도 실제 행동과 연결해 탐색한다. [분야별 검색 지도](./research/IDEA_BUILDUP_GUIDE.md#search-map-2026-11-17)를 사용하되 키워드 조합을 공백의 증거로 취급하지 않는다. 사용자가 약한 기존 후보의 삭제·폐기를 요청하여 [현행 후보](./work/research_topics/README.md)를 **유지 3개·예비 1개**로 줄였다. [폐기 7개](./work/research_topics/retired/README.md)는 자동 재개하지 않는다. 아래의 기존 residual/파이프라인 후보 보존 지시보다 이번 명시적 폐기가 우선하며, 해당 분야 전체를 향후 탐색에서 금지하는 것은 아니다. 작은 탐색의 진입 기준과 결과 주장의 증거 기준은 구분한다.

**2026-11-06 사용자 선호:** 새 VLA+RL 공백은 계층형 controller 연결 외에 **단일 VLA 정책 내부의 RL 학습**을 우선 탐색한다. 공유 표현/가치 공동 학습은 그중 한 후보이며 유일한 방향으로 제한하지 않는다. 기존 residual·파이프라인 후보는 보존한다. 통합 architecture·배포 시 단일 정책·동일 가중치의 공동 갱신을 구별하고, 이미 있는 end-to-end RL을 새 기여로 주장하지 않는다. 현재 질문과 근거는 [주제 index](./work/research_topics/README.md)가 연결한다.

이 저장소는 Robotics를 중심으로 foundation·최신 문헌을 비교하여 검증 가능한 연구 질문으로 연결하는 literature system이다. **2026-11-03 최신 사용자 요청에 따라 새 연구 공백 탐색은 VLA + RL을 중심**으로 하며, 다양한 로봇 manipulation·navigation의 성능 개선·데이터 학습·통합 파이프라인까지 열어 둔다. 기존 RL 선택형 후보와 넓은 registry 범위를 삭제하거나 일괄 재분류하지 않는다. 3D는 state estimation·spatial memory·affordance 등 행동에 필요한 표현을 지원한다. 같은 플랫폼의 fleet와 서로 다른 embodiment를 구분하며, 논문의 연령·PDF 보유 여부로 중요도를 정하지 않는다.

**2026-11-03 사용자 목표 명확화:** 석사 과정 중 현재 VLA·Robotics 방향과 연결되는 top-tier conference/journal 논문을 쓰는 것이 주목적이다. 연구 후보는 선행 대비 기여의 명확성·중요성, 실제 로봇 행동과의 연결, 석사 기간 내 구현·검증 부담을 함께 비교한다. 연구 주제의 매력과 현재 실행 준비도를 구별하고, 단순 미보고 조합이나 문서 완결만으로 출판 가능성을 주장하지 않는다. 새 알고리즘뿐 아니라 중요한 원인 분석·평가·시스템 기여도 검토하며, 탐색 진입 기준을 낮추고 결과 주장의 증거 기준은 유지한다. 현행 후보의 투자 우선순위·초기 탐색 판정은 [통합 index](./work/research_topics/README.md), 선택한 다음 행동은 TODO가 소유한다. 초기 후보와 비실험 검토를 마친 후보의 성숙도를 구분하며 후보 순위를 논문 reading tier와 혼동하지 않는다.

연구 후보별 실제 결과·한계·GPU 후속·재개 조건은 [16개 단일 요약](./work/research_candidates/summaries/README.md), 활성 작업은 [TODO](./TODO.md), 단계별 역사와 source는 각 dossier 및 [과거 작업 인계](./work/update/TASK_HISTORY_2026-10-22.md)를 따른다. 이 운영 규칙에 작업 일지를 계속 복제하지 않는다.

현재 E2는 일반 방법 NO-GO·진단 REVISE/HOLD, E1·D3는 재개 gate NOT_MET, D1·D2는 방법 NO-GO·진단 HOLD다. C1–C6의 기존 판단과 초기 RL 전이·RP-2/RP-3 RETIRED를 유지한다. GPU 확보·같은 metadata 재집계·문서 완료만으로 자동 재개하지 않는다. 새 비교 packet·차별적 예측·단순 대안 이후 남은 gap을 먼저 심사한다. Native 정책 효과와 실제 외부 연구자 피드백은 미검증이다.

2026-10-23 사용자 요청에 따라 다른 컴퓨터로 clone한 뒤의 Docker 재개 경로를 추가했다. [Portable replay](./work/experiments/portable/README.md)는 C3 저장 logits만 재분석한다. 한 checkpoint·16개 관측의 head score 진단을 학습/정책 성능 개선이나 광범위한 VLA 결론으로 확대하지 않는다. 과거 runtime manifest는 실행 당시 증거이며 현재 실행 계획으로 자동 재사용하지 않는다.

연구축의 우선관계는 다음과 같다.

1. **Robotics:** planning, control, RL/IL, manipulation, contact, locomotion, whole-body/mobile manipulation, safety, world models, data and evaluation.
2. **VLA:** robot policy interface와 scaling paradigm. Language 이해 자체보다 action representation, robot data, embodiment transfer, control frequency, memory, feedback, safety를 본다.
3. **3D Vision:** robot state estimation과 behavior를 바꾸는 enabling stack. Reconstruction benchmark 자체보다 manipulation, navigation, SLAM, semantic memory, active perception, collision avoidance에 주는 효과를 본다.

항상 다음 폐루프를 기준으로 논문을 해석한다.

`observation → state/world model → task & motion decision → policy/control → contact → feedback/failure recovery`

Humanoid는 별도 taxonomy로 만들지 않는다. Locomotion, whole-body control, imitation, mobile/loco-manipulation 안에 포함한다.

## 2. Non-Negotiable Rules

- **2026-10-22 D3-R1 최신 인계:** [공개 근거 심사](./work/research_candidates/2026-10-22_d3_buildup/R1_REVIEW.md)는 DONE이나 재개 gate는 NOT_MET다. Raw/annotation stem 200/200의 identity 연결은 실제 Cooked–RGB pair가 아니다. P2 skill 평가에는 hotdog가 없고 turn-off 0/3은 burner 대상이다. 별도 P4의 pre-cooking placement 보고도 continuation witness로 승격하지 않는다. 연구 REVISE·full-task 실험/학습 HOLD 유지. 다음 [TODO](./TODO.md)의 D3-R2는 [동일 instance event/관측·필요 행동 능력·matched 비교 증거](./work/research_candidates/2026-10-22_d3_buildup/R1_EVIDENCE_REQUIREMENTS.json)가 새로 확보될 때 심사한다. 같은 metadata 조사·adapter 구현·D4 전환을 자동 반복하지 않는다. 실험·payload 저장·신규 registry 등록·reading status 변경은 없었다. 위 B1/L1의 다음 단계 문구보다 이 인계가 우선한다.

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

- **연구 주제 파일 구성 — 2026-11-03 사용자 지시:** 현재 진행·대기·탐색 주제는 [work/research_topics](./work/research_topics/README.md)에서 주제별 `내용/`과 `재현 방법/` 두 폴더로 관리한다. `내용/README.md`에 질문·문헌·결과·한계·추가 buildup을 통합하고, `재현 방법/README.md`에 환경·명령·실제 실행/미구현 범위를 통합한다. Source는 주제별 단일 JSON 또는 기존 공통 원장을 참조하고, 실행에 필요한 코드·계약·원시 결과는 재현 폴더에 보존한다. 유사 brief·날짜별 주제 보고서를 별도로 늘리지 않는다. 공통 유지보수/다주제 비교 이력은 기존 위치에 남긴다. 과거 보류·종료 주제의 전체 이관과 paper별 5-note 구조 변경은 이번 범위가 아니다.
- 새 논문은 실제 paper folder와 5개 표준 note file로 등록한다. `paper.pdf`는 선택 사항이다.
- `PAPER.md`는 전체 registry와 topic navigation에 집중한다.
- 읽기 우선순위, tier, 장기 순서, 연구 관점은 `READING_PLAN.md` 하나에 통합한다.
- `README.md`의 snapshot, 문서 링크, workflow는 registry와 생성 결과가 바뀔 때 함께 갱신한다.
- 향후 추가는 dataset/benchmark, canonical task formulation, field-shaping foundation, 최신 핵심 trend-flow를 incremental method보다 우선한다.

## 3. Repository Sources of Truth

| Artifact | Role | Editing rule |
|---|---|---|
| [TODO.md](./TODO.md) | 활성 작업·직전 완료·다음 행동·의존성 인계 | 시작/완료 시 결과 링크와 다음 항목을 갱신한다. 문서 작업 완료를 연구 가설 입증으로 표시하지 않으며 읽기 priority source로 쓰지 않는다. |
| [PAPER.md](./PAPER.md) | 전체 1,227편 registry와 topic navigation | 구조를 유지한다. 논문 추가 시 row와 실제 folder가 일치해야 한다. |
| [READING_PLAN.md](./research/READING_PLAN.md) | 우선순위 기준, 연구 관점, 읽기 순서, CORE/NEXT 장기 정독 목록 | `build_reading_tiers.py`가 생성한다. 직접 수정하지 않는다. |
| [READING_TIERS.csv](./research/READING_TIERS.csv) | 전체 registry의 단일 tier assignment | 생성 파일. 직접 수정하지 않는다. |
| [READING_STATUS.csv](./research/READING_STATUS.csv) | 477편 정독 진행 상태와 사용자 분석 | 상태·분석 필드는 직접 편집 가능. 생성기는 기존 입력을 보존해야 한다. |
| [READING_STATUS_HISTORY.csv](./research/READING_STATUS_HISTORY.csv) | 집중 읽기에서 빠진 47편의 기존 상태·분석 보존 | 생성기는 active tracker와 함께 읽고 재승격 시 사용자 입력을 복원한다. 우선순위 source가 아니다. |
| [READING_STATUS.md](./research/READING_STATUS.md) | 상태값과 완료 규칙 | 상태 정의 변경 시 tracker와 synthesis 규칙도 함께 점검한다. |
| [synthesis/](./synthesis/) | 7개 트랙의 cross-paper comparison과 paper lineage | queue marker 내부는 자동 생성, 나머지는 수동 합성 영역이다. |
| 각 [synthesis](./synthesis/README.md)의 Open Questions와 paper별 `05_insights.md` | 근거에 연결된 research gap, 해석과 최소 실험 | 삭제된 `RESEARCH_GAPS.md`·`RESEARCH_IDEAS.md`를 복원하거나 새 priority source로 만들지 않는다. |
| [research/projects/](./research/projects/) | 폐기된 project overlay의 역사적 보존본 | `RETIRED` 문서는 활성 계획이 아니다. 재개 요청 전에는 과거 가설·실험 계획을 현재 결과로 갱신하지 않는다. |
| [work/update/WORKSPACE_UPGRADE_2026-10-23.md](./work/update/WORKSPACE_UPGRADE_2026-10-23.md) | 문서 합성·work 정리·Docker 이동성 검증. 직전 registry 등록은 2026-10-22 rollup 참조 | 날짜별 audit log로 유지하고 canonical plan 내용을 중복 관리하지 않는다. 앞으로의 update log도 `work/update/`에 작성한다. |
| [work/scripts/build_reading_tiers.py](./work/scripts/build_reading_tiers.py) | tier·plan·tracker·synthesis queue 생성 규칙 | CORE/NEXT membership의 canonical source다. |
| [work/sources/papers.json](./work/sources/papers.json) | 전체 registry identity/publication/source/taxonomy/provenance의 canonical manifest | 신규 등록은 `register_papers.py`를 사용한다. `paper_id`가 내부 stable identity다. |
| [work/sources/registry.schema.json](./work/sources/registry.schema.json) | manifest 구조와 허용 enum의 JSON Schema | schema 변경 시 migration, audit와 generator를 함께 갱신한다. |
| [work/sources/registry_meta.json](./work/sources/registry_meta.json) | manifest schema/count/identity/version/evidence policy | manifest count와 schema version을 audit로 검증한다. |
| [work/sources/benchmark_catalog.json](./work/sources/benchmark_catalog.json) / [metric_catalog.json](./work/sources/metric_catalog.json) | evaluation resource의 paper-ID 탐색 index | 모든 자동 연결은 `cue_only`; 실제 role/split/정의의 근거로 사용하지 않는다. |
| [work/sources/resources.json](./work/sources/resources.json) | benchmark/dataset·metric·code/project를 합친 단일 resource view | 생성 파일. 기존 benchmark/metric 항목은 `cue_only`이며 code/project URL은 manifest link일 뿐 재현성 증거가 아니다. |
| [research/REGISTRY_INDEX.csv](./research/REGISTRY_INDEX.csv) / [REGISTRY_STATS.md](./research/REGISTRY_STATS.md) | 전체 paper를 filter/search하고 registry 품질을 점검하는 생성 view | 직접 수정하지 않는다. manifest·tier·tracker에서 재생성한다. |
| [work/scripts/audit_repository.py](./work/scripts/audit_repository.py) | registry·tier·tracker·queue·note·taxonomy 무결성 검사 | read-only이며 주요 변경 전후에 실행한다. |

[2026-11-05 통합 검토](./work/update/INTEGRATED_GAP_REVIEW_2026-11-05.md)에서 기존·신규 후보를 함께 대조하고 직접 선행 12편을 추가했다. 11/06 [UNIFIED-N1](./work/research_topics/unified_vla_rl/내용/README.md#n1-review)에서 직접 선행 2편을 추가했다. 11/12 [REG-R14](./work/update/REGISTRY_MAINTENANCE_2026-11-12.md)에서 최근 공백 조사에 인용한 미등록8편을 추가했다. 이어서 [REG-R15](./work/update/FOUNDATION_FRONTIER_SUPPLEMENT_2026-11-12.md)에서 기반·핵심 비교12편과 최근12편을 추가했다. 11/16 [REG-R16](./work/update/REGISTRY_ACCURACY_PSI0_2026-11-16.md)에서 Ψ₀와 데이터 전제2편을 등록하고 AMO/SONIC의 설명·공개 자료를 교정했다. 11/18 [REG-R17](./work/update/REGISTRY_MAINTENANCE_2026-11-18.md)에서 직접 선행18편을 추가하고 SaPaVe·ActiveAlign을 NEXT로 조정했다. 같은 날 [REG-R18](./work/update/REGISTRY_MAINTENANCE_2026-11-18.md#reg-r18)에서 geometry 후보의 직접 선행3편을 추가했다. 현재 snapshot은 CORE 50편, NEXT 427편, REFERENCE 508편, ARCHIVE 242편이다. 등록·병합의 과거 수량과 근거는 [update index](./work/update/README.md)에 보존하며 기존 연구 판단은 유지한다. 이 숫자는 결과이지 목표 quota가 아니다. 논문 중요성 때문에 필요하면 CORE/NEXT를 늘릴 수 있으며, 장기 정독 규모 100–150편은 운영상 가이드일 뿐 hard cap이 아니다.

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

- 중요한 foundation, baseline, dataset, benchmark, survey이지만 현재 477편 정독 흐름의 prerequisite는 아니다.
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

1. `rg -i`로 exact title과 distinctive title phrase를 `PAPER.md`, `READING_TIERS.csv`, `work/sources/*.json`에서 검색하고 DOI/arXiv/OpenReview identifier 충돌도 확인한다.
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

`01_overview.md`에 다음 canonical metadata를 기록한다. 나머지 네 노트에는 정확한 title, evidence/source boundary와 overview 상대 링크를 두어 반복 metadata의 불일치를 줄인다.

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
- Tracker 재생성 시 `overview_path`를 key로 사용자 입력 필드를 보존한다. CORE/NEXT에서 빠지는 행은 `READING_STATUS_HISTORY.csv`에 저장하고 재진입 시 복원한다. 읽기 기록을 tier 변경으로 삭제하거나 초기화하지 않는다.
- Case-only 경로 수정은 유일한 현재 경로와 동일한 `paper_id`가 확인될 때만 읽기 입력을 이관한다. 실제 폴더 대소문자도 audit하며 Linux에서 실패할 경로를 macOS의 `exists()` 성공만으로 통과시키지 않는다.
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
7. Research Gaps (필요한 경우); 별도 register 대신 Open Questions 안에 통합할 수 있다.

`<!-- READING_QUEUE:START -->`와 `<!-- READING_QUEUE:END -->` 사이를 직접 편집하지 않는다. 이 영역은 `build_reading_tiers.py`가 tracker 상태, evidence level과 논문 queue를 갱신한다. 현재 Comparison Matrix의 `CURATION-SEED` 행은 읽기 전 비교 가설이다. 정독 후 source location을 확인해 수동 수정하며, seed script를 다시 실행해 덮어쓰지 않는다.

`SYNTHESIZED`로 올리기 위한 최소 조건:

- tracker의 문제·interface·evaluation·failure field가 채워짐
- 같은 track의 선행/후속 논문과 차이가 comparison matrix에 기록됨
- Open Questions 또는 Research Gaps에 구체적이고 검증 가능한 함의가 추가됨

## 13. Automation and Safe Editing

### Docker-only experiment constraint — 2026-10-19 / clone portability 2026-10-23

- 문헌 검토와 직접 충돌 연구의 확인을 실험보다 우선한다.
- 실험은 사용자가 선택한 현재 컴퓨터 또는 이 저장소를 clone한 컴퓨터의 로컬 Docker에서 수행하며, simulation·policy inference·학습·성능 측정과 그 dependency 설치는 반드시 Docker 내부에서 진행한다.
- Host Python/MPS 또는 원격 GPU·cloud로 실험 경로를 임의 변경하지 않는다. Docker 실행 가능성을 확인하지 못했으면 실험 결과를 추정하지 않는다.
- 문헌 읽기, 파일 편집, 읽기 전용 시스템 확인, 아래의 registry·문서 유지보수 검증 명령은 실험과 구분한다.

### 실험 준비 확인·로컬 Docker 실행 검증 — 2026-10-28 사용자 지시

- 실험 준비·재개 또는 다음 실험 TODO를 요청받으면, **사용자가 선택한 현재 컴퓨터의 로컬 Docker GPU·환경 조건을 먼저 확인한다.** 과거 GPU 실패 기록만으로 현재도 불가능하다고 단정하지 않는다. Docker endpoint가 로컬인지, daemon 동작·architecture·메모리, 필요한 NVIDIA GPU 할당·CUDA/graphics 지원, 대상 simulator/model의 version·asset·입출력 조건을 작업에 필요한 범위로 확인한다.
- **조건이 충족되면 이미 정한 최소 실행 검증까지 진행한다.** 문서 작성만으로 끝내거나 이미 허용된 동일 범위의 실행을 다시 확인받지 않는다. Dependency 설치, simulator·정책 추론·검사는 로컬 Docker 내부에서만 수행하며, 최소 검증을 큰 학습·성능 sweep의 자동 승인으로 해석하지 않는다.
- **조건이 충족되지 않으면 다른 컴퓨터에서 clone 후 재개할 수 있도록 실행 준비를 진행한다.** 확인한 실패 단계·명령/결과, 필요한 OS/GPU/driver·Docker·package 설정, code/checkpoint/normalizer revision·hash, asset 저장 위치·mount, 재개 명령과 남은 구현/검증을 기록한다. 경로는 저장소 상대 경로 또는 명시적 설정값으로 두고 특정 사용자의 절대 경로를 실행 조건으로 만들지 않는다.
- 필요한 패키지·weights·simulator assets를 host에 설치하지 않는다. 준비 artifact와 실행 결과를 구별하고, 미구현 adapter·미검증 image/manifest·미측정 효과를 완료로 표시하지 않는다. 자원 미충족은 연구 가설의 반증이 아니며 기존 NO-GO/HOLD 후보의 과학적 재개 조건도 자동 해제하지 않는다.
- 실패가 확정된 조건에서 무관한 대용 실험·대규모 다운로드를 반복하지 않는다. 이번 작업이 생성한 불필요한 container/image는 식별하여 정리하고, 기존 사용자 자산이나 다른 작업의 자산은 보존한다. TODO에는 **준비 완료 범위 / 실제 실행 확인 범위 / 남은 자원·구현 조건**을 각각 남긴다.

### 이전 실험의 판단 보존

- 현재 [C1 후속 검토](./work/research_candidates/2026-10-20_vla_rl/C1_REVIEW.md)는 문헌·bounded native probe 결과를 보존한 보류 상태다. Base competence는 미확인이고 learned selector·RL 학습·G1 이후 branch 비교는 미실행이다. 전용 실행 자원은 정리했다. 이전 작업은 [핵심 결과](./work/experiments/vla_rl_cross_embodiment/RESULTS.md)로 통합했다. Design freeze와 runtime 검증·연구 효과 입증을 구별한다.
- [C2 1차 결과](./work/experiments/vla_rl_c2_first_pass/RESULTS.md)는 실제 데이터 감사·경유 판정·의존성 probe를 수행한 기록이다. [분할 초안](./work/research_candidates/2026-10-20_vla_rl/C2_SPLIT_DRAFT.json)은 여전히 executable=false이며 정책 비교는 미실행이다. G0·G1 미충족으로 현재 설계를 종료했고, [재개 조건](./work/research_candidates/2026-10-20_vla_rl/C2_BUILDUP_RESULT.md) 없이 큰 학습 sweep이나 환경 이식을 시작하지 않는다.

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

사용자가 tracker에 입력한 상태와 분석 필드는 같은 `overview_path`가 유지되는 한 보존되어야 한다. 생성기 수정 후 반드시 이를 검증한다. `paper_id`와 `primary_track`은 manifest에서 파생되는 자동 필드다.

신규 등록·tier 조정 뒤에는 `reconcile_registry.py --priorities-only`의 dry-run을 확인한 뒤 `--apply`로 priority/header만 동기화한다. 전체 `reconcile_registry.py`는 review manifest와 실제 note header를 사용해 paper-level `content_evidence`와 note별 `note_evidence`를 정합화하므로 source evidence를 실제 갱신할 때만 별도로 검토한다. 이는 사용자의 reading `status`를 의미하지 않는다. `build_registry_views.py`는 이 canonical 상태에서 통합 resource view와 filter-friendly index를 생성한다. 별도의 첫 10/25/50편 진입 경로는 만들지 않는다.

### Paper registration and full rebuild safety

- 신규 metadata는 `python3 work/scripts/register_papers.py --input <json>`으로 dry-run한 뒤 `--apply`로 등록한다.
- 기존 manifest schema를 올릴 때는 `python3 work/scripts/migrate_registry_schema.py` dry-run 후 `--apply`를 사용하고, `registry.schema.json`과 `registry_meta.json`을 함께 갱신한다.
- evaluation vocabulary는 `python3 work/scripts/build_registry_catalogs.py`로 생성한다. benchmark/metric catalog의 자동 연결은 `cue_only`로만 기록한다.
- `build_lit_survey.py`는 인자 없이 read-only다. metadata refresh, PDF download, note overwrite, registry/manifest write는 각각 명시적 flag 없이는 실행되지 않아야 한다.
- `build_lit_survey.py`의 일반 CLI는 현재 canonical manifest 전체를 사용한다. 과거 discovery의 `build_papers()` 결과로 registry를 대체하지 않는다. `write_registry()`는 기존 stable ID 누락을 쓰기 전에 차단한다. 게재에 따른 경로 변경 시 stable ID·읽기 입력을 보존하고 review manifest의 원 identity는 `identity_at_review`에 남긴다.
- `--overwrite-notes`는 기존 수동 분석을 덮어쓰므로 사용자의 명시적 전체 재생성 요청 없이는 사용하지 않는다.
- 폐기된 one-off script와 사용하지 않는 발견용 dump는 2026-10-23 제거했다. [정리 기록](./work/update/WORKSPACE_UPGRADE_2026-10-23.md)과 [통합 과거 report](./work/sources/legacy_maintenance_reports.json)는 역사 자료이며 현재 source of truth가 아니다. `sources/candidates/cvf_candidates.json`은 현행 discovery script 입력이므로 보존한다.

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
- stable `paper_id`와 public identifier 중복이 없거나 명시적 version/same-work relation으로 설명되는가
- Year/venue/path가 서로 일치하는가
- manifest가 `registry.schema.json`과 `registry_meta.json`에 맞는가

### Tier integrity

- 모든 registry paper가 정확히 하나의 `CORE/NEXT/REFERENCE/ARCHIVE` tier에 속하는가
- CORE/NEXT 사이에 중복이 없는가
- CORE/NEXT 모든 paper가 `READING_PLAN.md`와 `READING_STATUS.csv`에 나타나는가
- 477편이 7개 synthesis queue에 정확히 한 번씩 배정되는가
- Tier 판단에 PDF 상태가 들어가지 않았는가

### Tracker integrity

- 허용된 status 값만 사용하는가
- 허용된 evidence level만 사용하며 status와 최소 조합이 맞는가
- 기존 사용자 입력이 재생성 후 active/history 합집합에서 보존되고 재승격 시 복원되는가
- tier/tracker의 `paper_id`와 `primary_track`이 manifest와 일치하는가
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

- Registry composition: 전체 1,227편 기준
- Intensive reading: CORE+NEXT 기준 (현재 477편)
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
