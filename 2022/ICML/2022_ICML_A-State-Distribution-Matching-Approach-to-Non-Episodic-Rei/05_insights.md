# A State-Distribution Matching Approach to Non-Episodic Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

시연 state 분포를 맞추는 backward policy로 task-relevant reset을 학습한다.

EARL의 sparse-reward continuous control task를 평가한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v162/sharma22a.html). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 demonstration 접근, forward/backward budget, independent evaluation은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

C5의 reset-induced state distribution 자체가 신규 문제가 아님을 보여준다.

### Dependency and Evolution

EARL → state-distribution matching → autonomous VLA 학습.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

Reset 분포별 learning curve와 고정 평가 분포의 checkpoint 성능을 함께 기록한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 human 비용에서 reset 분포의 성능 차이는 독립 평가에도 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
