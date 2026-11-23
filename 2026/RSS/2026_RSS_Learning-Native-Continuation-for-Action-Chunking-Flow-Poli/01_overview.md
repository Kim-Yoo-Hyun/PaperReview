# Learning Native Continuation for Action Chunking Flow Policies

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Yufeng Liu, Hang Yu, Juntu Zhao, Bocheng Li, Di Zhang, Mingzhu Li, Wenxuan Wu, Yingdong Hu, Junyuan Xie, Junliang Guo, Dequan Wang, Yang Gao
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, action-chunking, flow-policy, real-time-control
- Aliases: Legato
- Official paper: https://roboticsproceedings.org/rss22/p058.html
- Venue verification: https://roboticsproceedings.org/rss22/p058.html
- Code/Project: https://lyfeng001.github.io/Legato/
- Code: https://github.com/lyfeng001/Legato-kinetix
- Source audit: 2026-11-02 공식 proceedings/publisher의 서지·abstract와 저자 project/code 소개를 확인했다. 노트는 abstract/project 기반이며 본문 정독·native 실행을 뜻하지 않는다. 사용자 읽기 상태는 UNREAD 유지.

## Problem and Importance

Action chunk 경계의 불연속과 multimodal switching이 로봇 동작을 지연시키는 문제를 다룬다.

## Core Idea and Contribution

알려진 action과 noise를 섞는 schedule 및 flow 학습을 통해 chunk continuation을 정책 자체가 익히게 한다.

## Observation–State–Action Interface

관측·이전 action 정보·continuation schedule → flow action chunk → 실행. Inference-time RTC와 학습된 continuation을 구분한다.

## Evaluation Scope

다섯 실제 조작 과제에서 RTC와 비교해 동작 smoothness와 완료 시간을 평가한다. 공개 코드 링크는 Kinetix simulation 범위이며 전체 실기 경로 공개를 뜻하지 않는다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p058.html) · [저자 project](https://lyfeng001.github.io/Legato/).

## Why This Paper Is Here — Researcher Interpretation

ACT·Diffusion Policy와 RTC 이후 action interface를 이해할 NEXT다. Chunk queue나 지연으로 생긴 차이를 새로운 지시 이해/검색 효과로 혼동하지 않게 한다.

범위와 수치의 미확인 항목은 [평가 노트](./04_evaluation.md)에, 제안하는 반증 질문은 [insights](./05_insights.md)에 둔다.
