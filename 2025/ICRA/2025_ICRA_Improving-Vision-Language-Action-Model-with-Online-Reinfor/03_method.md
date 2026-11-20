# Method — Improving Vision-Language-Action Model with Online Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## 관측과 출력

탐색과 정책 갱신의 학습 절차를 분리한다.

## 학습·실행 방법

탐색과 정책 갱신의 학습 절차를 분리한다. 시뮬레이션과 실제 조작에서 이 절차를 평가한다.

- 직접 PPO 미세조정 기준선을 RL 탐색과 감독 갱신을 교대로 하는 절차로 대체해 시험한다. §IV 및 비교 실험. [pr-0524 · 원문](https://arxiv.org/pdf/2501.16664#page=4)
