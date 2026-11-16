# GRAD-NAV++: Vision-Language Model Enabled Visual Drone Navigation With Gaussian Radiance Fields and Differentiable Dynamics

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Gaussian radiance field와 differentiable dynamics를 이용한 학습에 VLM·mixture-of-experts를 결합한다.

Simulation과 실제 드론의 언어 조건부 navigation을 평가한다.

근거: [공식 paper/abstract](https://ieeexplore.ieee.org/document/11297793/) · [저자 project/code](https://qianzhong-chen.github.io/gradnavpp.github.io/) · [공식 code](https://github.com/Qianzhong-Chen/grad_nav). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 언어 encoder·MoE 갱신 범위, dynamics model 오차, 이전 GRaD-Nav 대비 새 평가 범위은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

언어·시각·행동과 differentiable RL을 결합한 직접 항법 선행이다. 기존 GRaD-Nav의 언어 조건부 확장이라 별도 등록한다.

### Dependency and Evolution

기등록 GRaD-Nav(pr-0290)·differentiable control과 VLA의 action interface를 비교한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 scene·언어·action으로 differentiable learning과 model-free RL을 비교하고 실제 전이를 분리 평가한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

효율 이득이 미분 가능한 환경에서 일반적인 비미분 simulator·실세계 적응으로도 유지되는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
