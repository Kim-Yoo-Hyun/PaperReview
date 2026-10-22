# Vela: Scaling Vision-Language-Action Models with Adaptive Action Curve Parametrization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

연속 spline action curve와 적응 길이 표현을 사용한다.

Simulation benchmark와 실제 long-horizon manipulation을 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.05230) · [저자 project/code](https://clementine24.github.io/Vela/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 spline fitting, horizon-matched 학습, controller tracking, code 공개 범위은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

E2에서 연속 행동 곡선 자체를 신규 기여로 재주장하지 않기 위한 REFERENCE다.

### Dependency and Evolution

ACT·FAST → 연속 action curve → PaceVLA.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 물리 reference의 discrete/curve 표현과 실행 시간·feedback을 분리 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 horizon과 controller에서 표현 변경 자체의 이득이 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
