# High-Dimensional Continuous Control Using Generalized Advantage Estimation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Paper-supported conclusion

가치함수를 이용한 지수 가중 advantage 추정으로 bias–variance를 조절하고 trust-region 정책·가치 갱신을 결합한다.

시뮬레이션의 이족·사족 보행과 기립 과제를 평가한다. 실제 로봇 검증으로 확대하지 않는다.

근거: [공식 paper/abstract](https://arxiv.org/abs/1506.02438). 초록의 주장 범위이며 독립 재현 결과가 아니다.

## Researcher interpretation

### Why This Matters

PPO 기반 VLA RL에서 advantage·bootstrap·시간 단위가 학습에 미치는 영향을 해석하기 위한 공통 원전이므로 CORE다.

### Dependency and Evolution

TD(λ)·policy gradient → GAE → PPO·SimpleVLA-RL의 advantage 구현을 비교한다.

이는 개념적 읽기 연결이며 직접 citation 또는 검증된 derivation을 뜻하지 않는다.

### Assumptions and Failure Questions

λ·γ의 시간 단위, truncation bootstrap, 가치함수 오차.

논문이 실제 보고한 failure case로 간주하지 않는다.

### Minimal Comparison

같은 trajectory에서 step/chunk bootstrap과 종료 mask를 고정해 advantage 및 gradient 차이를 비교한다.

### Falsifiable Question

Action chunk 경계를 바꾸면 동일 물리 시간의 advantage 추정도 달라지는가?

같은 정보·데이터·계산 조건에서 단순 대안이 차이를 설명하면 해당 확장 가설을 수정한다. ICLR 2016 공식 accepted conference list로 게재 확인. 2015 최초 preprint와 2018 v6를 별도 논문으로 만들지 않는다.
