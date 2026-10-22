# C3 — 같은 실행 명령으로 모이는 action token의 RL 처리

- 요약일: 2026-10-22. **실제 checkpoint 진단 완료; 본격 학습 투자 비추천.**
- 질문: 여러 token이 같은 robot command가 될 때 tokenwise PPO와 실행 class 기준 처리가 실제 학습에 의미 있는 차이를 만드는가?

## 실제 진행과 결과

Native decoder에서 256 gripper token이 2개 실행 명령으로 모이는 경로를 확인했다. 합성 확률 재분배로 token clipping과 class clipping이 달라질 수 있음을 확인했지만 raw policy gradient가 일반적으로 편향됐다는 주장은 성립하지 않았다. Marginalization 원리는 CAPG/MPG에 이미 있다.

실제 7.54B SFT checkpoint의 16개 demonstration 관측, 3 forward batch를 검사했다. T=1.6에서 128 gripper slot 중 120개가 대표 두 token에 99.9% 이상 질량을 두었다. 전체 chunk의 조건부 head-score trace 감소는 0.4962%이고, 제거 trace의 99.622%가 마지막 gripper slot에 집중됐다. 실제 reward-weighted gradient나 성공률 개선율이 아니다. Rollout·training은 0회다.

## GPU가 확보되면 가능한 최소 검증

여러 task/checkpoint·temperature에서 같은 진단을 확장하고 마지막 slot의 training-label/padding 및 decoder 위치를 점검할 수 있다. 넓고 유의미한 현상이 확인된 경우에만 같은 action outcome·데이터·PPO 예산의 class-level 대조를 검토한다.

## GPU 외 한계

현재 효과가 작고 국소적이며 기존 이론과 중복된다. Autoregressive coupling이나 continuous force에서는 gripper와 같은 단순 동치 처리가 성립하지 않을 수 있다. Logit metric의 큰 부분비율을 전체 policy 효과로 확대하지 않는다.

**현재 권고:** GPU가 있어도 즉시 대규모 RL을 권하지 않는다. 먼저 마지막 slot 현상의 원인과 다른 checkpoint에서의 비중을 확인할 때만 후속 가치가 있다.

근거: [C3 판단](../2026-10-21_execution_interface/README.md), [mechanism 검사](../../experiments/vla_rl_c3_interface/RESULTS.md), [실제 checkpoint 결과](../../experiments/vla_rl_c3_logits/RESULTS.md).

## Registry 연결 — 2026-10-22 등록

- [CAPG](../../../2018/ICML/2018_ICML_Clipped-Action-Policy-Gradient/01_overview.md) — 2018 ICML, `pr-1036`.
- [MPG](../../../2019/ICLR/2019_ICLR_Marginal-Policy-Gradients-A-Unified-Family-of-Estimators-f/01_overview.md) — 2019 ICLR, `pr-1037`.

발표 status와 신규 5개 note의 근거는 각 overview를 따른다. 이전 buildup의 정독/코드 감사와 이번 abstract 기반 등록의 범위를 합치지 않는다.
