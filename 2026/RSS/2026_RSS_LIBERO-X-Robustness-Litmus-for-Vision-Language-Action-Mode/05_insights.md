# LIBERO-X: Robustness Litmus for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Paper-supported conclusion

현재 근거는 [방법](./03_method.md)의 구성과 [평가](./04_evaluation.md)의 보고 범위다. 세부 수치·일반화 한계·재현 성공을 독립적으로 확인한 것은 아니다.

## Researcher interpretation

### Dependency and Evolution

LIBERO·LIBERO-Plus·VLABench 이후 복합 shift와 목표 다양성을 비교할 NEXT benchmark다. 같은 scene의 다른 goal을 다루는 연구에서 기존 평가 범위를 확인하는 데 필요하다.

위 선행 연결은 개념적 비교이며 직접 citation 계보를 검증한 뜻은 아니다.

### Research Gap and Falsifiable Question

동일 scene·target support에서 시각 교란과 의미상 같은 지시 변형이 검색 선택과 실제 성공에 주는 영향을 분리할 수 있는가?

### Minimal Reproduction and Rejection Rule

먼저 train/evaluation scene 중복·difficulty별 sample 수·init state 공개 범위·predicate 정의를 확인한다. 같은 scene과 target에서 시각 교란과 의미를 보존한 지시 변형을 각각 적용하는 paired 진단을 제안한다. 결합 교란의 결과만으로 개별 원인이나 검색 방법의 강건성을 주장하지 않는다. 실제 재현·정책 비교는 미실행이며, 후속 실행은 호환 로컬 Docker에서 진행한다.
