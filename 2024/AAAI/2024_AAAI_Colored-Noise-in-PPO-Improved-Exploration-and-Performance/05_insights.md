# Colored Noise in PPO: Improved Exploration and Performance through Correlated Action Sampling

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

시간 상관을 갖는 colored noise로 stochastic action sampling을 바꾸고 noise color와 병렬 환경 수의 영향을 비교한다.

On-policy RL의 correlated/white noise와 병렬 data 수집 조건을 비교한다. 이 조사에서 실제 로봇 trial은 확인하지 않았다.

근거: [공식 paper/abstract](https://ojs.aaai.org/index.php/AAAI/article/view/29139) · [저자 project/code](https://github.com/jkbjh/cn-ppo-paper-code). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 행동 likelihood와 trajectory correlation·noise 재사용·seed/환경 수은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

복잡한 관계 noise 학습 전에 비교해야 할 단순 시간 상관 탐색 baseline이다.

### Dependency and Evolution

PPO → Colored Noise PPO → StructRL의 실행 action-space noise를 비교한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 variance·시간 상관·학습 예산에서 관계 조건과 고정 colored noise를 대조한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

관계 조건 noise의 이득이 시간 smoothing만으로 설명되는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
