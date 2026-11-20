# VITA-E: Natural Embodied Interaction with Concurrent Seeing, Hearing, Speaking, and Acting

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
- Authors: Xiaoyu Liu, Chaoyou Fu, Chi Yan, Chu Wu, Haihan Gao, Yi-Fan Zhang, Shaoqi Dong, Cheng Qian, Bin Luo, Xiuyong Yang, Guanwu Li, Yusheng Cai, Yunhang Shen, Deqiang Jiang, Haoyu Cao, Xing Sun, Caifeng Shan, Ran He
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, interaction, interruption
- Aliases:
- Official paper: https://arxiv.org/abs/2510.21817
- Venue verification: https://arxiv.org/abs/2510.21817
- Code/Project: https://lxysl.github.io/VITA-E/
- Code: https://github.com/Tencent/VITA
- Source audit: 2026-10-21: official abstract / author project 확인. 5개 note는 abstract 기반이며 사용자 정독을 의미하지 않는다.

## Problem and Importance

로봇의 동시 보고·듣기·말하기·행동과 사용자 interruption을 연결한다.

## Core Idea and Contribution

Active/Standby dual-model과 system command token을 사용한다.

## Observation–State–Action Interface

시각·음성·지시 → 발화와 system/action command.

## Evaluation Scope and Claim Boundary

Humanoid platform의 동시 interaction을 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2510.21817) · [저자 project/code](https://lxysl.github.io/VITA-E/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

D3의 concurrency 자체를 기여로 주장하지 않게 하는 REFERENCE다.

## Verification Boundary

명령 token timing, rollback 범위, ICLR acceptance 미확인을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
