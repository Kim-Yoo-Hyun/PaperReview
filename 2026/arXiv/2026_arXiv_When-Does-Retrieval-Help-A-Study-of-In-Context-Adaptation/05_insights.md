# Insights — When Does Retrieval Help? A Study of In-Context Adaptation in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `FULL_TEXT_CHECKED`. 지정 본문 절만 확인; 전체 정독·재현 아님.

## Paper-supported conclusion

검색 representation의 품질이 downstream robot success에 어떻게 연결되는지 조사한다.에 대한 접근은 [method](./03_method.md), 지지하는 실험 범위는 [evaluation](./04_evaluation.md)에서 확인한다. 지정 절의 결과를 읽었으며 재현하거나 일반적인 우월성을 검증한 것은 아니다.

근거: [확인한 원문](https://arxiv.org/html/2610.05492v1), §2–3, Appendix D–E.

## Researcher interpretation

RETRIEVAL의 가장 직접적인 진단 선행으로, 단순 cross-task interference 발견만으로 기여를 주장하지 않게 한다.

개념 연결: RICL → retrieval study/RA-VLA → controlled bank growth.

- 취약 조건 점검: 연구자 점검: 다른 task의 도움과 다른 task의 오염을 하나의 범주로 합치지 않는다.
- 반증 가능한 질문: 고정 target bank에 goal-conflicting donor를 늘리는 조작이 기존 selector 비교보다 어떤 추가 예측을 주는가?
- 최소 비교 제안: Target bank와 top-k/token을 고정하고 related-helpful·goal-conflicting·무관 donor 추가를 분리한다. Partition 대비 이득이 없으면 독립 방법 투자 축소.

이 비교는 연구자 제안이며 논문이 이미 수행한 실험이나 새 기여의 입증이 아니다. 현재 evidence maturity는 `CURATION-HYPOTHESIS`다.
