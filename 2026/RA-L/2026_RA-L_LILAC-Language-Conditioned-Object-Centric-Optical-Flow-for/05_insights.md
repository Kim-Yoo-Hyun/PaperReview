# LILAC: Language-Conditioned Object-Centric Optical Flow for Open-Loop Trajectory Generation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Paper-supported conclusion

현재 근거는 [방법](./03_method.md)의 구성과 [평가](./04_evaluation.md)의 보고 범위다. 세부 수치·일반화 한계·재현 성공을 독립적으로 확인한 것은 아니다.

## Researcher interpretation

### Dependency and Evolution

Flow/geometry를 action으로 연결하는 REFERENCE다. 현재 frozen VLA 검색 실험의 직접 prerequisite는 아니므로 NEXT를 늘리기보다 표현·개방루프 비교가 필요할 때 찾도록 둔다.

위 선행 연결은 개념적 비교이며 직접 citation 계보를 검증한 뜻은 아니다.

### Research Gap and Falsifiable Question

같은 robot supervision과 초기 관측에서 flow 중간 표현이 직접 waypoint 예측보다 유리한 조건은 무엇이며 실행 중 변화에는 어떻게 대응하는가?

### Minimal Reproduction and Rejection Rule

먼저 publisher와 project의 loss/adapter 명칭 차이를 해소하고 2D→6-DoF 변환·embodiment별 calibration을 확인한다. 같은 초기 관측과 robot supervision에서 flow 중간 표현과 직접 waypoint 예측을 비교한다. Open-loop 결과를 실행 중 환경 변화에 대한 대응력으로 해석하지 않는다. 실제 재현·정책 비교는 미실행이며, 후속 실행은 호환 로컬 Docker에서 진행한다.
