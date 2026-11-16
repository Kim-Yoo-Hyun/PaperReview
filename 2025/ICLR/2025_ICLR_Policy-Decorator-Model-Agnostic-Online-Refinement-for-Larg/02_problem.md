# Policy Decorator: Model-Agnostic Online Refinement for Large Policy Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

## Problem and Bottleneck

Offline imitation 정책의 조작 오차를 online RL로 보완하면서 초반 탐색으로 기존 행동을 훼손하는 문제를 줄인다.

## Changed Formulation

동결 base 위에 SAC residual을 학습하고 residual 범위와 탐색 진행을 제어한다.

## Assumptions and Robotics Loop

초기 base 능력과 적절한 residual 크기·탐색 schedule이 학습에 중요하다.

Base 행동 + 제한된 residual → 환경. Base 모델 계열별 적용 가능성과 학습된 residual weights의 전이는 서로 다른 주장이다.

근거: [지정 본문](https://proceedings.iclr.cc/paper_files/paper/2025/file/45c361d4117d598d4bb6568b407e9ac9-Paper-Conference.pdf) — final paper §4.1–4.3, selected Appendix B.5; project/code README.
