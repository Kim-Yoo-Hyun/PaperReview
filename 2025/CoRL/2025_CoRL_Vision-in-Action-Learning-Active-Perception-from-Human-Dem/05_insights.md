# Insights — Vision in Action: Learning Active Perception from Human Demonstrations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## Paper-supported conclusion

가동형 로봇 목과 공유 관측을 제공하는 원격조작 인터페이스를 설계한다. 가림이 발생하는 다단계 조작에서 능동 관측을 평가한다. [원문 및 평가 절](https://raw.githubusercontent.com/mlresearch/v305/main/assets/xiong25a/xiong25a.pdf#page=7)

## Researcher interpretation

카메라 움직임을 학습한 양팔 정책과 고정 카메라 정책을 실물에서 비교한 능동 인식의 직접 선행이다.

- Diffusion Policy [12]로 능동 카메라와 양팔 동작을 시연에서 학습한다. Visuomotor policy. [pr-0019 · 원문](https://raw.githubusercontent.com/mlresearch/v305/main/assets/xiong25a/xiong25a.pdf#page=5)

## 최소 비교 실험

동일한 카메라·시연 예산에서 관측을 위해 움직인 직후의 조작 성공을 비교한다.
