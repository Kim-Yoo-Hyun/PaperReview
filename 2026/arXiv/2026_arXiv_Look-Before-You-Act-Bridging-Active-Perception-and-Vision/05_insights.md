# Look Before You Act: Bridging Active Perception and Vision-Language-Action Models via Observation-Aligned Data Adaptation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Active perception으로 관측을 맞추고 정렬된 continuation 자료로 adaptation한다.

LIBERO와 실제 robot manipulation을 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2610.23378). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 camera 행동 비용, state change, 성공 continuation 선택, data budget은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

C1/D1의 능동 관측·관측 정렬 주장과 직접 충돌한다.

### Dependency and Evolution

Active perception·VLA adaptation → ActiveAlign.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

같은 policy에서 immediate/look/wait와 matched continuation adaptation을 분리한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

추가 정렬 데이터 없이도 look 행동의 이득이 있는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
