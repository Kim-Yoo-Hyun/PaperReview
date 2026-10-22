# Efficient Evaluation of Multi-Task Robot Policies With Active Experiment Selection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

비용을 고려한 active experiment selection과 task/policy 정보를 활용한다.

실제 및 simulated 평가 자료를 이용한 효율 비교를 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/anwar25a.html). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 prior 언어 정보, 관측 noise, offline matrix와 실제 online 실행 차이은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

C6의 task-aware cost-aware 평가 배분에 대한 직접 REFERENCE다.

### Dependency and Evolution

AOPS·STEP → active multi-task evaluation.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 task-policy matrix와 cost ledger로 uniform/active selection을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

동일 prior 접근에서 새 allocator가 selection 비용을 줄이는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
