# RoboArena: Distributed Real-World Evaluation of Generalist Robot Policies

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2025 / CoRL
- Authors: Pranav Atreya, Karl Pertsch, Tony Lee, Moo Jin Kim, Arhan Jain, Artur Kuramshin, Clemens Eppner, Cyrus Neary, Edward Hu, Fabio Ramos, Jonathan Tremblay, Kanav Arora, Kirsty Ellis, Luca Macesanu, Matthew Leonard, Meedeum Cho, Ozgur Aslan, Shivin Dass, Jie Wang, Xingfang Yuan, Xuning Yang, Abhishek Gupta, Dinesh Jayaraman, Glen Berseth, Kostas Daniilidis, Roberto Martin-Martin, Youngwoon Lee, Percy Liang, Chelsea Finn, Sergey Levine
- Category: VLA and Generalist Robot Policies
- Primary track: VLA and generalist robot policies
- Tier: NEXT
- Tags: Robotics, Benchmark, real-robot, pairwise-evaluation
- Aliases: RoboArena
- Official paper: https://proceedings.mlr.press/v305/atreya25a.html
- Venue verification: https://proceedings.mlr.press/v305/atreya25a.html
- Code/Project: https://robo-arena.github.io/
- Code: https://github.com/pranavatreya/roboarena_backend
- Source audit: 2026-10-25 공식 abstract/서지정보 및 명시된 저자 링크 확인. 이번 노트는 abstract 기반이며 본문 전체·코드 실행·payload는 미검증이다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

RoboArena는 여러 기관이 각자의 로봇 환경에서 같은 두 정책을 비교해 범용 조작 정책의 상대 성능을 추정한다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/atreya25a/atreya25a.pdf#page=1)

## Core Idea and Contribution

- 각 비교에서는 환경과 지시를 맞추고 정책의 신원을 가린 채 두 실행에 대한 선호를 수집해 전체 순위를 추정한다. [PDF 3쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/atreya25a/atreya25a.pdf#page=3) · [PDF 4쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/atreya25a/atreya25a.pdf#page=4) · [PDF 5쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/atreya25a/atreya25a.pdf#page=5)
- 서로 다른 실제 환경에서 수집한 쌍대 비교로 일곱 정책을 평가하고 평가자와 작업에 따른 순위의 변동을 분석했다. [PDF 1쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/atreya25a/atreya25a.pdf#page=1) · [PDF 6쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/atreya25a/atreya25a.pdf#page=6) · [PDF 7쪽](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/atreya25a/atreya25a.pdf#page=7)

## Observation–State–Action Interface

같은 평가 상황의 두 정책 rollout → 선호 비교 → 전체 정책 순위.

## Evaluation Scope and Claim Boundary

DROID 플랫폼을 사용하는 여러 기관에서 generalist policy를 실로봇으로 비교한다.

근거: [공식 paper/abstract](https://proceedings.mlr.press/v305/atreya25a.html) · [저자 project/code](https://robo-arena.github.io/) · [공식 code](https://github.com/pranavatreya/roboarena_backend). 문장에 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

LIBERO-Plus·THE COLOSSEUM의 고정 benchmark와 구별되는 실환경 평가 기준을 보완한다.

## Verification Boundary

pairwise reset 조건, task 선택 편향, 선호 aggregation과 불확실성을 확인해야 한다. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 원문 대조

저자 표기와 순서는 이 판본의 표제면을 따른다. [표제면](https://raw.githubusercontent.com/mlresearch/v305/d42e9e994b3821cca9121500c717f9a87c7cb4f6/assets/atreya25a/atreya25a.pdf#page=1)

## 공개 자료

- 코드 — 실제 정책 대조 평가용 중앙 서버 · central_server/central_server.py [배포 파일](https://raw.githubusercontent.com/pranavatreya/roboarena_backend/ca7b8116c68c2f75313441d751ccfae7d9daacb3/central_server/central_server.py)
- 데이터 — 평가 정책별 집계 결과 · output/policy_analysis.json [배포 파일](https://raw.githubusercontent.com/pranavatreya/roboarena_backend/ca7b8116c68c2f75313441d751ccfae7d9daacb3/output/policy_analysis.json)
