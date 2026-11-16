# A process-centric manipulation taxonomy for the organization, classification and synthesis of tactile robot skills

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

전문가의 process specification을 taxonomy와 parametric tactile skill로 연결한다.

산업 응용의 여러 tactile skill과 목표 pose 교란을 실로봇에서 평가한다.

근거: [공식 paper/abstract](https://www.nature.com/articles/s42256-025-01045-3). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 전문가 specification 비용, grasp/접촉 가정, skill 선택과 저수준 controller 기여은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

언어 기반 skill 조합과 전문가가 명시한 물리적 요구·종료 조건을 비교할 참조다.

### Dependency and Evolution

Impedance control·skill library → process taxonomy; tactile VLA의 제어 경계와 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 skill/controller에 process 조건과 언어 selector를 각각 연결해 전환 오류를 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

같은 공정 정보를 제공할 때 learned selector의 이득이 명시적 skill 조건을 넘는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
