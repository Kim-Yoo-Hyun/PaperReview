# Same Path, Less Time: Training-Free Fast Execution of Vision-Language-Action Models under Inference Latency

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Frozen chunk policy에 경로 유지 time scaling을 적용해 비동기 추론과 실행 속도를 맞춘다.

LIBERO와 LIBERO-Dynamic에서 지연을 주입해 성공률과 task throughput을 비교한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2611.01390). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 미확인 항목: 실제 지연과 주입 지연·동작 제한·gripper 동기화·실제 로봇 전이.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

제어 주기 학습 전에 넘어야 할 학습 없는 실행 대안이며 예비 timing 질문의 비교 자료다.

### Dependency and Evolution

RTC 비동기 실행·action chunking·CAT 물리 시간 표현과 학습/실행 단계의 효과를 분리한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 frozen 정책에서 stop-and-wait·비동기1배속·PTS를 같은 지연과 성공/시간으로 대조한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

표현 학습의 추가 이득이 같은 decoder·latency·gripper 규칙의 단순 time scaling 이후 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
