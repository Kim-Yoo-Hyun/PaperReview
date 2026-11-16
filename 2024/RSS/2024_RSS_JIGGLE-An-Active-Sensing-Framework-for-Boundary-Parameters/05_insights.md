# JIGGLE: An Active Sensing Framework for Boundary Parameters Estimation in Deformable Surgical Environments

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

미분 가능한 soft-body 모델·EKF 추정과 정보 이득/안전 비용을 고려한 능동 조작을 결합한다.

실제 동물 조직의 부착점과 cutting/suturing 변화 실험을 보고한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss20/p007.html). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 재료 모델과 attachment 가정, 안전 비용 정의은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

물성·boundary 식별과 task-oriented probing을 구별하는 GAP-DE의 직접 선행이다.

### Dependency and Evolution

Deformable state estimation → JIGGLE → task-level sensing 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

정보 이득 probe와 단순 displacement probe를 task outcome으로 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 probe 비용에서 attachment 정보 증가가 downstream 작업 성공에 비례하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
