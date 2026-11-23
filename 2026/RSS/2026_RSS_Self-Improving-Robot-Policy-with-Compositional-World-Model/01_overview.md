# Self-Improving Robot Policy with Compositional World Model

> Evidence maturity: `ABSTRACT_CHECKED`. 개요 전반은 초록 수준이며, 아래 요약과 두 기여에는 확인한 본문 위치를 표시했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Jiazhi Yang, Kunyang Lin, Wencong Zhang, Jinwei Li, Tianwei Lin, Longyan Wu, Ya-Qin Zhang, Hao Zhao, Ping Luo, Zhizhong Su, Hongyang Li, Xiangyu Yue, Li Chen
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: imagination-RL, progress-value, manipulation
- Aliases: RISE
- Official paper: https://roboticsproceedings.org/rss22/p012.html
- Venue verification: https://roboticsproceedings.org/rss22/p012.html
- Code/Project: https://github.com/OpenDriveLab/RISE
- Code: https://github.com/OpenDriveLab/RISE
- Source audit: 2026-11-23 요약과 핵심 기여 두 개를 원문 본문에 대조했다. 나머지 세부 분석은 기존 초록·공식 자료에 근거한다.

## Problem and Importance

RISE는 조작의 다중 시점 미래를 예측하는 동역학 모델과 작업 진행도를 평가하는 가치 모델을 결합해 상상 궤적으로 정책을 개선한다. [PDF 1쪽](https://roboticsproceedings.org/rss22/p012.pdf#page=1)

## Core Idea and Contribution

- 두 모델을 서로 다른 목표로 학습하고 예측한 경로의 진행도에서 정책 갱신에 사용할 어드밴티지를 구한다. [PDF 3쪽](https://roboticsproceedings.org/rss22/p012.pdf#page=3) · [PDF 4쪽](https://roboticsproceedings.org/rss22/p012.pdf#page=4)
- 움직이는 블록 분류·배낭에 넣기·상자 닫기의 실물 결과와 학습에 쓰인 경험 구성의 효과를 비교했다. [PDF 6쪽](https://roboticsproceedings.org/rss22/p012.pdf#page=6) · [PDF 7쪽](https://roboticsproceedings.org/rss22/p012.pdf#page=7)

## Observation–State–Action Interface

Observation/action → imagined multi-view future → progress value/advantage → policy update.

## Evaluation Scope and Claim Boundary

RSS abstract는 dynamic brick sorting, backpack packing, box closing의 세 real-world task 평가를 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p012.html) · [저자 project/code](https://github.com/OpenDriveLab/RISE). 그 밖의 수치, 기준선의 비교 조건, 실패 범위는 별도 대조가 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Current trend. Multi-view dynamics와 progress value를 분리하여 imagined rollout의 advantage를 만든다. VLA-MBPO/WMPO와 reward/value 신뢰도 및 real-robot transfer를 비교할 가치가 있다.

## Verification Boundary

Progress label 생성, failure coverage, value calibration과 real rollout 예산을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
