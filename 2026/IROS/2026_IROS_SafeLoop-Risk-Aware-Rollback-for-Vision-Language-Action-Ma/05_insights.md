# SafeLoop: Risk-Aware Rollback for Vision-Language-Action Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

시각·proprioception 기반 위험 예측과 no-op/rollback 개입을 결합한다.

LIBERO 및 실제 manipulation을 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.26313) · [저자 project/code](https://github.com/Loule0-0/SafeLoop/tree/release/safeloop). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 joint history와 world state 구분, detector labels, collision 비용은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

D3에서 rollback이 세계 상태를 되돌린다는 잘못된 가정을 피할 직접 비교군이다.

### Dependency and Evolution

Failure detection·recovery → SafeLoop.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 event 이후 continue·hold·rollback의 실제 object/task 상태를 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

비가역 환경에서 joint rollback이 새 목표 성공을 보장하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
