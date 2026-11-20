# CoRE-VLA: Towards Scalable and Robust Vision-Language-Action Modeling via Conditional Routing of Experts

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Sensor availability와 task intent를 이용해 sparse expert를 routing한다.

LIBERO, RoboCasa GR1, 실제 dual-arm 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2607.03693) · [저자 project/code](https://arxiv.org/abs/2607.03693). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 v2 depth degradation 평가, availability indicator, 공식 CoRL 채택 확인은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

D1의 modality robustness와 직접 겹치는 NEXT다. 카메라 복원 CoRe-VLA와 다른 논문이다.

### Dependency and Evolution

Generalist VLA의 fixed sensor interface → Conditional Routing CoRE-VLA; AT-VLA의 adaptive tactile injection과 정보 가정을 비교한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

Known missingness와 present-but-corrupt 조건을 같은 정보로 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Availability가 알려지지 않은 오류에서도 routing이 충분한가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
