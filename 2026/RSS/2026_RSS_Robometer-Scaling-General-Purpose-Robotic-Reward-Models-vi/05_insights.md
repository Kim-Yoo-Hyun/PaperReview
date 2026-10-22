# Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Progress supervision과 trajectory comparison을 결합한다.

대규모 multi-robot 자료와 downstream 실제 robot RL을 보고한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p140.html) · [저자 project/code](https://robometer.github.io/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 policy version chronology, failure labels, reward training 중복, calibration은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

C4/C6의 reward·progress·평가 신호를 비교할 핵심 최신 baseline이다.

### Dependency and Evolution

PROGRESSOR·preference reward → Robometer → NSCORE.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 frozen policy rollout에서 progress/reward와 독립 outcome을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Reward 개선이 policy별 오류를 줄이는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
