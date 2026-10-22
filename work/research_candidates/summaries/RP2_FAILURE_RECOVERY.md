# RP-2 — 같은 실패 시점에서 복구 행동을 선택하기

- 요약일: 2026-10-22. **RETIRED historical overlay.** 아래는 과거 설계의 요약이며 재개 승인·현재 실험 계획이 아니다.
- 질문: 같은 failure onset에서 continue/retry/reobserve/reset/abort의 결과·위험·비용을 비교해 학습한 selector가 best-fixed·단순 heuristic보다 유용한가?

## 진행 내용과 핵심 판단

Frozen VLA·동일 detector·고정 option library 위에서 all-option branch supervision과 held-out selection을 설계했다. Agentic RL, ActFovea, ProbeAct, CoRe 등과의 직접 충돌 때문에 high-level recovery manager 자체를 기여에서 제외했다. 후속 RESCUE도 counterfactual intervention과 비용 평가의 강한 대안이다.

보존 문서는 계획과 문헌 비교다. 그 안의 onset sweep·regret·성공률 목표를 실제로 얻은 결과로 읽지 않는다. Selector 효과가 입증된 기록은 없다.

## GPU가 확보되면 가능한 최소 검증

별도 재개 결정과 native policy 자격이 있을 때 동일 env/policy/controller 상태를 분기해 각 applicable option을 실행할 수 있다. 먼저 branch equivalence와 기본 능력을 확인하고, option ranking이 onset·예산에 따라 실제로 교차하는지 검사한다. Best-fixed gap이 없으면 learned selector를 학습하지 않는다.

## GPU 외 한계

Failure onset의 selection bias, reset이 복원해야 하는 controller/policy memory, option별 추가 관측·human assistance·로봇 시간의 비용이 핵심이다. Privileged oracle outcome을 배포 입력으로 넣으면 안 된다. 물리 reset과 simulator state restore도 다르다. Broad method novelty는 이미 약하며 simulator 결과가 physical safety 보장은 아니다.

**현재 권고:** RETIRED 유지. GPU만으로 대형 recovery RL을 시작하지 않는다. 재개 시 기존 strong execution manager 이후의 추가 decision value를 먼저 보여야 한다.

근거: [보존된 RP-2](../../../research/projects/RP-2_FAILURE_RECOVERY.md), [C1/C2 탐색의 제외 사유](../2026-10-20_vla_rl/README.md). 과거 문서의 ‘현재’는 작성 당시를 뜻한다.

## Registry 연결 — 2026-10-22 등록

- [RESCUE: Is This Alarm Worth Acting On? Counterfactual Evaluation of VLA Runtime Monitors](../../../2026/arXiv/2026_arXiv_RESCUE-Is-This-Alarm-Worth-Acting-On-Counterfactual-Evalua/01_overview.md) — 2026 arXiv, `pr-1032`.
- [SafeLoop: Risk-Aware Rollback for Vision-Language-Action Manipulation](../../../2026/arXiv/2026_arXiv_SafeLoop-Risk-Aware-Rollback-for-Vision-Language-Action-Ma/01_overview.md) — 2026 arXiv, `pr-1013`.

발표 status와 신규 5개 note의 근거는 각 overview를 따른다. 이전 buildup의 정독/코드 감사와 이번 abstract 기반 등록의 범위를 합치지 않는다.
