# Learning Native Continuation for Action Chunking Flow Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Paper-supported conclusion

현재 근거는 [방법](./03_method.md)의 구성과 [평가](./04_evaluation.md)의 보고 범위다. 세부 수치·일반화 한계·재현 성공을 독립적으로 확인한 것은 아니다.

## Researcher interpretation

### Dependency and Evolution

ACT·Diffusion Policy와 RTC 이후 action interface를 이해할 NEXT다. Chunk queue나 지연으로 생긴 차이를 새로운 지시 이해/검색 효과로 혼동하지 않게 한다.

위 선행 연결은 개념적 비교이며 직접 citation 계보를 검증한 뜻은 아니다.

### Research Gap and Falsifiable Question

같은 추론 지연과 action budget에서 continuation 이득이 smoothness를 넘어 task success에도 유지되는가?

### Minimal Reproduction and Rejection Rule

먼저 schedule·지연 분포·실기 controller와 공개 Kinetix 구현의 차이를 확인한다. 같은 관측 주기·추론 예산·지연 조건에서 chunk continuation과 단순 chunk 실행을 비교한다. 성공률과 경계 연속성·소요 시간을 함께 보고, 지연이나 실행 빈도 차이만으로 설명되는 개선을 분리한다. 실제 재현·정책 비교는 미실행이며, 후속 실행은 호환 로컬 Docker에서 진행한다.
