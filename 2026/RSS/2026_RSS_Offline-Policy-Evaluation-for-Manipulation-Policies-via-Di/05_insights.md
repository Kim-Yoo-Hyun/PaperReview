# Offline Policy Evaluation for Manipulation Policies via Discounted Liveness Formulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Paper-supported conclusion

Task completion으로 평가를 정식화한 liveness Bellman operator와 conservative fixed point를 제안한다.

RSS abstract는 VLA·diffusion policy를 이용한 두 simulation 조작 과제를 명시한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p154.html). 초록의 주장 범위이며 독립 재현 결과가 아니다.

## Researcher interpretation

### Why This Matters

실험 rollout 종료와 실제 실패를 구별하고 가치 진단의 target을 정할 최신 기준이다.

### Dependency and Evolution

TD·Monte Carlo 평가 → liveness evaluation → VLA 제한된 rollout 해석.

이는 개념적 읽기 연결이며 직접 citation 또는 검증된 derivation을 뜻하지 않는다.

### Assumptions and Failure Questions

고정 정책·목표 predicate·유한 horizon·복구 구간·실제 성공과 진척의 차이.

논문이 실제 보고한 failure case로 간주하지 않는다.

### Minimal Comparison

같은 rollout의 truncation 길이를 바꾸어 TD·MC·liveness 순위와 완주 결과를 비교한다.

### Falsifiable Question

중간 복구 때문에 진척이 후퇴할 때 value 지표가 실제 성공 능력을 잘못 평가하는가?

같은 정보·데이터·계산 조건에서 단순 대안이 차이를 설명하면 해당 확장 가설을 수정한다. RSS official abstract의 두 simulation 과제를 기록한다. arXiv 초록의 추가 cloth demonstration은 venue 본문에서 동일성을 확인하기 전 평가 범위에 합치지 않았다.
