# RLVR-World: Training World Models with Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Decoded prediction의 검증 가능한 지표를 reward로 삼아 world model을 RL 후학습한다.

텍스트 환경의 상태 예측과 RT-1 영상 예측을 평가한다. 부록 표 12는 PushT 시뮬레이션에서 각 세계 모델을 CEM 계획기에 넣고 과제 성공률을 비교한다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b63a24a1832bd14fa945c71f535c0095-Abstract-Conference.html) · [저자 project/code](https://thuml.github.io/RLVR-World/) · [공식 code](https://github.com/thuml/RLVR-World). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 reward metric과 task 목표 정합성, planner의 model exploitation, 로봇 행동 평가 유무은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

VLA policy RL과 world model RL을 구분하며 예측 개선이 행동에 전달되는지 물을 비교 자료다.

### Dependency and Evolution

Dreamer·video world model과 RLVR의 최적화 대상을 비교한다..

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 planner·rollout budget에 MLE/RL world model을 각각 넣고 예측 지표와 실제 return을 함께 측정한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

영상 품질을 개선한 model이 동일 planner의 task success도 높이는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
