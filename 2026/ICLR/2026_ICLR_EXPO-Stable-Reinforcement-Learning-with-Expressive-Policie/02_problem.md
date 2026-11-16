# EXPO: Stable Reinforcement Learning with Expressive Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

## Problem and Bottleneck

표현력이 큰 imitation 정책을 online RL로 개선할 때 안정적인 최적화와 탐색을 확보하는 문제다.

## Changed Formulation

Expressive base의 imitation 업데이트와 Gaussian edit 정책의 Q 기반 업데이트를 결합하고, base/edit 행동을 value로 선택한다.

## Assumptions and Robotics Loop

Q 값이 base/edit 후보 선택에 유용해야 하며 base와 editor가 함께 적응하는 학습 분포를 전제한다.

관측 → base 행동 및 수정 행동 → Q 선택 → 환경. Rollout 선택과 TD target에서의 선택 역할을 함께 확인해야 한다.

근거: [지정 본문](https://arxiv.org/html/2507.07986v3) — §4 / Algorithm 1; expo_learner.py selected update paths. Code 검토 revision: `bbd571306b413e05d5d4b01a6efa20352c2b891a`; 실행하지 않았다.
