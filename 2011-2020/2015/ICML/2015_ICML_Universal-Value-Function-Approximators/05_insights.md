# Universal Value Function Approximators

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Paper-supported conclusion

상태와 목표를 입력으로 받는 가치함수와 분리된 embedding 학습을 제안하고 보상 기반 RL로 연결한다.

학습하지 않은 목표로 가치와 정책을 일반화하는 실험을 보고한다. 언어 지시나 다중 embodiment 보장은 아니다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v37/schaul15.html). 초록의 주장 범위이며 독립 재현 결과가 아니다.

## Researcher interpretation

### Why This Matters

HER·HIQL·목표 조건부 critic과 단일 VLA의 지시별 가치 표현을 이해하는 원전이므로 CORE다.

### Dependency and Evolution

TD/value approximation → UVFA → HER·HIQL·OGBench와 목표별 보존 진단.

이는 개념적 읽기 연결이며 직접 citation 또는 검증된 derivation을 뜻하지 않는다.

### Assumptions and Failure Questions

목표 표현·목표 holdout·목표별 coverage·value와 policy 일반화의 구분.

논문이 실제 보고한 failure case로 간주하지 않는다.

### Minimal Comparison

같은 상태의 두 목표에서 분리·공유 value와 목표별 행동 선택을 비교한다.

### Falsifiable Question

같은 관측에서 목표가 달라질 때 공유 가치 표현은 서로 다른 성공 행동을 보존하는가?

같은 정보·데이터·계산 조건에서 단순 대안이 차이를 설명하면 해당 확장 가설을 수정한다. 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.
