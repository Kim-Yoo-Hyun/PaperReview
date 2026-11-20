# Method — Efficient and Reliable Teleoperation through Real-to-Sim-to-Real Shared Autonomy

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-20 · CoRL 공식 채택 목록에서 제목·포럼 ID·포스터 세션 2의 56번을 대조했다. 저자 원문 §III–V와 표 II, 온라인 수집기 및 공개 학습 자료를 확인했다.

## 관측과 출력

실물에서 GELLO가 제공하는 손끝 목표와 그리퍼 명령, 추정한 부품·손끝 상태가 제어 입력이다. 학습한 잔차와 순응 제어로 관절 명령을 만든다. 저자의 온라인 수집기는 기본 목표와 보정 목표를 각각 기록한다.

## 학습·실행 방법

소량의 실물 원격조작 시연으로 k-최근접 이웃 조작자 대리 모델을 만든다. 시뮬레이션에서 이 모델의 행동에 더할 잔차 정책을 강화학습으로 훈련한 뒤, 같은 보정 경로를 실물 조작자의 명령에 적용한다.

- §IV-C와 부록 A-D에서 Diffusion Policy를 하류 학습기로 사용해 보조·직접 시연의 품질을 비교한다. [pr-0019 · 원문](https://arxiv.org/html/2603.17016#S4.SS3)
