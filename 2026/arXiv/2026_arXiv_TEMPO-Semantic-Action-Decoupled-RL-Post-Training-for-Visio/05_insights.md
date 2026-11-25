# TEMPO: Semantic-Action Decoupled RL Post-Training for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

VLM을 동결하고 semantic projection과 action expert를 서로 다른 빈도의 RL 갱신으로 적응한다.

CALVIN과 실제 조작 과제에서 후학습 정책·갱신 전략을 비교한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2608.07314) · 저자 프로젝트·코드 주소 미확인. 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 미확인 항목: 학습 task-set·두 학습기의 데이터/gradient 경계·초기 능력·비용 정의.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

단일 VLA 내부의 의미 보존과 모듈별 RL 갱신에 관한 직접 경쟁 선행이다.

### Dependency and Evolution

VLA RL·projection/action-expert 적응을 기존 U1 routing 및 LANGRET 보존 분석과 대조한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 정책·학습 목표에서 uniform update와 모듈별 update를 목표별 성공·비용으로 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

동일 목표 coverage·적응 비용에서 갱신 빈도 조절이 기존 목표 행동을 얼마나 보존하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.

## Related Research Review

[지시별 행동 보존의 선행 대조](https://github.com/Kim-Yoo-Hyun/PaperReview/blob/8303fdd74fedbd456c0ab94230bde5cfd64c40ba/work/research_topics/unified_vla_rl/%EB%82%B4%EC%9A%A9/README.md#langret-n1)와 [source 원장](../../../work/sources/vla_masters_gap_scout_2026-11-12.json)에 지정 본문·공개 코드 검토 범위를 보존한다. 이 링크가 위 초록 노트나 사용자 reading status를 정독 완료로 승격하지 않는다.
