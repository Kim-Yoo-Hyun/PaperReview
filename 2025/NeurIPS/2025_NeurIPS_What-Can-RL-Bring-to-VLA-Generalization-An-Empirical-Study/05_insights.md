# What Can RL Bring to VLA Generalization? An Empirical Study

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Visual·semantic·execution 변화 축으로 평가하고 PPO와 LLM 계열 RL 방법의 차이를 분석한다.

공식 NeurIPS abstract는 visual, semantic, execution generalization 및 PPO/DPO/GRPO 비교를 설명한다.

근거: [공식 paper/abstract](https://proceedings.nips.cc/paper_files/paper/2025/hash/8c0fabe372177d2aded596be2d3b4544-Abstract-Conference.html) · [저자 project/code](https://rlvla.github.io/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 Generalization split 생성, pretrained overlap, RL별 budget 및 real-robot 범위은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Benchmark / empirical study. Visual·semantic·execution generalization을 나누어 SFT와 RL을 비교한다. OpenVLA/OFT 이후 RL의 효과를 주장할 때 필요한 평가 기준이다. 해당 실험에서의 PPO 결과를 모든 VLA에 대한 우열로 일반화하지 않는다.

### Dependency and Evolution

OpenVLA/OFT + PPO → RL4VLA → SimpleVLA-RL/DyGRO-VLA 평가.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 VLA의 SFT와 PPO를 고정된 visual/semantic/execution split에서 평가하고 각 축의 성공률을 별도로 보고한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

RL의 generalization 이득이 reward·training data·rollout compute를 맞춘 뒤에도 semantic/execution 변화에서 유지되는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
