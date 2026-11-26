# Method — Compliance for Free: Learning Identifiable Impedance via Bilateral Teleoperation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §III-F/G, §IV, Table II 검토. [방법·평가 원문](https://arxiv.org/html/2609.19976)

## 관측과 출력

장면·손목 RGB, 언어와 wrench 이력에서 32스텝 청크를 예측한다. 각 스텝은 6차원 평형 자세와 6축 로그 강성이며 하위 임피던스 제어기가 실행한다.

## 학습·실행 방법

양방향 시연의 leader 자세로 의도한 평형점을 따로 기록하고, 관측으로 식별할 수 있는 축·시점에 강성 레이블을 만든다. SmolVLA의 공유 표현 위에서 평형 자세에 flow matching, 로그 강성에 마스킹한 Huber 손실을 쓴다.

- SmolVLA의 시각언어 백본을 고정하고 행동 전문가를 강성 출력에 맞게 학습한다. §III-F. [pr-0915 · 원문](https://arxiv.org/html/2609.19976)
