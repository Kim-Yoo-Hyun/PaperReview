# Robotics Research Synthesis

- Updated: 2026-10-23 KST

이 디렉토리는 논문별 요약을 반복하는 곳이 아니라, CORE/NEXT 논문을 연구 트랙별로 비교하고 근거 기반 `Open Questions`를 축적하는 공간이다.

현재 초점은 VLA 기반 manipulation·navigation과 action-relevant 3D다. 최신 후보 탐색에서는 RL을 필수 조건으로 두지 않는다. Generated queue는 CORE 47 + NEXT 275편을 7개 primary track에 배정한다. 수동 comparison matrix의 기존 읽기 결과는 tier 변경 후에도 보존한다. 읽기 순서의 기준은 [READING_PLAN.md](../research/READING_PLAN.md)이며, 각 트랙의 Reading Path는 비교 계보를 설명한다.

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

## 이번 합성의 근거 경계

2026-10-23 갱신은 [2026-10-22 등록 47편](../work/update/REGISTRY_ROLLUP_2026-10-22.md), 기존 source 감사와 [16개 후보 결과](../work/research_candidates/summaries/README.md)를 합성한다. 외부 paper의 새 full-text review나 사용자 정독 완료가 아니다. 각 track의 새 표는 **연구자 해석 / CURATION-HYPOTHESIS**이며 paper-supported claim, source 감사, 실제 측정을 구분한다. 공식 metadata의 확인일은 manifest의 원래 날짜를 유지한다.

같은 정의·통계 원리·기존 method family를 새 기여로 다시 제안하지 않는다. 후보의 진행 이력은 요약과 dossier에 두고, 여기에는 비교 후 남은 질문·최소 baseline·기각 조건만 남긴다. 현재 E1/E2를 포함한 native 연구 실험은 HOLD이며 GPU만으로 판정을 바꾸지 않는다. 저장된 C3 수치의 [Docker 재분석](../work/experiments/portable/README.md)은 정책 효과 검증과 구분한다.
