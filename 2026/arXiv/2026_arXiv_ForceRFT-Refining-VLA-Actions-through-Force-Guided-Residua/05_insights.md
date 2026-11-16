# ForceRFT: Refining VLA Actions through Force-Guided Residual Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Frozen SmolVLA prior의 동작을 wrist-feedback residual RL로 보정하며 human correction과 autonomous TD를 분리한다.

실제 plug·ring-on-peg·wiping에서 residual imitation을 포함한 기준선과 비교한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.22840). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 개입 경계, 데이터 예산, force 관측 주기와 base chunk 비용은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

RL 이득이 성공 데이터 선택·추가 imitation으로 설명되는지 판단할 직접 선행이다.

### Dependency and Evolution

Residual RL·힘 피드백과 VLA chunk 실행을 연결하는 경쟁 구조다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 데이터에서 residual imitation/RL 및 feedback 제거를 교차 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

실행 중 피드백의 이득과 value-guided 최적화의 이득을 분리할 수 있는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
