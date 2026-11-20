# TacCoRL: Integrating Tactile Feedback into VLA via Simulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

촉각 VLA를 sim-real co-training으로 초기화하고 simulation RL과 실환경 supervised anchor로 개선한다.

실제 양팔 접촉 과제로 전이를 평가한다. 실제 로봇 online RL을 사용한 결과와 구별한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2606.11743) · [저자 project/code](https://tac-corl.github.io/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 촉각 합성 정합성, real anchor 비용, 물리 변화별 분할은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

촉각 추가와 단일 VLA RL 자체가 이미 선행임을 확인할 직접 비교다.

### Dependency and Evolution

π₀ 계열 flow 정책·RL 후학습·촉각 입력을 연결하며 contact-adaptation의 학습 baseline이다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 초기화·접촉 관측의 motion-only RL과 joint motion/gain RL을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

동일 접촉 입력과 상호작용 비용에서 강성 공동 학습이 motion-only VLA RL보다 나은가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
