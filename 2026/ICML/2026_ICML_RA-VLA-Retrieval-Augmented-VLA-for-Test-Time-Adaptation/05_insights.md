# Insights — RA-VLA: Retrieval-Augmented VLA for Test-Time Adaptation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.

## Paper-supported conclusion

시연 context가 있어도 retrieval 및 pretrained 행동 관성 때문에 새 task에 적응하지 못하는 문제.에 대한 접근은 [method](./03_method.md), 지지하는 실험 범위는 [evaluation](./04_evaluation.md)에서 확인한다. 현재는 공식 abstract의 주장만 확인했으며 상세 성립 조건은 미검증이다.

근거: [확인한 원문](https://proceedings.mlr.press/v306/jang26c.html), 공식 proceedings abstract; arXiv identity.

## Researcher interpretation

RETRIEVAL 후보의 semantic retrieval·execution 결합이라는 넓은 주장이 이미 존재함을 확인하는 ICML 직접 선행.

개념 연결: in-context imitation/RICL → RA-VLA → bank growth의 이득과 간섭.

- 취약 조건 점검: 연구자 점검: retrieval bank의 성공 provenance·평가 episode 독립성을 확인한다.
- 반증 가능한 질문: 목표 bank를 보존한 채 다른 목표 시연을 추가하면, task partition보다 나은 재사용 이득이 생기는가?
- 최소 비교 제안: 고정 target bank와 token/selector 비용에서 goal partition·전체 bank·random 및 의미 selector를 비교한다.

이 비교는 연구자 제안이며 논문이 이미 수행한 실험이나 새 기여의 입증이 아니다. 현재 evidence maturity는 `CURATION-HYPOTHESIS`다.
