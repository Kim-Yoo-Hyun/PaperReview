# ForceRFT: Refining VLA Actions through Force-Guided Residual Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, residual-RL, force-feedback, contact
- Aliases: ForceRFT
- Official paper: https://arxiv.org/abs/2609.22840
- Venue verification: https://arxiv.org/abs/2609.22840
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-09: official abstract/project 및 metadata 확인. v1 abstract 확인. 공식 code/project는 이번 확인에서 식별하지 못했다. 새 5-note는 abstract 기반이며 전체 본문/실행/사용자 정독을 뜻하지 않는다.

## Problem and Importance

시연 기반 force VLA의 복구 coverage와 task return 최적화 부족을 다룬다.

## Core Idea and Contribution

Frozen SmolVLA prior의 동작을 wrist-feedback residual RL로 보정하며 human correction과 autonomous TD를 분리한다.

## Observation–State–Action Interface

Wrist wrench·변화량·base motion → pose residual; critic은 autonomous 구간을 사용한다.

## Evaluation Scope and Claim Boundary

실제 plug·ring-on-peg·wiping에서 residual imitation을 포함한 기준선과 비교한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2609.22840). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

RL 이득이 성공 데이터 선택·추가 imitation으로 설명되는지 판단할 직접 선행이다.

## Verification Boundary

개입 경계, 데이터 예산, force 관측 주기와 base chunk 비용을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
