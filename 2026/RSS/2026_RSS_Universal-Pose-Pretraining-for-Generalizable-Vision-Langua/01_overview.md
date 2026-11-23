# Universal Pose Pretraining for Generalizable Vision-Language-Action Policies

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
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
- Source audit: 2026-11-18: 공식 초록·bibliographic record와 연결된 저자 자료 확인. Abstract 기반 등록이며 본문 전체·실험 재현은 미확인.

## Problem and Importance

VQA 중심 표현과 희소한 로봇 action supervision이 세밀한 3D 상태 차이를 학습하기 어렵게 한다.

## Core Idea and Contribution

Camera-centric pose token으로 공간·trajectory 사전학습을 한 뒤 로봇 action space에 적응한다.

## Observation–State–Action Interface

3D pose·trajectory supervision으로 표현을 학습하고 embodiment별 행동을 출력한다.

## Evaluation Scope and Claim Boundary

공식 초록은 RoboTwin 2.0·LIBERO 및 실세계 물체 일반화 실험을 명시한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p145.html) · [저자 project/code](https://hetolin.github.io/PoseVLA/). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

Pose 표현을 VLA에 넣는 것만으로 새 기여를 주장하지 않도록 하는 직접 선행이다.

## Verification Boundary

3D 데이터 규모·pose supervision·camera convention·test object 중복을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
