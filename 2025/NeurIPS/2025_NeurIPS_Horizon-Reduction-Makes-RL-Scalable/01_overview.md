# Horizon Reduction Makes RL Scalable

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Seohong Park, Kevin Frans, Deepinder Mann, Benjamin Eysenbach, Aviral Kumar, Sergey Levine
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: offline-RL, scaling, temporal-abstraction, goal-conditioning
- Aliases: SHARSA
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2025/hash/0c66099070429b9b49ad8bb19c740c22-Abstract-Conference.html
- Venue verification: https://proceedings.neurips.cc/paper_files/paper/2025/hash/0c66099070429b9b49ad8bb19c740c22-Abstract-Conference.html
- Code/Project: https://github.com/seohongpark/horizon-reduction
- Code: https://github.com/seohongpark/horizon-reduction
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다.

## Problem and Importance

데이터·모델을 늘려도 긴 horizon의 offline RL 성능이 포화되는 이유를 분석한다.

## Core Idea and Contribution

Horizon 감소 기법을 비교하고 짧은 유효 결정 길이를 활용하는 SHARSA를 제안한다.

## Observation–State–Action Interface

대규모 goal-conditioned data → horizon을 줄인 value/policy 학습 → 목표 행동.

## Evaluation Scope and Claim Boundary

다양한 긴 목표 과제의 scaling을 비교한다. 모든 online VLA RL의 원인으로 일반화하지 않는다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0c66099070429b9b49ad8bb19c740c22-Abstract-Conference.html) · [저자 project/code](https://github.com/seohongpark/horizon-reduction). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Chunk 길이·목표 분해와 데이터 scaling의 효과를 분리할 최신 기준 연구다.

## Verification Boundary

본문에서 확인할 항목: 유효 결정 길이·coverage·데이터 크기·학습 계산량·물리 시간. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
