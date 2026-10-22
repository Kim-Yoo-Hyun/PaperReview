# DialogVLA: Bridging Reasoning Action in Bimanual Manipulation via Parallel Mixture-of-Experts

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Structured dialog와 parallel skill/arm MoE가 flow action expert를 조건화한다.

저자 project는 RoboTwin, RoboCasa GR1 및 실제 양팔 평가를 제시한다.

근거: [공식 paper/abstract](https://jjjenghi.github.io/dialogvla/) · [저자 project/code](https://jjjenghi.github.io/dialogvla/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 공식 proceedings, 원문 공개, source version, code release은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

D3 양팔 role reasoning의 중복을 피할 REFERENCE다. IROS 2026은 저자 표기이며 공식 채택 미확인이다.

### Dependency and Evolution

VoxAct-B의 acting/stabilizing 역할 → DialogVLA의 per-arm reasoning/routing; GR00T 계열 양팔 action policy와 비교한다.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 양팔 task에서 role routing 제거 ablation을 대조한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

명시적 arm role이 같은 입력의 단순 policy보다 필요한가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
