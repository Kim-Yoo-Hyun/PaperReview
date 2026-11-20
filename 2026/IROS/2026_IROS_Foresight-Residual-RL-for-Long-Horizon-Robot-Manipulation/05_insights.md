# Foresight Residual RL for Long-Horizon Robot Manipulation with Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Downstream rollout의 성공 예측을 terminal-state 평가에 사용해 residual RL을 연결한다.

Simulation의 여러 단계 manipulation을 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2607.16506) · [저자 project/code](https://jaysparrow.github.io/foresight-residual-rl). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 stage 경계, privileged state, backward training 순서, 실제 robot 범위은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

D2에서 후속 실행 가능성을 reward에 넣는 좁은 RL 주장도 제한한다.

### Dependency and Evolution

Residual RL·VLA → foresight-conditioned continuation.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 rollout budget에서 local reward·foresight reward·outcome ranker를 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 downstream label로 단순 ranker를 사용한 설명보다 이득이 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
