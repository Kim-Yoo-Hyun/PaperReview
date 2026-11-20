# Insights — Improving Vision-Language-Action Model with Online Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## Paper-supported conclusion

탐색과 정책 갱신의 학습 절차를 분리한다. 시뮬레이션과 실제 조작에서 이 절차를 평가한다. [원문 및 평가 절](https://arxiv.org/pdf/2501.16664#page=5)

## Researcher interpretation

온라인 RL을 VLA에 직접 적용하는 방식과 RL·감독학습을 교대하는 방식을 대조할 기준이다.

- 직접 PPO 미세조정 기준선을 RL 탐색과 감독 갱신을 교대로 하는 절차로 대체해 시험한다. §IV 및 비교 실험. [pr-0524 · 원문](https://arxiv.org/pdf/2501.16664#page=4)

## 최소 비교 실험

동일 상호작용 예산에서 RL 단계와 시연 재학습 단계의 기여를 분리한다.
