# RoboReward: General-Purpose Vision-Language Reward Models for Robotics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Robot 자료와 counterfactual negative를 사용해 reward 모델·benchmark를 구성한다.

공개 robot 자료의 reward 평가와 실제 robot RL을 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2601.00675). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 counterfactual label 검증, temporal clipping, policy shift, benchmark leakage은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

C4의 독립 outcome과 reward model 차이를 정할 직접 기준이다.

### Dependency and Evolution

VLM reward·Open X-Embodiment → RoboReward.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 데이터에서 original/constructed negative를 분리해 독립 success와 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Negative 구성의 변화가 held-out policy reward hacking을 줄이는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
