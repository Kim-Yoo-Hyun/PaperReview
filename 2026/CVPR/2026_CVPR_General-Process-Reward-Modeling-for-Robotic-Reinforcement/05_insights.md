# General Process Reward Modeling for Robotic Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

다시점 step-aware 보상 모델과 policy-invariant reward shaping을 제안한다.

Simulation·실제 조작에서 reward 평가와 policy 학습을 보고한다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Tan_General_Process_Reward_Modeling_for_Robotic_Reinforcement_Learning_CVPR_2026_paper.html) · [저자 project/code](https://robo-dopamine.github.io/) · [공식 code](https://github.com/FlagOpen/Robo-Dopamine). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 보존 정리의 가정, 종료 처리, multi-view 특권, task별 추가 시연은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

VLA+RL 보상 설계와 HINDSIGHT의 대안 설명을 검토할 직접 선행이다.

### Dependency and Evolution

Potential-based reward shaping·ReWiND·SRPO를 실제 최적 정책 보존 조건과 함께 비교한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

보상 오류를 독립 측정하고 sparse-only, 직접 dense, invariant shaping을 같은 rollout budget으로 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

불완전한 학습 reward에서도 shaping의 이론적 보존과 실제 안전한 행동이 함께 성립하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
