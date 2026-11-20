# SOE: Sample-Efficient Robot Policy Self-Improvement via On-Manifold Exploration

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Yang Jin, Jun Lv, Han Xue, Wendi Chen, Chuan Wen, Cewu Lu
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: robot self-improvement, latent exploration, action manifold, manipulation
- Aliases: SOE
- Official paper: https://arxiv.org/abs/2509.19292
- Venue verification: https://api.crossref.org/works/10.1109/icra57385.2026.11696357
- Code/Project: https://ericjin2002.github.io/SOE/
- Code: https://github.com/EricJin2002/SOE
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인. 저자 repo ICRA2026 표기와 일부 BibTeX IROS2025 문구가 혼재한다. 공식 proceedings identity를 확보하지 못해 arXiv2025 유지. 공식 conference/journal acceptance 확인을 확보하지 못해 preprint 유지.

## Problem and Importance

기존 policy의 action mode collapse와 무작위 perturbation이 유효한 탐색을 제한한다.

## Core Idea and Contribution

Task 관련 latent를 학습하고 유효한 행동 manifold에서 탐색하며 human-guided exploration을 지원한다.

## Observation–State–Action Interface

기본 policy에 추가하는 latent exploration 모듈이며 원 VLA 가중치의 공동 갱신과 구별해야 한다.

## Evaluation Scope and Claim Boundary

저자 project는 robomimic의 4개 simulation task와 mug hanging·toaster loading·lamp capping 실제 과제를 제시한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2509.19292) · [저자 project/code](https://ericjin2002.github.io/SOE/) · [공식 code](https://github.com/EricJin2002/SOE). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

관계 조건 탐색이 일반 latent/on-manifold 탐색보다 필요한지 확인할 직접 baseline이다.

## Verification Boundary

Manifold 학습 데이터·추가 supervision·policy update 방식·안전 주장 조건을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
