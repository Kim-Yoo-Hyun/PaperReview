# Flow Q-Learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Seohong Park, Qiyang Li, Sergey Levine
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: CORE
- Tags: flow-matching, offline-RL, offline-to-online
- Aliases: FQL
- Official paper: https://proceedings.mlr.press/v267/park25f.html
- Venue verification: https://proceedings.mlr.press/v267/park25f.html
- Code/Project: https://seohong.me/projects/fql/
- Code: https://github.com/seohongpark/fql
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요.

## Problem and Importance

복잡한 multimodal action 분포를 갖는 flow policy에 offline Q-learning을 적용할 때 효율적인 actor 최적화가 필요하다.

## Core Idea and Contribution

Flow-matching behavior model과 distilled one-step actor를 결합하여 value maximization과 expressive behavior regularization을 연결한다.

## Observation–State–Action Interface

Offline state/image-action data → flow policy 및 one-step actor → continuous action.

## Evaluation Scope and Claim Boundary

공식 abstract는 OGBench와 D4RL의 state/pixel offline 및 offline-to-online task 평가를 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v267/park25f.html) · [저자 project/code](https://seohong.me/projects/fql/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Foundation bridge. Expressive flow policy와 Q-learning/one-step actor를 연결한다. IQL/CQL 이후 flow-action RL과 Q-chunking 계열의 구현·비교 기준으로 중요하다. 평가가 곧 실제 robot VLA 학습을 입증하는 것은 아니다.

## Verification Boundary

Critic target, actor distillation loss, OOD action 제약과 online data 혼합비을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
