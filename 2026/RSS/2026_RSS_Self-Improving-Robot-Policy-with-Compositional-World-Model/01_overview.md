# Self-Improving Robot Policy with Compositional World Model

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue
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
- Source audit: 2026-10-19: 공식 paper abstract 및 저자 project/code README 확인; abstract 기반 — 본문 수동 확인 필요.

## Problem and Importance

Contact-rich/dynamic task에서 VLA의 작은 실행 오차가 누적되지만 실제 환경 on-policy RL은 reset·hardware 비용이 높다.

## Core Idea and Contribution

Multi-view controllable dynamics와 progress value model을 분리하여 imagined rollout에서 advantage를 만들고 policy를 개선한다.

## Observation–State–Action Interface

Observation/action → imagined multi-view future → progress value/advantage → policy update.

## Evaluation Scope and Claim Boundary

RSS abstract는 dynamic brick sorting, backpack packing, box closing의 세 real-world task 평가를 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p012.html) · [저자 project/code](https://github.com/OpenDriveLab/RISE). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Current trend. Multi-view dynamics와 progress value를 분리하여 imagined rollout의 advantage를 만든다. VLA-MBPO/WMPO와 reward/value 신뢰도 및 real-robot transfer를 비교할 가치가 있다.

## Verification Boundary

Progress label 생성, failure coverage, value calibration과 real rollout 예산을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
