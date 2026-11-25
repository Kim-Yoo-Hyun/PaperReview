# InsertAnything: Generalizable Contact-Rich Precision Insertion from Simulation to Reality

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Category: Manipulation, Contact, and Dexterity
- Primary track: Manipulation, contact, tactile, and dexterity
- Tier: NEXT
- Tags: reinforcement-learning, insertion, force-feedback, sim-to-real
- Aliases: InsertAnything
- Official paper: https://arxiv.org/abs/2609.24511
- Venue verification: https://arxiv.org/abs/2609.24511
- Code/Project: https://mzhsoul.github.io/InsertAnything/
- Code: https://github.com/mzhsoul/InsertAnything
- Source audit: arXiv 초록과 저자 공개 저장소의 시뮬레이션·실기 진입점을 확인했다. 학회 게재는 확인되지 않았다.

## Problem and Importance

구멍 위치에 오차가 있고 끼워맞춤 여유가 작을 때 정렬 실패와 걸림이 발생한다.

## Core Idea and Contribution

시뮬레이션에서 정렬과 삽입을 나누어 보상하고 손끝 힘을 이용해 접촉 뒤의 수정 동작을 학습한다.

## Observation–State–Action Interface

목표 자세와 3차원 손끝 힘이 입력이며 정책은 삽입을 위한 움직임을 출력한다.

## Evaluation Scope and Claim Boundary

저자는 실제 여러 형상에서 최소 공칭 간극 0.02 mm를 다뤘다. ManipulationNet의 20/20은 사람 개입을 허용한 프로토콜이며 다른 실험의 자율 지표와 구별한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.24511) · [저자 project/code](https://mzhsoul.github.io/InsertAnything/) · [공식 code](https://github.com/mzhsoul/InsertAnything). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

위치 오차가 있는 삽입에서 강성 학습에 앞서 대조할 힘 기반 동작 정책이다.

## Verification Boundary

형상별 시행 수, 목표 자세의 취득 방식과 사람 개입 범위을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
