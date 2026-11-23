# Reinforcement Learning with Action Chunking

> Evidence maturity: `ABSTRACT_CHECKED`. 개요 전반은 초록 수준이며, 아래 요약과 두 기여에는 확인한 본문 위치를 표시했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / NeurIPS
- Authors: Qiyang Li, Zhiyuan (Paul) Zhou, Sergey Levine
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: action-chunking, sparse-reward, offline-to-online
- Aliases: Q-chunking
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2025/hash/50348e8f9aef984abe0ea1ec2a326f78-Abstract-Conference.html
- Venue verification: https://proceedings.neurips.cc/paper_files/paper/2025/hash/50348e8f9aef984abe0ea1ec2a326f78-Abstract-Conference.html
- Code/Project: https://github.com/ColinQiyangLi/qc
- Code: https://github.com/ColinQiyangLi/qc
- Source audit: 2026-11-23 요약과 핵심 기여 두 개를 원문 본문에 대조했다. 나머지 세부 분석은 기존 초록·공식 자료에 근거한다.

## Problem and Importance

Q-chunking은 희소 보상의 장기 조작에서 연속된 행동 묶음을 강화학습의 행동 단위로 사용해 오프라인에서 온라인 학습으로의 전환을 돕는다. [PDF 1쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/50348e8f9aef984abe0ea1ec2a326f78-Paper-Conference.pdf#page=1)

## Core Idea and Contribution

- 오프라인 궤적의 연속 동작을 탐색에 사용하고 묶음 단위 가치 함수로 여러 시점을 건너뛰는 TD 갱신을 수행한다. [PDF 1쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/50348e8f9aef984abe0ea1ec2a326f78-Paper-Conference.pdf#page=1) · [PDF 4쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/50348e8f9aef984abe0ea1ec2a326f78-Paper-Conference.pdf#page=4)
- OGBench 등에서 오프라인 성능과 온라인 상호작용에 따른 개선을 따로 비교했다. [PDF 8쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/50348e8f9aef984abe0ea1ec2a326f78-Paper-Conference.pdf#page=8) · [PDF 9쪽](https://proceedings.neurips.cc/paper_files/paper/2025/file/50348e8f9aef984abe0ea1ec2a326f78-Paper-Conference.pdf#page=9)

## Observation–State–Action Interface

State → action chunk → 여러 환경 step 실행; critic도 action sequence를 평가한다.

## Evaluation Scope and Claim Boundary

공식 abstract는 long-horizon sparse-reward manipulation task에서 offline 성능과 online sample efficiency를 비교한다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/50348e8f9aef984abe0ea1ec2a326f78-Abstract-Conference.html) · [저자 project/code](https://github.com/ColinQiyangLi/qc). 그 밖의 수치, 기준선의 비교 조건, 실패 범위는 별도 대조가 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Current trend. Chunk 단위의 exploration과 TD backup을 결합한다. ACT/FAST의 표현 관점에 RLPD/FQL의 학습 관점을 더하므로 장기 manipulation의 비교 baseline으로 필요하다.

## Verification Boundary

Chunk 실행 중 feedback 처리, n-step target 조건과 exploration budget을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
