# Cooperative Grasping for Collective Object Transport in Constrained Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

환경·물체 조건을 반영하는 conditional embedding과 negative sampling으로 feasible grasp를 학습한다.

Simulation과 실제 협동 object transport를 평가한다.

근거: [공식 paper/abstract](https://doi.org/10.1109/LRA.2026.3653338). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 환경 표현, label 생성 planner, two-robot 제약, 일반화 split은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

D2의 운반 결과를 고려한 파지 주장이 이미 다뤄졌음을 보여준다.

### Dependency and Evolution

GraspNet·TAMP → transport-aware grasp selection.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

Grasp 후보를 고정하고 transport feasibility selector와 nearest/simple planner 기준을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

동일 planner 접근에서 새 selector가 학습된 feasibility 기준보다 유리한가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
