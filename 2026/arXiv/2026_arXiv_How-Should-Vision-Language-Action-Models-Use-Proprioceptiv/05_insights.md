# How Should Vision-Language-Action Models Use Proprioceptive State?

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

같은 flow-matching backbone에서 다섯 state interface와 history 길이를 통제한다.

45 atomic 및 20 composite task 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2608.03052) · 저자 프로젝트·코드 주소 미확인. 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 world-frame localization 포함 여부, native state 사용, checkpoint 공개은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

D1에서 state 사용과 history 효과를 먼저 입증할 NEXT prerequisite다.

### Dependency and Evolution

HPT·π0.5의 state interface → controlled state/history study → Self-Adaptive VLA의 hardware adaptation을 비교한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 slot 수의 repeated-current와 실제 history를 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

State history 효과가 반복 현재-state token 대조군보다 큰가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
