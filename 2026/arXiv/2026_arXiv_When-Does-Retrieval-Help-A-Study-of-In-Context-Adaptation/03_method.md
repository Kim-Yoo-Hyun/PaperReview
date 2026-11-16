# Method — When Does Retrieval Help? A Study of In-Context Adaptation in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Pipeline and Learning Rule

같은 RICL 계열 정책에서 image, image+state, VLA feature, random retrieval을 비교한다.

## Observation, State and Action

공유 시연 buffer에서 4개 entry → π0-FAST context → action. 원 RICL의 DINO distance interpolation은 모든 비교에서 제외한다.

## Temporal and Implementation Boundary

Control rate, action horizon, optimizer 전체 설정·checkpoint 호환성은 이번 노트에서 확정하지 않았다. 확인한 pipeline과 source 절을 넘어 수식·실행 가능성을 추정하지 않는다. Code URL의 존재는 native 실행 검증이 아니다.

근거: [확인한 원문](https://arxiv.org/html/2610.05492v1), §2–3, Appendix D–E.
