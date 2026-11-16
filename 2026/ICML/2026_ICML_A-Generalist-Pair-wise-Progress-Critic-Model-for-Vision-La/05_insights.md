# A Generalist Pair-wise Progress Critic Model for Vision-Language-Action Robots

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

단일 autoregressive 구조로 행동과 두 시점 사이의 진행 차이를 예측하고, 진행 판단을 RL 보상에 사용한다.

공식 abstract는 실제 로봇 RL 평가를 보고한다. 정확한 trial·baseline·수치는 최종 본문 확인 필요.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v306/zhang26if.html) · [저자 project/code](https://github.com/InternRobotics/VLAC). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 최종 ICML의 모델 크기·동일 weight 여부·reward/done model 및 PPO value의 분리는 미확인이다. 2025 preprint 설정을 최종본에 전사하지 않는다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

단일 VLA의 행동/가치/보상을 구분할 직접 선행이다. U2의 구조 통합 주장을 제한하며 U1의 state-value와 다른 target을 제공하므로 NEXT에 추가한다.

### Dependency and Evolution

개념 비교: OpenVLA → 행동·progress 통합; RL4VLA의 state-value critic과 역할을 구별한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

최종 학습 그래프의 weight sharing·freeze·reward 공급 경로를 확인한 뒤 독립 성공 판정과 자기 progress 점수의 변화를 분리한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

구조를 공유하는 것과 동일 가중치를 online 공동 갱신하는 것의 효과는 어떻게 구별되는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
