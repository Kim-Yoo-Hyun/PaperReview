# 탐색 단계 — VLM의 의미 능력을 보존하며 VLA로 적응하기

- 요약일: 2026-10-22. **탐색에서 새 후보로 승격하지 않음; 별도 8단계 buildup·실험 미진행.** E1의 robot-skill retention과 구분한다.
- 질문: VLM을 robot policy로 적응시킬 때 언어/시각 의미 능력의 보존이 실제 instruction following·robot generalization에도 유익한가?

## 검토 내용과 판단

Actions as Language(VLM2VLA)와 LAP가 자연어 action interface, adaptation과 semantic/cross-embodiment 전이를 이미 다룬다. 일반적으로 ‘언어 능력을 보존하자’거나 LoRA/action token 표현을 결합하는 것만으로 새 기여가 되지 않았다.

VQA 점수 보존, 순차 robot skill retention, 새로운 로봇의 실행 성능은 서로 다른 결과다. 이 연결을 검증한 자체 데이터·실험은 없다. 일반 memory relevance 방향은 [RP-3](./RP3_MEMORY_EXPIRY.md)에 따로 보존했다.

## GPU가 확보되면 가능한 최소 검증

Qualified model/data가 있을 때 같은 robot data·parameter/compute budget에서 semantic benchmark와 robot instruction contrast를 따로 평가할 수 있다. Semantic 개선이 실제 행동 선택을 바꾸는지 확인하는 것이 첫 검사다. 이는 기존 방법 재현/진단이며 곧바로 새 방법 연구는 아니다.

## GPU 외 한계

Semantic benchmark의 train overlap·답변 형식, action interface·normalizer·controller 차이, language-sensitive task의 자격이 필요하다. VQA 점수만 유지돼도 manipulation이 좋아진다고 결론 내릴 수 없다. 공개 pretraining coverage가 불명확하면 zero-shot 주장도 제한된다.

**현재 권고:** 별도 활성 후보로 자동 생성하지 않는다. 기존 VLM2VLA/LAP 이후에도 남는 구체적인 행동 실패·대안 설명·반증 가능한 질문을 먼저 찾아야 한다.

근거: [VLA 재탐색 결과](../2026-10-22_vla_rescout/README.md), [문헌 비교](../2026-10-22_vla_rescout/LITERATURE.md).

## Registry 연결 — 2026-10-22 등록

- [VLM2VLA](../../../2026/ICLR/2026_ICLR_Actions-as-Language-Fine-Tuning-VLMs-into-VLAs-Without-Cat/01_overview.md) — 2026 ICLR, `pr-0992`.
- [LAP: Language-Action Pre-training Enables Zero-Shot Cross-Embodiment Transfer](../../../2026/RSS/2026_RSS_LAP-Language-Action-Pre-training-Enables-Zero-Shot-Cross-E/01_overview.md) — 2026 RSS, `pr-0993`.

발표 status와 신규 5개 note의 근거는 각 overview를 따른다. 이전 buildup의 정독/코드 감사와 이번 abstract 기반 등록의 범위를 합치지 않는다.
