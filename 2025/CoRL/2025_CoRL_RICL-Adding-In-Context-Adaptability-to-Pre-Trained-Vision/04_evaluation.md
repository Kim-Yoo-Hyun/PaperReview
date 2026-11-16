# RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Reported Evaluation Scope

새 조작 과제의 소수 시연을 이용한 적응과 추가 fine-tuning을 비교한다. 공식 abstract의 개선 주장이며 개별 trial·split은 확인 필요다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/sridhar25a.html) · [저자 project](https://ricl-vla.github.io/).

## Protocol and Reproducibility Boundary

| 항목 | 이번 확인 범위 |
|---|---|
| 데이터·embodiment·task | 위 source가 명시한 범위만 확정. 이름 등장만으로 평가 역할을 추론하지 않음 |
| Train/test split·trial·seed | 본문 수동 확인 필요 |
| Metric 정의·main table·baseline/ablation | 본문 수동 확인 필요; 개선 주장과 비교 가능한 수치를 구분 |
| Failure·negative result | 위에 명시한 내용 외에는 미확인; 실패가 없다는 뜻이 아님 |
| 실행 재현 | 미실행; weights·assets·native runtime은 검증하지 않음 |

## Paper-Specific Verification Questions

시연 구간·action interpolation·target-task split·검색 query와 inference 예산.

제안 실험과 실제 보고 결과는 [insights](./05_insights.md)에서 구분한다.
