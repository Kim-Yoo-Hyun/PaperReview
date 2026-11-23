# ReWiND: Language-Guided Rewards Teach Robot Policies without New Demonstrations

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
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
- Source audit: 2026-11-07–08: official metadata/abstract 및 저자 project/repository 공개 범위 확인. 새 과제별 추가 시연이 없다는 주장과 사전학습에 사용한 Open-X 및 초기 시연을 구별한다. 본문 전체 정독·코드 실행·독립 성능 검증 아님. 사용자 reading status UNREAD 유지.

## Problem and Importance

새 언어 과제마다 보상 설계나 시연을 다시 확보하는 비용이 크다.

## Core Idea and Contribution

소규모 시연으로 언어 조건부 reward와 offline 정책을 학습하고 새 과제에 online 적응한다.

## Observation–State–Action Interface

영상·지시 → 학습 보상 → offline pretraining·online policy update.

## Evaluation Scope and Claim Boundary

Simulation과 실제 양팔 조작의 미관측 과제 적응을 평가한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/zhang25a.html) · [저자 project/code](https://rewind-reward.github.io/) · [공식 code](https://github.com/rewind-reward/ReWiND). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

새 VLA-RL 보상이나 실패 재사용이 기존 언어 보상 일반화와 어떻게 다른지 비교할 선행이다.

## Verification Boundary

사전학습 시연·외부 데이터 사용량, reward leakage, 신규 과제별 인간 감독을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
