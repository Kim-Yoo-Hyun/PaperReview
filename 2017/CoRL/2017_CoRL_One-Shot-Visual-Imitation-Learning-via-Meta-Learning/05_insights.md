# Insights - One-Shot Visual Imitation Learning via Meta-Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> 2026-11-20 게재본의 표제면·방법·평가 절 대조. [게재 정보](https://proceedings.mlr.press/v78/finn17a.html) · [원문](https://proceedings.mlr.press/v78/finn17a/finn17a.pdf)

## Paper-supported conclusion

서로 다른 과제의 시연으로 정책의 초기 파라미터를 메타학습해, 보지 못한 과제의 시각 시연 하나로 정책을 적응시킨다. 훈련과 테스트는 논문에서 정의한 과제 분포를 공유한다. 임의의 새 기술에 대한 한 번의 시연 성공을 보장하지 않는다.

## Researcher interpretation

동일한 메타훈련 물체 분할에서 테스트 시연 수와 목표 영상만 제공하는 조건을 통제하면, 파라미터 적응과 목표 식별의 기여를 구분할 수 있다.
