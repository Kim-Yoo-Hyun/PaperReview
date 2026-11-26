# Method — HumanVLA: Towards Vision-Language Directed Object Rearrangement by Physical Humanoid

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §3–4, Appendix A–B (state/action spaces and distillation) 검토. [방법·평가 원문](https://arxiv.org/html/2406.19972)

## 관측과 출력

학생은 1인칭 시각·언어와 로봇 고유수용 상태로 전신 28개 관절의 PD 목표를 30 Hz로 낸다. 관절 PD가 torque를 계산하고 교사의 waypoint·물체 정답은 배포 경로에서 빠진다.

## 학습·실행 방법

목표 조건 RL과 adversarial motion prior로 상태 기반 교사를 학습한다. DAgger로 교사 행동을 모방하고, 훈련용 active rendering으로 물체를 바라보는 시선을 가르친다.

- 교사 강화학습의 사람다운 동작 보상에 AMP를 사용한다. §3.1. [pr-0851 · 원문](https://arxiv.org/html/2406.19972)
