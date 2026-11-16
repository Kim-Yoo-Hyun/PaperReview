# Emergence of Human to Robot Transfer in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Target Problem and Bottleneck

사람 영상의 지식이 로봇 행동으로 전이되려면 어떤 사전학습 조건이 필요한지 묻는다.

## Changed Formulation

[방법](./03_method.md)의 입력과 학습/배포 개입을 구분해 선행과 비교한다. 단순 성공률 향상보다 어떤 정보가 언제 추가되는지가 비교의 기준이다.

## Assumptions to Verify — Researcher Interpretation

다양성 대 데이터량 분리·사람 행동 supervision 생성·평가 task 누출·동일 compute.

이는 본문에서 확인할 질문이며 논문이 직접 인정한 실패 목록이 아니다.

## Position in the Robotics Loop

사람/로봇 경험 → VLA co-training → 사람 자료에서만 본 조건의 로봇 행동. 다양성 조건의 관찰을 모든 로봇에 대한 전이 보장으로 확대하지 않는다.

정확한 sensor·state·action frame 및 controller 경계는 본문 확인 전 확정하지 않는다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p072.html).
