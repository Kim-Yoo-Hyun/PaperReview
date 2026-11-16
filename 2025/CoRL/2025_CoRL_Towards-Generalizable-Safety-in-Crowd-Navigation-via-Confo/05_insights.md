# Towards Generalizable Safety in Crowd Navigation via Conformal Uncertainty Handling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Adaptive conformal prediction의 불확실성을 관측에 넣고 constrained RL로 행동을 조절한다.

속도·행동 정책·집단 변화 및 실로봇 군중 navigation을 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/yao25a.html). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 보장의 단위, reactive crowd, calibration update와 intervention 비용은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

GAP-P 계열에서 uncertainty 추가 자체를 새로운 navigation 기여로 삼지 않게 하는 직접 선행이다.

### Dependency and Evolution

Trajectory prediction/ACI → constrained navigation → 반응형 crowd 진단.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 scene에서 보정 유무를 비교하고 collision·진행·coverage를 함께 기록한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Robot 행동이 pedestrian 분포를 바꾸는 상황에서도 예측 coverage와 안전 이득이 함께 유지되는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
