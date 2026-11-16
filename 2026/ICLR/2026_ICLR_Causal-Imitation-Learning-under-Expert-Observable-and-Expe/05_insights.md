# Causal Imitation Learning under Expert-Observable and Expert-Unobservable Confounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

Trajectory history를 instrumental variable로 이용하는 conditional moment 기반 DML-IL을 제안한다.

MuJoCo를 포함한 연속 상태·행동 환경에서 causal IL baseline과 비교한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/4415e8cb0741bc0beb79b316f0856108-Abstract-Conference.html). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 instrument relevance/exclusion, 시간적 confounding, history 접근, imitation-gap 가정은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

VLA history 추가를 새 해결책으로 주장하기 전에 정보 비대칭과 도구변수 조건을 점검할 선행이다.

### Dependency and Evolution

Behavior cloning·causal IL → DML-IL; Delphic과 식별 가능/불가능 조건 비교.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

History의 instrument 유효성만 바꾼 환경에서 BC·memory BC·DML-IL을 비교한다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

History가 유효한 instrument가 아닌 경우 단순 memory policy와 DML-IL의 차이는 남는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
