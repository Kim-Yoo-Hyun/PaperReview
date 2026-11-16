# Stable Language Guidance for Vision–Language–Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Paper-supported conclusion

현재 근거는 [방법](./03_method.md)의 구성과 [평가](./04_evaluation.md)의 보고 범위다. 세부 수치·일반화 한계·재현 성공을 독립적으로 확인한 것은 아니다.

## Researcher interpretation

### Dependency and Evolution

지시 수정·집합 지시·시연 검색 후보가 공유하는 언어 민감성의 NEXT 직접 대안이다. 같은 의미의 표현 차이를 새로운 task conflict로 해석하지 않도록 등록한다.

위 선행 연결은 개념적 비교이며 직접 citation 계보를 검증한 뜻은 아니다.

### Research Gap and Falsifiable Question

언어 의미를 유지하고 길이·추론 횟수를 맞춘 대조에서도 steering 이득이 단순 paraphrase ensemble 이후 남는가?

### Minimal Reproduction and Rejection Rule

먼저 semantic prior 제거 방식·추가 decode 비용·평가 instruction 분리를 확인한다. 의미가 같은 지시 변형에 대해 기본 정책, 단순 지시 정규화, semantic steering을 같은 비용 조건에서 비교한다. 정규화만으로 차이가 사라지면 별도 steering의 필요성을 재검토한다. 실제 재현·정책 비교는 미실행이며, 후속 실행은 호환 로컬 Docker에서 진행한다.
