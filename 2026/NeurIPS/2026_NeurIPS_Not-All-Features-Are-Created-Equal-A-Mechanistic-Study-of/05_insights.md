# Insights — Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Paper-supported conclusion

언어·시각 표현과 실제 운동 생성 사이의 관계를 intervention으로 조사한다.에 대한 접근은 [method](./03_method.md), 지지하는 실험 범위는 [evaluation](./04_evaluation.md)에서 확인한다. 지정 절의 결과를 읽었으며 재현하거나 일반적인 우월성을 검증한 것은 아니다.

근거: [확인한 원문](https://arxiv.org/pdf/2603.19233v6), v6 (2026-11-02), §4.7–4.8, Appendix B.

## Researcher interpretation

FEEDBACK의 출발 근거이자 과장 방지 선행. Activation replay 결과와 자연 정책의 closed-loop 행동을 구별하는 NEXT.

개념 연결: OpenVLA·π0.5 → mechanistic steering → RL4VLA 후학습 진단.

- 취약 조건 점검: 연구자 점검: 인위적 activation 개입의 효과를 자연 학습 메커니즘으로 일반화하지 않는다.
- 반증 가능한 질문: 동일 학습 계보의 RL/SFT 정책에서 fresh observation의 행동상 가치가 nuisance 반응과 다르게 변하는가?
- 최소 비교 제안: Activation 주입 없이 물리 이동×fresh/stale 관측을 교차하고, clean 능력·background 변화·같은 데이터 모방을 대조한다.

이 비교는 연구자 제안이며 논문이 이미 수행한 실험이나 새 기여의 입증이 아니다. 현재 evidence maturity는 `CURATION-HYPOTHESIS`다.
