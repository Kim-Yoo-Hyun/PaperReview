# Simple Masked Training Strategies Yield Control Policies That Are Robust to Sensor Failure

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Skand Skand, Bikram Pandit, Chanho Kim, Li Fuxin, Stefan Lee
- Conference year: 2024; proceedings publication year: 2025. [PMLR volume 270](https://proceedings.mlr.press/v270/)의 개최일과 출판일을 구분한다.
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: Robotics, evaluation, robustness
- Aliases:
- Official paper: https://proceedings.mlr.press/v270/skand25a.html
- Venue verification: https://proceedings.mlr.press/v270/skand25a.html
- Conference edition: 2024 · https://proceedings.mlr.press/v270/
- Code/Project: https://pvskand.github.io/projects/RME
- Code: project_only
- Source audit: 2026-10-25 공식 abstract와 publication metadata 및 명시된 project/code 공개 링크 확인. 본문 정독·코드 실행·payload 검증은 이번 등록 범위 밖이다. CoRL 개최 2024, PMLR 출판 2025를 분리한다.

## Problem and Importance

센서 결손이 배포된 robot policy의 행동을 불안정하게 만든다.

## Core Idea and Contribution

여러 sensor를 처리하는 encoder와 학습 중 modality dropout으로 결손에 대비한다.

## Observation–State–Action Interface

가용 sensor와 결손 처리 표현 → RL control policy.

## Evaluation Scope and Claim Boundary

Locomotion과 manipulation, simulation과 실로봇의 sensor failure를 평가한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v270/skand25a.html) · [저자 project/code](https://pvskand.github.io/projects/RME). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

새 multimodal VLA adaptation 전에 대조할 단순 sensor-dropout 기준이다.

## Verification Boundary

결손 종류·지속 시간·학습 노출, proprio와 image mask 차이을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
