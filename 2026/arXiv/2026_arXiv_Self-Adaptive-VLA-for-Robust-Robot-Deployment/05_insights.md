# Self-Adaptive VLA for Robust Robot Deployment

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

실패 rollout context를 encoder와 AdaLN으로 주입하고 여러 trial의 token을 합친다.

정밀 bimanual·dexterous 작업의 actuation bias와 encoder offset 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.30092) · [저자 project/code](https://icefoxzhx.github.io/self-adaptive-vla/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 episode/trial 간 offset 유지, encoder 모델, expert action 보상은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

D1의 hardware-cause adaptation과 가장 가까운 NEXT 비교군이다.

### Dependency and Evolution

π0 계열 flow action policy → Self-Adaptive VLA의 rollout context; ReViP의 task-progress feedback과 적응 대상을 구별한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 관측·실패 trial 예산으로 static-context와 online history를 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

고정 offset 적응이 원인 전환에도 충분한가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
