# EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

## Paper-supported conclusion

EXPO 계열의 editor와 VLA를 함께 갱신하는 chunk 수준 후학습을 사용한다. 공개 update_actor는 actor.train_step을 호출한다.

CoRL accepted list와 arXiv v1/code를 별도로 확인했다. 최종본 동일성·native 실행·독립 release 교체 효과는 미검증이다.

근거: [지정 본문](https://arxiv.org/html/2605.25477v1) — §4.2–4.3 / Appendix C; expo_ft.py update_actor/_update_jit. Code 검토 revision: `21fe3d3b7d913c80836496817965932f49e0aedf`; 실행하지 않았다.

## Researcher interpretation

### Novelty and Dependency

현재 VLA+RL 후보의 가장 가까운 공동 적응 baseline이다. 독립 base 갱신과 editor 공동 학습을 구별할 NEXT다.

개념 비교: DDPG/SAC·imitation → residual policy refinement → VLA 후학습/독립 base 업데이트. 직접 citation edge를 새로 확정한 것은 아니다.

### Fragile Assumption

VLA와 editor가 공동 적응하는 경로 및 intervention·기존 데이터의 역할을 비교 예산에 포함해야 한다. 이는 후속 비교에서 점검할 조건이며 새로 관측한 실패가 아니다.

### Falsifiable Research Question

Base가 독립적으로 바뀌는 상황의 residual 재사용은 공동 fine-tuning과 다른 비용·실패 양상을 갖는가?

### Minimal Comparison and Revise Rule

연구자 제안: image encoder·base action·residual actor 중 무엇을 이전/동결하는지 명시하고 warm-start와 같은 replay·새 데이터 예산으로 비교한다.

단순 gain·새 critic·동일 데이터 모방으로 설명되는 차이는 그 범위로 결론을 줄인다. 의미 있는 차이가 없으면 독립 방법 기여를 주장하지 않는다. 실행 실패·미실행은 연구 가설의 반증과 구분한다.
