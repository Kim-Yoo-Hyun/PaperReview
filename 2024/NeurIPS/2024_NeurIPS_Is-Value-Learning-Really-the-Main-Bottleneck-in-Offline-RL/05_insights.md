# Is Value Learning Really the Main Bottleneck in Offline RL?

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Paper-supported conclusion

Value learning·policy extraction·test-state 일반화를 분리해 비교하고 policy 개선 대안을 분석한다.

Offline RL의 extraction 선택과 데이터 coverage·test-time 정책 개선을 실증 비교한다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2024/hash/8ffb4e3118280a66b192b6f06e0e2596-Abstract-Conference.html). 초록의 주장 범위이며 독립 재현 결과가 아니다.

## Researcher interpretation

### Why This Matters

단일 VLA critic 개선 후보가 actor 학습·coverage 효과를 놓치지 않도록 하는 핵심 원인 분석이다.

### Dependency and Evolution

IQL/AWAC·TD3+BC → policy extraction 진단 → WCM·FQL의 이득 분해.

이는 개념적 읽기 연결이며 직접 citation 또는 검증된 derivation을 뜻하지 않는다.

### Assumptions and Failure Questions

critic 고정·extraction 예산·평가 state coverage·test-time 최적화 비용.

논문이 실제 보고한 failure case로 간주하지 않는다.

### Minimal Comparison

같은 고정 critic에서 weighted BC와 behavior-constrained policy gradient만 바꾼다.

### Falsifiable Question

더 정확한 critic을 사용해도 action head가 그 정보를 정책으로 추출하지 못하는가?

같은 정보·데이터·계산 조건에서 단순 대안이 차이를 설명하면 해당 확장 가설을 수정한다. 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.
