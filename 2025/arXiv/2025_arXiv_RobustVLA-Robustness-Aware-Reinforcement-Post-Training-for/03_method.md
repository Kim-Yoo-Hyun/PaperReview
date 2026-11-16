# Method — RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Pipeline and Learning Rule

PPO에 observation log-probability Jacobian penalty와 이전 reference 정책 대비 mean-action deviation penalty를 더하고 교란 강도를 조절한다.

## Observation, State and Action

교란된 관측·rollout advantage → regularized VLA update → 행동. Smooth penalty는 인접 시점 차분이 아니라 정책 갱신 전후 차이다.

## Temporal and Implementation Boundary

Control rate, action horizon, optimizer 전체 설정·checkpoint 호환성은 이번 노트에서 확정하지 않았다. 확인한 pipeline과 source 절을 넘어 수식·실행 가능성을 추정하지 않는다. Code URL의 존재는 native 실행 검증이 아니다.

근거: [확인한 원문](https://arxiv.org/html/2511.01331v2), v2 §4.2–4.3, Algorithm 1; §5 범위.
