# Policy invariance under reward transformations: Theory and application to reward shaping

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Paper-supported conclusion

상태 potential의 차이로 구성하는 보상 변환의 정책 보존 조건과 그 필요성을 분석한다.

정책 불변성 분석과 거리·부분 목표 potential의 학습 예제를 제시한다. VLA 평가 논문은 아니다.

근거: [공식 paper/abstract](https://people.eecs.berkeley.edu/~russell/papers/icml99-shaping.pdf). 초록의 주장 범위이며 독립 재현 결과가 아니다.

## Researcher interpretation

### Why This Matters

VLM progress·단계 보상·접촉 보상으로 목표를 변경하는지 판단할 공통 이론 원전이므로 CORE다.

### Dependency and Evolution

보상 설계·IRL → potential shaping → STARE-VLA 및 robot reward model의 주장 경계를 비교한다.

이는 개념적 읽기 연결이며 직접 citation 또는 검증된 derivation을 뜻하지 않는다.

### Assumptions and Failure Questions

할인율·종료 potential·Markov 상태·history 의존 보상.

논문이 실제 보고한 failure case로 간주하지 않는다.

### Minimal Comparison

작은 명시적 MDP에서 원 보상·potential 차이·그냥 progress 점수의 최적 행동을 대조한다.

### Falsifiable Question

부분 관측 VLA의 학습된 progress shaping은 timeout·목표 교체 아래에서도 같은 목적을 보존하는가?

같은 정보·데이터·계산 조건에서 단순 대안이 차이를 설명하면 해당 확장 가설을 수정한다. 저자 원문 abstract와 Russell의 ICML-99 publication 기록 확인. PDF는 웹에서 확인했으며 local cache는 저장하지 않았다. ACM endpoint는 403으로 접근 실패해 DOI를 추정하지 않았다.
