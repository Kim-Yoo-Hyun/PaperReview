# Evaluation — HumanVLA: Towards Vision-Language Directed Object Rearrangement by Physical Humanoid

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §3–4, Appendix A–B (state/action spaces and distillation) 검토. [방법·평가 원문](https://arxiv.org/html/2406.19972)

## 평가 조건

Isaac Gym에서 15개 강체로 구성한 휴머노이드가 물체로 걸어가 운반하고 재배치하는 과제를 평가했다. 본문은 배치 성공 및 거리 오차를 보고한다. 실물 휴머노이드 전이는 여기서 평가하지 않았다. [원문 및 평가 절](https://arxiv.org/html/2406.19972)

## 해석할 때 확인할 조건

보행 중 외란이나 물체 질량 변화에서 같은 관절 목표 정책이 발 접촉과 배치 오차를 함께 유지하는지는 별도 비교가 필요하다.
