# RL's Razor: Why Online Reinforcement Learning Forgets Less

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / ICLR
- Authors: Idan Shenfeld, Jyothish Pari, Pulkit Agrawal
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: reinforcement-learning, fine-tuning, forgetting, KL-divergence
- Aliases: RL's Razor, RL's Razor: Why On-Policy Reinforcement Learning Forgets Less
- Official paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/618c95f4557c15b253fb0e6f548ea0c0-Abstract-Conference.html
- Venue verification: https://proceedings.iclr.cc/paper_files/paper/2026/hash/618c95f4557c15b253fb0e6f548ea0c0-Abstract-Conference.html
- Code/Project: https://jyopari.github.io/posts/rl_razor
- Code: not_identified
- Source audit: 2026-11-12: 공식 abstract/metadata·명시한 project 확인. ICLR 최종 제목의 Online과 저자 페이지의 On-Policy는 같은 arXiv identity다. 로봇 공식 코드는 확인하지 못했다. 이전 N1 지정 본문 대조와 이번 초록 노트를 구별한다. 새 5-note는 초록 수준이며 과거 N1/N2의 지정 본문/source 검토는 work/sources/vla_masters_gap_scout_2026-11-12.json을 따른다. 사용자 정독·코드 재현을 뜻하지 않는다.

## Problem and Importance

새 과제를 학습할 때 기존 정책의 능력이 보존되는 조건을 묻는다.

## Core Idea and Contribution

같은 신규 과제 성능에서 RL과 SFT의 망각·정책 KL을 비교하고 on-policy RL의 작은 분포 변화 편향을 분석한다.

## Observation–State–Action Interface

기존 정책 → RL/SFT 후학습 정책 → 신규·기존 과제 행동 평가.

## Evaluation Scope and Claim Boundary

언어 모델과 로봇 foundation model에서 적응 성능과 기존 능력 보존을 평가한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/618c95f4557c15b253fb0e6f548ea0c0-Abstract-Conference.html) · [저자 project/code](https://jyopari.github.io/posts/rl_razor). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

RL이 지시 능력을 잃는다는 가정을 먼저 반박할 직접 선행이며 KL 진단의 기준이다.

## Verification Boundary

본문에서 확인할 항목: KL 방향·평가 관측 분포·기존 능력 정의·단순 학습률/모방 대안. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
