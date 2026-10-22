# Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

EEF-relative 정렬·embodiment mixture·regularization을 통제 비교하고 평가자 편향 통제를 제안한다.

Simulation과 real-robot 평가에서 데이터 혼합과 negative transfer를 분석한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2602.09722). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 EEF frame, normalization, split, grouped blind protocol은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

E1에서 정상 action 정렬·mixture 자체의 설명력을 먼저 제거할 기준이다.

### Dependency and Evolution

Open X-Embodiment·Octo → mixed-robot VLA scaling.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 sample 수·embodiment 비율·blind evaluation로 혼합 전후를 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

동일 물리 좌표 정렬 뒤에도 특정 데이터 쌍의 간섭이 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
