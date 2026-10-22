# Can Vision-Language-Action Models Learn from Real-World Data Continually without Forgetting?

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

실환경 continual 학습에서 replay와 데이터 정규화 등 기본 recipe를 비교한다.

단일 팔과 양팔 실환경 continual learning을 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2605.26820). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 v3 변경점, normalization 범위, joint training compute, trial 수은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

E1의 실환경 단순 baseline과 compute-matched 비교에 필요한 연구다.

### Dependency and Evolution

Continual VLA → Memory Anchors와 실환경 baseline 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

Task 순서·normalizer·update 수를 고정하고 old/new task와 joint-training 기준을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 학습량에서 새로운 selector가 uniform replay보다 유리한가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
