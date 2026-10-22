# Diffusion Policy Policy Optimization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Denoising 과정을 policy-gradient 최적화에 포함하고 diffusion policy에 맞춘 학습 설계를 제안한다.

Continuous-control/robotic simulation, pixel/state 입력 및 Furniture-Bench sim-to-real assembly 평가를 project에서 확인했다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2025/hash/c0749c39aaff9e9e4c91f7118bf21b1e-Abstract-Conference.html) · [저자 project/code](https://diffusion-ppo.github.io/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 정확한 likelihood 구성, denoising horizon, 실행 chunk와 sim-to-real reset 조건은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Foundation bridge. PPO를 denoising policy의 RL fine-tuning으로 연결한다. Diffusion Policy → DPPO → RL-100 등 직접 policy 개선을 비교하는 prerequisite이므로 CORE를 검토할 이유가 있다. VLA 자체를 제안한 논문은 아니다.

### Dependency and Evolution

PPO + Diffusion Policy → DPPO → RL-100/DSRL 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 pretrained Diffusion Policy에서 BC 유지와 DPPO를 비교하고, denoising 설정만 바꾸어 성공률·interaction 수·실행 latency를 측정한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Denoising exploration의 이득이 demonstration 양과 interaction budget을 맞춰도 유지되는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
