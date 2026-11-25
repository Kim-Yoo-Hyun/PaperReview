# Problem — See Selectively, Act Adaptively: Dual-Level Structural Decomposition for Bimanual Robot Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`

2026-11-20에 저자 본문 v2의 III–IV절을 확인했다. [논문 정보와 출처](./01_overview.md)

같은 에피소드에서도 두 팔이 서로 다른 물체로 접근하는 구간과 공동 물체를 안정시키거나 넘기는 구간이 이어진다. 단일 행동 생성기는 이때 달라지는 정보 의존성과 제약을 하나의 경로로 처리한다. 논문은 외부 카메라를 전체 상황 관측으로 유지하면서 두 손목 뷰의 관련성과 팔 사이의 의존성을 별도로 표현한다. [본문 I, III-A](https://arxiv.org/html/2606.13279v2#S3.SS1)

행동 모드의 의미는 작업 구간에 붙인 인간 라벨에 의존한다. 두 손이 동시에 움직이는 횟수나 실제 접촉력만으로 모드를 정의하지 않는다. 지각·상태 → 행동 경로 선택 → 다관절 명령의 제어 루프에 해당한다. [라벨 정의](https://arxiv.org/html/2606.13279v2#S3.SS4)
