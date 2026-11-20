# Problem - One-Shot Visual Imitation Learning via Meta-Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> 2026-11-20 게재본의 표제면·방법·평가 절 대조. [게재 정보](https://proceedings.mlr.press/v78/finn17a.html) · [원문](https://proceedings.mlr.press/v78/finn17a/finn17a.pdf)

## 문제와 가정

새 물체와 목표마다 많은 시연을 다시 수집해야 하는 시각 모방학습의 비용을 다룬다. 초록·§1.

## 정책과 제어에서의 위치

서로 다른 과제의 시연으로 정책의 초기 파라미터를 메타학습해, 보지 못한 과제의 시각 시연 하나로 정책을 적응시킨다.
