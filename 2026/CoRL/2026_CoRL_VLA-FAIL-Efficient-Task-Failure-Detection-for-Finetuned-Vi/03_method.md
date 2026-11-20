# Method — VLA-FAIL: Efficient Task Failure Detection for Finetuned Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## 관측과 출력

계산 비용이 큰 반복 행동 표집을 줄이는 실패 신호를 검토한다.

## 학습·실행 방법

계산 비용이 큰 반복 행동 표집을 줄이는 실패 신호를 검토한다. 서로 다른 실패 양상을 포착하는 신호의 결합을 평가한다.

- SAFE의 실패 궤적 의존성을 명시하고 실패 예시 없이 학습하는 감지기와 대조한다. §2 Related Work. [pr-0696 · 원문](https://arxiv.org/pdf/2606.21386#page=2)
