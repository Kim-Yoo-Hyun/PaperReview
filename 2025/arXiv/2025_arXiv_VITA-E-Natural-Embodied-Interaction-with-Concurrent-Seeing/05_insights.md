# VITA-E: Natural Embodied Interaction with Concurrent Seeing, Hearing, Speaking, and Acting

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Active/Standby dual-model과 system command token을 사용한다.

Humanoid platform의 동시 interaction을 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2510.21817) · [저자 project/code](https://lxysl.github.io/VITA-E/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 명령 token timing, rollback 범위, ICLR acceptance 미확인은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

D3의 concurrency 자체를 기여로 주장하지 않게 하는 REFERENCE다.

### Dependency and Evolution

Hi Robot의 상위 지시 처리 → VITA-E의 concurrent control; SwitchVLA의 physical switching과 시스템 경계를 비교한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

중단 latency와 task 재개 성공을 별도 metric으로 측정한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Interruption responsiveness가 physical recovery의 성공까지 설명하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
