# Guiding real-world reinforcement learning for in-contact manipulation tasks with Shared Control Templates

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

물체 관계·task geometry의 알려진 제약을 shared-control template으로 표현해 RL이 탐색하는 차원을 줄인다.

7-DoF 실제 로봇의 pouring·grid-clamp placement를 다룬다. 논문의 안전 주장 조건을 보편적 보증으로 일반화하지 않는다.

근거: [공식 paper/abstract](https://link.springer.com/article/10.1007/s10514-024-10164-6). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 수동 task constraint·phase 전환·안전 보증 전제·reward 정보은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

관계/geometry로 탐색을 제한한다는 원리를 이미 제시한 직접 선행이다.

### Dependency and Evolution

제약 제어 → Shared Control Templates → 관계 조건 VLA exploration을 비교한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

고정 제약 template과 learned weighting에 동일 관계 정보·action budget을 제공한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

학습한 관계 조건 탐색이 고정 task template의 구현 비용과 일반화 한계를 줄이는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
