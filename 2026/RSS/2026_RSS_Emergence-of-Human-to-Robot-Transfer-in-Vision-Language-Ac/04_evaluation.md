# Emergence of Human to Robot Transfer in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Reported Evaluation Scope

사전학습의 다양성을 달리하며 human-only generalization 조건을 평가한다. Abstract는 충분히 다양한 robot 사전학습 이후의 전이 이득을 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p072.html).

## Protocol and Reproducibility Boundary

| 항목 | 이번 확인 범위 |
|---|---|
| 데이터·embodiment·task | 위 source가 명시한 범위만 확정. 이름 등장만으로 평가 역할을 추론하지 않음 |
| Train/test split·trial·seed | 본문 수동 확인 필요 |
| Metric 정의·main table·baseline/ablation | 본문 수동 확인 필요; 개선 주장과 비교 가능한 수치를 구분 |
| Failure·negative result | 위에 명시한 내용 외에는 미확인; 실패가 없다는 뜻이 아님 |
| 실행 재현 | 미실행; weights·assets·native runtime은 검증하지 않음 |

## Paper-Specific Verification Questions

다양성 대 데이터량 분리·사람 행동 supervision 생성·평가 task 누출·동일 compute.

제안 실험과 실제 보고 결과는 [insights](./05_insights.md)에서 구분한다.
