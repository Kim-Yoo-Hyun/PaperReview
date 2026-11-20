# When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

LIBERO-CF로 반사실적 지시 수행을 평가하고 언어 조건부·비조건부 분기의 차이로 행동을 유도한다.

LIBERO-CF와 실제 로봇에서 언어 grounding과 task success를 구별해 평가한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2602.17659) · [저자 project/code](https://vla-cf.github.io/) · [공식 code](https://github.com/yuffish/VLA-CF). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 미확인 항목: focused suite의 장면 변경·OR/target-only 종료·두 목표의 기본 능력·guidance 비용.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

LANGRET의 공개 장면·지시쌍·평가기 source이며 기존 counterfactual benchmark와의 중복을 드러낸다.

### Dependency and Evolution

LIBERO·OpenVLA-OFT·π₀.₅의 지시 평가와 CounterAlign을 대조한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

Prompt·목표 predicate를 일치시키고 두 유효 목표의 첫 사건과 지정 목표 성공을 따로 기록한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 초기 장면에서 목표별 후학습 보존을 측정하면 aggregate success와 다른 판단을 얻는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.

## Related Research Review

[지시별 행동 보존의 선행 대조](../../../work/research_topics/unified_vla_rl/내용/README.md#langret-n1)와 [source 원장](../../../work/sources/vla_masters_gap_scout_2026-11-12.json)에 지정 본문·공개 코드 검토 범위를 보존한다. 이 링크가 위 초록 노트나 사용자 reading status를 정독 완료로 승격하지 않는다.
