# Compliance for Free: Learning Identifiable Impedance via Bilateral Teleoperation

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §III-F/G, §IV, Table II 검토. [방법·평가 원문](https://arxiv.org/html/2609.19976)

- Year/Venue: 2026 / arXiv
- Authors: Harsha Guda, Adrià Colomé, Carme Torras
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: VLA, variable stiffness, bilateral teleoperation, Impedance Control, force modulation
- Official paper: https://arxiv.org/abs/2609.19976
- Code/Project: not identified

## 연구 질문과 기여

실제 끝단 위치와 접촉력만 기록하면 평형점의 오차와 강성의 효과가 섞인다. 같은 힘도 다른 평형점과 강성 조합에서 발생한다.

양방향 시연의 leader 자세로 의도한 평형점을 따로 기록하고, 관측으로 식별할 수 있는 축·시점에 강성 레이블을 만든다. SmolVLA의 공유 표현 위에서 평형 자세에 flow matching, 로그 강성에 마스킹한 Huber 손실을 쓴다.

## 정책 출력

장면·손목 RGB, 언어와 wrench 이력에서 32스텝 청크를 예측한다. 각 스텝은 6차원 평형 자세와 6축 로그 강성이며 하위 임피던스 제어기가 실행한다. [방법 원문](https://arxiv.org/html/2609.19976)

## 평가 범위

실물 Franka Research 3로 경사진 화이트보드를 닦았다. Table II에서 normally/firmly 지시의 실현 접촉력 RMS 추정값은 6.40/9.12 N이다. 지시 세기마다 12회, 3개 학습 seed를 합쳤고, 손목 외력은 하드웨어 추정값이다. [원문 및 평가 절](https://arxiv.org/html/2609.19976)

## 선정 근거

CompVLA와 출력은 비슷하지만 강성 정답을 어떻게 얻는지가 다르다. 시연의 측정 가능성이 학습한 접촉력 차이로 이어지는지 추적할 수 있다.
