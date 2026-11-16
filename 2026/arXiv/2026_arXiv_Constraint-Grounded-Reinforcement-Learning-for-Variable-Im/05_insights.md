# Constraint-Grounded Reinforcement Learning for Variable Impedance Control in Contact-Rich Robotic Insertion

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Force-limit 조건부 RL이 motion·insertion rate·gain을 요청하고 controller가 gain 범위로 투영한다.

Simulated oblique insertion을 평가한다. Gain 범위 보장과 force-limit 경험적 만족은 구별한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.13516). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 Projection과 actor 범위, force constraint의 경험적/형식적 보장 차이은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

동작·강성 공동 RL 자체가 새롭지 않음을 보이는 controller 비교 자료다.

### Dependency and Evolution

Variable impedance RL을 VLA 내부 공동 행동 학습의 비-VLA 대안으로 둔다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 controller projection에서 비-VLA와 VLA actor의 조건 전이를 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

VLA prior가 gain 적응만으로 해결되지 않는 일반화를 제공하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
