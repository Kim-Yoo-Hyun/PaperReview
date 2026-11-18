# StructRL: Structured Action-Space Exploration for Flow-Based VLAs

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Deterministic ODE decoder 뒤 실행 action space에 구조적 noise를 넣고 last-step replay로 정책 갱신 신호를 구성한다.

초록은 로봇 조작의 online RL 탐색을 대상으로 한다. 이번 등록에서는 task별 수치·동일 compute 여부를 확정하지 않는다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2608.15139). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 Last-step likelihood 의미·noise covariance·중간 flow dilution 분석·코드 호환은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

관계 기반 RL 탐색의 noise 위치·시간 구조·재채점 설계와 직접 충돌하는 최신 선행이다.

### Dependency and Evolution

Flow Matching/PPO·Colored Noise → StructRL → 관계 조건 covariance의 차이를 심사한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 ODE·variance·time correlation·replay에서 관계 conditioning만 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

실행 action noise의 구조를 이미 맞춘 뒤에도 시각/상태 조건 관계 학습의 이득이 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
