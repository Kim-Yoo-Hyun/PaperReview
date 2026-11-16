# LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

물체·초기 상태·지시·환경 perturbation으로 일반화와 지시 의존성을 점검한다.

LIBERO 기반 변형 평가를 보고한다. 극단적 저하 수치의 task validity는 별도 본문 감사가 필요하다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2510.03827) · [저자 project/code](https://github.com/Zxy-MLlab/LIBERO-PRO). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 변경된 목표의 타당성, 언어 교란의 의미, v1/v2 차이은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

지시 교란 평가와 구현된 task의 유효성을 함께 점검할 비교 benchmark다.

### Dependency and Evolution

LIBERO → LIBERO-PRO/Plus → 유효성 통제 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

Goal/planner/evaluator를 먼저 맞춘 뒤 원본과 변형 task 성공을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Reachability·goal consistency를 확인한 perturbation에서도 성능 저하가 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
