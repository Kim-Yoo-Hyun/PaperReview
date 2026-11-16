# Robo-ABC: Affordance Generalization Beyond Categories via Semantic Correspondence for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Human video의 affordance memory에서 유사 물체를 찾고 semantic correspondence로 contact point를 옮긴다.

시각 affordance 추정과 실세계 cross-category grasping을 보고한다.

근거: [공식 paper/abstract](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5748_ECCV_2024_paper.php) · [저자 project/code](https://tea-lab.github.io/Robo-ABC/) · [공식 code](https://github.com/TEA-Lab/Robo-ABC). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 2D/3D lifting, grasp 실행기, source별 수치 차이은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

Semantic representation을 실제 contact/action에 연결하는 비교용 3D/affordance 지원 연구다.

### Dependency and Evolution

Semantic correspondence → Robo-ABC → action-valid contact transfer.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 object에서 retrieval 정확도와 실제 reachable grasp 성공을 분리 측정한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

의미 대응점이 비슷해도 물리적으로 실행 가능한 contact인가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
