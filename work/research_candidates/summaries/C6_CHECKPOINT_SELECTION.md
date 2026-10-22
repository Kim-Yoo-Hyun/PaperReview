# C6 — 제한된 평가로 VLA RL checkpoint를 선택하기

- 요약일: 2026-10-22. **독립 신규 방법 NO-GO; 평가 protocol 재사용.**
- 질문: 비슷한 평균 점수의 RL checkpoint들 중 배포 성능이 더 좋은 것을 적은 평가 비용으로 선택하고 나빠진 것을 배제할 수 있는가?

## 실제 진행과 결과

A-OPS·STEP·N-SCORE가 active selection·순차 비교·오류 제어를 이미 다룬다. World-model/offline ranking도 dWorldEval·RACE와 겹친다. RL checkpoint라는 적용 대상만으로 차별화하지 않는다.

문헌12편, 공식 repo8주소를 확인했다. 7개 repo의26개 text source를 고정했고 한 주소는404였다. RACE JSON의57개 checkpoint 집계 기록(VLA27·DP30)을 파싱했다. 개별 trial 순서·seed·초기 상태는 없으며 이를 가상 trial로 생성하지 않았다. 동일 VLA의 RL 이력×학습 evaluator×독립 outcome 연결을 확보하지 못했다. 정책 성능 실험은 없었다.

## GPU가 확보되면 가능한 최소 검증

Versioned checkpoint와 고정 task 분포·trial-level 결과가 확보되면 기존 STEP/N-SCORE 등을 적용할 수 있다. 같은 seed/reset을 사용한 독립 evaluator 비교와 inference 비용 측정도 가능하다. 이런 검증 장치는 다른 후보의 pilot에도 재사용할 수 있다.

## GPU 외 한계

순위 상관만으로 top checkpoint의 우수성을 보장하지 못한다. 집계 성공률은 순차 검정 자료가 아니다. 평가 자료를 보고 policy를 계속 수정하면 anytime-validity가 자동으로 전체 탐색을 보호하지 않는다. Reward exploitation을 주장하려면 reward 변경 개입과 독립 outcome이 필요하다.

**현재 권고:** 새 selector 개발보다 기존 통계적 검증을 활용한다. 독립 연구 재개에는 기존 방법으로도 남는 VLA/RL 고유 오류 조건이 필요하다.

근거: [C6 결과](../2026-10-21_c6_checkpoint_audit/README.md), [자료 감사](../2026-10-21_c6_checkpoint_audit/DATA_AND_CODE_REVIEW.md), [재개 계약](../2026-10-21_c6_checkpoint_audit/REOPEN_PROTOCOL.md).

## Registry 연결 — 2026-10-22 등록

- [AOPS](../../../2021/NeurIPS/2021_NeurIPS_Active-Offline-Policy-Selection/01_overview.md) — 2021 NeurIPS, `pr-1026`.
- [STEP](../../../2025/RSS/2025_RSS_Is-Your-Imitation-Learning-Policy-Better-than-Mine-Policy/01_overview.md) — 2025 RSS, `pr-1027`.
- [NSCORE](../../../2026/RSS/2026_RSS_Beyond-Binary-Success-Sample-Efficient-and-Statistically-R/01_overview.md) — 2026 RSS, `pr-1028`.
- [Active Experiment Selection](../../../2025/CoRL/2025_CoRL_Efficient-Evaluation-of-Multi-Task-Robot-Policies-With-Act/01_overview.md) — 2025 CoRL, `pr-1029`.
- [AutoEval: Autonomous Evaluation of Generalist Robot Manipulation Policies in the Real World](../../../2025/CoRL/2025_CoRL_AutoEval-Autonomous-Evaluation-of-Generalist-Robot-Manipul/01_overview.md) — 2025 CoRL, `pr-1025`.

발표 status와 신규 5개 note의 근거는 각 overview를 따른다. 이전 buildup의 정독/코드 감사와 이번 abstract 기반 등록의 범위를 합치지 않는다.
