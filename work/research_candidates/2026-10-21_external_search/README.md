# 외부 문헌에서 다시 탐색한 VLA + RL 연구 후보

- 조사일: 2026-10-21 KST
- 범위: 2024–2026의 Robotics/RL 주요 학회·저널, 최신 직접 충돌 preprint
- 단계: 최초 후보 선별 이후 **[C4](../2026-10-21_c4_reward_audit/README.md), [C5](../2026-10-21_c5_reset_audit/README.md), [C6 buildup 심사 완료](../2026-10-21_c6_checkpoint_audit/README.md)**. 아래 최초 탐색 근거와 구분한다.
- 최신 판정: C4/C5 보류 유지. 사용자 요청으로 C6까지 검토했으나 기존 selection·순차 검정과 충돌하고 VLA RL 이력/독립 outcome 연결이 부족해 **독립 신규 방법 채택 NO-GO**다. 평가 protocol은 후속 연구에 재사용한다.

## 이번 탐색의 결론

최초 탐색에서는 **VLA가 생성한 경험으로 보상 모델을 보정할 때, 어떤 데이터를 골라야 실제 RL 개선으로 이어지는가**를 우선 검토하도록 제안했다. 후속 C4 buildup에서는 high-reward audit와 policy-aware acquisition도 기존 기여임을 확인했다. 문제의 중요성과 새로운 논문으로의 채택을 구분한다.

| 순서 | 후보 | 남길 질문 | 현재 판단 |
|---|---|---|---|
| 1 | **C4. 정책 개선에 필요한 보상 오류의 선택적 보정** | 동일한 검수 예산에서, 현재 정책이 반복해서 이용하는 보상 오류를 고치는 것이 정적 정확도·불확실성 중심 보정보다 실제 성공률을 더 높이는가? | [Buildup 결과](../2026-10-21_c4_reward_audit/README.md): 현재 method NO-GO, 진단 연구 보류. 정책 효과 미측정 |
| 2 | **C5. 자동 reset의 편향 아래에서 학습 범위 유지** | 자율 reset이 쉬운 장면만 되돌려 줄 때, VLA RL의 개선은 고정된 목표 장면 분포에서도 유지되는가? 같은 reset 비용으로 coverage를 유지할 수 있는가? | [Buildup 결과](../2026-10-21_c5_reset_audit/README.md): 일반 방법 주장 NO-GO, 현상 진단 조건부 보류. 본격 학습 우선순위 하향 |
| 3 | **C6. RL checkpoint 선택의 평가 오류** | rollout 예산이 작을 때, 평가 모델이 선호하는 checkpoint와 독립적인 실제 성공률이 가장 높은 checkpoint의 불일치를 줄일 수 있는가? | [Buildup 결과](../2026-10-21_c6_checkpoint_audit/README.md): 독립 신규 방법 채택 NO-GO. 평가 protocol 재사용 |

세 후보의 비교군·반증 조건·입력 경계는 [CANDIDATES.md](./CANDIDATES.md), 공식 출처와 확인한 본문 위치는 [LITERATURE.md](./LITERATURE.md)에 있다. [SEARCH_AUDIT.json](./SEARCH_AUDIT.json)은 외부 문헌 identity와 확인 범위를 기록한다.

**연구 가치와 신규성을 구분한다.** 보상 오류, reset 비용, 평가 비용은 실제 로봇 학습에 중요하다. 그러나 이를 중요하다고 설명하는 것만으로 새 논문이 되지는 않는다. 이번 검토는 후속 검증의 우선순위를 정했으며, top-tier 논문으로 발전시킬 가치가 입증되었다고 판정하지 않는다.

## 외부 문헌이 바꾼 판단

- [Robometer, RSS 2026](https://www.roboticsproceedings.org/rss22/p140.html)는 실패 데이터와 preference supervision뿐 아니라 실제 VLA 기반 online RL까지 다룬다. 따라서 “실패 데이터를 더 넣자”는 C4의 새 기여가 아니다.
- [PROGRESSOR, ICCV 2025](https://openaccess.thecvf.com/content/ICCV2025/html/Ayalew_PROGRESSOR_A_Perceptually_Guided_Reward_Estimator_with_Self-Supervised_Online_Refinement_ICCV_2025_paper.html)는 online reward refinement를 이미 수행한다. C4는 이 baseline보다 필요한 것이 있는지 먼저 보여야 한다.
- [AutoEval, CoRL 2025](https://proceedings.mlr.press/v305/zhou25a.html)는 자동 reset과 성공 판정으로 평가를 자동화했다. C5는 자동 reset 시스템을 새로 제안하는 방향이 아니다.
- [Active Experiment Selection, CoRL 2025](https://proceedings.mlr.press/v305/anwar25a.html)은 제한된 비용으로 policy–task 평가를 고르는 문제를 이미 다룬다. C6는 “평가를 적게 한다”는 이유만으로 채택할 수 없다.

총 **21개 외부 비교 문헌**을 기록했다. 이 중 **15개는 공식 학회·저널 출판을 확인**했고, 6개는 arXiv로 기록하여 acceptance를 추정하지 않았다. 주요 후보와 직접 충돌하는 문헌은 관련 method/evaluation 본문까지 확인했으며, 모든 논문을 전체 정독했다는 의미는 아니다. 정규화 title·식별자 대조에서 이 21편의 registry entry는 발견되지 않았다. 이는 admission 목록이 아니므로 이번에 일괄 등록하거나 tier를 바꾸지 않았다.

## C4 최초 gate의 후속 처리

1. **완료:** PROGRESSOR·UPS·IJRR의 관련 본문/공개 code 대조, acquisition 계보 7편 추가 검토. [문헌 결론](../2026-10-21_c4_reward_audit/LITERATURE_REVIEW.md)
2. **완료:** Docker에서 RBM OOD와 RoboReward의 실제 metadata payload 20개 파싱. 성공·실패 label은 있으나 확인한 release에 policy update chronology와 당시 reward version이 없어 closed-loop 진단 전제는 미충족이다.
3. **판정:** 넓은 새 selector 주장은 채택하지 않는다. Native VLA에서 기존 검수법의 적용 조건을 비교하는 질문만 보류 상태로 남긴다.
4. **미착수:** Native VLA/reward inference·RL·robot rollout. [재개 계약](../2026-10-21_c4_reward_audit/DIAGNOSTIC_PROTOCOL.md)의 identity/headroom gate가 먼저다.

대형 VLA와 reward model의 동시 학습 실행 경로는 여전히 미검증이다. 최초 외부 탐색은 문헌 작업이었고, 후속 C4에서 metadata 검사를 Docker로 수행했다. 이후 C5에서는 별도의 [문헌·code·AutoEval payload 감사](../2026-10-21_c5_reset_audit/README.md)를 완료했다. 각 작업의 실행 범위를 구분하며 host dependency 설치는 없다.

## 이전 주제와의 관계

[C1/C2](../2026-10-20_vla_rl/README.md), [C3](../2026-10-21_execution_interface/README.md), [로봇 간 전이 결과](../../experiments/vla_rl_cross_embodiment/RESULTS.md)는 기존 판단을 유지한다. C4는 관측 행동을 고르는 C1이나 수행 방식의 조합 일반화 C2를 재개하지 않는다. C5도 이전 실패 시 retry/reset selector를 재개하는 것이 아니라 **학습 데이터의 시작 분포와 장기 coverage**를 묻는다. 로봇별 검증을 넓힐 수는 있지만 cross-embodiment policy transfer를 다시 primary claim으로 삼지 않는다.
