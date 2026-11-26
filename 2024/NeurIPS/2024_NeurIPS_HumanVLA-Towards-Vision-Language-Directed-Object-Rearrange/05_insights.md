# Insights — HumanVLA: Towards Vision-Language Directed Object Rearrangement by Physical Humanoid

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §3–4, Appendix A–B (state/action spaces and distillation) 검토. [방법·평가 원문](https://arxiv.org/html/2406.19972)

## Paper-supported conclusion

목표 조건 RL과 adversarial motion prior로 상태 기반 교사를 학습한다. DAgger로 교사 행동을 모방하고, 훈련용 active rendering으로 물체를 바라보는 시선을 가르친다. [원문 및 평가 절](https://arxiv.org/html/2406.19972)

## Researcher interpretation

기존 WholeBodyVLA와 달리 보행 명령을 받아 균형을 잡는 별도 RL 정책이 배포 경로에 없다. 전신 관절 인터페이스에 대한 시뮬레이션 근거를 제공한다.

- 교사 강화학습의 사람다운 동작 보상에 AMP를 사용한다. §3.1. [pr-0851 · 원문](https://arxiv.org/html/2406.19972)

## 최소 비교 실험

같은 지시와 장면에서 교사와 학생의 운반 성공·배치 오차를 기록하고, 물체가 가려지는 시점별 차이를 비교한다.

## 검증 질문

보행 중 외란이나 물체 질량 변화에서 같은 관절 목표 정책이 발 접촉과 배치 오차를 함께 유지하는지는 별도 비교가 필요하다.
