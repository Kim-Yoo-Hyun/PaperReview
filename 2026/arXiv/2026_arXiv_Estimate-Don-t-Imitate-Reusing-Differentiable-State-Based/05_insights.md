# Estimate, Don't Imitate: Reusing Differentiable State-Based Policies for Visuomotor Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

기존 미분 가능한 state-based expert를 고정하고, 상태 supervision과 expert를 통과하는 action-consistency loss로 시각 추정기를 학습한다. Expert의 행동 매핑을 다시 모방하는 비용을 줄이는 formulation이다.

초록은 goal-conditioned 조작 5개와 실제 Panda의 sim-to-real 평가를 보고한다. Trial 구성·각 조건별 성공 수·시연 분할은 이번 등록에서 확인하지 않았다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.34018). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 Expert의 미분 가능성·state/goal 정의·loss schedule·occlusion·held-out split·실제 로봇 trial 및 코드 release은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

현재 geometry 후보의 action-consistency 대조를 정하는 직접 NEXT다. 행동에 중요한 추정 오차를 학습한다는 원리를 신규성에서 제외하게 한다.

### Dependency and Evolution

Privileged-state RL·teacher-student distillation → expert 재사용과 task-aware perception → VLA geometry 개입 질문. 이는 개념 연결이며 직접 citation 확인은 별도다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 estimator·expert·시연에서 state-only, action-consistency 혼합, task outcome supervision을 비교한다. 이는 제안이며 원 논문 결과가 아니다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 상태/행동 supervision을 제공해도 action consistency로 설명되지 않는 task outcome 차이가 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
