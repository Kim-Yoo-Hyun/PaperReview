# SAGA: Open-World Mobile Manipulation via Structured Affordance Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Paper-supported conclusion

현재 근거는 [방법](./03_method.md)의 구성과 [평가](./04_evaluation.md)의 보고 범위다. 세부 수치·일반화 한계·재현 성공을 독립적으로 확인한 것은 아니다.

## Researcher interpretation

### Dependency and Evolution

VoxPoser·Mobile ALOHA와 구조적 3D grounding을 잇는 NEXT다. 다양한 로봇을 다룬다는 목표에서 의미 표현과 embodiment별 제어의 경계를 비교한다.

위 선행 연결은 개념적 비교이며 직접 citation 계보를 검증한 뜻은 아니다.

### Research Gap and Falsifiable Question

같은 3D 관측과 skill budget에서 affordance 표현의 이득이 목표 위치를 직접 전달하는 단순 방식 이후에도 남는가?

### Minimal Reproduction and Rejection Rule

먼저 affordance 생성 오차·정책이 받는 정답 정보·whole-body action 공간을 확인한다. 같은 관측·제어기에서 추정 affordance를 사용하는 경우와 단순 geometry 대안을 비교하고, 정답 affordance는 진단 상한으로만 둔다. 정답 정보 조건에서만 이득이 생기면 실제 추정 표현의 효과로 확대하지 않는다. 실제 재현·정책 비교는 미실행이며, 후속 실행은 호환 로컬 Docker에서 진행한다.
