# Benchmarking World-Model Learning with Environment-Level Queries

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

도달 가능성·개입 결과 같은 environment-level query를 평가하는 WorldTest를 제안한다.

AutumnBench grid-world에서 사람과 학습 agent를 비교한다. 실로봇 평가는 아니다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v306/warrier26a.html) · [저자 project/code](https://zenodo.org/records/19498269). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 query 정답 접근, exploration budget, 환경 생성 분할, robot task로의 전이은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

VLA world model의 시각 품질·정책 순위와 환경 이해를 구분할 평가 방법론이다.

### Dependency and Evolution

General agents need world models → WorldTest; dWorldEval과 평가 대상 차이 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

공유 rollout으로 구별 불가능한 환경 쌍을 만들고 추가 관측·query별 식별성을 평가한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

동일 관측 return의 두 모델이 새로운 action의 counterfactual 질의에서도 일치하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
