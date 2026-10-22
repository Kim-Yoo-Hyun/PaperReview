# OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Contact/thermal/fluid signal을 damage로 변환하는 DamageSim과 damage-aware household task benchmark를 제공한다.

RSS abstract는 OmniGibson과 RoboCasa 구현, safer demonstration, damage-conditioned IL/RL, VLA safety 및 sim-to-real use case를 설명한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p098.html) · [저자 project/code](https://robin-lab.cs.utexas.edu/oopsieverse/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 Damage threshold/단위, simulator fidelity, user preference와 real-world damage validation은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Benchmark. Task success와 물리적 damage를 분리하고 damage-aware IL/RL 및 VLA 평가를 지원한다. 기존 safety/recovery 흐름에 contact·thermal·fluid damage라는 구체적인 평가 축을 보충한다.

### Dependency and Evolution

Recovery RL/LIBERO-Safety → OopsieVerse; reward와 physical damage 구분.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 VLA checkpoint와 task에서 task-only와 damage-aware evaluation을 비교하고 성공 여부와 damage를 별도 보고한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Task success를 유지하는 policy도 damage 비용을 포함하면 비교 순위가 달라지는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
