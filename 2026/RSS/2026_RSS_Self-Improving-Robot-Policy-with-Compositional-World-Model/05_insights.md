# Self-Improving Robot Policy with Compositional World Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Multi-view controllable dynamics와 progress value model을 분리하여 imagined rollout에서 advantage를 만들고 policy를 개선한다.

RSS abstract는 dynamic brick sorting, backpack packing, box closing의 세 real-world task 평가를 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p012.html) · [저자 project/code](https://github.com/OpenDriveLab/RISE). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 Progress label 생성, failure coverage, value calibration과 real rollout 예산은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Current trend. Multi-view dynamics와 progress value를 분리하여 imagined rollout의 advantage를 만든다. VLA-MBPO/WMPO와 reward/value 신뢰도 및 real-robot transfer를 비교할 가치가 있다.

### Dependency and Evolution

WMPO/TD-MPC2 → RISE; VLA-MBPO/VLAW와 world-model feedback 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

고정 dynamics 아래 progress-value 구성과 rollout horizon을 바꾸고 imagined score와 real success의 일치도를 측정한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Progress value의 편향이 큰 실패 상태에서도 imagined improvement가 실제 성공률로 이어지는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
