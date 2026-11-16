# Problem — DRILL: Training World Models to Improve Policies, Not Predict Pixels

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Target Problem

World model의 pixel 예측 품질과 그 안에서 학습한 정책의 return이 일치하지 않는 문제.

## Robotics Loop

World model imagined trajectory → policy update → downstream return → world-model update.

## Assumptions to Check — Researcher Interpretation

연구자 점검: simulator budget과 world-model 학습 compute를 모두 비교해야 한다.

개념 연결: world-model RL → WMPO/VLAW → policy-utility objective.

## Boundary

VWI와 IMG의 관계는 가정에 의존한다. Pixel 품질과 control utility 차이 자체는 이 논문이 이미 직접 다룬다. 실제 로봇 검증으로 확대하지 않는다.

근거: [확인한 원문](https://arxiv.org/html/2610.30814v1), §3, §5.5, §6 limitations.
