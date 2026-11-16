# Dejavu: Towards Experience Feedback Learning for Embodied Intelligence

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Reported Evaluation Scope

공식 abstract와 author project는 여러 embodied task 및 실제 조작 사례를 보고한다. 정량 성과·matched bank의 범위는 본문 확인 전 확정하지 않는다.

근거: [공식 paper/abstract](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Dejavu_Towards_Experience_Feedback_Learning_for_Embodied_Intelligence_CVPR_2026_paper.html) · [저자 project](https://dejavu2025.github.io/).

## Protocol and Reproducibility Boundary

| 항목 | 이번 확인 범위 |
|---|---|
| 데이터·embodiment·task | 위 source가 명시한 범위만 확정. 이름 등장만으로 평가 역할을 추론하지 않음 |
| Train/test split·trial·seed | 본문 수동 확인 필요 |
| Metric 정의·main table·baseline/ablation | 본문 수동 확인 필요; 개선 주장과 비교 가능한 수치를 구분 |
| Failure·negative result | 위에 명시한 내용 외에는 미확인; 실패가 없다는 뜻이 아님 |
| 실행 재현 | 미실행; weights·assets·native runtime은 검증하지 않음 |

## Paper-Specific Verification Questions

EFN 학습/배포 갱신 경계·success-only bank 편향·task filter·residual 없는 대안·동일 경험 예산.

제안 실험과 실제 보고 결과는 [insights](./05_insights.md)에서 구분한다.
