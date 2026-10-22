# RP-3 — 상태 변화 후 오래된 memory를 언제 갱신·폐기할 것인가

- 요약일: 2026-10-22. **RETIRED historical overlay; hypothesis UNTESTED.** 최근 일반 memory 탐색도 새 후보로 승격하지 않았다.
- 질문: 외부 세계 변화 뒤 memory의 validity와 그 memory를 쓸 때의 unsafe-action risk를 구분하면, 같은 관측 비용에서 retain/refresh/expire/verify를 더 잘 선택하는가?

## 진행 내용과 핵심 판단

고정 memory representation과 frozen downstream policy 위에서 object relocation/removal/articulation 변화, fresh/stale/masked/verified branch, fixed TTL·confidence·transition verifier 대조를 설계했다. Persistent memory, transition verification, value-guided retention에 이미 강한 선행이 있어 단순한 memory 갱신 모듈은 기여가 아니다. 최근 HALO의 task-relevant retrieval도 일반 relevance 주장의 대안이다.

실제 policy가 memory를 쓰는지, stale memory가 harm을 만드는지, expiry로 줄어드는지는 미검증이다. 문서의 metric과 phase는 계획이지 측정 결과가 아니다.

## GPU가 확보되면 가능한 최소 검증

재개 결정 후 native memory-capable policy의 입력 경로와 competence를 확인한다. 같은 scene/policy 상태에서 fresh/stale/masked 입력을 비교해 실제 memory의 유용성과 피해를 먼저 측정할 수 있다. 이후 같은 verification 횟수·latency에서 단순 TTL/refresh와 비교한다.

## GPU 외 한계

물리 world change와 memory exposure의 원인 귀속, oracle object identity 누출, state restore·policy memory 동치, 학습/평가 shift family 분리가 필요하다. Fresh memory도 정책이 활용하지 못하거나 stale이 no-memory보다 해롭지 않으면 expiry 가설의 전제가 없다. Safety risk를 단순 item validity와 동일시하면 안 된다.

**현재 권고:** RETIRED 유지. 새 3D map이나 RL supervisor를 만들기 전에 downstream memory use와 harm을 입증해야 한다.

근거: [보존된 RP-3](../../../research/projects/RP-3_MEMORY_EXPIRY.md), [최근 VLA 탐색](../2026-10-22_vla_rescout/README.md).

## Registry 연결 — 2026-10-22 등록

- [CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance](../../../2026/arXiv/2026_arXiv_CarryOn-A-Dual-Loop-Harness-for-Personalized-and-Reliable/01_overview.md) — 2026 arXiv, `pr-1010`.
- [VoLo: A Physical Orchestrator for Open-Vocabulary Long-Horizon Manipulation](../../../2026/CoRL/2026_CoRL_VoLo-A-Physical-Orchestrator-for-Open-Vocabulary-Long-Hori/01_overview.md) — 2026 CoRL, `pr-1014`.

발표 status와 신규 5개 note의 근거는 각 overview를 따른다. 이전 buildup의 정독/코드 감사와 이번 abstract 기반 등록의 범위를 합치지 않는다.
