# THE COLOSSEUM: A Benchmark for Evaluating Generalization for Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Manipulation task에 시각·물리 perturbation을 체계적으로 적용하는 simulation benchmark를 제시한다.

Simulation 비교와 대응 실세계 perturbation의 관련성을 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss20/p133.html) · [저자 project/code](https://robot-colosseum.github.io/) · [공식 code](https://github.com/robot-colosseum/robot-colosseum). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 복합 요인 상호작용, simulator와 실세계 조건의 대응은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

LIBERO 계열에 한정하지 않고 manipulation 일반화를 점검할 benchmark 계보다.

### Dependency and Evolution

RLBench → THE COLOSSEUM → Colosseum V2.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

단일 perturbation과 결합 perturbation을 같은 초기 상태에서 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

시각 변화와 물리 변화가 task feasibility를 맞춘 뒤 서로 다른 실패를 만드는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
