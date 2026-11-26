# Successor Features for Transfer in Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Paper-supported conclusion

미래 feature 방문을 보상 가중치와 분리하고 generalized policy improvement로 기존 정책들을 재사용한다.

전이 성능 정리와 navigation·시뮬레이션 robot arm 실험을 보고한다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper/2017/hash/350db081a661525235354dd3e19b8c05-Abstract.html). 초록의 주장 범위이며 독립 재현 결과가 아니다.

## Researcher interpretation

### Why This Matters

보상 전이와 로봇 동역학 전이를 혼동하지 않게 하는 명확한 이론·로봇 비교 기준이다.

### Dependency and Evolution

UVFA·policy improvement → successor features → 목표/보상 전이와 cross-embodiment의 조건 비교.

이는 개념적 읽기 연결이며 직접 citation 또는 검증된 derivation을 뜻하지 않는다.

### Assumptions and Failure Questions

공유 동역학·보상 선형성·feature 근사·정책 coverage.

논문이 실제 보고한 failure case로 간주하지 않는다.

### Minimal Comparison

보상만 변경한 조건과 동역학까지 변경한 조건을 분리해 동일 전이 절차를 비교한다.

### Falsifiable Question

로봇이나 controller가 바뀔 때 같은 feature를 공유하는 것만으로 전이 보장이 남는가?

같은 정보·데이터·계산 조건에서 단순 대안이 차이를 설명하면 해당 확장 가설을 수정한다. 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.
