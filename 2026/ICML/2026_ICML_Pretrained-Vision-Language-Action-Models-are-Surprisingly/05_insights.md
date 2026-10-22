# Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

사전학습과 소량 experience replay의 망각 억제 효과를 분석한다.

순차 robot task의 학습·망각 비교를 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v306/liu26bu.html) · [저자 project/code](https://continual-vlas.github.io/forget-me-not/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 pretraining 중복, replay 비율, old-task 평가와 모듈별 동결은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

E1에서 복잡한 replay selector 전에 확인할 강한 단순 기준이다.

### Dependency and Evolution

OpenVLA·Octo → continual VLA → Memory Anchors.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 초기 checkpoint·task 순서·update 수로 naive fine-tuning과 uniform replay를 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 replay 예산에서 새 selector의 이득이 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
