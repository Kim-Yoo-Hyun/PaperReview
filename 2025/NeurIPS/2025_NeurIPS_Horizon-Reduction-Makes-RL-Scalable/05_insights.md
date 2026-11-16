# Horizon Reduction Makes RL Scalable

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Paper-supported conclusion

Horizon 감소 기법을 비교하고 짧은 유효 결정 길이를 활용하는 SHARSA를 제안한다.

다양한 긴 목표 과제의 scaling을 비교한다. 모든 online VLA RL의 원인으로 일반화하지 않는다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0c66099070429b9b49ad8bb19c740c22-Abstract-Conference.html). 초록의 주장 범위이며 독립 재현 결과가 아니다.

## Researcher interpretation

### Why This Matters

Chunk 길이·목표 분해와 데이터 scaling의 효과를 분리할 최신 기준 연구다.

### Dependency and Evolution

Options·HIQL·OGBench → horizon reduction → VLA chunk/return 설계.

이는 개념적 읽기 연결이며 직접 citation 또는 검증된 derivation을 뜻하지 않는다.

### Assumptions and Failure Questions

유효 결정 길이·coverage·데이터 크기·학습 계산량·물리 시간.

논문이 실제 보고한 failure case로 간주하지 않는다.

### Minimal Comparison

데이터·물리 시간·모델 크기를 맞춰 n-step return과 정책 chunk를 독립 변화시킨다.

### Falsifiable Question

VLA RL의 chunk 개선은 표현 변화보다 유효 credit horizon 감소로 설명되는가?

같은 정보·데이터·계산 조건에서 단순 대안이 차이를 설명하면 해당 확장 가설을 수정한다. 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.
