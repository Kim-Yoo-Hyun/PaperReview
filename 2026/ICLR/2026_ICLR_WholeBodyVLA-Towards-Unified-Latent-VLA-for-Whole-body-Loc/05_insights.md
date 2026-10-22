# WholeBodyVLA: Towards Unified Latent VLA for Whole-body Loco-manipulation Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Unified latent VLA와 loco-manipulation-oriented low-level RL을 연결한다.

Humanoid loco-manipulation과 확장 task를 보고한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/ff7373914a96956f2a7cacbdf3b0b8d8-Abstract-Conference.html) · [저자 project/code](https://opendrivelab.com/WholebodyVLA). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 실행 가능한 codebase, latent supervision, controller budget은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

NaVILA 이후 VLA와 low-level RL의 역할을 비교할 NEXT다.

### Dependency and Evolution

RMA의 adaptation 및 NaVILA의 VLA/locomotion interface → WholeBodyVLA의 상체·이동 latent control을 비교한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 low-level controller에서 latent action 표현을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

상위 latent 표현의 이득과 low-level controller 개선을 분리할 수 있는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
