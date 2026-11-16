# Enhancing Tactile-based Reinforcement Learning for Robotic Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

희소 이진 접촉·proprioception 표현을 self-supervised learning으로 학습하고 SSL memory와 on-policy memory의 분리를 검토한다.

RoTO 시뮬레이션의 공 튀기기·Baoding 회전 등 dexterity를 평가한다. 실로봇 결과로 확대하지 않는다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/bc09efb501c801ed92e181e26a885c2d-Abstract-Conference.html) · [저자 project/code](https://elle-miller.github.io/tactile_rl/) · [공식 code](https://github.com/elle-miller/roto). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 센서 노이즈·빈도, sim contact의 현실성, 실물 센서 전이은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

시각 VLA에 촉각을 넣기 전에 입력 유용성과 표현 학습을 분리할 진단 자원이다.

### Dependency and Evolution

PPO·tactile manipulation 선행과 센서 정보량·memory 구조를 비교한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 제어기에서 contact 유무와 SSL memory 공유/분리를 교차 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

추가 센서 이득과 SSL memory 이득이 각각 독립적으로 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
