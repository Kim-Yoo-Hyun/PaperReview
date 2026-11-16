# Accelerating Residual Reinforcement Learning With Uncertainty Estimation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

## Policy and Learning Pipeline

불확실성 기반 탐색 제어를 사용한다. 확인한 critic 구현은 base와 residual이 합쳐진 최종 행동을 평가한다.

## Observation, State, and Action

Base 예측·불확실성 및 관측 → residual 탐색 → 합성 행동 → Q 평가. Critic 입력에 base action을 반영하는 원리는 이미 선행에 있다.

## Training versus Deployment

불확실성 추정과 탐색 필요성이 관련되어야 한다. Actor 입력 변화와 critic 오차는 별도로 통제해야 한다.

제어 주기·horizon·loss 계수 전체는 이번 노트에서 확정하지 않았다. 실제 baseline 이식 전 원문과 code 설정을 함께 대조한다.

근거: [지정 본문](https://arxiv.org/html/2506.17564v2) — v2 IV-B / V-D; assymetric_sac.py critic_loss_fn/actor complete-action path. Code 검토 revision: `8125f33dcf490d4cf93d57a27d3e1963a47f52ea`; 실행하지 않았다.
