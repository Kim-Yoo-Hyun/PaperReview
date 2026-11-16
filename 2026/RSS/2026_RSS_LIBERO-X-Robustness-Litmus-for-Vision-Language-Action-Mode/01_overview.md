# LIBERO-X: Robustness Litmus for Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Category: Benchmarks and Datasets
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, Benchmark, robustness, instruction-grounding
- Aliases: LIBERO-X
- Official paper: https://roboticsproceedings.org/rss22/p097.html
- Venue verification: https://roboticsproceedings.org/rss22/p097.html
- Code/Project: https://meituan.github.io/LIBERO-X/
- Code: https://github.com/meituan/LIBERO-X
- Source audit: 2026-11-02 공식 proceedings/publisher의 서지·abstract와 저자 project/code 소개를 확인했다. 노트는 abstract/project 기반이며 본문 정독·native 실행을 뜻하지 않는다. 사용자 읽기 상태는 UNREAD 유지.

## Problem and Importance

단일 교란이나 균질한 장면만으로 평가하면 VLA의 공간·물체·지시 일반화 한계를 가릴 수 있다.

## Core Idea and Contribution

난이도별 복합 교란 평가와 장면당 여러 조작 목표를 포함하는 teleoperation 데이터를 결합한 benchmark를 제시한다.

## Observation–State–Action Interface

공간 배치·물체 속성·지시 표현을 바꾼 관측과 task → VLA 행동 → 다차원 label별 평가.

## Evaluation Scope

대표 VLA를 누적 교란 조건에서 비교한다. 공개 project는 training 2,520 demonstrations·600 tasks·100 scenes를 명시한다. 이를 test trial 수와 혼동하지 않는다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p097.html) · [저자 project](https://meituan.github.io/LIBERO-X/).

## Why This Paper Is Here — Researcher Interpretation

LIBERO·LIBERO-Plus·VLABench 이후 복합 shift와 목표 다양성을 비교할 NEXT benchmark다. 같은 scene의 다른 goal을 다루는 연구에서 기존 평가 범위를 확인하는 데 필요하다.

범위와 수치의 미확인 항목은 [평가 노트](./04_evaluation.md)에, 제안하는 반증 질문은 [insights](./05_insights.md)에 둔다.
