# Learning to Look: Seeking Information for Decision Making via Policy Factorization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

정보 탐색과 조작 정책을 분리하고 조작 정책에서 탐색 reward를 구성하는 DISaM을 제안한다.

공식 초록은 simulation·실세계의 정보 탐색이 필요한 조작 과제 5개를 평가한다고 명시한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/dass25a.html) · [저자 project/code](https://robin-lab.cs.utexas.edu/learning2look/) · [공식 code](https://github.com/UT-Austin-RobIn/l2l). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 Context privilege·KL 대상 분포·학습 reward·전환 threshold은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

행동 불확실성 기반 관측 전환이 이미 존재함을 확인할 필수 직접 선행이다.

### Dependency and Evolution

POMDP/정보 수집 → DISaM → 현재 pose별 행동 양립성 질문을 비교한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 context·행동 후보·관측 예산에서 분포 간 KL과 성공 lookup을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

정책 분포 차이와 실제 공통 성공 행동의 존재가 어긋나는 사례에서 별도 성공 예측이 유용한가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
