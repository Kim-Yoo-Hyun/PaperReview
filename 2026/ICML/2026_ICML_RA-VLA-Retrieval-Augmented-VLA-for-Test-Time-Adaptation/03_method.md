# Method — RA-VLA: Retrieval-Augmented VLA for Test-Time Adaptation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.

## Pipeline and Learning Rule

Behavior-aligned context retrieval과 grounded execution pipeline을 결합한다.

## Observation, State and Action

현재 관측·검색 context → frozen/test-time VLA의 행동 적응. 세부 selector·token budget·control timing은 본문 확인 필요.

## Temporal and Implementation Boundary

Control rate, action horizon, optimizer 전체 설정·checkpoint 호환성은 이번 노트에서 확정하지 않았다. Abstract에 없는 목적함수·모듈 세부는 본문 확인 필요. Code URL의 존재는 native 실행 검증이 아니다.

근거: [확인한 원문](https://proceedings.mlr.press/v306/jang26c.html), 공식 proceedings abstract; arXiv identity.
