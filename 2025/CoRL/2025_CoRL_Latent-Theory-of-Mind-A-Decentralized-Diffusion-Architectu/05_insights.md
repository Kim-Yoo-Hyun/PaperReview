# Insights — Latent Theory of Mind: A Decentralized Diffusion Architecture for Cooperative Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.

## Paper-supported conclusion

각 로봇이 자기 관측·계산만으로 공동 조작을 수행하는 문제.에 대한 접근은 [method](./03_method.md), 지지하는 실험 범위는 [evaluation](./04_evaluation.md)에서 확인한다. 현재는 공식 abstract의 주장만 확인했으며 상세 성립 조건은 미검증이다.

근거: [확인한 원문](https://proceedings.mlr.press/v305/he25a.html), 공식 proceedings abstract.

## Researcher interpretation

CROSSPLAY의 decentralized 협력·상대 행동 모델링은 이미 존재함을 보여 주는 CoRL 직접 선행.

개념 연결: Diffusion Policy → LatentToM → CHORUS 및 multi-agent VLA RFT.

- 취약 조건 점검: 연구자 점검: 중앙 학습으로 합의된 latent와 독립 팀 간 latent 호환성을 구별한다.
- 반증 가능한 질문: 학습 중 정렬된 consensus가 독립적으로 학습한 partner 사이에서도 호환되는가?
- 최소 비교 제안: 같은 role 능력을 맞춘 독립 학습 pair를 교차하고 통신·explicit role·population training 대조를 둔다.

이 비교는 연구자 제안이며 논문이 이미 수행한 실험이나 새 기여의 입증이 아니다. 현재 evidence maturity는 `CURATION-HYPOTHESIS`다.
