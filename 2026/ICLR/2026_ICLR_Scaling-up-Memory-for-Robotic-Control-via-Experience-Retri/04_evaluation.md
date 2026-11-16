# Scaling up Memory for Robotic Control via Experience Retrieval

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Reported Evaluation Scope

수분 동안의 기억이 필요한 실제 로봇 조작 과제 3개에서 비교한다. 프로젝트의 object search·counting·dust-and-replace는 task 설명이며 독립 재현 결과가 아니다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/9da515b1ad19d032a7398f00f5ff9b0c-Abstract-Conference.html) · [저자 project](https://jen-pan.github.io/memer/).

## Protocol and Reproducibility Boundary

| 항목 | 이번 확인 범위 |
|---|---|
| 데이터·embodiment·task | 위 source가 명시한 범위만 확정. 이름 등장만으로 평가 역할을 추론하지 않음 |
| Train/test split·trial·seed | 본문 수동 확인 필요 |
| Metric 정의·main table·baseline/ablation | 본문 수동 확인 필요; 개선 주장과 비교 가능한 수치를 구분 |
| Failure·negative result | 위에 명시한 내용 외에는 미확인; 실패가 없다는 뜻이 아님 |
| 실행 재현 | 미실행; weights·assets·native runtime은 검증하지 않음 |

## Paper-Specific Verification Questions

선택 supervision·실패 후 이력 분포·최근 frame 예산. 공식 proceedings는 Qwen 7B, project는 3B로 표기하므로 backbone 크기는 version 확인 필요.

제안 실험과 실제 보고 결과는 [insights](./05_insights.md)에서 구분한다.
