# D3 — 비가역 사건 이후 바뀐 지시의 가능성을 판단하기

- 요약일: 2026-10-22. **REVISE; D3-R1 gate NOT_MET / D3-R2 WAITING_EVIDENCE.**
- 질문: 조리·절단 같은 사건 이후 새 목표가 여전히 가능한지 판단하고 적절히 이어갈 수 있는가? Joint pose rollback과 세계 상태 복원을 구분한다.

## 진행 내용과 핵심 결과

SwitchVLA·Hi Robot·SafeLoop·VoLo와 충돌을 확인했다. 일반 interruption/replanning/rollback은 새 기여가 아니다. BEHAVIOR task45 cooking annotation200개와 raw file stem200개를 연결했으나 실제 event–RGB pair는 확보하지 못했다.

Task-ID model과 language-capable LL을 구분했고 후자의 stock server가 외부 지시를 읽지 않으며 원 goal/Q-score가 유지되는 경계를 확인했다. 추가 평가 P2에는 hotdog가 없고 turn-off0/3은 burner 대상이었다. 별도 P4도 조리 전 placement이며 post-event witness가 아니다. 정책 효과 실험은0회다.

## GPU가 확보되면 가능한 최소 검증

동일 instance의 사건 전후 관측·state timestamp와 language executor·변경 goal evaluator를 먼저 연결한다. Docker에서 pre-event feasible continuation과 post-event feasible/infeasible goal 대조를 실행할 수 있다. 동일 prefix/reset·queue 취소·시간 예산 아래 단순 predicate planner+같은 LL과 비교한다.

## GPU 외 한계

Data filename·annotation 끝점은 실제 사건 시점이 아니다. ‘Cooked’ label만으로 이미지에서 사건이 식별된다는 증거가 되지 않는다. Pre-event도 잔열 때문에 이미 불가능할 수 있어 feasible witness가 필요하다. 같은 object identity, 새 goal 평가, 기본 skill 능력과 정상 command 실행이 필수다. Kinematic qpos 변경·state restore를 physical rollback과 섞지 않는다.

**현재 권고:** event/관측 packet·continuation competence·matched 비교가 갖춰지기 전 adapter 구현이나 full-task 학습을 진행하지 않는다.

근거: [최신 R1](../2026-10-22_d3_buildup/R1_REVIEW.md), [task/policy 감사](../2026-10-22_d3_buildup/TASK_POLICY_AUDIT.md), [증거 요건](../2026-10-22_d3_buildup/R1_EVIDENCE_REQUIREMENTS.json).

## Registry 연결 — 2026-10-22 등록

- [SafeLoop: Risk-Aware Rollback for Vision-Language-Action Manipulation](../../../2026/arXiv/2026_arXiv_SafeLoop-Risk-Aware-Rollback-for-Vision-Language-Action-Ma/01_overview.md) — 2026 arXiv, `pr-1013`.
- [VoLo: A Physical Orchestrator for Open-Vocabulary Long-Horizon Manipulation](../../../2026/CoRL/2026_CoRL_VoLo-A-Physical-Orchestrator-for-Open-Vocabulary-Long-Hori/01_overview.md) — 2026 CoRL, `pr-1014`.
- [RSA](../../../2025/NeurIPS/2025_NeurIPS_Robust-and-Scalable-Autonomous-Reinforcement-Learning-in-I/01_overview.md) — 2025 NeurIPS, `pr-1015`.
- [RePlan-Bot: Multi-Level Replanning for Embodied Instruction Following](../../../2026/CVPR-Workshop/2026_CVPR-Workshop_RePlan-Bot-Multi-Level-Replanning-for-Embodied-Instruction/01_overview.md) — 2026 CVPR-Workshop, `pr-1016`.
- [RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents](../../../2026/CoRL/2026_CoRL_RoboFollow-Unveiling-the-Instruction-Following-Mirage-in-E/01_overview.md) — 2026 CoRL, `pr-1034`.

발표 status와 신규 5개 note의 근거는 각 overview를 따른다. 이전 buildup의 정독/코드 감사와 이번 abstract 기반 등록의 범위를 합치지 않는다.
