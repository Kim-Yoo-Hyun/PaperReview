# SAIL: Faster-than-Demonstration Execution of Imitation Learning Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

일관성·tracking·speed modulation·latency scheduling을 결합한다.

Simulation task와 실제 robot 플랫폼의 빠른 실행을 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/arachchige25a.html) · [저자 project/code](https://nadunranawaka1.github.io/sail-policy). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 target/command/torque 주기, motion 재표현, component ablation은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

E2에서 retiming·tracking·feedback 이득을 분해할 핵심 IL baseline이다.

### Dependency and Evolution

Diffusion Policy·ACT → SAIL → VLA 시간 표현.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

Reference 속도와 controller gain을 따로 바꾸고 success와 완료 시간을 공동 측정한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

동일 tracking controller에서 speed scheduling만의 기여가 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
