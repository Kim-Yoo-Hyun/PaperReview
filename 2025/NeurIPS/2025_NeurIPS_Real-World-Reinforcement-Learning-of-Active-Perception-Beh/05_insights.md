# Real-World Reinforcement Learning of Active Perception Behaviors

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

훈련 때만 사용하는 추가 센서로 privileged value를 학습하고 advantage-weighted regression으로 정책을 개선한다.

공식 초록은 3개 로봇·8개 조작 과제 및 generalist 초기 정책의 능동 관측 개선을 명시한다.

근거: [공식 paper/abstract](https://papers.neurips.cc/paper_files/paper/2025/hash/aa1b1a959c80086cba61d0fd66de412f-Abstract-Conference.html) · [저자 project/code](https://penn-pal-lab.github.io/aawr/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 추가 센서 접근·초기 demonstrations·advantage 추정·배포 observation은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

VLA+RL로 관측 행동을 만든다는 넓은 주장을 제한하는 핵심 실세계 기준이다.

### Dependency and Evolution

AWAC/advantage-weighted imitation → AAWR → pose ambiguity 기반 active VLA 질문을 비교한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

Actor 관측과 critic privilege를 분리하고 같은 초기 정책·interaction budget에서 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

동일 privileged label 예산에서 성공 양립성 학습이 value-weighted 정책 개선보다 관측을 잘 선택하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
