# ExecVLA: Following Fine-Grained Execution Constraints in Vision-Language-Action Models with Bi-Level Action Representation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

목표/실행 수준의 action representation과 reasoning 신호를 분리한다.

LIBERO와 Realman robot의 execution-constraint 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2603.17524). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 constraint label, evaluator geometry, KineVLA→ExecVLA version, 공개 checkpoint은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

C2의 수행 방식 지시 주장이 겹치는 직접 선행이며 KineVLA와 동일 identity다.

### Dependency and Evolution

VLA instruction alignment → ExecVLA/KineVLA → C2.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 목표에 상충하는 route/speed constraint를 주고 둘을 별도로 평가한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Task 성공을 고정한 뒤에도 새로운 방식 제약 준수의 이득이 있는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
