# Insights — VTDexManip: A Dataset and Benchmark for Visual-tactile Pretraining and Dexterous Manipulation with Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## Paper-supported conclusion

희소 이진 촉각과 시각을 함께 학습하는 조건을 제공한다. 과제·센서 잡음·시점 조건별로 모달리티의 기여를 평가한다. [원문 및 평가 절](https://proceedings.iclr.cc/paper_files/paper/2025/file/e19b6f65791e350347bcff8a3955cb5b-Paper-Conference.pdf#page=6)

## Researcher interpretation

희소 이진 촉각의 기여를 같은 RL 과제에서 비교할 수 있는 데이터셋과 벤치마크다.

- 시각·촉각 표현을 사용하는 조작 정책의 학습기로 PPO를 사용한다. Manipulation Policy Learning. [pr-0524 · 원문](https://proceedings.iclr.cc/paper_files/paper/2025/file/e19b6f65791e350347bcff8a3955cb5b-Paper-Conference.pdf#page=6)

## 최소 비교 실험

동일 PPO 예산에서 촉각 입력 효과와 시각·촉각 사전학습 효과를 분리한다.
