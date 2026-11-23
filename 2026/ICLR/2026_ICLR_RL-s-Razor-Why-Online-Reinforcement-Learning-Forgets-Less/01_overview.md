# RL's Razor: Why Online Reinforcement Learning Forgets Less

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
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
- Source audit: 2026-11-12: 공식 abstract/metadata·명시한 project 확인. ICLR 최종 제목의 Online과 저자 페이지의 On-Policy는 같은 arXiv identity다. 로봇 공식 코드는 확인하지 못했다. 이전 N1 지정 본문 대조와 이번 초록 노트를 구별한다. 새 5-note는 초록 수준이며 과거 N1/N2의 지정 본문/source 검토는 work/sources/vla_masters_gap_scout_2026-11-12.json을 따른다. 사용자 정독·코드 재현을 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 새 과제의 성능이 비슷한 정책들에서 온라인 강화학습과 지도 미세조정이 기존 기술을 얼마나 보존하는지 비교한다. [PDF 1쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/618c95f4557c15b253fb0e6f548ea0c0-Paper-Conference.pdf#page=1)

## Core Idea and Contribution

- 새 과제에서 측정한 사전학습 정책과의 KL 발산이 이전 능력의 손실과 어떤 관계인지 언어 모델과 로봇 시뮬레이션에서 조사했다. [PDF 4쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/618c95f4557c15b253fb0e6f548ea0c0-Paper-Conference.pdf#page=4) · [PDF 5쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/618c95f4557c15b253fb0e6f548ea0c0-Paper-Conference.pdf#page=5) · [PDF 6쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/618c95f4557c15b253fb0e6f548ea0c0-Paper-Conference.pdf#page=6)
- 온폴리시 갱신이 기본 정책에서 적게 벗어나는 해를 선호하는 조건을 분석하고, 이 경향이 주어진 시연을 모방하는 학습과 달라지는 이유를 설명했다. [PDF 7쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/618c95f4557c15b253fb0e6f548ea0c0-Paper-Conference.pdf#page=7) · [PDF 8쪽](https://proceedings.iclr.cc/paper_files/paper/2026/file/618c95f4557c15b253fb0e6f548ea0c0-Paper-Conference.pdf#page=8)

## Observation–State–Action Interface

기존 정책 → RL/SFT 후학습 정책 → 신규·기존 과제 행동 평가.

## Evaluation Scope and Claim Boundary

언어 모델과 로봇 foundation model에서 적응 성능과 기존 능력 보존을 평가한다.

근거: [공식 paper/abstract](https://proceedings.iclr.cc/paper_files/paper/2026/hash/618c95f4557c15b253fb0e6f548ea0c0-Abstract-Conference.html) · [저자 project/code](https://jyopari.github.io/posts/rl_razor). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

RL이 지시 능력을 잃는다는 가정을 먼저 반박할 직접 선행이며 KL 진단의 기준이다.

## Verification Boundary

본문에서 확인할 항목: KL 방향·평가 관측 분포·기존 능력 정의·단순 학습률/모방 대안. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
