# C1 — 고정 VLA에서 추가 관측의 순이득을 선택하기

- 요약일: 2026-10-22. **HOLD; 본격 rollout/학습 보류.**
- 질문: 지금 조작하는 것보다 한 번 더 관측하는 것이 이로운 상태를 구분할 수 있는가? One-step predictor·visibility heuristic 이후에도 순차 RL이 필요한가?

## 실제 진행과 결과

ActiveAlign·EyeRobot 2.0·RESCUE 등과 충돌을 검토하고 frozen native VLA의 선택적 관측 질문으로 좁혔다. Docker bounded probe에서 SmolVLA checkpoint의 strict load와 243 actions의 실행을 확인했다. 시간 제한 안에 task competence를 확인하지 못했다. 이는 성공률 0% 측정이나 관측 전략의 실패 판정이 아니다.

Immediate/look/wait/heuristic branch, learned selector, RL 학습의 효과 비교는 실행하지 않았다. 정책이 과거 시각 관측을 자동 기억한다는 가정도 제거했다.

## GPU가 확보되면 가능한 최소 검증

호환 Docker runtime과 동일 native checkpoint/interface를 새로 검증한 뒤 clean-task competence를 충분한 episode로 확인할 수 있다. 이를 통과하면 물리적으로 가능한 관측 primitive를 고정하고 immediate 실행, look, 같은 시간의 wait, pose-matched 대조를 비교한다. 상태별 추가 관측 순이득이 양수/음수로 갈리는지부터 측정한다.

## GPU 외 한계와 중단 기준

Look은 이미지뿐 아니라 로봇 자세·시간·policy support를 바꿀 수 있다. 관측 품질 개선과 downstream 조작 이득은 별개다. 강한 단순 confidence/one-step 선택이나 aligned adaptation으로 충분하면 새 RL 방법은 중단한다. 관측 primitive·비용·정보 경계와 직접 선행 이후의 차별적 설명이 필요하다.

**현재 권고:** GPU는 기존 probe의 처리량 제한을 완화할 수 있지만 base competence·선택 가치·RL 필요성을 보장하지 않는다. 새 자격 근거 전까지 HOLD를 유지한다.

근거: [C1 후속 검토](../2026-10-20_vla_rl/C1_REVIEW.md), [진단 계약](../2026-10-20_vla_rl/C1_PROTOCOL.md), [실제 probe](../../experiments/vla_rl_active_handoff/RESULTS.md).

## Registry 연결 — 2026-10-22 등록

- [ActiveAlign](../../../2026/arXiv/2026_arXiv_Look-Before-You-Act-Bridging-Active-Perception-and-Vision/01_overview.md) — 2026 arXiv, `pr-1030`.
- [EyeRobot 2.0: Active Gaze for Precise Manipulation without Wrist Cameras](../../../2026/arXiv/2026_arXiv_EyeRobot-2.0-Active-Gaze-for-Precise-Manipulation-without/01_overview.md) — 2026 arXiv, `pr-1031`.
- [RESCUE: Is This Alarm Worth Acting On? Counterfactual Evaluation of VLA Runtime Monitors](../../../2026/arXiv/2026_arXiv_RESCUE-Is-This-Alarm-Worth-Acting-On-Counterfactual-Evalua/01_overview.md) — 2026 arXiv, `pr-1032`.

발표 status와 신규 5개 note의 근거는 각 overview를 따른다. 이전 buildup의 정독/코드 감사와 이번 abstract 기반 등록의 범위를 합치지 않는다.
