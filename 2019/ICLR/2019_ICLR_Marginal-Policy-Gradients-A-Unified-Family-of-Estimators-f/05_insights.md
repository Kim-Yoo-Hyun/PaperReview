# Marginal Policy Gradients: A Unified Family of Estimators for Bounded Action Spaces with Applications

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Marginal policy gradient family로 angular/clipped estimator를 통합한다.

RTS와 navigation task 및 variance 분석을 보고한다.

근거: [공식 paper/abstract](https://openreview.net/forum?id=HkgqFiAcFm). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 transform measurability, discrete/continuous 차이, action-slot weighting은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

C3의 action equivalence 주장을 제한하는 가장 직접적인 이론 계보다.

### Dependency and Evolution

CAPG → MPG → token/controller equivalence 진단.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

Actual checkpoint에서 실행 preimage별 score와 reward-weighted variance를 측정한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Token alias를 합친 VLA score 변화가 reward-weighted gradient에서도 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
