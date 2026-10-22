# Is Your Imitation Learning Policy Better than Mine? Policy Comparison with Near-Optimal Stopping

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

순차 검정으로 비교를 멈출 시점을 결정한다.

Simulation 및 실제 policy 비교를 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss21/p077.html). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 독립성, indifference region, 오류 확률, 다중 비교 처리은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

C6의 trial budget·통계적 중단에 대한 표준 직접 기준이다.

### Dependency and Evolution

Sequential testing → STEP → NSCORE.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

고정한 두 policy·독립 trial로 sequential vs fixed-budget 비교를 수행한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Adaptive checkpoint selection에서 보장 조건을 만족하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
