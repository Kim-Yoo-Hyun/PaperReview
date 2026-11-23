# Active Offline Policy Selection

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2021 / NeurIPS
- Authors: Ksenia Konyushova, Yutian Chen, Thomas Paine, Caglar Gulcehre, Cosmin Paduraru, Daniel J. Mankowitz, Misha Denil, Nando de Freitas
- Category: Robotics Foundations: Robot Learning
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: RL, evaluation, learning-foundation
- Aliases: AOPS
- Official paper: https://papers.nips.cc/paper_files/paper/2021/hash/cec2346566ba8ecd04bfd992fd193fb3-Abstract.html
- Venue verification: https://papers.nips.cc/paper_files/paper/2021/hash/cec2346566ba8ecd04bfd992fd193fb3-Abstract.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다.

## Problem and Importance

Offline data가 있지만 online 평가 예산이 작은 상황에서 policy를 고른다.

## Core Idea and Contribution

OPE로 초기화하고 policy similarity 기반 Bayesian 선택으로 다음 평가를 배분한다.

## Observation–State–Action Interface

Logged data·policy 후보·평가 결과 → 다음 policy 선택.

## Evaluation Scope and Claim Boundary

여러 benchmark와 다수 후보 정책의 selection 효율을 보고한다.

근거: [공식 paper/abstract](https://papers.nips.cc/paper_files/paper/2021/hash/cec2346566ba8ecd04bfd992fd193fb3-Abstract.html). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

C6에서 OPE+능동 online 평가라는 넓은 방법의 직접 선행이다.

## Verification Boundary

kernel 입력, adaptive reuse, candidate chronology, online budget을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
