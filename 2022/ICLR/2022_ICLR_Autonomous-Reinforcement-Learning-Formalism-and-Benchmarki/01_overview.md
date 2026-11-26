# Autonomous Reinforcement Learning: Formalism and Benchmarking

> Evidence maturity: `FULL_TEXT_CHECKED`. 아래에 쪽수를 붙인 문장을 원문과 대조했다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2022 / ICLR
- Authors: Archit Sharma, Kelvin Xu, Nikhil Sardana, Abhishek Gupta, Karol Hausman, Sergey Levine, Chelsea Finn
- Category: Robotics Foundations: Robot Learning
- Primary track: RL, IL, offline learning, and robot data
- Tier: REFERENCE
- Tags: RL, evaluation, learning-foundation, Benchmark, reset-free learning
- Aliases: EARL
- Official paper: https://arxiv.org/abs/2112.09605
- Full-text retrieval: https://arxiv.org/pdf/2112.09605v2
- Venue verification: https://iclr.cc/Downloads/2022
- Code/Project: not identified
- Code: not_identified
- Source audit: 2026-11-24에 한 줄 요약과 핵심 기여 두 개를 아래 PDF 쪽수에 대조했다.

## Problem and Importance

EARL은 학습 중 매 시행마다 외부에서 환경을 초기화하기 어려운 상황을 정식화하고 자율 강화학습을 비교할 시뮬레이션 벤치마크를 제공한다. [PDF 1쪽](https://arxiv.org/pdf/2112.09605v2#page=1)

## Core Idea and Contribution

- 학습 중 거둔 보상과 학습 후 배포한 정책의 성능을 구분하는 평가 방식을 정의하고 과제별 재설정 조건을 기술했다. [PDF 3쪽](https://arxiv.org/pdf/2112.09605v2#page=3) · [PDF 4쪽](https://arxiv.org/pdf/2112.09605v2#page=4) · [PDF 5쪽](https://arxiv.org/pdf/2112.09605v2#page=5)
- 초기화 빈도를 바꾼 기준 강화학습 및 자율 학습 기법을 비교하고 최종 정책 성능과 방문 상태의 차이를 조사했다. [PDF 7쪽](https://arxiv.org/pdf/2112.09605v2#page=7) · [PDF 8쪽](https://arxiv.org/pdf/2112.09605v2#page=8) · [PDF 9쪽](https://arxiv.org/pdf/2112.09605v2#page=9)

## Observation–State–Action Interface

연속 환경 상호작용·개입 budget → 학습 policy → 별도 평가.

## Evaluation Scope and Claim Boundary

다양한 simulated task에서 reset 의존성과 기존 방법 한계를 분석한다.

근거: [공식 paper/abstract](https://openreview.net/forum?id=nkaba3ND7B5). 추가 수치와 실패 조건은 해당 실험의 표·설정을 확인해야 한다.

## 검색 태그 근거

EARL은 환경을 임의로 재설정할 수 있는 빈도를 제한하고 학습 중 개입과 배포 시 성능을 각각 평가한다. Sawyer 조작, DHand 파지, Minitaur 이동 등의 모의 과제가 비교 대상이다. [원문 5쪽](https://arxiv.org/pdf/2112.09605v2#page=5) · [원문 7쪽](https://arxiv.org/pdf/2112.09605v2#page=7)

## Why This Paper Is Here — Researcher Interpretation

C5의 continuing/deployed 평가와 human intervention 기준을 제공한다.

## Verification Boundary

reset 정의, intervention 비용, 평가 rollout의 학습 유입, denominator을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
