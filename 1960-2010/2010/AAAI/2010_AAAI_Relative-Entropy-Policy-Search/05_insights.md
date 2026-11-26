# Relative Entropy Policy Search

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Paper-supported conclusion

Relative entropy 제약으로 정책 개선을 제한하고 명시적 갱신을 도출한다.

소규모 MDP, Mountain Car와 모의 로봇 탁구에서 평가했다. 탁구 실험에서는 타구 성공 보상으로 동작 프리미티브를 선택했다.

근거: [공식 paper/abstract](https://ojs.aaai.org/index.php/AAAI/article/view/7727). 초록의 주장 범위이며 독립 재현 결과가 아니다.

## Researcher interpretation

### Why This Matters

TRPO·MPO·KL 제약의 개념 계보를 보완할 원전이며 현재 공통 정독은 GAE/PPO를 우선한다.

### Dependency and Evolution

정보 제약 policy search → REPS·MPO/TRPO → VLA 보존 regularization 비교.

이는 개념적 읽기 연결이며 직접 citation 또는 검증된 derivation을 뜻하지 않는다.

### Assumptions and Failure Questions

KL 방향·분포 제약·sample 추정·실제 행동 변화.

논문이 실제 보고한 failure case로 간주하지 않는다.

### Minimal Comparison

같은 목표 개선 수준에서 KL 방향·상태 분포를 바꾸고 미학습 목표 행동을 비교한다.

### Falsifiable Question

같은 KL 수치도 제약을 적용한 상태 분포가 달라지면 행동 보존이 달라지는가?

같은 정보·데이터·계산 조건에서 단순 대안이 차이를 설명하면 해당 확장 가설을 수정한다. 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.
