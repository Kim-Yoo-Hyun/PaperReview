# πRL: Online RL Fine-tuning for Flow-based Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Flow-Noise의 학습 가능한 noise 과정과 Flow-SDE의 ODE–SDE 변환을 대안으로 제시한다.

여러 benchmark에서 ID/OOD 개선을 보고한다. 접촉 강성 학습 효과를 직접 입증한 것은 아니다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2510.25889) · [저자 project/code](https://github.com/RLinf/RLinf). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 Flow-Noise/Flow-SDE 구분, likelihood 집계, normalizer와 update budget은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

현재 π₀ Flow-SDE/PPO backend의 likelihood·탐색 정의를 이해할 직접 prerequisite다.

### Dependency and Evolution

π₀/π₀.₅와 PPO·flow RL을 연결한다. RLinf-VLA 시스템 논문과 identity가 다른 방법 논문이다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 source/초기화에서 action dimension별 log-prob·entropy·학습 비용을 확인한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

추가 gain 차원의 정책 비율·탐색 비용을 motion-only 기준과 공정하게 맞출 수 있는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
