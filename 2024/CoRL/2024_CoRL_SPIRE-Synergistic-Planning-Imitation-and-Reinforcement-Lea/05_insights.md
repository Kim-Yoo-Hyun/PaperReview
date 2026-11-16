# SPIRE: Synergistic Planning, Imitation, and Reinforcement Learning for Long-Horizon Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

TAMP로 작은 학습 문제를 만들고 planning context에 맞춘 IL·RL 학습을 결합한다.

장기·접촉 중심 조작 문제 집합에서 planning·IL·RL 결합 시스템들을 비교한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/zhou25a.html) · [저자 project/code](https://sites.google.com/view/spire-corl-2024). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 planner의 상태·기하 접근, 하위 문제 성공 분포, 실로봇 평가 범위은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

단일 VLA 내부 RL이 계층형 분해보다 어떤 비용·일반화 이점을 주는지 비교하는 시스템 대안이다.

### Dependency and Evolution

TAMP·SayCan과 RL/IL 결합을 비교하되 언어 VLA 자체의 결과로 해석하지 않는다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 과제·reset·데모 예산으로 planning scaffold의 유무를 대조하고 전체 성공과 개입 비용을 측정한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 subgoal 정보와 데이터에서 계층형 분해보다 단일 정책의 task transfer가 나은가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
