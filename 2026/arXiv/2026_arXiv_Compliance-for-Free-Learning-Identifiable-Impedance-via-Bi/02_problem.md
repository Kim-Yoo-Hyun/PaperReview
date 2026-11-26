# Problem — Compliance for Free: Learning Identifiable Impedance via Bilateral Teleoperation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §III-F/G, §IV, Table II 검토. [방법·평가 원문](https://arxiv.org/html/2609.19976)

## 문제와 검증 범위

실제 끝단 위치와 접촉력만 기록하면 평형점의 오차와 강성의 효과가 섞인다. 같은 힘도 다른 평형점과 강성 조합에서 발생한다.

실물 Franka Research 3로 경사진 화이트보드를 닦았다. Table II에서 normally/firmly 지시의 실현 접촉력 RMS 추정값은 6.40/9.12 N이다. 지시 세기마다 12회, 3개 학습 seed를 합쳤고, 손목 외력은 하드웨어 추정값이다. [원문 및 평가 절](https://arxiv.org/html/2609.19976)
