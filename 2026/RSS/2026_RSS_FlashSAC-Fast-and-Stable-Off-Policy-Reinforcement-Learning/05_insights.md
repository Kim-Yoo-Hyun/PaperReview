# FlashSAC: Fast and Stable Off-Policy Reinforcement Learning for High-Dimensional Robot Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

가중치·feature·gradient norm을 제한하고 병렬 데이터와 replay coverage를 확대한다.

여러 simulator의 제어 과제와 실제 humanoid sim-to-real을 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p099.html) · [저자 project/code](https://github.com/Holiday-Robot/FlashSAC). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 상태/vision별 계산량, update-to-data 비율, 실제 로봇 전이 범위은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

새 VLA-RL 구조의 필요성을 판단할 때 참고할 강한 off-policy 학습 baseline이다.

### Dependency and Evolution

SAC·대규모 simulation RL을 잇는 학습 안정성 연구이며 직접 VLA 결과와는 구별한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

하나의 조작 환경에서 replay coverage와 norm 제한을 분리하고 sample·wall-clock 비용을 함께 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

동일 compute에서 critic 안정화만으로 새 표현 구조의 이득을 대체할 수 있는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
