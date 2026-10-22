# SPACE: Enabling Learning from Cross-Robot Data Toward Generalist Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Cartesian state delta를 예측하고 action adapter로 robot command로 변환한다.

Embodiment·동일 기종 개체·frequency/payload/gain 변화 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2606.24049) · [저자 project/code](https://haeone.site/space-website/). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 state delta 계산, adapter supervision, online 적응 자료, 실제 시간은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

E1/E2에서 정상적인 state-effect 표현과 dynamics adapter의 강한 대안이다.

### Dependency and Evolution

Octo·cross-embodiment action interfaces → SPACE.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 Cartesian displacement에서 direct command와 adapter를 비교하고 gain/frequency를 통제한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Adapter로 설명되지 않는 추가 물리 effect 정보가 존재하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
