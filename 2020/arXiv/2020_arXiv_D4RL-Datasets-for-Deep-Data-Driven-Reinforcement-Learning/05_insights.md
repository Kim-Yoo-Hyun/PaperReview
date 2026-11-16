# D4RL: Datasets for Deep Data-Driven Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Paper-supported conclusion

사람·규칙 controller·정책 혼합·멀티태스크 데이터를 포함하는 offline RL benchmark와 평가 프로토콜을 제시한다.

다양한 데이터 수집 조건에서 offline 알고리즘을 비교한다. 데이터셋 전체가 실물 로봇 trajectory라는 뜻은 아니다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2004.07219). 초록의 주장 범위이며 독립 재현 결과가 아니다.

## Researcher interpretation

### Why This Matters

CQL·IQL·Cal-QL의 데이터 조건과 결과를 읽기 위한 표준 benchmark의 누락을 보완한다.

### Dependency and Evolution

Batch RL 평가 → D4RL → CQL/IQL·OGBench와 robot data 조건 비교.

이는 개념적 읽기 연결이며 직접 citation 또는 검증된 derivation을 뜻하지 않는다.

### Assumptions and Failure Questions

dataset version·terminal/timeout·normalized score·현행 API와 원본 데이터 호환.

논문이 실제 보고한 failure case로 간주하지 않는다.

### Minimal Comparison

실제 데이터 subset의 coverage·성공률·정책 혼합을 분리해 같은 budget의 BC/RL을 비교한다.

### Falsifiable Question

데이터 품질이 같아도 coverage·수집 정책 혼합이 VLA offline 학습의 비교 순서를 바꾸는가?

같은 정보·데이터·계산 조건에서 단순 대안이 차이를 설명하면 해당 확장 가설을 수정한다. arXiv v4와 공식 유지 repository 확인. 확인되지 않은 conference venue를 부여하지 않으며 현행 라이브러리의 실행 호환성을 보장하지 않는다.
