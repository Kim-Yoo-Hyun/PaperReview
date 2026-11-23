# DISC: Decoupling Instruction from State-Conditioned Control via Policy Generation

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Hanxiang Ren, Pei Zhou, Xunzhe Zhou, Yanchao Yang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, proprioception, robustness
- Aliases:
- Official paper: https://www.roboticsproceedings.org/rss22/p147.html
- Venue verification: https://www.roboticsproceedings.org/rss22/p147.html
- Code/Project: https://github.com/ReNginx/DISC
- Code: https://github.com/ReNginx/DISC
- Source audit: 2026-10-21: official abstract / author project 확인. 5개 note는 abstract 기반이며 사용자 정독을 의미하지 않는다.

## Problem and Importance

관측 shortcut 때문에 지시가 정책 행동에 반영되지 않는 문제를 다룬다.

## Core Idea and Contribution

Instruction-only hypernetwork가 task-specific visuomotor policy의 파라미터를 생성한다.

## Observation–State–Action Interface

언어 → policy weights; 생성된 policy는 관측 → action.

## Evaluation Scope and Claim Boundary

LIBERO-90, Meta-World 및 동일 visual context의 실제 로봇 비교를 보고한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p147.html) · [저자 project/code](https://github.com/ReNginx/DISC). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

OpenVLA 이후 language-conditioned 행동 여부를 확인할 직접 비교군이므로 NEXT다.

## Verification Boundary

generated parameter 수, training budget, 동일 장면 통제을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
