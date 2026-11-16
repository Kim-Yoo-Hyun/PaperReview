# Method — Embodied Interpretability: Linking Causal Understanding to Generalization in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.

## Pipeline and Learning Rule

Interventional masking 기반 ISS와 nuisance attribution 비중 NMR을 제안한다.

## Observation, State and Action

시각 영역 개입 → action prediction 변화 → attribution 및 nuisance score.

## Temporal and Implementation Boundary

Control rate, action horizon, optimizer 전체 설정·checkpoint 호환성은 이번 노트에서 확정하지 않았다. Abstract에 없는 목적함수·모듈 세부는 본문 확인 필요. Code URL의 존재는 native 실행 검증이 아니다.

근거: [확인한 원문](https://proceedings.mlr.press/v306/zhang26gz.html), 공식 proceedings abstract; software landing.
