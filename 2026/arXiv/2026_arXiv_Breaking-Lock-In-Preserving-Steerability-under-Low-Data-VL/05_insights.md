# Breaking Lock-In: Preserving Steerability under Low-Data VLA Post-Training

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

후학습 중 시각 grounding을 보존하고 추론 시 contrastive prompt guidance로 denoising을 조절한다.

Simulation과 실제 로봇의 여덟 평가에서 새로운 지시에 대한 일반화를 비교한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2604.23121) · [저자 project/code](https://suninghuang19.github.io/delock_page/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 미확인 항목: 시각 보존 손실·guidance 입력·새 지시 split·RL과 SFT의 데이터/비용 차이.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

단순히 지시 보존·semantic freezing을 도입하는 것을 새 연구 기여로 주장하지 않도록 한다.

### Dependency and Evolution

일반 VLA SFT·시각 정렬 보존·추론 guidance를 RL 후학습 및 LIBERO-CF와 비교한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 지시쌍에서 기본 정책·후학습·guidance의 효과와 추가 추론 비용을 분리한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

RL 적응에서도 학습률과 시각 보존·추론 guidance 이후 잔여 행동 변화가 있는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.

## Related Research Review

[지시별 행동 보존의 선행 대조](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/8303fdd74fedbd456c0ab94230bde5cfd64c40ba/work/research_topics/unified_vla_rl/%EB%82%B4%EC%9A%A9/README.md#langret-n1)와 [source 원장](../../../work/sources/vla_masters_gap_scout_2026-11-12.json)에 지정 본문·공개 코드 검토 범위를 보존한다. 이 링크가 위 초록 노트나 사용자 reading status를 정독 완료로 승격하지 않는다.
