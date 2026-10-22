# CounterAlign: Counterfactual Supervision for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Instruction mismatch를 counterfactual supervision으로 사용해 reward/정책을 정렬한다.

LIBERO 계열 instruction 평가와 실제 robot 결과를 보고한다.

근거: [공식 paper/abstract](https://openreview.net/forum?id=AY4totylcx). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 negative validity, reward leakage, scene overlap, constraint label 범위은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

C2와 새로운 VLA 탐색에서 지시 준수 개선의 직접 baseline이다.

### Dependency and Evolution

OpenVLA·offline RL → CounterAlign → RoboFollow.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

Object/task 지시와 execution constraint를 분리한 held-out 평가를 수행한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 negative/compute에서 language alignment가 실행 방식 지시에도 전이되는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
