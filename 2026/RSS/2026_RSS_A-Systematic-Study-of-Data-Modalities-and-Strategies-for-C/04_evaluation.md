# A Systematic Study of Data Modalities and Strategies for Co-training Large Behavior Models for Robot Manipulation

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Reported Evaluation Scope

공식 abstract는 89개 정책을 simulation과 실제 로봇에서 평가했다고 보고한다. 모든 modality가 유익하다는 결론은 아니며 이산 action-token 변형의 이득은 해당 비교에서 유의하지 않았다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p007.html) · [저자 project](https://co-training-lbm.github.io/).

## Protocol and Reproducibility Boundary

| 항목 | 이번 확인 범위 |
|---|---|
| 데이터·embodiment·task | 위 source가 명시한 범위만 확정. 이름 등장만으로 평가 역할을 추론하지 않음 |
| Train/test split·trial·seed | 본문 수동 확인 필요 |
| Metric 정의·main table·baseline/ablation | 본문 수동 확인 필요; 개선 주장과 비교 가능한 수치를 구분 |
| Failure·negative result | 위에 명시한 내용 외에는 미확인; 실패가 없다는 뜻이 아님 |
| 실행 재현 | 미실행; weights·assets·native runtime은 검증하지 않음 |

## Paper-Specific Verification Questions

modality별 token/compute 균형·학습 단계·동일 task split·negative result의 적용 범위.

제안 실험과 실제 보고 결과는 [insights](./05_insights.md)에서 구분한다.
