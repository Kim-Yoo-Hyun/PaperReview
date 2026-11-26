# DART: Noise Injection for Robust Imitation Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Paper-supported conclusion

전문가가 시연할 때 noise를 주입하고 학습 정책의 오류에 맞춰 noise 수준을 조절한다.

MuJoCo locomotion과 실제 Toyota HSR의 clutter grasping을 평가한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v78/laskey17a.html). 초록의 주장 범위이며 독립 재현 결과가 아니다.

## Researcher interpretation

### Why This Matters

복구 성공을 RL 고유 이득으로 해석하기 전 넘어야 할 강한 데이터 수집·모방 대안이다.

### Dependency and Evolution

DAgger·BC 분포 이동 → DART → VLA recovery·RL 데이터 수집 비교.

이는 개념적 읽기 연결이며 직접 citation 또는 검증된 derivation을 뜻하지 않는다.

### Assumptions and Failure Questions

noise 분포·전문가 회복 능력·개입 비용·train-test 교란.

논문이 실제 보고한 failure case로 간주하지 않는다.

### Minimal Comparison

동일 전문가 개입·시연 수로 정상 BC·교란 BC·RL을 비교한다.

### Falsifiable Question

VLA RL의 perturbation 내성은 복구 시연을 맞춘 DART식 BC와 비교해 남는가?

같은 정보·데이터·계산 조건에서 단순 대안이 차이를 설명하면 해당 확장 가설을 수정한다. 공식 CoRL abstract 및 저자 project/code 공개 확인. 공개 repository의 simulation 구현과 실제 HSR 재현 경로는 구별한다.
