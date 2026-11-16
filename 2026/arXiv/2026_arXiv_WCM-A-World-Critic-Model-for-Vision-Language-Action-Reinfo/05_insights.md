# WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED` — 초록·명시한 project 근거. 전체 본문·구현 정독 및 사용자 읽기 완료가 아니다.

## Paper-supported conclusion

LeJEPA 기반 critic이 미래 latent state와 value를 함께 학습하여 시간 정보를 표현하도록 한다.

여러 VLA backbone과 simulation benchmark·실물 조작에서 평가한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2607.29613). 초록의 주장 범위이며 독립 재현 결과가 아니다.

## Researcher interpretation

### Why This Matters

공유 표현·가치 공동 학습 후보의 직접 경쟁 선행이므로 단순 world-model 보조 loss를 신규 기여로 재제안하지 않게 한다.

### Dependency and Evolution

GAE·value representation → WCM ↔ VLAC·단일 VLA 공동 학습 후보.

이는 개념적 읽기 연결이며 직접 citation 또는 검증된 derivation을 뜻하지 않는다.

### Assumptions and Failure Questions

critic/actor 가중치 공유·history 접근·latent target·on/off-policy 차이.

논문이 실제 보고한 failure case로 간주하지 않는다.

### Minimal Comparison

History·모델 크기·데이터를 맞춰 value-only, future-latent 보조, actor-shared gradient를 분리한다.

### Falsifiable Question

WCM의 개선은 critic의 temporal 정보인가, actor 표현의 공동 갱신인가?

같은 정보·데이터·계산 조건에서 단순 대안이 차이를 설명하면 해당 확장 가설을 수정한다. arXiv v1와 공식 repository의 configs/scripts/world_critic 존재 확인. 학회 acceptance 및 실제 구현 재현은 확인하지 않았다.
