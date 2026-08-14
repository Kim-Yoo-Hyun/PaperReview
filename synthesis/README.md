# Robotics Research Synthesis

이 디렉토리는 논문별 요약을 반복하는 곳이 아니라, CORE/NEXT 논문을 연구 트랙별로 비교하고 연구 공백을 축적하는 공간이다.

## Documents

1. [Planning and Control](./01_planning_control.md)
2. [RL, IL, Offline Learning, and Robot Data](./02_rl_il_offline.md)
3. [Manipulation, Contact, Tactile, and Dexterity](./03_manipulation_contact.md)
4. [VLA and Generalist Robot Policies](./04_vla_generalist.md)
5. [World Models, Safety, and Recovery](./05_world_models_safety.md)
6. [Locomotion, Whole-Body, Mobile Manipulation, and Humanoids](./06_locomotion_whole_body.md)
7. [Robotics-Enabling 3D Perception](./07_robotics_3d_perception.md)

Cross-track gap은 [RESEARCH_GAPS.md](../research/RESEARCH_GAPS.md), 실행 가능한 가설과 최소 실험은 [RESEARCH_IDEAS.md](../research/RESEARCH_IDEAS.md)에서 관리한다.

## Update Rule

논문을 `READ`로 바꿀 때 해당 트랙 문서의 comparison matrix에 한 행을 추가한다. `SYNTHESIZED`는 다음 조건을 모두 만족할 때만 사용한다.

1. 논문 단위로 문제, interface, 실험, failure mode가 기록되어 있다.
2. 같은 트랙의 선행 연구와 차이가 comparison matrix에 반영되어 있다.
3. `Open Questions` 또는 `Research Gaps`에 연구적 함의가 추가되어 있다.

`Dependency and Evolution`은 foundation → transition → frontier의 계보와 변화를 기록한다. 직접 citation과 개념적 연결을 혼동하지 않는다. 각 문서의 `Research Gaps`에는 중앙 gap ID와 정독으로 확인한 track-specific evidence만 남기고, gap 설명과 연구 아이디어를 복제하지 않는다.

현재 comparison matrix의 `CURATION-SEED` 행은 공식 abstract와 registry-level 지식을 바탕으로 만든 **읽기 전 비교 가설**이다. tracker가 `FULL_TEXT_CHECKED`가 되기 전에는 확정된 paper claim이나 정량 비교로 인용하지 않는다. 정독 시 source page/section/table을 확인해 해당 cell을 수정하고, seed script로 matrix를 다시 덮어쓰지 않는다.

읽기 진행 상태의 canonical source는 [READING_STATUS.csv](../research/READING_STATUS.csv)이며, 상태 전환 규칙은 [READING_STATUS.md](../research/READING_STATUS.md)를 따른다.
