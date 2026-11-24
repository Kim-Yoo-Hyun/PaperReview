# Information Directed Reward Learning for Reinforcement Learning

> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 쪽수를 붙인 문장을 원문과 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2021 / NeurIPS
- Authors: David Lindner, Matteo Turchetta, Sebastian Tschiatschek, Kamil Ciosek, Andreas Krause
- Category: Robotics Foundations: Robot Learning
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: reward-learning, robot-learning, evaluation
- Aliases: IDRL
- Official paper: https://proceedings.neurips.cc/paper/2021/hash/1fa6269f58898f0e809575c9a48747ef-Abstract.html
- Full-text retrieval: https://proceedings.neurips.cc/paper/2021/file/1fa6269f58898f0e809575c9a48747ef-Paper.pdf
- Venue verification: https://proceedings.neurips.cc/paper/2021/hash/1fa6269f58898f0e809575c9a48747ef-Abstract.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-24에 한 줄 요약과 핵심 기여 두 개를 아래 PDF 쪽수에 대조했다.

## Problem and Importance

IDRL은 보상 모형의 불확실성 중 가능한 최적 정책들의 기대 반환값 차이를 잘 구별하는 부분에 대해 전문가에게 질의한다. [PDF 1쪽](https://proceedings.neurips.cc/paper/2021/file/1fa6269f58898f0e809575c9a48747ef-Paper.pdf#page=1)

## Core Idea and Contribution

- 베이지안 보상 모형에서 유력한 정책 쌍을 고른 뒤 반환값 차이에 관한 정보 이득이 큰 상태·궤적 질의를 선택한다. [PDF 3쪽](https://proceedings.neurips.cc/paper/2021/file/1fa6269f58898f0e809575c9a48747ef-Paper.pdf#page=3) · [PDF 4쪽](https://proceedings.neurips.cc/paper/2021/file/1fa6269f58898f0e809575c9a48747ef-Paper.pdf#page=4) · [PDF 5쪽](https://proceedings.neurips.cc/paper/2021/file/1fa6269f58898f0e809575c9a48747ef-Paper.pdf#page=5)
- 서로 다른 환경과 피드백 형식에서 질의 횟수에 따른 학습 정책의 반환값 또는 후회를 비교했다. [PDF 8쪽](https://proceedings.neurips.cc/paper/2021/file/1fa6269f58898f0e809575c9a48747ef-Paper.pdf#page=8) · [PDF 9쪽](https://proceedings.neurips.cc/paper/2021/file/1fa6269f58898f0e809575c9a48747ef-Paper.pdf#page=9) · [PDF 10쪽](https://proceedings.neurips.cc/paper/2021/file/1fa6269f58898f0e809575c9a48747ef-Paper.pdf#page=10)

## Observation–State–Action Interface

Bayesian reward belief·policy 후보 → query → expert feedback.

## Evaluation Scope and Claim Boundary

여러 환경과 query 유형에서 label efficiency를 평가한다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper/2021/hash/1fa6269f58898f0e809575c9a48747ef-Abstract.html). 추가 수치와 실패 조건은 해당 실험의 표·설정을 확인해야 한다.

## Why This Paper Is Here — Researcher Interpretation

C4의 decision-relevant reward audit 주장의 직접 foundation이다.

## Verification Boundary

reward prior, policy 후보 생성, expert noise, compute 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
