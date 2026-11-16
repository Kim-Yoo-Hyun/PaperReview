# Tune to Learn: How Controller Gains Shape Robot Policy Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Paper-supported conclusion

정책과 제어 동역학의 상호작용을 바탕으로 BC·RL·sim-to-real에서 gain regime을 비교한다.

여러 과제·embodiment에서 학습 방식에 따라 gain 선호가 달라지는 결과를 보고한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p139.html). 초록의 주장 범위이며 독립 재현 결과가 아니다.

## Researcher interpretation

### Why This Matters

접촉 VLA RL의 이득을 baseline gain 튜닝과 분리해야 함을 보이는 직접 선행이다.

### Dependency and Evolution

Impedance control → gain별 learnability 분석 → CompVLA·CONTACT-RL 공정 비교.

이는 개념적 읽기 연결이며 직접 citation 또는 검증된 derivation을 뜻하지 않는다.

### Assumptions and Failure Questions

gain 단위·controller rate·policy 반응·hyperparameter 예산·sim-to-real 차이.

논문이 실제 보고한 failure case로 간주하지 않는다.

### Minimal Comparison

고정 gain grid와 학습 gain을 같은 정책·데이터·튜닝 예산에서 비교한다.

### Falsifiable Question

학습된 compliance의 성능 향상은 같은 비용의 고정 gain 튜닝 뒤에도 남는가?

같은 정보·데이터·계산 조건에서 단순 대안이 차이를 설명하면 해당 확장 가설을 수정한다. RSS의 Shape 제목을 사용하고 저자 페이지의 Affect 제목은 alias로 연결한다. Workshop award를 RSS 수상으로 기록하지 않는다.
