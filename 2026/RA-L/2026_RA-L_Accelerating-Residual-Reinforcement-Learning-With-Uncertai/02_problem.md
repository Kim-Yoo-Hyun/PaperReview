# Accelerating Residual Reinforcement Learning With Uncertainty Estimation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

## Problem and Bottleneck

Residual RL의 탐색을 base 정책의 불확실성에 맞춰 조절해 상호작용 효율을 개선하는 문제다.

## Changed Formulation

불확실성 기반 탐색 제어를 사용한다. 확인한 critic 구현은 base와 residual이 합쳐진 최종 행동을 평가한다.

## Assumptions and Robotics Loop

불확실성 추정과 탐색 필요성이 관련되어야 한다. Actor 입력 변화와 critic 오차는 별도로 통제해야 한다.

Base 예측·불확실성 및 관측 → residual 탐색 → 합성 행동 → Q 평가. Critic 입력에 base action을 반영하는 원리는 이미 선행에 있다.

근거: [지정 본문](https://arxiv.org/html/2506.17564v2) — v2 IV-B / V-D; assymetric_sac.py critic_loss_fn/actor complete-action path. Code 검토 revision: `8125f33dcf490d4cf93d57a27d3e1963a47f52ea`; 실행하지 않았다.
