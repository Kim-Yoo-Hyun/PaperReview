# Learning Visuotactile Estimation and Control for Non-prehensile Manipulation under Occlusions

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Simulation interaction으로 visuotactile estimator를 학습하고 불확실성을 정책에 연결한다.

비파지 manipulation의 가림 조건과 실로봇 sim-to-real을 평가한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/ferrandis25a.html). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 privileged training input, tactile modality, occlusion 분포, estimator와 policy ablation은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

접촉 VLA의 센서 이득과 상태 추정·feedback controller 이득을 분리할 직접 대안이다.

### Dependency and Evolution

POMDP·촉각 상태 추정 → visuotactile control; FuSe·force VLA와 입력 조건 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 estimator에서 uncertainty 입력만 제거하고 occlusion 조건별 제어 실패를 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

센서 정보가 같을 때 uncertainty 제공이 점 추정값만 사용하는 제어보다 유리한가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
