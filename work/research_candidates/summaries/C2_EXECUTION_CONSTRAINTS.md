# C2 — 목표 성공뿐 아니라 수행 방식 지시까지 따르는 VLA

- 요약일: 2026-10-22. **현재 설계 NO-GO, 1차 채택 심사 종료.**
- 질문: 같은 데이터·reward label·조합 coverage에서 RL이 새 object×waypoint×orientation 조합의 수행 방식 준수를 추가로 개선하는가?

## 실제 진행과 결과

ExecVLA·RoboFollow·CounterAlign과 조합 일반화 선행을 대조했다. Goal/how 구분이나 dependency coverage 자체는 새 기여가 아니다. 공개 task 8개와 4/4 split 초안을 만들었지만 executable=false다.

실제 metadata 400개, training instruction 200개, payload 12쌍, 경유 trace 50개를 확인했다. 일부 route supervision과 training task의 경유 negative는 있었지만 완전한 object pose/quaternion·reward·coverage 계약은 확보하지 못했다. Reference Docker 경로의 ARM64 dependency·GPU allocation·checkpoint 자격도 미충족이었다. Policy 효과 비교는 실행하지 않았다.

## GPU가 확보되면 가능한 최소 검증

먼저 완전한 label과 task/checkpoint가 갖춰진 새 packet이 필요하다. 그 뒤 호환 Docker에서 native evaluation과 reward 판정의 agreement를 확인하고, 동일 paired scene에서 instruction-only 변경이 실제 action을 바꾸는지 볼 수 있다. 마지막으로 matched SFT/성공선택/weighted imitation/RL 대조를 검토한다.

## GPU 외 한계와 재개 조건

GPU는 누락 label·조합 coverage·원래 checkpoint 부재·ARM64 compatibility를 자동 해결하지 않는다. Instruction을 바꿨는데 evaluator는 원 goal을 쓰는 오류도 방지해야 한다. 분할의 atomic/pair coverage만 맞아도 dependency 일반성이 보장되는 것은 아니다.

**현재 권고:** 새 reward/coverage·native 실행 근거 없이 학습 sweep이나 환경 이식을 재개하지 않는다. 현재 결과는 RL 효과의 부정 증거가 아니라 효과를 검증할 전제의 실패다.

근거: [1차 판단](../2026-10-20_vla_rl/C2_BUILDUP_RESULT.md), [직접 충돌](../2026-10-20_vla_rl/C2_REVIEW.md), [실제 데이터·Docker 검사](../../experiments/vla_rl_c2_first_pass/RESULTS.md).

## Registry 연결 — 2026-10-22 등록

- [ExecVLA](../../../2026/arXiv/2026_arXiv_ExecVLA-Following-Fine-Grained-Execution-Constraints-in-Vi/01_overview.md) — 2026 arXiv, `pr-1035`.
- [CounterAlign: Counterfactual Supervision for Vision-Language-Action Models](../../../2026/CoRL/2026_CoRL_CounterAlign-Counterfactual-Supervision-for-Vision-Languag/01_overview.md) — 2026 CoRL, `pr-1033`.
- [RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents](../../../2026/CoRL/2026_CoRL_RoboFollow-Unveiling-the-Instruction-Following-Mirage-in-E/01_overview.md) — 2026 CoRL, `pr-1034`.

발표 status와 신규 5개 note의 근거는 각 overview를 따른다. 이전 buildup의 정독/코드 감사와 이번 abstract 기반 등록의 범위를 합치지 않는다.
