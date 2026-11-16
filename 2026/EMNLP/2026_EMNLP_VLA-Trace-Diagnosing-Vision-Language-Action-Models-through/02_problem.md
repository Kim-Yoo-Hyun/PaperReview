# Problem — VLA-Trace: Diagnosing Vision-Language-Action Models through Representation and Behavior Tracing

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Target Problem

Robot adaptation에서 multimodal representation 변화가 행동의 grounding과 어떻게 이어지는지 분석한다.

## Robotics Loop

VLM→pretrained VLA→task-finetuned VLA의 표현 및 action 경로와 rollout behavior를 비교한다.

## Assumptions to Check — Researcher Interpretation

연구자 점검: latent similarity와 causal contribution의 추정 대상을 분리한다.

개념 연결: OpenVLA·CKA → VLA-Trace → post-training behavioral diagnosis.

## Boundary

읽은 arXiv v1과 EMNLP 최종본의 전체 동등성은 확인하지 않았다. 공개 toolkit의 존재와 우리 checkpoint adapter의 호환·실행은 별개다.

근거: [확인한 원문](https://arxiv.org/html/2605.30117v1), 공식 EMNLP metadata; arXiv v1 §3.1–3.3; code README.
