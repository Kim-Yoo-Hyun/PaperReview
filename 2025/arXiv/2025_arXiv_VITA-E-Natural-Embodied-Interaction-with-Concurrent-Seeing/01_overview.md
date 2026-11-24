# VITA-E: Natural Embodied Interaction with Concurrent Seeing, Hearing, Speaking, and Acting

> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 쪽수를 붙인 문장을 원문과 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / arXiv
- Authors: Xiaoyu Liu, Chaoyou Fu, Chi Yan, Chu Wu, Haihan Gao, Yi-Fan Zhang, Shaoqi Dong, Cheng Qian, Bin Luo, Xiuyong Yang, Guanwu Li, Yusheng Cai, Yunhang Shen, Deqiang Jiang, Haoyu Cao, Xing Sun, Caifeng Shan, Ran He
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, interaction, interruption
- Aliases:
- Official paper: https://arxiv.org/abs/2510.21817
- Full-text retrieval: https://arxiv.org/pdf/2510.21817v1
- Venue verification: https://arxiv.org/abs/2510.21817
- Code/Project: https://lxysl.github.io/VITA-E/
- Code: https://github.com/Tencent/VITA
- Source audit: 2026-11-24에 한 줄 요약과 핵심 기여 두 개를 아래 PDF 쪽수에 대조했다.

## Problem and Importance

VITA-E는 두 VLA 인스턴스가 실행 및 대기 역할을 나눠 로봇이 말하고 행동하는 동안에도 사용자의 새 음성 지시를 처리하게 한다. [PDF 1쪽](https://arxiv.org/pdf/2510.21817v1#page=1)

## Core Idea and Contribution

- 관측·음성·행동의 동시 처리를 설계하고 모형이 생성하는 특수 토큰을 응답·중단·전환의 시스템 명령에 연결한다. [PDF 5쪽](https://arxiv.org/pdf/2510.21817v1#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2510.21817v1#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2510.21817v1#page=7)
- 기본 조작 성능과 사용자가 개입하는 대화형 과제의 성공률을 구분해 평가했다. [PDF 9쪽](https://arxiv.org/pdf/2510.21817v1#page=9) · [PDF 10쪽](https://arxiv.org/pdf/2510.21817v1#page=10)

## Observation–State–Action Interface

시각·음성·지시 → 발화와 system/action command.

## Evaluation Scope and Claim Boundary

Humanoid platform의 동시 interaction을 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2510.21817) · [저자 project/code](https://lxysl.github.io/VITA-E/). 추가 수치와 실패 조건은 해당 실험의 표·설정을 확인해야 한다.

## Why This Paper Is Here — Researcher Interpretation

D3의 concurrency 자체를 기여로 주장하지 않게 하는 REFERENCE다.

## Verification Boundary

명령 token timing, rollback 범위, ICLR acceptance 미확인을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
