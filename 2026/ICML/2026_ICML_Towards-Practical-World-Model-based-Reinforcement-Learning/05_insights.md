# Towards Practical World Model-based Reinforcement Learning for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Unified multimodal model 기반 dynamics, interleaved multi-view decoding 및 chunk-level branched rollout을 결합한다.

공식 ICML abstract는 simulation과 real-world task에서 policy 성능 및 sample efficiency 평가를 명시한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v306/zhang26ez.html) · [저자 project/code](https://github.com/LAMDA-RL/VLA-MBPO). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 Multi-view conditioning, rollout branching state 분포, reward model과 실제 transfer 검증은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Current trend. Multi-view consistency와 chunk-level branched rollout으로 world-model RL의 오차 누적을 다룬다. WMPO/WorldGym을 읽을 때 직접 비교해야 할 누락 논문이다.

### Dependency and Evolution

WMPO/WorldGym + model-based RL → VLA-MBPO; VLAW/RISE와 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 world model과 policy에서 long rollout과 chunk-level branched rollout을 비교해 model error·real success·interaction 비용을 측정한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Branched rollout의 horizon 제한이 동일 world-model error 아래 실제 task 성능을 안정화하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
