# HIQL: Offline Goal-Conditioned RL with Latent States as Actions

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Paper-supported conclusion

하나의 action-free 가치함수에서 latent subgoal 정책과 그 목표에 도달하는 하위 정책을 추출한다.

장시간 offline goal-reaching·영상 관측·action-free data 사용을 평가한다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2023/hash/6d7c4a0727e089ed6cdd3151cbe8d8ba-Abstract-Conference.html). 초록의 주장 범위이며 독립 재현 결과가 아니다.

## Researcher interpretation

### Why This Matters

공유 가치함수와 계층 정책을 단일 actor 공동 학습과 구별하고 장기 credit 문제의 강한 대안으로 비교한다.

### Dependency and Evolution

UVFA·IQL → HIQL → SHARSA/OGBench·VLA 장기 조작.

이는 개념적 읽기 연결이며 직접 citation 또는 검증된 derivation을 뜻하지 않는다.

### Assumptions and Failure Questions

goal relabeling·latent 목표 표현·subgoal 거리·action-free 데이터 범위.

논문이 실제 보고한 failure case로 간주하지 않는다.

### Minimal Comparison

같은 data/value/compute에서 평면 정책과 subgoal 정책의 horizon별 오류를 비교한다.

### Falsifiable Question

공유 critic을 개선한 효과는 실제로 짧아진 목표 horizon으로 설명되는가?

같은 정보·데이터·계산 조건에서 단순 대안이 차이를 설명하면 해당 확장 가설을 수정한다. 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다.
