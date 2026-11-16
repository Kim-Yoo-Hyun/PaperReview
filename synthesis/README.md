# Robotics Research Synthesis

- Updated: 2026-11-16 KST

**현재 새 탐색은 VLA + RL·단일 정책 학습 중심**이다. [Hindsight 목표 선택](./04_vla_generalist.md#gap-hindsight-transfer)을 포함한 논문 간 질문을 여기서 관리한다. 현재 11개 주제의 가능성·준비 상태는 [주제 index](../work/research_topics/README.md), 선택한 다음 행동은 [TODO](../TODO.md)에 통합하며 실행 인계를 중복하지 않는다.

이 디렉토리는 논문별 요약을 반복하는 곳이 아니라, CORE/NEXT 논문을 연구 트랙별로 비교하고 근거 기반 `Open Questions`를 축적하는 공간이다.

집중 읽기의 출발점은 VLA 기반 manipulation·navigation과 action-relevant 3D다. 기존 control·causal/offline RL·데이터 학습·변형체·world model·장시간 운용·3D·HRI/multi-agent 비교도 보존한다. Generated queue는 CORE/NEXT를 7개 primary track에 배정하며 수동 comparison matrix의 읽기 결과를 덮어쓰지 않는다. 규모·읽기 순서의 기준은 [READING_PLAN.md](../research/READING_PLAN.md)이며, 각 트랙의 Reading Path는 비교 계보를 설명한다.

[11/16 보완](../work/update/REGISTRY_ACCURACY_PSI0_2026-11-16.md)은 [Ψ₀ 학습/제어 경계](./04_vla_generalist.md#psi0-2026), [데이터 전제](./02_rl_il_offline.md#humanoid-data-2026), [AMO/SONIC 버전 비교](./06_locomotion_whole_body.md#psi0-controller-boundary)를 추가한다. 앞선 기반→frontier 및 지시·시간·기억 비교는 유지하며 사용자 reading status나 정독 comparison matrix를 승격하지 않는다.

## Documents

1. [Planning and Control](./01_planning_control.md)
2. [RL, IL, Offline Learning, and Robot Data](./02_rl_il_offline.md)
3. [Manipulation, Contact, Tactile, and Dexterity](./03_manipulation_contact.md)
4. [VLA and Generalist Robot Policies](./04_vla_generalist.md)
5. [World Models, Safety, and Recovery](./05_world_models_safety.md)
6. [Locomotion, Whole-Body, Mobile Manipulation, and Humanoids](./06_locomotion_whole_body.md)
7. [Robotics-Enabling 3D Perception](./07_robotics_3d_perception.md)

Cross-track gap/idea 문서는 현재 삭제 정책에 따라 활성 source of truth로 유지하지 않는다. 해당 내용은 각 트랙의 `Open Questions`, comparison matrix, 그리고 paper-level `05_insights.md`의 근거 범위에 남긴다.

문헌 비교에서 얻은 질문을 본격적인 연구로 발전시키기 전에는 [아이디어 빌드업 가이드](../research/IDEA_BUILDUP_GUIDE.md)의 closest-work 비교, 경쟁 가설, 최소 파일럿과 진행·수정·중단 기준을 적용할 수 있다. 이 문서는 연구 방법론 안내이며 별도의 gap/idea registry나 활성 프로젝트 목록이 아니다.

## Update Rule

2026-10-28 [절차 감사](../work/update/BUILDUP_PROCESS_AUDIT_2026-10-28.md) 이후 새 질문은 [탐색 단계의 최소 요건](../research/IDEA_BUILDUP_GUIDE.md#stage-appropriate-gates)으로 선정한다. 방향 가설·완성된 mechanism 없이도 중요한 실증/평가 질문을 보존할 수 있다. 단순 baseline의 존재와 실제 충분성을 구별하며 기존 후보의 상태는 자동 변경하지 않는다.

논문을 `READ`로 바꿀 때 해당 트랙 문서의 comparison matrix에 한 행을 추가한다. `SYNTHESIZED`는 다음 조건을 모두 만족할 때만 사용한다.

1. 논문 단위로 문제, interface, 실험, failure mode가 기록되어 있다.
2. 같은 트랙의 선행 연구와 차이가 comparison matrix에 반영되어 있다.
3. `Open Questions`에 연구적 함의가 추가되어 있다.

`Comparison Matrix`는 아직 읽지 않은 CORE/NEXT 전체를 미리 채우는 catalog가 아니다. 다만 active tracker와 [inactive history](../research/READING_STATUS_HISTORY.csv)의 `READ`, `SYNTHESIZED`, `REPRODUCED` 논문은 해당 primary track matrix에 정확히 한 행으로 연결되어야 하며, 이 coverage는 `python3 work/scripts/audit_repository.py`가 검사한다. `CURATION-SEED` 행은 실제 읽기 전 가설로 남길 수 있다.

`Dependency and Evolution`은 foundation → transition → frontier의 계보와 변화를 기록한다. 직접 citation과 개념적 연결을 혼동하지 않는다. 별도 gap/idea register는 삭제 정책에 따라 유지하지 않으며, 각 문서에는 track-specific evidence와 검증 가능한 open question만 남긴다.

현재 comparison matrix의 `CURATION-SEED` 행은 공식 abstract와 registry-level 지식을 바탕으로 만든 **읽기 전 비교 가설**이다. Tracker evidence가 FULL_TEXT_CHECKED여도 이 행의 검증을 뜻하지 않는다. 사용자가 정독하고 각 cell의 page/section/table을 대조해 evidence 표기를 갱신하기 전에는 확정된 paper claim이나 정량 비교로 인용하지 않는다. Seed script로 matrix를 다시 덮어쓰지 않는다.

2026-10-19 등록한 24편의 연결은 각 트랙 Reading Path와 Open Questions의 사전 비교 질문에 반영했다. 이는 abstract/project 기반 연구자 해석이며, 새 논문을 읽었다는 뜻이나 직접 citation 관계의 확인이 아니다. 비교 결과가 생기면 기존 Matrix에 source anchor와 함께 기록한다.

읽기 진행 상태의 canonical source는 [READING_STATUS.csv](../research/READING_STATUS.csv)이며, 상태 전환 규칙은 [READING_STATUS.md](../research/READING_STATUS.md)를 따른다.

## 공통 비교 규약과 질문 분류

각 track은 primary axis·포함/제외 범위·역할 vocabulary를 소유한다. Matrix의 공통 facet은 `embodiment; modality/data; setting; control level; horizon/memory`이며 evaluation은 `setup; data/split; metric; real/trials`로 쓴다. Metadata의 최종 근거는 paper overview와 manifest다. Matrix에는 source anchor와 evidence 경계를 남긴다. 논문 단위 matrix는 한 논문당 한 행을 유지하고, 방법 간 묶음 비교는 별도 비교표에 둔다.

7개 primary track은 유지한다. 다음은 중복 등록·새 읽기 순서 없이 같은 논문을 다른 연구 질문으로 찾는 **교차 분류**다.

| 질문 렌즈 | 먼저 비교할 통제 조건 | 주로 연결되는 track |
|---|---|---|
| 행동 표현·로봇 간 정렬 | pose/frame, action unit, controller, mask, 실제 effect | [RL/IL](./02_rl_il_offline.md), [VLA](./04_vla_generalist.md) |
| 시간·feedback·실행 interface | sensor age, 물리 시간, queue, controller, compute | [VLA](./04_vla_generalist.md), [planning](./01_planning_control.md), [whole-body](./06_locomotion_whole_body.md) |
| 상태·관측·memory | 사용 가능한 cue, 가시성, stale state, 관측 비용 | [3D](./07_robotics_3d_perception.md), [VLA](./04_vla_generalist.md) |
| 접촉·실행 가능성·목표 변경 | attachment, contact mode, 사건 시점, feasible witness | [manipulation](./03_manipulation_contact.md), [planning](./01_planning_control.md) |
| 적응·보존·평가 신뢰도 | data/interaction 예산, 독립 outcome, reset/selection ledger | [RL/IL](./02_rl_il_offline.md), [safety](./05_world_models_safety.md) |
| 식별 가능성·데이터 선택의 전달 | hidden cue, coverage, source/target policy, 선택 계산 비용 | [CAUSAL](./02_rl_il_offline.md#gap-causal-2026), [DATA-TRANSFER](./02_rl_il_offline.md#gap-data-transfer-2026) |
| 모델 오차·물성·행동에 충분한 추정 | parameter vs model class, material/boundary, probe와 control utility | [SYSID](./05_world_models_safety.md#gap-sysid-2026), [DEFORM](./03_manipulation_contact.md#gap-deform-2026), [WM](./05_world_models_safety.md#gap-wm-2026) |
| 안전의 적용 범위·지속 운용 | 반응하는 상대, 지도/실공간 차이, 온도·payload·처리량 | [PLAN](./01_planning_control.md#gap-plan-2026), [GEOMETRY](./07_robotics_3d_perception.md#gap-geometry-2026), [THERMAL](./06_locomotion_whole_body.md#gap-thermal-2026) |
| 사람·다중 에이전트의 협업 | partner 능력, 응답 신뢰도·지연, task outcome·human workload | [HRI](./01_planning_control.md#gap-hri-2026) |
| VLA의 센싱과 영상 행동 표현 | 실행 시 contact 정보와 controller, 학습 시 video representation과 물리 supervision의 차이 | [CONTACT](./03_manipulation_contact.md#gap-contact-2026), [LATENT](./04_vla_generalist.md#gap-latent-2026) |
| VLA의 기억과 능력 보존 | memory/control confound, replay/normalizer·compute·phase coverage; 직접 선행으로 현재 보류 | [MEMORY](./04_vla_generalist.md#gap-memory-2026), [RETENTION](./04_vla_generalist.md#gap-retention-2026) |

## 이번 합성의 근거 경계

최근 [GAP-P4](../work/experiments/reactive_nav_pilot/RESULTS.md)는 [P3 계약 검사](../work/experiments/reactive_nav_contract/RESULTS.md) 뒤 로컬 Docker에서 dev12/cal24/test12 scene·384 branch를 비교했다. 위험 interaction은 양수였으나 보정 악화 방향은 반대여서 사전 joint gate가 실패했다. [GAP-PLAN](./01_planning_control.md#gap-plan-2026)은 **현재 진단 HOLD·일반 방법 NO-GO·native VLA HOLD**다. 좁은 synthetic negative evidence와 일반 가설·사용자 읽기 status를 구분한다. 이후 [GAP-DE1/DE2](../work/update/DEFORMABLE_ASSET_SUFFICIENCY_REVIEW_2026-10-24.md)는 변형체의 현재 공개 자산 설계를 종료했고, S1은 이 자료 부족을 P4의 실험 결과와 구분했다. 현재 인계는 [TODO](../TODO.md)를 따른다.

2026-10-23 첫 갱신은 [2026-10-22 등록 47편](../work/update/REGISTRY_ROLLUP_2026-10-22.md), 기존 source 감사와 [16개 후보 결과](../work/research_candidates/summaries/README.md)를 합성했다. 이 부분은 외부 paper의 새 full-text review나 사용자 정독 완료가 아니다. 이후 [GAP-R1 외부 조사](../work/update/VLA_GAP_SCOUT_2026-10-23.md)에서는 46건의 primary paper 자료와 resource 1건을 확인하고, 일부 직접 충돌 논문의 지정 본문·부록을 대조했다. 논문별 확인 깊이는 [source ledger](../work/sources/vla_gap_scout_2026-10-23.json)를 따른다. 모두를 전체 정독한 것으로 표시하지 않는다.

[GAP-W1 분야 확장](../work/update/BROAD_RESEARCH_GAP_SCOUT_2026-10-23.md)은 40건의 논문 근거를 통해 9개 조건부 질문을 추가했다. 7건은 지정 본문, 1건은 저자 method 설명, 나머지는 abstract/공식 색인 중심이다. [Source별 경계](../work/sources/broad_gap_scout_2026-10-23.json)를 유지하며, 기존 조사와 중복된 논문도 있어 두 목록의 수를 신규 논문 수로 합산하지 않는다. 새 질문은 모두 `CURATION-HYPOTHESIS`이고 별도 신규성 입증·사용자 정독·실험 완료를 뜻하지 않는다.

새 질문의 canonical 내용은 [접촉 센싱의 정보/제어 구분](./03_manipulation_contact.md#gap-contact-2026)과 [데이터 보완 선택의 직접 충돌](./04_vla_generalist.md#gap-data-2026)에 있다. 접촉은 GAP-R2 직접 비교 후 **REVISE / 진단 후보 HOLD**, 데이터 보완도 보류다. 각 track의 새 표는 **연구자 해석 / CURATION-HYPOTHESIS**이며 paper-supported claim, source 감사, 실제 측정을 구분한다. Manifest metadata 확인일·읽기 상태는 그대로 유지한다.

[GAP-V2 통합 비교](../work/update/INTEGRATED_GAP_REVIEW_2026-10-23.md)는 2024–2026 문헌 30건을 확인/재확인해 VLA 4축과 다른 분야 9축을 함께 검토했다. 공식 publication 근거 20건·저자 venue 1건·preprint 9건, 지정 HTML 구간 대조 6건이다. 추가 VLA 질문은 LATENT·MEMORY·RETENTION이며, 뒤 두 질문은 직접 충돌로 보류했다. 후속 [GAP-R2](../work/update/CONTACT_INTERFACE_REVIEW_2026-10-23.md)는 접촉 8편의 지정 본문/부록·RDP 공식 근거와 공개 code/data를 대조했다. 조사 목록 간 중복을 신규 논문 수로 합산하지 않는다. 질문의 상세 조건은 각 track의 Open Questions에 둔다.

[GAP-W2 직접 비교](../work/update/GAP_W2_COMPARATIVE_REVIEW_2026-10-23.md)는 GEOMETRY 5편·DATA-TRANSFER 6편(배경 1편 포함)·SYSID 3편의 지정 구간과 6개 code revision을 대조했다. Calibration/unknown-space·active perception, DP→π₀·π₀→π₀.₅ 데이터 전이, history 기반 grounding이 이미 존재한다. 넓은 신규 주장을 줄이고 세 분야의 진단 질문은 HOLD로 남겼다.

후속 [GAP-L2 latent-action 검토](../work/update/LATENT_ACTION_REVIEW_2026-10-23.md)는 직접 6편 지정 본문/부록과 registry 기반 2편, GitHub 4개 revision·HF 4개 목록을 대조했다. 일반 supervision/alignment/proxy 주장은 직접 충돌하며, 물리 조건에 따른 label 사용 위치의 예측만 REVISE / HOLD로 남겼다. Label 합집합·teacher/policy/decoder·단계별 holdout의 차이를 [VLA Open Questions](./04_vla_generalist.md#gap-latent-2026)에 반영했다. 두 작업 모두 새로운 가설의 성숙도·사용자 reading status를 올리지 않았다. 다음 활성 작업은 [TODO](../TODO.md)가 소유한다.

같은 정의·통계 원리·기존 method family를 새 기여로 다시 제안하지 않는다. 후보의 진행 이력은 요약과 dossier에 두고, 여기에는 비교 후 남은 질문·최소 baseline·기각 조건만 남긴다. 현재 E1/E2를 포함한 native 연구 실험은 HOLD이며 GPU만으로 판정을 바꾸지 않는다. 저장된 C3 수치의 [Docker 재분석](../work/experiments/portable/README.md)은 정책 효과 검증과 구분한다.

[REG-R3 top-tier 보완](../work/update/TOP_TIER_SUPPLEMENT_2026-10-25.md)은 17편의 abstract 기반 노트와 6개 track의 비교 연결을 추가했다. RoboArena/STAR-Gen의 평가 분해, 데이터 개입·접촉 controller·환경 질의의 차이를 반영했고 기존 연구 gate와 읽기 matrix는 보존했다.
