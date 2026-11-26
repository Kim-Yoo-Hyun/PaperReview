# Overcoming Exploration in Reinforcement Learning with Demonstrations

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED` — 지정 절만 확인한 기록이며 전체 정독·실험 재현을 뜻하지 않는다.

## Paper-supported conclusion

DDPG·HER와 demonstration replay 및 behavior cloning을 결합한다. Q-filter는 demonstration 행동이 actor 행동보다 높은 Q를 받을 때 모방 손실을 적용한다.

이번 확인은 Q-filter 수식과 서지에 한정한다. 정확한 seed·전체 baseline/ablation·현재 공식 code 상태는 확인하지 않았다.

근거: [지정 본문](https://arxiv.org/pdf/1709.10089) — Q-Filter subsection / Eq. 8; arXiv abstract and publisher-deposited metadata.

## Researcher interpretation

### Novelty and Dependency

선택적 Q 기반 imitation의 직접 기원으로 REFERENCE에 추가한다. 2024–2026 최신 동향 수에는 포함하지 않으며 기존 SAC/DDPG 기반 읽기 흐름을 보완한다.

개념 비교: DDPG/SAC·imitation → residual policy refinement → VLA 후학습/독립 base 업데이트. 직접 citation edge를 새로 확정한 것은 아니다.

### Fragile Assumption

Q 추정이 demonstration과 현재 actor의 행동 비교에 의미 있는 신호여야 한다. 이는 후속 비교에서 점검할 조건이며 새로 관측한 실패가 아니다.

### Falsifiable Research Question

새 residual 이전 규칙의 이득은 이미 알려진 Q-filter와 return-weighted imitation으로 설명되는가?

### Minimal Comparison and Revise Rule

연구자 제안: 같은 reference 행동·critic·데이터·loss 계수를 사용한 원리 수준 Q-filter와 무조건 모방을 분리하고, 원 논문 전체 알고리즘 재현 여부를 명시한다.

단순 gain·새 critic·동일 데이터 모방으로 설명되는 차이는 그 범위로 결론을 줄인다. 의미 있는 차이가 없으면 독립 방법 기여를 주장하지 않는다. 실행 실패·미실행은 연구 가설의 반증과 구분한다.
