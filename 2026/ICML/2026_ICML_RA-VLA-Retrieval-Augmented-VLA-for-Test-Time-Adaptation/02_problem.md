# Problem — RA-VLA: Retrieval-Augmented VLA for Test-Time Adaptation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.

## Target Problem

시연 context가 있어도 retrieval 및 pretrained 행동 관성 때문에 새 task에 적응하지 못하는 문제.

## Robotics Loop

현재 관측·검색 context → frozen/test-time VLA의 행동 적응. 세부 selector·token budget·control timing은 본문 확인 필요.

## Assumptions to Check — Researcher Interpretation

연구자 점검: retrieval bank의 성공 provenance·평가 episode 독립성을 확인한다.

개념 연결: in-context imitation/RICL → RA-VLA → bank growth의 이득과 간섭.

## Boundary

정확한 formulation·loss·필요 가정은 본문 확인 전 확정하지 않는다.

근거: [확인한 원문](https://proceedings.mlr.press/v306/jang26c.html), 공식 proceedings abstract; arXiv identity.
