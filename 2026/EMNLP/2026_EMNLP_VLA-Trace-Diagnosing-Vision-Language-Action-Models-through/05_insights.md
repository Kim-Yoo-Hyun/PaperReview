# Insights — VLA-Trace: Diagnosing Vision-Language-Action Models through Representation and Behavior Tracing

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Paper-supported conclusion

Robot adaptation에서 multimodal representation 변화가 행동의 grounding과 어떻게 이어지는지 분석한다.에 대한 접근은 [method](./03_method.md), 지지하는 실험 범위는 [evaluation](./04_evaluation.md)에서 확인한다. 지정 절의 결과를 읽었으며 재현하거나 일반적인 우월성을 검증한 것은 아니다.

근거: [확인한 원문](https://arxiv.org/html/2605.30117v1), 공식 EMNLP metadata; arXiv v1 §3.1–3.3; code README.

## Researcher interpretation

FEEDBACK의 표현/행동 연결 진단 도구로 REFERENCE에 보존한다. 기존 mechanistic NEXT와 중복되는 도구 축이며 현재 학습 메커니즘의 직접 검증은 아니다.

개념 연결: OpenVLA·CKA → VLA-Trace → post-training behavioral diagnosis.

- 취약 조건 점검: 연구자 점검: latent similarity와 causal contribution의 추정 대상을 분리한다.
- 반증 가능한 질문: 표현 변화 없이 행동 피드백 사용이 바뀌거나, 그 반대인 RL/SFT pair가 있는가?
- 최소 비교 제안: 같은 입력의 CKA를 행동 fresh/stale 개입과 나란히 보며 representation drift만으로 정책 원인을 판단하지 않는다.

이 비교는 연구자 제안이며 논문이 이미 수행한 실험이나 새 기여의 입증이 아니다. 현재 evidence maturity는 `CURATION-HYPOTHESIS`다.
