# One-Shot Visual Imitation Learning via Meta-Learning

> Evidence maturity: `FULL_TEXT_CHECKED`.
> 2026-11-20 게재본의 표제면·방법·평가 절 대조. [게재 정보](https://proceedings.mlr.press/v78/finn17a.html) · [원문](https://proceedings.mlr.press/v78/finn17a/finn17a.pdf)

- Year/Venue: 2017 / CoRL
- Authors: Chelsea Finn, Tianhe Yu, Tianhao Zhang, Pieter Abbeel, Sergey Levine
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, Imitation Learning, meta-learning, visual manipulation
- Official paper: https://proceedings.mlr.press/v78/finn17a.html
- Code/Project: https://sites.google.com/view/one-shot-imitation
- Code: https://github.com/tianheyu927/mil

## Why This Paper Is Here

서로 다른 과제의 시연으로 정책의 초기 파라미터를 메타학습해, 보지 못한 과제의 시각 시연 하나로 정책을 적응시킨다.

## Main Claims and Actual Contribution

- 각 훈련 과제에서 시연 하나를 이용한 기울기 갱신 뒤 다른 시연의 행동을 예측하는 손실을 줄인다. 테스트에서는 새 과제의 시연으로 정책을 적응시킨 뒤 현재 관측에서 행동한다. §§3–5.
- 시뮬레이션에서는 목표에 손을 뻗거나 물체를 미는 과제를, 실제 PR2에서는 이미 쥔 물체를 시연으로 지정된 용기에 두는 과제를 평가한다. 시연을 문맥으로 입력하는 순환 방식과 목표 영상 방식 등이 비교군이다. §6, 그림 3–5.

## Evaluation Scope

훈련과 테스트는 논문에서 정의한 과제 분포를 공유한다. 임의의 새 기술에 대한 한 번의 시연 성공을 보장하지 않는다.
