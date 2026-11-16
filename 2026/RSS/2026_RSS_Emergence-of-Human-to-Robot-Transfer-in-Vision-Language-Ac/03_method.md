# Emergence of Human to Robot Transfer in Vision-Language-Action Models

> Canonical metadata: [01_overview.md](./01_overview.md).
> Evidence maturity: `ABSTRACT_CHECKED`. abstract/project 기반 — 본문 수동 확인 필요.
> Source audit: 2026-11-02 공식 서지·abstract 및 저자 소개 확인. 실제 정독·코드 실행을 뜻하지 않는다.

## Pipeline and Representation

Human video와 robot data를 함께 학습하며 robot 사전학습의 scene·task·embodiment 다양성과 전이의 관계를 조사한다.

사람/로봇 경험 → VLA co-training → 사람 자료에서만 본 조건의 로봇 행동. 다양성 조건의 관찰을 모든 로봇에 대한 전이 보장으로 확대하지 않는다.

## Training vs Inference

다양성 대 데이터량 분리·사람 행동 supervision 생성·평가 task 누출·동일 compute을 확인해 추가 supervision과 실제 배포 입력을 분리한다. 공개 code link의 존재를 재현 성공으로 간주하지 않는다.

## Objective and Temporal Contract

Exact loss/control law, optimizer, action horizon, control rate와 memory budget은 이번 abstract/project 확인에서 확정하지 않았다. [평가 조건](./04_evaluation.md)과 함께 읽는다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p072.html).
