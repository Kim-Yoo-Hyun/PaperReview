# Stable Language Guidance for Vision–Language–Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Reported Evaluation Scope

공식 abstract는 manipulation benchmark의 언어 교란 강건성을 보고한다. Backbone·실기 여부·세부 성공률은 이번 abstract 확인 범위에서 확정하지 않는다.

근거: [공식 paper/abstract](https://aclanthology.org/2026.acl-long.190/) · [저자 project](https://github.com/Doo-mon/RSS).

## Protocol and Reproducibility Boundary

| 항목 | 이번 확인 범위 |
|---|---|
| 데이터·embodiment·task | 위 source가 명시한 범위만 확정. 이름 등장만으로 평가 역할을 추론하지 않음 |
| Train/test split·trial·seed | 본문 수동 확인 필요 |
| Metric 정의·main table·baseline/ablation | 본문 수동 확인 필요; 개선 주장과 비교 가능한 수치를 구분 |
| Failure·negative result | 위에 명시한 내용 외에는 미확인; 실패가 없다는 뜻이 아님 |
| 실행 재현 | 미실행; weights·assets·native runtime은 검증하지 않음 |

## Paper-Specific Verification Questions

semantic prior 제거 방식·추가 decode 비용·paraphrase 정답 정보·평가 instruction 분리.

제안 실험과 실제 보고 결과는 [insights](./05_insights.md)에서 구분한다.
