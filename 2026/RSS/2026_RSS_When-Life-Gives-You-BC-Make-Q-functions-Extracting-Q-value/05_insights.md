# When Life Gives You BC, Make Q-functions: Extracting Q-values from Behavior Cloning for On-Robot Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

BC로부터 Q를 추정하고 BC·RL 행동을 가치에 따라 선택하며 online 학습한다.

D4RL·robomimic과 실제 pipe assembly·kitting을 평가한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p153.html) · [저자 project/code](https://pages.rai-inst.com/q2rl_website/) · [공식 code](https://github.com/rai-opensource/q2rl). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 Q 초기화에 필요한 상호작용, 두 정책 유지 비용, gating의 행동 분포 변화은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

BC prior 보존을 새 unified objective 없이 달성하는 강한 대안이다.

### Dependency and Evolution

BC→offline-to-online RL의 전이와 V-GPS의 가치 선택을 함께 비교한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

초기 BC와 환경 예산을 고정하고 gating 유무 및 BC 유지 regularization을 교차 대조한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

통합 actor-critic의 안정성 이득이 단순 Q-Gating보다 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
