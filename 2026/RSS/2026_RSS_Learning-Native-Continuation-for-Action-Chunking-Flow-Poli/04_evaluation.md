# Learning Native Continuation for Action Chunking Flow Policies

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Reported Evaluation Scope

다섯 실제 조작 과제에서 RTC와 비교해 동작 smoothness와 완료 시간을 평가한다. 공개 코드 링크는 Kinetix simulation 범위이며 전체 실기 경로 공개를 뜻하지 않는다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p058.html) · [저자 project](https://lyfeng001.github.io/Legato/).

## Protocol and Reproducibility Boundary

| 항목 | 이번 확인 범위 |
|---|---|
| 데이터·embodiment·task | 위 source가 명시한 범위만 확정. 이름 등장만으로 평가 역할을 추론하지 않음 |
| Train/test split·trial·seed | 본문 수동 확인 필요 |
| Metric 정의·main table·baseline/ablation | 본문 수동 확인 필요; 개선 주장과 비교 가능한 수치를 구분 |
| Failure·negative result | 위에 명시한 내용 외에는 미확인; 실패가 없다는 뜻이 아님 |
| 실행 재현 | 미실행; weights·assets·native runtime은 검증하지 않음 |

## Paper-Specific Verification Questions

schedule·delay 분포·실기 controller·성공/시간 trade-off·Kinetix와 실기 구현 차이.

제안 실험과 실제 보고 결과는 [insights](./05_insights.md)에서 구분한다.
