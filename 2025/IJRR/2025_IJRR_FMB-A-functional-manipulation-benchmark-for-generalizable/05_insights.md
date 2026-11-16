# FMB: A functional manipulation benchmark for generalizable robotic learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

복제 가능한 3D 프린트 물체·조립 과제와 imitation baseline을 구성한다.

실로봇의 개별 skill과 조합 과제를 평가하는 데이터·CAD·정책 자산을 제공한다.

근거: [공식 paper/abstract](https://journals.sagepub.com/doi/full/10.1177/02783649241276017) · [저자 project/code](https://functional-manipulation-benchmark.github.io/) · [공식 code](https://github.com/rail-berkeley/fmb). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 skill/전체 과제 성공 정의, object split, reset과 force/torque 접근은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

범용 pick-and-place 성능과 접촉 조립 능력을 구분할 benchmark를 보완한다.

### Dependency and Evolution

robomimic·FurnitureBench → FMB; HIL-SERL과 조립 평가 조건 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 object split에서 고정 skill 순서와 feedback 기반 전환을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

개별 skill 성공률이 같아도 조합 시 실패 복구·전이 조건이 전체 성공을 좌우하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
