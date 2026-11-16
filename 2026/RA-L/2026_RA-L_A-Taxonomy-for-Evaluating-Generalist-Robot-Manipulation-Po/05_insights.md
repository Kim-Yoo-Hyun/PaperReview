# A Taxonomy for Evaluating Generalist Robot Manipulation Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

시각·의미·행동 변화를 분리하는 STAR-Gen taxonomy와 평가 지침을 제안한다.

Bridge V2 기반 정책과 ALOHA 2의 실로봇 사례를 비교한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2503.01238) · [저자 project/code](https://stargen-taxonomy.github.io/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 각 축의 동시 변화, base competence, in-domain adaptation과 평가 분할은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

VLA 일반화 주장을 시각 변화·언어 이해·행동 변화로 분해할 평가 formulation이다.

### Dependency and Evolution

OpenVLA·Bridge V2 → STAR-Gen; LIBERO-Plus와 perturbation 정의 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

초기 관측을 맞춘 지시 쌍을 만들고 행동 필요성·성공 판정을 독립 확인한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

시각 cue가 같고 필요한 행동만 다른 지시에서도 semantic generalization 이득이 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
