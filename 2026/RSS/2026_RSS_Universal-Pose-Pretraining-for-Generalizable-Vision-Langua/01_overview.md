# Universal Pose Pretraining for Generalizable Vision-Language-Action Policies

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Haitao Lin, Hanyang Yu, Jingshun Huang, He Zhang, Yonggen Ling, Ping Tan, Xiangyang Xue, Yanwei Fu
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, pose tokens, pretraining, embodiment alignment
- Aliases: Pose-VLA
- Official paper: https://roboticsproceedings.org/rss22/p145.html
- Venue verification: https://roboticsproceedings.org/rss22/p145.html
- Code/Project: https://hetolin.github.io/PoseVLA/
- Code: https://github.com/hetolin/PoseVLA
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

Pose-VLA는 카메라 기준 3차원 자세 토큰을 먼저 학습하고 그 표현을 개별 로봇의 행동 공간에 맞춰 조작 정책을 훈련한다. [PDF 1쪽](https://roboticsproceedings.org/rss22/p145.pdf#page=1)

## Core Idea and Contribution

- 다양한 3차원 자료의 공간 관계와 로봇 시연의 움직임을 같은 이산 자세 표현에 연결하고, 공간 정합 학습 뒤 궤적 감독을 추가한다. [PDF 3쪽](https://roboticsproceedings.org/rss22/p145.pdf#page=3) · [PDF 4쪽](https://roboticsproceedings.org/rss22/p145.pdf#page=4) · [PDF 5쪽](https://roboticsproceedings.org/rss22/p145.pdf#page=5)
- RoboTwin 2.0과 LIBERO에서 시뮬레이션 성능을 측정하고 실제 조작에서는 과제당 100개 시연을 사용해 물체가 바뀌었을 때의 일반화를 평가했다. [PDF 7쪽](https://roboticsproceedings.org/rss22/p145.pdf#page=7) · [PDF 8쪽](https://roboticsproceedings.org/rss22/p145.pdf#page=8)

## Observation–State–Action Interface

3D pose·trajectory supervision으로 표현을 학습하고 embodiment별 행동을 출력한다.

## Evaluation Scope and Claim Boundary

공식 초록은 RoboTwin 2.0·LIBERO 및 실세계 물체 일반화 실험을 명시한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p145.html) · [저자 project/code](https://hetolin.github.io/PoseVLA/). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

Pose 표현을 VLA에 넣는 것만으로 새 기여를 주장하지 않도록 하는 직접 선행이다.

## Verification Boundary

3D 데이터 규모·pose supervision·camera convention·test object 중복을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
