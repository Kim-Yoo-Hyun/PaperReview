# Method — KineDex: Learning Tactile-Informed Visuomotor Policies via Kinesthetic Teaching for Dexterous Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## 관측과 출력

직접 교시 중 시각·촉각·접촉력에 대응하는 행동을 수집한다.

## 학습·실행 방법

직접 교시 중 시각·촉각·접촉력에 대응하는 행동을 수집한다. 확산 정책이 자세와 힘 명령을 예측해 접촉 조작을 실행한다.

- 촉각과 고유수용감각을 조건으로 하는 Diffusion Policy [44]가 힘을 포함한 목표 행동을 예측한다. Policy learning. [pr-0019 · 원문](https://raw.githubusercontent.com/mlresearch/v305/main/assets/zhang25l/zhang25l.pdf#page=5)
