# SwitchVLA: Execution-Aware Task Switching for Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / arXiv
- Authors: Meng Li, Zhen Zhao, Zhengping Che, Fei Liao, Kun Wu, Zhiyuan Xu, Pei Ren, Zhao Jin, Ning Liu, Jian Tang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, task-switching, contact-phase
- Aliases:
- Official paper: https://arxiv.org/abs/2506.03574
- Venue verification: https://arxiv.org/abs/2506.03574
- Code/Project: https://switchvla.github.io/
- Code: not_identified
- Source audit: 2026-10-21: official abstract / author project 확인. 5개 note는 abstract 기반이며 사용자 정독을 의미하지 않는다.

## Problem and Importance

실행 도중 새 지시로 바뀔 때 적절히 task를 전환한다.

## Core Idea and Contribution

Contact phase와 behavior-conditioned trajectory를 이용해 switching을 학습한다.

## Observation–State–Action Interface

언어·관측·execution state → forward/rollback/advance action.

## Evaluation Scope and Claim Boundary

실행 중 task switching 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2506.03574) · [저자 project/code](https://switchvla.github.io/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

D3의 일반 task interruption 주장을 제한하는 REFERENCE다.

## Verification Boundary

contact label, rollback 가정, 정식 venue status을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
