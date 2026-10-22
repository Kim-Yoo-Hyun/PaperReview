# 초기 주제 — VLA 실행 지연·adaptive chunk·slow/fast 보정

- 요약일: 2026-10-22. **넓은 신규 주제에서 제외; 해당 초기 방향의 정책 실험 없음.**
- 질문: 느린 VLA의 chunk 실행 중 feedback을 추가하거나 실행 길이를 바꾸면 실제 제어를 개선할 수 있는가?

## 진행 내용과 결론

초기 로봇 간 RL 전이 검토 중 함께 살펴본 방향이다. REMAC와 TIC-VLA 등이 adaptive chunk·시간 일관성·빠른 보정의 직접 비교 대상이어서 그 조합만으로 새 기여를 주장하지 않았다. 초기 검토의 별도 효과 수치는 없다.

후속 [E2](./E2_TEMPORAL_FEEDBACK.md)는 이 문제를 다시 넓게 채택한 것이 아니라 시간 표현·관측 갱신·controller 효과의 분리 가능성을 심사한 주제다. E2의 문헌/source 결과를 초기 실험의 성과로 소급하지 않는다.

## GPU가 확보되면 가능한 최소 검증

사용자가 선택한 현재/clone 컴퓨터의 로컬 Docker에서 qualified native model의 실제 sensor capture, inference completion, action 적용 시점을 계측하고, fixed horizon과 공개 asynchronous 방법을 같은 물리 시간·계산 budget으로 비교할 수 있다. 단순 wall-clock sleep을 physics delay로 취급하지 않는다.

## 한계와 연구 가치

GPU는 지연을 줄일 수 있어도 신규성을 만들지 않는다. Controller의 위치 유지, queue 교체, frame age와 modality별 delay가 다른 문제를 만든다. Contact 등 새로운 조건에서 기존 방법과 예측이 갈리는 현상·설명이 있어야 독립 연구가 된다. 일반적인 scheduler·빠른 residual의 구현만으로 채택하지 않는다.

**현재 권고:** 별도 활성 프로젝트로 복원하지 않고 E2의 시간/정보 비교 계약을 재사용한다.

근거: [초기 결과의 문헌 경계](../../experiments/vla_rl_cross_embodiment/RESULTS.md), [E2 비교 계약](../2026-10-22_e2_buildup/CLAIM_CONTRACT.md).

## Registry 연결 — 2026-10-22 등록

- [RTC](../../../2025/NeurIPS/2025_NeurIPS_Real-Time-Execution-of-Action-Chunking-Flow-Policies/01_overview.md) — 2025 NeurIPS, `pr-1002`.
- [AAC](../../../2026/CVPR/2026_CVPR_Adaptive-Action-Chunking-at-Inference-time-for-Vision-Lang/01_overview.md) — 2026 CVPR, `pr-0994`.
- [A2C2](../../../2025/arXiv/2025_arXiv_Leave-No-Observation-Behind-Real-time-Correction-for-VLA-A/01_overview.md) — 2025 arXiv, `pr-1005`.

발표 status와 신규 5개 note의 근거는 각 overview를 따른다. 이전 buildup의 정독/코드 감사와 이번 abstract 기반 등록의 범위를 합치지 않는다.
