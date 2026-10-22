# Clipped Action Policy Gradient

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

실행 action이 clipping되는 사실을 이용한 unbiased estimator를 제안한다.

Continuous control의 이론·실험 비교를 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v80/fujita18a.html) · [저자 project/code](https://github.com/pfnet-research/capg). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 clipping preimage, policy family, gradient unbiasedness 조건은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

C3에서 실행 동치 action의 확률 질량을 합치는 원리의 foundation이다.

### Dependency and Evolution

REINFORCE·PPO → CAPG → MPG/C3.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 reward·action sample에서 raw/clipped score variance를 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

VLA의 실제 controller mapping에서도 estimator 분산 감소가 유의미한가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
