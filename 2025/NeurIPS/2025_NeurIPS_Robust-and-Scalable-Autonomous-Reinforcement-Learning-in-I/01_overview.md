# Robust and Scalable Autonomous Reinforcement Learning in Irreversible Environments

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / NeurIPS
- Category: Robotics Foundations: Robot Learning
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: RL, evaluation, learning-foundation
- Aliases: RSA
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2025/hash/56d748a1d7128158681280be7668e0d3-Abstract-Conference.html
- Venue verification: https://proceedings.neurips.cc/paper_files/paper/2025/hash/56d748a1d7128158681280be7668e0d3-Abstract-Conference.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

자율 RL에서 초기·목표 state 다양성과 비가역 실패를 함께 다룬다.

## Core Idea and Contribution

학습 진전에 따른 curriculum과 행동 기반 비가역성 식별을 결합한다.

## Observation–State–Action Interface

Forward/reset 경험 → informative state 선택·위험 회피.

## Evaluation Scope and Claim Boundary

가역/비가역 환경에서 성능과 manual reset 감소를 보고한다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2025/hash/56d748a1d7128158681280be7668e0d3-Abstract-Conference.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

C5/D3의 비가역성·reset 질문에 필요한 RL 선행이다.

## Verification Boundary

irreversibility 정의, behavior encoding, task-specific 정보, reset 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
