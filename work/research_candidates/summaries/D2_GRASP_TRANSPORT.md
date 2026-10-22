# D2 — 이후 운반·배치까지 고려하는 VLA 파지와 계획

- 요약일: 2026-10-22. **넓은 방법 NO-GO / 구체적 native 진단 HOLD.**
- 질문: 같은 geometry·grasp 후보·계산 budget에서 VLA가 후속 transport/place의 수행 가능성을 고려하면 기존 planner·supervised outcome ranking 이후의 이득이 남는가?

## 진행 내용과 핵심 결과

문헌10편과 공개 source를 비교했다. ReKep은 grasped-object collision geometry를 이미 고려한다. Cooperative Grasping은 운반 가능한 grasp를 학습하고 WBAG/CarryOn은 attached geometry와 VLA shield를 다룬다. GTP-FA의 grasp/execution attribution, Foresight Residual RL의 downstream phase도 직접 충돌이다.

Known geometry에서 다음 운반을 생각한다는 넓은 주장만으로는 차별화되지 않았다. 추가 MoManipVLA 후보 repo는 README/그림 수준이어서 native 비교 자격을 확보하지 못했다. Policy inference·simulation·RL은 실행하지 않았다.

## GPU가 확보되면 가능한 최소 검증

하나의 task–native executor–checkpoint가 연결되면 clean competence와 grasp 후보 이후의 transport/place 성공을 측정할 수 있다. 같은 perception·planner budget에서 native VLA, 기하 planner, 단순 supervised outcome ranker를 비교하고, attachment/goal이 달라져 선택이 갈리는 조건을 확인한다.

## GPU 외 한계

Finite-budget planner가 실패했다는 사실은 물리적으로 불가능하다는 label이 아니다. Privileged geometry·후속 rollout·candidate 수가 다르면 공정 비교가 아니다. Grasp/execution attribution의 독립성, 실제 observation cue, collision checker의 coverage와 attachment transition이 필요하다. Hardware 실행과 simulator 포팅도 동일한 baseline이 아니다.

**현재 권고:** 구체적 공개 task/executor와 기존 대안 이후의 차별적 예측을 확보하기 전 큰 학습·새 환경 이식을 하지 않는다.

근거: [D2 결과](../2026-10-22_d2_buildup/README.md), [직접 선행](../2026-10-22_d2_buildup/CLOSEST_WORK.md), [비교 계약](../2026-10-22_d2_buildup/CLAIM_CONTRACT.md).

## Registry 연결 — 2026-10-22 등록

- [Cooperative Grasping for Collective Object Transport in Constrained Environments](../../../2026/RA-L/2026_RA-L_Cooperative-Grasping-for-Collective-Object-Transport-in-Co/01_overview.md) — 2026 RA-L, `pr-1007`.
- [G3F](../../../2025/RA-L/2025_RA-L_Globally-Guided-Geometric-Fabrics-for-Reactive-Mobile-Mani/01_overview.md) — 2025 RA-L, `pr-1008`.
- [WBAG: A Whole-Body and Attached-Geometry Safety Framework for Vision-Language-Action Manipulation](../../../2026/arXiv/2026_arXiv_WBAG-A-Whole-Body-and-Attached-Geometry-Safety-Framework-f/01_overview.md) — 2026 arXiv, `pr-1009`.
- [CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance](../../../2026/arXiv/2026_arXiv_CarryOn-A-Dual-Loop-Harness-for-Personalized-and-Reliable/01_overview.md) — 2026 arXiv, `pr-1010`.
- [GTP-FA](../../../2026/NeurIPS/2026_NeurIPS_Grasp-Then-Plan-with-Failure-Attribution-A-Closed-Two-Stag/01_overview.md) — 2026 NeurIPS, `pr-1011`.
- [Foresight Residual RL for Long-Horizon Robot Manipulation with Vision-Language-Action Models](../../../2026/arXiv/2026_arXiv_Foresight-Residual-RL-for-Long-Horizon-Robot-Manipulation/01_overview.md) — 2026 arXiv, `pr-1012`.

발표 status와 신규 5개 note의 근거는 각 overview를 따른다. 이전 buildup의 정독/코드 감사와 이번 abstract 기반 등록의 범위를 합치지 않는다.
