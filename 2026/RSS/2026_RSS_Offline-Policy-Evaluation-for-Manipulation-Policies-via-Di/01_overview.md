# Offline Policy Evaluation for Manipulation Policies via Discounted Liveness Formulation

> Evidence maturity: `ABSTRACT_CHECKED`. 요약과 핵심 기여 두 개는 아래에 표시한 원문 쪽수에서 확인했다. 나머지 분석은 각 절에 적힌 근거 범위를 따른다.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2026 / RSS
- Authors: Hao Wang, Joshua Bowden, Colton Crosby, Somil Bansal
- Category: World Models, Safety, and Recovery
- Primary track: World models, safety, uncertainty, and recovery
- Tier: NEXT
- Tags: offline-evaluation, truncation-bias, manipulation, value-function
- Aliases: Discounted Liveness OPE
- Official paper: https://www.roboticsproceedings.org/rss22/p154.html
- Venue verification: https://www.roboticsproceedings.org/rss22/p154.html
- Code/Project: https://github.com/haowwang/offline_policy_eval_manipulation
- Code: https://github.com/haowwang/offline_policy_eval_manipulation
- 방법·평가 확인 (2026-11-25): [원문 3, 4, 5, 6, 7, 8쪽](https://www.roboticsproceedings.org/rss22/p154.pdf#page=3) · [다축 분류와 공개 범위](../../../work/sources/batches/core_next_10.yaml)
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. RSS official abstract의 두 simulation 과제를 기록한다. arXiv 초록의 추가 cloth demonstration은 venue 본문에서 동일성을 확인하기 전 평가 범위에 합치지 않았다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다. 2026-11-23 개요의 요약과 핵심 기여 두 개를 원문 지정 쪽과 대조했다.

## Problem and Importance

이 연구는 실패와 시간 종료가 뒤섞인 유한 길이 조작 궤적으로부터 정책의 목표 달성 가능성을 오프라인에서 추정한다. [PDF 1쪽](https://www.roboticsproceedings.org/rss22/p154.pdf#page=1)

## Core Idea and Contribution

- 과제 완료 가능성을 나타내는 할인된 벨만 연산자를 정의하고 보수적인 고정점과 수축 성질을 분석해 시간 제한에 의한 편향을 다룬다. [PDF 3쪽](https://www.roboticsproceedings.org/rss22/p154.pdf#page=3) · [PDF 4쪽](https://www.roboticsproceedings.org/rss22/p154.pdf#page=4) · [PDF 5쪽](https://www.roboticsproceedings.org/rss22/p154.pdf#page=5)
- VLA·확산 정책의 시뮬레이션 조작과 실제 로봇을 조종한 사람의 천 접기 시연에서 TD 및 몬테카를로 추정과 과제 진행·중단 편향을 비교했다. [PDF 5쪽](https://www.roboticsproceedings.org/rss22/p154.pdf#page=5) · [PDF 7쪽](https://www.roboticsproceedings.org/rss22/p154.pdf#page=7) · [PDF 8쪽](https://www.roboticsproceedings.org/rss22/p154.pdf#page=8)

## Observation–State–Action Interface

정책 rollout·목표 상태 → liveness value → offline 정책 평가.

## Evaluation Scope and Claim Boundary

RSS abstract는 VLA·diffusion policy를 이용한 두 simulation 조작 과제를 명시한다.

근거: [공식 paper/abstract](https://www.roboticsproceedings.org/rss22/p154.html). 인용한 결과 외의 수치, 기준선의 비교 조건과 실패 범위는 추가 확인이 필요하다.

## Why This Paper Is Here — Researcher Interpretation

실험 rollout 종료와 실제 실패를 구별하고 가치 진단의 target을 정할 최신 기준이다.

## Verification Boundary

본문에서 확인할 항목: 고정 정책·목표 predicate·유한 horizon·복구 구간·실제 성공과 진척의 차이. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.

## 공개 자료의 확인 범위

- Square 너트 조립의 할인 가치 추정기 학습 스크립트 · square_task/train_our_method_square_task.sh [배포 파일](https://raw.githubusercontent.com/haowwang/offline_policy_eval_manipulation/45bbad6756aea9ad69176e1c44f7da2dc99c249d/square_task/train_our_method_square_task.sh)
