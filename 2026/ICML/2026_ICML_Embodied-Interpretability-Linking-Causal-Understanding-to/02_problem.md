# Problem — Embodied Interpretability: Linking Causal Understanding to Generalization in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.

## Target Problem

분포 변화 아래 실패가 task-irrelevant 시각 단서 의존과 어떤 관계인지 측정한다.

## Robotics Loop

시각 영역 개입 → action prediction 변화 → attribution 및 nuisance score.

## Assumptions to Check — Researcher Interpretation

연구자 점검: masking이 입력 분포를 바꾸는 효과와 유효 정보 제거를 구별해야 한다.

개념 연결: OpenVLA → mechanistic attribution → RL 후학습의 행동 진단.

## Boundary

정확한 formulation·loss·필요 가정은 본문 확인 전 확정하지 않는다.

근거: [확인한 원문](https://proceedings.mlr.press/v306/zhang26gz.html), 공식 proceedings abstract; software landing.
