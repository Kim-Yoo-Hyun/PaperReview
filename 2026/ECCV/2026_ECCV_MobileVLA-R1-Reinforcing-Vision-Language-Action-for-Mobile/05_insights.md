# MobileVLA-R1: Reinforcing Vision-Language-Action for Mobile Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

구조화 CoT alignment 뒤 GRPO RL로 추론·제어 일관성을 학습한다.

VLN·VLA benchmark와 실제 사족 로봇 배포를 보고한다. MobileVLA-R1 2.0의 추가 주장은 포함하지 않는다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2511.17889) · [저자 project/code](https://aigeeksgroup.github.io/MobileVLA-R1/) · [공식 code](https://github.com/AIGeeksGroup/MobileVLA-R1). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 속도·이산 행동 output 형식, low-level controller 고정 여부, 2.0 코드와 원 논문 차이은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Manipulation 외에 단일 VLA 후학습을 검토할 모바일 로봇 선행이다.

### Dependency and Evolution

NaVILA·LongNav-R1과 action abstraction 및 RL reward를 비교한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 navigation 경로에서 CoT-only, RL, reasoning 제거 대조를 수행한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

언어 추론 개선과 제어 안정성 개선이 동일 RL objective에서 함께 발생하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
