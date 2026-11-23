# WholeBodyVLA: Towards Unified Latent VLA for Whole-body Loco-manipulation Control

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICLR
- Authors: Haoran Jiang, Jin Chen, Qingwen Bu, Li Chen, Modi Shi, Yanjie Zhang, Delong Li, Chuanzhe Suo, wang chuang, zhihui peng, Hongyang Li
- Category: Locomotion, Whole-Body, and Mobile Manipulation
- Primary track: Locomotion, whole-body, mobile manipulation, and humanoids
- Tier: NEXT
- Tags: VLA, mobile-manipulation, control-interface
- Aliases:
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/ff7373914a96956f2a7cacbdf3b0b8d8-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2026/hash/ff7373914a96956f2a7cacbdf3b0b8d8-Abstract-Conference.html
- Code/Project: https://wholebodyvla.github.io/
- Code: https://github.com/OpenDriveLab/WholebodyVLA
- Source audit: 2026-10-21: official abstract / author project 확인. 5개 note는 abstract 기반이며 사용자 정독을 의미하지 않는다.

## Problem and Importance

이동과 상체 조작을 결합할 때 데이터 부족과 decision–execution 차이를 줄인다.

## Core Idea and Contribution

Unified latent VLA와 loco-manipulation-oriented low-level RL을 연결한다.

## Observation–State–Action Interface

시각·언어 → 상체 action·locomotion command → whole-body control.

## Evaluation Scope and Claim Boundary

Humanoid loco-manipulation과 확장 task를 보고한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/ff7373914a96956f2a7cacbdf3b0b8d8-Abstract-Conference.html) · [저자 project/code](https://wholebodyvla.github.io/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

NaVILA 이후 VLA와 low-level RL의 역할을 비교할 NEXT다.

## Verification Boundary

실행 가능한 codebase, latent supervision, controller budget을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
