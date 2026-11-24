# Constraint-Grounded Reinforcement Learning for Variable Impedance Control in Contact-Rich Robotic Insertion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 표시한 평가 항목을 확인했다.
> Source audit: 2026-11-24 원문 대조.

## Evaluation in One Sentence

허용 구간 투영이 보장하는 대상은 적용 이득이다. 힘 상한을 지킨 삽입의 85.8±7.7%는 경사 삽입 시뮬레이션에서 측정한 시드 간 평균±표준편차다. [PDF 5쪽](https://arxiv.org/pdf/2609.13516v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2609.13516v1#page=6) · [PDF 10쪽](https://arxiv.org/pdf/2609.13516v1#page=10) · [PDF 15쪽](https://arxiv.org/pdf/2609.13516v1#page=15)

## Evaluation Type and Scope

- **Evaluation type:** `EMPIRICAL / SIMULATION`.

## Dataset / Benchmark Role

힘 상한과 이득 허용 범위가 주어진 경사 삽입 시뮬레이션을 평가했다. [PDF 7쪽](https://arxiv.org/pdf/2609.13516v1#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2609.13516v1#page=8)

## Metrics and Success Definition

힘 상한 준수와 과제 완료를 함께 요구하는 성공률(CCS)과 기하학적 삽입 성공률을 따로 보고했다. [PDF 9쪽](https://arxiv.org/pdf/2609.13516v1#page=9) · [PDF 10쪽](https://arxiv.org/pdf/2609.13516v1#page=10)

## Baselines and Fairness

표 V에는 고정 중간 이득 제어기, 힘 상한 입력을 제거한 정책, 장벽 항을 사용한 학습 비교군이 있다. [PDF 10쪽](https://arxiv.org/pdf/2609.13516v1#page=10)

표 IV·V의 K-conditioned 비교 정책은 이득 구간을 직접 입력받고 힘 상한은 받지 않는다. 훈련 분포에서 이 정책의 힘 상한 준수 삽입 성공률은 89.34±2.45%였다. [PDF 9쪽](https://arxiv.org/pdf/2609.13516v1#page=9) · [PDF 10쪽](https://arxiv.org/pdf/2609.13516v1#page=10)

## Statistics, Efficiency, and Reproducibility

학습 시드 5개의 평균과 표준편차를 보고했다. [PDF 9쪽](https://arxiv.org/pdf/2609.13516v1#page=9) · [PDF 10쪽](https://arxiv.org/pdf/2609.13516v1#page=10) · [PDF 15쪽](https://arxiv.org/pdf/2609.13516v1#page=15)

## Proposed Evaluation — Researcher Interpretation

동일 controller projection에서 비-VLA와 VLA actor의 조건 전이를 비교한다.

이 실험은 실행하지 않았으며, 수치나 결론을 미리 부여하지 않는다.

## Evidence Anchor

[공식 paper/abstract](https://arxiv.org/abs/2609.13516).
