# RoboReward: General-Purpose Vision-Language Reward Models for Robotics

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / arXiv
- Authors: Tony Lee, Andrew Wagenmaker, Karl Pertsch, Percy Liang, Sergey Levine, Chelsea Finn
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: reward-learning, robot-learning, evaluation
- Aliases:
- Official paper: https://arxiv.org/abs/2601.00675
- Venue verification: https://arxiv.org/abs/2601.00675
- Code/Project: https://crfm.stanford.edu/helm/robo-reward-bench/
- Code: not_identified
- Source audit: 2026-10-22 공식 abstract/arXiv abstract와 publication metadata 확인. 새 5개 note는 abstract 수준의 분석이며 상세 본문·코드 감사는 기존 buildup dossier의 명시 범위만 따른다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.
- Metadata refresh: 2026-10-25 arXiv v2와 저자가 연결한 HELM project URL 확인. 목적지 HTML은 client-rendered shell이며 code/data/checkpoint 공개 범위는 검증하지 않았다. OpenReview challenge로 정식 acceptance를 확인하지 못해 arXiv 유지.

## Problem and Importance

RoboReward는 실제 조작 영상과 지시로부터 진행·성공 정도를 판단하는 보상 데이터셋과 시각언어 보상 모델을 제시한다. [PDF 1쪽](https://arxiv.org/pdf/2601.00675v2#page=1)

## Core Idea and Contribution

- 성공 영상의 지시를 바꾸거나 궤적을 중간에 잘라 실패와 부분 진척 예시를 만들어 성공 편향을 줄였다. [PDF 4쪽](https://arxiv.org/pdf/2601.00675v2#page=4) · [PDF 6쪽](https://arxiv.org/pdf/2601.00675v2#page=6)
- 보상 판정 정확도와 실제 로봇 강화학습의 결과를 따로 시험하고 학습한 보상, 범용 VLM 보상, 사람 보상을 비교했다. [PDF 1쪽](https://arxiv.org/pdf/2601.00675v2#page=1) · [PDF 8쪽](https://arxiv.org/pdf/2601.00675v2#page=8)

## Observation–State–Action Interface

지시·trajectory → task completion reward.

## Evaluation Scope and Claim Boundary

공개 robot 자료의 reward 평가와 실제 robot RL을 보고한다.

근거: [공식 paper/abstract](https://arxiv.org/abs/2601.00675). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

C4의 독립 outcome과 reward model 차이를 정할 직접 기준이다.

## Verification Boundary

counterfactual label 검증, temporal clipping, policy shift, benchmark leakage을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
