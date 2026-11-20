# Evaluation — Back to the Familiar Future: Failure Recovery for VLA Policies via Pre-Imagined Milestone Selection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## 평가 조건

기본 LIBERO와 실패 주입 LIBERO를 구분했다. 주입 시점에 맞춘 복구 수치는 독립적인 실패 감지 성능을 포함하지 않는다. [원문 및 평가 절](https://arxiv.org/pdf/2606.09258#page=6)

## 해석할 때 확인할 조건

감지 시점의 지연을 고정하고 이정표 선택과 단순 재계획을 비교한다.

## 저자가 밝힌 한계

의미를 잘못 이해했거나 되돌릴 수 없는 상태에 도달한 실패는 복구 범위 밖이다. [원문](https://arxiv.org/pdf/2606.09258#page=9)
