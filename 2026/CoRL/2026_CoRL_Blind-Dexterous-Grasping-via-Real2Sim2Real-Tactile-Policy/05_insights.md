# Insights — Blind Dexterous Grasping via Real2Sim2Real Tactile Policy Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## Paper-supported conclusion

기하를 아는 시뮬레이션 전문가들의 성공 궤적을 수집한다. 실물에서는 촉각·로봇 상태를 관측하는 확산 정책을 배포한다. [원문 및 평가 절](https://arxiv.org/pdf/2606.11767#page=6)

## Researcher interpretation

시각이 없는 다지 파지에서 촉각 접촉 보정과 RL 전문가 증류를 검토할 기준이다.

- 다양한 RL 전문가의 성공 궤적을 촉각에 조건화한 Diffusion Policy [10]로 증류한다. Method overview. [pr-0019 · 원문](https://arxiv.org/pdf/2606.11767#page=2)

## 최소 비교 실험

실물 접촉 이벤트 보정 유무를 고정된 전문가 궤적으로 비교한다.
