# RoboArena: Distributed Real-World Evaluation of Generalist Robot Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

분산 평가자가 두 정책을 double-blind로 비교하고 선호 결과를 통합한다.

DROID 플랫폼을 사용하는 여러 기관에서 generalist policy를 실로봇으로 비교한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/atreya25a.html) · [저자 project/code](https://robo-arena.github.io/) · [공식 code](https://github.com/pranavatreya/roboarena_backend). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 pairwise reset 조건, task 선택 편향, 선호 aggregation과 불확실성은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

LIBERO-Plus·THE COLOSSEUM의 고정 benchmark와 구별되는 실환경 평가 기준을 보완한다.

### Dependency and Evolution

DROID → RoboArena; LIBERO-Plus·THE COLOSSEUM과 평가 분포 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

정책과 예산을 고정하고 기관/과제별 순위 및 leave-one-site-out 안정성을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

기관·task 구성 변화에도 정책 순위가 유지되며, 고정 benchmark 순위와 일치하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
