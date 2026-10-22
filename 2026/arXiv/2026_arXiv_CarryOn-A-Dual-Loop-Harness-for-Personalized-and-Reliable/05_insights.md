# CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

계획과 action safety/recovery의 dual-loop 구조를 frozen VLA에 결합한다.

Simulation과 실제 robot assistance 결과를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.21453) · [저자 project/code](https://vincent2311.github.io/Projects/CarryOn/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 메모리 입력, failure detector, recovery 비용, 공개 구현 범위은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

D2/D3에서 persistent planning·shield 결합의 신규성 경계를 정한다.

### Dependency and Evolution

VLA·task planning·safety filter → CarryOn.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 policy·정보·도구에서 planner와 shield를 하나씩 제거해 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

추가 scene/user 정보 없이도 dual-loop 이득이 유지되는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
