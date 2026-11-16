# SAGA: Open-World Mobile Manipulation via Structured Affordance Grounding

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Reported Evaluation Scope

실제 quadrupedal manipulator의 11개 task에서 end-to-end 및 modular 대안과 비교한다. IEEE의 RA-L 11(9), 2026 게재를 우선하며 lab page의 오래된 under-review 표기는 채택하지 않는다.

근거: [공식 paper/abstract](https://ieeexplore.ieee.org/document/11568510/) · [저자 project](https://robot-saga.github.io/).

## Protocol and Reproducibility Boundary

| 항목 | 이번 확인 범위 |
|---|---|
| 데이터·embodiment·task | 위 source가 명시한 범위만 확정. 이름 등장만으로 평가 역할을 추론하지 않음 |
| Train/test split·trial·seed | 본문 수동 확인 필요 |
| Metric 정의·main table·baseline/ablation | 본문 수동 확인 필요; 개선 주장과 비교 가능한 수치를 구분 |
| Failure·negative result | 위에 명시한 내용 외에는 미확인; 실패가 없다는 뜻이 아님 |
| 실행 재현 | 미실행; weights·assets·native runtime은 검증하지 않음 |

## Paper-Specific Verification Questions

affordance 생성 오차·policy가 받는 GT·whole-body action 공간·zero/few-shot split.

제안 실험과 실제 보고 결과는 [insights](./05_insights.md)에서 구분한다.
