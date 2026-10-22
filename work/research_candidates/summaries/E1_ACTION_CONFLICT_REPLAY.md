# E1 — 로봇 간 행동 충돌 지표가 replay·기존 능력 보존에 유용한가

- 요약일: 2026-10-22. **REVISE / E1-R1 gate NOT_MET / E1-R2 WAITING_EVIDENCE.**
- 질문: 로봇마다 다른 command 표현을 정상 정렬한 뒤 실제 효과 정보가 action residual보다 retention과 replay 선택을 더 잘 설명하는가?

## 진행 내용과 핵심 결과

Memory Anchors·MIR·물리 action 정렬·heterogeneity 분리 선행을 대조했다. 단순 effect-space 가중 잔차는 기존 가중 metric과 동치일 수 있고 동일 잔차가 반대 old-loss 변화를 만들 수도 있다. 실행하지 않은 action의 실제 effect는 observation/label만으로 일반적으로 식별되지 않는다.

RH20T 공개 view key82,920개에서 UR5/WSG50·Franka의 공통 task ID59개와 push/place 후보를 확인했다. View 수는 독립 trial 수가 아니다. Converted episode82,894행과의 join·command/time/scene 연결은 미완료다. X-VLA-Pt의 두 로봇 pose-native output·시간 보간·mask/loss를 감사했지만 실제 effect/evaluator packet은 미확보다. 두 로봇이 pretraining에 있으므로 unseen embodiment가 아니다. 정책 실험0회다.

## GPU가 확보되면 가능한 최소 검증

한 coherent 두-로봇 task/model/controller packet이 갖춰지면 정상 frame·rotation·mask·normalizer·시간 정렬 이후의 action discrepancy와 held-out retention을 측정할 수 있다. 같은 parameter-sharing·data budget에서 균형 replay, MIR/AnchorER, prompt-only/frozen 대조를 시행한다.

## GPU 외 한계

공통 task ID는 같은 scene/goal/독립 trial pairing의 보증이 아니다. Pose 오차는 실제 접촉 효과가 아니며 inverse action adapter도 forward-effect oracle이 아니다. RoboInter VLM weight를 native VLA executor로 취급할 수 없다. Memory Anchors/SPACE의 release 경계와 exact baseline recipe가 남았다.

**현재 권고:** 정상 pose/time residual 이후의 추가 정보와 일관된 평가 packet 없이 새 replay 방법을 채택하지 않는다. GPU만으로 새로운 정보·신규성이 생기지 않는다.

근거: [최신 R1](../2026-10-22_e1_buildup/R1_REVIEW.md), [해석적 계약](../2026-10-22_e1_buildup/CLAIM_CONTRACT.md), [현재 evidence 요건](../2026-10-22_e1_buildup/R1_EVIDENCE_REQUIREMENTS.json).

## Registry 연결 — 2026-10-22 등록

- [Forget-Me-Not](../../../2026/ICML/2026_ICML_Pretrained-Vision-Language-Action-Models-are-Surprisingly/01_overview.md) — 2026 ICML, `pr-0991`.
- [Memory Anchors](../../../2026/CoRL/2026_CoRL_Memory-Anchors-for-Continual-Robot-Learning/01_overview.md) — 2026 CoRL, `pr-0995`.
- [Rethinking VLA Scaling](../../../2026/arXiv/2026_arXiv_Rethinking-Visual-Language-Action-Model-Scaling-Alignment/01_overview.md) — 2026 arXiv, `pr-0996`.
- [Real-world Continual VLA](../../../2026/arXiv/2026_arXiv_Can-Vision-Language-Action-Models-Learn-from-Real-World-Da/01_overview.md) — 2026 arXiv, `pr-0997`.
- [HiMoE-VLA: Hierarchical Mixture-of-Experts for Generalist Vision-Language-Action Policies](../../../2025/arXiv/2025_arXiv_HiMoE-VLA-Hierarchical-Mixture-of-Experts-for-Generalist-V/01_overview.md) — 2025 arXiv, `pr-0998`.
- [SPACE: Enabling Learning from Cross-Robot Data Toward Generalist Policies](../../../2026/arXiv/2026_arXiv_SPACE-Enabling-Learning-from-Cross-Robot-Data-Toward-Gener/01_overview.md) — 2026 arXiv, `pr-1000`.
- [MIR](../../../2019/NeurIPS/2019_NeurIPS_Online-Continual-Learning-with-Maximal-Interfered-Retrieva/01_overview.md) — 2019 NeurIPS, `pr-1017`.

발표 status와 신규 5개 note의 근거는 각 overview를 따른다. 이전 buildup의 정독/코드 감사와 이번 abstract 기반 등록의 범위를 합치지 않는다.
