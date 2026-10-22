# Flow Q-Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Flow-matching behavior model과 distilled one-step actor를 결합하여 value maximization과 expressive behavior regularization을 연결한다.

공식 abstract는 OGBench와 D4RL의 state/pixel offline 및 offline-to-online task 평가를 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v267/park25f.html) · [저자 project/code](https://seohong.me/projects/fql/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 Critic target, actor distillation loss, OOD action 제약과 online data 혼합비은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Foundation bridge. Expressive flow policy와 Q-learning/one-step actor를 연결한다. IQL/CQL 이후 flow-action RL과 Q-chunking 계열의 구현·비교 기준으로 중요하다. 평가가 곧 실제 robot VLA 학습을 입증하는 것은 아니다.

### Dependency and Evolution

Flow Matching + IQL/CQL → FQL → Q-chunking.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

OGBench manipulation 한 task에서 FQL과 IQL을 같은 data로 비교하고, distillation/regularization 변화에 따른 return·sample efficiency·latency를 확인한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 offline data와 online interaction 예산에서 one-step actor가 multistep flow policy의 표현력을 유지하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
