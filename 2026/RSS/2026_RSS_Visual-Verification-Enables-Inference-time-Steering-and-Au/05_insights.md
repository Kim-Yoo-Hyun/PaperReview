# Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

시각 verifier가 후보 행동을 선택하고 검증된 rollout을 후속 정책 학습에 사용한다.

SIMPLER와 실제 DROID setup에서 steering 및 offline 개선을 평가한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p079.html). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 verifier 오류와 성공 판정의 독립성, fine-tuning objective, 인간 개입의 집계 범위은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

RL 자체의 기여를 주장할 때 반드시 비교할 자율 데이터 선택·모방 대안이다.

### Dependency and Evolution

V-GPS의 가치 기반 선택과 CoVer의 언어 정렬 검증을 비교하며, 선택과 정책 갱신의 효과를 분리한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

후보 수·verifier 비용·수집 예산을 맞춰 원 정책, 선택만, 선택 데이터 모방, RL을 대조한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

동일 rollout pool에서 검증 후 모방이 RL 후학습의 개선을 설명하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
