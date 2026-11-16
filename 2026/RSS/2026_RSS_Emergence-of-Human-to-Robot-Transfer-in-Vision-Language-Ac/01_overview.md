# Emergence of Human to Robot Transfer in Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: VLA, human-video, cross-embodiment, data-scaling
- Aliases:
- Official paper: https://roboticsproceedings.org/rss22/p072.html
- Venue verification: https://roboticsproceedings.org/rss22/p072.html
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-02 공식 proceedings/publisher의 서지·abstract와 저자 project/code 소개를 확인했다. 노트는 abstract/project 기반이며 본문 정독·native 실행을 뜻하지 않는다. 사용자 읽기 상태는 UNREAD 유지.

## Problem and Importance

사람 영상의 지식이 로봇 행동으로 전이되려면 어떤 사전학습 조건이 필요한지 묻는다.

## Core Idea and Contribution

Human video와 robot data를 함께 학습하며 robot 사전학습의 scene·task·embodiment 다양성과 전이의 관계를 조사한다.

## Observation–State–Action Interface

사람/로봇 경험 → VLA co-training → 사람 자료에서만 본 조건의 로봇 행동. 다양성 조건의 관찰을 모든 로봇에 대한 전이 보장으로 확대하지 않는다.

## Evaluation Scope

사전학습의 다양성을 달리하며 human-only generalization 조건을 평가한다. Abstract는 충분히 다양한 robot 사전학습 이후의 전이 이득을 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p072.html).

## Why This Paper Is Here — Researcher Interpretation

Open X-Embodiment와 사람 영상 기반 로봇 학습을 잇는 NEXT 데이터 조건 연구다. Cross-embodiment 전이를 보편적 성질로 가정하지 않도록 비교 기준을 추가한다.

범위와 수치의 미확인 항목은 [평가 노트](./04_evaluation.md)에, 제안하는 반증 질문은 [insights](./05_insights.md)에 둔다.
