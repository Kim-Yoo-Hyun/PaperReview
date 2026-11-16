# Facet-0: A Robotic Foundation Model for Contact-Rich Precise Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Joint action–wrench proposal과 distributional critic으로 접촉 결과를 학습하며 bounded actor가 현장 적응한다.

세 embodiment의 force-synchronized corpus와 정밀 컴퓨터 조립 과제를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.01596) · [저자 project/code](https://pine-lab-ntu.github.io/facet-0/) · [공식 code](https://github.com/PINE-Lab-NTU/FACET). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 Frozen backbone/actor 경계, task adaptation 비용, 데이터 누출은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Action–wrench 예측·가치·RL 결합 자체의 중복을 점검할 직접 경쟁 선행이다.

### Dependency and Evolution

Flow VLA와 contact-selective credit, frozen representation 기반 적응을 연결한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 데이터·접촉 관측에서 action-only와 action/gain 학습을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Gain을 직접 학습하는 효과가 action–wrench 예측·bounded correction 이후에도 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
