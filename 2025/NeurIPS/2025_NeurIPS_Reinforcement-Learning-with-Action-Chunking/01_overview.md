# Reinforcement Learning with Action Chunking

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / NeurIPS
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: action-chunking, sparse-reward, offline-to-online
- Aliases: Q-chunking
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2025/hash/50348e8f9aef984abe0ea1ec2a326f78-Abstract-Conference.html
- Venue verification: https://proceedings.neurips.cc/paper_files/paper/2025/hash/50348e8f9aef984abe0ea1ec2a326f78-Abstract-Conference.html
- Code/Project: https://github.com/ColinQiyangLi/qc
- Code: https://github.com/ColinQiyangLi/qc
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요.

## Problem and Importance

Offline demonstration을 online RL exploration에 활용하면서 long-horizon sparse-reward 문제의 value backup을 개선하는 문제다.

## Core Idea and Contribution

Chunked action space에서 RL을 수행하여 시간적으로 일관된 exploration과 n-step TD backup을 결합한다.

## Observation–State–Action Interface

State → action chunk → 여러 환경 step 실행; critic도 action sequence를 평가한다.

## Evaluation Scope and Claim Boundary

공식 abstract는 long-horizon sparse-reward manipulation task에서 offline 성능과 online sample efficiency를 비교한다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/50348e8f9aef984abe0ea1ec2a326f78-Abstract-Conference.html) · [저자 project/code](https://github.com/ColinQiyangLi/qc). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Current trend. Chunk 단위의 exploration과 TD backup을 결합한다. ACT/FAST의 표현 관점에 RLPD/FQL의 학습 관점을 더하므로 장기 manipulation의 비교 baseline으로 필요하다.

## Verification Boundary

Chunk 실행 중 feedback 처리, n-step target 조건과 exploration budget을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
