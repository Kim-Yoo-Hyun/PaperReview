# RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Target Problem and Bottleneck

사전학습 VLA가 새 시연을 문맥으로 읽는 능력을 자동으로 갖추지 못하는 문제를 다룬다.

## Changed Formulation

[방법](./03_method.md)의 입력과 학습/배포 개입을 구분해 선행과 비교한다. 단순 성공률 향상보다 어떤 정보가 언제 추가되는지가 비교의 기준이다.

## Assumptions to Verify — Researcher Interpretation

시연 구간·action interpolation·target-task split·검색 query와 inference 예산.

이는 본문에서 확인할 질문이며 논문이 직접 인정한 실패 목록이 아니다.

## Position in the Robotics Loop

현재 관측·지시와 검색된 시연 → π0-FAST 기반 정책 → 로봇 행동. ICL 능력을 만드는 후학습과 새 task에서의 무갱신 적응을 구분한다.

정확한 sensor·state·action frame 및 controller 경계는 본문 확인 전 확정하지 않는다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/sridhar25a.html) · [저자 project](https://ricl-vla.github.io/).
