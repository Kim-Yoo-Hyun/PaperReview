# ActMem-VLA: Action-History Memory with Dual-Expert Denoising for Long-Horizon Vision-Language-Action Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Mamba 행동 이력 memory와 PreAction Expert를 학습하고 frozen action expert에 denoising을 넘긴다.

LIBERO-Mem과 네 실제 조작 과제에서 memory 및 기존 VLA와 비교한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.37307). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 미확인 항목: memory reset·실제 실행 이력의 정의·효과 피드백 접근권·분할과 예산.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

행동 이력 memory의 강한 비교 자료이며 결과 기반 기억이라는 질문의 기존 대안을 구체화한다.

### Dependency and Evolution

MemoryVLA·π₀.₅·RoboMME와 명령 이력/관측 결과/작업 진행도의 차이를 비교한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 명령 이력에서 실제 접촉/효과가 달라지는 자연 사례로 관측·이력 의존성을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

행동 이력이 유지돼도 실행 결과가 바뀌는 경우 memory가 결과를 올바르게 반영하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
