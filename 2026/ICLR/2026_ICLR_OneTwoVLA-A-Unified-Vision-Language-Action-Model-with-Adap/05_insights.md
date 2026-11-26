# Insights — OneTwoVLA: A Unified Vision-Language-Action Model with Adaptive Reasoning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-25 · §3.1, Algorithm 1, §4, Appendix F (hardware) 검토. [방법·평가 원문](https://arxiv.org/html/2505.11917) · [저자 코드](https://github.com/Fanqi-Lin/OneTwoVLA)

## Paper-supported conclusion

같은 모델이 [BOR]와 [BOA] 중 하나를 먼저 생성한다. 전자에서는 텍스트로 계획·상태를 갱신하고 후자에서는 π0의 flow-matching 전문가로 행동 청크를 낸다. [원문 및 평가 절](https://arxiv.org/html/2505.11917)

## Researcher interpretation

상위 추론과 연속 행동 전문가가 한 정책 안에서 모드를 교대하는 사례다. π0.5의 하위 지시 재예측과 달리 추론할 시점 자체가 학습 대상이다.

- π0를 기본 VLA로 사용하고 연속 행동 전문가의 flow-matching 손실을 계승한다. §3.1. [pr-0746 · 원문](https://arxiv.org/html/2505.11917)

## 최소 비교 실험

같은 체크포인트·과제에서 학습된 모드 선택과 같은 평균 호출 수의 주기적 선택을 비교해 복구 성공과 재추론 지연을 기록한다.

## 검증 질문

추론 호출 빈도를 맞췄을 때도 사건에 맞춘 모드 전환이 긴 작업의 실패 후 복구에 이득을 주는지 따로 비교할 수 있다.
