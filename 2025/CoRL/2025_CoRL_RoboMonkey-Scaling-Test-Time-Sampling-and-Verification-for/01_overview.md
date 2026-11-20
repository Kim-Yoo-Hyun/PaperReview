# RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

- Year/Venue: 2025 / CoRL
- Authors: Jacky Kwok, Christopher Agia, Rohan Sinha, Matt Foutter, Shulu Li, Ion Stoica, Azalia Mirhoseini, Marco Pavone
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, action verification, test-time sampling
- Official paper: https://proceedings.mlr.press/v305/kwok25a.html
- Code/Project: https://robomonkey-vla.github.io

## 연구 질문과 기여

VLA가 생성한 후보 행동을 검증해 실행할 행동을 선택한다.

합성 데이터로 시각언어 행동 검증기를 학습한다. 후보 샘플링과 검증에 투입하는 추론 계산량의 효과를 평가한다.

## 평가 범위

OpenVLA를 기본 정책으로 시뮬레이션과 실물 WidowX에서 표집 및 검증 방식을 비교했다. [원문 및 평가 절](https://raw.githubusercontent.com/mlresearch/v305/main/assets/kwok25a/kwok25a.pdf#page=7)

## 선정 근거

추가 학습 없이 행동 후보를 더 뽑는 효과와 학습한 검증기가 주는 이득을 분리할 기준이다.
