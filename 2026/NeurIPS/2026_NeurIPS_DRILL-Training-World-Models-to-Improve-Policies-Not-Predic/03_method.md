# Method — DRILL: Training World Models to Improve Policies, Not Predict Pixels

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Pipeline and Learning Rule

Imagined rollout의 GRPO update 이후 return을 목표로 world model을 학습하는 bilevel 구성. VWI 가중 surrogate와 IMG meta-gradient 두 형태를 제안한다.

## Observation, State and Action

World model imagined trajectory → policy update → downstream return → world-model update.

## Temporal and Implementation Boundary

Control rate, action horizon, optimizer 전체 설정·checkpoint 호환성은 이번 노트에서 확정하지 않았다. 확인한 pipeline과 source 절을 넘어 수식·실행 가능성을 추정하지 않는다. Code URL의 존재는 native 실행 검증이 아니다.

근거: [확인한 원문](https://arxiv.org/html/2610.30814v1), §3, §5.5, §6 limitations.
