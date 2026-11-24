# HiMoE-VLA: Hierarchical Mixture-of-Experts for Generalist Vision-Language-Action Policies

> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 쪽수를 붙인 문장을 원문과 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / arXiv
- Authors: Zhiying Du, Bei Liu, Yaobo Liang, Yichao Shen, Haidong Cao, Xiangyu Zheng, Zhiyuan Feng, Zuxuan Wu, Jiaolong Yang, Yu-Gang Jiang
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: REFERENCE
- Tags: VLA, action-interface, cross-embodiment
- Aliases:
- Official paper: https://arxiv.org/abs/2512.05693
- Full-text retrieval: https://arxiv.org/pdf/2512.05693v2
- Venue verification: https://arxiv.org/abs/2512.05693
- Code/Project: https://github.com/ZhiyingDu/HiMoE-VLA
- Code: https://github.com/ZhiyingDu/HiMoE-VLA
- Source audit: 2026-11-24에 한 줄 요약과 핵심 기여 두 개를 아래 PDF 쪽수에 대조했다.

## Problem and Importance

HiMoE-VLA는 로봇마다 다른 행동 공간과 관측의 차이를 고려해 전문가 층과 공유 층을 갖는 행동 모듈을 학습한다. [PDF 1쪽](https://arxiv.org/pdf/2512.05693v2#page=1)

## Core Idea and Contribution

- 입출력에 행동 공간별 전문가를 배치하고 이웃 층에는 관측·형태 다양성을 맡기는 전문가를, 중앙에는 공유 블록을 배치한다. [PDF 3쪽](https://arxiv.org/pdf/2512.05693v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2512.05693v2#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2512.05693v2#page=5)
- 공동 학습 자료를 통제해 음의 전이 여부를 비교하고 시뮬레이션과 실제 xArm7·ALOHA 과제에서 성공률을 평가했다. [PDF 6쪽](https://arxiv.org/pdf/2512.05693v2#page=6) · [PDF 7쪽](https://arxiv.org/pdf/2512.05693v2#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2512.05693v2#page=8)

## Observation–State–Action Interface

언어·영상·embodiment/action-space 정보 → expert routing → action.

## Evaluation Scope and Claim Boundary

CALVIN·LIBERO 및 실제 로봇 평가를 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2512.05693) · [저자 project/code](https://github.com/ZhiyingDu/HiMoE-VLA). 추가 수치와 실패 조건은 해당 실험의 표·설정을 확인해야 한다.

## Why This Paper Is Here — Researcher Interpretation

E1에서 물리 action 충돌을 단순 expert 분리와 구별할 직접 REFERENCE다.

## Verification Boundary

routing에 쓰는 robot ID, contrastive objective, load balance, parameter 예산을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
