# Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

지시 재표현과 action sample을 함께 확장하고 contrastive verifier로 prompt·action을 선택한다.

SIMPLER·PolaRiS와 실로봇의 in/out-of-distribution 지시 실행을 평가한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2602.12281) · [저자 project/code](https://cover-vla.github.io/) · [공식 code](https://github.com/cover-vla/cover-vla). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 재표현의 의미 보존, verifier 감독량, rollout-independent evaluation은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

정책 RL 갱신의 필요성을 검증할 강한 추론 계산량·검증 대안이다.

### Dependency and Evolution

V-GPS·VERITAS·OpenVLA와 critic/verifier의 목표 및 학습 데이터 차이를 비교한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 backbone·데이터에 candidate 수와 verifier 비용을 포함한 성능/latency 곡선을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 총 계산량에서 단일 RL 정책이 verifier 기반 test-time scaling보다 유리한가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
