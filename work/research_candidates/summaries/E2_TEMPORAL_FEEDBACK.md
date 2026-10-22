# E2 — 시간 표현·관측 갱신·제어기 효과를 분리하기

- 요약일: 2026-10-22. **일반 신규 방법 NO-GO / 진단 REVISE·HOLD; 주력 채택 보류.**
- 질문: VLA 실행 주기 변경의 이득은 시간 표현, fresh observation, 저수준 controller 중 어디에서 오며 통제 후 방법 선택의 결론이 달라지는가?

## 진행 내용과 핵심 결과

RTC·SAIL·RTR·AAC 등 공식 proceedings4편과 직접 preprint5편을 비교했다. Continuous trajectory, adaptive horizon, 매 관측의 residual correction, open/closed-loop stability 진단까지 기존 연구에 있다.

Pinned RTR의 π0.5 15/60Hz recipe는 horizon12/48과 non-servo/servo mode를 함께 바꾸며 설정 control_hz60·execute_hz50은 같다. 이는 source 차이이지 성능 원인·논문 오류의 입증이 아니다. AAC의 entropy→chunk 길이→env.step 경로, A2C2의 delay/horizon 분리·매 step 최신 residual 입력을 확인했다. 정책 실행0회다.

## GPU가 확보되면 가능한 최소 검증

Qualified 한 task/checkpoint/controller에서 label·command·servo·센서·replanning 시간을 계측할 수 있다. 같은 timed reference의 resampling과 retiming, fresh/stale input, gain-only 개입을 나누고 fixed horizon부터 비교한다. 호환된 backbone에서 RTC/AAC와 추가 학습 비용을 계정한 A2C2를 대조한다.

## GPU 외 한계

같은 chunk 길이는 같은 물리 horizon이 아니다. Reference 경로를 맞춰도 realized trajectory는 결과로 달라질 수 있다. Delta aggregation은 contact/gripper/rotation 결과를 보존하지 않는다. Lockstep simulator의 wall-time sleep은 물리 지연이 아니다. A2C2 eval model 경로는 placeholder이며 RTR는 real hardware가 필요하다. 세 release의 장점을 하나의 qualified packet처럼 합치지 않는다.

**현재 권고:** GPU 확보보다 coherent native packet과 기존 선행을 넘어서는 차별적 예측이 먼저다. 통제 후 유용한 설계 지식이 남지 않으면 독립 연구로 종료한다.

근거: [E2 결과](../2026-10-22_e2_buildup/README.md), [source 감사](../2026-10-22_e2_buildup/SOURCE_INTERFACE_AUDIT.md), [비교 계약](../2026-10-22_e2_buildup/CLAIM_CONTRACT.md), [미실행 spec](../2026-10-22_e2_buildup/QUALIFICATION_SPEC.json).

## Registry 연결 — 2026-10-22 등록

- [RTC](../../../2025/NeurIPS/2025_NeurIPS_Real-Time-Execution-of-Action-Chunking-Flow-Policies/01_overview.md) — 2025 NeurIPS, `pr-1002`.
- [SAIL: Faster-than-Demonstration Execution of Imitation Learning Policies](../../../2025/CoRL/2025_CoRL_SAIL-Faster-than-Demonstration-Execution-of-Imitation-Lear/01_overview.md) — 2025 CoRL, `pr-1003`.
- [RTR](../../../2026/ICML/2026_ICML_Learning-High-Frequency-Continuous-Action-Chunks-in-Latent/01_overview.md) — 2026 ICML, `pr-1004`.
- [AAC](../../../2026/CVPR/2026_CVPR_Adaptive-Action-Chunking-at-Inference-time-for-Vision-Lang/01_overview.md) — 2026 CVPR, `pr-0994`.
- [A2C2](../../../2025/arXiv/2025_arXiv_Leave-No-Observation-Behind-Real-time-Correction-for-VLA-A/01_overview.md) — 2025 arXiv, `pr-1005`.
- [SPACE: Enabling Learning from Cross-Robot Data Toward Generalist Policies](../../../2026/arXiv/2026_arXiv_SPACE-Enabling-Learning-from-Cross-Robot-Data-Toward-Gener/01_overview.md) — 2026 arXiv, `pr-1000`.
- [Vela: Scaling Vision-Language-Action Models with Adaptive Action Curve Parametrization](../../../2026/arXiv/2026_arXiv_Vela-Scaling-Vision-Language-Action-Models-with-Adaptive-A/01_overview.md) — 2026 arXiv, `pr-0999`.
- [PaceVLA: Adaptive Temporal Action Quantization in Vision-Language-Action Models](../../../2026/arXiv/2026_arXiv_PaceVLA-Adaptive-Temporal-Action-Quantization-in-Vision-La/01_overview.md) — 2026 arXiv, `pr-1001`.
- [Measuring the Stability Assumption Behind Action Chunking](../../../2026/arXiv/2026_arXiv_Measuring-the-Stability-Assumption-Behind-Action-Chunking/01_overview.md) — 2026 arXiv, `pr-1006`.

발표 status와 신규 5개 note의 근거는 각 overview를 따른다. 이전 buildup의 정독/코드 감사와 이번 abstract 기반 등록의 범위를 합치지 않는다.
