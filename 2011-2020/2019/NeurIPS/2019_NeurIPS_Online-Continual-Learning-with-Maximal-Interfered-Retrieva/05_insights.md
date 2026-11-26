# Online Continual Learning with Maximal Interfered Retrieval

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

예상 parameter update 뒤 손실이 많이 증가할 sample을 선택해 replay한다.

Continual learning benchmark에서 경험/생성 replay 비교를 보고한다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper/2019/hash/15825aee15eb335cc13f9b559f166ee8-Abstract.html) · [저자 project/code](https://github.com/optimass/Maximally_Interfered_Retrieval). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 virtual step, candidate memory budget, classification과 robot rollout의 차이은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

E1에서 loss/gradient interference를 신규 원리로 재주장하지 않게 하는 foundation이다.

### Dependency and Evolution

Experience replay → MIR → Memory Anchors/E1.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

Virtual-update 비용을 포함해 uniform·MIR·제안 score의 retention을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

Action 정렬 뒤 새 selector가 동일 비용의 MIR보다 유리한가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
