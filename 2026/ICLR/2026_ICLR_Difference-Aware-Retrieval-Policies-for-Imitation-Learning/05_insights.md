# Difference-Aware Retrieval Policies for Imitation Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

시연의 가까운 상태·행동 및 query와의 상대 차이를 이용하는 semi-parametric policy를 학습한다.

Continuous control과 manipulation, 고차원 시각 표현에서 BC와 비교한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8c2ecd140ebe227a531edc9a0c3b69d4-Abstract-Conference.html) · [저자 project/code](https://weirdlabuw.github.io/darp-site/) · [공식 code](https://github.com/WEIRDLabUW/darp). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 이웃 수, history 사용, retrieval 지연과 rollout split은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

학습 전 subset 선택과 실행 중 retrieval의 효과를 분리할 직접 대안이다.

### Dependency and Evolution

Behavior cloning → retrieval policy → DARP.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 시연·encoder에서 BC와 DARP를 비교하고 retrieval 시간까지 센다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Subset 선택 이득이 inference retrieval을 허용하면 줄어드는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
