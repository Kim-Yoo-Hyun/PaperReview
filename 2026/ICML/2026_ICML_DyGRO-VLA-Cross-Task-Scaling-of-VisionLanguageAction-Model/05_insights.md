# DyGRO-VLA: Cross-Task Scaling of Vision–Language–Action Models via Dynamic Grouped Residual Optimization

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Cross-task latent representation과 mixture-of-RL-residuals를 이용한 두 단계 grouped residual optimization을 제안한다.

ICML abstract는 LIBERO, RoboTwin2와 real-world 평가 및 multitask/distribution-shift 조건을 명시한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v306/lin26af.html) · [저자 project/code](https://github.com/EDEM-AI/DyGRO-VLA). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 Task grouping, residual routing, representation loss와 unseen split leakage은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Current trend. RL fine-tuning 중 task-specific overfitting을 줄이는 것이 연구 질문일 때 RL4VLA/ConRFT와 비교한다. 새 architecture라는 이유만으로 CORE로 올리지는 않는다.

### Dependency and Evolution

ConRFT/SimpleVLA-RL + RL4VLA generalization → DyGRO-VLA.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 base VLA에서 standard RL과 DyGRO-VLA를 비교하고 seen/unseen task 성공률과 representation 변화·추론 비용을 기록한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

동일 multitask rollout budget에서 residual RL이 일반 fine-tuning보다 unseen-task retention을 개선하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
