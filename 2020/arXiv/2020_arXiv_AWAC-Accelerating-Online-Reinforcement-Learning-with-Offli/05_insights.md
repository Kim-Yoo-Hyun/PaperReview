# AWAC: Accelerating Online Reinforcement Learning with Offline Datasets

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Paper-supported conclusion

Dynamic programming과 advantage 기반 가중 최대우도 정책 갱신을 결합한다.

시뮬레이션과 실제 다지 손·서랍 열기·밸브 조작을 평가한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2006.09359). 초록의 주장 범위이며 독립 재현 결과가 아니다.

## Researcher interpretation

### Why This Matters

RL 이득이 성공 선택이나 weighted imitation으로 설명되는지 비교할 핵심 baseline이다.

### Dependency and Evolution

정책 iteration·가중 회귀 → AWAC → IQL·Cal-QL·VLA offline-to-online.

이는 개념적 읽기 연결이며 직접 citation 또는 검증된 derivation을 뜻하지 않는다.

### Assumptions and Failure Questions

advantage scale·weight clipping·replay 비율·새 데이터 수집 비용.

논문이 실제 보고한 failure case로 간주하지 않는다.

### Minimal Comparison

데이터·초기 정책·학습량을 맞춰 BC·success-only BC·AWAC·online RL을 대조한다.

### Falsifiable Question

같은 데이터에서 VLA 개선은 online 탐색보다 advantage 가중 모방으로 설명되는가?

같은 정보·데이터·계산 조건에서 단순 대안이 차이를 설명하면 해당 확장 가설을 수정한다. 저자 project·arXiv v6 확인. OpenReview forum은 browser challenge로 본문 접근 실패했고 공식 acceptance를 확인하지 못해 arXiv 2020으로 등록한다. Project의 code 링크는 식별했으나 해당 경로 직접 fetch는 실패했다.
