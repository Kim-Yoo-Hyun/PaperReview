# VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

실제 rollout으로 action-conditioned video world model을 개선하고 그 synthetic rollout으로 VLA를 개선하는 반복 학습을 제안한다.

ICML abstract는 실제 robot의 여러 downstream task에서 base policy 및 synthetic-rollout 학습 효과를 비교한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v306/guo26i.html) · [저자 project/code](https://sites.google.com/view/vla-w). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 Policy update objective, 실패 data 구성, synthetic/real 혼합비와 evaluation leakage은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Current trend. 실제 rollout으로 world model의 failure coverage를 개선하고 synthetic rollout으로 policy를 개선하는 반복 구조다. 이미 등록된 Ctrl-World/WMPO와 연결해 model bias와 real-data budget을 비교한다. Abstract만으로 특정 RL optimizer를 단정하지 않는다.

### Dependency and Evolution

Ctrl-World → VLAW; WMPO/VLA-MBPO와 model-bias 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

Fixed world model, 반복 갱신 world model, real-data-only policy 학습을 동일 real-data budget으로 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

동일 real rollout budget에서 world model을 반복 갱신하는 것이 고정 model보다 실제 policy 성공률을 높이는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
