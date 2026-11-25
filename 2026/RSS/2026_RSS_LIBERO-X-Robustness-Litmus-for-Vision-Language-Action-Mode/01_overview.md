# LIBERO-X: Robustness Litmus for Vision-Language-Action Models

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Guodong Wang, Chenkai Zhang, Qingjie Liu, Jinjin Zhang, Jiancheng Cai, Junjie Liu, Xinmin Liu
- Category: Benchmarks and Datasets
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: VLA, Benchmark, robustness, instruction-grounding
- Aliases: LIBERO-X
- Official paper: https://roboticsproceedings.org/rss22/p097.html
- Venue verification: https://roboticsproceedings.org/rss22/p097.html
- Code/Project: https://meituan.github.io/LIBERO-X/
- Code: https://github.com/meituan/LIBERO-X
- Source audit: 2026-11-02 공식 proceedings/publisher의 서지·abstract와 저자 project/code 소개를 확인했다. 노트는 abstract/project 기반이며 본문 정독·native 실행을 뜻하지 않는다. 사용자 읽기 상태는 UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

LIBERO-X는 같은 환경에서 여러 목표를 수행하게 해 VLA가 공간 관계·물체 개념·복합 지시를 얼마나 일반화하는지 측정한다. [PDF 1쪽](https://roboticsproceedings.org/rss22/p097.pdf#page=1)

## Core Idea and Contribution

- 서로 다른 목표에 대한 사람의 원격조작 시연과 단계별 평가 과제를 구성해 같은 장면에 하나의 행동만 대응하는 편향을 줄였다. [PDF 3쪽](https://roboticsproceedings.org/rss22/p097.pdf#page=3) · [PDF 4쪽](https://roboticsproceedings.org/rss22/p097.pdf#page=4) · [PDF 5쪽](https://roboticsproceedings.org/rss22/p097.pdf#page=5)
- 시각 교란과 의미적 난도를 조절해 표준 조건과 누적 변화 조건에서 로봇 정책의 성공률을 비교했다. [PDF 7쪽](https://roboticsproceedings.org/rss22/p097.pdf#page=7) · [PDF 8쪽](https://roboticsproceedings.org/rss22/p097.pdf#page=8)

## Observation–State–Action Interface

공간 배치·물체 속성·지시 표현을 바꾼 관측과 task → VLA 행동 → 다차원 label별 평가.

## Evaluation Scope

대표 VLA를 누적 교란 조건에서 비교한다. 공개 project는 training 2,520 demonstrations·600 tasks·100 scenes를 명시한다. 이를 test trial 수와 혼동하지 않는다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p097.html) · [저자 project](https://meituan.github.io/LIBERO-X/).

## Why This Paper Is Here — Researcher Interpretation

LIBERO·LIBERO-Plus·VLABench 이후 복합 shift와 목표 다양성을 비교할 NEXT benchmark다. 같은 scene의 다른 goal을 다루는 연구에서 기존 평가 범위를 확인하는 데 필요하다.

범위와 수치의 미확인 항목은 [평가 노트](./04_evaluation.md)에, 제안하는 반증 질문은 [insights](./05_insights.md)에 둔다.

## 공개 자료

- 코드 — LIBERO-X 정책 평가 · eval_template.py [배포 파일](https://raw.githubusercontent.com/meituan/LIBERO-X/f528726421c7211d8eb05fe48e9e5e2535ccc813/eval_template.py)
- 데이터 — LIBERO-X 사람 원격조작 시뮬레이션 시연 · data/chunk-000/episode_000000.parquet [배포 파일](https://huggingface.co/datasets/meituan/LIBERO-X/resolve/6ad3cebe79e25dea1102838633e4938608c7c1c8/data/chunk-000/episode_000000.parquet)
