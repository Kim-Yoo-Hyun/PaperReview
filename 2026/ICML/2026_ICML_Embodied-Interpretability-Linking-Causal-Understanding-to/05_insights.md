# Insights — Embodied Interpretability: Linking Causal Understanding to Generalization in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.

## Paper-supported conclusion

분포 변화 아래 실패가 task-irrelevant 시각 단서 의존과 어떤 관계인지 측정한다.에 대한 접근은 [method](./03_method.md), 지지하는 실험 범위는 [evaluation](./04_evaluation.md)에서 확인한다. 현재는 공식 abstract의 주장만 확인했으며 상세 성립 조건은 미검증이다.

근거: [확인한 원문](https://proceedings.mlr.press/v306/zhang26gz.html), 공식 proceedings abstract; software landing.

## Researcher interpretation

FEEDBACK에서 attribution 자체를 새 기여로 주장하지 않도록 하는 직접 진단 baseline.

개념 연결: OpenVLA → mechanistic attribution → RL 후학습의 행동 진단.

- 취약 조건 점검: 연구자 점검: masking이 입력 분포를 바꾸는 효과와 유효 정보 제거를 구별해야 한다.
- 반증 가능한 질문: 정책 입력에 대한 민감도 진단이 실제 fresh feedback의 성공 이득을 예측하는가?
- 최소 비교 제안: 동일 policy의 NMR과 물리 변화 후 관측 갱신 이득을 따로 측정하고 일치·불일치 사례를 비교한다.

이 비교는 연구자 제안이며 논문이 이미 수행한 실험이나 새 기여의 입증이 아니다. 현재 evidence maturity는 `CURATION-HYPOTHESIS`다.
