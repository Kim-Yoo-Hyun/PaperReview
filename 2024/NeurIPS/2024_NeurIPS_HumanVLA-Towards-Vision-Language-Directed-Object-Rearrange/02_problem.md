# Problem — HumanVLA: Towards Vision-Language Directed Object Rearrangement by Physical Humanoid

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §3–4, Appendix A–B (state/action spaces and distillation) 검토. [방법·평가 원문](https://arxiv.org/html/2406.19972)

## 문제와 검증 범위

물체 위치·목표·내비게이션 waypoint를 아는 시뮬레이터 교사의 전신 행동을, 1인칭 영상과 언어를 받는 정책으로 옮길 수 있는지 묻는다.

Isaac Gym에서 15개 강체로 구성한 휴머노이드가 물체로 걸어가 운반하고 재배치하는 과제를 평가했다. 본문은 배치 성공 및 거리 오차를 보고한다. 실물 휴머노이드 전이는 여기서 평가하지 않았다. [원문 및 평가 절](https://arxiv.org/html/2406.19972)
