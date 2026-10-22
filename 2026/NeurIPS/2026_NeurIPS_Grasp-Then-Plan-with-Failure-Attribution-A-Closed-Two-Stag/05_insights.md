# Grasp-Then-Plan with Failure Attribution: A Closed Two-Stage Framework for Precise and Generalizable Robotic Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Grasp-then-plan 두 단계와 failure attribution을 연결한다.

Simulation과 실제 manipulation 및 여러 정책 계열 비교를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2606.03385) · [저자 project/code](https://sites.google.com/view/gtp-fa/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 failure label 출처, planner 성공과 policy 성공 구분, code 공개은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

D2에서 downstream outcome·failure attribution을 새 방법으로 주장하지 않게 한다.

### Dependency and Evolution

Grasp planning·Diffusion Policy → GTP-FA.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 grasp 후보로 geometry-only ranking과 execution-outcome ranking을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

실패 label·planner 예산을 맞춰도 새 grasp ranking 이득이 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
