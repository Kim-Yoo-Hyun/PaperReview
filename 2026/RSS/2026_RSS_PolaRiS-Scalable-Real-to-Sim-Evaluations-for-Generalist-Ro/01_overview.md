# PolaRiS: Scalable Real-to-Sim Evaluations for Generalist Robot Policies

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Arhan Jain, Mingtong Zhang, Kanav Arora, William Chen, Marcel Torne, Muhammad Zubair Irshad, Sergey Zakharov, Yue Wang, Sergey Levine, Chelsea Finn, Wei-Chiu Ma, Dhruv Shah, Abhishek Gupta, Karl Pertsch
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: policy-evaluation, real-to-sim, Gaussian Splatting
- Aliases: PolaRiS
- Official paper: https://roboticsproceedings.org/rss22/p062.html
- Venue verification: https://roboticsproceedings.org/rss22/p062.html
- Code/Project: https://polaris-evals.github.io/
- Code: https://github.com/arhanjain/PolaRiS
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인.  본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

PolaRiS는 실제 장면을 찍은 짧은 영상으로 시뮬레이션을 만들고 그곳에서 얻은 정책 순위가 같은 실물 조건에서의 순위와 일치하는지 검증한다. [PDF 1쪽](https://roboticsproceedings.org/rss22/p062.pdf#page=1)

## Core Idea and Contribution

- 신경 장면 재구성으로 상호작용 가능한 장면을 만들고 정책이 시뮬레이션 자료를 함께 학습하도록 해 실물에서 훈련된 정책의 상대 성능을 예측한다. [PDF 4쪽](https://roboticsproceedings.org/rss22/p062.pdf#page=4) · [PDF 5쪽](https://roboticsproceedings.org/rss22/p062.pdf#page=5)
- 여러 정책의 실물·시뮬레이션 실행을 짝지어 비교하고 재구성한 환경의 순위 예측력을 기존 시뮬레이션 벤치마크와 대조했다. [PDF 6쪽](https://roboticsproceedings.org/rss22/p062.pdf#page=6) · [PDF 7쪽](https://roboticsproceedings.org/rss22/p062.pdf#page=7) · [PDF 8쪽](https://roboticsproceedings.org/rss22/p062.pdf#page=8)

## Observation–State–Action Interface

실환경 영상 → 재구성 환경 → generalist 정책 평가.

## Evaluation Scope and Claim Boundary

실제·시뮬레이션의 짝지은 rollout으로 정책 순위 상관을 평가한다.

근거: [공식 paper/abstract](https://roboticsproceedings.org/rss22/p062.html) · [저자 project/code](https://polaris-evals.github.io/) · [공식 code](https://github.com/arhanjain/PolaRiS). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

SIMPLER·RoboCasa의 점수를 실제 개선으로 해석하기 전 필요한 평가 타당성 비교다.

## Verification Boundary

평가 전에 허용된 co-training 데이터, 독립 실환경 trial, 장면 선택 편향을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료

- 코드 — 재구성한 장면에서 로봇 정책 평가 · src/polaris/environments/manager_based_rl_splat_environment.py [배포 파일](https://raw.githubusercontent.com/arhanjain/PolaRiS/129abc45f680559a7da62b9280fdb127b02b7275/src/polaris/environments/manager_based_rl_splat_environment.py)
- 데이터 — 블록 쌓기 평가 장면의 재구성된 가우시안 · block_stack_kitchen/assets/g60_kitchen_table_zed/splat.ply [배포 파일](https://huggingface.co/datasets/owhan/PolaRiS-Hub/resolve/8c7e4103e266ef83d8b1ad2e9a63116edd5f155b/block_stack_kitchen/assets/g60_kitchen_table_zed/splat.ply)
