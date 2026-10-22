# C4 — 정책 개선에 유용한 보상 오류를 선택적으로 검수하기

- 요약일: 2026-10-22. **새 acquisition 방법 NO-GO / 진단 HOLD.**
- 질문: 같은 검수 비용에서 높은 reward를 받는 실패를 고치는 것이 uncertainty·policy-value 기반 기존 선택보다 독립 성공률을 개선하는가?

## 실제 진행과 결과

ReQueST의 high-reward false-positive query, IDRL의 policy-return 정보 이득, PROGRESSOR의 online correction과 직접 겹쳤다. ‘정책에 중요한 label을 고른다’는 동기는 새 방법이 아니다.

Docker에서 metadata payload 20개를 읽었다. Robometer OOD export는 18,261 frame/571 episode/41 task, 성공233·실패166·suboptimal172였다. 별도 legacy export와 합산하지 않았다. RoboReward는 54,135 row였지만 확인 필드만으로 policy checkpoint·RL round·당시 reward prediction을 연결할 수 없었다. Clip timestamp는 RL chronology가 아니다. VLA/reward inference·RL은 실행하지 않았다.

## GPU가 확보되면 가능한 최소 검증

Versioned native rollout이 확보되면 reward prediction과 독립 outcome을 비교하고 uniform/high-reward/uncertainty/policy-aware 검수의 오류 coverage를 볼 수 있다. Native competence와 oracle-reward headroom을 통과한 뒤 제한된 update에서 reward 보정과 정책 변화의 관계를 검증할 수 있다.

## GPU 외 한계

동일 policy update 전후의 checkpoint·reward version·독립 outcome 로그가 필요하다. 정적 영상 label만으로 반사실 RL 개선을 복원하지 못한다. Label 형태별 사람 시간·정보량이 다르며 정답 검토 설명을 acquisition 입력에 쓰면 leakage다. Termination도 reward가 바꾸면 rollout 길이가 교란된다.

**현재 권고:** 새 selector보다 일관된 chronology/independent-outcome packet 확보가 먼저다. 기존 방법 이후의 VLA 고유 현상이 없으면 독립 연구로 채택하지 않는다.

근거: [C4 결과](../2026-10-21_c4_reward_audit/README.md), [자료 감사](../2026-10-21_c4_reward_audit/DATA_AND_CODE_REVIEW.md), [진단 계약](../2026-10-21_c4_reward_audit/DIAGNOSTIC_PROTOCOL.md).

## Registry 연결 — 2026-10-22 등록

- [ReQueST](../../../2020/ICML/2020_ICML_Learning-Human-Objectives-by-Evaluating-Hypothetical-Behav/01_overview.md) — 2020 ICML, `pr-1018`.
- [IDRL](../../../2021/NeurIPS/2021_NeurIPS_Information-Directed-Reward-Learning-for-Reinforcement-Lea/01_overview.md) — 2021 NeurIPS, `pr-1019`.
- [PROGRESSOR: A Perceptually Guided Reward Estimator with Self-Supervised Online Refinement](../../../2025/ICCV/2025_ICCV_PROGRESSOR-A-Perceptually-Guided-Reward-Estimator-with-Sel/01_overview.md) — 2025 ICCV, `pr-1020`.
- [Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons](../../../2026/RSS/2026_RSS_Robometer-Scaling-General-Purpose-Robotic-Reward-Models-vi/01_overview.md) — 2026 RSS, `pr-1021`.
- [RoboReward: General-Purpose Vision-Language Reward Models for Robotics](../../../2026/arXiv/2026_arXiv_RoboReward-General-Purpose-Vision-Language-Reward-Models-f/01_overview.md) — 2026 arXiv, `pr-1022`.

발표 status와 신규 5개 note의 근거는 각 overview를 따른다. 이전 buildup의 정독/코드 감사와 이번 abstract 기반 등록의 범위를 합치지 않는다.
