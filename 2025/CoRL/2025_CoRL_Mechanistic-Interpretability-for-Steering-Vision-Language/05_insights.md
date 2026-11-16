# Mechanistic Interpretability for Steering Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Transformer activation의 semantic 방향을 찾고 inference 때 activation steering으로 행동을 조절한다.

Pi0·OpenVLA를 LIBERO 및 UR5에서 평가한다고 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/haon25a.html). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 방향 추출 데이터, 개입 강도, 속도와 성공의 trade-off은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Instruction 대응이나 VLA 행동 교정을 연구할 때 fine-tuning 없는 직접 baseline이다.

### Dependency and Evolution

OpenVLA/π0 → activation steering → instruction 개입의 대조.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 checkpoint에서 semantic·random direction의 task/control 변화를 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Semantic 개입 효과가 같은 크기의 무작위·비의미 방향 개입보다 일관적인가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
