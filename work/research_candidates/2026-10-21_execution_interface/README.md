# C3 빌드업: 실행 행동의 동치성과 VLA RL

- Updated: **2026-10-21 KST**
- 판정: **실제 checkpoint 진단 완료. 현재 C3의 본격 학습/방법 논문 투자는 권하지 않으며 우선순위를 낮춘다. 마지막 slot의 국소적 현상은 진단 결과로 보존한다.**
- [문헌·직접 충돌](./LITERATURE.md) · [초기 mechanism 계약](./PROTOCOL.md) · [이전 mechanism 검사](../../experiments/vla_rl_c3_interface/RESULTS.md) · [실제 logits 계약](./LOGITS_PROTOCOL.md) · [최신 실제 checkpoint 결과](../../experiments/vla_rl_c3_logits/RESULTS.md)
- 이전 [C1/C2](../2026-10-20_vla_rl/README.md)의 재개가 아니다. 여러 robot의 행동 interface라는 관심축을 유지하면서 질문을 바꿨다.

## 연구 질문

**같은 로봇 명령으로 실행되는 여러 action token을 서로 다른 행동처럼 RL 업데이트하는 것이 실제 학습 효율을 낮추는가? 그 영향은 gripper·controller interface에 따라 어떻게 달라지는가?**

예를 들어 서로 다른 token이 모두 “gripper 닫기”로 변환된다면, 그 token들 사이의 확률 이동은 실제 로봇 동작을 바꾸지 않을 수 있다. 그럼에도 tokenwise PPO clipping은 달라질 수 있다. C3는 observation 선택이나 instruction 제약이 아닌 **policy output → execution transform → RL objective** 연결을 다룬다.

수학적으로 decoder를 `u=T(a)`라 하면 실행 명령의 확률은 `p(u|o)=Σ[a:T(a)=u] π(a|o)`다. 이 합을 사용하는 원리와 gradient 분산 감소는 [CAPG](https://proceedings.mlr.press/v80/fujita18a.html)·[MPG](https://arxiv.org/html/1806.05134v3)에 이미 있다. C3의 가능한 기여는 원리의 발명이 아니라, **현대 VLA에서 효과가 남는 조건을 측정하고 기존 강한 baseline으로 설명되지 않는 문제를 찾는 것**이다.

## 검증 결과

| 질문 | 확인 결과 | evidence 한계 |
|---|---|---|
| Native 공개 경로에 행동 동치가 존재하는가? | SimpleVLA-RL의 256개 token이 gripper 명령 2개로 모임 | 특정 LIBERO decoder/metadata 경로; 모든 VLA에 대한 주장 아님 |
| 실제 명령 확률이 같아도 clipping이 달라지는가? | 내부 ±60% 확률 재분배에서 token clip 49.61%, class clip 0 | 구성한 확률 분포를 native loss에 넣은 검사; 실제 정책의 빈도 아님 |
| Raw PG 자체가 틀린가? | 기대 gradient는 일치. 문제를 일반적인 bias로 주장할 수 없음 | 한 decision, return이 실행 class에만 의존하는 조건 |
| Marginalization이 항상 큰 이득인가? | Synthetic 집중분포에서는 이득이 줄어듦. 실제 T=1.6에서는 128개 gripper slot 중 120개가 대표 두 token에 ≥99.9% 확률을 둠 | 한 SFT checkpoint의 16개 demonstration 관측 |
| 실제 checkpoint에서 영향이 넓게 나타나는가? | 전체 chunk의 조건부 head score trace 감소 0.4435%(T=1), 0.4962%(T=1.6) | 실제 reward-weighted gradient·성공률의 개선율이나 상한이 아님 |
| 예외는 있는가? | T=1.6에서 제거되는 head score trace의 99.622%가 마지막 gripper slot에 집중 | 원본 위치/decoder 대조 통과; SFT label/padding 원인은 미확정 |
| 실제 manipulation 성공률이 개선되는가? | **미검증** | 실제 checkpoint forward 3 batch/16 관측 완료; rollout·training은 0회 |

이전 synthetic 검사에서 실제 7.54B parameter checkpoint의 forward까지 진행했다. 원 가중치 4 shard의 hash, 982 tensor의 key·shape, native action 위치, 마지막 head의 독립 autograd 검사를 통과했다. 학습 효과까지 검증했다고 해석하지 않는다.

## 연구적으로 발전시킬 가치

**재현 가능한 진단 결과의 가치는 있다. 현재 형태를 top-tier 방법 논문으로 밀어붙일 근거는 약하다.**

실제 분포에서도 같은 “닫기” 명령 내부의 확률 분산이 확인된 점은 유용하다. 다만 gripper만 집계한 head score 감소 84.65%(T=1.6)를 전체 policy 효과로 확대하면 과장이다. 전체 chunk에서는 0.4962%이며, 마지막 slot을 제외한 일곱 gripper만 처리하면 0.001874%다. 해당 상대 비중은 actual advantage가 없는 조건부 score metric이다.

본격 채택을 보류하는 이유는 기존 CAPG/MPG 원리와의 중복, 실제 signal의 마지막 slot 집중, 좁은 checkpoint·표본 범위, policy 효과 미측정이다. 작은 score 비중만으로 드문 contact failure에서의 이득까지 부정하지는 않는다. 하지만 그 가능성만으로 큰 학습을 시작할 근거도 충분하지 않다. Binary head/기존 MPG로 설명되는 개선만 남으면 새 method contribution이 아니다.

최신 [ManiPhysicsBench](https://arxiv.org/html/2610.02802)는 연속 grip을 직접 실행하는 조건을 다룬다. 이처럼 force/closure 차이가 물리 결과를 바꾸는 interface에서는 token을 binary class로 합치면 안 된다. 따라서 여러 로봇을 다루려면 interface별 동치성의 성립 조건부터 확인해야 한다.

## 종료 범위와 재개 조건

1. **완료:** 실제 native logits 확보, 실제 분포의 집중도·조건부 head score covariance·counterfactual clipping 분석, 전체 chunk에서의 비중, 마지막 slot 사후 감사. [작은 evidence artifact](../../experiments/vla_rl_c3_logits/evidence/native_logits.npz)를 보존했다.
2. **현재 결정:** 본격 PPO/GRPO 학습과 multi-robot 확장은 진행하지 않는다. 현재 넓은 C3 formulation은 낮은 우선순위의 진단 결과로 정리한다.
3. **재개한다면 가장 먼저:** 마지막 slot의 SFT label/padding과 checkpoint 계보를 감사한다. Native decoder/position 일치만으로 training supervision까지 검증된 것은 아니다. 이 원인이 설명되기 전에는 새로운 algorithm gap으로 주장하지 않는다.
4. **다음 gate:** 다른 checkpoint와 실제 on-policy advantage에서도 의미 있는 효과가 남는지 확인한다. 그 뒤에만 native token PPO, 기존 MPG/class PPO, binary head, temperature/clip sweep을 matched budget으로 비교한다. Return-weighted imitation도 데이터 이득의 통제로 둔다.
5. **논문 채택 조건:** 서로 다른 task family·controller에서의 반복 가능한 성공/sample cost 개선과 강한 baseline을 넘는 설명이 필요하다. 현재 두 mug 관련 task를 두 task family 또는 여러 로봇으로 세지 않는다.

이번 후속 단계는 실제 checkpoint 분포 검증까지 완료했다. Actual advantage·old/new RL update·backbone gradient·정책 성능은 미측정으로 남긴다. Registry 974편과 tier·사용자 읽기 상태는 유지했다.
