# Problem — RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Target Problem

Reward 중심 후학습이 관측·실행 교란에 대한 강건성을 충분히 다루지 못하는 문제.

## Robotics Loop

교란된 관측·rollout advantage → regularized VLA update → 행동. Smooth penalty는 인접 시점 차분이 아니라 정책 갱신 전후 차이다.

## Assumptions to Check — Researcher Interpretation

연구자 점검: 일반 nuisance regularization을 semantic-change 보존으로 해석하지 않는다.

개념 연결: PPO → RL4VLA → robustness-aware post-training.

## Boundary

ICLR under-review PDF는 확인했으나 채택을 확인하지 못해 arXiv로 등록한다. 2510.00037의 동명 Multi-Modal Perturbations 논문과 별개다.

근거: [확인한 원문](https://arxiv.org/html/2511.01331v2), v2 §4.2–4.3, Algorithm 1; §5 범위.
