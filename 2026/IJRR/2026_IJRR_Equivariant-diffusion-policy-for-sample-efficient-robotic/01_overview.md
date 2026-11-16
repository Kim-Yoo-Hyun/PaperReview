# Equivariant diffusion policy for sample-efficient robotic manipulation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / IJRR
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: Robotics, Imitation Learning, Diffusion, equivariance, sample-efficiency
- Aliases: Equivariant Diffusion Policy, EquiDiff
- Official paper: https://journals.sagepub.com/doi/10.1177/02783649261424445
- Venue verification: https://journals.sagepub.com/doi/10.1177/02783649261424445
- Code/Project: https://equidiff.github.io/
- Code: https://github.com/pointW/equidiff
- Source audit: 2026-10-25 공식 abstract/서지정보 및 명시된 저자 링크 확인. 이번 노트는 abstract 기반이며 본문 전체·코드 실행·payload는 미검증이다. 공식 journal abstract·확장판 설명을 확인했다. CoRL 2024 원판이 미등록이므로 IJRR 2026 확장판 하나로 등록하고 원판은 alias/계보로 보존. 연결 code는 원판 기반이며 journal 전체 구현 coverage는 미검증.

## Problem and Importance

Diffusion policy의 복잡한 denoising 학습에는 많은 시연이 필요하다.

## Core Idea and Contribution

조작의 기하학적 대칭성을 denoising에 반영해 데이터 효율을 높인다.

## Observation–State–Action Interface

관측·noisy action trajectory → equivariant denoiser → action trajectory.

## Evaluation Scope and Claim Boundary

MimicGen simulation과 실로봇 manipulation에서 소량 시연 학습을 비교한다.

근거: [공식 paper/abstract](https://journals.sagepub.com/doi/10.1177/02783649261424445) · [저자 project/code](https://equidiff.github.io/) · [공식 code](https://github.com/pointW/equidiff). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

일반화 이득이 더 큰 VLA보다 대칭성 같은 inductive bias로 설명되는지 대조할 기준이다.

## Verification Boundary

적용 가능한 symmetry, 절대/상대 action, RGB/point-cloud 정보량, checkpoint 선택을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
