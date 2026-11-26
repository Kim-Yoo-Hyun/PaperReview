# Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Paper-supported conclusion

여러 step 동안 실행되는 closed-loop option과 SMDP를 연결하고 중단·intra-option 학습을 분석한다.

시간 추상화의 이론과 학습·계획 예제를 다룬다. VLA chunk가 자동으로 option이라는 주장은 없다.

근거: [공식 paper/abstract](https://www.sciencedirect.com/science/article/pii/S0004370299000521). 초록의 주장 범위이며 독립 재현 결과가 아니다.

## Researcher interpretation

### Why This Matters

가변 chunk·재계획·중단을 해석할 기본 formulation을 보완하며 계층형 주제로 전환하라는 의미는 아니다.

### Dependency and Evolution

MDP·Q-learning → options/SMDP → action chunk·실행 중단·시간별 credit assignment.

이는 개념적 읽기 연결이며 직접 citation 또는 검증된 derivation을 뜻하지 않는다.

### Assumptions and Failure Questions

initiation·termination·closed-loop 조건·물리 시간 할인.

논문이 실제 보고한 failure case로 간주하지 않는다.

### Minimal Comparison

같은 행동열에서 고정 chunk와 상태 의존 종료를 분리해 discount·return의 정의를 대조한다.

### Falsifiable Question

고정 길이 open-loop chunk를 closed-loop option처럼 취급하면 어떤 가정이 깨지는가?

같은 정보·데이터·계산 조건에서 단순 대안이 차이를 설명하면 해당 확장 가설을 수정한다. 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.
