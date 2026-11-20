# Real-World Reinforcement Learning of Active Perception Behaviors

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Edward Hu, Jie Wang, Xingfang Yuan, Fiona Luo, Muyao Li, Gaspard Lambrechts, Oleh Rybkin, Dinesh Jayaraman
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: active perception, real-world RL, privileged value, partial observability
- Aliases: AAWR
- Official paper: https://papers.neurips.cc/paper_files/paper/2025/hash/aa1b1a959c80086cba61d0fd66de412f-Abstract-Conference.html
- Venue verification: https://papers.neurips.cc/paper_files/paper/2025/hash/aa1b1a959c80086cba61d0fd66de412f-Abstract-Conference.html
- Code/Project: https://penn-pal-lab.github.io/aawr/
- Code: https://github.com/penn-pal-lab/aawr
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인.

## Problem and Importance

부분 관측 때문에 범용 robot policy가 필요한 정보 수집 행동을 하지 못한다.

## Core Idea and Contribution

훈련 때만 사용하는 추가 센서로 privileged value를 학습하고 advantage-weighted regression으로 정책을 개선한다.

## Observation–State–Action Interface

훈련 critic의 privileged 정보와 배포 actor의 제한된 관측을 구분하는 AAWR이다.

## Evaluation Scope and Claim Boundary

공식 초록은 3개 로봇·8개 조작 과제 및 generalist 초기 정책의 능동 관측 개선을 명시한다.

근거: [공식 paper/abstract](https://papers.neurips.cc/paper_files/paper/2025/hash/aa1b1a959c80086cba61d0fd66de412f-Abstract-Conference.html) · [저자 project/code](https://penn-pal-lab.github.io/aawr/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

VLA+RL로 관측 행동을 만든다는 넓은 주장을 제한하는 핵심 실세계 기준이다.

## Verification Boundary

추가 센서 접근·초기 demonstrations·advantage 추정·배포 observation을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
