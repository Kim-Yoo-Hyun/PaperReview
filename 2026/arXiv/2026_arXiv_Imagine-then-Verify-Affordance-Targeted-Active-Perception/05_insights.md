# Imagine then Verify: Affordance-Targeted Active Perception for Task-Oriented Grasping in Cluttered Scenes

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

완성 shape에서 affordance 가설을 만들고 entropy 감소·실제 관측 검증을 함께 고려해 다음 시점을 정한다.

Simulation과 실제 cluttered scene의 기능적 grasp 및 NBV step을 평가한다. 전체 pouring/insertion 성공과 구별한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.23504). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 Shape hallucination·hypothesis weighting·view feasibility·stop threshold은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Task-aware NBV와 verification 기반 중단이 이미 있는 점을 반영할 직접 비교다.

### Dependency and Evolution

Shape completion/affordance → ATAP → 후보 행동의 continuation 성공을 다루는 질문을 비교한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 visibility·pose 정보·budget에서 affordance verification과 후보별 task success를 대조한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Affordance가 검증돼도 실행 후보의 성공 집합은 충돌할 수 있는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
