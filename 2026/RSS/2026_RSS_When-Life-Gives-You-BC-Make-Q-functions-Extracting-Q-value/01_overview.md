# When Life Gives You BC, Make Q-functions: Extracting Q-values from Behavior Cloning for On-Robot Reinforcement Learning

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Lakshita Dodeja, Ondrej Biza, Shivam Vats, Stephen Hart, Stefanie Tellex, Robin Walters, Karl Schmeckpeper, Thomas Weng
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: offline-to-online-RL, behavior-cloning, Q-learning, contact
- Aliases: Q2RL
- Official paper: https://roboticsproceedings.org/rss22/p153.html
- Venue verification: https://roboticsproceedings.org/rss22/p153.html
- Code/Project: https://pages.rai-inst.com/q2rl_website/
- Code: https://github.com/rai-opensource/q2rl
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

BC에서 online RL로 전환할 때 기존의 좋은 행동을 잃을 수 있다.

## Core Idea and Contribution

BC로부터 Q를 추정하고 BC·RL 행동을 가치에 따라 선택하며 online 학습한다.

## Observation–State–Action Interface

BC 정책·학습 정책 → Q-Gating → 실제 상호작용·RL 갱신.

## Evaluation Scope and Claim Boundary

D4RL·robomimic과 실제 pipe assembly·kitting을 평가한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p153.html) · [저자 project/code](https://pages.rai-inst.com/q2rl_website/) · [공식 code](https://github.com/rai-opensource/q2rl). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

BC prior 보존을 새 unified objective 없이 달성하는 강한 대안이다.

## Verification Boundary

Q 초기화에 필요한 상호작용, 두 정책 유지 비용, gating의 행동 분포 변화을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
