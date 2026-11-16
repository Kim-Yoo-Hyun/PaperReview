# Causal World Modeling for Robot Control

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Paper-supported conclusion

RSS abstract의 CauVA는 autoregressive MoT로 frame/action을 처리하고 KV history와 noisy latent augmentation을 사용한다.

시뮬레이션과 실제 장시간·정밀·변형체 조작을 평가한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p016.html). 초록의 주장 범위이며 독립 재현 결과가 아니다.

## Researcher interpretation

### Why This Matters

Architecture 통합과 RL 공동 갱신을 구별할 world-action 비교 대상으로 보완한다.

### Dependency and Evolution

영상 world model·Diffusion Policy → frame/action 공동 모델 → 단일 VLA RL과의 목적함수 차이.

이는 개념적 읽기 연결이며 직접 citation 또는 검증된 derivation을 뜻하지 않는다.

### Assumptions and Failure Questions

예측/행동 gradient 경로·추론 history·실제 피드백·버전별 모델 명칭.

논문이 실제 보고한 failure case로 간주하지 않는다.

### Minimal Comparison

동일 action head에서 예측 보조 loss와 value loss를 분리하여 표현·행동 효과를 비교한다.

### Falsifiable Question

미래 예측을 공유하는 표현이 RL 가치 학습에 유용한 정보를 보존하는가?

같은 정보·데이터·계산 조건에서 단순 대안이 차이를 설명하면 해당 확장 가설을 수정한다. 공식 RSS abstract만을 canonical scope로 사용한다. 같은 제목의 arXiv2601.21998은 LingBot-VA와 다른 저자 구성·설계를 표기하므로 version mapping을 확정하지 않았고 arXiv ID/code를 자동 합치지 않았다. 별도 중복 등록도 하지 않았다.
