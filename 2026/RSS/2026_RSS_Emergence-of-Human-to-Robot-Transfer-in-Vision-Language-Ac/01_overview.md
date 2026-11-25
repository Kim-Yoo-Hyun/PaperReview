# Emergence of Human to Robot Transfer in Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Simar Kareer, Karl Pertsch, James Darpinian, Judy Hoffman, Danfei Xu, Sergey Levine, Chelsea Finn, Suraj Nair
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: VLA, human-video, cross-embodiment, data-scaling
- Aliases:
- Official paper: https://roboticsproceedings.org/rss22/p072.html
- Venue verification: https://roboticsproceedings.org/rss22/p072.html
- Code/Project: https://www.pi.website/research/human_to_robot
- Code: not_identified
- Source audit: 2026-11-02 공식 proceedings/publisher의 서지·abstract와 저자 project/code 소개를 확인했다. 노트는 abstract/project 기반이며 본문 정독·native 실행을 뜻하지 않는다. 사용자 읽기 상태는 UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 사람의 영상에서 본 동작이 로봇으로 전이되는 정도가 기존 로봇 학습 자료의 다양성에 따라 어떻게 달라지는지 조사한다. [PDF 1쪽](https://roboticsproceedings.org/rss22/p072.pdf#page=1)

## Core Idea and Contribution

- 사람 영상에만 등장하는 조건을 평가에 두고 로봇 사전학습 자료의 과제·장면·기종 다양성을 바꿔 사람 영상의 추가 효과를 비교했다. [PDF 5쪽](https://roboticsproceedings.org/rss22/p072.pdf#page=5) · [PDF 6쪽](https://roboticsproceedings.org/rss22/p072.pdf#page=6)
- 더 다양한 로봇 자료로 사전학습한 정책에서 사람 영상의 전이가 두드러짐을 보이고 표현 공간의 변화와 그 관계를 분석했다. [PDF 6쪽](https://roboticsproceedings.org/rss22/p072.pdf#page=6) · [PDF 7쪽](https://roboticsproceedings.org/rss22/p072.pdf#page=7)

## Observation–State–Action Interface

사람/로봇 경험 → VLA co-training → 사람 자료에서만 본 조건의 로봇 행동. 다양성 조건의 관찰을 모든 로봇에 대한 전이 보장으로 확대하지 않는다.

## Evaluation Scope

사전학습의 다양성을 달리하며 human-only generalization 조건을 평가한다. Abstract는 충분히 다양한 robot 사전학습 이후의 전이 이득을 보고한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p072.html).

## Why This Paper Is Here — Researcher Interpretation

Open X-Embodiment와 사람 영상 기반 로봇 학습을 잇는 NEXT 데이터 조건 연구다. Cross-embodiment 전이를 보편적 성질로 가정하지 않도록 비교 기준을 추가한다.

범위와 수치의 미확인 항목은 [평가 노트](./04_evaluation.md)에, 제안하는 반증 질문은 [insights](./05_insights.md)에 둔다.

## 판본과 출처

저자 프로젝트. [공식 페이지](https://www.pi.website/research/human_to_robot)
