# From Prior to Pro: Efficient Skill Mastery via Distribution Contractive RL Finetuning

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

## Paper-supported conclusion

Prior를 동결하고 chunk residual을 학습한다. 선택적 regularization과 value 기반 선택을 사용하며 공개 구현에서 Q/Monte-Carlo filtering을 확인했다.

ICML 공식 metadata와 arXiv v2의 지정 절/code를 확인했다. 현재 deterministic TD3·Q-filter 계획을 DICE-RL 전체 재현으로 부르지 않는다.

근거: [지정 본문](https://arxiv.org/html/2603.10263v2) — v2 §4; model/rl/distill_residual_rl_img.py selected filter/loss paths. Code 검토 revision: `98d936e52523878f0172e606ea32403176497100`; 실행하지 않았다.

## Researcher interpretation

### Novelty and Dependency

Frozen prior+residual+선택적 모방의 최신 직접 선행이다. 현재 후보의 규칙 조합만으로 독립 방법 기여를 주장하지 않도록 NEXT에 추가한다.

개념 비교: DDPG/SAC·imitation → residual policy refinement → VLA 후학습/독립 base 업데이트. 직접 citation edge를 새로 확정한 것은 아니다.

### Fragile Assumption

Prior가 유용한 행동 support를 제공하고 critic/return 신호가 선택적 제약을 안내해야 한다. 이는 후속 비교에서 점검할 조건이며 새로 관측한 실패가 아니다.

### Falsifiable Research Question

독립 base 교체 후 residual actor 재사용은 DICE식 regularization·value 선택과 동일 데이터 조건에서도 유효한가?

### Minimal Comparison and Revise Rule

연구자 제안: prior 교체와 학습 대상·critic 재초기화·replay를 명시하고 zero/frozen/gain/warm/fresh 및 선택적 모방을 동일 예산으로 비교한다.

단순 gain·새 critic·동일 데이터 모방으로 설명되는 차이는 그 범위로 결론을 줄인다. 의미 있는 차이가 없으면 독립 방법 기여를 주장하지 않는다. 실행 실패·미실행은 연구 가설의 반증과 구분한다.
