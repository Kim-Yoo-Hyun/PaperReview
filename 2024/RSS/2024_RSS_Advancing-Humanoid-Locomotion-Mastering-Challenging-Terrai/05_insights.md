# Insights — Advancing Humanoid Locomotion: Mastering Challenging Terrains with Denoising World Model Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## Paper-supported conclusion

세계 모델 학습과 보행 강화학습을 결합한다. 다른 지형의 실제 보행에서 시뮬레이션 학습 정책의 전이를 평가한다. [원문 및 평가 절](https://roboticsproceedings.org/rss20/p058.pdf#page=7)

## Researcher interpretation

잡음 제거 세계 모델과 보행 RL을 실제 불규칙 지형에 전이한 대표 제어 사례다.

- 세계 모델의 상태 표현과 PPO의 정책 최적화 [29]를 결합한다. Training losses, p.7 지형별 PPO 비교. [pr-0524 · 원문](https://roboticsproceedings.org/rss20/p058.pdf#page=4)

## 최소 비교 실험

보행 보상을 고정하고 상태 추정기 교체 전후의 지형별 실패를 나눈다.
