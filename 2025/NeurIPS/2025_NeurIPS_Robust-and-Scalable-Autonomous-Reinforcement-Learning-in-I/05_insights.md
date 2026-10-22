# Robust and Scalable Autonomous Reinforcement Learning in Irreversible Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

학습 진전에 따른 curriculum과 행동 기반 비가역성 식별을 결합한다.

가역/비가역 환경에서 성능과 manual reset 감소를 보고한다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/56d748a1d7128158681280be7668e0d3-Abstract-Conference.html). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 irreversibility 정의, behavior encoding, task-specific 정보, reset 비용은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

C5/D3의 비가역성·reset 질문에 필요한 RL 선행이다.

### Dependency and Evolution

EARL·MEDAL → RSA → VLA interruption 진단.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 위험 event에서 task predicate와 행동 기반 탐지를 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 state 접근에서 VLA 현상은 기존 비가역성 탐지로 설명되는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
