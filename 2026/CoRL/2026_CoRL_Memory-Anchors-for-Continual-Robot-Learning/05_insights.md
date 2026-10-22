# Memory Anchors for Continual Robot Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

겹치는 latent representation에서 요구 action이 충돌하는 memory를 replay anchor로 사용한다.

LIBERO와 real-robot continual learning 평가를 보고한다.

근거: [공식 paper/abstract](https://openreview.net/forum?id=dSbtHPqFj9) · [저자 project/code](https://robot-adaptation.github.io/MemoryAnchors). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 latent layer, action normalization, task order, replay step scaling은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

E1의 action-conflict replay와 가장 가까운 직접 비교군이다.

### Dependency and Evolution

Experience replay·MIR → continual VLA → Memory Anchors.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 replay budget에서 uniform·MIR·anchor selection의 old/new task 성능을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

물리적 action 정렬 이후에도 latent conflict score가 uniform/MIR보다 유효한가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
