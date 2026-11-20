# Insights — RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## Paper-supported conclusion

합성 데이터로 시각언어 행동 검증기를 학습한다. 후보 샘플링과 검증에 투입하는 추론 계산량의 효과를 평가한다. [원문 및 평가 절](https://raw.githubusercontent.com/mlresearch/v305/main/assets/kwok25a/kwok25a.pdf#page=7)

## Researcher interpretation

추가 학습 없이 행동 후보를 더 뽑는 효과와 학습한 검증기가 주는 이득을 분리할 기준이다.

- OpenVLA를 고정된 행동 후보 생성기로 사용하고 후보 검증·선택을 추가한다. Experiments, base model. [pr-0051 · 원문](https://raw.githubusercontent.com/mlresearch/v305/main/assets/kwok25a/kwok25a.pdf#page=6)

## 최소 비교 실험

후보 수와 추론 시간을 맞추고 검증기 선택과 다수결의 성공률을 비교한다.
