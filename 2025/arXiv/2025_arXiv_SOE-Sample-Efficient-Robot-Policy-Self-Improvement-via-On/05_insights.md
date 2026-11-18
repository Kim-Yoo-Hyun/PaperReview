# SOE: Sample-Efficient Robot Policy Self-Improvement via On-Manifold Exploration

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Task 관련 latent를 학습하고 유효한 행동 manifold에서 탐색하며 human-guided exploration을 지원한다.

저자 project는 robomimic의 4개 simulation task와 mug hanging·toaster loading·lamp capping 실제 과제를 제시한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2509.19292) · [저자 project/code](https://ericjin2002.github.io/SOE/) · [공식 code](https://github.com/EricJin2002/SOE). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 Manifold 학습 데이터·추가 supervision·policy update 방식·안전 주장 조건은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

관계 조건 탐색이 일반 latent/on-manifold 탐색보다 필요한지 확인할 직접 baseline이다.

### Dependency and Evolution

정책 사전학습 → SOE latent exploration → StructRL/관계 조건 탐색을 비교한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

공통 policy·latent capacity·interaction budget에서 조건 없는 manifold와 관계 conditioning을 대조한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 backbone과 유효 행동 coverage에서 관계 조건이 latent exploration보다 이득을 주는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
