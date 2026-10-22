# HiMoE-VLA: Hierarchical Mixture-of-Experts for Generalist Vision-Language-Action Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Action-space별 expert와 공유 처리의 계층적 mixture를 구성한다.

CALVIN·LIBERO 및 실제 로봇 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2512.05693) · [저자 project/code](https://github.com/ZhiyingDu/HiMoE-VLA). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 routing에 쓰는 robot ID, contrastive objective, load balance, parameter 예산은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

E1에서 물리 action 충돌을 단순 expert 분리와 구별할 직접 REFERENCE다.

### Dependency and Evolution

Octo·RDT-1B → embodiment-specific routing → E1.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

Dense/shared와 expert 분리를 같은 domain split에서 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

동일 parameter·데이터 예산에서 routing 이득이 action 정렬 이후에도 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
