# Insights — DRILL: Training World Models to Improve Policies, Not Predict Pixels

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Paper-supported conclusion

World model의 pixel 예측 품질과 그 안에서 학습한 정책의 return이 일치하지 않는 문제.에 대한 접근은 [method](./03_method.md), 지지하는 실험 범위는 [evaluation](./04_evaluation.md)에서 확인한다. 지정 절의 결과를 읽었으며 재현하거나 일반적인 우월성을 검증한 것은 아니다.

근거: [확인한 원문](https://arxiv.org/html/2610.30814v1), §3, §5.5, §6 limitations.

## Researcher interpretation

World-model utility라는 broad gap의 직접 충돌을 registry에 남겨 같은 제안을 반복하지 않도록 한다.

개념 연결: world-model RL → WMPO/VLAW → policy-utility objective.

- 취약 조건 점검: 연구자 점검: simulator budget과 world-model 학습 compute를 모두 비교해야 한다.
- 반증 가능한 질문: Policy가 독립적으로 바뀐 뒤 world-model utility에 대한 기존 선택이 얼마나 유지되는가?
- 최소 비교 제안: 연구자 예비 질문: 고정 imagined budget에서 서로 다른 policy에 대한 실제 update utility 순위를 비교한다. 새 채택 주제가 아니다.

이 비교는 연구자 제안이며 논문이 이미 수행한 실험이나 새 기여의 입증이 아니다. 현재 evidence maturity는 `CURATION-HYPOTHESIS`다.
