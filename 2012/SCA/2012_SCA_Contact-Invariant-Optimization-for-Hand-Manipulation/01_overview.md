# Contact-Invariant Optimization for Hand Manipulation

> Evidence maturity: `FULL_TEXT_CHECKED`.
> 2026-11-20 게재본의 표제면·방법·평가 절 대조. [게재 정보](https://diglib.eg.org/items/5e09458c-a0c5-4899-a46d-2a233b0f82bd) · [원문](https://diglib.eg.org/bitstreams/c5cbe554-57f8-4db0-b413-1bd8cc5cb9ce/download)

- Year/Venue: 2012 / SCA
- Authors: Igor Mordatch, Zoran Popović, Emanuel Todorov
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: REFERENCE
- Tags: Robotics, contact-rich manipulation, trajectory optimization, contact invariant
- Official paper: https://diglib.eg.org/items/5e09458c-a0c5-4899-a46d-2a233b0f82bd
- Code/Project: not identified

## Why This Paper Is Here

목표 물체의 움직임을 지정하면 손가락 접촉과 손의 궤적을 함께 최적화해 다양한 손 조작 동작을 합성한다.

## Main Claims and Actual Contribution

- 이동 동작용 contact-invariant optimization의 접촉 모델을 손과 물체 사이의 접촉에 맞게 확장한다. 접촉 보조변수와 움직임 궤적을 함께 최적화해 높은 자유도와 접촉 전환을 처리한다. pp. 2–5.
- 물체 집기, 손가락 사이에서 돌리기, 던지고 받기, 그리기 등 합성 동작을 비교한다. 세 손가락 손 모형과 두 손의 협력 사례도 제시한다. §7, pp. 6–7.

## Evaluation Scope

평가 대상은 시뮬레이션으로 합성한 손·물체 운동이다. 실물 촉각이나 실기 제어 성공률은 이 논문의 평가 범위 밖이다. §8.
