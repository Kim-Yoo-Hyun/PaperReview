# Insights — Efficient and Reliable Teleoperation through Real-to-Sim-to-Real Shared Autonomy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-20 · CoRL 공식 채택 목록에서 제목·포럼 ID·포스터 세션 2의 56번을 대조했다. 저자 원문 §III–V와 표 II, 온라인 수집기 및 공개 학습 자료를 확인했다.

## Paper-supported conclusion

소량의 실물 원격조작 시연으로 k-최근접 이웃 조작자 대리 모델을 만든다. 시뮬레이션에서 이 모델의 행동에 더할 잔차 정책을 강화학습으로 훈련한 뒤, 같은 보정 경로를 실물 조작자의 명령에 적용한다. [원문 및 평가 절](https://arxiv.org/html/2603.17016#S4.SS3)

## Researcher interpretation

사람과 RL 잔차 정책이 함께 모은 시연을 직접 원격조작과 비교한 실물 조립 기준선이다. 공유 제어 시연의 학습 가치와 재수집 비용을 평가할 때 조회한다.

- §IV-C와 부록 A-D에서 Diffusion Policy를 하류 학습기로 사용해 보조·직접 시연의 품질을 비교한다. [pr-0019 · 원문](https://arxiv.org/html/2603.17016#S4.SS3)

## 최소 비교 실험

공개한 동일 시도 수의 기어 맞물림 학습본에서 시연 단위의 입력과 행동 필드를 수집기와 대조한다. 원래 입력이 공개된 시행이 확보되면 보조 전후 행동을 연결해 비교한다.
