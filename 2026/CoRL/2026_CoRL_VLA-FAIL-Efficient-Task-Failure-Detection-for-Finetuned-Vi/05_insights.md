# Insights — VLA-FAIL: Efficient Task Failure Detection for Finetuned Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## Paper-supported conclusion

계산 비용이 큰 반복 행동 표집을 줄이는 실패 신호를 검토한다. 서로 다른 실패 양상을 포착하는 신호의 결합을 평가한다. [원문 및 평가 절](https://arxiv.org/pdf/2606.21386#page=6)

## Researcher interpretation

실패 감지의 정확도와 알림 시간을 함께 평가하는 지표와 VLA용 감지 기준을 제공한다.

- SAFE의 실패 궤적 의존성을 명시하고 실패 예시 없이 학습하는 감지기와 대조한다. §2 Related Work. [pr-0696 · 원문](https://arxiv.org/pdf/2606.21386#page=2)

## 최소 비교 실험

같은 오경보 수준에서 성공 불가능 시점 이전에 확보한 개입 시간을 비교한다.
