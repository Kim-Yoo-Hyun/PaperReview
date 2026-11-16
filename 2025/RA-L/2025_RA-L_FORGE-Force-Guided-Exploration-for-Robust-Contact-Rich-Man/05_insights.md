# FORGE: Force-Guided Exploration for Robust Contact-Rich Manipulation Under Uncertainty

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Force threshold와 dynamics randomization으로 sim-to-real 접촉 정책을 학습하고 성공을 예측한다.

삽입·gear meshing·nut threading과 snap-fit/다단계 조립을 보고한다.

근거: [공식 paper/abstract](https://ieeexplore.ieee.org/document/10925874/) · [저자 project/code](https://noseworm.github.io/forge/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 pose uncertainty 범위, gain randomization, 독립 실환경 trials은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

VLA의 추가 복잡도 전에 넘어야 할 비-VLA 접촉 RL 기준선이다.

### Dependency and Evolution

Impedance control·domain randomization 기반 RL을 contact VLA의 단순 대안으로 연결한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 관측·force ceiling·환경 비용의 비-VLA RL과 VLA RL을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

강한 force-conditioned RL 대비 VLA prior의 이득이 과제/언어 전이에 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
