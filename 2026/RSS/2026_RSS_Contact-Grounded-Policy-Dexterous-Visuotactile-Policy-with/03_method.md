# Method — Contact-Grounded Policy: Dexterous Visuotactile Policy with Generative Contact Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-19 · 서지·초록과 링크한 방법·비교 절을 확인했다. 논문 전체 정독과 실험 재현은 미확인이다.

## 관측과 출력

확산 모델로 로봇 상태와 촉각 궤적을 함께 예측한다.

## 학습·실행 방법

확산 모델로 로봇 상태와 촉각 궤적을 함께 예측한다. 예측을 제어 목표에 대응시켜 실물·시뮬레이션 손에서 평가한다.

- Diffusion Policy [4]의 조건부 U-Net에 미래 로봇 상태와 촉각의 공동 예측을 적용한다. 구현 및 p.6 비교표. [pr-0019 · 원문](https://roboticsproceedings.org/rss22/p005.pdf#page=5)
