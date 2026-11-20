# SAIL: Faster-than-Demonstration Execution of Imitation Learning Policies

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Nadun Ranawaka Arachchige, Zhenyang Chen, Wonsuhk Jung, Woo Chul Shin, Rohan Bansal, Pierre Barroso, Yu Hang He, Yingyan Celine Lin, Benjamin Joffe, Shreyas Kousik, Danfei Xu
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: robot-learning, imitation-learning, Control
- Aliases:
- Official paper: https://proceedings.mlr.press/v305/arachchige25a.html
- Venue verification: https://proceedings.mlr.press/v305/arachchige25a.html
- Code/Project: https://nadunranawaka1.github.io/sail-policy
- Code: https://github.com/nadunRanawaka1/SAIL
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

Imitation policy를 시연 속도보다 빠르게 실행하면서 성능을 유지한다.

## Core Idea and Contribution

일관성·tracking·speed modulation·latency scheduling을 결합한다.

## Observation–State–Action Interface

시연 motion target → policy → tracking/speed 제어.

## Evaluation Scope and Claim Boundary

Simulation task와 실제 robot 플랫폼의 빠른 실행을 보고한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/arachchige25a.html) · [저자 project/code](https://nadunranawaka1.github.io/sail-policy). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

E2에서 retiming·tracking·feedback 이득을 분해할 핵심 IL baseline이다.

## Verification Boundary

target/command/torque 주기, motion 재표현, component ablation을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
