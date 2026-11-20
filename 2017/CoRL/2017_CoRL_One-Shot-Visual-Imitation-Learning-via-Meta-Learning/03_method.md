# Method - One-Shot Visual Imitation Learning via Meta-Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`.
> 2026-11-20 게재본의 표제면·방법·평가 절 대조. [게재 정보](https://proceedings.mlr.press/v78/finn17a.html) · [원문](https://proceedings.mlr.press/v78/finn17a/finn17a.pdf)

## 입력과 계산

각 훈련 과제에서 시연 하나를 이용한 기울기 갱신 뒤 다른 시연의 행동을 예측하는 손실을 줄인다. 테스트에서는 새 과제의 시연으로 정책을 적응시킨 뒤 현재 관측에서 행동한다. §§3–5.

## 적용 조건

훈련과 테스트는 논문에서 정의한 과제 분포를 공유한다. 임의의 새 기술에 대한 한 번의 시연 성공을 보장하지 않는다.
