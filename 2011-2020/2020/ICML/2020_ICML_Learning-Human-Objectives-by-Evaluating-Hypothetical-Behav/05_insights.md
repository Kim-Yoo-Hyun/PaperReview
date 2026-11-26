# Learning Human Objectives by Evaluating Hypothetical Behavior

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

가상 행동을 생성하고 평가를 받아 human objective를 추정한다.

Navigation·driving 성격의 simulated task를 평가한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v119/reddy20a.html) · [저자 project/code](https://github.com/rddy/ReQueST). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 가상 trajectory 실현 가능성, feedback 형태, model bias은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

C4에서 query 선택·reward refinement의 오래된 직접 선행이다.

### Dependency and Evolution

Preference-based RL → ReQueST → VLA reward audit.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

Reward uncertainty와 policy-relevant query selection을 같은 label budget으로 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 expert 비용에서 새 검수 선택이 task 성능을 개선하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
