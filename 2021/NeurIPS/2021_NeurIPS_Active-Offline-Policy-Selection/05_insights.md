# Active Offline Policy Selection

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

OPE로 초기화하고 policy similarity 기반 Bayesian 선택으로 다음 평가를 배분한다.

여러 benchmark와 다수 후보 정책의 selection 효율을 보고한다.

근거: [공식 paper/abstract](https://papers.nips.cc/paper_files/paper/2021/hash/cec2346566ba8ecd04bfd992fd193fb3-Abstract.html). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 kernel 입력, adaptive reuse, candidate chronology, online budget은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

C6에서 OPE+능동 online 평가라는 넓은 방법의 직접 선행이다.

### Dependency and Evolution

Offline RL·OPE → AOPS → active robot evaluation.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

동일 후보 집합에서 OPE-only·uniform·AOPS 계열을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

새 checkpoint 선택은 같은 prior·interaction budget에서 더 좋은 정책을 고르는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
