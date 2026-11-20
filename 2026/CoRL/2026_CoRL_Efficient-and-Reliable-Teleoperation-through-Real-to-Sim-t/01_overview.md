# Efficient and Reliable Teleoperation through Real-to-Sim-to-Real Shared Autonomy

> Evidence maturity: `FULL_TEXT_CHECKED`. 2026-11-20 · CoRL 공식 채택 목록에서 제목·포럼 ID·포스터 세션 2의 56번을 대조했다. 저자 원문 §III–V와 표 II, 온라인 수집기 및 공개 학습 자료를 확인했다.

- Year/Venue: 2026 / CoRL
- Authors: Shuo Sha, Yixuan Wang, Binghao Huang, Antonio Loquercio, Yunzhu Li
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: shared autonomy, teleoperation, residual policy, Reinforcement Learning, contact-rich manipulation
- Official paper: https://arxiv.org/abs/2603.17016
- Code/Project: https://residual-copilot.github.io/

## 연구 질문과 기여

접촉이 있는 정밀 조립에서 사람이 원격으로 지정하는 행동에 어떤 보정을 더하면 초심자의 실패가 줄고 후속 모방 정책이 사용할 시연의 품질이 높아지는가?

소량의 실물 원격조작 시연으로 k-최근접 이웃 조작자 대리 모델을 만든다. 시뮬레이션에서 이 모델의 행동에 더할 잔차 정책을 강화학습으로 훈련한 뒤, 같은 보정 경로를 실물 조작자의 명령에 적용한다.

## 평가 범위

§IV-A 및 부록 A-E는 xArm7으로 너트 나사 체결, 기어 맞물림, 핀 삽입을 수행한 참여자 16명의 결과를 보고한다. §IV-C 표 II의 기어 맞물림에서 같은 시도 수로 수집한 시연으로 학습한 Diffusion Policy의 삽입 성공은 보조 11/20, 직접 조작 1/20이다. 같은 성공 시연 수 비교에서는 각각 9/20, 0/20이다. [원문 및 평가 절](https://arxiv.org/html/2603.17016#S4.SS3)

## 선정 근거

사람과 RL 잔차 정책이 함께 모은 시연을 직접 원격조작과 비교한 실물 조립 기준선이다. 공유 제어 시연의 학습 가치와 재수집 비용을 평가할 때 조회한다.
