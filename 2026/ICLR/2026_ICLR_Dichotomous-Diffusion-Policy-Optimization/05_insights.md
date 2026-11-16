# Dichotomous Diffusion Policy Optimization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

보상 최대화·최소화 diffusion policy를 따로 학습하고 score의 선형 결합으로 추론 greediness를 조절한다.

ExORL·OGBench의 offline 및 offline-to-online RL과 NAVSIM 자율주행 VLA를 평가한다. 주행 VLA 결과를 조작 VLA의 근거로 확대하지 않는다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/64a0192102e1421a2b2c15ae0bdb9f3a-Abstract-Conference.html) · [저자 project/code](https://lrmbbj.github.io/DIPOLE/) · [공식 code](https://github.com/LRMbbj/DIPOLE). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 두 모델의 추가 계산량, 추론 결합 계수 선택, manipulation 전이은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Diffusion RL 안정화의 알고리즘 대안으로 참고하며 로봇 조작 효과는 별도 검증한다.

### Dependency and Evolution

Diffusion Policy·Q-score matching 계열과 ReinFlow의 정책 갱신 방식을 비교한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 데이터와 denoising 예산에서 single/dual score를 대조하고 return 및 seed 분산을 기록한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 RL 데이터에서 dual-score 결합이 단일 diffusion actor의 안정성 문제를 줄이는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
