# SwitchVLA: Execution-Aware Task Switching for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Contact phase와 behavior-conditioned trajectory를 이용해 switching을 학습한다.

실행 중 task switching 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2506.03574) · [저자 project/code](https://switchvla.github.io/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 contact label, rollback 가정, 정식 venue status은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

D3의 일반 task interruption 주장을 제한하는 REFERENCE다.

### Dependency and Evolution

RT-H·Hi Robot의 task hierarchy → SwitchVLA의 execution-aware transition; VITA-E의 interruption/concurrency와 비교한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

가역·비가역 task를 나누어 switching 후 task damage를 측정한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

되돌릴 수 없는 접촉 이후에도 rollback이 적절한가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
