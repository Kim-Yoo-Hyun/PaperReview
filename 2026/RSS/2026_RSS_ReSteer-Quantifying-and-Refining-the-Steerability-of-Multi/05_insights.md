# ReSteer: Quantifying and Refining the Steerability of Multitask Robot Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> Source audit: 공식 abstract/project 수준; 실제 정독 및 코드 실행은 미확인.

## Paper-supported conclusion

### What the Source Supports

상태별 task steerability를 측정하고, 전환이 어려운 상태의 추정·전환 구간 데이터 생성·정책 self-refinement를 연결한다.

LIBERO와 실제 로봇의 지시 전환을 평가한다. 공개 repository는 LIBERO 평가·데이터 생성 경로를 제공하지만 로컬 native 실행은 아직 확인하지 않았다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p143.html) · [저자 project/code](https://resteer-vla.github.io/) · [공식 code](https://github.com/ChenZhenY/ReSteer). 이는 논문의 abstract/project 주장 범위이며 독립 재현 결과가 아니다.

### Evidence Boundary

Exact assumptions·negative results·transfer limits는 본문 확인 필요. 특히 steerability score의 분모·switch timing·초기 능력, estimator와 실제 성공의 관계, 데이터 생성 비용, 제약 유지·철회가 평가에 포함되는 범위은 아직 확정하지 않았다.

## Researcher interpretation

### Reusable Lesson in the Robotics Loop

현재 부분 지시 수정 후보의 기본 switching 선행이자 최소 실행의 직접 prerequisite다. 단순 task switch나 행동 큐 교체를 신규 기여로 삼지 않도록 NEXT에 추가한다.

### Dependency and Evolution

OpenVLA·π0 계열의 언어 조건 정책 → ReSteer의 상태별 전환 평가; Hi Robot의 문맥 해석과 비교; Causeway의 접근 가능성 복구와 구별.

이 연결은 개념적 읽기·비교 경로다. 직접 citation 또는 검증된 derivation 관계라는 뜻은 아니다.

### Minimal Reproduction

기존 R8 단일 지시 전환 IO를 Docker에서 먼저 확인한다. 이후 같은 상태에서 전체 재명시·규칙 갱신·oracle 지시를 비교하는 것은 별도 연구 설계이며 아직 실행하지 않았다.

실행 전 source의 data split, checkpoint, reward·reset 접근과 metric 정의를 고정한다. 아직 실행한 실험은 없다.

### Research Gap and Falsifiable Question

기본 task switching이 가능한 상태에서도 부분 수정으로 유지·철회해야 할 제약을 전체 이력 재명시가 충분히 처리하는가?

**Reject / revise:** 위 matched comparison에서 목표 성능이나 검증하려는 이득이 재현되지 않으면 가설을 기각한다. 추가 data·privileged input·compute 차이로만 설명되면 방법 효과의 주장을 수정한다.
