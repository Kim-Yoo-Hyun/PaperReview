# Towards Long-Lived Robots: Continual Learning VLA Models via Reinforcement Fine-Tuning

> Evidence maturity: `ABSTRACT_CHECKED`. 요약·기여와 아래에 인용한 방법·평가를 원문에서 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Yuan Liu, Haoran Li, Shuai Tian, Yuxing Qin, Yuhui Chen, Yupeng Zheng, Yongzhen Huang, Dongbin Zhao
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, continual-learning, Reinforcement Learning, action-chunking
- Aliases: LifeLong-RFT
- Official paper: https://roboticsproceedings.org/rss22/p086.html
- Venue verification: https://roboticsproceedings.org/rss22/p086.html
- Code/Project: https://yuan-liu-lifelong-rft.github.io/
- Code: not_identified
- Source audit: 2026-11-25 게재본에서 아래에 인용한 요약·기여와 평가 조건을 대조했다. [평가 노트](./04_evaluation.md)

## Problem and Importance

VLA의 순차적 과제 적응에서 SFT 데이터 부담과 기존 능력 보존이 문제다.

## Core Idea and Contribution

행동 chunk의 이산 일치·연속 궤적 정렬·출력 형식 보상으로 reinforcement fine-tuning한다.

## Observation–State–Action Interface

관측·지시 → 행동 chunk; 참조 행동과의 일치도가 학습 보상.

## Evaluation Scope and Claim Boundary

SimplerEnv·LIBERO 및 실제 조작, LIBERO continual learning을 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p086.html). 확인한 조건은 [평가 노트](./04_evaluation.md)에 기록했다.

## Why This Paper Is Here — Researcher Interpretation

환경 return 최적화와 참조 행동 기반 RLVR을 구별하기 위한 직접 비교다.

## Verification Boundary

참조 궤적 의존성, rehearsal 여부, 순차 task order, 보상별 효과를 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 원문 대조

LifeLong-RFT는 순차적으로 과제를 학습하는 VLA에 시연과의 행동 일치도를 보상으로 주어 적응과 망각을 평가한다. [게재본](https://www.roboticsproceedings.org/rss22/p086.pdf#page=4)

- 참조 행동의 토큰 일치와 연속 궤적 정합도 및 출력 형식으로 행동 묶음의 과정 보상을 구성한다. [원문](https://www.roboticsproceedings.org/rss22/p086.pdf#page=5)
- NORA-Long을 사용해 시뮬레이터·실제 Franka에서 작업 성능을 측정하고 순차 학습 후 이전 작업의 성능을 비교했다. [원문](https://www.roboticsproceedings.org/rss22/p086.pdf#page=7)

## 판본과 출처

저자 프로젝트. [공식 페이지](https://yuan-liu-lifelong-rft.github.io/)
