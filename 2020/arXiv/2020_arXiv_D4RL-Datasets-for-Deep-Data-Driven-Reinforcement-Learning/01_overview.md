# D4RL: Datasets for Deep Data-Driven Reinforcement Learning

> Evidence maturity: `FULL_TEXT_CHECKED`. 요약과 기여를 아래 쪽수에서 확인했다.

- Year/Venue: 2020 / arXiv
- Authors: Justin Fu, Aviral Kumar, Ofir Nachum, George Tucker, Sergey Levine
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: offline-RL, Benchmark, robot-data, distribution-shift
- Aliases: D4RL
- Official paper: https://arxiv.org/abs/2004.07219
- Venue verification: https://arxiv.org/abs/2004.07219
- Code/Project: https://github.com/Farama-Foundation/D4RL
- Code: https://github.com/Farama-Foundation/D4RL
- Full-text retrieval: https://arxiv.org/pdf/2004.07219v4
- Source audit: 2026-11-24에 요약과 핵심 기여 두 개를 원문과 대조했다.

## Problem and Importance

D4RL은 고정된 자료로 학습하는 오프라인 강화학습을 위해 서로 다른 행동 정책과 수집 방식에서 나온 자료 및 공통 평가 절차를 제공한다. [PDF 1쪽](https://arxiv.org/pdf/2004.07219v4#page=1) · [PDF 3쪽](https://arxiv.org/pdf/2004.07219v4#page=3)

## Core Idea and Contribution

- 혼합 정책, 사람 시연, 목표 지향 제어기에서 얻은 자료로 부분 궤적의 조합과 학습 자료에 드문 행동 등 오프라인 학습의 난점을 설계했다. [PDF 3쪽](https://arxiv.org/pdf/2004.07219v4#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2004.07219v4#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2004.07219v4#page=5) · [PDF 6쪽](https://arxiv.org/pdf/2004.07219v4#page=6)
- 여러 알고리즘의 성과를 환경별 기준점에 대한 정규화 점수로 비교해, 수집 방식에 따라 성능이 어떻게 달라지는지 보고했다. [PDF 7쪽](https://arxiv.org/pdf/2004.07219v4#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2004.07219v4#page=8) · [PDF 15쪽](https://arxiv.org/pdf/2004.07219v4#page=15)

## Observation–State–Action Interface

고정 transition dataset → offline 정책 학습 → 환경별 평가.

## Evaluation Scope and Claim Boundary

다양한 데이터 수집 조건에서 offline 알고리즘을 비교한다. 데이터셋 전체가 실물 로봇 trajectory라는 뜻은 아니다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2004.07219) · [저자 project/code](https://github.com/Farama-Foundation/D4RL).

## Why This Paper Is Here — Researcher Interpretation

CQL·IQL·Cal-QL의 데이터 조건과 결과를 읽기 위한 표준 benchmark의 누락을 보완한다.

## Verification Boundary

본문에서 확인할 항목: dataset version·terminal/timeout·normalized score·현행 API와 원본 데이터 호환. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
