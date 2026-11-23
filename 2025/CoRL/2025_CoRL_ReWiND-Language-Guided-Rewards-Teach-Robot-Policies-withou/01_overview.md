# ReWiND: Language-Guided Rewards Teach Robot Policies without New Demonstrations

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / CoRL
- Authors: Jiahui Zhang, Yusen Luo, Abrar Anwar, Sumedh Anand Sontakke, Joseph J Lim, Jesse Thomason, Erdem Biyik, Jesse Zhang
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: language-conditioned-reward, offline-to-online-RL, manipulation
- Aliases: ReWiND
- Official paper: https://proceedings.mlr.press/v305/zhang25a.html
- Venue verification: https://proceedings.mlr.press/v305/zhang25a.html
- Code/Project: https://rewind-reward.github.io/
- Code: https://github.com/rewind-reward/ReWiND
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인. 새 과제별 추가 시연이 없다는 주장과 사전학습에 사용한 Open-X 및 초기 시연을 구별한다. 본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

ReWiND는 기존 시연으로 언어 조건부 보상과 조작 정책을 학습한 뒤 새로운 과제 변형에서 추가 시연 없이 온라인 적응한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/zhang25a/zhang25a.pdf#page=1)

## Core Idea and Contribution

- 언어에 조건화된 보상 모델로 시연 자료에 보상을 붙이고 이를 사용해 정책을 오프라인 강화학습으로 사전학습한다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/zhang25a/zhang25a.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/zhang25a/zhang25a.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/zhang25a/zhang25a.pdf#page=5)
- 시뮬레이션과 실제 Koch 양팔 로봇에서 보상 모델의 미관측 과제 일반화와 그 보상을 이용한 정책 적응을 구분해 평가했다. [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/zhang25a/zhang25a.pdf#page=7) · [PDF 8쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/zhang25a/zhang25a.pdf#page=8) · [PDF 9쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/zhang25a/zhang25a.pdf#page=9)

## Observation–State–Action Interface

영상·지시 → 학습 보상 → offline pretraining·online policy update.

## Evaluation Scope and Claim Boundary

Simulation과 실제 양팔 조작의 미관측 과제 적응을 평가한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/zhang25a.html) · [저자 project/code](https://rewind-reward.github.io/) · [공식 code](https://github.com/rewind-reward/ReWiND). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

새 VLA-RL 보상이나 실패 재사용이 기존 언어 보상 일반화와 어떻게 다른지 비교할 선행이다.

## Verification Boundary

사전학습 시연·외부 데이터 사용량, reward leakage, 신규 과제별 인간 감독을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
