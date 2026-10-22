# PaceVLA: Adaptive Temporal Action Quantization in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

여러 시간 granularity의 표현과 router로 적응형 temporal quantization을 구성한다.

Simulation과 실제 manipulation에서 실행 효율·성능을 평가한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.25961) · [저자 project/code](https://pacevla.github.io/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 v2 controller 설정, router 비용, task별 gain, success/time denominator은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

E2의 adaptive time compression과 직접 겹치는 REFERENCE다.

### Dependency and Evolution

FAST·Vela → PaceVLA → 시간/feedback 진단.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 controller gain·물리 시간 예산에서 고정/적응 granularity를 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Tracking gain과 관측 횟수를 맞춘 뒤에도 temporal router 이득이 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
