# HIQL: Offline Goal-Conditioned RL with Latent States as Actions

> Evidence maturity: `ABSTRACT_CHECKED`. abstract 기반 — 본문 수동 확인 필요.
> 자동 작성 노트는 실제 정독을 뜻하지 않는다. 사용자 reading status는 UNREAD로 시작한다.

- Year/Venue: 2023 / NeurIPS
- Category: Robot Learning and Data
- Primary track: RL, IL, offline learning, and robot data
- Tier: NEXT
- Tags: offline-RL, goal-conditioning, temporal-abstraction, value-function
- Aliases: HIQL
- Official paper: https://proceedings.neurips.cc/paper_files/paper/2023/hash/6d7c4a0727e089ed6cdd3151cbe8d8ba-Abstract-Conference.html
- Venue verification: https://proceedings.neurips.cc/paper_files/paper/2023/hash/6d7c4a0727e089ed6cdd3151cbe8d8ba-Abstract-Conference.html
- Code/Project: https://seohong.me/projects/hiql/
- Code: https://github.com/seohongpark/HIQL
- Source audit: 2026-11-12: 공식 publication/초록 또는 저자 source 확인. 공식 초록과 metadata 수준의 정리다. 구체적 실험 조건·수치·본문 한계는 추가 확인이 필요하다. 초록·지정 project 범위이며 전체 정독·코드 실행·사용자 reading 완료를 뜻하지 않는다.

## Problem and Importance

긴 목표 거리에서 가치 추정 오차가 offline goal-reaching 정책을 망가뜨린다.

## Core Idea and Contribution

하나의 action-free 가치함수에서 latent subgoal 정책과 그 목표에 도달하는 하위 정책을 추출한다.

## Observation–State–Action Interface

상태·최종 목표 → latent subgoal → 실제 행동; 공유 value에서 두 정책 학습.

## Evaluation Scope and Claim Boundary

장시간 offline goal-reaching·영상 관측·action-free data 사용을 평가한다.

근거: [공식 paper/abstract](https://proceedings.neurips.cc/paper_files/paper/2023/hash/6d7c4a0727e089ed6cdd3151cbe8d8ba-Abstract-Conference.html) · [저자 project/code](https://seohong.me/projects/hiql/) · [공식 code](https://github.com/seohongpark/HIQL). 정확한 수치·baseline fairness·failure 범위는 본문 확인 전까지 확정하지 않는다.

## Why This Paper Is Here — Researcher Interpretation

공유 가치함수와 계층 정책을 단일 actor 공동 학습과 구별하고 장기 credit 문제의 강한 대안으로 비교한다.

## Verification Boundary

본문에서 확인할 항목: goal relabeling·latent 목표 표현·subgoal 거리·action-free 데이터 범위. 이 항목들은 연구자의 점검 질문이며 논문이 보고한 실패 목록이 아니다.
