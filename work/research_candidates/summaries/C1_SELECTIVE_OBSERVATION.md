# C1 — 고정 VLA에서 추가 관측의 순이득을 선택하기

- 갱신일: 2026-10-28. **C1-E1 문헌 비교 완료·탐색 질문 유지 / 본격 rollout·학습 HOLD.**
- 질문: 같은 frozen VLA에서 초기 관측만 사용하는 단순 규칙으로 추가 관측을 생략해 성공률을 허용 범위 안에서 유지하면서 동작·시간을 줄일 수 있는가? RL 필요성은 미정이다.

사용자 요청에 따른 [GAP-S3 재검토](../../update/VLA_EXPLORATION_REOPENING_2026-10-28.md) 후 [C1-E1](../../update/C1_OBSERVATION_COST_REVIEW_2026-10-28.md)에서 지정 3편의 실제 비교와 비용 단위를 대조했다. 물리 이동/가상 gaze, 정책 재학습/frozen 비교를 구분하고 immediate/always-look/초기 관측 gate의 작은 비교를 남겼다. 효과·신규성·독립 논문 가치는 미확인이다. 완성된 기제·RL 필요성·baseline 실패를 탐색 입장 조건으로 두지 않는다. [Canonical 탐색 카드](../../../synthesis/04_vla_generalist.md#gap-selective-observation-2026), 활성 후속 작업은 [TODO](../../../TODO.md)를 따른다.

## 실제 진행과 결과

ActiveAlign·EyeRobot 2.0·RESCUE 등과 충돌을 검토하고 frozen native VLA의 선택적 관측 질문으로 좁혔다. Docker bounded probe에서 SmolVLA checkpoint의 strict load와 243 actions의 실행을 확인했다. 시간 제한 안에 task competence를 확인하지 못했다. 이는 성공률 0% 측정이나 관측 전략의 실패 판정이 아니다.

Immediate/look/wait/heuristic branch, learned selector, RL 학습의 효과 비교는 실행하지 않았다. 정책이 과거 시각 관측을 자동 기억한다는 가정도 제거했다.

## GPU가 확보되면 가능한 최소 검증

호환 Docker runtime과 선택한 native checkpoint/interface를 검증한 뒤 clean-task competence와 물리 관측 primitive를 확인할 수 있다. 같은 정책의 immediate/always-look/초기 관측 gate를 비교하고 scene별 성공·전체 비용을 측정한다. Wait/pose-matched 대조는 원인을 구별할 때 추가한다. 양/음 교차를 미리 요구하지 않으며 항상 관측 또는 즉시 실행이 충분할 가능성도 평가한다. 과거 probe 설정은 현재 실행 계획으로 자동 재사용하지 않는다.

## GPU 외 한계와 중단 기준

Look은 이미지뿐 아니라 자세·시간·policy support를 바꿀 수 있다. 관측 품질과 조작 이득은 별개다. 단순 규칙이 충분하면 새 RL 방법은 만들지 않는다. Adapted 정책의 skip 능력도 가정하지 않으며 checkpoint를 섞어 선택 효과를 계산하지 않는다. Gate에는 look 후 정보를 누출하지 않고 성공 보존은 허용치·불확실성으로 판단한다. Endpoint 호환성만 남으면 HANDOFF와 통합한다.

**현재 권고:** [GAP-SELECT-E1](../../update/VLA_EXPLORATION_SELECTION_2026-10-28.md)에서 HANDOFF를 먼저 탐색하기로 해 C1은 **대안 후보로 유지**한다. 실제 선택 가치·단순 규칙의 충분성은 실험이 필요하며 C1의 부정 결과가 새로 생긴 것은 아니다. 같은 문헌을 반복해 이를 입증하려 하지 않는다. GPU만으로 competence나 효과가 보장되지 않으며 실제 비교의 실행 계약 전 rollout/학습 HOLD를 유지한다.

근거: [C1 후속 검토](../2026-10-20_vla_rl/C1_REVIEW.md), [진단 계약](../2026-10-20_vla_rl/C1_PROTOCOL.md), [실제 probe](../../experiments/vla_rl_active_handoff/RESULTS.md).

## Registry 연결 — 2026-10-22 등록

- [ActiveAlign](../../../2026/arXiv/2026_arXiv_Look-Before-You-Act-Bridging-Active-Perception-and-Vision/01_overview.md) — 2026 arXiv, `pr-1030`.
- [EyeRobot 2.0: Active Gaze for Precise Manipulation without Wrist Cameras](../../../2026/arXiv/2026_arXiv_EyeRobot-2.0-Active-Gaze-for-Precise-Manipulation-without/01_overview.md) — 2026 arXiv, `pr-1031`.
- [RESCUE: Is This Alarm Worth Acting On? Counterfactual Evaluation of VLA Runtime Monitors](../../../2026/arXiv/2026_arXiv_RESCUE-Is-This-Alarm-Worth-Acting-On-Counterfactual-Evalua/01_overview.md) — 2026 arXiv, `pr-1032`.

발표 status와 신규 5개 note의 근거는 각 overview를 따른다. 이전 buildup의 정독/코드 감사와 이번 abstract 기반 등록의 범위를 합치지 않는다.
