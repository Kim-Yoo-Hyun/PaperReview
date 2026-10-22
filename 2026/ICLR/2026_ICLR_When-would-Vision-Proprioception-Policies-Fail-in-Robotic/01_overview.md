# When would Vision-Proprioception Policies Fail in Robotic Manipulation?

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICLR
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, proprioception, robustness
- Aliases: GAP
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/2b3bb2c95195130977a51b3bb251c40a-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2026/hash/2b3bb2c95195130977a51b3bb251c40a-Abstract-Conference.html
- Code/Project: https://gewu-lab.github.io/GAP/
- Code: https://github.com/GeWu-Lab/GAP
- Source audit: 2026-10-21: official abstract / author project 확인. 5개 note는 abstract 기반이며 사용자 정독을 의미하지 않는다.

## Problem and Importance

Vision–proprioception 정책의 일반화 실패가 발생하는 시점을 분석한다.

## Core Idea and Contribution

Motion-transition phase에 따라 proprioception gradient를 조정하는 GAP을 제안한다.

## Observation–State–Action Interface

영상·proprioception → manipulation action; 학습 중 phase-guided gradient 조정.

## Evaluation Scope and Claim Boundary

Simulation·실제 single/dual-arm 및 Octo 적용을 보고한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/2b3bb2c95195130977a51b3bb251c40a-Abstract-Conference.html) · [저자 project/code](https://gewu-lab.github.io/GAP/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

D1에서 modality dominance를 새 발견으로 주장하지 않도록 추가한 직접 NEXT다.

## Verification Boundary

phase 추정 신호, task split, native Octo 코드·checkpoint을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
