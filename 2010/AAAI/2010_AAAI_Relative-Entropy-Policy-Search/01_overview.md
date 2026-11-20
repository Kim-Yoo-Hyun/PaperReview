# Relative Entropy Policy Search

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Jan Peters, Katharina Mulling, Yasemin Altun
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: reinforcement-learning, policy-search, KL-divergence, information-constraint
- Aliases: REPS
- Official paper: https://ojs.aaai.org/index.php/AAAI/article/view/7727
- Venue verification: https://ojs.aaai.org/index.php/AAAI/article/view/7727
- Code/Project:
- Code: not_identified
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다.

## Problem and Importance

큰 정책 변경에 따른 정보 손실과 조기 수렴을 줄인다.

## Core Idea and Contribution

Relative entropy 제약으로 정책 개선을 제한하고 명시적 갱신을 도출한다.

## Observation–State–Action Interface

정책 분포·return → 정보 제약 최적화 → 새 정책 분포.

## Evaluation Scope and Claim Boundary

정책 탐색 benchmark에서 방법을 평가한다. VLA나 대규모 foundation model 결과는 아니다.

근거: [공식 paper/abstract](https://ojs.aaai.org/index.php/AAAI/article/view/7727). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

TRPO·MPO·KL 제약의 개념 계보를 보완할 원전이며 현재 공통 정독은 GAE/PPO를 우선한다.

## Verification Boundary

본문에서 확인할 항목: KL 방향·분포 제약·sample 추정·실제 행동 변화. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
