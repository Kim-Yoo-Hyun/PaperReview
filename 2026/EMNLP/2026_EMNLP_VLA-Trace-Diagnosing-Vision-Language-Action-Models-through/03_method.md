# Method — VLA-Trace: Diagnosing Vision-Language-Action Models through Representation and Behavior Tracing

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Pipeline and Learning Rule

Checkpoint CKA, attention knockout, region masking과 input editing을 단계적으로 연결한다.

## Observation, State and Action

VLM→pretrained VLA→task-finetuned VLA의 표현 및 action 경로와 rollout behavior를 비교한다.

## Temporal and Implementation Boundary

Control rate, action horizon, optimizer 전체 설정·checkpoint 호환성은 이번 노트에서 확정하지 않았다. 확인한 pipeline과 source 절을 넘어 수식·실행 가능성을 추정하지 않는다. Code URL의 존재는 native 실행 검증이 아니다.

근거: [확인한 원문](https://arxiv.org/html/2605.30117v1), 공식 EMNLP metadata; arXiv v1 §3.1–3.3; code README.
